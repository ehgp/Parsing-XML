# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:19:14 2019

@author: erick
"""
import xml.etree.ElementTree as ET
import zipfile
import lxml.html
from lxml.etree import tostring
from bs4 import BeautifulSoup
import re
with zipfile.ZipFile("C:\\Users\\erick\\Downloads\\xml_containing_html.xml.zip","r") as zip_ref:
    zip_ref.extractall("C:\\Users\\erick\\Downloads\\xml_containing_html")
element_tree = lxml.html.parse("C:\\Users\\erick\\Downloads\\xml_containing_html\\xml_containing_html.xml")
tree_title_element = element_tree.xpath(rb'//content')
for i in range(0,len(tree_title_element)):
    soup = BeautifulSoup(tostring(tree_title_element[i]), 'html.parser')
    soup1 = soup.encode(formatter=None)
    soup2 = soup1.count(rb"a href")
    print("Number of Links for HTML Content #%1d Equals: %1d" % (i,soup2))