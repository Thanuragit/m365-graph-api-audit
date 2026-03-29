# M365 Graph API User Audit

A Python script that authenticates to Microsoft 365 via the 
Microsoft Graph API and pulls a full user audit including 
display name, email, department, account status, and licence count.

## What it does
- Authenticates using OAuth2 client credentials flow
- Calls Microsoft Graph API users endpoint
- Exports results to CSV

## Tech used
- Python
- Microsoft Graph API
- Azure App Registration
- python-dotenv for secrets management

## Setup
1. Register an app in Entra ID with User.Read.All permission
2. Create a .env file with your TENANT_ID, CLIENT_ID, CLIENT_SECRET
3. Run: py graph_users.py
