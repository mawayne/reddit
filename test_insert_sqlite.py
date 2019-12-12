import dataset
from stuf import stuf
import pytest

db = dataset.connect('sqlite:///sqlite_testing.db', row_type=stuf)
table = db['reddit_submissions']

def test_len_table():
    len_table = len(table)
    assert len_table == 3144

def test_table_columns():
     assert table.columns == ['id', 'subreddit', 'category', 'sub_title', 'sub_url', 'sub_id', 'sub_score', 'sub_comms_num', 'sub_author', 'time_created_utc', 'is_original_content', 'self_post', 'sub_full_name', 'nsfw', 'permalink', 'sub_selftext', 'sub_stickied', 'sub_subreddit', 'upvotes_percentage']

def test_row_datatype():
    for row in table:
        assert str(type(row)) == "<class 'stuf.core.stuf'>"

def test_subreddit_column():
        result = db.query("SELECT subreddit FROM reddit_submissions WHERE subreddit='learnpython'")
        for row in result:
                assert row['subreddit'] == 'learnpython'

def test_url():
        result = db.query("SELECT sub_url FROM reddit_submissions LIMIT 10")
        for row in result:
                assert 'https://' in row['sub_url']


 
# def test_upload_reddit_users():
#     test_table_columns = 


# def test_
# result = db.query('SELECT sub_comms_num, COUNT(*) scm FROM test ORDER BY scm DESC')
# print(result)


