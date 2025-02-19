# test_app.py
from app import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b"Hello, this blog is about Building CI/CD Pipelines with Docker: A Hands-On Guide for Containerized Workflows

!"
