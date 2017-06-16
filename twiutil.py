#!/usr/bin/env python3
"""Functions that deal with twitter

   date   : some day in June I should spend working on something else
   author : @dakuten
   license: (c)ovfefe
"""

import twitter

def get_last_tweets_from_user(api, user, nb, block_size=200):
    tl = api.GetUserTimeline(screen_name=user, count=min(nb,block_size))
    last_id = tl[-1].id
    block_size=min(len(tl),block_size)
    nb-=block_size
    yield tl
    while nb > 0:
        tl = api.GetUserTimeline(screen_name=user, count=min(nb,block_size), max_id=last_id-1)
        if len(tl)==0:
            break
        last_id = tl[-1].id
        nb-=block_size+1
        yield tl

tweet_text = lambda tw : tw.text
