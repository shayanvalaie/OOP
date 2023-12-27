class MusicPlayer:
    def play_audio(self, file):
        # Code to play audio

class VideoPlayer:
    def play_video(self, file):
        # Code to play video

class VideoPlayerAdapter(MusicPlayer):
    def __init__(self, video_player):
        # Initialize with a VideoPlayer object

    def play_audio(self, file):
        # Adapt the VideoPlayer's play_video method

# Example Usage
audio_player = MusicPlayer()
video_adapter = VideoPlayerAdapter(VideoPlayer())

audio_player.play_audio("song.mp3")
video_adapter.play_audio("video.mp4")  # Plays video through the adapter
