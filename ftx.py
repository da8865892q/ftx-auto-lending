import hmac
import json
import schedule
import time
from datetime import datetime
from requests import Request, Session

API_KEY = ""
API_SECRET = ""
currencys = []

balances = "https://ftx.com/api/wallet/balances"
lendingInfo = "https://ftx.com/api/spot_margin/lending_info"
offers = "https://ftx.com/api/spot_margin/offers"

def main():
  now = datetime.now()
  current_time = now.strftime("%Y/%m/%d %H:%M:%S")
  print ("Current time is:", current_time)
  for currency in currencys:
    print (spotMargin(currency))

def spotMargin(currency):
  balance = getBalances(currency)
  lendable = getLendingIfo(currency)
  offer = postOffers(currency, lendable)
  size = getOffers(currency)
  return "%s balance:%s. Spot margin size:%s. Work status:%s" %(currency, balance, size, offer)

def getBalances(currency):
  request = Request('GET', balances)
  resp = getHeader(request)
  json_str = json.dumps(resp)
  resp = json.loads(json_str)
  for i in range (len(resp['result'])):
    if (resp['result'][i]['coin'] == currency):
      return (resp['result'][i]['total'])

def getLendingIfo(currency):
  request = Request('GET', lendingInfo)
  resp = getHeader(request)
  json_str = json.dumps(resp)
  resp = json.loads(json_str)
  for i in range (len(resp['result'])):
    if (resp['result'][i]['coin'] == currency):
      return (resp['result'][i]['lendable'])

def postOffers(currency, amount):
  body = {"coin":currency, "size":amount, "rate":0.000001}
  request = Request('POST', offers, json=body)
  resp = getHeader(request)
  json_str = json.dumps(resp)
  resp = json.loads(json_str)
  return resp['success']

def getOffers(currency):
  request = Request('GET', offers)
  resp = getHeader(request)
  json_str = json.dumps(resp)
  resp = json.loads(json_str)
  for i in range (len(resp['result'])):
    if (resp['result'][i]['coin'] == currency):
      return (resp['result'][i]['size'])

def getHeader(request):
  ts = int(time.time() * 1000)
  prepared = request.prepare()
  signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()

  if prepared.body: signature_payload += prepared.body
  signature_payload = signature_payload
  signature = hmac.new(API_SECRET.encode(), signature_payload, 'sha256').hexdigest()

  prepared.headers['FTX-KEY'] = API_KEY
  prepared.headers['FTX-SIGN'] = signature
  prepared.headers['FTX-TS'] = str(ts)

  session = Session()
  resp = session.send(prepared)
  return resp.json()

main()
schedule.every(1).hours.do(main)

while True:
  schedule.run_pending()
  time.sleep(1)
  