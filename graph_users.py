import requests
import csv
from dotenv import load_dotenv
import os

load_dotenv()

tenant_id = os.getenv("TENANT_ID")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Step 1 - Get an access token
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

token_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": "https://graph.microsoft.com/.default"
}

token_response = requests.post(token_url, data=token_data)
token = token_response.json()["access_token"]
print("Token acquired successfully")

# Step 2 - Set headers
headers = {
    "Authorization": "Bearer " + token
}

# Step 3 - Call Graph API with selected fields
graph_url = "https://graph.microsoft.com/v1.0/users?$select=displayName,mail,department,accountEnabled,assignedLicenses"

all_users = []
next_url = graph_url

while next_url:
    response = requests.get(next_url, headers=headers)
    data = response.json()
    all_users.extend(data["value"])
    next_url = data.get("@odata.nextLink")

print(f"Total users found: {len(all_users)}")

# Step 4 - Print all users with full details
for user in all_users:
    name = user["displayName"]
    email = user["mail"] if user["mail"] else "No email"
    department = user["department"] if user["department"] else "No department"
    enabled = "Active" if user["accountEnabled"] else "Disabled"
    licences = len(user["assignedLicenses"])

    print(f"{name} | {email} | {department} | {enabled} | {licences} licences")

# Step 5 - Export to CSV
with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Email", "Department", "Status", "Licences"])
    
    for user in all_users:
        name = user["displayName"]
        email = user["mail"] if user["mail"] else "No email"
        department = user["department"] if user["department"] else "No department"
        enabled = "Active" if user["accountEnabled"] else "Disabled"
        licences = len(user["assignedLicenses"])
        writer.writerow([name, email, department, enabled, licences])

print("Exported to users.csv")