import json
from services.zoho_recruit_client import zoho_get

def handler(event, context):
    try:
        data = zoho_get("JobOpenings")

        jobs = []
        for job in data.get("data", []):
            jobs.append({
                "id": job.get("id"),
                "title": job.get("Job_Opening_Name"),
                "location": job.get("City"),
                "status": job.get("Job_Opening_Status"),
                "external_url": job.get("Career_Page_URL", "")
            })

        return {
            "statusCode": 200,
            "body": json.dumps(jobs)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
