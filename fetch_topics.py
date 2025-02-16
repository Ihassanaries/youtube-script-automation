import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

# Directly use the Streamlit secret (no need for json.dumps or json.loads)
service_account_info = st.secrets["GOOGLE_CREDENTIALS"]

# Authenticate with Google Sheets API
creds = Credentials.from_service_account_info(service_account_info)
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
