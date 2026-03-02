import requests
from bs4 import BeautifulSoup

WEBHOOK = "https://discord.com/api/webhooks/1477929350039863409/8xQdOT50K72u1xHMyVgjY2m6Onodm9iWBcUfEGhZYAtEMlS36Gbe3EJbookCp4VqawDL"
URL = "https://undrgroundz18-ugz.github.io/Boss-Respawn-Timer/index.html"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

message = "Boss Respawn Update\n\n"

rows = soup.find_all("tr")

for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 4:
        boss = cols[0].text.strip()
        status = cols[1].text.strip()
        respawn = cols[2].text.strip()
        countdown = cols[3].text.strip()

        message += f"**{boss}**\nStatus: {status}\nRespawn: {respawn}\nCountdown: {countdown}\n\n"

requests.post(WEBHOOK, json={"content": message})
