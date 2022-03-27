from selenium.webdriver.common.by import By


class AutomationPracticePage:

    def __init__(self, driver):
        self.driver = driver
        driver.get("https://rahulshettyacademy.com/AutomationPractice/");
        self.autocomplete = self.driver.find_element(By.ID, 'autocomplete')

    def enter_text(self, text):
        self.autocomplete.send_keys(text)

    def close_window(self):
        self.driver.quit()