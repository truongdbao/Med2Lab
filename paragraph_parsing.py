case = open('case01' ,'r').read() # load the case file
symptoms_file = open ('symptoms' , 'r')

import re  # Load regular expression module
import process_history_info
from process_history_info import VitalSigns

lines = case.split('.')

# Initiate an empty vitals object

vitals = process_history_info.VitalSigns(-1,-1,-1,-1,-1,-1)

#Load the symptoms into an
symptoms = []
for word in symptoms_file:
    word = word.rstrip()
    symptoms.append(word)


cc_line = ''
age = 0
gender = ''
cc_symptoms = []
positive_symptoms = []
negative_symptoms = []


for line in lines:
    match_cc = re.match(r'.*?(\d+| [A-Z ]+)(-year-old| years old| year old|-month-old| montold).*?(male|female|boy|girl|man|gentleman|woman|lady).*',line,re.I)

    # Determine the sentence that has the intro and  chief complaint
    # Pattern of the chief complaint sentence:
    # (... [age] ... [gender] ... with ...[chief symptoms] ... [timing]...)

    vitals = process_history_info.UpdateVitalSigns(line, vitals)   # try to look for vital signs contained in this line.

    if match_cc:
        # this is indeed the sentence that has the chief complaint and the intro
        cc_line = match_cc.group()
        age = process_history_info.ObtainAge(match_cc.group(1))
        age_unit = process_history_info.ObtainAgeUnit(match_cc.group(2))
        gender = process_history_info.ObtainGender(match_cc.group(3))

        cc_symptoms = process_history_info.SelectSymptoms(symptoms,cc_line)
        # attempt to get as much symptoms containing from the chief complaint sentence. these are the primary symptoms of the case

    else:
        # not a chief complain line

        # first, check to see if this is the 'pertinent-negatives' sentence, which usually formats '... denies [negative symptoms] ...'
        negative_statement = re.match (r'(.*?)(denied|denies|deny)(.*)',line)
        new_negative_symptoms = []
        new_positive_symptoms = []
        if negative_statement:
            # special processing for the 'pertinent-negatives' - some pertinent-negative statements also had some pertinent-positives first
            # for example "He said that he had a cough, but denied having running nose ..."
            new_positive_symptoms = process_history_info.SelectSymptoms(symptoms,negative_statement.group(1))
            new_negative_symptoms = process_history_info.SelectSymptoms(symptoms,negative_statement.group(3))
        else:
            # if not the pertinent-negative statments, just go and look for pertinent-positives throughout the statement
            new_positive_symptoms = process_history_info.SelectSymptoms(symptoms, line)

        # all done, now load the new pertinent-negatives and pertinent-positives to the main lists
        for symptom in new_negative_symptoms:
            if not (symptom in negative_symptoms) and not (symptom in cc_symptoms):
                negative_symptoms.append(symptom)
        for symptom in new_positive_symptoms:
            if not (symptom in positive_symptoms) and not (symptom in cc_symptoms):
                positive_symptoms.append(symptom)


print cc_line,'\n'

print 'Age of patient: ',age,age_unit
print 'Gender: ',gender
print '\n'
print 'Chief complaints:'
for symptom in cc_symptoms:
    print '    ',symptom

print '\n'
print 'Pertinent positive symptoms mentioned in this case:'
for symptom in positive_symptoms:
    print '    ',symptom

print '\n'
print 'Pertinent negative symptoms mentioned in this case:'
for symptom in negative_symptoms:
    print '    ',symptom

print '\n'
if vitals.temperature > -1:
    print 'Temperature:',vitals.temperature
if vitals.heart_rate > -1:
    print 'Heart Rate:', vitals.heart_rate
if vitals.systolic > -1:
    print 'Blood Pressure:',vitals.systolic,'/',vitals.diastolic
if vitals.respiratory_rate > -1:
    print 'Respiratory Rate:', vitals.respiratory_rate
if vitals.saturation > -1:
    print 'O2 Saturation:', vitals.saturation


