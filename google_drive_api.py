from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

# Path to the credentials file
CLIENT_SECRET_FILE = 'credentials/client_secret.json'

# Get credentials
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
creds = flow.run_local_server(port=0)

# Save the credentials for future runs
with open('credentials/token.json', 'w') as token:
    token.write(creds.to_json())

# Connect to Google Drive API
service = build('drive', 'v3', credentials=creds)

# Now, you can interact with Google Drive API
results = service.files().list(pageSize=10).execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(f"{item['name']} ({item['id']})")
