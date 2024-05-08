#!/usr/bin/python3
"""function that queries the Reddit API and returns
the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                              AppleWebKit/537.36 (KHTML, like Gecko) \
                              Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        results = response.json().get('data')
        return results.get('subscribers', 0)
    except requests.exceptions.RequestException as e:
        print("Error accessing Reddit API: {}".format(e))
        return 0
