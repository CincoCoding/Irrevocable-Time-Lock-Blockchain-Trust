################################################################################
# Import libraries
################################################################################
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import web3

# Load .env file
load_dotenv()

# Define and connect to a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))


################################################################################
# Load Contract
################################################################################

# import ABI file
with open(Path('./contracts/compiled/timeLock_abi.json')) as f:
        timeLock_ABI = json.load(f)

# import bytecode object
timeLock_bytecode = "608060405234801561001057600080fd5b5060405161061c38038061061c833981810160405281019061003291906100a1565b601e4261003f91906100ca565b60008190555080600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550506101a2565b60008151905061009b8161018b565b92915050565b6000602082840312156100b357600080fd5b60006100c18482850161008c565b91505092915050565b60006100d582610152565b91506100e083610152565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff038211156101155761011461015c565b5b828201905092915050565b600061012b82610132565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b61019481610120565b811461019f57600080fd5b50565b61046b806101b16000396000f3fe6080604052600436106100705760003560e01c806352a90c421161004e57806352a90c42146100e25780636d26ec181461010d5780638da5cb5b14610117578063efbe1c1c1461014257610070565b80630fb5a6b41461007557806312065fe0146100a05780633ccfd60b146100cb575b600080fd5b34801561008157600080fd5b5061008a61016d565b6040516100979190610348565b60405180910390f35b3480156100ac57600080fd5b506100b5610172565b6040516100c29190610348565b60405180910390f35b3480156100d757600080fd5b506100e061017a565b005b3480156100ee57600080fd5b506100f7610262565b6040516101049190610348565b60405180910390f35b610115610268565b005b34801561012357600080fd5b5061012c610283565b604051610139919061030d565b60405180910390f35b34801561014e57600080fd5b506101576102a9565b6040516101649190610348565b60405180910390f35b601e81565b600047905090565b3373ffffffffffffffffffffffffffffffffffffffff16600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16146101d457600080fd5b600054421015610219576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161021090610328565b60405180910390fd5b3373ffffffffffffffffffffffffffffffffffffffff166108fc479081150290604051600060405180830381858888f1935050505015801561025f573d6000803e3d6000fd5b50565b60015481565b346001600082825461027a9190610374565b92505081905550565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60005481565b6102b8816103ca565b82525050565b60006102cb600983610363565b91507f746f6f206561726c7900000000000000000000000000000000000000000000006000830152602082019050919050565b610307816103fc565b82525050565b600060208201905061032260008301846102af565b92915050565b60006020820190508181036000830152610341816102be565b9050919050565b600060208201905061035d60008301846102fe565b92915050565b600082825260208201905092915050565b600061037f826103fc565b915061038a836103fc565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff038211156103bf576103be610406565b5b828201905092915050565b60006103d5826103dc565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fdfea2646970667358221220dc04e2b7ea9a1ac08308235ba57a2699d8ee978caa943890fa5e18c5544aa9d264736f6c63430008000033"

# Create Contract Class Object
@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the Contract
    contract = w3.eth.contract(
        abi=timeLock_ABI,
        bytecode=timeLock_bytecode
    )

    return contract

timeLock_contract = load_contract()


################################################################################
# Display Titles and Wallet Details
################################################################################

# Title
st.title("Irrevocable Time Lock Blockchain Trust")
accounts = w3.eth.accounts

# Use a Streamlit component to get the address of the trustee owner from the user
trustee_address = st.sidebar.selectbox("Select Trustee", options=accounts)

# Use a Streamlit component to get the address of the benificiary one from the user
benificiary1_address = st.sidebar.selectbox("Select Benificiary One", options=accounts)

# Use a Streamlit component to get the address of the benificiary two from the user
benificiary2_address = st.sidebar.selectbox("Select Benificiary Two", options=accounts)

# Display trustee balance
trustee_balance = str(w3.eth.getBalance(trustee_address))
st.write("## Trustee Balance: ")
st.write(f"### {trustee_balance}")
         
# Display benificiary1 balance
benificiary1_balance = str(w3.eth.getBalance(benificiary1_address))
st.write("## Benificiary One Balance: ")
st.write(f"### {benificiary1_balance}")

