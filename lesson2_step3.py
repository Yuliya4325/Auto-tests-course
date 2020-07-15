from selenium import webdriver
import time
import math

try:
   link = "http://suninjuly.github.io/selects1.html"
   browser = webdriver.Chrome()
   browser.get(link)
   
   num1_element = browser.find_element_by_id("num1")
   num1 = num1_element.text

   num2_element = browser.find_element_by_id("num2")
   num2 = num2_element.text
   
   sum_n = str(int(num1)+int(num2))

   from selenium.webdriver.support.ui import Select
   select = Select(browser.find_element_by_tag_name("select"))
   select.select_by_value(sum_n)

   button = browser.find_element_by_css_selector("button.btn")
   button.click()

finally:
   print(sum_n)
   time.sleep(10)
   browser.quit()
