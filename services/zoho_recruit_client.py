import os
import requests

ZOHO_RECRUIT_BASE_URL = "https://www.zohoapis.in/recruit/v2"
ZOHO_ACCESS_TOKEN = os.environ.get("ZOHO_ACCESS_TOKEN")


def get_headers():
    if not ZOHO_ACCESS_TOKEN:
        raise Exception("ZOHO_ACCESS_TOKEN not set")

    return {
        "Authorization": f"Zoho-oauthtoken {ZOHO_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }


def _is_html_response(response):
    return "text/html" in response.headers.get("Content-Type", "")


def zoho_get(endpoint, params=None):
    url = f"{ZOHO_RECRUIT_BASE_URL}/{endpoint}"
    print(f"[Zoho GET] {url}")

    response = requests.get(
        url,
        headers=get_headers(),
        params=params,
        timeout=10
    )

    # 🔴 Zoho trial restriction detection
    if _is_html_response(response):
        raise Exception("ZOHO_API_DISABLED")

    if response.status_code != 200:
        raise Exception(f"Zoho error {response.status_code}: {response.text}")

    return response.json()


def zoho_post(endpoint, payload):
    url = f"{ZOHO_RECRUIT_BASE_URL}/{endpoint}"
    print(f"[Zoho POST] {url}")

    response = requests.post(
        url,
        headers=get_headers(),
        json=payload,
        timeout=10
    )

    if _is_html_response(response):
        raise Exception("ZOHO_API_DISABLED")

    if response.status_code not in (200, 201):
        raise Exception(f"Zoho error {response.status_code}: {response.text}")

    return response.json()
