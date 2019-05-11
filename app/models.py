from marshmallow import fields

from app import db, ma


class Keywords(db.Model):
    __tablename__ = 'keywords'
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(100), nullable=False)
    auto_response = db.Column(db.String(200), nullable=False)
    invalid_response = db.Column(db.String(500), nullable=False)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(10), nullable=False)


class KeywordsSchema(ma.Schema):
    id = fields.Integer()
    keyword = fields.String(required=True)
    auto_response = fields.String(required=True)
    invalid_response = fields.String(required=True)


class UsersSchema(ma.Schema):
    id = fields.Integer()
    mobile_number = fields.String(required=True)
