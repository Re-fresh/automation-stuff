import selenium
import inspect
from selenium import webdriver
from time import sleep
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=r"E:\webdriver\chromedriver.exe")

def get_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


def clear_cache(driver, timeout):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')

    # wait for the button to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(get_clear_browsing_button)

    # click the button to clear the cache
    get_clear_browsing_button(driver).click()

    # wait for the button to be gone before returning
    wait.until_not(get_clear_browsing_button)
    driver.close()
    time.sleep(2)

# sleep(5)

option1 = "/html/body/div[5]/div[1]/div/div[1]/div/form/div[1]/div[1]/span/input"
option2 = "/html/body/div[5]/div[1]/div/div[1]/div/form/div[1]/div[2]/span/input"
option3 = "/html/body/div[5]/div[1]/div/div[1]/div/form/div[1]/div[3]/span/input"
option4 = "/html/body/div[5]/div[1]/div/div[1]/div/form/div[1]/div[4]/span/input"
option5 = "/html/body/div[5]/div[1]/div/div[1]/div/form/div[1]/div[5]/span/input"
while(True):
    try:
        driver.get("https://www.quiz-maker.com/pollasdasasfaf")
        time.sleep(2)
        driver.find_element_by_xpath(option2).click()
        driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div[1]/div/form/div[2]/a[1]/input").click()
        clear_cache(driver, timeout=10)
        sleep(10)

    except:
        driver.refresh()
        time.sleep(5)

# searchBox = driver.find_element_by_xpath('''//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input''')
# searchBox.send_keys("asdasdasd")

#searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
#searchButton.click()


# op = selenium.webdriver.chrome.webdriver.WebDriver(executable_path=r"E:\webdriver\chromedriver.exe")
# op.create_options()

# print(inspect.getmembers(op))
# x = op.experimental_options()
# print(x)
