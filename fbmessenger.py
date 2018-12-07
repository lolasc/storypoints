#Python libraries that we need to import for our bot
from pymessenger.bot import Bot
import stories

ACCESS_TOKEN='EAAEKy1nZC6WABAE2SQArsKTnSyBZAZAxwi1NBQTG1OT3Bot7GVrKA4ZBY4SNCmlcZAFf55vVdVl4EADNzaUbw2eI6IYmqbBMZCablPlI69ZAetcFmb5gRZAYyKNBHB1C6PSgzmY5un7GD1qZBlpKz1sZAy2YjpX8O0hLY5ULHbBHYY4wZDZD'
VERIFY_TOKEN = 'STORYPOINTS1975'

bot = Bot(ACCESS_TOKEN)

def receive_message(request):
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(request,token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    send_location_req(recipient_id)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    a = message['message']['attachments'][0]
                    if a['type'] == 'location':
                        story = stories.get_story_by_location(a['payload']['coordinates'])
                        send_message(recipient_id, story)
                    else:
                        send_location_req(recipient_id)

    return "Message Processed"


def verify_fb_token(request,token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

def send_location_req(recipient_id):
    locqreply = {
    "text": "Here is a quick reply!",
    "quick_replies":[
      {
        "content_type":"location"
      }
    ]
    }
    bot.send_message(recipient_id,locqreply)
