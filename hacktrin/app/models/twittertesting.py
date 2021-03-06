client_key = 'XDjlZjOCRTeVzCShEeZwmeeMG'
client_secret = 'uZtuVMOHbv7oJcS054UHe1svMxZQ0MxWOGI1oOw3NccU3jzoi7'

import base64

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

import requests

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

# Check status code okay
auth_resp.status_code

# Keys in data response are token_type (bearer) and access_token (your access token)
auth_resp.json().keys()

access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params = {
    'q': 'girlpower',
    'result_type': 'recent',
    'count': 5
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

search_resp.status_code

tweet_data = search_resp.json()

for x in tweet_data['statuses']:
    print(x['text'] + '\n')
