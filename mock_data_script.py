from graphqlclient import GraphQLClient
gqlClient = GraphQLClient('https://crypto-bots-back.herokuapp.com/graphql')
import random
import requests
from datetime import datetime
import json


def coin_price(coin):
  url = 'https://api.binance.com/api/v3/avgPrice?symbol=' + coin
  price = requests.get(url).json()['price']
  return price

query = """
    mutation transactionCreate(
        $bot_name:String!,
        $coin_abbrev:String!,
        $username:String!,
        $api_key:String!,
        $is_sale:Boolean!,
        $coin_quantity:Decimal!,
        $transaction_price:Decimal!,
        $contemporary_coin_price:Decimal!,
        $profit:Decimal!,
        $transaction_name:String!
        ){
        createTransaction(
            inputData: {
                bot: {
                    name: $bot_name
                },
                coin:{
                    abbrev: $coin_abbrev
                }
                user: {
                    username: $username
                    apiKey: $api_key
                }
                isSale: $is_sale
                coinQuantity: $coin_quantity
                transactionPrice: $transaction_price
                contemporaryCoinPrice: $contemporary_coin_price
                profit: $profit
                name: $transaction_name
            }
        ){
            transaction{
                bot{
                    name
                    id
                }
                coin{
                    name
                    abbrev
                }
                user{
                    username
                }
                coinQuantity
                transactionPrice
                contemporaryCoinPrice
                transactionDateTime
                profit
                name
                changeInTotal
            }
        }
    }"""

def send_mock_data(botName, isSale, coins):
  for coin in coins:
    if botName == 'mockmarketbot':
      positiveOrNegative = -1 if random.random() < .5 else 1
      transaction_price_deviation_from_contemporary_price = random.random() * positiveOrNegative
    else:
      transaction_price_deviation_from_contemporary_price = random.random() * 10
    price = float(coin_price(coin))
    quanity = random.random()
    if isSale:
      transactionPrice = price + transaction_price_deviation_from_contemporary_price
      profit = ( quanity * transactionPrice ) - ( quanity * price )
    else:
      transactionPrice = price - transaction_price_deviation_from_contemporary_price
      profit = ( quanity * price ) - ( quanity * transactionPrice )

    variables = {
        'bot_name': botName,
        'coin_abbrev': coin,
        'username': 'mockuser',
        'api_key': 'cfc1e3f4-5d07-49fc-9bbf-05ceeeffe626',
        'is_sale': False,
        'coin_quantity': quanity,
        'transaction_price': transactionPrice,
        'contemporary_coin_price': price,
        'profit': profit,
        'transaction_name': botName + coin + datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
      }
    gqlClient.execute(query, variables)

currentCoins = [ 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ]

send_mock_data('mockbot', False, currentCoins)
send_mock_data('mockbot', True, currentCoins)
send_mock_data('mockmarketbot', False, currentCoins)
send_mock_data('mockbot2', False, currentCoins)
send_mock_data('mockbot2', True, currentCoins)
send_mock_data('mockbot3', False, currentCoins)
send_mock_data('mockbot3', True, currentCoins)