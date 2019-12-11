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
    # submissions = [top_submissions, new_submissions, hot_submissions]
    all_submissions = []
    # all_submissions.extend(top_submissioins)
    for submission in top_submissions:
        submission_as_dict = {}
        submission_as_dict['title'] = submission.title
        # url
        # so on
        submission['category'] = 
        all_submissions.append(submission)

    for submission in new_submissions:
        submission_as_dict = {}
        submission_as_dict['title'] = submission.title
        # url
        # so on
        submission['category'] = 'new'
        all_submissions.append(submission)
    return all_submissions


        


    
    return top_submissions

def test_get_submissions():
    subreddit_name = 'learnpython'
    top_submissions = get_submissions(subreddit_name)
    for submission in top_submissions:
        assert submission.url
        assert submission.title


if __name__ == '__main__':
    subreddit_name = 'learnpython'
    top_submissions = get_submissions(subreddit_name)
    # print(top_su)
    # for submission in top_submissions:
        # print(type(submission))
        # print(dir(submission))
        # print(dict(submission))
        # print(submission._get_json_dict())
        # print(submission.json_dict)
        # time.sleep(1)
        # print(submission.title)
    for subreddit in subreddits:
        submissions = get_submissions(subreddit)
        for submission in submissions:
            submission_as_dict = create_dict_from_submission(submission)
            table.insert(submission_as_dict)