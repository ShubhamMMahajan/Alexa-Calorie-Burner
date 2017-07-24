'''
Created on Jul 17, 2017

@author: shubham
'''


def duration_minutes(duration):
    '''returns the number of minutes spent on the exercise assumes the format of alexa's AMAZON.DURATION type'''
    t_index = duration.index("T")
    if "H" in duration and "M" in duration:
        hour_index = duration.index('H') - 1
        minute_index = duration.index('M') - 1
        return (int(duration[t_index + 1:hour_index + 1]) * 60) + int(duration[hour_index + 2:minute_index+ 1])
    elif "H" not in duration and "M" in duration:        
        minute_index = duration.index('M') - 1
        return int(duration[t_index + 1:minute_index+ 1])
    elif "M" not in duration and "H" in duration:         
        hour_index = duration.index('H') - 1
        return (int(duration[t_index + 1:hour_index + 1]) * 60)
    else:
        return 0
