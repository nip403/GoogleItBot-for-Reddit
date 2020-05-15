import praw
import random

def search(phrase):
    return random.choice(["qqqq", "rrrrr", "ssss", "tttttt"])

def main():
    reddit = praw.Reddit(
        client_id="EeWPOWVvE4TLKA",
        client_secret="CTU1zRDpHalLtnv3xDgbGZgSJFo",
        username="googleitbot",
        password="googleitbot",
        user_agent="GoogleItBot (by /u/Nip403)"
    )

    subreddit = reddit.subreddit("bottest")
    keyphrase = "!googleit"

    for comment in subreddit.stream.comments():
        if keyphrase in comment.body:
            try:
                comment.reply(
                    f"Top 3 search results for: '{search_term}'" +\
                    search(comment.replace(keyphrase, ""))
                )

            except:
                pass

if __name__ == "__main__":
    main()
