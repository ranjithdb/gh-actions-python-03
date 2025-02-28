import requests

def fetch_api_response(url):
    """Fetch data from the given API URL and return the response JSON."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    data = fetch_api_response(api_url)
    print(data if data else "Failed to fetch API response")
