# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:03:45 2019

@author: erick
"""
import re
import zipfile
import lxml.html
from lxml.etree import tostring

with zipfile.ZipFile("C:\\Users\\erick\\Downloads\\xml_containing_html.xml.zip","r") as zip_ref:
    zip_ref.extractall("C:\\Users\\erick\\Downloads\\xml_containing_html")
element_tree = lxml.html.parse("C:\\Users\\erick\\Downloads\\xml_containing_html\\xml_containing_html.xml")
tree_title_element = element_tree.xpath(rb'//content')
pattern = r'HTML(.+?)/HTML'
pattern1 = r'a href=(.+?)/a'
for i in range(0,len(tree_title_element)):
    hi1 = re.findall(pattern,str(tostring(tree_title_element[i])))
    hi2 = len(re.findall(pattern1,str(hi1[0])))
    print("Number of Links for HTML Content #%1d Equals: %1d" % (i,hi2))