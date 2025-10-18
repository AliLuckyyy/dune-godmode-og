import requests
import os
from datetime import datetime

# گرفتن API Key از secret
DUNE_API_KEY = os.getenv("DUNE_API_KEY")
QUERY_ID = 5986631  # ID کوئری Dune شما

url = f"https://api.dune.com/api/v1/query/{QUERY_ID}/execute"
headers = {"x-dune-api-key": DUNE_API_KEY}

response = requests.post(url, headers=headers)

if response.status_code == 200:
    print("Query executed successfully!")
    data = response.json()
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"dune_output_{today}.json"
    with open(filename, "w") as f:
        f.write(str(data))
    print(f"Output saved to {filename}")
else:
    print("Error:", response.status_code, response.text)
