import praw 
import dataset

reddit = praw.Reddit(client_id='tiHEaLH1D4ds-w', client_secret='iMvbqDQxbW9FJIc5ZtH2bVuwAcY', user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')

sub_names = ['learnpython', 'funny', 'AskReddit', 'todayilearned', 'worldnews']
# sub_names = ['learnpython', 'funny', 'askreddit', 'todayilearned', 'worldnews']

for sub in sub_names:
    # print(sub)
    subreddit = reddit.subreddit(sub)
    print(type(subreddit))
# Cannot use attribute subreddit on a list

# learn_python = reddit.subreddit('learnpython')
# funny = reddit.subreddit('funny')
# askreddit = reddit.subreddit('AskReddit')
# todayilearned = reddit.subreddit('todayilearned')
# worldnews = reddit.subreddit('world_news')

# subreddits = [learn_python, funny, askreddit, todayilearned, worldnews]

# top_python_learn = subreddit.top()
# for subreddit in subreddits:
#     new_submissions = subreddit.new() 
#     top_submissions = subreddit.top()
#     hot_submissions = subreddit.hot()
#     rising_submissions = subreddit.rising()
#     gilded_submissions = subreddit.gilded()
#     controversial_submissions = subreddit.controversial()

# submissions_lists = [new_submissions, top_submissions, hot_submissions, rising_submissions, gilded_submissions, controversial_submissions]

# # for submission_list in submissions_lists:
# #     for submission in submission_list:

# db = dataset.connect('sqlite:///reddit_learnpython.db')
# # # table = db['reddit_submissions']
# table = db['test_2']

# if __name__ == '__main__':
#     for submission in submissions:
#         sub_title = submission.title
#         sub_url = submission.url
#         sub_id = submission.id
#         sub_score = submission.score
#         sub_comms_num = submission.num_comments
#         table.insert(dict(title=sub_title, url=sub_url, sub_id=sub_id, score=sub_score, comms_num=sub_comms_num))