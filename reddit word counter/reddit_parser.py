import praw
import simplejson
import string

import config

reddit = config.reddit
subreddit = config.subreddit

database = {}
x = 0

with open("database.json", "r") as file:
    database = simplejson.load(file)

for comment in subreddit.stream.comments(skip_existing=True):
    comment_body = comment.body.split()
    
    for word in comment_body:
        for punction in string.punctuation:
            if punction in word:
                word.replace(punction, "") # Sanatize inputs

        if not word in database:
            database.setdefault(word, {})
            database[word].setdefault("TOTAL_COUNT", 0)
        if not comment.subreddit.display_name in database[word]:
            database[word].setdefault(comment.subreddit.display_name, 0)
        
        database[word]["TOTAL_COUNT"] += 1
        database[word][comment.subreddit.display_name] += 1
    
    if x == 1000:
        print("Dumping to file ...")
        with open("database.json", "w") as file:
            simplejson.dump(database, file, indent="  ")
        x = 0
        print("Dumped!")
        
    x += 1