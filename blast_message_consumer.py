from twilio.rest import Client
from kafka import KafkaConsumer
from json import loads

from app import app
from resources.SendMsg import SendMsgResource
from twilio.base.exceptions import TwilioRestException

consumer = KafkaConsumer('bulk-message', bootstrap_servers=['0.0.0.0:9092'], group_id='my-group', enable_auto_commit=True,
                         auto_offset_reset = 'earliest', value_deserializer=lambda x: loads(x.decode('utf-8')))

account_sid = app.config["TWILIO_ACCOUNT"]
auth_token = app.config["TWILIO_TOKEN"]
client = Client(account_sid, auth_token)


def kafkastream():
    sender_resource = SendMsgResource()
    sender_resource.SENDER = app.config["TWILIO_NUMBER"]
    for msg in consumer:
        try:
            print(sender_resource.sendMsg(client, msg.value["body"], msg.value["to"]))
        except TwilioRestException as ex:
            print(ex)

if __name__ == "__main__":
    while True:
        kafkastream()
