from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://www.netscribes.com/"
driver.get(url)
driver.implicitly_wait(3)
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Get started']").click()