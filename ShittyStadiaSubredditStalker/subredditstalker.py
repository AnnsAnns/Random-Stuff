from dhooks import Webhook, Embed
import praw

reddit = praw.Reddit("CREDENTIALS")

subreddit = reddit.subreddit("Stadia")

hook = Webhook("WEBHOOK")

for submission in subreddit.stream.submissions(skip_existing=True):
    try:
        embed = Embed(description=f"Hey, ????? du Zerstörerin ;^)! {submission.title}", color=0xfc14ff)

        embed.add_field(name="Link:", value=f"https://reddit.com{str(submission.permalink)}")
        
        hook.send(embed=embed)
    except:
        pass
    finally:
        hook.send(f"Insta-Link: https://reddit.com{str(submission.permalink)}")
        hook.send("<@!141532589725974528>")