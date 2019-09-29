import random
import time

import speech_recognition as sr
import dateutil
from wit import Wit


def interpret_transcript():
    intentdict = {
    "fill_incident": "Fill incident number",
    "fill_address": "Fill address",
    "fill_dispatch": "Fill dispatch",
    "fill_disposition": "Fill patient disposition",
    "fill_patients_on_scene": "Fill patients on scene",
    "fill_request": "Fill request",
    "fill_cardiac_arrest": "Fill cardiac arrest",
    "fill_safety_equipment": "Fill safety equipment",
    "fill_barriers": "Fill barriers",
    "fill_response_mode": "Fill response mode",
    "fill_transport_mode": "Fill transport mode"
    }
    paramsdict = {
        "fill_incident": ['incident_number', 'unit_id', 'incident_date'],
        "fill_address": ['address', 'city', 'state', 'zipcode'],
        "fill_dispatch": ["complaint", "dispatch_performed", "level of service"],
        "fill_disposition": ["disposition"],
        "fill_patients_on_scene": ["number_patients_on_scene", "mass_casualty"],
        "fill_request": ["type_of_request_selected", "primary_role_of_unit", "service", "role"],
        "fill_cardiac_arrest": ["cardiac_arrest", "resuscitation", "cardiac_cause"],
        "fill_safety_equipment": ["equipment", "airbag_deployment"],
        "fill_barriers": ["impairment"],
        "fill_response_mode": ["mode"],
        "fill_transport_mode": ["mode"]
    }
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
    out = client.message(trans)
    entities = out['entities']

    items = dict()
    for key in entities.keys():
        items[key] = entities[key][0]['value']
        if key == 'datetime':
            date = dateutil.parser.parse(entities[key][0]['value'])
            items[key] = '{} {} {}'.format(months[date.month-1], date.day, date.year)

    print(items)
    result = dict()
    if 'intent' in items and items['intent'] in paramsdict:
        for i in range (len(paramsdict[items['intent']])):
            if paramsdict[items['intent']][i] in items:
                result[paramsdict[items['intent']][i]] = items[paramsdict[items['intent']][i]]

    print(result)
    return result 
    
    
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

interpret_transcript()