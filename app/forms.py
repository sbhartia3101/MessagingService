from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Optional

from resources.SendMsg import SendMsgResource


class KeywordForm(FlaskForm):
    keyword = StringField('keyword', validators=[DataRequired()])
    auto_response = StringField('auto_response', validators=[DataRequired()])
    invalid_response = StringField('invalid_response', validators=[DataRequired()])
    save = SubmitField('save')


class MessageForm(FlaskForm):
    msg = StringField('msg', validators=[DataRequired()])
    mobile_number = StringField('mobile_number', validators=[Optional()])
    send = SubmitField('Send')


