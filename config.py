import os
from pathlib import Path

GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")
GOOGLE_TOKEN_PATH = os.getenv("GOOGLE_TOKEN_PATH")
GOOGLE_CALENDAR_SCOPES = ["https://www.googleapis.com/auth/calendar"]
OBSIDIAN_VAULT_PATH = Path(os.getenv("OBSIDIAN_VAULT_PATH"))
OBSIDIAN_DEFAULT_FOLDER = os.getenv("OBSIDIAN_DEFAULT_FOLDER")
LOG_PATH = Path(os.getenv("LOG_PATH"))
TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
