import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class PrivacyPreservingAgent:
    def __init__(self):
        self.url = f"{os.getenv('URL')}/v1/detect/deidentify/string"
        self.headers = {
            "X-SKYFLOW-ACCOUNT-ID": os.getenv('SKYFLOW_ACCOUNT_ID'),
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}"
        }
        self.payload_template = {
            "entity_types": ["all"],
            "token_type": {"default": "vault_token"},
            "vault_id": os.getenv('VAULT_ID')
        }

    def deidentify_text(self, text: str) -> str:
        payload = self.payload_template.copy()
        payload["text"] = text
        response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            result = response.json()
            processed_text = result.get("processed_text", "")
            print(processed_text)
            return processed_text
        else:
            return f"API Error: {response.status_code} - {response.text}"
