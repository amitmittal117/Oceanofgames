import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
book = Workbook()
sheet = book.active
index_count = 3
percentage = 0
number_pages = 1
for i in range(1,number_pages+1):
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
		uClient_link = uReq(link)
		page_html_link = uClient_link.read()
		uClient_link.close()
		page_soup_link = soup(page_html_link, "html.parser")
		containers_link = page_soup_link.findAll("ul")[2].findAll("li")
		mylist = []
		my_count = 0
		for p in containers_link:
			if(count == 0):
				mylist.append(containers_link[my_count].string.split(": ")[0])
				print("0 = "+containers_link[my_count].string.split(": ")[0])
			else:
				mylist.append(containers_link[my_count].string.split(": ")[1])
				print("1 = "+containers_link[my_count].string.split(": ")[0])
		sheet["C"+ str(index_count)] = mylist[0]
		sheet["D"+ str(index_count)] = mylist[1]
		sheet["E"+ str(index_count)] = mylist[2]
		sheet["F"+ str(index_count)] = mylist[3]
		sheet["G"+ str(index_count)] = mylist[4]
		sheet["H"+ str(index_count)] = mylist[5]
		index_count = index_count+1
		my_count = my_count + 1
		count=count+1
		book.save("oofgtes.xlsx")
	percentage_find = 100/(number_pages)
	percentage=percentage+percentage_find
	if percentage > (100-(2*percentage_find)):
		percentage = 100
	print str(i) + " of "+str(number_pages)+ " " + str(percentage) + "% completed"