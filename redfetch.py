import praw 
import dataset
from stuf import stuf

reddit = praw.Reddit(client_id='tiHEaLH1D4ds-w', client_secret='iMvbqDQxbW9FJIc5ZtH2bVuwAcY', user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')

# sub_names = ['learnpython', 'funny', 'AskReddit', 'todayilearned', 'worldnews']
# sub_names = ['learnpython', 'funny', 'askreddit', 'todayilearned', 'worldnews']

# for sub in sub_names:
#     subreddit = reddit.subreddit(sub_names)
#     print(subreddit)
# Cannot use attribute subreddit on a list

learn_python_submissions = reddit.subreddit('learnpython')
funny_submissions = reddit.subreddit('funny')
askreddit_submissions = reddit.subreddit('AskReddit')
todayilearned_submissions = reddit.subreddit('todayilearned')
worldnews_submissions = reddit.subreddit('world_news')

submissions_list = [ learn_python_submissions, funny_submissions, askreddit_submissions, todayilearned_submissions, worldnews_submissions]

# subreddit = reddit.subreddit('learnpython')


# top_python_learn = subreddit.top()


# db = dataset.connect('sqlite:///reddit_learnpython.db')
# table = db['reddit_submissions']


# if __name__ == '__main__':
#     for submission in top_python_learn:
#         sub_title = submission.title
#         sub_url = submission.url
#         sub_id = submission.id
#         sub_score = submission.score
#         sub_comms_num = submission.num_comments
#         table.insert(dict(title=sub_title, url=sub_url, sub_id=sub_id, score=sub_score, comms_num=sub_comms_num))