from src.agent.function_calling.apis.crypts import execute_agent
import pytest

def test_get_current_weather():
    result = execute_agent("東京の天気を教えて")
    assert result is not ""
    print(result)
