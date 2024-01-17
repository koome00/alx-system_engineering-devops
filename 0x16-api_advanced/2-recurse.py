#!/usr/bin/python3
"""
Module 3: Recurse it!
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
     queries the Reddit API and returns a list containing
     the titles of all hot articles for
     a given subreddit. If no results are found for
     the given subreddit, the function should return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    r = response.json()
    if r.get('data').get('after') is not None:
        hot = r.get('data', {}).get('children')[0].get('data').get('title')
        hot_list.append(hot)
        return recurse(subreddit, hot_list=[])
    else:
        return hot_list
