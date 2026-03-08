import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os
import json

URL = "https://www.premierpadel.com"

WATCH_PAIRS = [
    ["coello", "tapia"],
    ["galan", "chingotto"]
]

EMAIL = os.environ["EMAIL_USER"]
PASSWORD = os.environ["EMAIL_PASS"]
DEST = os.environ["EMAIL_DEST"]

STATE_FILE = "alert_state.json"


def send_email(message):

    msg = MIMEText(message)

    msg["Subject"] = "Alerta Premier Padel"
    msg["From"] = EMAIL
    msg["To"] = DEST

    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(EMAIL,PASSWORD)
    server.sendmail(EMAIL,DEST,msg.as_string())
    server.quit()


def load_state():

    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except:
        return {}


def save_state(state):

    with open(STATE_FILE,"w") as f:
        json.dump(state,f)


def detect_match():

    r = requests.get(URL)
    soup = BeautifulSoup(r.text,"html.parser")

    text = soup.get_text().lower()

    for pair in WATCH_PAIRS:

        if pair[0] in text and pair[1] in text:
            return pair

    return None


state = load_state()

pair = detect_match()

if pair:

    pair_name = f"{pair[0]} / {pair[1]}"

    if state.get("last_alert") != pair_name:

        send_email(
            f"🎾 Detectado partido de {pair_name} en Premier Padel"
        )

        state["last_alert"] = pair_name

else:

    state["last_alert"] = None


save_state(state)
