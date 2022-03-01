import pytest
from cars_backend import youtube_api as api


# Test the build_query() function that returns a search query from car information
def test_build_query():
    # Test expected input
    query = api.build_query("Toyota", "Camry", 2016)

    assert isinstance(query, str)  # Query must be a string
    assert query.endswith("review")  # Query must end with review
    assert query.count(" ") >= 3  # Query must have at least 3 spaces


# Test various inputs that should raise exceptions, including empty strings and None
@pytest.mark.parametrize("brand", ["Toyota", "", None])
@pytest.mark.parametrize("model", ["Camry", "", None])
@pytest.mark.parametrize("year", [2016, "", None])
def test_build_query_exceptions(brand, model, year):
    # Testing all combinations for exceptions, skip the one valid combination
    if brand == "Toyota" and model == "Camry" and year == 2016:
        return

    with pytest.raises(ValueError):
        api.build_query(brand, model, year)


def test_build_link():
    link = api.build_link("qvCz5o3L02w")  # Video ID of Toyota Camry 2016 review video

    assert isinstance(link, str)  # Link must be a string
    assert link.startswith("https://www.youtube.com/embed/")  # Link must start with a YouTube embed
    assert len(link) == 41  # Link must be 41 in length, 30 for the link, and 11 for the video ID


# Test various inputs that should raise exceptions, including empty strings and None
@pytest.mark.parametrize("video_id", ["x", "", None])
def test_build_link_exceptions(video_id):
    with pytest.raises(ValueError):
        api.build_link(video_id)


# Integration test
def test_find_car_video():
    car = {"brand": "Toyota", "model": "Camry", "year": 2016}
    link = api.find_car_video(car)

    assert isinstance(link, str)  # Link must be a string
    assert link.startswith("https://www.youtube.com/embed/qvCz5o3L02w")  # Expected link to be returned
