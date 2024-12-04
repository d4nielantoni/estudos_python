from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from credenciais import EMAIL, SENHA
import chromedriver_autoinstaller

# Instala automaticamente o chromedriver compatível
chromedriver_autoinstaller.install()

# Configuração do WebDriver
driver = webdriver.Chrome()

try:
    driver.get('https://mail.google.com/')
    
    email_input = driver.find_element(By.ID, 'identifierId')
    email_input.send_keys(EMAIL)
    email_input.send_keys(Keys.ENTER)
    time.sleep(2) 
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'Passwd'))
    )
    password_input.send_keys(SENHA)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5) 

    spam_link = driver.find_element(By.XPATH, "//a[contains(@href, '#spam')]")
    spam_link.click()
    time.sleep(3) 

    select_all_checkbox = driver.find_element(By.XPATH, "//div[@role='checkbox']")
    select_all_checkbox.click()
    time.sleep(1)

    delete_button = driver.find_element(By.XPATH, "//div[@aria-label='Excluir']")
    delete_button.click()
    time.sleep(2)

finally:
    driver.quit()