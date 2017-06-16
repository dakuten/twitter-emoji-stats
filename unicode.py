#!/usr/bin/env python3
"""Functions that deal with unicode strings

   date   : some day in June I should spend working on something else
   author : @dakuten
   license: (c)ovfefe
"""
import emoji
import re
from collections import Counter

R_emoji = emoji.get_emoji_regexp()
ZWJ = u"\u200d"
variation_selectors = "".join(map(chr,range(0xfe00,0xfe0f+1,1)))
variation_selector_pattern = "["+variation_selectors+"]?"
zwj_joined_sequence_pattern = "((."+variation_selector_pattern+ZWJ+")+.)"
R_zwjseq = re.compile(zwj_joined_sequence_pattern)


def is_valid_zwj_sequence(zwjseq):
    return len(R_emoji.findall(zwjseq)) - zwjseq.count(ZWJ) == 1

def get_ZWJseq(ustring):
    retstring  = ustring
    correctzwj = []

    for zwjseqmatch in R_zwjseq.finditer(ustring):
        zwjseq = zwjseq[0]
        if is_valid_zwj_sequence(zwjseq):
            retstring = retstring[:zwjseqmatch.start()]+retstring[:zwjseqmatch.end()]
            correctzwj.append(zwjseq)
    return (retstring, correctzwj)


def get_emojis(ustring):
    ustring, emojis = get_ZWJseq(ustring)
    for emoji_match in R_emoji.finditer(ustring):
        i = emoji_match.end()
        nextchar = ustring[i] if i<len(ustring) else 'q'

        if nextchar in variation_selectors:
            emojis.append(emoji_match[0]+nextchar)
        else:
            emojis.append(emoji_match[0])
    return emojis

count_emojis = lambda ustring: Counter(get_emojis(ustring))
