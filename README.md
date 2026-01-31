ATS Integration Microservice (Zoho People)

This project is a serverless ATS (Applicant Tracking System) integration microservice built using Python and the Serverless Framework.
It exposes a unified REST API for jobs, candidates, and applications while internally integrating with Zoho People.

ATS Used

Zoho People

Zoho People was selected due to its:

Reliable API documentation

OAuth-based authentication

ATS-like employee and recruitment modules

During development, Zoho OAuth access tokens were short-lived and rate-limited, so mock responses are used for demo purposes, while the integration structure closely follows real Zoho API logic.
This allows easy switching to live APIs in production.

Features

GET /jobs – List open jobs (with pagination)

POST /candidates – Create a candidate and attach them to a job

GET /applications?job_id=... – List applications for a given job (with pagination)

Clean error handling and input validation

Environment-variable-based configuration for secrets

Tech Stack

Python 3.9

Serverless Framework

AWS Lambda (local execution via serverless-offline)

Zoho People (ATS)

Project Structure
ats-zoho-service/
├── handlers/
│   ├── jobs.py
│   ├── candidates.py
│   ├── applications.py
├── serverless.yml
├── requirements.txt
└── README.md

Setup Instructions
1️⃣ Install Dependencies
npm install -g serverless@3
pip install -r requirements.txt

2️⃣ Set Environment Variables
export ZOHO_BASE_URL=https://people.zoho.in/people/api
export ZOHO_ACCESS_TOKEN=your_access_token_here


For local demo, a dummy token can be used since mock responses are enabled.

3️⃣ Run Locally
serverless offline


Server will start at:

http://localhost:3000

API Usage
🔹 GET /jobs (With Pagination)
curl "http://localhost:3000/jobs?page=1&per_page=5"


Response

{
  "page": 1,
  "per_page": 5,
  "total": 50,
  "jobs": [
    {
      "id": "job_1",
      "title": "Python Backend Intern",
      "location": "Remote",
      "status": "OPEN",
      "external_url": ""
    }
  ]
}

🔹 POST /candidates
curl -X POST http://localhost:3000/candidates \
-H "Content-Type: application/json" \
-d '{
  "name": "Sai",
  "email": "sai@example.com",
  "phone": "9999999999",
  "resume_url": "https://example.com/resume.pdf",
  "job_id": "job_1"
}'


Response

{
  "message": "Candidate created and attached to job",
  "candidate_id": "cand_123",
  "application_status": "APPLIED",
  "job_id": "job_1"
}

🔹 GET /applications (With Pagination)
curl "http://localhost:3000/applications?job_id=job_1&page=1&per_page=3"


Response

{
  "job_id": "job_1",
  "page": 1,
  "per_page": 3,
  "total": 40,
  "applications": [
    {
    "id": "app_1",
      "candidate_name": "Candidate 1",
      "email": "user1@example.com",
      "status": "APPLIED"
    }
  ]
}

Pagination Support

Pagination is supported using query parameters:

?page=<page_number>&per_page=<items_per_page>


Examples

GET /jobs?page=2&per_page=5
GET /applications?job_id=job_1&page=1&per_page=10

Notes

Zoho OAuth access tokens are short-lived

Mock responses ensure stable demo behavior

Integration logic is production-ready

Mock layer can be replaced with live Zoho People APIs easily

Author

Tungala Lakshmi Venkata Sai
