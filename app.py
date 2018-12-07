#Python libraries that we need to import for our bot
from flask import Flask, request
import fbmessenger

app = Flask(__name__)

#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/fbmessenger", methods=['GET', 'POST'])
def fbmessenger_receive_message():
    return fbmessenger.receive_message(request)

if __name__ == "__main__":
    app.run()
