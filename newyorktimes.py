"""
Grabs NYT politics
"""
import random
import feedparser

#
# Main prog
def choppy(data):
    headlines = [
        i["title"].replace("'", "").replace('"', "").replace(":", "").encode("ascii", "ignore") \
        for i in data["entries"]
    ]
    lines = random.choice(headlines).split(" ")
    banga = 10 if len(lines) >= 10 else len(lines)
    words = [word for word in lines[0:random.randrange(4, banga)]]
    return " ".join(words)

def nytimes():
    """
    crappy celeb news
    """
    data = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml')
    #
    # Filter out crap and fix utf encoding so it can be listed
    #print data
    return choppy(data)


def skynews():
    """
    crappy celeb news
    """
    data = feedparser.parse('http://feeds.skynews.com/feeds/rss/uk.xml')
    return choppy(data)
  
#
# for test runs
if __name__ == "__main__":
    print nytimes()
    print skynews()