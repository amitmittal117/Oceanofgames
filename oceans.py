import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
book = Workbook()
sheet = book.active


info_list = []
def info (str1):
	my_link = str1
	uClient = uReq(my_link)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	containers_link = page_soup.findAll("ul")[2].findAll("li")
	counter = 0
	for i in containers_link:
		info_list.append(containers_link[counter].text)
		counter+=1
	
my_url = 'http://oceanofgames.com/page/2'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers_outer_div = page_soup.findAll("h2",{"class":"title"})
counter = 0
link_inner = []
name = []
for i in containers_outer_div:
	link_inner.append(containers_outer_div[counter].a['href'])
	name.append(containers_outer_div[counter].a.string)
	info_list.append(containers_outer_div[counter].a.string)
	info_list.append(containers_outer_div[counter].a['href'])
	info (link_inner[counter])
	counter+= 1

final_list = ([info_list[i:i+8] for i in range(0, len(info_list), 8)])
for i in final_list:
	sheet.append(i)
	book.save("ocean.xlsx")
		# print(len(i))
