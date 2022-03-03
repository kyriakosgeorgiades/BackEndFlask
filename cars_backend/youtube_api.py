from dotenv import dotenv_values
from googleapiclient.discovery import build

# Get environment variables from .env file
dotenv_vars = dotenv_values(".env")
# API key from a Google account required to use the YouTube search API
API_KEY = dotenv_vars["API_KEY"]
API_VERSION = "v3"

def find_car_video(car):
    """Search YouTube for a review video of the car and return a link to the top video.

    :param car: dictionary - contains information about the car
    :return: string - embed link to the top video found
    """

    youtube = build("youtube", API_VERSION, developerKey=API_KEY)

    # Build the query string to search for
    query = build_query(car["brand"], car["model"], car["year"])

    # Make a call to the YouTube Search API
    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        type="video",
        videoEmbeddable="true"
    ).execute()

    # Get the top video by popularity from the results
    top_video = search_response.get("items", [])[0]

    # Build the final embed link to return
    link = build_link(top_video["id"]["videoId"])
    return link


def build_query(brand, model, year):
    """Build the search query for the car review video

    :param brand: string - brand of the car
    :param model: string - model of the car
    :param year: int or string - car's manufacture year
    :return: string - search query for the car review video
    """

    # Ensure that all parameters are valid
    if not brand or not model or not year:
        raise ValueError("Invalid car information")

    # Build the query using the parameters and the string literal "review"
    query = str(brand) + " " + str(model) + " " + str(year) + " review"
    return query


def build_link(video_id):
    """Build a YouTube embed link

    :param video_id: string - YouTube ID of the video
    :return: string - embed link to the YouTube video
    """
    # Ensure that video_id is valid according to YouTube's video ID format
    if not video_id or len(video_id) != 11:
        raise ValueError("Invalid video ID")

    # Build the link
    link = "https://www.youtube.com/embed/" + str(video_id)
    return link
