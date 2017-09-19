#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月24日

@author: li tao
"""
import xml.etree.ElementTree


class BastPage:
    """
    封装读取page.xml
    """

    def __init__(self, filename):
        self.level = 1  # 节点的深度从1开始
        self.root = xml.etree.ElementTree.parse(filename).getroot()
        self.result_list = []

# 遍历所有的节点
    def walk_data(self, root_node, level, page_name, locator):
        if root_node.text.encode('utf-8') == locator:
            self.result_list = root_node.attrib
            return
        else:
            try:
                if root_node.tag == 'map' or root_node.attrib['pageName'] == page_name:
                    children_node = root_node.getchildren()
                    if len(children_node) == 0:
                        pass
                    for child in children_node:
                        self.walk_data(child, level + 1,  page_name, locator)
                    return self.result_list
            except:
                pass

    def run(self, page_name, locator):
        result = self.walk_data(self.root, self.level, page_name, locator)
        return result