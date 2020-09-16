'''
Grabs celeb stuff
'''
import random
import sys
import feedparser
if sys.version_info[0] < 3:
    from __future__ import print_function

#
# Main prog
def celebgrab():
    '''
    crappy celeb news
    '''
    data = feedparser.parse('http://feeds.accesshollywood.com/AccessHollywood/LatestNews')
    #
    # Filter out crap and fix utf encoding so it can be listed
    headlines = [
        i['title'].replace(''', '').replace(''', '').replace(':', '').encode('ascii', 'ignore') \
        for i in data['entries']
    ]
    words = random.choice(headlines).split(' ')[0:2]
    return ' '.join(words)
#
# for test runs
if __name__ == '__main__':
    print(celebgrab())
