import requests
import pandas
import json
import csv
import time

def run_query(query):  # A simple function to use requests.post to make the API call.
    headers = {'X-API-KEY': 'BQYdfA9yMkZqesqsq8N1RUwHXQMdrqiD'}
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                        query))



with open('PRE-Addresses.csv', 'r') as file:
    reader = csv.reader(file)
    for address in reader:
        query = """
        {{
          ethereum {{
            address(address: {{is: "{user}"}}) {{
              balances (
                currency: {{is: "ETH"}}
                date: {{till: "2022-05-01"}}
              ) {{
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
            print("Crashed")
            time.sleep(1)

        try:
            result = result['data']['ethereum']['address'][0]['balances'][0]['history']
            with open('data_'+address[0]+'.json', 'w') as json_file:
                json.dump(result, json_file)
        except:
            print("File skipped")
        
        time.sleep(0.15)
        
        #df = pandas.read_json('data_'+address[1]+'.json')