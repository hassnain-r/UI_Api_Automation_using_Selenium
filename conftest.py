import os

import pytest
from selenium import webdriver
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import logging

class SessionData:
    """class for keeping necessary session related info"""

    iteration_directory_base = None
    test_case_name = None
    iteration_directory = None
    configs = dict()


def pytest_configure(config):
    """
    called after command line options have been parsed
    and all plugins and initial conftest files been loaded
    """
    marker = config.getoption("-m")
    current_day = (datetime.now().strftime("%Y_%m_%d_[%H_%M]"))
    SessionData.configs['current_day'] = current_day
    iteration_name = f"Iteration_{current_day}"
    iteration_name = f'{marker}_{current_day}' if marker else iteration_name

    SessionData.iteration_directory_base = os.path.join(
        os.path.dirname(__file__), "results", iteration_name.lower())

    config.option.xmlpath = os.path.join(SessionData.iteration_directory_base, 'report.xml')
    config.option.htmlpath = os.path.join(SessionData.iteration_directory_base,
                                          f'{iteration_name}.html')
    config.option.allure_report_dir = os.path.join(SessionData.iteration_directory_base, "allure_report")


@pytest.fixture(scope="class")
def setup(request):
    load_dotenv(find_dotenv())
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(os.getenv("BASE_URL"))
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()


@pytest.fixture
def base_url(request):
    parameter = request.config.getoption("--x_api_key")
    os.environ["x_api_key"] = parameter
    return parameter


def pytest_addoption(parser):
    parser.addoption(
        "--x_api_key", action="store", default="",  help="token to access the api"
    )
