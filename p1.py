import bs4
import requests
import csv
content = requests.get("https://www.ebay.com/b/Camera-Drones/179697/bn_89951")
content = bs4.BeautifulSoup(content.text,'html.parser')
products =content.find_all('li', class_="s-item")
names=["TITLE"]
descriptions=["DESCRIPTION"]
prices=["PRICE"]
locations=["SHIPPING LOCATION"]
lcosts=["SHIPPING COSTS"]
statuss=["STATUS"]
for product in products:
	name=product.h3.text
	names.append(name)

	try:
		description=product.find('div',class_="s-item__summary").text
	except AttributeError as e:
		description=None
	descriptions.append(description)

	price=product.find('span',class_="s-item__price").text
	prices.append(price)

	try:
		location=product.find('span',class_="s-item__location s-item__itemLocation").text
	except AttributeError as e:
		location=None
	locations.append(location)

	try:
		lcost=product.find('span', class_="s-item__shipping s-item__logisticsCost").text
	except AttributeError as e:
		lcost=None
	lcosts.append(lcost)

	try:
		status=product.find('span',class_="s-item__hotness s-item__itemHotness").text
	except AttributeError as e:
		status=None
	statuss.append(status)

with open('f1.csv','w',newline='') as f:
	rows = zip(names,descriptions,prices,locations,lcosts,statuss)
	w=csv.writer(f)
	w.writerows(rows)
