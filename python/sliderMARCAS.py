import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


linkMARCAS = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]")
linkMARCAS.click()
time.sleep(2)

if linkMARCAS == "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]":
	print ("El slider de marcas se visualiza correctamente")
else: 
	print("No se visualiza el slider de marcas")