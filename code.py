import os
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

EXECUT = os.getcwd()+"/geckodriver"
options = Options()
options.headless = True

def hit():
	try:
		#print("1")
		browser = webdriver.Firefox(options=options,executable_path=EXECUT)
	except Exception:
		print("Failed")
		subprocess.run(["./kill-gecko.sh"])
		subprocess.run(["python3","code.py"])
	
	try:
		#print("2")
		browser.get("http://hdjshrn.tk/")
		print(browser.page_source)
		body = browser.find_elements_by_tag_name("body")
		print(body)
		body[0].click()
		
		
		browser.switch_to.window(browser.window_handles[1])
		ad = browser.find_elements_by_tag_name("iframe")
		print(ad)
		ad[0].click()
		
		for tab in browser.window_handles:
			browser.switch_to.window(tab)
			browser.close()
	except Exception:
		subprocess.run(["./end.sh"])

while True:
	hit()
