import requests

DATA_URL = "https://undrgroundz18-ugz.github.io/Boss-Respawn-Timer/data.json"
WEBHOOK_URL = "https://discord.com/api/webhooks/1480494683321794661/_EZMPjLT52NPKcZbBROQNuW9MQpF4jUqe98z6rrijMaaFKpx7OzKzx8uUqvSDwHrg8XW"

response = requests.get(DATA_URL)
data = response.json()

# Debug: show what the JSON actually looks like
print("JSON DATA:", data)

message = "🔥 **Boss Respawn Timer** 🔥\n\n"

# If JSON is a list
if isinstance(data, list):
    bosses = data

# If JSON is a dictionary
elif isinstance(data, dict):
    bosses = data.get("bosses", [])

else:
    bosses = []

for boss in bosses:

    if not isinstance(boss, dict):
        continue

    name = boss.get("name", "Unknown")
    location = boss.get("location", "Unknown")
    respawn = boss.get("respawn", "Unknown")

    message += f"⚔️ **{name}** - {location}\n⏰ {respawn}\n\n"

requests.post(WEBHOOK_URL, json={"content": message})

print("Posted boss list to Discord!")
