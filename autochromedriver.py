from requests import get
from io import BytesIO
from selenium import webdriver
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os
class ChromeDriverTesterException(Exception):pass
class AutoChromedriverDownload:
    def test(self, expected_path = "chromedriver.exe", Windows = True):
        self.expected_path = expected_path
        try:
            driver = webdriver.Chrome(expected_path)
            driver.quit()
            return 1
        except:  
            page = get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
            latest = BeautifulSoup(page.content, 'html.parser')
            self.driverdownload(Windows, str(latest))            
            try:
                driver = webdriver.Chrome(expected_path)
                driver.quit()
                return 2
            except:
                raise ChromeDriverTesterException("Please make sure your chrome is up-to-date. Try again!")
        return 0
    def driverdownload(self, win, version):
        z = ZipFile(BytesIO(get("https://chromedriver.storage.googleapis.com/{}/chromedriver_win32.zip".format(version, "win32" if win else "mac64")).content))
        z.extractall(path = os.path.split(self.expected_path)[0])

