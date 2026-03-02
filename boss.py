import requests
from bs4 import BeautifulSoup

# Website URL
URL = "https://undrgroundz18-ugz.github.io/Boss-Respawn-Timer/"

# Your Discord webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1477929350039863409/8xQdOT50K72u1xHMyVgjY2m6Onodm9iWBcUfEGhZYAtEMlS36Gbe3EJbookCp4VqawDL"

# Fetch website
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to fetch website:", response.status_code)
    exit(1)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Get visible text
page_text = soup.get_text()

# For now, send entire page text (we'll refine after)
message = page_text[:1500]  # Discord limit safety

# Send to Discord
requests.post(WEBHOOK_URL, json={"content": message})

print("Posted to Discord successfully!")
