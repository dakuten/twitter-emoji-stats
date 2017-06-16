#!/usr/bin/env python3
"""Functions that deal with mainly main things

   date   : some day in June I should spend working on something else
   author : @dakuten
   license: (c)ovfefe
"""

import twiutil, emojicount
import twitter
from collections import Counter


def most_used_emojis(api, user, upto=-1):
    """le upto est en nombre de tweets
    """

    c = Counter()

    for part_tl in twiutil.get_last_tweets_from_user(api, user, upto):
        c = sum(map(emojicount.count_emojis, map(twiutil.tweet_text, part_tl)), c)

    return c
