import time

from selenium import webdriver


def browser(Browser,URL):
    if Browser == "chrome":
        web = webdriver.Chrome()
        web.get(URL)
    elif Browser == "firefox":
        web = webdriver.Firefox()
        web.get(URL)
    elif Browser == "edge":
        web = webdriver.Edge()
        web.get(URL)



time.sleep(5460)