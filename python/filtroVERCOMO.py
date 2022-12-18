import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


"""seteamos el webdriver"""
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains

website = "https://bertoldi.com.ar/"


driver.maximize_window()
time.sleep(2)
driver.get(website)

link2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[3]")
link2.click()
time.sleep(2)


#SCROLL
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(2)

filtro1 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[1]")
filtro1.click()
time.sleep(2)

filtro2 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[2]")
filtro2.click()
time.sleep(2)

filtro3 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[3]")
filtro3.click()
time.sleep(2)

filtro4 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[4]")
filtro4.click()
time.sleep(2)

filtro5 = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/span[5]")
filtro5.click()
time.sleep(2)

driver.get(website)
time.sleep(2)