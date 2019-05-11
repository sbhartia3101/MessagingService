from flask import render_template, redirect, request, flash
from twilio.twiml.messaging_response import MessagingResponse

from app import app
from app.forms import KeywordForm, MessageForm
from resources.Keyword import KeywordResource
from resources.User import UserResource
from resources.SendMsg import SendMsgResource


@app.route('/')
@app.route('/keyword', methods=['GET', 'POST'])
def keyword():
    form = KeywordForm()
    keyword = KeywordResource().getKeyword()
    form.keyword_placeholder = keyword.keyword
    form.auto_response_placeholder = keyword.auto_response
    form.invalid_response_placeholder = keyword.invalid_response
    if request.method == 'POST':
        response, status = KeywordResource().post()
        if status == 201:
            message = "Keyword Replaced Successfully!"
        else:
            message = response['message']
        flash(message)
        return render_template('keyword.html', title='Gap', form=form)
    return render_template('keyword.html', title='Gap', form=form)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    # form = MessageForm()
    # form.receivers = SendMsgResource().getUsers()
    if request.method == 'POST':
        response, status = SendMsgResource().post()
        if status == 201:
            message = "Message sent Successfully!"
        else:
            message = response['message']
        flash(message)

        return render_template('messages.html', title='Gap', form= MessageForm())

    form = MessageForm()
    form.receivers = SendMsgResource().getUsers()
    return render_template('messages.html', title='Gap', form=form)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    print(request.values)
    received_message = request.values.get('Body', None)
    sender = request.values.get('From', None)

    keyword_data = list(KeywordResource().get())[0]['data'][0]
    print(keyword_data)
    keyword = keyword_data['keyword']

    if keyword == received_message:
        resp.message(keyword_data['auto_response'])
        UserResource().addUser(sender)
    else:
        resp.message(keyword_data['invalid_response'])

    return str(resp)



