#!/usr/bin/python3
'''
Module 1: Reddit API querying
'''


import requests


def number_of_subscribers(subreddit):
    """
    returns number of subscribers of a channel
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
    # check if subreddits exist
        try:
            # check if valid json response
            r = response.json()
            subscribers = r.get('data', {}).get('subscribers')
            if subscribers is not None:
                return subscribers
            else:
                return 9
        except requests.exceptions.JSONDecodeError as e:
            return 3

    elif response.status_code == 404:
    # if subreddit does not exist
        return 4
    else:
        return response.status_code
