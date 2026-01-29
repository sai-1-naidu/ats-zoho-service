import os
import requests

ZOHO_BASE_URL = os.getenv("ZOHO_BASE_URL")
ZOHO_ACCESS_TOKEN = os.getenv("ZOHO_ACCESS_TOKEN")

HEADERS = {
    "Authorization": f"Zoho-oauthtoken {ZOHO_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def zoho_get(endpoint, params=None):
    try:
        response = requests.get(
            f"{ZOHO_BASE_URL}{endpoint}",
            headers=HEADERS,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Zoho API Error: {str(e)}")
