# ===============================================================================
# File Name     : crawler.py
# Purpose       : fetch the content of web page
# Creation Date : 07-05-2016
# Last Modified : 07-05-2016
# Created By    : Yuanying Chen
# ===============================================================================

# coding = utf-8
import urllib
import re


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, 'pic//%s.jpg' % x)
        x += 1


html = getHtml("http://d3.blizzard.cn/home")

print getImg(html)
