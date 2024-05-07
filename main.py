import praw

# Reddit API
redditAPI = praw.Reddit(
    client_id='wsmpPsB8AQWfgcYHgS8IyQ',
    client_secret='j6Sm_4n1Oy9XVMM59POsnZwO68EW9g',
    user_agent='MyRedditScraper',
)

running = True

while running:
    subredditName = input("Which subreddit would you like to scrape? ")
    incorrectSorting = True
    
    # Get the sorting type
    while incorrectSorting:
        sorting = input("What would you like to sort by? (new/hot/top/controversial) ").strip().capitalize() 
        if sorting in ["New", "Hot", "Top", "Controversial"]:
            incorrectSorting = False
        else:
            print("Incorrect choice")

    numPosts = input("How many posts would you like? ")
    numPosts = int(numPosts)

    # This is the variable of the actual subreddit
    scrapedSub = redditAPI.subreddit(subredditName)

    if sorting == "New":
        posts = scrapedSub.new(limit=numPosts)
    elif sorting == "Hot":
        posts = scrapedSub.hot(limit=numPosts)
    elif sorting == "Top":
        posts = scrapedSub.top(limit=numPosts)
    elif sorting == "Controversial":
        posts = scrapedSub.controversial(limit=numPosts)


    # Print post titles
    print(f"\nTop {numPosts} {sorting} posts from r/{subredditName}:\n")
    for post in posts:
        print("Post Title: ", post.title)

    again = input("\nWould you like to scrape another subreddit? (yes/no) ").strip().lower()
    if again != 'yes':
        running = False

