from flask import Blueprint
from flask_restful import Api


from resources.Keyword import KeywordResource
from resources.SendMsg import SendMsgResource
from resources.User import UserResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(KeywordResource, '/Keyword')
api.add_resource(UserResource, '/User')
api.add_resource(SendMsgResource, '/send_msg')

