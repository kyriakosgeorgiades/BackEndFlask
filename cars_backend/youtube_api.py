from dotenv import dotenv_values
from googleapiclient.discovery import build

# Get environment variables from .env file
dotenv_vars = dotenv_values(".env")
print(dotenv_vars)
# API key from a Google account required to use the YouTube search API
API_KEY = dotenv_vars["API_KEY"]
API_VERSION = "v3"


# Takes a car and returns a link to a YouTube video review of that car
# Input: car dictionary containing info about the car from the database
# Output: Returns a YouTube embed link to the top video review of that car
def find_car_video(car):
    youtube = build("youtube", API_VERSION, developerKey=API_KEY)

    query = str(car["brand"]) + " " + str(car["model"]) + " " + str(car["year"]) + " review"
    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        type="video",
        videoEmbeddable="true"
    ).execute()

    # Get the top video by popularity from the results
    top_video = search_response.get("items", [])[0]

    # Generate the embed link using the video ID
    link = "https://www.youtube.com/embed/" + str(top_video["id"]["videoId"])
    return link