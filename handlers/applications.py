import json

def handler(event, context):
    params = event.get("queryStringParameters") or {}

    job_id = params.get("job_id")
    page = int(params.get("page", 1))
    per_page = int(params.get("per_page", 10))

    if not job_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "job_id query parameter is required"})
        }

    all_applications = [
        {
            "id": f"app_{i}",
            "candidate_name": f"Candidate {i}",
            "email": f"user{i}@example.com",
            "status": "APPLIED"
        }
        for i in range(1, 41)
    ]

    start = (page - 1) * per_page
    end = start + per_page

    return {
        "statusCode": 200,
        "body": json.dumps({
            "job_id": job_id,
            "page": page,
            "per_page": per_page,
            "total": len(all_applications),
            "applications": all_applications[start:end]
        })
    }
