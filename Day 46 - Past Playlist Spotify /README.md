# Day 46 - Past Playlist Spotify

This Python script automates the creation of a Spotify playlist based on Billboard Hot 100 songs for a specified year. Here's a quick overview:

## Libraries Used:
- **requests**: Fetches Billboard Hot 100 data via HTTP requests.
- **BeautifulSoup**: Extracts data from HTML and XML files.
- **spotipy**: A lightweight Python library for the Spotify Web API.
- **SpotifyOAuth**: Manages Spotify OAuth2 authentication.

## Spotify API Credentials:
Replace **"CLIENT_ID"** and **"CLIENT_SECRET"** with your Spotify API credentials.

## Usage:
1. Run the script and input the desired year.
2. The script fetches Billboard Hot 100 songs for the specified year.
3. Prints titles and artists of the Billboard Hot 100 songs.
4. Initiates Spotify OAuth for playlist creation.
5. Searches and extracts Spotify URIs for each song.
6. Creates a private Spotify playlist with the year as the name.
7. Adds Billboard songs to the created playlist.
8. Prints "Successful!" upon completion.

Note: Replace "YOUR_ID" and "YOUR_SECRET" with your Spotify API credentials.

This script streamlines playlist creation, enabling users to enjoy top hits from a specific year effortlessly.
