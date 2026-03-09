import requests
from bs4 import BeautifulSoup

URL = "https://undrgroundz18-ugz.github.io/Boss-Respawn-Timer/"
WEBHOOK_URL = "https://discord.com/api/webhooks/1480494683321794661/_EZMPjLT52NPKcZbBROQNuW9MQpF4jUqe98z6rrijMaaFKpx7OzKzx8uUqvSDwHrg8XW"

response = requests.get(URL)

if response.status_code != 200:
    print("Failed to fetch website:", response.status_code)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Try to extract boss table rows
bosses = []

rows = soup.find_all("tr")

for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 3:
        boss_name = cols[0].get_text(strip=True)
        status = cols[1].get_text(strip=True)
        respawn = cols[2].get_text(strip=True)

        bosses.append(f"⚔️ {boss_name} | {status} | {respawn}")

if not bosses:
    message = "❌ No boss data found (site may load with JavaScript)."
else:
    message = "**🔥 Boss Respawn Today 🔥**\n\n" + "\n".join(bosses[:20])

requests.post(WEBHOOK_URL, json={"content": message})

print("Posted to Discord!")
