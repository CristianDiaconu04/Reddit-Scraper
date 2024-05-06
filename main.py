import praw 

# Reddit API
reddit = praw.Reddit(
    client_id='wsmpPsB8AQWfgcYHgS8IyQ',
    client_secret='j6Sm_4n1Oy9XVMM59POsnZwO68EW9g',
    user_agent='MyRedditScraper',  # Describe your bot with a user agent
)

running = True

while running:
    subreddit = input("Which subreddit would you like to scrape?")
