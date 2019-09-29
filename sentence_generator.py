import random as r
import datetime
import json
import requests
import time

N = 10
intent = "fill_cardiac_arrest"

url = "https://api.wit.ai/samples?v=20190928"
headers = {"Authorization": "Bearer BZNHG6WHHPFV6Z3HVLKU7Z55JKQTGBIN",
"Content-Type": "application/json"}
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
    "fill_request": ["type_of_service_requested", "primary_role_of_unit"],
    "fill_cardiac_arrest": ["yes", "resuscitation", "cause"],
    "fill_safety_equipment": ["equipment", "airbag_deployment"],
    "fill_barriers": ["impairment"],
    "fill_response_mode": ["mode"],
    "fill_transport_mode": ["mode"]
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
                0: ('treated_transport_ems', 'treated transport EMS'),
                1: ('cancelled', 'cancelled'),
                2: ('treated_released', 'treated released'),
                3: ('no_treatment', 'no treatment'),
                4: ('dead at scene', 'dead at scene'),
                5: ('treated_transferred_care', 'treated transferred care'),
                6: ('patient_refused_care', 'patient refused care'),
                7: ('treated_transported_private', 'treated transported private vehicle'),
                8: ('treated_transported_law', 'treated transported law enforcement')
            }
for i in range(N):
    time.sleep(1)
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
                    #"start": 0,
                    #"end": len(intentdict[intent])
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
                    "entity": "incident_date",
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
        dp = r.randint(0,9)
        sentence = '{} {}'.format(
            intentdict[intent],
            dispositions[dp][1]
        )
        data = [{
            "text": sentence,
            "entities": [
                {
                    "entity": "intent",
                    "value": intent,
                    #"start": 0,
                    #"end": len(intentdict[intent])
                },
                {
                    "entity": "disposition",
                    "value": dispositions[dp][0],
                    "start": sentence.find(dispositions[dp][1]),
                    "end": sentence.find(dispositions[dp][1]) + len(dispositions[dp][1])
                }
            ]
        }]
    elif intent == "fill_patients_on_scene":
        num_patients = {0: ('single','single'),
                        1: ('multiple','multiple')}
        num_casualty = {0: ('','No'),
                        1: ('mass casualty','Yes')}
        np = r.randint(0,1)
        np
        mc = 0
        if np == 1:
            mc = r.randint(0,1)

        sentence = '{} {} {}'.format(
            intentdict[intent],
            num_patients[np][0],
            num_casualty[mc][0],
        )
        if mc == 0:
            data = [{
                "text": sentence,
                "entities": [
                    {
                        "entity": "intent",
                        "value": intent
                    },
                    {
                        "entity": "num_patients",
                        "value": num_patients[np][1],
                        "start": sentence.find(num_patients[np][1]),
                        "end": sentence.find(num_patients[np][1]) + len(num_patients[np][1])
                    }
                ]
            }]
        elif mc == 1:
            data = [{
                "text": sentence,
                "entities": [
                    {
                        "entity": "intent",
                        "value": intent
                    },
                    {
                        "entity": "num_patients",
                        "value": num_patients[np][1],
                        "start": sentence.find(num_patients[np][1]),
                        "end": sentence.find(num_patients[np][1]) + len(num_patients[np][1])
                    },
                    {
                        "entity": "mass_casualty",
                        "value": num_casualty[mc][0],
                        "start": sentence.find(num_casualty[mc][0]),
                        "end": sentence.find(num_casualty[mc][0]) + len(num_casualty[mc][0])
                    }
                ]
            }]
    elif intent == 'fill_request':
        services = ['scene response','ED','mutual aid','intercept']
        roles = ['transport','non-transport','supervisor','rescue']
        for s in range(len(services)):
            for r in range(len(roles)):
                time.sleep(1)
                sentence = '{} {} {}'.format(
                    intentdict[intent],
                    services[s],
                    roles[r]
                )
                data = [{
                    "text": sentence,
                    "entities": [
                        {
                            "entity": "intent",
                            "value": intent
                        },
                        {
                            "entity": "service",
                            "value": services[s],
                            "start": sentence.find(services[s]),
                            "end": sentence.find(services[s]) + len(services[s])
                        },
                        {
                            "entity": "role",
                            "value": roles[r],
                            "start": sentence.find(roles[r]),
                            "end": sentence.find(roles[r]) + len(roles[r])
                        }
                    ]
                }]
                payload = data
                print(json.dumps(payload))
                req = requests.post(
                    url,
                    data=json.dumps(payload),
                    headers=headers)        
        break
    elif intent == 'fill_cardiac_arrest':
        arrest_state = ['prior to arrival', 'after arrival']
        resuscitation_state = ['defibrillation', 'ventilation', 'chest compressions', 'DOA', 'DNR', 'no signs of life']
        arrest_cause = ['presumed cardiac', 'trauma', 'drowning','electrocution','respiratory','other']
        for a in range(len(arrest_state)):
            for r in range(len(resuscitation_state)):
                for c in range(len(arrest_cause)):
                    time.sleep(.5)
                    sentence = '{} {} {} {}'.format(
                    intentdict[intent],
                    arrest_state[a],
                    resuscitation_state[r],
                    arrest_cause[c]
                    )
                    data = [{
                        "text": sentence,
                        "entities": [
                            {
                                "entity": "intent",
                                "value": intent
                            },
                            {
                                "entity": "cardiac_arrest",
                                "value": arrest_state[a],
                                "start": sentence.find(arrest_state[a]),
                                "end": sentence.find(arrest_state[a]) + len(arrest_state[a])
                            },
                            {
                                "entity": "resuscitation",
                                "value": resuscitation_state[r],
                                "start": sentence.find(resuscitation_state[r]),
                                "end": sentence.find(resuscitation_state[r]) + len(resuscitation_state[r])
                            },
                            {
                                "entity": "cardiac_cause",
                                "value": arrest_cause[c],
                                "start": sentence.find(arrest_cause[c]),
                                "end": sentence.find(arrest_cause[c]) + len(arrest_cause[c])
                            }
                        ]
                    }]
                    payload = data
                    # print('{} {} {}'.format(a,r,c))
                    print(json.dumps(payload))
                    req = requests.post(
                        url,
                        data=json.dumps(payload),
                        headers=headers)        
        break
    payload = data
    print(json.dumps(payload))
    req = requests.post(
        url,
        data=json.dumps(payload),
        headers=headers)


