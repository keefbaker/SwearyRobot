"""
Master sweary robot program
"""

#!/usr/bin/env python
#
# Sweary Robot by Keith Baker
#
# To get this to work for yourself (or use it in a similar way), you'll need modules:
# feedparser and tweepy
# And put your api credentials just as variables into a sweary_creds.py, variable names
# are in the import statement below
#

import sys
import os
import random
import tweepy
import mailgen

# from games import gamegrab # pylint: disable=W0611
from holly import celebgrab
# from films import dvdgrab # pylint: disable=W0611
from newsfeeds import * # pylint: disable=W0614,W0401
from sweary_creds import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET # pylint: disable=E0401
if sys.version_info[0] < 3:
    from __future__ import unicode_literals, print_function
#
# set auth
try:
    AUTH = tweepy.OAuthHandler(API_KEY, API_SECRET)
    AUTH.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    API = tweepy.API(AUTH)
    twitter_name = "SwearyRobot"
except:
    pass
#
# It's combination list time!
#
rss = getmahfeeds()
superlative = ("Custard", "Dead", "Cunty", "Fucked", "Shitted", "Pink", "Blank", "Arsecake", "Fcuk",
               "Cock", "Insect", "Argonian", "Super", "Molested", "Ultra", "Fuckaroo", "Mega",
               "Enormo", "Mini", "Funky", "Moo", "Crap", "Ultra", "Weak", "Weepy", "Mad", "Rage",
               "Sad", "Farty", "Disgust-o-", "Bilious", "Pre-raphaelite-", "Vomito", "Arsey-",
               "Bad", "cavernous", "Good", "Insdious", "Rupert-Murdochian-", "Cry", "Foxnews",
               "Stilted-", "Impossa", "Bleeding ", "Nostril", "Diahorretic", "Enochian ",
               "Cockripping ", "Sharp", "Evil", "Disturbing ", "Jerkwad ", "Screwy ",
               "Arseweeping-", "Scagged-up ", "Stink", "Gunked-up ", "Fisted ", "Smeared ",
               "Disappointing-", "Pus-filled ", "Botty", "Dingle", "Pissy", "Rancid ", "Rot",
               "Cacky", "Skank", "Funsize ", "Baby", "Ming", "Dodgy", "Fuck", "Skate", "Dirty",
               "Death", "Murder", "Frothing wrath", "Porn", "Micro", "Internet", "Massive",
               "Crotch", "Dong", "King", "Queen", "Princess", "Hot", "Ice", "Nasty", "Bog",
               "Lantern-jawed-", "Crack", "Smeg", "Shitty", "Rat", "Lamplicking", "Incontinent ",
               "Trump", "Waste", "Gun-toting-", "Poo", "Milky", "Slime", "Colonic-",
               "Classically Greek ", "French rennaissance ", "Redfaced", "Minging", "Milquetost",
               "Muckchucking ", "Vomitous", "Victorian", "Ottoman-esque-", "Turdy", "Ape-like-",
               "Penis", "Burst", "Knob", "Horse", "Tiger", "Dog", "Donkey", "Hepatitis", "Bilge",
               "Torpid", "Bob-a-job-", "Shite", "Putrid", "Turd", "Spit", "Fuckknocking", "Jet",
               "Oozing", "Worthless", "Rank", "Mockable", "Soggy ", "Moist ", "Affable ",
               "Sproingy", "Meticulous ", "Orificial ", "Phallic")
with open('swears.txt') as swearfile:
    sfile = swearfile.read()
