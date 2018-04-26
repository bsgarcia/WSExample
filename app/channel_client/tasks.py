from channels import Group
from app.channel_client import helpers
import json


def get_user_id(kwargs):

    who = kwargs['who']

    string = helpers.get_user_id(who)

    response = {
        "message": string
    }

    Group('test').send({'text': json.dumps(response)}, immediately=True)

