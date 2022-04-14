
import json
from solana.rpc.api import Client
# get_confirmed_signature_for_address2 is similar to get_signature_for_address. Get_signature_for_address is not currently supported.
import sqlite3
from discord_webhook import DiscordWebhook, DiscordEmbed

# get_confirmed_transaction is similar to get_transaction. Get_transaction is not currently supported.

solana_client = Client("https://api.mainnet-beta.solana.com")


resul = solana_client.get_confirmed_transaction("YhnzCri6D9wkMeKE1kLEWHMNjx8u5VsEZVVPSas6hquee2QSJWwKuhS2RQbMwbk8axBhhP3VsBaTUAh5s7jsHYD")

resul = resul["result"]
resul = resul["meta"]
resul = resul["logMessages"]

for c in resul:
	if "price" in str(c):
		dados = c.replace("Program log: ", "")
		break
	else:
		pass
dados = json.loads(dados)

print(dados["price"] / 1000000000)