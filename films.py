import feedparser
import random
def dvdgrab():
	data = feedparser.parse('http://www.amazon.co.uk/gp/rss/bestsellers/dvd/ref=zg_bs_dvd_rsslink')
	headlines = [i["title"].encode("ascii", "ignore") for i in data["entries"]]
	words = [word for word in random.choice(headlines).split(" ")[1:-1] if "[" not in word and "]" not in word and "(" not in word and ")" not in word]
	return " ".join(words)
if __name__ == "__main__":
	print dvdgrab()