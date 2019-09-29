from numpy import random as r
import datetime
import json
import requests
import time

N = 10
url = "https://api.wit.ai/samples?v=20190928"
headers = {"Authorization": "Bearer BZNHG6WHHPFV6Z3HVLKU7Z55JKQTGBIN",
"Content-Type": "application/json"}
intent = "fill_incident"
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
dispositions = {
                'treated_transport_ems': 'treated Transport EMS',
                'cancelled': 'cancelled',
                'treated_released': 'treated released',
                'no_treatment': 'no treatment',
                'dead at scene': 'dead at scene',
                'treated_transferred_care': 'treated transferred care',
                'patient_refused_care': 'patient refused care',
                'treated_transported_private': 'treated transported private vehicle',
                'treated_transported_law': 'treated transported law enforcement'
            }
for i in range(N):
    time.sleep(2)
    if intent == "fill_incident":
        incident_id = r.randint(100000,999999)
        unit_id = r.randint(1000,9999)
        month = r.randint(0,11)
        day = r.randint(1,30)
        year = r.randint(1950, 2018)
        sentence = "{} {} {} {} {} {}".format(
            intentdict["fill_incident"],
            incident_id,
            unit_id,
            months[month],
            day,
            year
        )
        iids = sentence.find(str(incident_id))
        uids = sentence.find(str(unit_id), iids+len(str(incident_id))+1)
        ms = sentence.find(months[month])
        ds = sentence.find(str(day), ms+len(months[month])+1)
        ys = sentence.find(str(year), ds+len(str(day))+1)

        data = [{
            "text": sentence,
            "entities": [
                {
                    "entity": "intent",
                    "value": intent,
                    "start": 0,
                    "end": len(intentdict[intent])
                },
                {
                    "entity": "incident_number",
                    "value": incident_id,
                    "start": iids,
                    "end": iids + len(str(incident_id))
                },
                {
                    "entity": "unit_id",
                    "value": unit_id,
                    "start": uids,
                    "end": uids + len(str(unit_id))
                },
                {
                    "entity": "datetime",
                    "value": datetime.datetime(
                            year,
                            month+1,
                            day).isoformat(),
                    "start": ms,
                    "end": ys + len(str(year))
                }
            ]
        }]
    elif intent == "fill_address":
        pass 
    elif intent == "fill_dispatch":
        pass
    elif intent == "fill_disposition":
        sentence = '{} {}'.format(
            intentdict[intent],
            dispositions[r.randint(0,9)]
        )
        data = [{
            "text": sentence,
            "entities": [
                {
                    "entity": "intent",
                    "value": intent,
                    "start": 0,
                    "end": len(intentdict[intent])
                },
                {
                    "entity": "incident_number",
                    "value": incident_id,
                    "start": iids,
                    "end": iids + len(str(incident_id))
                }
            ]
        }]
        payload = data
        print(json.dumps(payload))
        req = requests.post(
            url,
            data=json.dumps(payload),
            headers=headers)


