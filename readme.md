# 🤖 DialogFlow Chatbot in Flask + Kommunicate

# Description

This project applies [Google’s Dialogflow and packing it in a simple Python service](https://www.kommunicate.io/blog/create-chatbot-in-flask-and-python/). The chatbot connects to the Dialogflow API where an agent is trained with various intents. For this project, a simple `Delivery Inquiry` chatbot service is created, where the `name`, `address` and `date` of delivery are processed by the chatbot via ******intent******. The welcome intent is processed in the beginning as well. Here is a sample demonstration:

![Chatbot shown in terminal](%F0%9F%A4%96%20DialogFlow%20Chatbot%20in%20Flask%20+%20Kommunicate%20088cba029eb24ea0b804d7c709e83f22/BoomAI_Q5_-_Dialogflow_Flask_App_Sample.png)

Chatbot shown in terminal

In addition, the service is integrated with Kommunicate for easy integration with your other projects (ex. website) Below is a sample demonstration:

![Chatbot in Kommunicate UI/app](%F0%9F%A4%96%20DialogFlow%20Chatbot%20in%20Flask%20+%20Kommunicate%20088cba029eb24ea0b804d7c709e83f22/BoomAI_Q5_-_Dialogflow_Flask_App_Kommunicate_Sample.png)

Chatbot in Kommunicate UI/app

---

# Overview

1. Setup Agent and Intents in Dialogflow. For this project, only 3 intents were made for agent Merbot:
    
    ## **Welcome Intent**
    
    1. **Training Phrases**: the default given by Dialogflow
        
        ![Screen Shot 2022-10-23 at 7.35.58 PM.png](%F0%9F%A4%96%20DialogFlow%20Chatbot%20in%20Flask%20+%20Kommunicate%20088cba029eb24ea0b804d7c709e83f22/Screen_Shot_2022-10-23_at_7.35.58_PM.png)
        
    2. **Responses**: Asks for name
        
        ![Screen Shot 2022-10-23 at 7.36.55 PM.png](%F0%9F%A4%96%20DialogFlow%20Chatbot%20in%20Flask%20+%20Kommunicate%20088cba029eb24ea0b804d7c709e83f22/Screen_Shot_2022-10-23_at_7.36.55_PM.png)
        
    
    ## **Get Name**
    
    1. **Training Phrases** and **Action and Parameter**s: Gave sample answers to “What is your name?” and labels these as name (`$name`)
        
        ![Screen Shot 2022-10-23 at 7.38.39 PM.png](%F0%9F%A4%96%20DialogFlow%20Chatbot%20in%20Flask%20+%20Kommunicate%20088cba029eb24ea0b804d7c709e83f22/Screen_Shot_2022-10-23_at_7.38.39_PM.png)
        
        ![Screen Shot 2022-10-23 at 7.38.56 PM.png](%F0%9F%A4%96%20DialogFlow%20Chatbot%20in%20Flask%20+%20Kommunicate%20088cba029eb24ea0b804d7c709e83f22/Screen_Shot_2022-10-23_at_7.38.56_PM.png)
        
    2. **Responses**: Gets the `name`, and asks for delivery inquiry
        
        ![Screen Shot 2022-10-23 at 7.41.16 PM.png](%F0%9F%A4%96%20DialogFlow%20Chatbot%20in%20Flask%20+%20Kommunicate%20088cba029eb24ea0b804d7c709e83f22/Screen_Shot_2022-10-23_at_7.41.16_PM.png)
        
    
    ## Delivery Inquiry
    
    1. **Training Phrases** and **Action and Parameter**s: Gave sample phrases for delivery inquiry. Expected parameters would be address (`$address`) and the date (`$date`) of delivery
        
        ![Screen Shot 2022-10-23 at 7.43.41 PM.png](%F0%9F%A4%96%20DialogFlow%20Chatbot%20in%20Flask%20+%20Kommunicate%20088cba029eb24ea0b804d7c709e83f22/Screen_Shot_2022-10-23_at_7.43.41_PM.png)
        
        ![Screen Shot 2022-10-23 at 7.43.54 PM.png](%F0%9F%A4%96%20DialogFlow%20Chatbot%20in%20Flask%20+%20Kommunicate%20088cba029eb24ea0b804d7c709e83f22/Screen_Shot_2022-10-23_at_7.43.54_PM.png)
        
    2. **Responses**: Confirms the delivery `address` and `date`
        
        ![Screen Shot 2022-10-23 at 7.44.50 PM.png](%F0%9F%A4%96%20DialogFlow%20Chatbot%20in%20Flask%20+%20Kommunicate%20088cba029eb24ea0b804d7c709e83f22/Screen_Shot_2022-10-23_at_7.44.50_PM.png)
        
    
2. Create Python Flask File
    
    This part is where the API gets the json payload from the Dialogflow. This only `['queryText']` and `['fulfillmentText']` which are the input of the user and output of the bot
    
    ```bash
    ...
    
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
    ...
    ```
    

1. Create Webhook fulfillment
    - On your local machine, run ngrok to get a local web URL to connect your Python service to Dialogflow via webhook
    - Add this URL to `Fulfillment` page in Dialogflow
2. Extra: [Kommunicate to integrate Chatbot to your website/other project](https://www.kommunicate.io/blog/integrate-dialogflow-cx-bot-website/)
    - On GCP, get `Agent ID` for Dialogflow agent project
    - On Kommunicate, add bot integration using agent ID
    - On Kommunicate, get script to integrate bot to your project. For this project, HTML javascript is used.

---

# Running the Service

## VirtualEnv and Dependencies Installation

Before running the API, create a virtual environment and install the dependencies in the **requirements.txt** file.

```bash
$ virtualenv chatbot
$ source chatbot/bin/activate
(chatbot)$ pip3 install -r path/to/requirements.txt
```

## Get ngrok URL and paste to Dialogflow Fulfillment

- go to folder containing ngrok.exe and run

```bash
./ngrok http 5000
```

- get `forwarding URL` and paste to Webhooks URL in dialogflow

## Testing

To run the simple python service, simply run it via:

```bash
(chatbot)$ python3 app.py
```

To open chatbot UI, simply open HTML file

DEMO:

[https://drive.google.com/file/d/1k9rqxDFoNZWLcWEBL5ellVICnoI1Rzt6/view?usp=sharing](https://drive.google.com/file/d/1k9rqxDFoNZWLcWEBL5ellVICnoI1Rzt6/view?usp=sharing)

# References

[Dialogflow Tutorial](https://www.kommunicate.io/blog/create-chatbot-in-flask-and-python/)

[Dialogflow + Kommunicate Tutorial](https://www.kommunicate.io/blog/integrate-dialogflow-cx-bot-website/)

[Dialogflow Video](https://www.youtube.com/watch?v=lKNaklJwNzk)