swear = sfile.split(',')
preposition = ("I mean %s,  right?", "Just %s!!", "There's %s.", "And there it is... %s.",
               "For the love of %s.", "For %s's sake!",
               "I'm raging about %s.", "It... %s just makes me sad.",
               "You're such a %s!", "This %s just isn't worth my time.",
               "I know I'm a bot, but %s, right?", "I can't take any more of this %s.",
               "I'm actually really pleased you %s!", "I just ate some %s. It tasted awful!",
               "This can %s off!", "%s!", "Life would be better without %s, don't you think?",
               "This is a new design of %s, let me tell you!",
               "I need some %s for my garage, has anyone got some?", "Your face is a %s!",
               "Your mum's %s makes me sick.", "Stick %s up your massive arse!",
               "New %s, please.",
               "I could do with a %s.", "What this country needs is a new %s.",
               "I'm not arsed about your your %s, so shut your fucking gob.",
               "If only the %s was real..", "There's some %s on telly tonight.",
               "Instagrammed my %s. Not many likes. Feeling sad.",
               "Amazon have free %s. I paid loads for mine. ", "I am president %s. Fear me!",
               "20 times I said. %s yourself!", "There's no %s here.", "Fuck a %s!!",
               "Nothing makes me %s like donuts.", "I need %s.", "Five %s's in my house!",
               "No way! %s!", "Start %sing yourself!", "I want to claw my own %s off!",
               "I could do with a %s,", "Hey, call me baby, love my %s.", "Sexy %s!",
               "Hotter than %s,", "Worst %s ever.", "Lick my %s!", "I wish I could %s. :(",
               "A mega%s..", ":) %s :( :/", "That %sing bastard!", "%s-a-tron!",
               "Well, %s me!",
               "How much %s do you need??", "Tell me more about %s!",
               "You failed %s!", "%s is nicer than this.", "I feel like a %s",
               "My life is %s.", "Is %s what it's come to?", "Aaaaaaaaaaaaaaaah %s!!!!!!",
               "New %s?"
               "Floweers like %s", "Lords of %s", "%s is the best", "No %s in Tesco.", "It's %s!")
stuff = ("New World Order", "funeral home", "tea", "toilet", "post office", "work canteen",
         "fish fingers", "Fenton pub", "salad bowl", "lemon juice", "helicopter cockpit",
         "DFS sale", "prison shower", "bolognese", "chistmas cake", "garden", "nude",
         "nearby branch of Tesco", "city of Whiterun", "dog's mouth", "spleen", "hotel towel",
         "cavernous arse of Alexander the Great", "martian rover", "photocopier outlet",
         "boot cupboard", "sellotape", "dogs mouth", "queen's ladygarden", "french mustard",
         "rotting turkey", "butthole of Santa", "dark one's testes", "nuclear waste barrel",
         "only copy of Half life 3", "last open Woolworths", "word of God", "ford fiesta",
         "nun's cleavage", "cop's gun holster", "punch bowl", "estate agent's dignity",
         "bag of haribo", "vegan restaurant", "latest episode of Corrie", "french toast",
         "maven repository", "burger van", "pointless stenching quagmire", "heart of darkness")
dang = ("Enough of", "Why", "How do you", "I never did", "No more", "Had my fill of",
        "Please stop the", "Less of the", "So much for", "And then", "Don't talk to me about",
        "We've run out of", "So then,", "Some more", "A new", "What's with",
        "Is there any point to", "Fine then.", "Someone likes", "I know all about",
        "Diseases are spread by", "What? Some", "Nothing but")
dong = ("So I said,", "Well he thought,", "I don't want", "He said to me,",
        "I never wanted to hear", "I asked for oil, I didn't say,", "Philosophy:",
        "Why all the,", "Never mind, I said,", "Fantasically,", "She retorted,", "Sad eh?")
celebline = ("I wish %s would %s %s!", "%s has %s'd in the %s. Disgraceful!",
             "I know %s is famous but %s a %s!", "%s, a classic %s %s", "Woo! %s #%s%s",
             "Fuck %s, I'm %sed off with all the %s.",
             "Right, so %s. You know what I think? #%s%s",
             "Nothing %s can say but, '%s %s!'",
             "Nothing against %s apart from %s and %s!",
             "No need for %s to be so %s for %s all the time.",
             "What does %s think of %s? I say %s!",
             "%s is my hero. Anyone who has a problem with that can %s %s!",
             "I love %s so much I could %s %s!",
             "I'm happy %s %s's %s! Yay!",
             "Nothing like %s to start the %s day. #%s",
             "The most important person alive is %s. Without %s we would %s.")
butscrewthis = ("But screw this", "Toss off", "Piles of", "Great, more", "Bugger", "No point in",
                "Loving the", "I can't live without", "I can still taste", "Oh, car full of",
                "Nobody minds my", "I don't understand", "floating", "flipping the bird to",
                "Loving the", "Sad about", "Why worry about", "Nothing gets past my")
noidea = ("No idea what this %s is about.", "This subject gets my %s.", "What a load of %s",
          "%s eh? I think", "What ever this %s hastag is about. Looks like", "Loving this %s",
          "Feeling good about %s.", "No %s on me!", "Wow! Fuck a %s!", "New %s please!",
          "Who made this %s up?", "People have been soaked in %s for less.")
