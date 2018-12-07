#chooses a random message to send to the user
import random

def get_intro():
    sample_responses = ["Hm,let see", "Aha.", "What we have here"]
    # return selected item to the user
    return random.choice(sample_responses)

def get_story_by_location(coordinates):
    intro = get_intro()
    story = 'You are in %s 200m from here the 1974 riots against the militaty junta started. University students seized the Techincal University to demanding freedom. The protest ended with a tank entering the building' %coordinates

    return intro + story
