import json

def handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON format"})
        }

    required = ["name", "email", "phone", "resume_url", "job_id"]
    missing = [field for field in required if not body.get(field)]

    if missing:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Missing required fields",
                "fields": missing
            })
        }

    # MOCK Zoho Candidate Creation
    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Candidate created and attached to job",
            "candidate_id": "cand_123",
            "application_status": "APPLIED",
            "job_id": body["job_id"]
        })
    }
