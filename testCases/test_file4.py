# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.service import Service


# class Test_Pytest:
#     def test_Credence_Url_010(self):
#         driver = webdriver.Chrome()
#         driver.get("https://credence.in/")
#         v = "Credence"
#         if driver.title in v:
#             print("You are at Right place")
#         else:
#             print("You are at Wrong place")

import logging

from selenium import webdriver
from selenium.webdriver.common.service import Service


class Test_Pytest:
    def test_Credence_Url_010(self):
        logging.basicConfig(level=logging.INFO)  # Configure logging
        logger = logging.getLogger(__name__)

        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        v = "Credence"
        if driver.title in v:
            logger.info("You are at the right place")
        else:
            logger.info("You are at the wrong place")
