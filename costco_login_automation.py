from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
	driver = webdriver.Chrome()
	driver.get("http://www.costco.com")

	try:
		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "header_sign_in"))
		)

		element.click()

		login_button_element = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.ID, "logonId"))
		)

		input()

	finally:
		driver.quit()


if __name__ == "__main__":
	main()