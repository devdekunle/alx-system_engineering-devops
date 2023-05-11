#!/usr/bin/python3
"""
queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a subreddit"""
    subreddit = requests.get('https://www.reddit.com/r/{}/about.json'
                             .format(subreddit),
                             headers={'user-agent': "google-chrome"},
                             allow_redirects=False)

    if subreddit.status_code >= 300:
        return 0

    return subreddit.json().get('data').get('subscribers')
