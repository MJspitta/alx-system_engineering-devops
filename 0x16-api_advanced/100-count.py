#!/usr/bin/python3
"""count words in all hot posts of a given reddit subreddit"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """recursive func that queries the reddit api"""
    if not word_list or word_list == [] or not subreddit:
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/10.0/API'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url,
                           headers=headers,
                           params=params,
                           allow_redirects=False)
    if response.status_code != 200:
        return

    mdata = response.json()
    data = mdata.get('data')
    children = data.get('children')
    for post in children:
        title = post.get('data', {}).get('title').lower()
        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + title.count(word.lower())
    after = mdata.get('data', {}).get('after')
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print("{}: {}".format(word.lower(), count))
