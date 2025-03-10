"""
Filename:
    test_views.py
"""
def test_index_get(client):
    """Test the index route with GET request"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'SkyCast' in response.data

def test_index_post(client, valid_form_data):
    """Test the index route with POST request"""
    response = client.post('/', data=valid_form_data)
    assert response.status_code == 200
    assert b'San Francisco' in response.data

def test_index_post_invalid_form_data(client, invalid_form_data):
    """Test the index route with invalid form data"""
    response = client.post('/', data=invalid_form_data)
    assert response.status_code == 200
    assert b'None' in response.data

def test_successful_weather_request(client, valid_form_data, mock_weather_response, monkeypatch):
    """Test successful weather data fetch through the form"""
    def mock_fetch(city, state, country):
        return (
            mock_weather_response,  # weather_data
            None,                   # error_message
            51.5074,               # lat
            -0.1278,              # lon
            "San Francisco"       # name
        )

    monkeypatch.setattr('website.views.fetch_weather_data', mock_fetch)

    response = client.post('/', data=valid_form_data)
    assert response.status_code == 200 
