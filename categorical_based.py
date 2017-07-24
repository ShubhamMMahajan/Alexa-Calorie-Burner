'''
Created on Jul 21, 2017

@author: shubham
'''
import basic_calculations
def get_swimming_calories(intent, WEIGHT):
    '''returns the amount of calories burned spent spent swimming'''
    calories = calculate_swimming_calories(get_stroke(intent),
                                            basic_calculations.duration_minutes(intent['slots']['duration']['value']),
                                             WEIGHT)
    return calories

def calculate_swimming_calories(stroke, time, WEIGHT):
    '''calculates the amount of calories burned when swimming based on the stroke and the time spent'''
    MET_dict = {'breaststroke': 8, 'backstroke': 10, 'freestyle': 10, 'butterfly': 11}
    MET = 0
    for key in MET_dict.keys():
        if key == stroke:
            MET = MET_dict[key]
    return 0.0175 * MET * (WEIGHT/2.2) * time            
    
def get_stroke(intent):
    '''returns the swimming stroke'''
    return intent['slots']['classifying_unit']['value']