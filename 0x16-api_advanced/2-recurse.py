#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit"""
    global after
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, params=params, headers=user_agent,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('after')
        if data is not None:
            after = data
            recurse(subreddit, hot_list)
        titles = response.json().get('data').get('children')
        for title in titles:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        return None
