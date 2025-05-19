import os
import requests
import time
from requests.auth import HTTPBasicAuth

url = os.getenv("GLUETUN_URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
interval_hours = float(os.getenv("INTERVAL_HOURS", "2"))

def stop_vpn():
    try:
        response = requests.put(
            url,
            auth=HTTPBasicAuth(username, password),
            headers={"Content-Type": "application/json"},
            json={"status": "stopped"}
        )
        print(f"[INFO] Status: {response.status_code} | Response: {response.text}")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    while True:
        stop_vpn()
        print(f"[INFO] Sleeping for {interval_hours} hours...")
        time.sleep(interval_hours * 3600)