# Display benificiary2 balance
benificiary2_balance = str(w3.eth.getBalance(benificiary2_address))
st.write("## Benificiary Two Balance: ")
st.write(f"### {benificiary2_balance}")

# User selects amount to deposit into contract
transaction_amount = st.text_input("Deposit Into Contract Amount")


################################################################################
# Create and Deploy Contract
################################################################################

# Transactions must be signed with private key
private_key = "5ff75846b9f3b58d9e660b6dc2fd088cbe2f3582b086569dc4c29d57665d6413"

# Nonce for security
nonce = w3.eth.getTransactionCount(trustee_address)

x = "hi"
y = ''

a = st.button('Construct Contract')
if a:
    st.session_state.x = timeLock_contract.constructor(trustee_address).buildTransaction({"gasPrice": w3.eth.gas_price,"chainId": 1337, "from": trustee_address,"nonce": nonce})
    st.write(st.session_state.x)

b = st.button('Sign Transaction')
if b:
    st.write(st.session_state.x)

'''
# Push to start Contract Deployment
if st.button("Construct Contract"):  
    # Constructor
    transaction = timeLock_contract.constructor(trustee_address).buildTransaction({"gasPrice": w3.eth.gas_price,"chainId": 1337, "from": trustee_address,"nonce": nonce})
    st.write(transaction)
    
    # Sign transaction with private key
if st.button("Sign Transaction"):
    signed_transaction = w3.eth.account.sign_transaction(x, private_key=str(private_key))
    st.write("#### Contract Transaction Signed!")
    '''
    # Send signed transaction
if st.button("Send Transaction"):
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    st.write("#### Signed Transaction Sent!")
    
    # Don't forget your receipt
if st.button("Receipt"):
    transaction_receipt = w3.eth.waitForTransactionReceipt(transaction_hash)
    st.write(transaction_receipt)
    
    ################################################################################
    # Use the timelock contract functions from Solidity
    # each function that changes contract state must be;
    # paid for, signed, sent, and received(via receipt)
    ################################################################################
    
    # Create contract instance
if st.button("Deploy Contract Instance"):
    timelock_contract_instance = w3.eth.contract(address=transaction_receipt.contractAddress, abi=timeLock_ABI)
    
    # Transact payable solidity function receiveMoney that moves ETH from wallet to contract
if st.button("Receive Money"):
    receiveMoneyTransaction = timelock_contract_instance.functions.receiveMoney().buildTransaction(
    {
    'from': trustee_address,
    'value': int(transaction_amount),
    'chainId': 1337,
    'nonce': nonce + 1}
    )
    
    # Sign transaction again
if st.button("Sign Receive Money Transaction"):
    receiveMoneysigned_transaction = w3.eth.account.sign_transaction(receiveMoneyTransaction, private_key=str(private_key))
    st.write("#### Receive Money Transaction Signed!")
    
    # Send transaction
if st.button("Send Receive Money Transaction"):
    receiveMoneytransaction_hash = w3.eth.send_raw_transaction(receiveMoneysigned_transaction.rawTransaction)
    st.write("#### Receive Money Transaction Sent!")
    
    # Get receipt
if st.button("Recive Money Receipt"):
    receiveMoneytransaction_receipt = w3.eth.waitForTransactionReceipt(receiveMoneytransaction_hash)
    st.write("#### Receive Money Receipt")
    st.write(receiveMoneytransaction_receipt)
    
    # Display contract address
    contract_address = str(timelock_contract_instance.address)
    st.write("## Contract Address: ")
    st.write(f"### {contract_address}")
    
    # Display contract balance
    contract_balance = w3.eth.getBalance(contract_address)
    st.write("## Contract Balance: ")
    st.write(f"### {contract_balance}")   
    
    # NOT WORKING YET
    # withdraw solidity function that moves ETH from contract back to wallet after duration
    # timelock_contract_instance.functions.withdraw().transact({"gasPrice": w3.eth.gas_price,"chainId": 1337, "from": trustee_address,"nonce": nonce+2})