proop = ("to", "and", "it's", "not too", "less than", "worse than", "the best", "I think",
         "A pile of", "Astoundingly", "Makes me so happy I could", "not particularly", "in",
         "similar to", "bog all like", "amazingly a real", "a disappointing", "sadly eqautes to",
         "a goddamn", "what's", "why", "close as arse to", "not", "as", "felchbugger a"
         "what's the point of")

#
# Time to construct the tweet
#
def construct_a_tweet():
    """
    Makes the tweet... the tweet u want
    """
    if random.randrange(20) < 9:
        #
        # check top 10 games and comment
        nooz = eval(random.choice(rss) + "()")
        tweet = "%s %s%s #%s%s" % (nooz, random.choice(superlative), random.choice(swear),
                                   random.choice(superlative), random.choice(swear))
    if random.randrange(20) < 5:
        #
        # check top 10 games and comment
        nooz = eval(random.choice(rss) + "()")
        tweet = random.choice(preposition) % nooz
    elif random.randrange(20) < 2:
        #
        # random mix of mail top words and swearing
        mail_guff = mailgen.younutter()
        mail_guff += swear
        tweet = "%s %s %s %s! %s %s? %s %s #%s%s" % (random.choice(mail_guff).capitalize(),
                                                     random.choice(mail_guff),
                                                     random.choice(mail_guff),
                                                     random.choice(mail_guff),
                                                     random.choice(mail_guff).capitalize(),
                                                     random.choice(mail_guff),
                                                     random.choice(mail_guff).capitalize(),
                                                     random.choice(mail_guff),
                                                     random.choice(mail_guff),
                                                     random.choice(mail_guff))
    elif random.randrange(20) < 3:
        #
        # check top 10 games and comment
        game = eval(random.choice(rss) + "(True)")
        tweet = "%s! %s%s %s %s #%s%s" % (game, random.choice(superlative), random.choice(swear),
                                          random.choice(proop), random.choice(swear),
                                          random.choice(superlative), random.choice(swear))
    elif random.randrange(20) < 5:
        #
        # check bbc world
        item = eval(random.choice(rss) + "(True)")
        blags = item.split(" ")
        blags[random.randrange(0, len(blags))] = random.choice(swear)
        tweet = " ".join(blags)
    elif random.randrange(20) < 8:
        #
        # check world news, replace a word
        item = eval(random.choice(rss) + "(True)")
        blags = item.split(" ")
        blags[random.randrange(0, len(blags))] = random.choice(swear)
        tweet = "%s. %s %s #%s" % (" ".join(blags), random.choice(butscrewthis),
                                   random.choice(swear), random.choice(swear))
    elif random.randrange(20) < 8:
        #
        # check low carb recipes
        item = eval(random.choice(rss) + "()")
        blags = item.split(" ")
        blags[random.randrange(0, len(blags))] = random.choice(swear)
        tweet = random.choice(celebline) % (" ".join(blags), random.choice(swear),
                                            random.choice(swear))

    elif random.randrange(20) < 3:
        #
        # check BBC Entertainment
        game = eval(random.choice(rss) + "()")
        tweet = "%s %s #%s%s" % (game, random.choice(swear),
                                 random.choice(superlative), random.choice(swear))
    elif random.randrange(20) < 7:
        #
        # check BBC World News
        game = eval(random.choice(rss) + "()")
        tweet = "%s%s! %s %s #%s%s" % (random.choice(superlative), random.choice(swear),
                                       game, random.choice(swear),
                                       random.choice(superlative), random.choice(swear))
    elif random.randrange(20) < 3:
        #
        # check top 10 dvds and comment
        dvd = eval(random.choice(rss) + "()")
        tweet = "%s! %s... %s%s %s %s #%s%s" % (random.choice(swear).capitalize(), dvd,
                                                random.choice(superlative), random.choice(swear),
                                                random.choice(proop), random.choice(swear),
                                                random.choice(superlative), random.choice(swear))
    elif random.randrange(20) < 3:
        #
        # check bbc world and comment
        dvd = eval(random.choice(rss) + "()")
        tweet = "%s %s... %s%s? %s %s #%s%s" % (random.choice(swear).capitalize(), dvd,
                                                random.choice(superlative), random.choice(swear),
                                                random.choice(proop), random.choice(swear),
                                                random.choice(superlative), random.choice(swear))
    elif random.randrange(20) < 5:
        #
        # grab some random bollocks from the Daily mail and comment oddly on it.
        crappo = mailgen.biglad()
        fksakedailymail = ("Fucking news..",
                           "I heard", "In the news: ", "", "What? Apparently ", "Sadly ")
        tweet = "%s'%s' I say %s %s %s %s #%s%s" % (random.choice(fksakedailymail), crappo[0],
                                                    random.choice(swear), crappo[1],
                                                    random.choice(swear), crappo[2],
                                                    crappo[3], random.choice(swear))
    elif random.randrange(20) < 9:
        #
        # Get a (hopefully) celebrities name from hollywood insider and use it in a tweet
        tweet = random.choice(celebline) % (celebgrab(), random.choice(swear), random.choice(swear))
    elif random.randrange(20) > 5:
        #
        # make a nonsense sentence out of popular words from The Mail and swearing.
        crappo = mailgen.biglad()
        blob = ("Nonsense!", "Yeah, right!", "Never", "Total Garbage if you ask me!",
                "And never a truer word..", "Fucks sake, eh?", "I need more pills.",
                "So there you go.", "I want it!", "CRYFACE!", "waaaaah", "HUNGREE!")
        tweet = "%s %s! %s %s %s %s. %s #%s%s" % (random.choice(swear).capitalize(), crappo[1],
                                                  random.choice(swear).capitalize(), crappo[2],
                                                  random.choice(swear), crappo[4],
                                                  random.choice(blob), crappo[3],
                                                  random.choice(swear))
    elif random.randrange(20) > 8:
        nooz = skynews()
        zoos = []
        for item in nooz.split(" "):
            zoos.append(item)
            zoos.append(random.choice(swear))
        zoos[-1] = "#%s" % zoos[-1]
        noo = " ".join(zoos)
        tweet = noo
    #     tweet = ""
    #     while len(tweet) < 150:
    #         tweet += "%s " % random.choice(swear)
    elif random.randrange(20) > 8:
        nooz = skynews()
        tweet = "%s %s %s? #%s%s" % (random.choice(swear), nooz, random.choice(swear),
                                     random.choice(superlative), random.choice(swear))
    else:
        nooz = nytimes()
        zoos = nooz.split(" ")
        zoos[random.randrange(len(zoos))] = random.choice(swear).strip()
        nooz = str(" ".join(zoos))
        tweet = "%s %s %s? %s! #%s" % (random.choice(superlative), 
                                       nooz, random.choice(swear),
                                       random.choice(superlative), random.choice(swear))

    return tweet
