import requests
import sys
import os
import json

def search_github_code(keyword, token):
    url = f"https://api.github.com/search/code?q={keyword}&sort=indexed&order=desc&per_page=100"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def search_github_repositories(keyword, token):
    url = f"https://api.github.com/search/repositories?q={keyword}&sort=stars&order=desc&per_page=100"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python github_search.py <keyword> ")
        sys.exit(1)

    keyword = sys.argv[1]
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set.")
        sys.exit(1)

    result = search_github_code(keyword, token)
    if result:
        print(json.dumps(result, indent=4))
