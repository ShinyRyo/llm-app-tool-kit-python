from starlette.testclient import TestClient
from src.main import app
import os

client = TestClient(app)


def test_cors_for_allowed_origin():
    """許可されたオリジンからのリクエストが成功することを確認するテスト"""
    response = client.get("/", headers={"origin": os.getenv("DEVELOPMENT_URL")})
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert "access-control-allow-origin" in response.headers


def test_cors_for_disallowed_origin():
    """許可されていないオリジンからのリクエストが失敗することを確認するテスト"""
    response = client.get("/", headers={"origin": "http://unauthorized-origin.com"})
    assert response.status_code == 200
    assert "access-control-allow-origin" not in response.headers
