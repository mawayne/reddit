import praw 
import dataset
import json

reddit = praw.Reddit(client_id='tiHEaLH1D4ds-w', client_secret='iMvbqDQxbW9FJIc5ZtH2bVuwAcY', user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
subreddit = reddit.subreddit('learnpython')
top_python_learn = subreddit.top()

for submission in top_python_learn:
    title = submission.title
    score = submission.score
    sub_id = submission.id
    url = submission.url
    comms_num = submission.num_comments
    top_learn_python_dict = { "title": title, "score": score, "id": sub_id, "url": url, "comms_num": comms_num}
    # print(type(top_learn_python_dict))
    # print(top_learn_python_dict)
    # db = dataset.connect('sqlite:///reddit_learnpython.db')
    # table = db['top posts']
    # table.insert(top_learn_python_dict)
    # return top_learn_python_dict
    # print(title)
    # print(score)
    # print(sub_id)
    # print(url)
    # print(comms_num)

# def get_reddit_submissions():
#     for submission in submissions:
#         title = submission.title
#         score = submission.score
#         sub_id = submission.id
#         url = submission.url
#         comms_num = submission.num_comments
#         reddit_submission = {"title": title, "score": score, "id": sub_id, "url": url, "comms_num": comms_num}
#     return submission

# for submission in submissions:
#     title = submission.title
#     score = submission.score
#     sub_id = submission.id
#     url = submission.url
#     comms_num = submission.num_comments
# print(submission)


# top_learn_python_dict = { "title":[], \
#                             "score":[], \
#                             "id":[], \
#                             "url":[], \
#                             "comms_num": []}

# for submission in submissions:
#     top_learn_python_dict["title"].append(submission.title)
#     top_learn_python_dict["score"].append(submission.score)
#     top_learn_python_dict["id"].append(submission.id)
#     top_learn_python_dict["url"].append(submission.url)
#     top_learn_python_dict["comms_num"].append(submission.num_comments)

if __name__ == '__main__':
    for dict in top_learn_python_dict:
        # print(type(top_learn_python_dict))
        # print(top_learn_python_dict)
        db = dataset.connect('sqlite:///reddit_learnpython.db')
        table = db['top posts']
        table.insert(dict)

    
    # db = dataset.connect('sqlite:///reddit_learnpython.db')
    # table = db['top posts']
    # table.insert(json.loads(title))
    # table.insert(json.loads(score))
    # table.insert(json.loads(sub_id))
    # table.insert(json.loads(url))
    # table.insert(json.loads(comms_num))


    
    # reddit_submissions = get_reddit_submissions()
    # print(reddit_submissions)

    # top_learn_python_dict = build_reddit_submissions()
    # print(top_learn_python_dict)
    # print(type(top_learn_python_dict))

    # dict = get_reddit_submissions()
    # print(dict)
