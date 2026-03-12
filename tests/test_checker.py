from src.checker import check_url_status

def test_valid_url_is_successful():
    """Test that a known reliable URL returns True."""
    result = check_url_status("https://www.google.com")
    assert result is True

def test_invalid_url_fails_gracefully():
    """Test that a non-existent URL returns False instead of crashing."""
    result = check_url_status("https://this-website-definitely-does-not-exist-12345.com")
    assert result is False

def test_404_status_returns_false():
    """Test that a valid domain but missing page returns False."""
    result = check_url_status("https://www.google.com/this-page-is-a-404")
    assert result is False