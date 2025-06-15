from data.variables import *
from ..text_to_speech import text_to_speech

def get_critique_upper( 
                 exercise, 
                 distance_wrists_status, 
                 distance_elbows_status):
    global last_critique

    voice_critique = None

    if distance_wrists_status == "Wide" and distance_elbows_status == "Wide":
        voice_critique = "You're arms are too wide narrow them"
    elif distance_wrists_status == "Narrow" and distance_elbows_status == "Narrow":
        voice_critique = "You're arms are too narrow widen them"
    else:                         
        voice_critique = "Perfect form"

    if voice_critique and voice_critique != last_critique[exercise]:
        text_to_speech.text_to_speech(voice_critique)
        last_critique[exercise] = voice_critique

def get_critique_lower( 
                 exercise, 
                 distance_knees_status, 
                 distance_ankles_status):
    global last_critique

    voice_critique = None

    if distance_knees_status == "Wide" and distance_ankles_status == "Wide":
        voice_critique = "You're legs are too wide narrow them"
    elif distance_knees_status == "Narrow" and distance_ankles_status == "Narrow":
        voice_critique = "You're legs are too narrow widen them"
    else:                         
        voice_critique = "Perfect form"

    if voice_critique and voice_critique != last_critique[exercise]:
        text_to_speech.text_to_speech(voice_critique)
        last_critique[exercise] = voice_critique