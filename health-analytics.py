import pandas as pd  
import numpy as np  

varNumber = 90
varString = 'breathing information'
varList = ['o2 level', 'respiration rate', 'lung capacity']
varDictionary = {
    "patient" : "Frank Gallagher",
    "age" : "50",
    "symptoms" : ['cough', 'dizziness', 'headache'],
    "emergencycontact" : {
        'emergencycontact1' : 'fiona gallagher',
        'emergencycontact2' : 'philip gallagher',
        'emergencycontact3' : 'sheila jackson'
    }
}

oxygenSaturation = 89
respiratoryRate = 22
if oxygenSaturation >=95 and respiratoryRate <12:
    print('You do not need oxygen treatment, your percentage is at: ', oxygenSaturation)
    print('Your respiratory rate is low at: ', respiratoryRate)
elif oxygenSaturation >=95 and respiratoryRate >=12 and respiratoryRate <=20:
    print('You do not need oxygen treatment, your percentage is at: ', oxygenSaturation)
    print('Your respiratory rate is normal at: ', respiratoryRate)
elif oxygenSaturation >=95 and respiratoryRate >20: 
    print('You do not need oxygen treatment, your percentage is at: ', oxygenSaturation)
    print ('Your respiratory rate is high at: ', respiratoryRate)
elif oxygenSaturation <=94 and respiratoryRate <12:
    print('You need oxygen treatment, your percentage is at: ', oxygenSaturation)
    percentageUntilNormal = 95 - oxygenSaturation
    print('Your oxygen saturation level is this percent away from normal: ', percentageUntilNormal)
    print('Your respiratory rate is low at: ', respiratoryRate)
elif oxygenSaturation <=94 and respiratoryRate >=12 and respiratoryRate <=20:
    print('You need oxygen treatment, your percentage is at: ', oxygenSaturation)
    percentageUntilNormal = 95 - oxygenSaturation
    print('Your oxygen saturation level is this percent away from normal: ', percentageUntilNormal)
    print('Your respiratory rate is normal at: ', respiratoryRate)
else: 
    print('You need oxygen treatment, your percentage is at: ', oxygenSaturation)
    percentageUntilNormal = 95 - oxygenSaturation
    print('Your oxygen saturation level is this percent away from normal: ', percentageUntilNormal)
    print('Your respiratory rate is high at: ', respiratoryRate) 