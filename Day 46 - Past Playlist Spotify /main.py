import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# SPOTIFY ACCESS
CLIENT_ID = "YOUR_ID"
CLIENT_SECRET = "YOUR_SECRET"

# GETTING BILLBOARD MUSIC LIST
date = input("Which year do you want to travel to? Please type the date in this format YYYY-MM-DD: ")
BILLBOARD_HTML = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(BILLBOARD_HTML)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("li h3.c-title")
artists = soup.select("li span.c-label.a-no-trucate")

title_list = [title.text.strip() for title in titles]
artist_list = [artist.text.strip() for artist in artists]

print(title_list)
print(artist_list)

# SPOTIFY OAUTH
auth_manager = SpotifyOAuth(scope="playlist-modify-private",
                            client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri="http://example.com",
                            show_dialog=True,
                            cache_path="token.txt")

sp = spotipy.Spotify(auth_manager=auth_manager)

print(date[0:4])
song_uris = []
for i in range(100):
    try:
        song = sp.search(q=f"track: {title_list[i]} artist: {artist_list[i]} year: {date[0:4]}", type="track")
        song_uris.append(song["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{title_list[i]} from {artist_list[i]} was not found. Skipped.")

# Creating Playlist at Spotify

playlist_name = f"{date} Billboard 100"
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

print("Successful!")
