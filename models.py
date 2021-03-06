class User:
    def __init__(self, id, name, screen_name, profile_image, friends_count, followers_count, statuses_count, favourites_count, listed_count, verified):
        self.id = id
        self.name = name
        self.screen_name = screen_name
        self.profile_image = profile_image
        self.friends_count = friends_count
        self.followers_count = followers_count
        self.statuses_count = statuses_count
        self.favourites_count = favourites_count
        self.listed_count = listed_count
        self.verified = verified

class Session:
    def __init__(self, id, user, timestamp, mk_turk):
        self.id = id
        self.user = user
        self.timestamp = timestamp
        self.mk_turk = mk_turk

class Tweet:
    def __init__(self, id, text, retweet_count, user, selected):
        self.id = id
        self.text = text
        self.retweet_count = retweet_count
        self.user = user
        self.selected = selected

    def getDisplayText(self):
        tokens = self.text.split(" ")
        words = []
        for token in tokens:
            word = ""
            if token.startswith("http"):
                word='<a target="_blank" href="'+token+'" class="link">'+token+'</a>'
            elif token.startswith("@"):
                word='<a target="_blank" href="https://twitter.com/'+token.replace("@","")+'" class="link">'+token+'</a>'
            elif token.startswith("#"):
                word = '<a target="_blank" href="https://twitter.com/search?q=%23'+token.replace("#","")+'&src=hash" class="link">'+token+'</a>'
            else:
                word = token
            words.append(word)
        return " ".join(words)
            
class Timeline:
    def __init__(self):
        self.tweets = []
    def add_tweet(self, tweet):
        self.tweets.append(tweet)

class Question:
    def __init__(self, session, number, timeline):
        self.session = session
        self.number = number
        self.timeline = timeline
