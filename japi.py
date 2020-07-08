import json
import urllib.request

apikey = 'Z5QSJWGCO3Q05M7R'
QUERY_URL = "https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=AAPL&apikey=Z5QSJWGCO3Q05M7R"

def StockData(symbol):
  try:
    ts = TimeSeries(key=apikey, output='')
    data, metadata = ts.get_intraday(symbol=symbol, interval='1min')
    return str(data.tail(1).iloc[0]['4. close'])
  except:
    return "please try again"
  
def main():
  f = open('japi.out', 'w')
  while 1:
    userinput = input('Please enter the symbol: ').upper()
    if userinput != "EXIT":
      response = 'The current price of {} is {}\n'.format(userinput, StockData(userinput))
      print(response)
      f.write(response)
    else:
      raise System_Exit

main()
