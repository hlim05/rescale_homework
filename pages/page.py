from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    """
    Base class the rest will inherit from
    """
    baseurl = 'https://platform.rescale.com/login/'

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_present(self, element_locator, wait=10):
        WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(element_locator))

    def wait_for_element_to_be_visible(self, element_locator, wait=10):
        self.wait_for_element_to_be_present(element_locator, wait=wait)
        WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(element_locator))

    def send_keys(self, keys, element_locator):
        self.wait_for_element_to_be_visible(element_locator)
        element = self.find_element_by(*element_locator)
        element.send_keys(keys)

    def click(self, element_locator):
        self.wait_for_element_to_be_clickable(element_locator)
        element = self.find_element_by(*element_locator)
        element.click()

    def navigate(self, url=None):
        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.url)

    def find_element_by(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements_by(self, *loc):
        return self.driver.find_elements(*loc)

    def is_element_present(self, *loc):
        try:
            self.driver.find_element(*loc)
            return True
        except NoSuchElementException:
            return False

    def wait_for_element_to_be_clickable(self, element_locator, wait=10):
        self.wait_for_element_to_be_present(element_locator, wait)
        self.wait_for_element_to_be_visible(element_locator, wait)
        WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable(element_locator))

    def wait_for_element(self, loc, wait=15):
        try:
            WebDriverWait(self.driver, int(wait)).until(
                EC.presence_of_element_located(loc)
            )
            return self.is_element_present(*loc)
        except Exception as e:
            print(e)
