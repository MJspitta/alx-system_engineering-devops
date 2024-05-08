#!/usr/bin/python3
"""recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """return all hot articles or NOne if invalid"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                              AppleWebKit/537.36 (KHTML, like Gecko) \
                              Chrome/58.0.3029.110 Safari/537.3'}
    params = {'after': after, 'count': count, 'limit': 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get('data')
    after = results.get('after')
    count += results.get('dist')
    for i in results.get('children'):
        hot_list.append(i.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
