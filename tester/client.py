import requests
import time

def fetch(url, timeout=3):
    
    start = time.time()

    try:
        response = requests.get(url, timeout=timeout)

        latency = time.time() - start

        return {
            "status": response.status_code,
            "json": response.json(),
            "latency": latency,
            "error": None
        }

    except Exception as e:

        latency = time.time() - start

        return {
            "status": None,
            "json": None,
            "latency": latency,
            "error": str(e)
        }
