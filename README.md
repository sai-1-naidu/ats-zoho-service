# ATS Integration Microservice (Zoho People)

This project is a serverless ATS (Applicant Tracking System) integration microservice built using Python and the Serverless Framework. It exposes a unified REST API for jobs, candidates, and applications while integrating with Zoho People as a third-party platform.

## ATS Used
Zoho People

Zoho People was selected due to its reliable REST APIs, OAuth-based authentication, and HR/ATS-style data models.

## Third-Party Integration

The service fetches data directly from Zoho People using live HTTP requests.  
All job data returned by the `/jobs` endpoint depends on the response from Zoho People APIs and is not statically generated.

Authentication is handled using OAuth access tokens supplied via environment variables.

## Features
- GET /jobs – Fetch jobs from Zoho People (with pagination support)
- POST /candidates – Accept candidate details and associate them with a job
- GET /applications?job_id=... – List applications for a given job
- Clean error handling and input validation
- Environment-variable-based configuration for secrets

## Tech Stack
- Python 3.9
- Serverless Framework
- AWS Lambda (local execution via serverless-offline)
- Zoho People (Third-Party ATS)

## Project Structure
ats-zoho-service/
├── handlers/
│ ├── jobs.py
│ ├── candidates.py
│ └── applications.py
├── serverless.yml
├── requirements.txt
└── README.md


## Setup Instructions

### 1️⃣ Install Dependencies
```bash
npm install -g serverless@3
pip install -r requirements.txt
```
2️⃣ Set Environment Variables
Windows PowerShell
$env:ZOHO_BASE_URL="https://people.zoho.in/people/api"
$env:ZOHO_ACCESS_TOKEN="your_real_zoho_access_token"
Linux / macOS
export ZOHO_BASE_URL=https://people.zoho.in/people/api
export ZOHO_ACCESS_TOKEN=your_real_zoho_access_token
3️⃣ Run Locally
serverless offline
Server starts at:

http://localhost:3000
API Usage
🔹 GET /jobs
curl http://localhost:3000/jobs
Response:

[
  {
    "id": "123456",
    "title": "Python Backend Intern",
    "location": "N/A",
    "status": "OPEN",
    "external_url": ""
  }
]
🔹 POST /candidates
curl -X POST http://localhost:3000/candidates \
-H "Content-Type: application/json" \
-d '{
  "name": "Sai",
  "email": "sai@example.com",
  "phone": "9999999999",
  "resume_url": "https://example.com/resume.pdf",
  "job_id": "123456"
}'
🔹 GET /applications
curl "http://localhost:3000/applications?job_id=123456"
Response:

{
  "count": 0,
  "applications": []
}
Notes
Zoho OAuth access tokens are short-lived and scope-based

API responses depend on Zoho People availability and permissions

No static or hardcoded job data is used

The service demonstrates real third-party platform integration

Author
Tungala Lakshmi Venkata Sai
