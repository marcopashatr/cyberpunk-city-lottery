import requests
import ast

snapshot = requests.get("https://raw.githubusercontent.com/marcopashatr/cyberpunk-city-lottery/main/snapshot.txt")
wallets = snapshot.text

wallets = ast.literal_eval(wallets)

nonce1 = 11815500 #approx block-heights for 9:00 AM UTC 29.10.2022
nonce2 = 11815501 #approx block-heights for 9:00 AM UTC 29.10.2022
nonce3 = 11815502 #approx block-heights for 9:00 AM UTC 29.10.2022

api1 = requests.get(f"https://api.elrond.com/blocks?nonce={nonce1}&withProposerIdentity=false") #fetching 1st block information
api2 = requests.get(f"https://api.elrond.com/blocks?nonce={nonce2}&withProposerIdentity=false") #fetching 2nd block information
api3 = requests.get(f"https://api.elrond.com/blocks?nonce={nonce3}&withProposerIdentity=false") #fetching 3rd block information

data1 = api1.json() #converting the data to json
data2 = api2.json() #converting the data to json
data3 = api3.json() #converting the data to json

hash1 = data1[0]["hash"] #getting the block hash for nonce1
hash2 = data2[0]["hash"] #getting the block hash for nonce2
hash3 = data3[0]["hash"] #getting the block hash for nonce3

x1 = int(hash1, 16) #convert hash hex to integer
x2 = int(hash2, 16) #convert hash hex to integer
x3 = int(hash3, 16) #convert hash hex to integer

sum = x1 + x2 - x3  #to make numbers mixed together


mod = len(wallets) #total numbers of the snanshot wallets
winnerId = sum % mod
winner1 = wallets[winnerId]
print("The first winner is: " + winner1)


while (winner1 in wallets):
    wallets.remove(winner1)


mod = len(wallets)
winnerId = sum % mod
winner2 = wallets[winnerId]
print("The second winner  is: " + winner2)





