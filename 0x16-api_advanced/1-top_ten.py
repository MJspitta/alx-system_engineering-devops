#!/usr/bin/python3
"""function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    response = requests.get(url, headers=headers).json()
    topten = response.get('data', {}).get('children', [])
    if not topten:
        print(None)
    for i in topten:
        print(i.get('data').get('title'))
