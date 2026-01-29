import json

def handler(event, context):
    jobs = [
        {
            "id": "job_001",
            "title": "Python Backend Intern",
            "location": "Remote",
            "status": "OPEN",
            "external_url": ""
        }
    ]

    return {
        "statusCode": 200,
        "body": json.dumps(jobs)
    }
