import requests
import time

url = "http://localhost:9080/test"

while True:
    try:
        r = requests.get(url)
        print(f"{r.status_code} - {r.text.strip()}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(1)