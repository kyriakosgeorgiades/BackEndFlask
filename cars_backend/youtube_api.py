from dotenv import dotenv_values
from googleapiclient.discovery import build
import os

# Get environment variables from .env file
dotenv_vars = dotenv_values(".env")

API_KEY = dotenv_vars["API_KEY"]
API_VERSION = "v3"


def find_car_video(car):
    youtube = build("youtube", API_VERSION, developerKey=API_KEY)

    query = str(car["brand"]) + " " + str(car["model"]) + " " + str(car["year"]) + " review"
    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        type="video",
        videoEmbeddable="true"
    ).execute()

    # List of returned videos, max 25 by default
    videos = []

    for search_result in search_response.get("items", []):
        videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["videoId"]))

    top_video = search_response.get("items", [])[0]
    link = "https://www.youtube.com/watch?v=" + str(top_video["id"]["videoId"])
    print(link)
