import google.generativeai as genai
from .prompts import NEXUS_SYSTEM_PROMPT
from .config import MODEL_NAME
import json

class NexusController:
    def __init__(self, api_key):
        self.api_key = api_key
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(MODEL_NAME, system_instruction=NEXUS_SYSTEM_PROMPT)
        else:
            self.model = None

    def analyze_input(self, input_data, input_type):
        if not self.model:
            return "Error: API Key missing."
        
        prompt = f"INPUT TYPE: {input_type}\nINPUT DATA: {input_data}\n\nDECIDE STRATEGY."
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Nexus Error: {str(e)}"

    def verify_intelligence(self, target_query, intel_summary):
        if not self.model:
            return False

        prompt = f"""
        VERIFICATION PROTOCOL:
        Target Query: "{target_query}"
         gathered Intelligence:
        {intel_summary}

        TASK: Determine if the gathered intelligence refers to the entity specified in the target query.
        Be strict. 
        1. IF the target has a common name (e.g. "Konsol Oyun"), CHECK if the gathered data matches the SPECIFIC requested entity (e.g. Taner Işıldak vs Murat Sönmez).
        2. IF the user provided a URL, the gathered intel MUST match the content of that URL.
        3. IF the names conflict (e.g. Target is "Konsol Oyun" but intel is about "Murat Engin"), return FALSE immediately.

        Example:
        Target: "Konsol Oyun" (User means the YouTuber Taner Işıldak)
        Intel: "Konsol Oyun" is a channel by Murat Sönmez.
        Result: FALSE (Entity Mismatch).

        Output only JSON: {{"match": true/false, "reason": "..."}}
        """
        try:
            response = self.model.generate_content(
                prompt, 
                generation_config={"response_mime_type": "application/json"}
            )
            result = json.loads(response.text)
            return result
        except Exception as e:
            return {"match": False, "reason": f"Verification Error: {str(e)}"}