#
# use p after the python script for print test eg : SwearyRobot.py p or use an integer to print
# that number of messages out.
# You can used "dotweet" to bypass probability too
#     also extracted out so only run if main program as this is imported by the reply scraper.
if __name__ == "__main__":
    # if no argument set arg to no to prevent exceptions
    if len(sys.argv) > 1:
        ARG = str(sys.argv[1])
    else:
        ARG = str("no")
    # process command line option (if any)
    if ARG == "p":
        print(construct_a_tweet())
    elif ARG == "no":
        if random.randrange(50) < 5:
            tweeter = construct_a_tweet()
            API.update_status(tweeter)
    elif ARG == "dotweet":
        tweeter = construct_a_tweet()
        API.update_status(tweeter)
    else:
        try:
            number = int(ARG)
            for i in range(0, number):
                try:
                    print(construct_a_tweet())
                except Exception as exc:
                    print(str(exc))
                    EXC_T, EXC_O, EXC_TB = sys.exc_info()
                    fname = os.path.split(EXC_TB.tb_frame.f_code.co_filename)[1]
                    print(EXC_T, fname, EXC_TB.tb_lineno)
        except Exception as exc:
            print(str(exc))
            EXC_T, EXC_O, EXC_TB = sys.exc_info()
            fname = os.path.split(EXC_TB.tb_frame.f_code.co_filename)[1]
            print(EXC_T, fname, EXC_TB.tb_lineno)
            print("argument not understood - either:\n\t no argument to run normally,")
            print("\t 'dotweet' to ignore probabilities and just tweet\n\t'p' for print one or ")
            print("\tenter a number to print that many arguments")
