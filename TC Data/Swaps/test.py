from etherscan import Etherscan
import json
import csv
import time

i=0
eth = Etherscan("11BMSKIP2BIIKHVHDMM9GQ8NWVIXPY52E2") # key in quotation marks

transaction=eth.get_normal_txs_by_address(
    address="0xcd54ff0e52a61b6dab8c24d1348116ca3bb522a9",
    startblock="0",
    endblock="99999999",
    sort="asc"
)

print(transaction)
#pd.to_datetime(df['time'], unit='s')
