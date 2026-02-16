
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def browser(browser_name, url):
    try:
        if browser_name.lower() == "chrome":
            driver = webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            driver = webdriver.Firefox()
        elif browser_name.lower() == "edge":
            driver = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.get(url)
        input("Press Enter to close the browser...")
    except WebDriverException as e:
        print(f"WebDriver error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass