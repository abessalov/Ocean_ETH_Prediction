import time
NAME = "ETH predictions" + str(time.time())
URL  = "<your csv url>" 
#e.g. url = "https://arweave.net/qctEbPb3CjvU8LmV3G_mynX74eCxo1domFQIlOBH1xU"

###########################
# Create Ocean instance
from ocean_lib.example_config import ExampleConfig
from ocean_lib.ocean.ocean import Ocean
config = ExampleConfig.get_config("https://polygon-rpc.com") # points to Polygon mainnet
config["BLOCK_CONFIRMATIONS"] = 1 #faster
ocean = Ocean(config)


# Create Alice's wallet (you're Alice)
import os
from ocean_lib.web3_internal.wallet import Wallet
alice_private_key = os.getenv('REMOTE_TEST_PRIVATE_KEY1')
alice_wallet = Wallet(ocean.web3, alice_private_key, config["BLOCK_CONFIRMATIONS"], config["TRANSACTION_TIMEOUT"])
assert alice_wallet.web3.eth.get_balance(alice_wallet.address) > 0, "Alice needs MATIC"


# Publish the csv as an Ocean asset, in Polygon
asset = ocean.assets.create_url_asset(NAME, URL, alice_wallet) #will take 30+ seconds
datatoken_address = asset.datatokens[0]["address"]
print(f"New asset created, with did={asset.did}, and datatoken_address={datatoken_address}")


# Share predictions to judges, in Polygon
#retrieve Datatoken object
from ocean_lib.models.datatoken import Datatoken
datatoken = Datatoken(ocean.web3, datatoken_address)
#send tokens to judges
to_address="0xA54ABd42b11B7C97538CAD7C6A2820419ddF703E" #official judges address
datatoken.mint(to_address, ocean.to_wei(10), alice_wallet)