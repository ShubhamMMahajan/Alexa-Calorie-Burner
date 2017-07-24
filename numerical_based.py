
def get_pushup_calories(intent, WEIGHT):
    '''returns the number of calories burned by doing pushups'''
    number = get_number(intent)
    minutes = number/20
    MET = 8
    return 0.0175 * MET * (WEIGHT/2.2) * minutes

def get_situp_calories(intent, WEIGHT):
    '''returns the number of calories burned by doing situps'''
    number = get_number(intent)
    minutes = number/10
    MET = 6
    return 0.0175 * MET * (WEIGHT/2.2) * minutes
    
def get_squat_calories(intent, WEIGHT):
    '''returns the number of calories burned by doing pullups'''
    number = get_number(intent)
    return number * 2

def get_pullup_calories(intent, WEIGHT):
    '''returns the number of calories burned by doing squats'''
    number = get_number(intent)
    return number * 1

#Returns the number of pushups, situps, pullups, or squats    
def get_number(intent):
    return int(intent['slots']['number']['value'])