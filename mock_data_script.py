from graphqlclient import GraphQLClient
gqlClient = GraphQLClient('https://crypto-bots-back.herokuapp.com/graphql')
import random
import json
import csv
from six.moves import urllib
import requests

from binance.client import Client

API_Key='4a2L2JdIsUGshgaCBZF56bhdTMWikgdOgQtgzkawtr7MfyM4rNfXOHztHEEzlz0S' 
Secret_Key='5d2C7XDQ7kwC51WjycVZZssr0eB8PQW5XfYzGdV9ndyxTF6ZqdoWnknnwl199D3o'
client = Client(API_Key, Secret_Key, tld='us')
client.API_URL='https://testnet.binance.vision/api'

def get_data():
  url = 'https://api.binance.com/api/v3/avgPrice?symbol=BNBBTC'
  data = requests.get(url).json()
  print(data)


# assets_url = "https://data.messari.io/api/v1/assets"
# assets_bytes = urllib.request.urlopen(assets_url).read()
# assets_json = assets_bytes.decode('utf8').replace("'", '"')
# assets_dict = json.loads(assets_json)

# ticker_list = []
# for asset in assets_dict["data"]:
#     if (asset["symbol"] != "btc") and (asset["symbol"] != "eth") and (asset["symbol"] != "ltc"):
#         pass
#     else:
#         ticker_list.append(asset["symbol"])
#         print(ticker_list)

# query = """
#     mutation transactionCreate(
#         $bot_name:String!,
#         $coin_abbrev:String!,
#         $username:String!,
#         $api_key:String!,
#         $is_sale:Boolean!,
#         $coin_quantity:Decimal!,
#         $contemporary_coin_price:Decimal!,
#         $profit:Decimal!,
#         $transaction_name:String!
#         ){
#         createTransaction(
#             inputData: {
#                 bot: {
#                     name: $bot_name
#                 },
#                 coin:{
#                     abbrev: $coin_abbrev
#                 }
#                 user: {
#                     username: $username
#                     apiKey: $api_key
#                 }
#                 isSale: $is_sale
#                 coinQuantity: $coin_quantity
#                 contemporaryCoinPrice: $contemporary_coin_price
#                 profit: $profit
#                 name: $transaction_name
#             }
#         ){
#             transaction{
#                 bot{
#                     name
#                     id
#                 }
#                 coin{
#                     name
#                     abbrev
#                 }
#                 user{
#                     username
#                 }
#                 coinQuantity
#                 contemporaryCoinPrice
#                 transactionDateTime
#                 profit
#                 name
#                 changeInTotal
#             }
#         }
#     }"""

# def send_mock_data(variables):
#   gqlClient.execute(query, variables)

# def random_reasonable_coin_price(coin):
#   if coin
# send_mock_data({
#   'bot_name': 'mockbot',
#   'coin_abbrev': 'BTCUSD',
#   'username': 'mockuser',
#   'api_key': 'cfc1e3f4-5d07-49fc-9bbf-05ceeeffe626',
#   'is_sale': True,
#   'coin_quantity': random.random(),
#   'contemporary_coin_price': 2,
#   'profit': 2,
#   'transaction_name': 'testtransaction'
# })