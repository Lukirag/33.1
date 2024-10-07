import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome('C:\chomedriver\chomedriver.exe')
    driver.get('https://lk.rt.ru/')
    WebDriverWait(driver, 10)
    driver.implicitly_wait(5)
    yield driver

    driver.quit()

def test_auth_page(driver):

    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
    driver.find_element(By.ID,'username').send_keys('')
    driver.find_element(By.ID, 'password').send_keys('')
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    assert driver.find_element(By.TAG_NAME, 'h2').text == "Главная"


def test_auth_page(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    driver.find_element(By.ID,'username').send_keys('')
    driver.find_element(By.ID, 'password').send_keys('')
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    assert driver.find_element(By.TAG_NAME, 'h2').text == "Главная"


def test_auth_page(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
    driver.find_element(By.ID,'username').send_keys('')
    driver.find_element(By.ID, 'password').send_keys('')
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    assert driver.find_element(By.TAG_NAME, 'h2').text == "Главная"


def test_auth_page(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-ls"]').click()
    driver.find_element(By.ID,'username').send_keys('')
    driver.find_element(By.ID, 'password').send_keys('')
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    assert driver.find_element(By.TAG_NAME, 'h2').text == "Главная"