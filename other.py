import basic_calculations

def get_sitting_calories(intent, WEIGHT):
    '''returns the amount of calories spent sitting'''
    time = get_time(intent)
    MET = 1
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_jumprope_calories(intent, WEIGHT):
    '''returns the amount of calories spent jump roping'''
    time = get_time(intent)
    MET = 10
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_chores_calories(intent, WEIGHT):
    '''returns the amount of calories doing chores'''
    time = get_time(intent)
    MET = 3
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_yoga_calories(intent, WEIGHT):
    '''returns the amount of calories doing yoga'''
    time = get_time(intent)
    MET = 3
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_mowing_calories(intent, WEIGHT):
    '''returns the amount of calories spent mowing the lawn'''
    time = get_time(intent)
    MET = 6
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_shoveling_calories(intent, WEIGHT):
    '''returns the amount of calories spent shoveling snow'''
    time = get_time(intent)
    MET = 6
    return 0.0175 * MET * (WEIGHT/2.2) * time

def get_sleeping_calories(intent, WEIGHT):
    '''returns the amount of calories spent sleeping'''
    time = get_time(intent)
    MET = 0.75
    return 0.0175 * MET * (WEIGHT/2.2) * time
    

def get_time(intent):
    '''gets the time from the intent'''
    return basic_calculations.duration_minutes(intent['slots']['duration']['value'])


