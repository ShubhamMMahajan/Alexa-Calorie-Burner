'''
Created on Jul 17, 2017

@author: shubham
'''
import basic_calculations
from collections import OrderedDict

##RUNNING CALCULATIONS
def get_running_calories(intent, WEIGHT):
    '''returns the amount of calories burned when running'''
    pace, time = get_data(intent)
    print(pace)
    if pace == "":
        return "distance"
    if time == "":
        return "time"
    if pace == "unit":
        return "distance unit"
    calories = calculate_running_calories(pace, time, WEIGHT)
    return calories    

def calculate_running_calories(pace, time, WEIGHT):
    '''calculate the amount of calories burned when running based on the pace'''
    dict = {"5.2": 8, "6": 9, "6.7": 10, "7": 11, "7.5": 11.5, "8": 12.5, "8.6": 13.5, "9": 14, "10": 15, "10.9": 16}
    new_dict = OrderedDict(sorted(dict.items(), key = lambda t: float(t[0])))
    for key in new_dict.keys():
        if float(key) > pace:
            MET = new_dict[key]
            break
    else:
        MET = 18    
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_biking_calories(intent, WEIGHT):
    '''returns the amount of calories burned when biking'''
    pace, time = get_data(intent)
    if pace == "":
        return "distance"
    if time == "":
        return "time"
    if pace == "unit":
        return "distance unit"
    calories = calculate_biking_calories(pace, time, WEIGHT)
    return calories

def calculate_biking_calories(pace, time, WEIGHT):
    '''calculate the amount of calories burned when biking based on the pace'''
    dict = {"10": 4, "12": 6, "14": 8, "16": 10, "20": 12}
    new_dict = OrderedDict(sorted(dict.items(), key = lambda t: float(t[0])))
    for key in new_dict.keys():
        if float(key) > pace:
            MET = new_dict[key]
            break
    else:
        MET = 16    
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_walking_calories(intent, WEIGHT):
    '''returns the amount of calories burned when walking'''
    pace, time = get_data(intent)
    if pace == "":
        return "distance"
    if time == "":
        return "time"
    if pace == "unit":
        return "distance unit"
    calories = calculate_walking_calories(pace, time, WEIGHT)
    return calories

def calculate_walking_calories(pace, time, WEIGHT):
    '''calculate the amount of calories burned when walking based on the pace'''
    dict = {"2": 2.5, "2.5": 3, "3": 3.5, "4": 4, "4.5": 4.5}
    new_dict = OrderedDict(sorted(dict.items(), key = lambda t: float(t[0])))
    for key in new_dict.keys():
        if float(key) > pace:
            MET = new_dict[key]
            break
    else:
        MET = 6    
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_skiing_calories(intent, WEIGHT):
    '''returns the amount of calories burned when skiing'''
    pace, time = get_data(intent)
    if pace == "":
        return "distance"
    if time == "":
        return "time"
    if pace == "unit":
        return "distance unit"
    calories = calculate_skiing_calories(pace, time, WEIGHT)
    return calories

def calculate_skiing_calories(pace, time, WEIGHT):
    '''calculate the amount of calories burned when skiing based on the pace'''
    dict = {"2.5": 7, "5":8, "8": 9}
    new_dict = OrderedDict(sorted(dict.items(), key = lambda t: float(t[0])))
    for key in new_dict.keys():
        if float(key) > pace:
            MET = new_dict[key]
            break
    else:
        MET = 14    
    return 0.0175 * MET * (WEIGHT/2.2) * time    
    
def get_data(intent):
    '''gets the distance and time and returns the pace and time'''
    time = ""
    distance = ""
    try:
        distance = int(intent['slots']['distance']['value'])
        try:
            distance_unit = intent['slots']['distance_unit']['value']
        except:
            return("unit", None)
        time = basic_calculations.duration_minutes(intent['slots']['duration']['value'])
        if distance_unit == "kilometer" or distance_unit == "kilometers":
            distance = convert_to_mile(distance)
        elif distance_unit == "mile" or distance_unit == "miles":           
            distance = distance
        else:            
            return ("unit", None)
        pace = calculate_pace(distance, time)
        return (pace, time)
    except:
        return (distance, time)
              

def convert_to_mile(kilometer):
    '''converts kilometers to mile'''
    return kilometer / 1.6

def calculate_pace(distance, time):
    '''calculates the pace given the distance and time'''
    return (distance / time) * 60

    