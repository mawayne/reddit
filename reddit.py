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
    gilded_submissions = subreddit.gilded()
    controversial_submissions = subreddit.controversial()
    all_submissions = []
    time.sleep = 1
    for submission in top_submissions:
        submission_as_dict = {}
        submission_as_dict['subreddit'] = subreddit_name
        submission_as_dict['category'] = 'top'
        submission_as_dict['sub_title'] = submission.title
        submission_as_dict['sub_url'] = submission.url
        submission_as_dict['sub_id'] = submission.id 
        submission_as_dict['sub_score'] = submission.score
        submission_as_dict['sub_comms_num'] = submission.num_comments
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
        all_submissions.append(submission_as_dict)       
    return all_submissions

def test_get_submissions():
    subreddit_name = 'learnpython'
    top_submissions = get_submissions(subreddit_name)
    for submission in top_submissions:
        assert submission.title
        assert submission.url
        assert submission.id
        assert submission.score
        assert submission.num_comments
        
subreddits = ['learnpython', 'funny', 'AskReddit', 'todayilearned', 'worldnews']

db = dataset.connect('sqlite:///reddit_learnpython.db')
table = db['test_13']



if __name__ == '__main__':
    for subreddit in subreddits:
        submissions = get_submissions(subreddit)
        for submission in submissions:
            table.insert(submission)