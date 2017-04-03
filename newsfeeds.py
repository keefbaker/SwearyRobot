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
    bbc world news
    """
    data = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk')
    return choppy(data, force)

def skynews(force=False):
    """
    Sky news
    """
    data = feedparser.parse('http://feeds.skynews.com/feeds/rss/uk.xml')
    return choppy(data, force)
def guardian(force=False):
    """
    from The Guardian
    """
    data = feedparser.parse('https://www.theguardian.com/world/rss')
    return choppy(data, force)
def lowcarb(force=False):
    """
    Low Carb recipes
    """
    data = feedparser.parse('http://feeds.feedburner.com/SimplyRecipesLowCarb')
    return choppy(data, force)
def denofgeek(force=False):
    """
    Low Carb recipes
    """
    data = feedparser.parse('http://www.denofgeek.com/uk/feeds/all')
    return choppy(data, force)
def science(force=False):
    """
    Low Carb recipes
    """
    data = feedparser.parse('https://rss.sciencedaily.com/all.xml')
    return choppy(data, force)
def rockpaper(force=False):
    """
    Low Carb recipes
    """
    data = feedparser.parse('http://feeds.feedburner.com/RockPaperShotgun')
    return choppy(data, force)
def compweek(force=False):
    """
    Low Carb recipes
    """
    data = feedparser.parse('http://www.computerweekly.com/rss/IT-security.xml')
    return choppy(data, force)
def hedge(force=False):
    """
    Stuff
    """
    data = feedparser.parse('http://feeds.feedburner.com/zerohedge/feed')
    return choppy(data, force)

#
# for test runs
if __name__ == "__main__":
    lists = [ "lowcarb", "guardian", "skynews", "nytimes", "bbcent", "compweek"]
    #print eval(random.choice(lists) + "(True)")
    print hedge(True)
    