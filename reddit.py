import time
import praw 
import dataset

reddit = praw.Reddit(
    client_id='tiHEaLH1D4ds-w', 
    client_secret='iMvbqDQxbW9FJIc5ZtH2bVuwAcY',
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')

def get_submissions(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    top_submissions = subreddit.top()
    new_submissions = subreddit.new()
    hot_submissions = subreddit.hot()
    rising_submissions = subreddit.rising()
    controversial_submissions = subreddit.controversial()
    all_submissions = []
    time.sleep(1)
    for submission in top_submissions:
        submission_as_dict = {}
        submission_as_dict['subreddit'] = subreddit_name
        submission_as_dict['category'] = 'top'
        submission_as_dict['sub_title'] = submission.title
        submission_as_dict['sub_url'] = submission.url
        submission_as_dict['sub_id'] = submission.id 
        submission_as_dict['sub_score'] = submission.score
        submission_as_dict['sub_comms_num'] = submission.num_comments
        # submission_as_dict['sub_author'] = submission.author
        submission_as_dict['time_created_utc'] = submission.created_utc 
        submission_as_dict['is_original_content'] = submission.is_original_content
        submission_as_dict['self_post'] = submission.is_self
        submission_as_dict['sub_full_name'] = submission.name
        submission_as_dict['nsfw'] = submission.over_18
        submission_as_dict['permalink'] = submission.permalink
        submission_as_dict['sub_selftext'] = submission.selftext
        submission_as_dict['sub_stickied'] = submission.stickied
        # submission_as_dict['sub_subreddit'] = submission.subreddit
        submission_as_dict['upvotes_percentage'] = submission.upvote_ratio
        all_submissions.append(submission_as_dict)
    for submission in new_submissions:
        submission_as_dict = {}
        submission_as_dict['subreddit'] = subreddit_name
        submission_as_dict['category'] = 'new'
        submission_as_dict['sub_title'] = submission.title
        submission_as_dict['sub_url'] = submission.url
        submission_as_dict['sub_id'] = submission.id 
        submission_as_dict['sub_score'] = submission.score
        submission_as_dict['sub_comms_num'] = submission.num_comments
        # submission_as_dict['sub_author'] = submission.author
        submission_as_dict['time_created_utc'] = submission.created_utc 
        submission_as_dict['is_original_content'] = submission.is_original_content
        submission_as_dict['self_post'] = submission.is_self
        submission_as_dict['sub_full_name'] = submission.name
        submission_as_dict['nsfw'] = submission.over_18
        submission_as_dict['permalink'] = submission.permalink
        submission_as_dict['sub_selftext'] = submission.selftext
        submission_as_dict['sub_stickied'] = submission.stickied
        # submission_as_dict['sub_subreddit'] = submission.subreddit
        submission_as_dict['upvotes_percentage'] = submission.upvote_ratio
        all_submissions.append(submission_as_dict)
    for submission in hot_submissions:
        submission_as_dict = {}
        submission_as_dict['subreddit'] = subreddit_name
        submission_as_dict['category'] = 'hot'
        submission_as_dict['sub_title'] = submission.title
        submission_as_dict['sub_url'] = submission.url
        submission_as_dict['sub_id'] = submission.id 
        submission_as_dict['sub_score'] = submission.score
        submission_as_dict['sub_comms_num'] = submission.num_comments
        # submission_as_dict['sub_author'] = submission.author
        submission_as_dict['time_created_utc'] = submission.created_utc 
        submission_as_dict['is_original_content'] = submission.is_original_content
        submission_as_dict['self_post'] = submission.is_self
        submission_as_dict['sub_full_name'] = submission.name
        submission_as_dict['nsfw'] = submission.over_18
        submission_as_dict['permalink'] = submission.permalink
        submission_as_dict['sub_selftext'] = submission.selftext
        submission_as_dict['sub_stickied'] = submission.stickied
        # submission_as_dict['sub_subreddit'] = submission.subreddit
        submission_as_dict['upvotes_percentage'] = submission.upvote_ratio
        all_submissions.append(submission_as_dict)
    for submission in rising_submissions:
        submission_as_dict = {}
        submission_as_dict['subreddit'] = subreddit_name
        submission_as_dict['category'] = 'rising'
        submission_as_dict['sub_title'] = submission.title
        submission_as_dict['sub_url'] = submission.url
        submission_as_dict['sub_id'] = submission.id 
        submission_as_dict['sub_score'] = submission.score
        submission_as_dict['sub_comms_num'] = submission.num_comments
        # submission_as_dict['sub_author'] = submission.author
        submission_as_dict['time_created_utc'] = submission.created_utc 
        submission_as_dict['is_original_content'] = submission.is_original_content
        submission_as_dict['self_post'] = submission.is_self
        submission_as_dict['sub_full_name'] = submission.name
        submission_as_dict['nsfw'] = submission.over_18
        submission_as_dict['permalink'] = submission.permalink
        submission_as_dict['sub_selftext'] = submission.selftext
        submission_as_dict['sub_stickied'] = submission.stickied
        # submission_as_dict['sub_subreddit'] = submission.subreddit
        submission_as_dict['upvotes_percentage'] = submission.upvote_ratio
        all_submissions.append(submission_as_dict)
    for submission in controversial_submissions:
        submission_as_dict = {}
        submission_as_dict['subreddit'] = subreddit_name
        submission_as_dict['category'] = 'controversial'
        submission_as_dict['sub_title'] = submission.title
        submission_as_dict['sub_url'] = submission.url
        submission_as_dict['sub_id'] = submission.id 
        submission_as_dict['sub_score'] = submission.score
        submission_as_dict['sub_comms_num'] = submission.num_comments
        # submission_as_dict['sub_author'] = submission.author - Author attribute creates it's own instance (refer to notes in Notion) - figure out how to add to table.
        submission_as_dict['time_created_utc'] = submission.created_utc 
        submission_as_dict['is_original_content'] = submission.is_original_content
        submission_as_dict['self_post'] = submission.is_self
        submission_as_dict['sub_full_name'] = submission.name
        submission_as_dict['nsfw'] = submission.over_18
        submission_as_dict['permalink'] = submission.permalink
        submission_as_dict['sub_selftext'] = submission.selftext
        submission_as_dict['sub_stickied'] = submission.stickied
        # submission_as_dict['sub_subreddit'] = submission.subreddit - Subreddit attribute creates it's own instance (refer to notes in Notion) - figure out how to add to table.
        submission_as_dict['upvotes_percentage'] = submission.upvote_ratio
        all_submissions.append(submission_as_dict)       
    return all_submissions

# def add_submissions(subreddit_name):
#     subreddit = reddit.subreddit(subreddit_name)
#     top_submissions = subreddit.top()
#     new_submissions = subreddit.new()
#     hot_submissions = subreddit.hot()
#     rising_submissions = subreddit.rising()
#     controversial_submissions = subreddit.controversial()
#     all_added_submissions = []
#     time.sleep = 1
#     for submission in top_submissions:
#         submission_as_dict = {}

#         all_added_submissions.append(submission_as_dict)       
#     for submission in new_submissions:
#         submission_as_dict = {}
#         submission_as_dict['sub_author'] = submission.author
#         submission_as_dict['time_created_utc'] = submission.created_utc 
#         submission_as_dict['is_original_content'] = submission.is_original_content
#         submission_as_dict['self_post'] = submission.is_self
#         submission_as_dict['sub_full_name'] = submission.name
#         submission_as_dict['nsfw'] = submission.over_18
#         submission_as_dict['permalink'] = submission.permalink
#         submission_as_dict['sub_selftext'] = submission.selftext
#         submission_as_dict['sub_stickied'] = submission.stickied
#         submission_as_dict['sub_subreddit'] = submission.subreddit
#         submission_as_dict['upvotes_percentage'] = submission.upvote_ratio
#         all_added_submissions.append(submission_as_dict)
#     for submission in hot_submissions:
#         submission_as_dict = {}
#         submission_as_dict['sub_author'] = submission.author
#         submission_as_dict['time_created_utc'] = submission.created_utc 
#         submission_as_dict['is_original_content'] = submission.is_original_content
#         submission_as_dict['self_post'] = submission.is_self
#         submission_as_dict['sub_full_name'] = submission.name
#         submission_as_dict['nsfw'] = submission.over_18
#         submission_as_dict['permalink'] = submission.permalink
#         submission_as_dict['sub_selftext'] = submission.selftext
#         submission_as_dict['sub_stickied'] = submission.stickied
#         submission_as_dict['sub_subreddit'] = submission.subreddit
#         submission_as_dict['upvotes_percentage'] = submission.upvote_ratio
#         all_added_submissions.append(submission_as_dict)
#     for submission in rising_submissions:
#         submission_as_dict = {}
#         submission_as_dict['sub_author'] = submission.author
#         submission_as_dict['time_created_utc'] = submission.created_utc 
#         submission_as_dict['is_original_content'] = submission.is_original_content
#         submission_as_dict['self_post'] = submission.is_self
#         submission_as_dict['sub_full_name'] = submission.name
#         submission_as_dict['nsfw'] = submission.over_18
#         submission_as_dict['permalink'] = submission.permalink
#         submission_as_dict['sub_selftext'] = submission.selftext
#         submission_as_dict['sub_stickied'] = submission.stickied
#         submission_as_dict['sub_subreddit'] = submission.subreddit
#         submission_as_dict['upvotes_percentage'] = submission.upvote_ratio
#         all_added_submissions.append(submission_as_dict)
#     for submission in controversial_submissions:
#         submission_as_dict = {}
#         submission_as_dict['sub_author'] = submission.author
#         submission_as_dict['time_created_utc'] = submission.created_utc 
#         submission_as_dict['is_original_content'] = submission.is_original_content
#         submission_as_dict['self_post'] = submission.is_self
#         submission_as_dict['sub_full_name'] = submission.name
#         submission_as_dict['nsfw'] = submission.over_18
#         submission_as_dict['permalink'] = submission.permalink
#         submission_as_dict['sub_selftext'] = submission.selftext
#         submission_as_dict['sub_stickied'] = submission.stickied
#         submission_as_dict['sub_subreddit'] = submission.subreddit
#         submission_as_dict['upvotes_percentage'] = submission.upvote_ratio
#         all_added_submissions.append(submission_as_dict)
#     return all_added_submissions

subreddits = ['learnpython', 'funny', 'AskReddit', 'todayilearned', 'worldnews']

db = dataset.connect('sqlite:///sqlite_testing.db')
table = db['reddit_submissions']

if __name__ == '__main__':
    for subreddit in subreddits:
        submissions = get_submissions(subreddit)
        for submission in submissions:
            table.insert(submission)
    # for subreddit in subreddits:
    #     submissions = add_submissions(subreddit)
    #     for submission in submissions:
    #         table.insert(submission)
    
