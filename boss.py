import requests

DATA_URL = "https://undrgroundz18-ugz.github.io/Boss-Respawn-Timer/data.json"
WEBHOOK_URL = "https://discord.com/api/webhooks/1480494683321794661/_EZMPjLT52NPKcZbBROQNuW9MQpF4jUqe98z6rrijMaaFKpx7OzKzx8uUqvSDwHrg8XW"

response = requests.get(https://undrgroundz18-ugz.github.io/Boss-Respawn-Timer/data.json)
data = response.json()

message = "🔥 **Boss Respawn Timer** 🔥\n\n"

for boss in data["bosses"]:
    name = boss.get("name", "Unknown")
    location = boss.get("location", "Unknown")
    respawn = boss.get("respawn", "Unknown")

    message += f"⚔️ **{name}** - {location}\n⏰ {respawn}\n\n"

requests.post(WEBHOOK_URL, json={"content": message})

print("Posted boss list to Discord!")
