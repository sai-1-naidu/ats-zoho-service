import json

def handler(event, context):
    params = event.get("queryStringParameters") or {}

    page = int(params.get("page", 1))
    per_page = int(params.get("per_page", 10))

    # MOCK DATA (Paginated)
    all_jobs = [
        {
            "id": f"job_{i}",
            "title": f"Python Intern {i}",
            "location": "Remote",
            "status": "OPEN",
            "external_url": ""
        }
        for i in range(1, 51)
    ]

    start = (page - 1) * per_page
    end = start + per_page
    paginated_jobs = all_jobs[start:end]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "page": page,
            "per_page": per_page,
            "total": len(all_jobs),
            "jobs": paginated_jobs
        })
    }
