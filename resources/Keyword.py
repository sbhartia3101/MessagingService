from flask import request,  jsonify
from flask_restful import Resource
# from Model import db, Keywords, KeywordsSchema
from crossdomain import crossdomain

from app.models import db, Keywords, KeywordsSchema
from app.forms import KeywordForm

keywords_schema = KeywordsSchema(many=True)
keyword_schema = KeywordsSchema()


class KeywordResource(Resource):
    def get(self):
        keywords = Keywords.query.all()
        keywords = keywords_schema.dump(keywords).data
        return {'status': 'success', 'data': keywords}, 200

    # @crossdomain(origin='*')
    def post(self):
        json_data = request.form.to_dict()
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = keyword_schema.load(json_data)
        if errors:
            return errors, 422
        keyword = Keywords.query.filter_by(keyword = data['keyword']).first()
        if keyword:
            return {'message': 'Keyword already exists'}, 400

        Keywords.query.delete()
        db.session.commit()

        keyword = Keywords(
            keyword=data['keyword'],
            auto_response = data['auto_response'],
            invalid_response = data['invalid_response']
        )
        db.session.add(keyword)
        db.session.commit()
        result = keyword_schema.dump(keyword).data

        # return {"status": 'success', 'data': result}, 201
        response = jsonify({"status": 'success', 'data': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 201

    @crossdomain(origin='*')
    def options(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = keyword_schema.load(json_data)
        if errors:
            return errors, 422
        keyword = Keywords.query.filter_by(keyword = data['keyword']).first()
        if keyword:
            return {'message': 'Keyword already exists'}, 400
        keyword = Keywords(
            keyword=data['keyword'],
            auto_response = data['auto_response'],
            invalid_response = data['invalid_response']
        )
        db.session.add(keyword)
        db.session.commit()
        result = keyword_schema.dump(keyword).data

        # return {"status": 'success', 'data': result}, 201
        response = jsonify({"status": 'success', 'data': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 201

    def getKeyword(self):
        keyword = Keywords.query.first()
        return keyword

