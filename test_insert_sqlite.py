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

def test_subreddit_column_general():
    result = db.query("SELECT subreddit FROM reddit_submissions GROUP BY subreddit")
    for row in result:
        subreddits = ['learnpython', 'funny', 'AskReddit', 'todayilearned', 'worldnews']
        assert row['subreddit'] in subreddits

def test_subreddit_column_specific():
        result = db.query("SELECT subreddit FROM reddit_submissions WHERE subreddit='learnpython'")
        for row in result:
                assert row['subreddit'] == 'learnpython'

def test_url():
        result = db.query("SELECT sub_url FROM reddit_submissions LIMIT 10")
        for row in result:
                assert 'https://' in row['sub_url']

def test_categories():
        result = db.query("SELECT category FROM reddit_submissions GROUP BY category")
        for row in result:
                if row['category'] == 'controversial':
                        assert row['category'] == 'controversial'
                elif row['category'] == 'hot':
                        assert row['category'] == 'hot'
                elif row['category'] == 'top':
                        assert row['category'] == 'top'
                elif row['category'] == 'new':
                        assert row['category'] == 'new'
                elif row['category'] == 'rising':
                        assert row['category'] == 'rising'

def test_categories_2():
        result = db.query("SELECT category FROM reddit_submissions GROUP BY category")
        categories = ['top', 'new', 'hot', 'rising', 'controversial']
        for row in result:
            assert row['category'] in categories

def test_datatypes():
        result = db.query("SELECT * from reddit_submissions LIMIT 1")
        for row in result:
                assert type(row['subreddit']) == str
                assert type(row['category']) == str
                assert type(row['sub_title']) == str
                assert type(row['sub_url']) == str
                assert type(row['sub_comms_num']) == int
                assert type(row['is_original_content']) == bool
                assert type(row['upvotes_percentage']) == float
                assert type(row['time_created_utc']) == float







