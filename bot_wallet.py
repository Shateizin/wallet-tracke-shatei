import requests
import time
import time
import json
from solana.rpc.api import Client
# get_confirmed_signature_for_address2 is similar to get_signature_for_address. Get_signature_for_address is not currently supported.
import sqlite3
from discord_webhook import DiscordWebhook, DiscordEmbed

# get_confirmed_transaction is similar to get_transaction. Get_transaction is not currently supported.

solana_client = Client("https://api.mainnet-beta.solana.com")







# get_confirmed_transaction is similar to get_transaction. Get_transaction is not currently supported.


def ver_signature(signa):
	resul = solana_client.get_confirmed_transaction(signa)
	
	resul = resul['result']
	resul = resul['meta']
	log_mes = resul['logMessages']
	if "InitializeMint" in str(log_mes):
		print("MINT")
	else:
		for c in log_mes:
			if c == "Program log: Instruction: Buy":
				comprando = True
				break
			else:
				comprando = False
		if comprando == True:
			resul = resul['postTokenBalances']
			if resul == []:
				return "NENHUM"
			else:
				resul = resul[0]
				mint = resul["mint"]
				own = resul['owner']
				if mint == '':
					return "BUG"
				else:
					achando_nft = requests.get(f"https://api-mainnet.magiceden.dev/v2/tokens/{mint}").json()
					
					if str(achando_nft) == "{}":
						return "NÃO É NFT"
					else:
						for c in log_mes:
							if "price" in str(c):
								dados = c.replace("Program log: ", "")
								break
							else:
								pass
						dados = json.loads(dados)
						quanto_custou = dados["price"] / 1000000000
							
							
						colecao = achando_nft["collection"]
						nome_nft = achando_nft["name"]
						if own == "DUC1tgNPbceu91hLCkS1rfDDTAcgb1vqctqaoTsrSjoR":
							return f"COMPROU \n\nNOME: {nome_nft}\n\nCOMPROU POR: {quanto_custou} SOL\n\nDONO DA NFT AGORA: {own}"
						
						else:
							return f"VENDEU \n\nNOME: {nome_nft}\n\nVENDEU POR: {quanto_custou} SOL\n\nDONO DA NFT AGORA: {own}"
						
						
		else:
			return "NÃO É COMPRA"




conn = sqlite3.connect('signatures.db')
cursor = conn.cursor()

sinais_vistos = []
while True:
	sinais = solana_client.get_signatures_for_address("DUC1tgNPbceu91hLCkS1rfDDTAcgb1vqctqaoTsrSjoR", limit=5)
	sinais = sinais['result']
	cursor.execute("""
SELECT * FROM signatures;
""")
    
	cu = cursor.fetchall()
	
	
    
	for c in sinais:
		sign = c['signature']
		
		if sign in str(cu):
			print("JÁ VISTO")
			pass
		else:
			print(sign)
			resultado = ver_signature(sign)
			
			if resultado == "NENHUM":
				print("RESULTADO: NENHUM")
				pass
				
			elif resultado == "BUG":
				print("RESULTADO: BUG")
				pass
				
			elif resultado == "NÃO É NFT":
				print("RESULTADO: NÃO É NFT")
				pass
				
			elif resultado == "MINT":
				print("RESULTADO: MINT")
				pass
				
			elif resultado == "NÃO É COMPRA":
				print("RESULTADO: NÃO É COMPRA")
				pass
				
			else:
				
				if "COMPROU" in resultado:
					resultado = resultado.replace("COMPROU","")
					webhook = DiscordWebhook(url='https://discord.com/api/webhooks/963855845395939348/uLziO-D781481NPXumh5S4OOlqQEw6krlooFwRlwPYN-mxZ0DaG289lV6Pd6pn0bOlnw')
					embed = DiscordEmbed(title='COMPROU', description=resultado, color='00FF00')
					webhook.add_embed(embed)
					response = webhook.execute()
					print(resultado)
					
				elif "VENDEU" in resultado:
					resultado = resultado.replace("VENDEU", "")
					webhook = DiscordWebhook(url='https://discord.com/api/webhooks/963855845395939348/uLziO-D781481NPXumh5S4OOlqQEw6krlooFwRlwPYN-mxZ0DaG289lV6Pd6pn0bOlnw')
					embed = DiscordEmbed(title='VENDEU', description=resultado, color='FF0000')
					webhook.add_embed(embed)
					response = webhook.execute()
					print(resultado)
					
				
				
			#data = {
#   'content': resultado
#			}
#			requests.post("https://discord.com/api/webhooks/963855845395939348/uLziO-D781481NPXumh5S4OOlqQEw6krlooFwRlwPYN-mxZ0DaG289lV6Pd6pn0bOlnw", data=data)
			
           
			print("\n")
			cursor.execute(f"""
INSERT INTO signatures (assinamentos)
VALUES ("{sign}")
""")
			conn.commit()
			
            
			
			
			#sinais_vistos.append(sign)
	time.sleep(60)
		






