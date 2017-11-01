#!/usr/bin/env python3

# =====================================================
#   My Tickers
# =====================================================

network_tickers = ['FB', 'YELP', 'TWTR', 'GRPN', 'EBAY', 'V', 'MA', 'PYPL', 'ETSY', 'WB']

otherTickers = ['ACGL', 'GALT', 'WMT', 'SPR', 'PXLW', 'PGRE', 'C', 'RIGL', 'CCI', 'QSII', 'MDLZ', 'GIS', 'BAC',
                'CSCO', 'SYUT', 'BKS', 'BRKL', 'GPS', 'ANF', 'M', 'KR', 'DPS', 'PEP', 'BID', 'AEO', 'BEBE', 'RL',
                'PVH', 'VFC', 'SWK', 'SNA', 'GE', 'MCD', 'TSLA', 'KO', 'PG', 'JNJ', 'MRK', 'JPM', 'MMM', 'UTX',
                'HON', 'XOM', 'PM', 'RAI', 'CVX', 'BP', 'GM', 'COST', 'NKE', 'DIS', 'INTC', 'HD', 'LOW', 'DRYS']

# =====================================================
#   Network Industries
# =====================================================

# Internet Services - NEC
internet_services_nec = {'Industry Name': 'Internet Services - NEC','Parsed Name': 'internet_services_nec','Tickers': ['LEXEA', 'YY', 'NFLX', 'ATHM', 'WB', 'WBMD', 'EGOV', 'YRD', 'SSTK', 'ATHN', 'LTRPA', 'LIVE', 'TCX', 'AWAY', 'LGZ', 'LFGR', 'BCOR', 'CRCM', 'YELP', 'ANGI', 'CNXR', 'MARK', 'NAME', 'IAC', 'TRUE', 'BITA', 'TRVG', 'JMU', 'WUBA', 'YOKU', 'QUNR', 'TUDO', 'LEXEB', 'LTRPB']}

# E-commerce & Auction Services
e_commerce_and_auction_services = {'Industry Name': 'E-commerce & Auction Services','Parsed Name': 'e_commerce_and_auction_services','Tickers': ['BABA', 'EBAY', 'MELI', 'BID', 'JMEI', 'DANG', 'OSTK', 'TKAT', 'PCOM', 'BRDR', 'LOOK', 'GKNT', 'OMNT', 'CAZAU', 'PRSS', 'TTD', 'ETSY', 'SHOP', 'CNV', 'JD', 'GMC', 'TMG']}

# Social Media & Networking
social_media_and_networking = {'Industry Name': 'Social Media & Networking','Parsed Name': 'social_media_and_networking','Tickers': ['SINA', 'JIVE', 'MEET', 'RENN', 'FB', 'TWTR', 'IZEA', 'LN', 'MTCH', 'DATE', 'LNKD']}

# Internet Security & Transactions Services
internet_security_and_transactions_services = {'Industry Name': 'Internet Security & Transactions Services','Parsed Name': 'internet_security_and_transactions_services','Tickers': ['MIME', 'V', 'MA', 'PYPL', 'KEYW']}


# =====================================================
#   Non-Network Industries
# =====================================================

# Pharmaceuticals - NEC
pharmaceuticals_nec = {'Industry Name': 'Pharmaceuticals - NEC','Parsed Name': 'pharmaceuticals_nec','Tickers': ['NEOS', 'CUR', 'GALE', 'TTPH', 'HSGX', 'IPXL', 'ACET', 'SCYX', 'TBPH', 'LCI', 'AZRX', 'TARO', 'VRX', 'CORI', 'APRI', 'AQXP', 'SPHS', 'SCLN', 'AZN', 'FOLD', 'AMPH', 'EVOK', 'NAII', 'INVA', 'TEVA', 'NVS', 'HZNP', 'CORT', 'AKRX', 'TLGT', 'RDY', 'LLY', 'GSK', 'CBM', 'BDSI', 'TYHT', 'JNP', 'SHPG', 'ABT', 'JNJ', 'MRK', 'SNY', 'BLFS', 'PFE', 'CXRX', 'CTLT', 'AMAG', 'NVO', 'BMY', 'MRNS', 'PTX', 'CLRB', 'IBIO', 'PCRX', 'UG', 'OPK', 'ARLZ', 'NEOT', 'IMNP', 'COLL', 'ADMP', 'INNL', 'MBRX']}

# Auto & Truck Manufacturers - NEC
auto_and_truck_manufacturers_nec = {'Industry Name': 'Auto & Truck Manufacturers - NEC', 'Parsed Name': 'auto_and_truck_manufacturers_nec', 'Tickers': ['GM', 'ADNT', 'REVG', 'F', 'TSLA', 'WKHS', 'TM', 'HMC', 'TTM', 'GM-B', 'KNDI']}


# =====================================================
#   Variables that holds Industries for ease
# =====================================================

all_industries = [internet_services_nec, e_commerce_and_auction_services, social_media_and_networking, internet_security_and_transactions_services, pharmaceuticals_nec, auto_and_truck_manufacturers_nec]

non_network_industries = [pharmaceuticals_nec, auto_and_truck_manufacturers_nec]
