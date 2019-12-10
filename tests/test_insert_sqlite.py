import dataset
import pytest

db = dataset.connect('sqlite:///reddit_learnpython.db')
table = db['r/learnpython top']

def test_len_table():
    len_db = len(table)
    assert len_db == 100

def test_table_columns():
    assert table.columns == ['id', 'title', 'url', 'sub_id', 'score', 'comms_num']

def test_row_datatype():
    for row in table:
        assert str(type(row)) == "<class 'collections.OrderedDict'>"

