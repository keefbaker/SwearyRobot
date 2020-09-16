'''
Get the daily fail stuff
'''

#!/usr/bin/env python
import random
import sys
import feedparser
if sys.version_info[0] < 3:
    from __future__ import print_function


class BreakOut(Exception):
    '''
    crash out
    '''
#
# Fill out usable common word the Daily Hate uses
def grabstuff():
    '''
    Grabs mail headlines
    '''
    maildata = feedparser.parse('http://www.dailymail.co.uk/home/index.rss')
    global SUMMARIES # pylint: disable=W0601
    SUMMARIES = [i['summary'] for i in maildata['entries']]
    hotwords = {}
    crapwords = ('the', 'a', 'in', 'and', 'from', 'for', 'with', 'on', 'was', 'at',
                 'earlier', 'his', 'her', 'is', 'after', 'are', 'they', 'go', 'to',
                 'by', 'that', 'be', 'as', 'their', 'have', 'he', 'of', 'has', '-',
                 'were', 'it', 'an', 'but', 'said', 'been', 'up', 'who', 'she',
                 'year', 'its', '', 'while', 'this', 'which', 'about', 'black',
                 'before', 'had', 'not', 'one', 'or', 'more', 'new', 'over', 'can', 'than',
                 'being', 'you', 'all', 'two', 'will', 'may', 'now', 'only', 'your', 'some',
                 'out', 'last', 'made', 'mother', 'left', 'just', 'people', 'time', 'found',
                 'most', 'per', 'into', 'could', 'state', 'off', 'home', 'would', '(pictured)',
                 'them', 'if', 'when', 'daily', 'car', 'city', 'around', 'what', 'video', 'south',
                 'five', 'other', 'told', 'study', 'how', 'way', 'first',
                 'show', 'according', 'west',
                 'world', 'through', 'during', 'london,', 'following', 'need', 'even', 'men')
    for nasty_headline in SUMMARIES:
        for word in nasty_headline.split(' '):
            try:
                word = str(word).lower()
            except ValueError:
                word = 'a'
            if word not in hotwords and word not in crapwords:
                hotwords[word] = 1
            elif word not in crapwords:
                hotwords[word] += 1
    global TAG # pylint: disable=W0601
    TAG = []
    sorted_hotwords = sorted(hotwords.items(), key=lambda x: x[1], reverse=True)
    for hword, _ in sorted_hotwords[:150]:
        TAG.append(hword)

#
# Grab Daily Heil headlines
def grab():
    '''
    master grabber
    '''
    summary = random.choice(SUMMARIES)
    sentence = []
    try:
        if len(str(summary)) > 100:
            words = summary.split(' ')
            for word in words:
                sentence.append(word)
                if word.endswith(',') and len(sentence) > 4:
                    message = ' '.join(sentence)
                    if (len(str(message)) < 100) and (len(str(message)) > 10):
                        return str(message)
    except ValueError:
        return ''
    return None
#
# Short loop to catch any issues with headlines, some parse weirdly.
def mail():
    '''
    Yep, catch crap
    '''
    global MAIL_CRAP # pylint: disable=W0601
    MAIL_CRAP = grab()
    if MAIL_CRAP is None:
        mail()
#
# Export a load of common words from The Fail (used in SwearyRobot)
def younutter():
    '''
    common word grabber
    '''
    headline = []
    grabstuff()
    for _ in 'TheMailAreABunchOfCuntsAndIWouldntPissOn' + \
        'ThemIfTheyWereOnFireNoIMeanItIHateTheBunchOfFascist' + \
            'FuckingBastardsAndTheyCanShoveTheirRacismUpTheirArse':
        headline.append(random.choice(TAG))
    return headline
#
# Main program, returns a list of a headline and a few common words for use
def biglad():
    '''
    Master controller
    '''
    headline = []
    grabstuff()
    mail()
    headline.append(MAIL_CRAP)
    for _ in 'Mail':
        headline.append(random.choice(TAG))
    return headline
#
# so it can be run directly for testing
if __name__ == '__main__':
    print(biglad())
