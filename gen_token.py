import os.path
import json
from google_auth_oauthlib.flow import InstalledAppFlow

def gen_token():
  credentials = os.path.join(os.getcwd(), 'credentials.json')
  tokens = os.path.join(os.getcwd(), 'tokens.json')

  # Set the paths for your credentials and token files
  CREDENTIALS_FILE = credentials  # Replace with the correct path to your credentials file
  TOKEN_FILE = tokens  # Replace with the correct path where you want to store the token file

  # Load your credentials from the file
  creds = None
  if os.path.exists(TOKEN_FILE):
      with open(TOKEN_FILE, 'r', encoding='utf-8') as token:
          creds = json.load(token)

  # Check if the credentials are valid, and if not, start the OAuth flow
  if not creds or 'expiry' not in creds or 'refresh_token' not in creds:
      flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/drive'])
      creds = flow.run_local_server(port=0)
      creds = {
          'token': creds.token,
          'refresh_token': creds.refresh_token,
          'token_uri': creds.token_uri,
          'client_id': creds.client_id,
          'client_secret': creds.client_secret,
          'scopes': creds.scopes,
          'expiry': creds.expiry.isoformat()
      }

      # Save the credentials to the token file for future use
      with open(TOKEN_FILE, 'w', encoding='utf-8') as token:
          json.dump(creds, token, ensure_ascii=False, indent=2)