#!/usr/bin/env python
import feedparser
import random
class BreakOut(Exception): pass
#
# Fill out usable common word the Daily Hate uses
def grabstuff():
        Maildata = feedparser.parse('http://www.dailymail.co.uk/home/index.rss')
        global summaries
        summaries = [i["summary"] for i in Maildata["entries"]]
        hotwords= {}
        crapwords = ( "the", "a", "in", "and", "from", "for", "with", "on", "was", "at", "earlier", "his", "her", "is", "after", "are", "they", "go", "to", "by", "that", "be", "as", "their", "have", "he" , 'of', 'has', '-', 'were', 'it', 'an', 'but', 'said', 'been', 'up', 'who', 'she', 'university', 'year', 'its', '', 'while', 'this', 'which', 'about', 'before', 'had', 'not', 'one', 'or', 'more', 'new', 'over', 'christmas', 'can', 'than', 'being', 'you', 'all', 'two', 'will', 'may', 'now', 'only', 'your', 'some', 'out', 'last', 'made', 'mother', 'left', 'just', 'people', 'time', 'found', 'most', 'per', 'into', 'could', 'state', 'off', 'home', 'would', '(pictured)', 'them', 'if', 'when', 'daily', 'car', 'city', 'around', 'what', 'video', 'south', 'five', 'other', 'told', 'study', 'how', 'way', 'first', 'show', 'according', 'west', 'world', 'through', 'during', 'london,', 'following', 'need', 'even', 'men')
        for urghHeadline in summaries:
                for word in urghHeadline.split(" "):
                        try:
                                word = str(word).lower()
                        except:
                                word = "a"
                        if word not in hotwords and word not in crapwords:
                                hotwords[word] = 1
                        elif word not in crapwords:
                                hotwords[word] += 1
        mailcrap = ""
        global tag
        tag = []
        zimbus = sorted(hotwords.items(), key=lambda x: x[1], reverse=True)
        for f, v in zimbus[:150]:
                tag.append(f)
#
# Grab Daily Heil headlines
def grab():
        summary = random.choice(summaries)
        sentence = []
        try:
                if len(str(summary)) > 100:
                        words = summary.split(' ')
                        for word in words:
                                sentence.append(word)
                                if word.endswith(",") and len(sentence) > 4:
                                        message = ' '.join(sentence)
                                        if (len(str(message)) < 100) and (len(str(message)) > 10):
                                                return str(message)
        except:
                pass
#
# Short loop to catch any issues with headlines, some parse weirdly.
def mail():
        global mailcrap
        mailcrap = grab()
        if mailcrap is None:
                mail()
#
# Export a load of common words from The Fail (used in SwearyRobot)
def younutter():
        headline = []
        grabstuff()
        for letters in "TheMailAreABunchOfCuntsAndIWouldntPissOnThemIfTheyWereOnFireNoIMeanItIHateTheBunchOfFascistFuckingBastardsAndTheyCanShoveTheirRacismUpTheirArse":
                headline.append(random.choice(tag))
        return headline
#
# Main program, returns a list of a headline and a few common words for use
def biglad():
        headline = []
        grabstuff()
        mail()
        headline.append(mailcrap)
        for letters in "Mail":
                headline.append(random.choice(tag))
        return headline
#
# so it can be run directly for testing
if __name__ == "__main__":
        dumper = biglad()
        print dumper


