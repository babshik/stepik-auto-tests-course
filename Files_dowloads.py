import os

from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

First_name = browser.find_element_by_css_selector('input[name="firstname"]')
First_name.send_keys("Sasha")
Last_name = browser.find_element_by_css_selector('input[name="lastname"]')
Last_name.send_keys("Sasha")
Email = browser.find_element_by_css_selector('input[name="email"]')
Email.send_keys("Sasha")
file = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(file, "file.txt")
element = browser.find_element_by_id("file")
element.send_keys(file_path)
submit = browser.find_element_by_tag_name("button")
submit.click()



