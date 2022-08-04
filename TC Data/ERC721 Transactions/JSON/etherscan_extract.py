from etherscan import Etherscan
import json
import csv
import time

i=0
eth = Etherscan("11BMSKIP2BIIKHVHDMM9GQ8NWVIXPY52E2") # key in quotation marks

with open('26K.csv', 'r') as file:
    reader = csv.reader(file)
    for data in reader:
        try:
            transaction=eth.get_erc721_token_transfer_events_by_address(
                address=data[0],
                startblock="0",
                endblock="99999999",
                sort="asc"
            )
            with open('data_'+data[0]+'.json', 'w') as json_file:
                json.dump(transaction, json_file)
        except:
            print("skipped..."+data[0])