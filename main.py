import re
import asyncio
from pyrogram import Client
# --------- Replace these ----------
api_id = 123456
api_hash = "api_hash"
session_str = "session_str"
# ----------------------------------


PRIMARY_PATTERN = re.compile(r'(?i)\b(?:login code|code)\s*[:\-]?\s*(\d{4,6})\b')
FALLBACK_PATTERN = re.compile(r'\b(\d{4,6})\b')

async def extract_login_code(limit_msgs=300, per_dialog_limit=100):
    app = Client("session", api_id=api_id, api_hash=api_hash, session_string=session_str)
    await app.start()

    me = await app.get_me()
    print(f"Connected as: {getattr(me, 'username', me.first_name)} (id={me.id})\n")

    checked, found = 0, False

    async for dialog in app.get_dialogs():
        async for msg in app.get_chat_history(dialog.chat.id, limit=per_dialog_limit):
            if checked >= limit_msgs:
                break
            checked += 1

            text = msg.text or msg.caption
            if not text:
                continue
            text = text.strip()

            m = PRIMARY_PATTERN.search(text)
            if m:
                code = m.group(1)
                print("🔐 Found login code (explicit):", code)
                print("From:", getattr(dialog.chat, 'title', getattr(dialog.chat, 'username', dialog.chat.id)))
                print("Message:", text)
                found = True
                break

            m2 = FALLBACK_PATTERN.search(text)
            if m2:
                hint = any(word in text.lower() for word in ["login", "telegram", "do not give", "code"])
                if hint:
                    code = m2.group(1)
                    print("🔐 Found probable login code (fallback):", code)
                    print("From:", getattr(dialog.chat, 'title', getattr(dialog.chat, 'username', dialog.chat.id)))
                    print("Message:", text)
                    found = True
                    break

        if found or checked >= limit_msgs:
            break

    if not found:
        print(f"No login code found in the most recent {checked} messages (limit {limit_msgs}).")

    await app.stop()

if __name__ == "__main__":
    asyncio.run(extract_login_code())
