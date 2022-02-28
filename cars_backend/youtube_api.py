from dotenv import dotenv_values
from googleapiclient.discovery import build

# Get environment variables from .env file
dotenv_vars = dotenv_values(".env")
# API key from a Google account required to use the YouTube search API
API_KEY = dotenv_vars["API_KEY"]
API_VERSION = "v3"


# Takes a car and returns a link to a YouTube video review of that car
# Input: car dictionary containing info about the car from the database
# Output: Returns a YouTube embed link to the top video review of that car
def find_car_video(car):
    youtube = build("youtube", API_VERSION, developerKey=API_KEY)

    query = build_query(car["brand"], car["model"], car["year"])

    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        type="video",
        videoEmbeddable="true"
    ).execute()

    # Get the top video by popularity from the results
    top_video = search_response.get("items", [])[0]

    link = build_link(top_video["id"]["videoId"])
    return link


def build_query(brand, model, year):
    if not brand or not model or not year:
        raise ValueError("Invalid car information")

    query = str(brand) + " " + str(model) + " " + str(year) + " review"
    return query


# Generate the embed link using the video ID
def build_link(video_id):
    if not video_id or len(video_id) != 11:
        raise ValueError("Invalid video ID")

    link = "https://www.youtube.com/embed/" + str(video_id)
    return link