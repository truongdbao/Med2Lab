from words_to_number import WordsToNumbers
import re

class VitalSigns:

    def __init__(self,temperature,heart_rate,systolic,diastolic,respiratory_rate,saturation):
        VitalSigns.temperature = temperature
        VitalSigns.heart_rate = heart_rate
        VitalSigns.systolic = systolic
        VitalSigns.diastolic = diastolic
        VitalSigns.respiratory_rate = respiratory_rate
        VitalSigns.saturation = saturation



def ObtainAge(text_on_age): # Return the a word such as "twenty five" to the number such as 25
    if re.match(r'\d+',text_on_age):
        age_value = int(text_on_age)
    else:
        wtn = WordsToNumbers()
        age_value = wtn.parse(text_on_age)

    return age_value

def ObtainAgeUnit(text_on_age_unit): # Determine if the unit for age is "-year-old" or "-month-old"
    if re.match(r'.*?year.*',text_on_age_unit):
        age_unit = "year-old"
    else:
        age_unit = "month-old"

    return age_unit

def ObtainGender(text_on_gender): # Determine gender
    if re.match(r'.*?(female|woman|lady|girl).*',text_on_gender):
        gender = "female"
    else:
        gender = "male"

    return gender


def SelectSymptoms (set_of_symptoms,text): # create a list of symptoms from the set the are present in the text

    results = []

    for symptom in set_of_symptoms :
        if text.find(symptom) <> -1:
            results.append (symptom)

    return results

def UpdateVitalSigns (text, old_vitals): #obtain vital signs from a text
    new_vitals = VitalSigns(-1,-1,-1,-1,-1,-1)

    match = re.match(r'.*?(temperature|temp).*?(\d+\.?\d*).*', text)
    if (match) and (old_vitals.temperature == -1):
        new_vitals.temperature = match.group(2)
    else:
        new_vitals.temperature = old_vitals.temperature


    match = re.match(r'.*?(heart rate|heart rates|HR|pulse).*?(\d+).*', text)
    if (match) and (old_vitals.heart_rate  == -1):
        new_vitals.heart_rate = match.group(2)
    else:
        new_vitals.heart_rate = old_vitals.heart_rate

    match = re.match(r'.*?(pressure).*?(\d+).*?.(\d+).*', text)
    if (match) and (old_vitals.systolic == -1):
        new_vitals.systolic = match.group(2)
        new_vitals.diastolic = match.group (3)
    else:
        new_vitals.systolic  = old_vitals.systolic
        new_vitals.diastolic = old_vitals.diastolic

    match = re.match(r'.*?(respiratory rate|breathing rate|RR).*?(\d+).*', text)
    if (match) and (old_vitals.respiratory_rate  == -1):
        new_vitals.respiratory_rate  = match.group(2)
    else:
        new_vitals.respiratory_rate  = old_vitals.respiratory_rate

    match = re.match(r'.*?(saturation|sat).*?(\d+).*', text)
    if (match) and (old_vitals.saturation == -1):
        new_vitals.saturation = match.group(2)
    else:
        new_vitals.saturation = old_vitals.saturation

    return new_vitals

