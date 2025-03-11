"""
Filename:
    test__init__.py
"""
from website import create_app
def test_default_config():
    """Test configuration"""
    app = create_app()
    assert app.config['SECRET_KEY'] == 'secret keyyyyy'
    assert 'GEMINI_API_KEY' in app.config
