from burq_api.api_pages.create_delivery import CreateDelivery
from resources.constants import *
import logging


class TestLogin:
    delivery = CreateDelivery()

    def test_and_validate_get_quote_with_valid_address(self):
        """
        submit an api ("https://preprod-api.burqup.com/v1/quotes") with valid pickup and dropoff location and validate
        - status code to be 200
        - id key exist with some value in it (will store that value to perform delivery)
        - fee key exist with some valid int value
        - created key exist and must have time field in the value
        - currency key exist with value to be USD
        - service key exist with valid name

        """
        response = self.delivery.submit_get_quote_api(dropoff_address, pickup_address)
        response_body = self.delivery.get_content(response)
        logging.info(response_body)
        status_code = self.delivery.get_status_code(response)
        logging.info(f"status code: {status_code}")
        assert STATUS_CODE_GOOD == status_code
        assert self.delivery.compare_expected_and_actual_result(response_body, currency_key, "USD")
        logging.info("currency key exist with value to be USD")
