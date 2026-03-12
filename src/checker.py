import requests

def check_url_status(url: str) -> bool:
    """
    Pings a URL and returns True if it responds with a 200 OK status.
    """
    try:
        # We use a short timeout so the pipeline doesn't hang on bad URLs
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        # Catches connection errors, timeouts, and invalid URLs
        return False

if __name__ == "__main__":
    # A quick manual test if you run the script directly
    target = "https://www.google.com"
    is_up = check_url_status(target)
    print(f"Website {target} is UP: {is_up}")