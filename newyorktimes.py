"""
Grabs NYT politics
"""
import random
import feedparser

#
# Main prog
def nytimes():
    """
    crappy celeb news
    """
    data = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml')
    #
    # Filter out crap and fix utf encoding so it can be listed
    #print data
    headlines = [
        i["title"].replace("'", "").replace('"', "").replace(":", "").encode("ascii", "ignore") \
        for i in data["entries"]
    ]
    words = [word for word in random.choice(headlines).split(" ")[0:random.randrange(2, 10)]]
    return " ".join(words)
#
# for test runs
if __name__ == "__main__":
    print nytimes()
