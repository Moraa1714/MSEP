import google.generativeai as genai
import json
from .prompts import GHOST_COMPOSITOR_SYSTEM_PROMPT
from .config import MODEL_NAME

class GhostCompositor:
    def __init__(self, api_key):
        self.api_key = api_key
        
        self.current_profile = {
            "full_name": "UNKNOWN",
            "aliases": [],
            "demographics": {},
            "contact_info": {},
            "psych_profile": {"traits": [], "motivations": [], "vulnerabilities": []},
            "digital_footprint": {"platforms": [], "usernames": []},
            "narrative_bio": "No data available."
        }

        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(MODEL_NAME, system_instruction=GHOST_COMPOSITOR_SYSTEM_PROMPT)
        else:
            self.model = None

    def update_profile(self, new_intel):
        if not self.model:
            return {"error": "API Key missing."}
        
        prompt = f"""
        CURRENT PROFILE:
        {json.dumps(self.current_profile)}

        NEW INTELLIGENCE:
        {new_intel}
        """

        try:
            response = self.model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            updated_data = json.loads(response.text)
            self.current_profile = updated_data
            return updated_data
        except Exception as e:
            return {"error": f"Profile Update Failed: {str(e)}"}

    def get_profile(self):
        return self.current_profile
