# Twillio-marketing for GAP

## UI
Please watch the <B>LIVE Demo</B> of the Application at: http://recordit.co/8xzfK7oUJw

## Server Details

### Link to the application : <a>https://emotiveai.herokuapp.com</a>

### Local Environment Deployment
1. Download the Project provided in the zip file.
2. Create a new virtualenv
  ```
    virtualenv venv
    source venv/bin/activate
  ```
3. Install the dependencies
   ```python
     pip install -r requirements.txt
   ```
4. Add the configurations
   
   Alter the .env file as per local configurations. Execute the env file.
   ```
   source .env
   ```
5. Run the main python endpoint file emotiveai.py which defines the route for the APIs
   ```python
   python emotiveai.py
   ```
6. Run the migrations
   ```python
   flask db init
   flask db migrate
   flask db upgarde
   ```
7. Start the server
   ```python
   flask run
   ```
8. Your server can be accessed at: <a>http://localhost:5000</a>

9. To create webhooks to receive a reply from the User, install <a href="https://ngrok.com/download">ngrok</a> and host it on http 5000. Use the forwarding address to configure the Twilio Messaging Service when a Message comes in.
  ```
    ngrok http 5000
  ```  
 
### APIs

|Endpoint|Method|Use|
|--------|------|---|
|/keyword| POST | URL used to add keyword|
|/messages| POST | URL used to send messages to opted-in users (blast or individual)|
|/sms| POST | Callback URL for wehooks for Twillio, to respond to a keyword|

### Twillio APIs used:

1. Send an SMS using the Programmable SMS API - https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python?code-sample=code-send-an-sms-using-the-programmable-sms-api&code-language=Python&code-sdk-version=6.x#linkcode
This API is used to send individual text messages to mobile numbers which are opted in through the keyword.
2. Respond to an incoming text message - https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python#linkcode
This API is used to reply individuals for their keyword sent.

### Twillio API Challenges faced:

1. Notification API (Blast messaging feature) is a part of Messaging Service while the Reply to User API uses the Webhook service. Both Messaging and Webhook service cannot be enabled together for a single number.
2. Every number that is sent a message from the Twillio owned number, has to be added to the Verified numbers list on the Twillio account. If the number is not verified, then it will not recieve the message. This is because, the Twillio Account is a <b>TRIAL ACCOUNT</b> right now.


## Assumptions
1. Only one keyword can be present in the keywords table. Everytime a new keyword is added, the remaining keywords are deleted.
2. 10 digit mobile numbers are stored in the users table. As of now, only the US country code is added to the mobile numbers.
3. Keyword matching is case-sensitive.
4. Every number that is sent a message from the Twillio owned number, has to be added to the Verified numbers list on the Twillio account. If the number is not verified, then it will not recieve the message. This is because, the Twillio Account is a <b>TRIAL ACCOUNT</b> right now.
