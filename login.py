import sys
from selenium import webdriver
import time

driver = webdriver.Firefox()
print "Driver launched"


driver.get("http://seleniumhq.org/")

try:
	username = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/form/input[1]")
	username.clear()
	username.send_keys('*****') # Replace ***** with your username
	password = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/form/input[2]")
	password.clear()
	password.send_keys('*****') # Replace ***** with your password
	driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/form/input[3]").click()
	driver.close()
	print "Logged In."


except:
	driver.close()
	print "Already Logged In"
