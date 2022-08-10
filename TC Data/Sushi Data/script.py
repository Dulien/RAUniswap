import requests
import json
import csv
import time
import pandas as pd


def run_query(query):  # A simple function to use requests.post to make the API call.
    headers = {'X-API-KEY': API_KEY}
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                        query))


i=0
API_KEYS = ["BQYN8KmMj3B85iEqSkogmRGudfHualuK",
            "BQYJalF13QYIOaFWIeriDL2xVnY04CoW",
            "BQYdEOjWZGGA4SQ6KbJz6Ynbx3aJeNlz",
            "BQYLGB9TxYGVoYrdU47EMpGTfZbzzVVt",
            "BQYEISdSukuz43Zq68uUBroSnui6Erfo",
            "BQYmzWRaV3cfbjVgrSp76k2HNnCy6qQ8",
            "BQYV3HxWdKBiY9Z7uzuQzkU7zkeCJLJZ",
            "BQYhb80Vx4i8ZCPWcHmFanuHzljVSVMX",
            "BQYlvgaEjy6ai6HZVawJrFMxOHax7BeZ",
            "BQYOkeIEGgkWt0u8UMwzxkdNIzgtXlJF",
            "BQYxUirM6OwEGvpRPjk4Ox0pQbsEcBxV",
            "BQYemLlIwxkUSyTzL5IThoFajzn6xJp7",
            "BQYec3BU4fnZ4fjIqrhb6OVyTxqN5koR",
           "BQYl61hRj3UI9vDqGEw0nGrsqpWR99yM",
           "BQYuS9PuzC1rvS1qzsN6s92zwLWaUbwm",
           "BQYCInDdczBkSaF4tmY1CfGRzjRgCx9n",
           "BQY2YKDekdMOghBauFdXDnE5zkbJ8TlM",
           "BQYmfFjcsrmvvgnKnlT4r1O8YnxZ5TA1"]
API_KEY = API_KEYS.pop()
data = []

with open('26K.csv', 'r') as file:
    reader = csv.reader(file)
    for address in reader:
        
        #if (i%500)==0:
            #print("Saving...")
            #df = pd.DataFrame(data)
            #df.to_csv("out.csv", encoding='utf-8', index=False)
            #time.sleep(5)
            
        query = """
        {{
          ethereum {{
            address(address: {{is: "{user}"}}) {{
              balances(currency: {{is: "0x6b3595068778dd592e39a122f4f5a5cf09c90fe2"}}, date: {{since: "2020-09-17" till: "2020-11-30"}}) {{
                history {{
                  value
                  timestamp
                }}
              }}
            }}
          }}
        }}""".format(user=address[0])
    
        try:
            result = run_query(query)  # Execute the query
        except:
            print("Crashed...")
            df = pd.DataFrame(data)
            df.to_csv("out2.csv", encoding='utf-8', index=False) #replace with list
            time.sleep(10)
            API_KEY = API_KEYS.pop()
            result = run_query(query)
        try:
            result = result['data']['ethereum']['address'][0]['balances'][0]['history']
            df = pd.DataFrame(result)
            df["address"] = address[0]
            max_index = df["value"].idxmax()
            row = df.iloc[max_index]
            data.append(row)
        except:
            print("File skipped")
        
        time.sleep(0.3)
        #i=i+1
        
df = pd.DataFrame(data)
df.to_csv("out2.csv", encoding='utf-8', index=False)
