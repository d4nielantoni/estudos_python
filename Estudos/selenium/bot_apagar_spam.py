from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from credenciais import EMAIL, SENHA
import chromedriver_autoinstaller
import undetected_chromedriver as uc

driver = uc.Chrome()

try:
    driver.get('https://mail.google.com/')
    
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'identifierId'))
    )
    email_input.send_keys(EMAIL)
    email_input.send_keys(Keys.ENTER)

    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'Passwd'))
    )
    password_input.send_keys(SENHA)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    more_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Mais marcadores']"))
    )
    more_button.click()
    time.sleep(2)

    spam_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#spam') and contains(@class, 'J-Ke n0')]"))
    )
    spam_link.click()
    time.sleep(3)

    while True:
        checkboxes = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@role='checkbox' and contains(@id, ':lv')]"))
        )
        if not checkboxes:
            break
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
                time.sleep(0.5) 

    delete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Excluir']"))
    )
    delete_button.click()
    time.sleep(2)

finally:
    driver.quit()