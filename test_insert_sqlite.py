import dataset
import pytest

db = dataset.connect('sqlite:///sqlite_testing.db')
table = db['reddit_submissions']



def test_len_table():
    len_table = len(table)
    assert len_table == 3144

def test_table_columns():
     assert table.columns == ['id', 'subreddit', 'category', 'sub_title', 'sub_url', 'sub_id', 'sub_score', 'sub_comms_num', 'sub_author', 'time_created_utc', 'is_original_content', 'self_post', 'sub_full_name', 'nsfw', 'permalink', 'sub_selftext', 'sub_stickied', 'sub_subreddit', 'upvotes_percentage']

def test_row_datatype():
    for row in table:
        assert str(type(row)) == "<class 'collections.OrderedDict'>"

# def test_upvotes_percentage:
# result = 


# def test_upload_reddit_users():
#     test_table_columns = 


# def test_
# result = db.query('SELECT sub_comms_num, COUNT(*) scm FROM test ORDER BY scm DESC')
# print(result)


