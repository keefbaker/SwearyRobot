import feedparser
import random
def celebgrab():
	data = feedparser.parse('http://feeds.accesshollywood.com/AccessHollywood/LatestNews')
	headlines = [i["title"].replace("'","").replace('"',"").replace(":","").encode("ascii", "ignore") for i in data["entries"]]
	words = [word for word in random.choice(headlines).split(" ")[0:2]]
	return " ".join(words)
if __name__ == "__main__":
	print celebgrab()