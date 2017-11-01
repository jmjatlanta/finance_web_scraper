#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from psql_exporter import export_earnings, export_eps, export_industry_earnings, export_net_income


def strip_this(unstripped_row):
	all_cells = unstripped_row.find_all('td')
	return [cell.string.strip() for cell in all_cells]


def find_eps(rows):
	for row in rows:
		if strip_this(row)[0] =="EPS Basic Total Ops":
			return strip_this(row)


def find_net_income(rows):
	for row in rows:
		if strip_this(row)[0] =="Net Income":
			return strip_this(row)


def format_dates(dates):
	return list(map(lambda x: x.replace("-", "-01-"), dates))


def format_revenues(revenues):
	return list(map(lambda x: int(x.replace(",", "")), revenues))


def format_eps(eps):
	return list(map(lambda x: float(x) if x != "N/A" else None, eps))


def format_net_income(net_income):
	donzo = list(map(lambda x: x.replace(",", ""), net_income))
	return list(map(lambda x: int(x.replace("$", "")), donzo))


def scrape_it(ticker):
	num_pages = 10
	url = 'https://www.barchart.com/stocks/quotes/' + ticker + '/income-statement/quarterly?reportPage='
	ticker_results = dict()

	for i in range(num_pages):
		try:
			get_url = url + str(i+1)
			r = requests.get(get_url)
			soup = BeautifulSoup(r.text, 'lxml')
			table = soup.find('table')

			dates = strip_this(table.find_all('tr')[0])
			revenues = strip_this(table.find_all('tr')[1])

			dates.pop(0)
			revenues.pop(0)

			final = dict(zip(format_dates(dates), format_revenues(revenues)))

			ticker_results.update(final)

		except:
			print("Page ", i, "doesn't exist.")
			return ticker_results

	return ticker_results


def scrape_it_new(ticker):
	num_pages = 10
	url = 'https://www.barchart.com/stocks/quotes/' + ticker + '/income-statement/quarterly?reportPage='
	ticker_revenues_results = dict()
	ticker_eps_results = dict()

	for i in range(num_pages):
		try:
			get_url = url + str(i+1)
			r = requests.get(get_url)
			soup = BeautifulSoup(r.text, 'lxml')
			table = soup.find('table')

			dates = strip_this(table.find_all('tr')[0])
			revenues = strip_this(table.find_all('tr')[1])
			eps = find_eps(table.find_all('tr'))

			dates.pop(0)
			revenues.pop(0)
			eps.pop(0)


			final_revenues = dict(zip(format_dates(dates), format_revenues(revenues)))
			final_eps = dict(zip(format_dates(dates), format_eps(eps)))

			ticker_revenues_results.update(final_revenues)
			ticker_eps_results.update(final_eps)

		except:
			print("Page ", i, "doesn't exist.")
			return dict({'revenues': ticker_revenues_results, 'eps': ticker_eps_results})

	return dict({'revenues': ticker_revenues_results, 'eps': ticker_eps_results})


def scrape_net_income(ticker):
	num_pages = 10
	url = 'https://www.barchart.com/stocks/quotes/' + ticker + '/income-statement/quarterly?reportPage='
	ticker_net_income_results = dict()

	for i in range(num_pages):
		try:
			get_url = url + str(i+1)
			r = requests.get(get_url)
			soup = BeautifulSoup(r.text, 'lxml')
			table = soup.find('table')

			dates = strip_this(table.find_all('tr')[0])
			net_income = find_net_income(table.find_all('tr'))

			dates.pop(0)
			net_income.pop(0)
			format_net_income(net_income)
			final_net_income = dict(zip(format_dates(dates), format_net_income(net_income)))

			ticker_net_income_results.update(final_net_income)

		except:
			print("Page ", i, "doesn't exist.")
			return ticker_net_income_results

	return ticker_net_income_results


def scrape_earnings(tickers, for_industry=False, ind_name=False):
	for ticker in tickers:
		net_income_vals = scrape_net_income(ticker)
		export_net_income(ticker, net_income_vals)

		# vals = scrape_it(ticker)
		# vals = scrape_it_new(ticker)
		#
		# if for_industry:
		# 	export_industry_earnings(ticker, ind_name, vals['revenues'])
		# 	export_eps(ticker, vals['eps'])
		# else:
		# 	export_earnings(ticker, vals['revenues'])





