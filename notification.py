from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account = "ACd29dce7470e6ec135d024c91579ae96b"
token = "0dbb6d285298369e081e93bfc2f9aae5"
client = Client(account, token)

binding1 = '{"binding_type":"sms","address":"+19174787238"}'
notification = client.notify.services("IS7ab0037fdef46943ed6829ac36f6a9fc") \
    .notifications.create(to_binding=[binding1], body="Hello Sweety")

print(notification)