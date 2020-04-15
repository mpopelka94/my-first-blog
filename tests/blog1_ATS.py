import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "mpopelka"
       pwd = "Aklepop1994!"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(3)
       elem.send_keys(Keys.RETURN)
       driver.get("http://127.0.0.1:8000")
       assert "Logged In"
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
       time.sleep(5)
       elem = driver.find_element_by_id("id_title")
       elem.send_keys("Selenium Test Post")
       elem = driver.find_element_by_id("id_text")
       elem.send_keys("Hi Callie! This is my test post!")
       elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
       driver.get("http://127.0.0.1:8000/admin/")
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/th/a").click()
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr/th/a").click()
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys("Matthew")
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys("Popelka")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()

       driver.get("http://127.0.0.1:8000/admin/auth/user/")
       time.sleep(5)
       driver.get("http://127.0.0.1:8000/admin/auth/user/")

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
