import requests

WEBHOOK = "https://discord.com/api/webhooks/1477929350039863409/8xQdOT50K72u1xHMyVgjY2m6Onodm9iWBcUfEGhZYAtEMlS36Gbe3EJbookCp4VqawDL"
DATA_URL = "https://raw.githubusercontent.com/undergroundz18-ugz/Boss-Respawn-Timer/master/data.json"

response = requests.get(DATA_URL)

if response.status_code != 200:
    print("Failed to fetch data:", response.status_code)
    print(response.text)
    exit(1)

try:
    data = response.json()
except Exception as e:
    print("JSON Error:", e)
    print(response.text)
    exit(1)

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
