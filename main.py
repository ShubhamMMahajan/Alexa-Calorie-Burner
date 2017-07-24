'''
Created on Jul 14, 2017

@author: shubham
'''


WEIGHT = 150

import speed_based
import intensity_based
import categorical_based
import numerical_based
import other






 
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
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

def get_welcome_response(session):

     session_attributes = {}
     
    
     #print(session.keys())
     if session == "":
         name = "No one"
         card_title = "Welcome"
     else:
        name = session['slots']['MyName']['value']
        card_title = session['name']
     speech_output = name + " is in the house"
     should_end_session = True
     return build_response(session_attributes, build_speechlet_response(
     card_title, speech_output, None, should_end_session))

def print_output(intent, calories):
    session_attributes = {}
    card_title = intent['name']
    speech_output = "You burned " + str(round(calories)) + " calories"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, None, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Calorie Burner. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}


def set_color_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Color' in intent['slots']:
        favorite_color = intent['slots']['Color']['value']
        session_attributes = create_favorite_color_attributes(favorite_color)
        speech_output = "I now know your favorite color is " + \
                        favorite_color + \
                        ". You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_color_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


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
    should_end_session = True
    card_title = session["name"]
    speech_output = "Please tell me your activity to see how many calories you burned"

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    #return get_welcome_response("")
    return build_response(session_attributes, build_speechlet_response(
     card_title, speech_output, None, should_end_session))
    


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    session_attributes = {}

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "RunningCalories":        
        calories = speed_based.get_running_calories(intent, WEIGHT)
        return print_output(intent, calories)    
    elif intent_name == "BikingCalories":
        calories = speed_based.get_biking_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "WalkingCalories":
        calories = speed_based.get_walking_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "SkiingCalories":
        calories = speed_based.get_skiing_calories(intent, WEIGHT)
        return print_output(intent, calories) 
    elif intent_name == "CyclingCalories":
        calories = intensity_based.get_cycling_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "DancingCalories":
        calories = intensity_based.get_dancing_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "RowingCalories":
        calories = intensity_based.get_rowing_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "SwimmingCalories":
        calories = categorical_based.get_swimming_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "PushUpCalories":
        calories = numerical_based.get_pushup_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "SitUpCalories":
        calories = numerical_based.get_situp_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "SquatCalories":
        calories = numerical_based.get_squat_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "PullUpCalories":
        calories = numerical_based.get_pullup_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "SittingCalories":
        calories = other.get_sitting_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "JumpRopeCalories":
        calories = other.get_jumprope_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "ChoresCalories":
        calories = other.get_chores_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "YogaCalories":
        calories = other.get_yoga_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "MowingCalories":
        calories = other.get_mowing_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "ShovelingCalories":
        calories = other.get_shoveling_calories(intent, WEIGHT)
        return print_output(intent, calories)
    elif intent_name == "SleepingCalories":
        calories = other.get_sleeping_calories(intent, WEIGHT)
        return print_output(intent, calories)
    
    ##DEFAULT AMAZON INTENTS
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
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
        return on_session_ended(event['request'], event['session'])



