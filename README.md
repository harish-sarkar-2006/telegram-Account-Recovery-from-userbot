# Telegram OTP Extractor / Account Recovery Helper

A small utility (Pyrogram) that scans your own Telegram account's recent messages and extracts login codes (OTP) such as messages that look like:

**Login code:** 25903. Do not give this code to anyone...

> ⚠️ Use this only for **your own** Telegram account. Do **not** use for unauthorized access. I will not help with any illegal or unethical activity.

---

## Features
- Scans recent dialogs and messages for OTP patterns (explicit "Login code" lines or 4–6 digit codes with OTP-like hints).
- Works with Pyrogram session strings or local session files.
- Lightweight and easy to run locally or on a VPS to avoid missing temporary messages.

---

## Quick start

### 1. Clone / copy files
Place your script (e.g. `account-recovery.py`) and `requirements.txt` in a folder.

### 2. Create & activate virtual environment

**Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

Linux / macOS

python3 -m venv venv
source venv/bin/activate


3. Install dependencies
pip install -r requirements.txt



4. Configure the script

Open account-recovery.py and set these variables:

api_id = 123456                  # your API ID
api_hash = "your_api_hash"       # your API hash
session_str = "YOUR_SESSION_STRING"  # OR None to use a local session file


Get API ID & Hash from my.telegram.org
.

If session_str = None, Pyrogram will create a local .session file after login.

Do not share api_id, api_hash, or session_str.




5. Run the script
python main.py


The script will connect to your Telegram account.

It scans recent messages and prints any login codes (OTP) found.
