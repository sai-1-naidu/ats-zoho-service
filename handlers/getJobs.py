import json
from services.zoho_service import fetch_jobs

def handler(event, context):
    try:
        jobs = fetch_jobs()
        return {
            "statusCode": 200,
            "body": json.dumps({
                "source": "Zoho People",
                "count": len(jobs),
                "jobs": jobs
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
