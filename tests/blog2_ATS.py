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
       driver.get("http://127.0.0.1:8000/admin")
       assert "Logged In"
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/a").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr/th/a").click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_text")
       elem.send_keys(" This post is now so much better!")
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()

       driver.get("http://127.0.0.1:8000")
       time.sleep(5)
       driver.get("http://127.0.0.1:8000")

   def tearDown(self):
       self.driver.close()


if __name__ == "__main__":
   unittest.main()