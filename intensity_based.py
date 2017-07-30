'''
Created on Jul 21, 2017

@author: shubham
'''
import basic_calculations


def get_cycling_calories(intent, WEIGHT):
    '''returns the number of calories burned by cycling in place'''
    intensity, time = get_data(intent)
    if intensity == "intensity":
        return "intensity"
    if time == "time":
        return "time"
    calories = calculate_cycling_calories(intensity, time, WEIGHT)
    return calories
    
def calculate_cycling_calories(intensity, time, WEIGHT):
    '''calculates the amount of calories burned by cycling in place based on intensity'''
    MET_dict = {'casual': 3, 'moderate': 7, 'intense': 12.5}
    MET = 0
    for key in MET_dict.keys():
        if key == intensity:
            MET = MET_dict[key]
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_dancing_calories(intent, WEIGHT):
    '''returns the number of calories burned by dancing'''
    intensity, time = get_data(intent)
    if intensity == "intensity":
        return "intensity"
    if time == "time":
        return "time"
    calories = calculate_dancing_calories(intensity, time, WEIGHT)
    return calories

def calculate_dancing_calories(intensity, time, WEIGHT):
    '''calculates the amount of calories burned by dancing based on intensity'''
    MET_dict = {'casual': 5, 'moderate': 6, 'intense': 7}
    MET = 0
    for key in MET_dict.keys():
        if key == intensity:
            MET = MET_dict[key]
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_rowing_calories(intent, WEIGHT):
    '''returns the number of calories burned by rowing'''
    intensity, time = get_data(intent)
    if intensity == "intensity":
        return "intensity"
    if time == "time":
        return "time"
    calories = calculate_rowing_calories(intensity, time, WEIGHT)
    return calories

def calculate_rowing_calories(intensity, time, WEIGHT):
    '''calculates the amount of calories burned by rowing based on intensity'''
    MET_dict = {'casual': 5, 'moderate': 8.5, 'intense': 12.5}
    MET = 0
    for key in MET_dict.keys():
        if key == intensity:
            MET = MET_dict[key]
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_data(intent):
    '''gets the intensity as well as time spent on exercise'''
    try:
        intensity = intense_string(intent)
    except:
        return ("intensity", None)
    try:
        time = basic_calculations.duration_minutes(intent['slots']['duration']['value'])
    except:
        return (None, "time")
    return (intensity, time)

def intense_string(intent):
    '''finds out the intensity of the exercise
    based on 3 levels: casual, moderate, or intense'''
    intense_word = intent['slots']['intensity_unit']['value']
    
    if 'easy' in intense_word or 'casual' in intense_word or 'leisure' in intense_word:
        return 'casual'
    elif 'moderate' in intense_word or 'medium' in intense_word or 'normal' in intense_word:
        return 'moderate'
    elif 'hard' in intense_word or 'intense' in intense_word or 'vigor' in intense_word:
        return 'intense'
    else:
        return 'moderate'
