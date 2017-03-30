"""
Grabs NYT politics
"""
import random
import feedparser

#
# Main prog
def choppy(data, force=False):
    """
    Chops what u need
    """
    headlines = [
        i["title"].replace("'", "").replace('"', "").replace(":", "").encode("ascii", "ignore") \
        for i in data["entries"]
    ]
    if force:
        return random.choice(headlines)
    else:
        lines = random.choice(headlines).split(" ")
        banga = 10 if len(lines) >= 10 else len(lines)
        start = 4 if len(lines) >= 8 else 1
        words = [word for word in lines[0:random.randrange(start, banga)]]
        return " ".join(words)

def nytimes(force=False):
    """
    crappy celeb news
    """
    data = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml')
    #
    # Filter out crap and fix utf encoding so it can be listed
    #print data
    return choppy(data, force)

def bbcent(force=False):
    """
    crappy celeb news
    """
    data = feedparser.parse('http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml?edition=uk')
    return choppy(data, force)
def bbcworld(force=False):
    """
    crappy celeb news
    """
    data = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk')
    return choppy(data, force)

def skynews(force=False):
    """
    crappy celeb news
    """
    data = feedparser.parse('http://feeds.skynews.com/feeds/rss/uk.xml')
    return choppy(data, force)
#
# for test runs
if __name__ == "__main__":
    print nytimes()
    print skynews()
    print bbcworld()
    print bbcent(True)
    