import requests

# bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
#
# response = requests.get(bitcoin_api_url)
#
# response_json = response.json()
#
# print(response_json[0])
#
# print(response_json[0]['price_usd'])

ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/bXoak1YhmEV8atwvGb8oeg'

print(requests.post(ifttt_webhook_url))

