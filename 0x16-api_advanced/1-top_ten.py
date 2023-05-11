#!/usr/bin/python3
"""
prints the first 10 posts of the hotlist
"""
import requests


def top_ten(subreddit):
    """ prints the titles"""
    sub_reddit = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                              .format(subreddit),
                              headers={"user-agent": "google-chrome"},
                              allow_redirects=False)
    if sub_reddit.status_code >= 300:
        print('None')
    else:
        for value in sub_reddit.json().get('data').get('children'):
            print(value.get('data').get('title'))
