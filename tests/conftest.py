"""
Filename:
    conftest.py
"""
import pytest
from website import create_app

@pytest.fixture
def app():
    """Create and configure a test Flask application"""
    app = create_app({
        'TESTING': True,
        'WEATHER_API_KEY': 'test_weather_key',
        'GOOGLE_MAP_KEY': 'test_google_key'
    })
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    """Create a test client for the app"""
    return app.test_client()

@pytest.fixture
def mock_weather_response():
    """Sample weather API response data"""
    return {
        "coord": {"lat": 51.5074, "lon": -0.1278},
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "main": {
            "temp": 15.0,
            "feels_like": 14.5,
            "temp_min": 13.8,
            "temp_max": 16.2,
            "humidity": 76
        },
        "wind": {
            "speed": 4.12,
            "deg": 280
        },
        "name": "London",
        "sys": {
            "country": "GB"
        },
        "visibility": 10000,
        "clouds": {
            "all": 0
        },
        "dt": 1619432400
    }

@pytest.fixture
def valid_form_data():
    """Valid form data for weather request"""
    return {
        'city': 'San Francisco',
        'state': '',
        'country': 'US'
    }

@pytest.fixture
def invalid_form_data():
    """Invalid form data for weather request"""
    return {
        'city': '',
        'state': '',
        'country': ''
    }
