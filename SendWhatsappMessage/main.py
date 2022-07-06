from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

nav = webdriver.Chrome()
nav.get('https://web.whatsapp.com')
sleep(25)
navegacao = nav.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
navegacao.click()
navegacao.send_keys('euSÓ')
navegacao.send_keys(Keys.ENTER)
sleep(2)
navegacao.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').click()
sleep(2)
navegacao.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
sleep(2)
navegacao.send_keys(Keys.ENTER)