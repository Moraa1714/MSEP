import requests
from bs4 import BeautifulSoup
import re
import warnings
import io
import pandas as pd
from pypdf import PdfReader

# Suppress HTTPS warnings for scraping
warnings.filterwarnings("ignore")

class WebWalker:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        from .config import SCRAPING_API_KEY
        self.scraping_api_key = SCRAPING_API_KEY

    def scrape_url(self, url):
        try:
            if not url.startswith("http"):
                return "Invalid URL"

            response = None
            
            if self.scraping_api_key:
                try:
                    proxy_url = "https://api.zenrows.com/v1/"
                    params = {
                        "apikey": self.scraping_api_key,
                        "url": url,
                        "js_render": "true", 
                        "premium_proxy": "true" 
                    }
                    response = requests.get(proxy_url, params=params, timeout=30)
                    response.raise_for_status()
                except Exception as api_error:
                     return f"Premium API (ZenRows) Failed: {api_error}. Falling back to standard."
            
            if not response:
                try:
                    response = requests.get(url, headers=self.headers, timeout=15, verify=False)
                    response.raise_for_status()
                except Exception as e:
                    raise e

            content_type = response.headers.get('Content-Type', '').lower()
            metadata_report = ""
            if 'application/pdf' in content_type:
                text, metadata = self._parse_pdf(response.content)
                metadata_report = self._format_metadata(metadata, "PDF DOCUMENT")
                return f"{metadata_report}\n\n[CONTENT START]\n{text}"
            elif 'excel' in content_type or 'spreadsheet' in content_type:
                return self._parse_spreadsheet(response.content, url)
            elif content_type.startswith('image/') or any(x in url.lower() for x in ['.jpg', '.jpeg', '.png', '.tiff']):
                metadata = self._parse_image(response.content)
                return self._format_metadata(metadata, "IMAGE FILE")
            else:
                return self._parse_html(response.text)
            
        except Exception as e:
            return f"Scraping Failed: {str(e)}"

    def _format_metadata(self, metadata, source_type):
        if not metadata:
            return f"[{source_type} METADATA]: None found."
        
        report = f"[{source_type} FORENSIC DATA]\n"
        for key, value in metadata.items():
            if value:
                report += f"  > {key.upper()}: {value}\n"
        return report + "----------------------------------------"

    def _parse_pdf(self, content):
        try:
            reader = PdfReader(io.BytesIO(content))
            meta = reader.metadata
            metadata = {}
            if meta:
                metadata = {
                    "author": meta.get('/Author'),
                    "creator": meta.get('/Creator'),
                    "producer": meta.get('/Producer'),
                    "creation_date": meta.get('/CreationDate'),
                    "mod_date": meta.get('/ModDate')
                }

            text = ""
            for page in reader.pages[:10]:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            return text[:4000], metadata
        except Exception as e:
            return f"PDF Parse Error: {e}", {}

    def _parse_image(self, content):
        try:
            from PIL import Image, ExifTags
            from PIL.ExifTags import TAGS, GPSTAGS
            
            img = Image.open(io.BytesIO(content))
            exif_data = {}
            
            if hasattr(img, '_getexif') and img._getexif():
                exif = img._getexif()
                for tag, value in exif.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name in ['Make', 'Model', 'DateTime', 'Software', 'Artist', 'Copyright', 'UserComment']:
                        exif_data[tag_name] = str(value)
                    if tag_name == 'GPSInfo':
                        gps_data = {}
                        for t in value:
                            sub_tag = GPSTAGS.get(t, t)
                            gps_data[sub_tag] = value[t]
                        
                        lat, lon = self._get_lat_lon(gps_data)
                        if lat and lon:
                            exif_data['GPS_COORDINATES'] = f"{lat}, {lon}"
                            exif_data['GOOGLE_MAPS_LINK'] = f"https://www.google.com/maps?q={lat},{lon}"
            
            return exif_data
        except Exception as e:
            return {"Error": f"Image Parse Error: {e}"}

    def _get_lat_lon(self, gps_info):
        try:
            def convert_to_degrees(value):
                d = float(value[0])
                m = float(value[1])
                s = float(value[2])
                return d + (m / 60.0) + (s / 3600.0)

            lat = convert_to_degrees(gps_info.get('GPSLatitude'))
            if gps_info.get('GPSLatitudeRef') != 'N': lat = -lat
            
            lon = convert_to_degrees(gps_info.get('GPSLongitude'))
            if gps_info.get('GPSLongitudeRef') != 'E': lon = -lon
            
            return lat, lon
        except:
            return None, None


    def _parse_spreadsheet(self, content, url):
        try:
            if url.endswith('.csv'):
                df = pd.read_csv(io.BytesIO(content))
            else:
                df = pd.read_excel(io.BytesIO(content))
            return f"[SPREADSHEET DATA]:\n{df.to_string()[:4000]}"
        except Exception as e:
            return f"Excel Parse Error: {e}"

    def _parse_html(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.extract()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text[:4000]

    def check_archive(self, url):
        archive_api = f"http://archive.org/wayback/available?url={url}"
        try:
            resp = requests.get(archive_api)
            data = resp.json()
            if data.get('archived_snapshots'):
                return data['archived_snapshots']['closest']['url']
            return None
        except:
            return None
