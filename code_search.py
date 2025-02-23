import requests
import sys
import os
import json
from security import safe_requests

def search_github(action, keyword, token):
    url = f"https://api.github.com/search/{action}?q={keyword}&sort=indexed&order=desc&per_page=100"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = safe_requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python github_search.py <code | repositories | issues | topics> <keyword>")
        sys.exit(1)

    action = sys.argv[1]
    keyword = sys.argv[2]
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("Error: GITHUB_TOKEN environment variable not set.")
        sys.exit(1)

    if action not in ["code", "repositories", "issues", "topics"]:
        print("Error: Action must be either 'code' or 'repositories'.")
        sys.exit(1)

    if action:
        result = search_github(action, keyword, token)


    if result:
        print(json.dumps(result, indent=4))
    else:
        print("No results found or an error occurred.")
