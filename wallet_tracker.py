# get_confirmed_signature_for_address2 is similar to get_signature_for_address. Get_signature_for_address is not currently supported.
import sqlite3


import time
from solana.rpc.api import Client


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
				print("NENHUM")
			else:
				resul = resul[0]
				mint = resul["mint"]
				own = resul['owner']
				if mint == '':
					print("BUG")
				else:
					if own == "DUC1tgNPbceu91hLCkS1rfDDTAcgb1vqctqaoTsrSjoR":
						print("COMPROU")
						print(mint)
						print(own)
						
					else:
						print("VENDEU")
						print(mint)
						print(own)
		else:
			print("NÃO É COMPRA")




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
			ver_signature(sign)
			print("\n")
			cursor.execute(f"""
INSERT INTO signatures (signature)
VALUES ("{sign}")
""")
			conn.commit()
			
            
			
			
			#sinais_vistos.append(sign)
	time.sleep(60)
		


