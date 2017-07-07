#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = 'redhootcp'
password = 'test'

def login():
    driver = webdriver.Firefox()
    driver.get('https://www.instagram.com/accounts/login/?force_classic_login')
    assert "Instagram" in driver.title
    elem = driver.find_element_by_name("username")
    elem.clear()
    elem.send_keys(username)
    elem = driver.find_element_by_name("password")
    elem.clear()
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    driver.close()

with open('wordlist.txt', 'r') as f:
    line = f.readlines()
    print line
