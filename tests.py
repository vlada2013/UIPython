import pytest
import time
from automation_practice_page import AutomationPracticePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestDemo:

    def test_demo(self):
        serv = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=serv)
        url = 'https://rahulshettyacademy.com/AutomationPractice/'
        driver.get(url)

        page = AutomationPracticePage(driver)

        page.enter_text("Sample text")
        page.close_window()

        time.sleep(5)




