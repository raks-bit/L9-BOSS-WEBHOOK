import requests

WEBHOOK = "https://discord.com/api/webhooks/1477929350039863409/8xQdOT50K72u1xHMyVgjY2m6Onodm9iWBcUfEGhZYAtEMlS36Gbe3EJbookCp4VqawDL"

# JSON data source used by the boss timer site
DATA_URL = "https://undrgroundz18-ugz.github.io/Boss-Respawn-Timer/data.json"

response = requests.get(DATA_URL)
data = response.json()

message = "Boss Respawn Update\n\n"

for boss in data:
    name = boss.get("name", "Unknown")
    status = boss.get("status", "Unknown")
    respawn = boss.get("respawn", "Unknown")
    countdown = boss.get("countdown", "Unknown")

    message += f"**{name}**\n"
    message += f"Status: {status}\n"
    message += f"Respawn: {respawn}\n"
    message += f"Countdown: {countdown}\n\n"

requests.post(WEBHOOK, json={"content": message})
