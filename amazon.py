from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.amazon.com")
time.sleep(2)

browser.maximize_window()
time.sleep(1)

assert "Discover Amazon" in browser.page_source

time.sleep(2)

# element_to_hover_over = browser.find_element_by_css_selector('#nav-link-accountList')
# hover = ActionChains(browser).move_to_element(element_to_hover_over)
# hover.perform()


browser.find_element_by_id("nav-link-accountList").click()

time.sleep(2)
#
# sign_in_button = browser.find_element_by_xpath(
#     "//div[@id= 'nav-flyout-ya-signin']/a[@class= 'nav-action-button']/span[@class = 'nav-action-inner']").click()

time.sleep(2)

browser.find_element_by_id("ap_email").send_keys("gulsan.celep@useinsider.com")

time.sleep(2)
browser.find_element_by_id("continue").click()

time.sleep(5)
browser.find_element_by_id("ap_password").send_keys("wsxzaq1")

time.sleep(5)
browser.find_element_by_id("signInSubmit").click()

time.sleep(30)

search = browser.find_element_by_id("twotabsearchtextbox")
search.send_keys("samsung")
search.send_keys(Keys.RETURN)

assert "samsung" in browser.page_source

browser.find_element_by_xpath(
    "//*[@id='search']/div[1]/div[2]/div/span[8]/div/span/div/div/ul/li[3]/a").click()

assert '17-32 of over' in browser.page_source

time.sleep(5)

browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[1]/div[2]/div/span[4]/div[1]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a").click()

time.sleep(2)
add_to_list = browser.find_element_by_id("add-to-wishlist-button")
ActionChains(browser).move_to_element(add_to_list).perform()
add_to_list.click()

time.sleep(5)

browser.find_element_by_xpath("//ul[@id = 'atwl-dd-ul']/li[3]").click()

time.sleep(5)

assert "Customers who bought also bought" in browser.page_source

browser.find_element_by_id("WLHUC_viewlist").click()

browser.find_element_by_xpath("//*[@id='a-autoid-7']/span/input").click()

time.sleep(5)

# a = browser.find_element_by_xpath("//div[text()='Deleted']")

assert "Deleted" in browser.page_source

browser.quit()
