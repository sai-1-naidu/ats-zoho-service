ATS Integration Microservice (Zoho Recruit)

This project is a serverless ATS (Applicant Tracking System) integration microservice built using Python and the Serverless Framework.
It exposes a unified REST API for jobs, candidates, and applications, while integrating with Zoho Recruit as a third-party ATS platform.

ATS Used

Zoho Recruit

Zoho Recruit was selected because it is a dedicated ATS platform that provides REST APIs, OAuth 2.0 authentication, and standard hiring workflows such as job openings, candidates, and applications.

Third-Party Integration

The service integrates with Zoho Recruit APIs using live HTTP requests.

OAuth 2.0 access tokens are used for authentication and are supplied via environment variables.

API calls are made to official Zoho Recruit endpoints (/recruit/v2).

Error handling is implemented to gracefully manage API restrictions and failures.

⚠️ Note: Zoho Recruit restricts API access for trial accounts. In such cases, the service detects non-JSON (HTML) responses and handles them gracefully while keeping the real integration logic intact.

Features

GET /jobs – Fetch job openings from Zoho Recruit (pagination supported)

POST /candidates – Create a candidate in Zoho Recruit

GET /applications?job_id=... – List applications for a given job

Clean input validation and error handling

Environment-variable-based configuration for secrets

Production-style API client abstraction

Tech Stack

Python 3.9

Serverless Framework

AWS Lambda (local execution via serverless-offline)

Zoho Recruit (Third-Party ATS)

Project Structure
ats-zoho-service/
├── handlers/
│   ├── jobs.py
│   ├── candidates.py
│   └── applications.py
├── services/
│   └── zoho_recruit_client.py
├── serverless.yml
├── requirements.txt
└── README.md

Setup Instructions
1️⃣ Install Dependencies
npm install -g serverless@3
pip install -r requirements.txt

2️⃣ Set Environment Variables
Windows (PowerShell)
$env:ZOHO_ACCESS_TOKEN="your_zoho_access_token"

Linux / macOS
export ZOHO_ACCESS_TOKEN=your_zoho_access_token

3️⃣ Run Locally
serverless offline


Server starts at:

http://localhost:3000

API Usage
🔹 GET /jobs
curl http://localhost:3000/jobs


Response:

{
  "data": []
}

🔹 POST /candidates
curl -X POST http://localhost:3000/candidates \
-H "Content-Type: application/json" \
-d '{
  "name": "Sai Naidu",
  "email": "sai@example.com",
  "phone": "9999999999"
}'

🔹 GET /applications
curl "http://localhost:3000/applications?job_id=123456"


Response:

{
  "count": 0,
  "applications": []
}

Notes

Zoho Recruit OAuth access tokens are short-lived and scope-based

API access may be restricted for trial accounts

The service includes graceful handling for API limitations

Real Zoho Recruit integration logic is implemented and production-ready

No static or hardcoded ATS data is used in the integration layer

Author

Tungala Lakshmi Venkata Sai
