import requests
import pandas as pd
import json
import csv
import time



def run_query(query):  # A simple function to use requests.post to make the API call.
    headers = {'X-API-KEY': API_KEY}
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                        query))

import csv
import time 
import pandas as pd

df = pd.DataFrame(columns=['address', 'date'])
API_KEYS = [
    'BQYGQkwOt65MI0dMORpVr2aVB7gNXunP',
    'BQYeEaGaXx9notnyokDerdvotnC72zbF',
    'BQY8TTA89uZp8erZc6nxBfmrnscjY36h'
    ]
API_KEY = API_KEYS.pop()
i = 0

with open('file0.csv', 'r') as file: 
    reader = csv.reader(file) 
    for address in reader:

        print(str(i)+"/"+"4000"+" --- "+str((i/4000)*100)+"%")
        if (i%1000)==0:
            print("Saving...")
            df.to_csv("out.csv", encoding='utf-8', index=False)
            time.sleep(5)

        query = """
        {{
          ethereum(network: ethereum) {{
            dexTrades(
              exchangeName: {{is: "Uniswap"}}
              txSender: {{is: "{user}"}}
              options: {{limit: 1}}

            ) {{
              transaction {{
                txFrom {{
                  address
                }}
              }}
              date {{
                date(format: "%y-%m-%d")
              }}
            }}
          }}
        }}""".format(user=address[1])
        try:
            result = run_query(query)  # Execute the query
        except:
            print("Crashed...")
            df.to_csv("out.csv", encoding='utf-8', index=False)
            time.sleep(60)
            API_KEY = API_KEYS.pop()
            result = run_query(query)
        try:
            address = result['data']['ethereum']['dexTrades'][0]['transaction']['txFrom']["address"]
            date = result['data']['ethereum']['dexTrades'][0]['date']['date']
            print("data - "+address+" "+date)
            df.loc[i] = [address] + [date]
        except:
            print("File skipped")

        i+=1
        time.sleep(0.1)
    
    df.to_csv("out.csv", encoding='utf-8', index=False)
