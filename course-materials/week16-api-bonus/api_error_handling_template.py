import requests


def fetch_json(url: str, *, timeout: int = 10):
    """Return parsed JSON data or None on failure."""
    try:
        response = requests.get(url, timeout=timeout)
    except requests.RequestException as exc:
        print(f"Network error: {exc}")
        return None

    if response.status_code == 200:
        return response.json()
    if response.status_code == 401:
        print("Unauthorized (401): check your API key.")
        return None
    if response.status_code == 404:
        print("Not found (404): verify endpoint path/params.")
        return None
    if response.status_code == 429:
        print("Rate limited (429): slow down and retry later.")
        return None

    print(f"Unexpected status code: {response.status_code}")
    return None


if __name__ == "__main__":
    demo_url = "https://rickandmortyapi.com/api/character/1"
    payload = fetch_json(demo_url)
    if payload is not None:
        print("Top-level keys:", list(payload.keys()))
