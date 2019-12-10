import pytest 
import praw 
import dataset

reddit = praw.Reddit(client_id='tiHEaLH1D4ds-w', client_secret='iMvbqDQxbW9FJIc5ZtH2bVuwAcY', user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
subreddit = reddit.subreddit('learnpython')
submissions = subreddit.top()

top_learn_python_list = []

def test_list():
    for submission in submissions:
        top_learn_python_list.append(submission.title)
        top_learn_python_list.append(submission.score)
        top_learn_python_list.append(submission.id)
        top_learn_python_list.append(submission.url)
        top_learn_python_list.append(submission.num_comments)
    assert type(top_learn_python_list) == list 
    assert type(top_learn_python_list[3]) == str


