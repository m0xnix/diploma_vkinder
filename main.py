import requests
from enum import Enum
from random import randrange
from typing import Tuple, Optional

import vk_api
from vk_api.longpoll import VkEventType

from ybvdl.client import APIClient
from ybvdl.db.engine import db_init
from ybvdl import settings as app_settings



if __name__ == '__main__':
    api_client = APIClient(app_settings.vk_app_id, app_settings.vk_app_secret)
    poll_obj = api_client.get_poll_object()


    for event in poll_obj.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:
                request = event.text
                search_users((10, 100), SexEnum.FEMALE)

                # if request == "привет":
                #     write_msg(event.user_id, f"Хай, {event.user_id}")
                # elif request == "пока":
                #     write_msg(event.user_id, "Пока((")
                # else:
                #     write_msg(event.user_id, "Не поняла вашего ответа...")
