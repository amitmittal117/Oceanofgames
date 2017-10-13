import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
book = Workbook()
sheet = book.active
index_count = 3
percentage = 0
number_pages = 3
for i in range(3,number_pages+1):
	my_url = 'http://oceanofgames.com/page/'+str(i)
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	count = 0
	page_soup = soup(page_html, "html.parser")
	containers_outer_div = page_soup.findAll("h2",{"class":"title"})
	for j in containers_outer_div:
		sheet["A"+ str(index_count)] = containers_outer_div[count].a.string
		sheet["B"+ str(index_count)] = containers_outer_div[count].a['href']

		link = containers_outer_div[count].a['href']
		print link
		uClient_link = uReq(link)
		page_html_link = uClient_link.read()
		uClient_link.close()
		page_soup_link = soup(page_html_link, "html.parser")
		containers_link = page_soup_link.findAll("ul")[2].findAll("li")
		count =0
		mycount=1
		mylist = []
		for p in containers_link:
			if(count == 0):
				mylist.append(containers_link[count].string.split(": ")[0])
			else:
				mylist.append(containers_link[count].string.split(": ")[1])
			count=count+1
		sheet["C"+ str(index_count)] = mylist[0]
		sheet["D"+ str(index_count)] = mylist[1]
		sheet["E"+ str(index_count)] = mylist[2]
		sheet["F"+ str(index_count)] = mylist[3]
		sheet["G"+ str(index_count)] = mylist[4]
		sheet["H"+ str(index_count)] = mylist[5]
		index_count = index_count + 1
		book.save("oofg123.xlsx")
		print (mylist[0])
		print (mylist[1])
		print (mylist[2])
		print (mylist[3])
		print (mylist[4])
		print (mylist[5])