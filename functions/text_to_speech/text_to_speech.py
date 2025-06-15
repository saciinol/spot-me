import os
import uuid
import queue
import threading
import subprocess
from gtts import gTTS
from io import BytesIO
import tempfile
# from playsound import playsound

tts_cache = {}
playback_lock = threading.Lock()
playback_queue = queue.Queue()
current_playback = {"thread": None}

def stop_current_playback():
    if (current_playback["thread"] and current_playback["thread"].is_alive()
        and current_playback["thread"] != threading.current_thread()):
        current_playback["thread"].join()

def play_tts(mp3_data: BytesIO):
    stop_current_playback()
    
    # Create a temp file path manually (no open handle)
    temp_path = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4()}.mp3")
    
    try:
        # Write the mp3 data to the temp file
        with open(temp_path, 'wb') as f:
            f.write(mp3_data.read())

        # Play it with ffplay
        subprocess.run(['ffplay', '-nodisp', '-autoexit', temp_path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    finally:
        # Clean up
        try:
            os.remove(temp_path)
        except Exception as e:
            print(f"Could not delete temp file: {e}")

def text_to_speech(text):
    def run_tts():
        try:
            tts = gTTS(text, lang='en', tld='co.uk', slow=False)
            mp3_data = BytesIO()
            tts.write_to_fp(mp3_data)
            mp3_data.seek(0)
            play_tts(mp3_data)
        except Exception as e:
            print(f"Error in TTS: {e}")

    stop_current_playback()

    tts_thread = threading.Thread(target=run_tts, daemon=True)
    current_playback["thread"] = tts_thread
    tts_thread.start()