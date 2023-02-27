import vk_api
import requests
from random import randrange

from typing import Optional
from .client_types import SexEnum, MaritalStatusEnum
from vk_api.longpoll import VkLongPoll, VkEventType


class APIClient:
    base_url: str = 'https://oauth.vk.com'

    def __init__(self, app_id: str, app_secret: str, vk_object: Optional[object]):
        self._settings = {
            'app_id': app_id,
            'app_secret': app_secret
        }
        self._vk = vk_object

    def _meth_url(self, method_name: str) -> str:
        return '/'.join((self.base_url, method_name or ''))

    def _get_app_token(self, client_id: int, scope: int) -> str:
        params = {
            'client_id': client_id,
            'redirect_uri': 'https://oauth.vk.com/blank.html',
            'display': 'mobile',
            'scope': scope,
            'response_type': 'code',
            'state': 'fa'
        }

        resp = requests.get(
            self._meth_url('authorize'),
            params=params,
            allow_redirects=True
        )
        return resp.json()

    def login(self, ):
        token = self._get_app_token(self._settings['app_id'], 2)
        self._vk = vk_api.VkApi(
            app_id=self._settings['app_id'],
            client_secret=self._settings['app_secret']
            token=token
        )

    def get_poll_object(self):
        if not self._vk:
            raise Exception('API wrapper instance not created yet')

        return VkLongPoll(self._vk)

    def write_msg(user_id, message):
        self._vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})

    def search_users(
        self,
        age: Optional[Tuple[int, int]],
        sex: SexEnum,
        city: Optional[str]=None,
        marital_status: Optional[MaritalStatusEnum]=None,
        **kwargs
    ):
        age_from, age_to = age
        search_params = {
            'age_from': age_from,
            'age_to': age_to,
            'sex': sex
        }
        if marital_status:
            search_params['status'] = marital_status

        if city:
            search_params['hometown'] = city.strip().lower()

        if kwargs:
            search_params.update(kwargs)
        
        ret = self._vk.method('users.search', search_params)
        return ret
