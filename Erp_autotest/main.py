#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time, random
import unittest


class ErpTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://oauth.test.sixi.com/sso-login/index.html?appId=erp")
        time.sleep(2)
        phone = self.driver.find_element_by_xpath('//*[@id="appCenter"]/div/form/div[1]/div/div[1]/input')
        phone.send_keys("15827418090")
        password = self.driver.find_element_by_xpath('//*[@id="appCenter"]/div/form/div[2]/div/div/div[1]/div/input')
        password.send_keys("123456")
        time.sleep(2)
        log = self.driver.find_element_by_xpath('//*[@id="appCenter"]/div/form/div[3]/button')
        log.click()
        time.sleep(2)
        self.driver.get("http://erp.test.sixi.com")
        time.sleep(3)

    def test_erpOrder(self):
        add = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/span[1]/span')
        add.click()
        time.sleep(2)
        add2 = self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/button[1]')
        add2.click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/span/div[1]/input').send_keys("你们")
        time.sleep(3)
        search = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/span/button[1]')
        search.click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[6]/div/div/button').click()
        time.sleep(5)

        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/div[2]/input').send_keys("10")

        save = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[3]/div/button[1]')
        save.click()
        time.sleep(5)
        creat = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/button')
        creat.click()
        time.sleep(5)

        creat2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div[5]/button')
        creat2.click()
        time.sleep(5)
        a = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/button')
        a.click()
        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[1]/ul/li[3]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/ul/li[2]').click()
        time.sleep(4)


        y = random.choice('大概代付搞得给对方更多风格的')
        name = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/input')
        name.send_keys(y * 5)
        name2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div[2]/div/div/div[1]/div/input')
        name2.send_keys("测试")

        cho = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div[3]/div/div/div[1]/i[2]')
        cho.click()
        time.sleep(2)
        cho2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div[3]/div/div/div[2]/div/span/ul/li[1]')
        cho2.click()
        time.sleep(4)

        w = random.randint(1000000, 2000000)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div[4]/div/div/div[1]/div/input').send_keys(w)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div[5]/div/div/div[1]/div/i').click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div[5]/div/div/div[2]/ul[2]/li[2]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div[6]/div/div/div/div/input').send_keys('e:\pictest\k123.jpg')
        time.sleep(4)

        h = random.randint(0,20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]/div[2]/div/div[2]/input').send_keys(h)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div[2]/div[2]/div/div[2]/input').send_keys(h)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div[3]/div[2]/div/div[2]/input').send_keys("9999999")
        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/button[1]').click()
        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/ul/li/span[2]').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[2]/a[2]/i').click()
        time.sleep(5)

        self.driver.quit()

if __name__ == "__main__":
        unittest.main()