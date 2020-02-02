from math_func import StudentDB
import pytest

@pytest.fixture(scope='module')
def db():
    print('-------setup------')
    db = StudentDB()
    db.connect('data.json')
    return db

def test_tom_data(db):
    tom_data = db.get_data("Tom")
    assert tom_data ['id'] == 1
    assert tom_data['name'] == "Tom"
    assert tom_data['result'] == "pass"

def test_mac_data(db):
    mac_data = db.get_data("Mac")
    assert mac_data ['id'] == 2
    assert mac_data['name'] == "Mac"
    assert mac_data['result'] == "fail"
