import urllib2
from lxml import etree

url =  "http://oceanofgames.com/project-remedium-free-download/"
response = urllib2.urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)

print tree.xpath(xpathselector)