from flask import request, jsonify
from flask_restful import Resource
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from app import app
from crossdomain import crossdomain
from resources.User import UserResource


class SendMsgResource(Resource):
    # @crossdomain(origin='*')
    def post(self):
        # json_data = request.get_json(force=True)
        json_data = request.form.to_dict()
        print(json_data)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        msg = json_data['msg']
        receiver = json_data.get('receiver')
        self.SENDER = app.config["TWILIO_NUMBER"]
        isBlast = json_data.get('isBlast')

        account_sid = app.config["TWILIO_ACCOUNT"]
        auth_token = app.config["TWILIO_TOKEN"]
        client = Client(account_sid, auth_token)

        # if its an individual message request
        if isBlast == 'False':
            if not receiver or len(receiver) == 0:
                return {'status': 'failed', 'message': 'No number provided!'}, 400
            elif not self.isUserOptedIn(receiver):
                return {'status': 'failed', 'message': 'Mobile Number not opted in!'}, 400
            else:
                message_sid = self.sendMsg(client, msg, receiver)
                response = {"status": 'success', 'data': message_sid}
                return response, 201
        # if its a blast message request
        else:
            response = self.send_blast_msg(client, msg)
            return {"status": 'success', 'data': response}, 201

    @crossdomain(origin='*')
    def options(self):
        # json_data = request.get_json(force=True)
        json_data = request.form.to_dict()
        print(json_data)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        msg = json_data['msg']
        receiver = json_data.get('receiver')
        self.SENDER = app.config["TWILIO_NUMBER"]
        isBlast = json_data.get('isBlast')

        account_sid = app.config["TWILIO_ACCOUNT"]
        auth_token = app.config["TWILIO_TOKEN"]
        client = Client(account_sid, auth_token)

        # if its an individual message request
        if isBlast == 'False':
            if not receiver or len(receiver) == 0:
                return {'status': 'failed', 'message': 'No number provided!'}, 400
            elif not self.isUserOptedIn(receiver):
                return {'status': 'failed', 'message': 'Mobile Number not opted in!'}, 400
            else:
                message_sid = self.sendMsg(client, msg, receiver)
                response = {"status": 'success', 'data': message_sid}
                return response, 201
        # if its a blast message request
        else:
            response = self.send_blast_msg(client, msg)
            return {"status": 'success', 'data': response}, 201

    def send_bulk_msg(self, client, msg):
        receivers = self.getUsers()
        binding = list()
        binding_data = dict()
        binding_data["binding_type"] = "sms"
        print(receivers)

        for receiver in receivers:
            binding_data["address"] = receiver
            binding.append(binding_data.copy())

        print(binding)
        notification = client.notify.services(app.config["TWILIO_SSID"]).notifications.create(
            to_binding=binding, body=msg)
        return notification

    def send_blast_msg(self, client, msg):
        receivers = self.getUsers()
        message_sids = list()
        for receiver in receivers:
            # producer.send(topic, {"body": msg, "to":receiver})
            message_sids.append(self.sendMsg(client, msg, receiver))
        response = jsonify({"status": 'success', 'data': message_sids})
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def sendMsg(self, client, msg, receiver):
        try:
            message = client.messages.create(
                from_=self.SENDER,
                body=msg,
                to=receiver
            )
            return message.sid
        except TwilioRestException as ex:
            print(ex)
            return ""

    def isUserOptedIn(self, receiver):
        mobile_number = receiver.replace("+1", "")
        return UserResource().isUserOptedIn(mobile_number)

    def getUsers(self):
        receivers = list()
        user_data = list(UserResource().get())[0]['data']

        for user in user_data:
            receivers.append("+1" + user['mobile_number'])
        print('in users api')
        print(receivers)
        return receivers
