import uuid
import _codecs
import codecs
import re
import requests
from resources.base_page import BurqBase
from resources.constants import *
from resources.utils import *


class LoginPage(BurqBase):

    """
    Base class for page objects.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super().__init__()

    def get_state_token(self):
        response = requests.get(url=f'{self.env_values("BASE_URL")}api/auth/login', allow_redirects=True)
        breakpoint()
        return re.search(r'value="(.*?)\"', response.text).group(1)

    def hit_login_api(self):
        token = self.get_state_token()
        data = {"state": str(token),
                "username": "devops@burqup.com",
                "password": "KvFDkgZ6@a3fXx6Q",
                "action": "default"}
        url = f'https://auth.burqup.com/u/login?state={token}'

        response = requests.post(url=url, params=data, allow_redirects=True)
        breakpoint()
