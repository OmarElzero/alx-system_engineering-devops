from pytube import Playlist

def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    for video in playlist.video_urls:
        print(f"Downloading video: {video}")
        youtube = YouTube(video)
        youtube.streams.get_highest_resolution().download()
        print(f"Video {video} downloaded successfully!")

if __name__ == "__main__":
    playlist_url = input("Enter the URL of the playlist: ")
    download_playlist(playlist_url)
