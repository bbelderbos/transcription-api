from unittest.mock import patch

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


@patch("app.create_summary_of_transcript")
def test_summary_endpoint(marvinai_mock):
    marvinai_mock.return_value = "A summary"
    response = client.post(
        "/summarize", json={"transcript": "Hello World, this is a test"}
    )
    assert response.status_code == 200
    assert response.json() == {"summary": "A summary"}


@patch("app.extract_keywords_from_transcript")
def test_keywords_endpoint(marvinai_mock):
    marvinai_mock.return_value = ["rust", "performance", "safety"]
    response = client.post(
        "/keywords",
        json={"transcript": "Welcome to this intro on Rust...", "number": 3},
    )
    assert response.status_code == 200
    assert response.json() == {"keywords": ["rust", "performance", "safety"]}


@patch("app.create_social_media_posts")
def test_social_media_posts_endpoint(marvinai_mock):
    marvinai_mock.return_value = ["post 1", "post 2"]
    response = client.post(
        "/social-media-posts",
        json={"transcript": "Welcome to this intro on Rust...", "number": 2},
    )
    assert response.status_code == 200
    assert response.json() == {"posts": ["post 1", "post 2"]}
