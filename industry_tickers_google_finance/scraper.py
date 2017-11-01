#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re


def strip_this(ticker_url):
	regex = r"\w+:(.*?)&\w+"
	match = re.findall(regex, ticker_url)
	if match:
		return match[0]
	else:
		print("did not find for: ", ticker_url)


def create_var_name(name):
	step_one = name.lower().replace("&", "and")
	final_name = re.sub(r"[^A-Za-z0-9]+", '_', step_one)
	return final_name


def create_final_variable(ind_name, ind_tickers):
	var_name = create_var_name(ind_name)
	comment = "\n\n# {}\n".format(ind_name)
	variable = "{} = ".format(var_name)
	industry_name = "'{}': '{}',".format("Industry Name", ind_name)
	parsed_name = "'{}': '{}',".format("Parsed Name", var_name)
	tickers = "'{}': {}".format("Tickers", ind_tickers)
	inside = "{" + industry_name + parsed_name + tickers + "}"
	final = comment + variable + inside
	return final, var_name


def scrape_it(get_url):
	ticker_links = list()

	try:
		r = requests.get(get_url)
		soup = BeautifulSoup(r.text, 'lxml')
		table = soup.find('table', attrs={'class': 'results'})
		company_links = table.find_all('a', attrs={'name': lambda x: x != 'link_Company'})

		for i in company_links:
			if not i.has_attr('name'):
				ticker_link = i['href']
				ticker_links.append(ticker_link)

	except:
		print("fuck up")
		return ticker_links

	return ticker_links


def get_tickers(url):
	ticker_links = scrape_it(url)
	tickers = [strip_this(link) for link in ticker_links]
	final_cleaned_tickers = list(filter(lambda a: a != None, tickers))
	return final_cleaned_tickers


def scrape_for_industry_tickers(industry_list):
	# Overwriting Existing File to be blank if First Time Loading DB
	# with open("all_industries_tickers.py", "w") as out_file:
	# 	out_file.write("#!/usr/bin/env python3\n\n")

	with open("new_industries_tickers.py", "a") as out_file:
		all_industries = list()
		for ind, ind_url in industry_list.items():
			ind_tickers = get_tickers(ind_url)
			final, var_name = create_final_variable(ind, ind_tickers)
			all_industries.append(var_name)
			out_file.write(final)
			print(final)

		# all_industries_var = "\n\nall_industries = {}".format(str(all_industries).replace("\'", ""))
		# out_file.write(all_industries_var)
		# print(all_industries_var)
