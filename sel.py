import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service(r"C:\Users\Rami Salame\OneDrive\Desktop\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.leagueoflegends.com/en-us/news/game-updates/patch-13-7-notes/")

element_xpath = "/html/body/div[2]/div[1]/div/section/section[2]/div/div/div[3]/div/div/blockquote"
element = driver.find_element(By.XPATH, element_xpath)

# Get the text of the element
text = element.text

# Print the text
print(text)




