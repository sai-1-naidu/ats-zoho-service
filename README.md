ATS Integration Microservice (Zoho People)

This project is a serverless ATS (Applicant Tracking System) integration microservice built using Python and the Serverless Framework.

ATS Used

Zoho People

Zoho People was chosen due to reliable API documentation and OAuth support.
During development, Zoho access tokens were short-lived and rate-limited, so mock responses are used for demo purposes while maintaining real integration logic.

Features

GET /jobs – List open jobs

POST /candidates – Create a candidate and attach to a job

GET /applications?job_id=... – List applications for a given job

Tech Stack

Python 3.9

Serverless Framework

AWS Lambda (local via serverless-offline)

Zoho People (ATS)

Project Structure

ats-zoho-service/

handlers/

jobs.py

candidates.py

applications.py

serverless.yml

requirements.txt

README.md

Setup Instructions
1. Install Dependencies

npm install -g serverless@3
pip install -r requirements.txt

2. Set Environment Variable

export ZOHO_ACCESS_TOKEN=your_access_token_here

3. Run Locally

serverless offline

Server will start at:
http://localhost:3000

API Usage
GET /jobs

curl http://localhost:3000/jobs

POST /candidates

curl -X POST http://localhost:3000/candidates

-H "Content-Type: application/json"
-d '{
"name": "Sai",
"email": "sai@example.com
",
"phone": "9999999999",
"resume_url": "https://example.com/resume.pdf
",
"job_id": "job_001"
}'

GET /applications

curl http://localhost:3000/applications?job_id=job_001

Notes

Zoho OAuth access tokens are short-lived.

Mock responses are used for consistent demo behavior.

Integration logic can easily be switched to live Zoho APIs.

Author

Tungala Lakshmi Venkata Sai