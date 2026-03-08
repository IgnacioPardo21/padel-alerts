import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

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

def send_email(message):

    msg = MIMEText(message)

    msg["Subject"] = "Alerta Premier Padel"
    msg["From"] = EMAIL
    msg["To"] = DEST

    server = smtplib.SMTP_SSL("smtp.gmail.com",465)

    server.login(EMAIL,PASSWORD)

    server.sendmail(
        EMAIL,
        DEST,
        msg.as_string()
    )

    server.quit()


response = requests.get(URL)

soup = BeautifulSoup(response.text,"html.parser")

text = soup.get_text().lower()

for player in PLAYERS:

    if player in text:

        send_email(
            f"Detectado partido de {player} en la web de Premier Padel"
        )

        break
