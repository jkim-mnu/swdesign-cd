from app import app

def test_health():
    assert app.test_client().get("/health").data == b"ok\n"

def test_home_shows_version():
    assert b"v0." in app.test_client().get("/").data
