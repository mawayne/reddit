import time
import praw 
import dataset

reddit = praw.Reddit(
    client_id='tiHEaLH1D4ds-w', 
    client_secret='iMvbqDQxbW9FJIc5ZtH2bVuwAcY',
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')

def get_submissions(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    category_names = ['top', 'new', 'hot', 'rising', 'controversial']
    top = subreddit.top()
    new = subreddit.new()
    hot = subreddit.hot()
    rising = subreddit.rising()
    controversial = subreddit.controversial()
    all_category_submissions = [top, new, hot, rising, controversial]
    all_submissions = []
    time.sleep(1)
    for category_submissions in all_category_submissions:
        for category_name in category_names:
            category = category_name
        submissions = category_submissions
        for submission in submissions:
            submission_as_dict = {'subreddit': subreddit_name, 
                                'category': category, 
                                'sub_title': submission.title, 
                                'sub_url': submission.url,
                                'sub_id': submission.id,
                                'sub_score': submission.score,
                                'sub_comms_num': submission.num_comments,
                                #   'sub_author': submission.author,
                                'time_created_utc': submission.created_utc,
                                'is_original_content': submission.is_original_content,
                                'self_post': submission.is_self,
                                'sub_full_name': submission.name,
                                'over_18': submission.over_18,
                                'permalink': submission.permalink,
                                'sub_selftext': submission.selftext,
                                'sub_stickied': submission.stickied,
                                #   'sub_subreddit': submission.subreddit,
                                'upvote_ratio': submission.upvote_ratio
                                }
            all_submissions.append(submission_as_dict)
    return all_submissions       

subreddits = ['learnpython', 'funny', 'AskReddit', 'todayilearned', 'worldnews']

db = dataset.connect('sqlite:///test.db')
table = db['test2']

if __name__ == '__main__':
    for subreddit in subreddits:
        submissions = get_submissions(subreddit)
        for submission in submissions:
            table.insert(submission)