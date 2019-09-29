import random
import time

import speech_recognition as sr
from ibm_watson import SpeechToTextV1

from wit import Wit


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    #  url = 'https://stream.watsonplatform.net/speech-to-text/api'
    #  pwd = 'Rlj8ifTeuLS9XCooI3HPmP9wROs1PN6lSv2Uijg0a0tk'

    # speech_to_text = SpeechToTextV1(
        # iam_apikey = pwd,
        # url = url
        # )
    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        print("couldnt understand :(")
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    months = {  0:"January", 
            1:"February",
            2:"March",
            3:"April",
            4:"May",
            5:"June",
            6:"July",
            7:"August",
            8:"September",
            9:"October",
            10:"November",
            11:"December"}
    access_token = '7J2X2UTJFDJ4FMPUQJ7ELNNOH5MUYHMD'
    client = Wit(access_token)
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=1)
    print('Listening now...')
    trans = recognize_speech_from_mic(recognizer, microphone)['transcription']
    if (trans.find('Phil') == 0) or (trans.find('Bill') == 0):
        trans = trans.replace('Phil','Fill',1)
        trans = trans.replace('Bill','Fill',1)
    #print(trans)
    out = client.message(str_input)
    entities = out['entities']

    items = dict()
    for key in entities.keys():
        items[key] = entities[key][0]['value']
        if key == 'datetime':
            date = dateutil.parser.parse(entities[key][0]['value'])
            items[key] = '{} {} {}'.format(months[date.month-1], date.day, date.year)

    print(items)