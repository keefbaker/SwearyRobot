'''
Grabs top 10 films from amazone
'''
import random
import sys
import feedparser
if sys.version_info[0] < 3:
    from __future__ import print_function


def dvdgrab(yep=True):
    '''
    grabs amazon top 10
    '''
    data = feedparser.parse(
        'http://www.amazon.co.uk/gp/rss/bestsellers/dvd/ref=zg_bs_dvd_rsslink'
        )
    headlines = [i['title'].encode('ascii', 'ignore') for i in data['entries']]
    brackets = set('[]()-')
    words = [
        word for word in random.choice(
            headlines).split(' ')[1:-1] if not brackets.intersection(word)
        ]
    if yep:
        return ' '.join(words)
    return ''
if __name__ == '__main__':
    print(dvdgrab())
