#!/usr/bin/python3
"""
returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    returns a list of all hot topic title
    """
    url = "https://www.reddit.com/r/{}/hot.json"
    sub_reddit = requests.get(url.format(subreddit),
                              headers={"User-Agent": "google-chrome"},
                              params={"count": count, "after": after},
                              allow_redirects=False)

    if sub_reddit.status_code >= 300:
        return None

    updated_list = []
    for value in sub_reddit.json().get('data').get('children'):
        updated_list.append(value.get('data').get('title'))

    hot_list = hot_list + updated_list

    if not sub_reddit.json().get('data').get('after'):
        return hot_list

    return recurse(subreddit, hot_list,
                   sub_reddit.json().get('data').get('count'),
                   sub_reddit.json().get('data').get('after'))
