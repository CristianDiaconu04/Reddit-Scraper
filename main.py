import praw 
from sorting import Sorting

# Reddit API
reddit = praw.Reddit(
    client_id='wsmpPsB8AQWfgcYHgS8IyQ',
    client_secret='j6Sm_4n1Oy9XVMM59POsnZwO68EW9g',
    user_agent='MyRedditScraper',  # Describe your bot with a user agent
)

running = True

while running:
    subredditName = input("Which subreddit would you like to scrape? ")
    incorrectSorting = True
    
    # Get the sorting type
    while incorrectSorting:
        sorting = input("What would you like to sort by? Options are New, Hot, Top, or Controversial: ") # Has to be one of New, Hot, Top, Controversial
        if sorting == "New" or sorting == "Hot" or sorting == "Top" or sorting == "Controversial":
            incorrectSorting = False
        else:
            print("Incorrect choice")

    numPosts = input("How many posts would you like? ")


    if sorting == "New":
        
    elif sorting == "Hot":

    elif sorting == "Top":

    elif sorting == "Controversial":

    


