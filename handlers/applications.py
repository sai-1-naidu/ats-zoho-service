import json
from services.zoho_recruit_client import zoho_get

def handler(event, context):
    params = event.get("queryStringParameters") or {}

    page = int(params.get("page", 1))
    limit = int(params.get("limit", 10))

    try:
        data = zoho_get(
            "Candidates",
            params={
                "page": page,
                "per_page": limit
            }
        )

        applications = []
        for record in data.get("data", []):
            applications.append({
                "id": record.get("id"),
                "candidate_name": record.get("Full_Name"),
                "email": record.get("Email"),
                "status": record.get("Candidate_Status", "APPLIED")
            })

        return {
            "statusCode": 200,
            "body": json.dumps({
                "page": page,
                "limit": limit,
                "count": len(applications),
                "applications": applications
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
