import flask
import json
import os
from flask import send_from_directory, request, render_template

# Flask app should start in global layout
app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    # Gets payload from Dialogflow
    payload = request.get_json(force=True)
    # Gets the queryText and fulfillmentText only -- input of user, output of chatbot
    user_response = (payload['queryResult']['queryText'])
    bot_response = (payload['queryResult']['fulfillmentText'])
    if user_response or bot_response != "":
        print("User: " + user_response)
        print("Bot: " + bot_response)
    return "Message received."

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()