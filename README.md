# health-analytics
This is an assignment that encompasses the skills acquired over the past 6 weeks about topics in Github, Google Shell, and Python.

# Summary of the Variables
I created a number variable, a string variable, a list, and a dictionary that consists of multiple key:value pairs. One of the key:value pairs is a list and a second key:value pair is a nested dictionary. 

Number Variable: 
```
varNumber = 90
```
String Variable:
```
varString = 'breathing information'
```
List: 
```
varList = ['o2 level', 'respiration rate', 'lung capacity']
```
Key Value Pairs in Dictionary:
```
{
    "patient" : "Frank Gallagher",
    "age" : "50",
    "symptoms" : ['cough', 'dizziness', 'headache'],
    "emergencycontact" : {
        'emergencycontact1' : 'fiona gallagher',
        'emergencycontact2' : 'philip gallagher',
        'emergencycontact3' : 'sheila jackson'
    }
}
```
The key:value pair "symptons" is the key:value pair that is a list. The key:value pair "emergencycontact" is the key:value pair that is a nested dictionary. 

# Summary of the Function

The purpose of the function is to generate a response to a patient's oxygen saturation level and respiratory rate. 

-If a patient's oxygen saturation is low and respiratory rate is low, a response will be generated telling the patient their oxygen saturation level is low, state how far their oxygen saturation level is from normal, and tell the patient their respiratory rate is low

-If a patient's oxygen saturation is low and respiratory rate is normal, a response will be generated telling the patient their oxygen saturation level is low, state how far their oxygen saturation level is from normal, and tell the patient their respiratory rate is normal

-If a patient's oxygen saturation is low and respiratory rate is high, a response will be generated telling the patient their oxygen saturation level is low, state how far their oxygen saturation level is from normal, and tell the patient their respiratory rate is high

-If a patient's oxygen saturation rate is normal and respiratory rate is low, a response will be generated telling the patient their oxygen saturation level is normal and their respiratory rate is low

-If a patient's oxygen saturation rate is normal and respiratory rate is normal, a response will be generated telling the patient their oxygen saturation level is normal and their respiratory rate is normal

-If a patient's oxygen saturation rate is normal and respiratory rate is high, a response will be generated telling the patient their oxygen saturation level is normal and their respiratory rate is high

The example data provided is in lines 18 and 19. From the given data, the response generated should be:
```
oxygenSaturation = 89
respiratoryRate = 22

'You need oxygen treatment, your percentage is at 89'
'Your oxygen saturation level is this percent away from normal: 6'
'Your respiratory rate is high at: 22'