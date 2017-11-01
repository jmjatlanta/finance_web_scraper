#!/usr/bin/env python3
from psql_connector import *
import re


def export_industry_earnings(ticker, ind_name, vals):
	for date, earnings in vals.items():
		sql_statement = "INSERT INTO industry_earnings VALUES('{}', '{}', '{}', {});".format(ind_name, ticker, date, earnings)
		print(sql_statement)
		post_db(sql_statement)


def export_earnings(ticker, vals):
	for date, earnings in vals.items():
		sql_statement = "INSERT INTO earnings VALUES('{}', '{}', {});".format(ticker, date, earnings)
		print(sql_statement)
		post_db(sql_statement)


def export_eps(ticker, vals):
	for date, eps in vals.items():
		sql_statement = "INSERT INTO eps VALUES('{}', '{}', {});".format(ticker, date, eps)
		print(sql_statement)
		post_db(sql_statement)


def export_net_income(ticker, vals):
	for date, ni in vals.items():
		sql_statement = "INSERT INTO net_income VALUES('{}', '{}', {});".format(ticker, date, ni)
		print(sql_statement)
		post_db(sql_statement)


def add_is_network(tickers, ne):
	for ticker in tickers:
		sql_statement = "INSERT INTO is_network VALUES('{}', {});".format(ticker, ne)
		print(sql_statement)
		post_db(sql_statement)


def export_zacks_eps(data_collection):
	for each_company in data_collection:
		company_name, ticker, final_url, data = each_company
		for date, value in data:
			new_val = "NULL" if value == "N/A" else value
			new_date = re.sub(r'/.*/', "/01/", date)
			sql_statement = "INSERT INTO eps VALUES('{}', '{}', {});".format(ticker, new_date, new_val)
			print(sql_statement)
			post_db(sql_statement)


def industry_categorizer(tickers, industry):
	for ticker in tickers:
		sql_statement = "INSERT INTO ticker_industry VALUES('{}', '{}');".format(ticker, industry)
		print(sql_statement)
		post_db(sql_statement)
