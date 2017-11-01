#!/usr/bin/env python3

from psql_exporter import export_zacks_eps
from zacks_web_scraper.scraper import scraperUniversal


def scrape_this_url(ticker, url_extension, table_id, tab_id_in_table, num_pages2crawl):
	print("{0:6}{1:6}{2}".format("  ~~> ", ticker, ": "), end="", flush=True)
	final_url = "https://www.zacks.com/stock/chart/" + ticker + url_extension
	eps_data, company_name = scraperUniversal(final_url, table_id, tab_id_in_table, num_pages2crawl)
	print("Done.")
	return (company_name, ticker, final_url, eps_data)


def get_eps_12months(tickers):
	eps_url = "/eps"
	table_id = "DataTables_Table_3"
	tab_id_in_table = "ui-id-6"
	num_pages2crawl = 4
	export_table_title = "12 Month EPS"
	print("{0}{1}{2}".format("Scraping ", export_table_title, " data for:"))
	eps_data_collection = [scrape_this_url(ticker, eps_url, table_id, tab_id_in_table, num_pages2crawl) for ticker in tickers]
	if eps_data_collection:
		export_zacks_eps(eps_data_collection)
