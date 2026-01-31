import json
from services.application_store import get_applications

def handler(event, context):
    applications = get_applications()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "count": len(applications),
            "applications": applications
        })
    }
