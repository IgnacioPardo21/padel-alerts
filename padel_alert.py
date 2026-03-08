import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os
import json
from datetime import datetime, timedelta

URL = "https://www.premierpadel.com"

PLAYERS = [
    "coello",
    "tapia",
    "galan",
    "chingotto"
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

    if not os.path.exists(STATE_FILE):
        return {}

    with open(STATE_FILE,"r") as f:
        return json.load(f)


def save_state(state):

    with open(STATE_FILE,"w") as f:
        json.dump(state,f)


def check_matches():

    r = requests.get(URL)
    soup = BeautifulSoup(r.text,"html.parser")

    text = soup.get_text().lower()

    for player in PLAYERS:

        if player in text:
            return player

    return None


state = load_state()

player = check_matches()

now = datetime.utcnow()

if player:

    if state.get("alert_sent") != True:

        send_email(
            f"🎾 Partido detectado de {player}. Posible inicio pronto."
        )

        state["alert_sent"] = True

else:

    state["alert_sent"] = False


save_state(state)
