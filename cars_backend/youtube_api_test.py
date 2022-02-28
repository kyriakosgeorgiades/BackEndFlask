from cars_backend import youtube_api as api


# Test the build_query() function that returns a search query from car information
def test_build_query():
    query_1 = api.build_query("Toyota", "Camry", 2016)  # Test expected input

    assert isinstance(query_1, str)  # Query must be a string
    assert query_1.endswith("review")  # Query must end with review
    assert query_1.count(" ") >= 3  # Query must have at least 3 spaces


    query_2 = api.build_query("", "", "")  # Test empty string inputs
    # Error

    query_3 = api.build_query(None, None, None)  # Test null inputs
    # Error


def test_build_link():
    link
    assert query_1.startswith("https://www.youtube.com/embed/")
    assert len(query_1) == 41  # 30 for the link, 11 for the video ID
