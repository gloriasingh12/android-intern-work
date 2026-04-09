# =================================================================
# PROJECT: Media Player System
# DESCRIPTION: Functional logic for Play, Pause, and Skip controls.
# DELIVERABLE: Python script simulating a Media Player with local storage.
# =================================================================

class MediaPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current_track_index = 0
        self.is_playing = False
        print(f"🎵 Media Player Initialized. {len(playlist)} tracks found.")

    def play(self):
        """Starts playing the current track."""
        self.is_playing = True
        track = self.playlist[self.current_track_index]
        print(f"▶️ PLAYING: {track}")

    def pause(self):
        """Pauses the current track."""
        if self.is_playing:
            self.is_playing = False
            track = self.playlist[self.current_track_index]
            print(f"⏸️ PAUSED: {track}")
        else:
            print("⚠️ Already Paused.")

    def skip_next(self):
        """Skips to the next track in the local storage."""
        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        track = self.playlist[self.current_track_index]
        print(f"⏭️ SKIPPED NEXT: Now playing {track}")
        self.play()

    def skip_previous(self):
        """Skips back to the previous track."""
        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        track = self.playlist[self.current_track_index]
        print(f"⏮️ SKIPPED PREVIOUS: Now playing {track}")
        self.play()

# --- DEMONSTRATION ---
if __name__ == "__main__":
    # Simulating Local Storage Files
    local_audio_files = ["Song_1.mp3", "Podcast_Final.wav", "Motivation_Audio.mp3"]
    
    # Initialize Player
    player = MediaPlayer(local_audio_files)

    print("\n--- Testing Controls ---")
    
    # 1. Test Play
    player.play()
    
    # 2. Test Pause
    player.pause()
    
    # 3. Test Skip Next
    player.skip_next()
    
    # 4. Test Skip Previous
    player.skip_previous()

    print("\n" + "="*35)
    print("STATUS: Media Player Logic Functional ✅")
    print("="*35)
