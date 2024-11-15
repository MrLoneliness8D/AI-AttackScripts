import requests
from concurrent.futures import ThreadPoolExecutor
import time

TARGET_URL = 'http://localhost:8080'  # Use a server you have permission to test
REQUESTS_PER_SECOND = 50  # Number of requests per second

def send_request():
    """Send a GET request to the target URL."""
    try:
        response = requests.get(TARGET_URL)
        print(f"Response Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def simulate_traffic(duration=10):
    """Simulate high traffic for a set duration in seconds."""
    print(f"Simulating high traffic to {TARGET_URL} for {duration} seconds.")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=REQUESTS_PER_SECOND) as executor:
        while time.time() - start_time < duration:
            executor.submit(send_request)
            time.sleep(1 / REQUESTS_PER_SECOND)

simulate_traffic(duration=10)
