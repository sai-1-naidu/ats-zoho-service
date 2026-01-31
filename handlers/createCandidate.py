import json
import base64
from services.application_store import add_application

def handler(event, context):
    body = event.get("body")

    if body and event.get("isBase64Encoded"):
        body = base64.b64decode(body).decode("utf-8")

    data = json.loads(body) if body else {}

    application = {
        "candidate_name": data.get("name"),
        "email": data.get("email"),
        "job_id": data.get("job_id"),
        "status": "Applied"
    }

    add_application(application)

    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Candidate applied successfully",
            "application": application
        })
    }
