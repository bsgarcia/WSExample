from channels.auth import channel_session_user
from channels import Group
import json


@channel_session_user
def ws_connect(message):

    Group('test').add(message.reply_channel)

    message.reply_channel.send({
        'accept': True,
        'text': "Connection accepted"
    })


@channel_session_user
def ws_receive(message):

    try:
        data = json.loads(message.content.get('text'))
    except TypeError:
        data = message.content.get('text')

    Group('test').send({"text": f"Tu me dis {data} ? Je réponds TAMERE"})


@channel_session_user
def ws_disconnect(message):

    # room_id = message.channel_session["room-group"]
    Group('test').discard(message.reply_channel)
