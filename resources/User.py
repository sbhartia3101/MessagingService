from flask import request
from flask_restful import Resource

from app.models import db, Users, UsersSchema

users_schema = UsersSchema(many=True)
user_schema = UsersSchema()


class UserResource(Resource):
    def get(self):
        users = Users.query.all()
        users = users_schema.dump(users).data
        return {'status': 'success', 'data': users}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        if self.isUserOptedIn(data['mobile_number']):
            return {'message': 'Mobile Number already exists'}, 400

        result = self.addUser(data['mobile_number'])

        return {"status": 'success', 'data': result}, 201

    def addUser(self, mobile_number):
        mobile_number = mobile_number.replace("+1", "")
        print(mobile_number)
        if not self.isUserOptedIn(mobile_number):
            user = Users(
                mobile_number=mobile_number
            )
            db.session.add(user)
            db.session.commit()
            result = user_schema.dump(user).data
            print(result)
            return result
        else:
            Users.query.filter_by(mobile_number=mobile_number).delete()

    def isUserOptedIn(self, mobile_number):
        user = Users.query.filter_by(mobile_number=mobile_number).first()
        if user:
            return True
        else:
            return False
