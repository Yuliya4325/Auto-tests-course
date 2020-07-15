from selenium import webdriver
import time

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_css_selector("[name = 'firstname']")
	input1.send_keys("Ivan")

	input2 = browser.find_element_by_css_selector("[name = 'lastname']")
	input2.send_keys("Petrov")

	input3 = browser.find_element_by_css_selector("[name = 'email']")
	input3.send_keys("petrov@mail.ru")

	

	import os
	option1 = browser.find_element_by_id("file")
	current_dir = os.path.abspath(os.path.dirname("/Users/Yuliya1/environments/section2/"))
	file_path = os.path.join(current_dir, 'file.txt')
	option1.send_keys(file_path)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	print(os.path.abspath(__file__))

finally:
    time.sleep(20)
    browser.quit()	