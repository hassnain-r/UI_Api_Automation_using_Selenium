"""
base class for page objects
"""
import requests
import json
import logging
from resources.constants import *
import os
from dotenv import load_dotenv, find_dotenv


class BurqBase(object):
    """
    Base class for page objects.
    """

    def __init__(self):
        """
        Initializing the session.
        """
        self.session = requests.session()

    @staticmethod
    def env_values(env_name):
        load_dotenv(find_dotenv())
        return os.getenv(env_name)

    @staticmethod
    def verify_keys_exist_with_valid_value_type(response_body, keys_list, value_type=str):
        """
        verify each entry exit in response body with valid value and type
        :return (bool) True if all entries valid
        """
        for key in keys_list:
            value = response_body[key]
            if value and type(value) == value_type:
                continue
            raise Exception(RESULTS_NOT_FOUND.format(key))

        return True

    @staticmethod
    def verify_key_exist_with_valid_value_type(response_body, key, value_type=str):
        """
        verify each entry exit in response body with valid value and type
        :return (bool) True if all values matched
        """
        value = response_body[key]
        if not value and not isinstance(value, value_type):
            raise Exception(RESULTS_NOT_FOUND.format(key))
        return True

    @staticmethod
    def verify_value_exist_in_a_list(value, list_values):
        """
        validate value exist in a list
        :return (bool) True if exist
        """
        if value not in list_values:
            raise Exception(RESULTS_NOT_FOUND.format(value))
        return True

    @staticmethod
    def verify_value_not_exist(response_body, key, value=''):
        """
        validate value is empty
        :return (bool) True if not exist
        """
        result = response_body[key]
        if result != value:
            raise Exception(RESULTS_FOUND.format(result))
        return True

    def compare_expected_and_actual_results(self, response_body, keys, values_to_match):
        """
        base page method
        compare expected result with actual result
        :return (bool) True if matches
        """
        for key, value in zip(keys, values_to_match):
            self.compare_expected_and_actual_result(response_body, key, value)
            logging.info(f"{key} key found having value as: {value}")
        return True

    @staticmethod
    def compare_expected_and_actual_result(response_body, expected_key, actual):
        """
        base page method
        compare expected result with actual result
        :return (bool) True if matches
        """
        expected = response_body.get(expected_key)
        results_matched = actual == expected or actual in expected
        if not results_matched:
            raise Exception(FAILED_TO_MATCH_VALUES.format(expected, actual))
        return results_matched

    @staticmethod
    def compare_expected_and_actual_values(expected, actual):
        """
        base page method
        compare expected result with actual result
        :return (bool) True if matches
        """
        results_matched = actual == expected or actual in expected
        if not results_matched:
            raise Exception(FAILED_TO_MATCH_VALUES.format(expected, actual))
        return results_matched

    @staticmethod
    def verify_entry(response_body, value, bool_val):
        """
        compare entry with name
        :return (bool) True if matched
        """
        entry_value = response_body[value]
        if entry_value != bool_val:
            raise Exception(FAILED_TO_FIND_VALUE_IN_RESPONSE.format(value, response_body))
        return True

    def verify_entries(self, response_body, keys, bool_val):
        for each in keys:
            self.verify_entry(response_body, each, bool_val)
        return True

    @staticmethod
    def get_status_code(response):
        """
        get response
        :return status code
        """
        return response.status_code

    @staticmethod
    def get_content(response):
        """
        get response
        :return python object
        """
        return json.loads(response.text)

    def _check_response(self, response, email):
        """
        Check whether a response was successful.
        """
        if response.status_code != 200:
            raise Exception(f'API request failed with following error code: {str(response.status_code)} and text: '
                            f'{str(response.status_code)} with user email {email}')

    def _get_headers(self, x_api_key):
        return {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'x-api-key': x_api_key
        }

    def _post_headers(self, cookie):
        headers = {
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en',
            'content-type': 'application/json'
        }
        if cookie:
            headers.update(cookie)
        return headers

    def _get(self, url, token, allow_redirects=True):
        """
        Make a GET request to the server.
        Make the response to fail if verification string is not present in the response
        """
        with self.session.get(
                url,
                verify=False,
                headers=self._get_headers(token),
                allow_redirects=allow_redirects
        ) as response:
            if response.status_code == 402:
                raise Exception(f'API request failed with following error code: {str(response.status_code)} ')
        return response

    def _post(self, url, params, cookie, allow_redirects=True):
        """
        Make a POST request to the server.
        Skips SSL verification and sends the CSRF cookie.
        """
        with self.session.post(
                url,
                json=params,
                verify=False,
                headers=self._post_headers(cookie),
                allow_redirects=allow_redirects
        ) as response:
            if response.status_code == 402:
                raise Exception(f'API request failed with following error code: {str(response.status_code)}')
        return response
