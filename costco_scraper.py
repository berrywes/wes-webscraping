import requests
import html
from pprint import pprint
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class Product:
	price: str
	title: str

def main():
	while True:
		query = input("What would you like to search for?\n")
		encoded_query = html.escape(query)

		req = requests.get(f"https://www.costco.com/CatalogSearch?dept=All&keyword={query}", headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"})

		soup = BeautifulSoup(req.content, 'html.parser')

		results = extract_results(soup)

		pprint(results)
		print("\n\n")

def extract_results(soup):
	html_products = soup.findAll("div", {"class": "product"})
	print(len(html_products))

	products = []
	for html_product in html_products:
		price = html_product.find("div", {"class": "price"})
		if price == None:
			# print(html_product)
			continue

		title_span = html_product.find("span", {"class": "description"})
		title = title_span.find("a").text
		product = Product(title=title, price=price.text)
		products.append(product)
	return products

if __name__ == "__main__":
	main()