import time
from typing import Optional
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from utils.variables import Paths
from utils.files_automator import data_mes_ano


def gen_browser() -> Optional[tuple[WebDriver, WebDriverWait]]:
    try:
        options = ChromeOptions()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--start-maximized")
        driver = Chrome(options=options)
        driver.set_page_load_timeout(60)
        wait = WebDriverWait(driver, 10)
        return driver, wait
    except Exception:
        return gen_browser()


def click(driver: WebDriver, path: str, by = By.XPATH):
    element = driver.find_element(by, path)
    element.click()
    return element


def selenium_screenshot(driver:WebDriver, nome, tipo):
    path_capture_screenshot = f"{Paths.PATH_DRIVE}\\{data_mes_ano()}\\{nome}\\{tipo}\\SEFAZ BA.png"
    driver.save_screenshot(path_capture_screenshot)
    print("SCREENSHOT")


def close(driver: WebDriver):
    element = driver.close()
    return element


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


def waiter_by(wait: WebDriverWait, path: str, by = By.XPATH):
    wait.until(EC.presence_of_element_located((by, path)))
    for _ in range(5):
        wait.until(EC.invisibility_of_element_located((by, path)))
        time.sleep(1)


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
