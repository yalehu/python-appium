#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Exception import Custom_exception


class Element:
    """
    封装Appium中关于元素对象的方法
    """

    def __init__(self, driver):
        self.driver = driver

    # 获取页面元素
    def get(self, message):
        way, timeout, value = message
        way_list = ['xpath', 'id', 'ids', 'name', 'classes_name']
        for i in way_list:
            if i == way and i == 'xpath':
                element = self.driver.find_element_by_xpath(value)
                return element
            elif i == way and i == 'id':
                element = self.driver.find_element_by_id(value)
                return element
            elif i == way and i == 'ids':
                elements = self.driver.find_elements_by_id(value)
                return elements
            elif i == way and i == 'name':
                element = self.driver.find_element_by_name(value)
                return element
            elif i == way and i == 'classes_name':
                elements = self.driver.find_elements_by_class_name(value)
                return elements
            else:
                raise Custom_exception.WrongLocation

    # 等待页面元素加载
    def wait_element(self, message):
        way, timeout, value = message
        timeout = int(timeout)
        way_list = ['xpath', 'id', 'name', 'classes_name']
        for i in way_list:
            if i == way and i == 'xpath':
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value)))
                return element
            elif i == way and i == 'id':
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value)))
                return element
            elif i == way and i == 'name':
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value)))
                return element
            elif i == way and i == 'classes_name':
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
                return element
            else:
                raise Custom_exception.WrongLocation

    # 关闭driver
    def over(self):
        element = self.driver.quit()
        return element

    # 截图
    def get_screen(self, path):
        self.driver.get_screenshot_as_file(path)

    # 获取屏幕大小
    def get_size(self):
        size = self.driver.get_window_size()
        return size

    # 向上移动
    def swipe_to_up(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    # 向下移动
    def swipe_to_down(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    # 向左移动
    def swipe_to_left(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    # 向右移动
    def swipe_to_right(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    # 物理键返回
    def back(self):
        self.driver.keyevent(4)

    # 切换至web_view
    def switch_h5(self):
        self.driver.switch_to.context("WEBVIEW")

    # 切换至app原生
    def switch_app(self):
        self.driver.witch_to.context("NATIVE_APP")