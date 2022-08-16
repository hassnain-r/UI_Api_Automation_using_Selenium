import random
import string
from datetime import datetime

from resources.base_page import BurqBase
from resources.constants import *


class CreateDelivery(BurqBase):
    def __init__(self):
        super().__init__()

    def submit_get_quote_api(self, add1, add2):
        params = {
            "dropoff_address": add1,
            "pickup_address": add2
        }

        return self.session.post(
            url=f'{self.env_values("API_BASE_URL")}v1/quote', headers=self._get_headers(self.env_values("X_API_KEY")), data=params
        )

    @staticmethod
    def get_current_month_and_year():
        current_month = datetime.now().strftime('%B')
        current_year = datetime.now().strftime('%y')
        return current_month, current_year

    @staticmethod
    def _get_random_strings():
        random_string_f = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
        random_string_s = ''.join(random.choices(string.ascii_uppercase + string.hexdigits, k=2))
        return random_string_f, random_string_s

    def get_unique_config_id(self):
        current_month, current_year = self.get_current_month_and_year()
        random_string_f, random_string_s = self._get_random_strings()
        return f'{random_string_f}_{random_string_s}_{current_month}{current_year}'
