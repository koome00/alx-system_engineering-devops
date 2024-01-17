#!/usr/bin/python3
'''
Module 2: Top Ten
'''


import requests


def top_ten(subreddit):
    '''
    queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
    '''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            r = response.json()
            top = r.get('data', {}).get('children')
            for posts in top:
                print(r.get('data').get('title'))
        except requests.exceptions.JSONDecodeError as e:
            return None
    elif response.status_code == 404:
    # if subreddit does not exist
        return None
    else:
        return None
