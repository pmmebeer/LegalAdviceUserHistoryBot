import config
import praw
from collections import defaultdict

reddit = praw.Reddit(
    user_agent = config.user_agent,
    client_id = config.client_id,
    client_secret = config.client_secret,
    )

warning_subreddits = ['raisedbynarcissists',
                      'relationships',
                      'freeuse',
                      'trees',
                      'drugs',
                      'darknetmarkets',
                      'relationships',
                      'rbnlegaladvice',
                      'theredpill',
                      'legaladviceinaction',
                      'imgoingtohellforthis',
                      'drama',
                      'shitredditsays',
                      'bad_cop_no_donut',
                      'mensrights',
                      'kotakuinaction',
                      'incels',
                      'redpillwomen',
                      'mgtow',
                      'justnomil']
warning_sub_dict_comments = defaultdict(int)
warning_sub_dict_posts = defaultdict(int)

political_subreddits = ['enoughtrumpspam',
                        'the_donald',
                        'libertarian',
                        'politics',
                        'hillaryclinton',
                        'libertarian',
                        'sandersforpresident',
                        'political_revolution']
political_sub_dict_comments = defaultdict(int)
political_sub_dict_posts = defaultdict(int)

def comment_check():

    for comment in reddit.redditor(lookup_user).comments.new(limit=900):
        if comment.subreddit in warning_subreddits:
            warning_sub_dict_comments[str(comment.subreddit)] += 1
        elif comment.subreddit in political_subreddits:
            political_sub_dict_comments[str(comment.subreddit)] += 1
    if warning_sub_dict_comments is True or political_sub_dict_comments is True:
        print("Commented in:")

    for k, v in warning_sub_dict_comments.items():
        if v != 0:
            print("    " + k, v)

    for k, v in political_sub_dict_comments.items():
        if v != 0:
            print ("    " + k, v)

def submission_check():

    for submission in reddit.redditor(lookup_user).submissions.new(limit=100):
        if submission.subreddit in warning_subreddits:
            warning_sub_dict_posts[str(submission.subreddit)] += 1
        elif submission.subreddit in political_subreddits:
            political_sub_dict_posts[str(submission.subreddit)] += 1
    if warning_sub_dict_posts is True or political_sub_dict_posts is True:
        print("Posted to:")

    for k, v in warning_sub_dict_posts.items():
        if v != 0:
            print("    " + k, v)

    for k, v in political_sub_dict_posts.items():
        if v != 0:
            print ("    " + k, v)

subreddit = reddit.subreddit('legaladvice')
for submission in subreddit.stream.submissions():
    lookup_user = str(submission.author)

    print("User: " + lookup_user)
    print("Submission Title: " + str(submission.title))
    print("Submission Link: " + str(submission.shortlink))

    comment_check()
    submission_check()

    warning_sub_dict_comments.clear()
    warning_sub_dict_posts.clear()
    political_sub_dict_comments.clear()
    political_sub_dict_posts.clear()

    print("\n")


