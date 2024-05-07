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
        posts = list(scrapedSub.new(limit = numPosts))
    elif sorting == "Hot":
        posts = list(scrapedSub.hot(limit = numPosts))
    elif sorting == "Top":
        posts = list(scrapedSub.top(limit = numPosts))
    elif sorting == "Controversial":
        posts = list(scrapedSub.controversial(limit = numPosts))


    # Print post titles
    print(f"\nTop {numPosts} {sorting} posts from r/{subredditName}:\n")
    counter = 0
    for post in posts:
        print(f"Post Title {counter}: ", post.title)
        counter += 1

    # Ask user if they want more information about a certain post
    # Get more information about the post if required
    correctNum = False
    while (not correctNum):
        postInterest = input("Would you like more information about any of the posts? Enter its number, or no: ")
        if postInterest == "no":
            break
        else:
            postInterest = int(postInterest)
            if postInterest < 1 or postInterest > numPosts:
                print(f"Your post number is out of bounds, enter a number from 0 to {numPosts}.")
                continue
            else:
                print(f"Post {postInterest} Title: {posts[postInterest].title}")
                # Output the post body if there is one
                if posts[postInterest].selftext:
                    print("-------------------------------")
                    print(f"{posts[postInterest].selftext}")
                    print("-------------------------------")
                print(f"Post {postInterest} Author: {posts[postInterest].author}")
                print(f"Post {postInterest} # of Upvotes: {posts[postInterest].score}")
                print(f"Post {postInterest} # of Comments: {posts[postInterest].num_comments}")
                print(f"Post {postInterest} awards received: {posts[postInterest].total_awards_received}")
                print(f"Post {postInterest} NSFW: {posts[postInterest].over_18}")

                # Get the top 10 comments
                comments = posts[postInterest].comments[:10]
                print(f"The top comments of post {postInterest} are: ")
                for comment in comments:
                    print(f"{comment.body}")


    again = input("\nWould you like to scrape another subreddit? (yes/no) ").strip().lower()
    if again != 'yes':
        running = False

