'''
Created on Jul 14, 2017

@author: shubham
'''

import re

import speed_based
import intensity_based
import categorical_based
import numerical_based
import other

WEIGHT = 150
#TOTAL_CALORIES = 0
 
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def help_message():
    output_message = "Simply tell Alexa the activity you did to see how many calories you burned."
    return build_response({}, build_speechlet_response("Help", output_message, "", False))

def help_message_2(missing_value):
    output_message = "Error, you either forgot to specify or invalidly specified the " + missing_value
    return build_response({}, build_speechlet_response("Help", output_message, "", False))

def welcome_message():
    output_message = "Welcome to Calorie Burn Calculator, to get started tell Alexa the activity you did and how long it took you to do it to see how many calories you burned."
    return build_response({}, build_speechlet_response("Welcome", output_message, "", False))

def print_output(intent, calories):
    session_attributes = {}
    card_title = intent['name']
    intent_name_list = re.findall('[A-Z][a-z]*', card_title)
    intent_name = ""
    for index in range(len(intent_name_list) - 1):
        intent_name += intent_name_list[index] + " "
    speech_output = "You burned " + str(round(calories)) + " calories."
    reprompt_text = "If you want figure out how many calories you burned doing another activity please tell me now."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
    intent_name + "\n", speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Calorie Burner. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    #intent = launch_request['intent']
    session_attributes = {}
    should_end_session = False
    

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return welcome_message()
def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    session_attributes = {}

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    intent_name_dict = {"RunningCalories": speed_based.get_running_calories,
                        "BikingCalories": speed_based.get_biking_calories,
                        "WalkingCalories": speed_based.get_walking_calories,
                        "SkiingCalories": speed_based.get_skiing_calories,
                        "CyclingCalories": intensity_based.get_cycling_calories,
                        "DancingCalories": intensity_based.get_dancing_calories,
                        "RowingCalories": intensity_based.get_rowing_calories,
                        "SwimmingCalories": categorical_based.get_swimming_calories,
                        "PushUpCalories": numerical_based.get_pushup_calories,
                        "SitUpCalories": numerical_based.get_situp_calories,
                        "SquatCalories": numerical_based.get_squat_calories,
                        "PullUpCalories": numerical_based.get_pullup_calories,
                        "SittingCalories": other.get_sitting_calories,
                        "JumpRopeCalories": other.get_jumprope_calories,
                        "ChoresCalories": other.get_chores_calories,
                        "YogaCalories": other.get_yoga_calories,
                        "MowingCalories": other.get_mowing_calories,
                        "ShovelingCalories": other.get_shoveling_calories,
                        "SleepingCalories": other.get_sleeping_calories}
    
    # Dispatch to your skill's intent handlers
    for intent_name_in_dict in intent_name_dict.keys():
        if intent_name == intent_name_in_dict:
           
            calories = intent_name_dict[intent_name_in_dict](intent, WEIGHT)
            if type(calories) != int and type(calories) != float:
                return help_message_2(calories)
            return print_output(intent, calories)

    ##DEFAULT AMAZON INTENTS
    else: 
        if intent_name == "AMAZON.HelpIntent":
            return help_message()
        elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
            return handle_session_end_request()
        else:
            raise ValueError("Invalid intent")
        


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    handle_session_end_request()
    # add cleanup logic here

# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])
    

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return handle_session_end_request()




