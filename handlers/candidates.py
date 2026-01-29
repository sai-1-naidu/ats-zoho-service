import json

def handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON"})
        }

    required_fields = ["name", "email", "phone", "resume_url", "job_id"]
    missing = [f for f in required_fields if not body.get(f)]

    if missing:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Missing required fields",
                "fields": missing
            })
        }

    # Mock candidate creation
    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Candidate created successfully",
            "candidate_id": "cand_001",
            "job_id": body["job_id"]
        })
    }
