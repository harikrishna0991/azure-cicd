
import sys
import os
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data
