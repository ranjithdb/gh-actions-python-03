from app import fetch_api_response

def test_fetch_api_response(monkeypatch):
    """Mock API response for testing."""
    class MockResponse:
        status_code = 200
        def json(self):
            return {"id": 1, "title": "Test API Response"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    response = fetch_api_response("https://fakeapi.com/data")
    assert response is not None
    assert isinstance(response, dict)
    assert response["title"] == "Test API Response"
