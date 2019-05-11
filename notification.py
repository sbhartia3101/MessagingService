from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account = {{twilio-account}}
token = {{twilio-token}}
client = Client(account, token)

binding1 = '{"binding_type":"sms","address":{{twilio-number}}}'
notification = client.notify.services("IS7ab0037fdef46943ed6829ac36f6a9fc") \
    .notifications.create(to_binding=[binding1], body="Hello")

print(notification)
