import requests 
from millify import millify
from web3 import Web3
import json
import subprocess
import os 
from dotenv import load_dotenv

load_dotenv()

FTMSCAN_API=os.getenv("FTMSCAN_API")

bsc = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(bsc))

# urls to be used 
nomics=f"https://maroz.online/api/ftm-spooky/tokens/0x49894fcc07233957c35462cfc3418ef0cc26129f"
supply=f"https://api.ftmscan.com/api?module=stats&action=tokensupply&contractaddress=0x49894fcc07233957c35462cfc3418ef0cc26129f&apikey={FTMSCAN_API}"
headers = {"User-Agent": "Chrome/79"}

print("<b><u>FANG (POTLUCK PROTOCOL TOKEN)</u></b>")
 
#extractin data from nomics 
nomics_data_temp=requests.get(url=nomics,headers=headers)
nomics_data = nomics_data_temp.json()
print('Price: $'+'<b><u>'+str('%.3f'%(float(nomics_data['price']['usd'])))+'</u></b>')
print('LP Price: $'+'<b><u>'+str('%.2f'%(float(nomics_data['lpPrice'])))+'</u></b>')


supply_temp=requests.get(url=supply,headers=headers)
supply=json.loads(supply_temp.text)

burn_url=f"https://api.ftmscan.com/api?module=account&action=tokenbalance&contractaddress=0x49894fcc07233957c35462cfc3418ef0cc26129f&address=0x000000000000000000000000000000000000dead&apikey={FTMSCAN_API}"
burn_token=requests.get(url=burn_url,headers=headers)
burn_token=burn_token.json()
supply=(web3.fromWei(int(supply['result']), 'ether'))-(web3.fromWei(int(burn_token['result']), 'ether'))

print('Circulating Supply: '+'<b><u>'+str(millify(float(supply), precision=3))+'</u></b>')


bashCmd = ["sh","fang-holders.sh"]
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
output, error = process.communicate()
lines = output.decode('utf-8').splitlines()
print(lines[0])
print("<a href='https://fantom.potluckprotocol.com/swap?outputCurrency=0x49894fcc07233957c35462cfc3418ef0cc26129f'><u>BUY ON OUR DEX - FANG</u></a>")

