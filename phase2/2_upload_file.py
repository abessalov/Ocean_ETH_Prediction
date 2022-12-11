FILE_NAME = 'eth_predict.csv'


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


# Put the file online
from pybundlr import pybundlr
url = pybundlr.fund_and_upload(FILE_NAME, "matic", alice_wallet.private_key)
print(f"Your csv url: {url}")
