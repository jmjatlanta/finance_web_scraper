#!/usr/bin/env python3
from psql_exporter import add_is_network, industry_categorizer
from barchart_web_scraper import scrape_earnings
from zacks_web_scraper import get_eps_12months
from industry_tickers_google_finance import scraper
from all_tickers import *


def main():
	industry_list = \
		{
			'Internet Services - NEC'                  : 'https://www.google.com/finance?catid=us-TRBC%3A5720103010&sort=ANIAC&ei=t7XUWIHJO4vejAGfrLT4BA&start=0&num=100',
			'E-commerce & Auction Services'            : 'https://www.google.com/finance?catid=us-TRBC%3A5720103013&sort=ANIAC&ei=L7vUWKmBF4vejAGfrLT4BA&start=0&num=100',
			'Social Media & Networking'                : 'https://www.google.com/finance?catid=us-TRBC%3A5720103012&ei=_LTUWImeA8T2jAG6m7XADQ',
			'Internet Security & Transactions Services': 'https://www.google.com/finance?catid=us-TRBC%3A5720103015&ei=YrvUWLn4M4Sf2Ab59ZmgCw',
			'Pharmaceuticals - NEC'                    : 'https://www.google.com/finance?catid=us-TRBC%3A5620104010&ei=senUWKnFKorNjAHb-I-YBA&num=100'
		}

	auto_industry_list = \
		{
			'Auto & Truck Manufacturers - NEC': 'https://www.google.com/finance?catid=us-TRBC%3A5310101010&ei=hx7XWMrSMIvejAGfrLT4BA',
			'Electrical (Alternative) Vehicles': 'https://www.google.com/finance?catid=us-TRBC%3A5310101014&ei=CCDXWPnGBcfDjAGq1p_YCw'
		}

	# # Scraping all Tickers of each Industry
	# scraper.scrape_for_industry_tickers(industry_list)
	# scraper.scrape_for_industry_tickers(auto_industry_list) #Combine the 2 auto Industries

	# # Scraping Earnings For Industry Total Earnings (Revenues and EPS)
	# for industry in all_industries:
	# 	scrape_earnings(industry['Tickers'], for_industry=True, ind_name=industry['Industry Name'])

	# scrape_earnings(network_tickers)
	for i in non_network_industries:
		scrape_earnings(i['Tickers'])

	# Adding if Company has NE or not
	# add_is_network(network_tickers, 1)
	# for i in non_network_industries:
	# 	add_is_network(i['Tickers'], 0)

	# # Mapping Companies to their Industries
	# internet_services = ['YELP','GRPN','WB',]
	# e_commerce_services = ['EBAY','ETSY']
	# social_media = ['FB','TWTR']
	# transactions_services = ['V','PYPL','MA']

	# # Networks
	# industry_categorizer(internet_services, 'Internet Services - NEC')
	# industry_categorizer(e_commerce_services, 'E-commerce & Auction Services')
	# industry_categorizer(social_media, 'Social Media & Networking')
	# industry_categorizer(transactions_services, 'Internet Security & Transactions Services')

	# # Non-Networks
	# for i in non_network_industries:
	# 	industry_categorizer(i['Tickers'], i['Industry Name'])

	# # OLD - ZACKS SCRAPER
	# get_eps_12months(network_tickers)
	# get_eps_12months(pharma_tickers)

if __name__ == "__main__":
	main()
