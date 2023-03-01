#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed
for a given subreddit"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    try:
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
