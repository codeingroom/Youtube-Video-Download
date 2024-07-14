from pytube import YouTube

# Function to download a YouTube video
def download_youtube_video(video_url, save_path):
    try:
        yt = YouTube(video_url)
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        # Download the video
        stream.download(output_path=save_path)
        print(f"Video downloaded successfully and saved to {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = 'https://www.youtube.com/watch?v=your_video_id'
save_path = 'path_to_save_the_video'
download_youtube_video(video_url, save_path)
