import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from typing import Optional
import undetected_chromedriver as uc

from src.library.dates import past_month_year
from src.utils import env


def gen_undetected_webdriver() -> Optional[tuple[WebDriver,  WebDriverWait]]:
    driver = uc.Chrome()
    wait = WebDriverWait(driver, 60)
    return driver, wait 


def find_click(wait: WebDriverWait, path: str, by = By.XPATH):
    element = wait.until(EC.element_to_be_clickable((by, path)))
    element.click()
    return element


def verify(wait: WebDriverWait, path: str, by = By.XPATH):
    wait_especial = WebDriverWait(wait, 2)
    element = wait_especial.until(EC.element_to_be_clickable((by, path)))
    return element


def verify_multi(wait: WebDriverWait, path: str, by = By.XPATH):
    for i in path:
        wait_especial = WebDriverWait(wait, 2)
        element = wait_especial.until(EC.element_to_be_clickable((by, path)))
        return element


def waiter_by(wait: WebDriverWait, path: str, by = By.XPATH):
    wait.until(EC.presence_of_element_located((by, path)))
    for _ in range(3):
        wait.until(EC.invisibility_of_element_located((by, path)))
        time.sleep(1)


def find_send(wait: WebDriverWait, path: str, keys: str, by = By.XPATH):
    element = wait.until(EC.element_to_be_clickable((by, path)))
    element.clear()
    element.send_keys(keys)
    return element


def find_click(wait: WebDriverWait, path: str, by = By.XPATH):
    element = wait.until(EC.element_to_be_clickable((by, path)))
    element.click()
    return element


def find(wait: WebDriverWait, path: str, by = By.XPATH):
    element = wait.until(EC.element_to_be_clickable((by, path)))
    return element


def find_presence(wait: WebDriverWait, path: str, by = By.XPATH):
    element = wait.until(EC.presence_of_element_located((by, path)))
    return element


def wait_loading(wait: WebDriverWait, driver: WebDriver, element_path):
    while True:
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, element_path)))
            break
        except TimeoutException:
            pass
        
    while True:
        try:
            driver.find_element(By.XPATH, element_path)
            time.sleep(1)
        except NoSuchElementException:
            break


def wait_presence(wait: WebDriverWait, driver: WebDriver, element):
    while True:
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, element)))
            break
        except TimeoutException:
            pass
        
    while True:
        try:
            driver.find_element(By.XPATH, element)
            time.sleep(1)
        except NoSuchElementException:
            break


def wait_attribute(wait: WebDriverWait, element):
    while True:
        loading = find_presence(wait, element)
        box_loading = loading.get_attribute('style')
        if 'display: none' in box_loading:
            time.sleep(5)
            break
        time.sleep(1)


def selenium_screenshot(driver: WebDriver, nome):
    path_capture_screenshot = f"{env.PATH_DRIVE}\\{past_month_year()}\\{nome}\\CND.png"
    driver.save_screenshot(path_capture_screenshot)
    print("SCREENSHOT")


def close_webdriver(driver: WebDriver):
    driver.delete_all_cookies()
    driver.quit()
    time.sleep(5)
