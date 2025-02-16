from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def save_to_google_docs(script, topic):
    creds = Credentials.from_service_account_file("google_credentials.json")
    service = build("docs", "v1", credentials=creds)

    document = service.documents().create(body={"title": topic}).execute()
    doc_id = document["documentId"]

    requests = [{"insertText": {"location": {"index": 1}, "text": script}}]
    service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()

    return f"https://docs.google.com/document/d/{doc_id}"
