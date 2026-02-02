import json
from services.zoho_recruit_client import zoho_post

def handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON"})
        }

    required = ["name", "email", "phone"]
    missing = [f for f in required if not body.get(f)]

    if missing:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Missing required fields",
                "fields": missing
            })
        }

    payload = {
        "data": [{
            "Full_Name": body["name"],
            "Email": body["email"],
            "Mobile": body["phone"]
        }]
    }

    try:
        zoho_post("Candidates", payload)

        return {
            "statusCode": 201,
            "body": json.dumps({
                "message": "Candidate created successfully in Zoho Recruit"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
