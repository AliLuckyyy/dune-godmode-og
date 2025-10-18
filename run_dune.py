import requests
import os
from datetime import datetime

DUNE_API_KEY = os.getenv("DUNE_API_KEY")
QUERY_ID = 5986631  # شناسه query خودت در Dune

url = f"https://api.dune.com/api/v1/query/{QUERY_ID}/execute"
headers = {"x-dune-api-key": DUNE_API_KEY}

response = requests.post(url, headers=headers)

if response.status_code == 200:
    print("Query executed successfully on Dune!")
    data = response.json()

    today = datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"dune_output_{today}.json"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(data))

    print(f"Output saved to {filename}")
else:
    print("Error executing query:", response.status_code, response.text)
