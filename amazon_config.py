from selenium import webdriver

DIRECTORY = 'reports'
NAME = 'PS4'
CURRENCY = '$'
MIN_PRICE = '275'
MAX_PRICE = '650'
FILTSERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = 'https://www.amazon.us'

def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver', chrome_options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def    