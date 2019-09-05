#!/usr/bin/python3
# coding=utf-8
# Filename: login.py
import time
def login_test(self, driver, code, name, pwd ):
    self.driver =driver
    driver.get('https://tkzhushou.mylianzhi.com/eldf-sso/login.htm')
    company_code =driver.find_element_by_id('j_companyCode')
    company_code.clear()
    company_code.send_keys(code)
    username = self.driver.find_element_by_id('j_username')
    username.clear()
    username.send_keys(name)
    password = self.driver.find_element_by_id('j_password')
    password.clear()
    password.send_keys(pwd)
    self.driver.find_element_by_xpath('//button[text()="登录"]').click()
    time.sleep(2)
    try:
        actual = self.driver.find_element_by_xpath('//*[@id="show-shortcut"]/span')
    except:
        print("无法找到元素，可能原因：登录失败，页面未跳转")
    finally:
        self.assertEqual(actual.text, name.capitalize())

