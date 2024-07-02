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
