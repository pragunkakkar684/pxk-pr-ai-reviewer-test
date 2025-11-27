from app.security import weak_hash

def test_hash():
    assert weak_hash("test")
