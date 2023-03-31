import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r"C:\Users\Rami Salame\OneDrive\Desktop\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("https://www.google.com")

search_box = driver.find_element_by_name("q")

search_box.send_keys("Testing Sel")

search_box.submit()







