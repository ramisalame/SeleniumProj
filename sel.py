import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r"C:\Users\Rami Salame\OneDrive\Desktop\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.leagueoflegends.com/en-us/news/tags/patch-notes/")

text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/section/section[2]/div/div/div[3]/div/div/blockquote");

print(text)



