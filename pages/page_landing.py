from selenium.webdriver.common.by import By
from pages.page import BasePage
import hashlib


class RescaleLandingPage(BasePage):
    url = BasePage.baseurl

    new_job_button = (By.XPATH, "//SPAN[@class='dn dib-l nowrap']")
    upload_from_this_computer = (
    By.XPATH, "//div[@class='rescale-blue b input-from-computer']")
    file_input = (By.XPATH, "//div[@class='btn btn-default bl-0 br0 w-100 pa0']//input[@name='file']")
    upload_file_xpath = "//div[@class='editable-input']//a[contains(text(),'{}')]"
    menu_files = (By.XPATH, "//li[@id='menuFiles']")

    def upload_file(self, file_name):
        self.click(self.new_job_button)
        self.send_keys(file_name, self.upload_from_this_computer)

    def validate_file_uploaded_to_ui(self, file_name):
        self.click(self.menu_files)
        file_check = (By.XPATH, self.upload_file_xpath.format(file_name))
        if self.wait_for_element(file_check, wait=15):
            file_found = self.find_element_by(*file_check)
            if file_found:
                print('File uploaded = {}'.format(file_found.text))
            else:
                print('File failed to upload.')

    def download_file_from_ui(self, file_name):
        self.click(self.menu_files)
        download_file = (By.XPATH, self.upload_file_xpath.format(file_name))
        self.click(download_file)

    def validate_file_integrity(self, path_to_file):
        file_hash = hashlib.md5(open('{}'.format(path_to_file), 'rb').read()).hexdigest()
        return file_hash


