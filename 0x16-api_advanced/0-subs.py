#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscriber
"""
import requests


def number_of_subscribers(subreddit):
    """return number of subscribers or 0 if invalid"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    try:
        resp = requests.get(url, headers=headers, allow_redirects=False)
        if resp.status_code == 200:
            data = resp.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            return 0
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return 0
