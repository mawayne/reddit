import praw 
import dataset

reddit = praw.Reddit(client_id='tiHEaLH1D4ds-w', client_secret='iMvbqDQxbW9FJIc5ZtH2bVuwAcY', user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
subreddit = reddit.subreddit('learnpython')
top_python_learn = subreddit.top()

db = dataset.connect('sqlite:///reddit_learnpython.db')
# table = db['top posts']
# table = db['r/learnpython top posts']
table = db['test']

if __name__ == '__main__':
    for submission in top_python_learn:
        sub_title = submission.title
        sub_url = submission.url
        sub_id = submission.id
        sub_score = submission.score
        sub_comms_num = submission.num_comments
        print(sub_title)
        print(sub_url)
        print(sub_id)
        print(sub_score)
        print(sub_comms_num)
        table.insert(dict(title=sub_title, url=sub_url, sub_id=sub_id, score=sub_score, comms_num=sub_comms_num))
        # table.insert(dict(url=sub_url))
        # table.insert(dict(sub_id=sub_id))
        # table.insert(dict(score=sub_score))
        # table.insert(dict(comms_num=sub_comms_num))
        







    # print(type(top_learn_python_dict))
    # print(top_learn_python_dict)
    # table.insert(dict(title=title, score=score, id=sub_id, url=url, comms_num=comms_num))
    
    # reddit_submissions = get_reddit_submissions()
    # print(reddit_submissions)

    # top_learn_python_dict = build_reddit_submissions()
    # print(top_learn_python_dict)
    # print(type(top_learn_python_dict))

    # dict = get_reddit_submissions()
    # print(dict)
