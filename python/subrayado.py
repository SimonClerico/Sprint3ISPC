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


#Validar subrayado de los links del nav al posicionar el cursor encima
website = "https://bertoldi.com.ar/"


driver.maximize_window()
time.sleep(2)
driver.get(website)


#INICIO

x= driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[1]")
#Creating object of an Actions class
a = ActionChains(driver)
#Performing the mouse hover action on the target element.
a.move_to_element(x).perform()
time.sleep(2)


#MARCAS
x= driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]")
#Creating object of an Actions class
a = ActionChains(driver)
#Performing the mouse hover action on the target element.
a.move_to_element(x).perform()
time.sleep(2)

#GIFTCARD
x= driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[3]")
#Creating object of an Actions class
a = ActionChains(driver)
#Performing the mouse hover action on the target element.
a.move_to_element(x).perform()
time.sleep(2)


#ACADEMIA
x= driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[4]")
#Creating object of an Actions class
a = ActionChains(driver)
#Performing the mouse hover action on the target element.
a.move_to_element(x).perform()
time.sleep(2)




#CLUB BERTOLDI
x= driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[5]")
#Creating object of an Actions class
a = ActionChains(driver)
#Performing the mouse hover action on the target element.
a.move_to_element(x).perform()
time.sleep(2)


#PROMOS PROFESIONALES
x= driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[6]")
#Creating object of an Actions class
a = ActionChains(driver)
#Performing the mouse hover action on the target element.
a.move_to_element(x).perform()
time.sleep(2)

driver.get(website)
time.sleep(2)