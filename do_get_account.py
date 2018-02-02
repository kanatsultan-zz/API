import json
import requests

api_token = 'your_api_token'
api_url_base = 'https://api.digitalocean.com/v2/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}


# Defining a function here:
def get_account_info():

    api_url = '{0}account'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

# Calling the above function and assign it to account_info variable.
account_info = get_account_info()

if account_info is not None:
    print("Here's your info: ")
    for k, v in account_info['accounts'].items():
        print ('{0}:{1}'.format(k, v))

else:
    print ('[!] Request Failed')