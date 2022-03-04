"""Unit tests for functions in youtube_api.py"""

import pytest
from cars_backend import youtube_api as api


def test_build_search_query():
    """Test the build_search_query function for cases where success is expected"""

    # Valid inputs
    query = api.build_search_query("Toyota", "Camry", 2016)

    assert isinstance(query, str)  # Query must be a string
    assert query.endswith("review")  # Query must end with the string literal "review"
    assert query.count(" ") >= 3  # Query must have at least 3 spaces


@pytest.mark.parametrize("brand", ["Toyota", "", None])
@pytest.mark.parametrize("model", ["Camry", "", None])
@pytest.mark.parametrize("year", [2016, "", None])
def test_build_search_query_exceptions(brand, model, year):
    """ Test the build_search_query function for cases where an exception should be raised.
        The inputs are parametrized to test all combinations."""

    # Skip the one valid combination since only exceptions are being tested for
    if brand == "Toyota" and model == "Camry" and year == 2016:
        return

    # Expecting a ValueError exception
    with pytest.raises(ValueError):
        api.build_search_query(brand, model, year)


def test_build_link():
    """Test the build_link function for cases where success is expected"""

    # Valid input, video ID of Toyota Camry 2016 review video
    link = api.build_link("qvCz5o3L02w")

    assert isinstance(link, str)  # Link must be a string
    assert link.startswith("https://www.youtube.com/embed/")  # Link must start with a YouTube embed
    assert len(link) == 41  # Link must be 41 in length, 30 for the link, and 11 for the video ID


@pytest.mark.parametrize("video_id", ["x", "", None])
def test_build_link_exceptions(video_id):
    """ Test the build_link function for cases where an exception should be raised.
        The inputs are parametrized to test all combinations."""

    # Expecting a ValueError exception
    with pytest.raises(ValueError):
        api.build_link(video_id)


def test_find_car_video():
    """ Test the find_car_video function for cases where success is expected
        This is the function that is imported into and called by the car route"""

    # Valid input
    car = {"brand": "Toyota", "model": "Camry", "year": 2016}
    link = api.find_car_video(car)

    assert isinstance(link, str)  # Link must be a string
    assert link.startswith("https://www.youtube.com/embed/qvCz5o3L02w")  # Expected link to be returned
