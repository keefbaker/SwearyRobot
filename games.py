'''
game grabber from amazon
'''
import random
import sys
import feedparser
if sys.version_info[0] < 3:
    from __future__ import print_function

def gamegrab(yep=True):
    '''
    Grabs top 10 films from amazon
    '''
    data = feedparser.parse(
        'http://www.amazon.co.uk/gp/rss/bestsellers/videogames/ref=zg_bs_videogames_rsslink'
        )
    headlines = [i['title'].encode('ascii', 'ignore') for i in data['entries']]
    badstuff = set('-()')
    words = [word for word in random.choice(headlines).split(
        ' ')[1:-1] if not badstuff.intersection(word)]
    if yep:
        return ' '.join(words)
    return ''
if __name__ == '__main__':
    print(gamegrab())
