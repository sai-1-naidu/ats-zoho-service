import json
from services.application_store import get_applications

def handler(event, context):
    params = event.get("queryStringParameters") or {}

    page = int(params.get("page", 1))
    limit = int(params.get("limit", 10))

    if page < 1 or limit < 1:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "page and limit must be positive integers"
            })
        }

    offset = (page - 1) * limit

    applications, total_count = get_applications(offset=offset, limit=limit)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "page": page,
            "limit": limit,
            "count": len(applications),
            "total": total_count,
            "applications": applications
        })
    }
