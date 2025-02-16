import gspread
from google.oauth2.service_account import Credentials

# Authenticate with Google Sheets API
creds = Credentials.from_service_account_file("google_credentials.json")
client = gspread.authorize(creds)

# Open Google Sheets
SHEET_NAME = "slscriptwritingautomation"
sheet = client.open(SHEET_NAME).worksheet("Topics")

# Fetch all topics & categories
data = sheet.get_all_records()

def get_topic_and_category():
    for row in data:
        topic = row['Topic']
        category = row['Category']
        yield topic, category
