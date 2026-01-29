import json

def handler(event, context):
    params = event.get("queryStringParameters") or {}
    job_id = params.get("job_id")

    if not job_id:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "job_id query parameter is required"
            })
        }

    # Mock applications
    applications = [
        {
            "id": "app_001",
            "candidate_name": "Sai",
            "email": "sai@example.com",
            "status": "APPLIED"
        }
    ]

    return {
        "statusCode": 200,
        "body": json.dumps(applications)
    }
