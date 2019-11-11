import os
import unittest
import rescale_config
from pages import page_landing, page_login
from helper import config_browser


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = config_browser.initiate_driver(str(os.path.basename(__file__)), self._testMethodName)
        self.login_page = page_login.LoginPage(self.driver)
        self.rescale_landing_page = page_landing.RescaleLandingPage(self.driver)
        self.login_page.navigate()
        self.user_email = rescale_config.login_user
        self.user_password = rescale_config.login_password
        self.file_name = '{}{}'.format(rescale_config.upload_dir, rescale_config.upload_file)
        self.download_file_name = '{}{}'.format(rescale_config.download_dir, rescale_config.upload_file)

        #Log into the Web interface
        self.login_page.enter_email_address(self.user_email)
        self.login_page.enter_password(self.user_password)

    def tearDown(self):
        self.driver.quit()

    def test_upload_file(self):
        self.rescale_landing_page.upload_file(self.file_name)
        self.rescale_landing_page.validate_file_uploaded_to_ui(self.file_name)
        # validate file integrity before
        file_hash_before = self.rescale_landing_page.validate_file_integrity(self.file_name)
        # download file from the UI
        self.rescale_landing_page.download_file_from_ui(self.file_name)
        file_hash_after = self.rescale_landing_page.validate_file_integrity(self.download_file_name)
        self.assertEqual(file_hash_before, file_hash_after)



