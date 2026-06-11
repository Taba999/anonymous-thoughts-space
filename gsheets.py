import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

SERVICE_ACCOUNT_FILE = "service_account.json"

creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

client = gspread.authorize(creds)

# Open your Google Sheet (must match EXACT name)
sheet = client.open_by_key("1Bt2Bi2bMFv3NB17nOOrKn4SxacfnqhPa5-JzbfGDNuk").sheet1

def add_post(user, character, text):
    sheet.append_row([user, character, text])


def get_posts():
    return sheet.get_all_records()