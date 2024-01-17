#!/usr/bin/python3
'''
Module 1: Reddit API querying
'''


import requests


def number_of_subscribers(subreddit):
    """
    returns number of subscribers of a channel
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    header = requests.utils.default_headers()
    header.update({'User-Agent': 'Reddit Api'})

    response = requests.get(url, headers=header)
    r = response.json()

    subscribers = r.get('data', None).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
