import requests
from utlis.token_manager import get_access_token

ZOHO_JOBS_URL = (
    "https://people.zoho.in/people/api/forms/"
    "job_openings/getRecords"
)

def fetch_jobs():
    access_token = get_access_token()

    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}"
    }

    response = requests.get(ZOHO_JOBS_URL, headers=headers, timeout=10)

    if response.status_code == 401:
        raise Exception("Unauthorized: Access token expired or invalid")

    if response.status_code != 200:
        raise Exception(f"Zoho API error: {response.text}")

    data = response.json()

    if data.get("response", {}).get("status") != 0:
        raise Exception("Zoho returned failure response")

    jobs = []

    for item in data["response"]["result"]:
        for record_id, records in item.items():
            job = records[0]
            jobs.append({
                "job_id": record_id,
                "title": job.get("Job_Tite"),
                "status": job.get("Status"),
                "location": job.get("Location")
            })

    return jobs
