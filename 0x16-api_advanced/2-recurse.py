#!/usr/bin/python3
"""query api recursively for all hot articles"""
import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    """return hot articles or None if invalid"""
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after != "tmp":
        url = url + "?after={}".format(after)
    r = requests.get(url, headers=headers, allow_redirects=False)
    results = r.json().get('data', {}).get('children', [])
    if not results:
        return hot_list
    for e in results:
        hot_list.append(e.get('data').get('title'))
    after = r.json().get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
