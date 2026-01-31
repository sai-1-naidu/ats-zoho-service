import os

def get_access_token():
    token = os.getenv("ZOHO_ACCESS_TOKEN")
    if not token:
        raise Exception("Access token not found")
    return token
