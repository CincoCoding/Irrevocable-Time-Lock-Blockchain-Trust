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
with open(Path('./contracts/compiled/irrevocableTrust_abi.json')) as f:
        irrevocableTrust_ABI = json.load(f)

# import bytecode object
with open('./contracts/compiled/irrevocableTrust_bytecode.txt', "r") as text_file:
        irrevocableTrust_bytecode = text_file.read()
        
        
# Create Contract Class Object
@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the Contract
    contract = w3.eth.contract(
        abi=irrevocableTrust_ABI,
        bytecode=irrevocableTrust_bytecode
    )

    return contract

contract = load_contract()


################################################################################
# Display Titles and Wallet Details
################################################################################

# Title
st.title("Irrevocable Time Lock Blockchain Trust")
accounts = w3.eth.accounts

# Use a Streamlit component to get the address of the trustee owner from the user
trusteeAddress = st.sidebar.selectbox("Select Trustee", options=accounts)

# Use a Streamlit component to get the address of the beneficiary one from the user
beneficiary1Address = st.sidebar.selectbox("Select Beneficiary One", options=accounts)

# Use a Streamlit component to get the address of the beneficiary two from the user
beneficiary2Address = st.sidebar.selectbox("Select Beneficiary Two", options=accounts)

# Display trustee balance
trusteeBalance = str(w3.eth.getBalance(trusteeAddress))
st.write("#### Trustee Balance: ")
st.write(f"###### {trusteeBalance}")
         
# Display beneficiary1 balance
beneficiary1Balance = str(w3.eth.getBalance(beneficiary1Address))
st.write("#### Beneficiary One Balance: ")
st.write(f"##### {beneficiary1Balance}")

# Display beneficiary2 balance
beneficiary2Balance = str(w3.eth.getBalance(beneficiary2Address))
st.write("#### Beneficiary Two Balance: ")
st.write(f"##### {beneficiary2Balance}")

with st.sidebar:
    # User selects amount to deposit into contract
    paymentPerPayoutPeriod = st.text_input("paymentPerPayoutPeriod")
    waitingPeriod = st.text_input("waitingPeriod")

    # Transactions must be signed with private key
    privateKey = st.text_input("Trustee Private Key")

    
################################################################################
# Create and Deploy Contract
################################################################################

# Nonce for security
nonce = w3.eth.getTransactionCount(trusteeAddress)
beneficiary1Nonce = w3.eth.getTransactionCount(beneficiary1Address)


with st.sidebar:
    a = st.button('Construct Contract')
    if a:
        st.session_state.constructContract = contract.constructor(Web3.toChecksumAddress(trusteeAddress), Web3.toChecksumAddress(beneficiary1Address), Web3.toChecksumAddress(beneficiary2Address), int(paymentPerPayoutPeriod), int(waitingPeriod)).buildTransaction({"gasPrice": w3.eth.gas_price,"chainId": 1337, "from": trusteeAddress,"nonce": nonce})
        st.write(st.session_state.constructContract)

    b = st.button('Sign Contract')
    if b:
        st.session_state.signedContract = w3.eth.account.sign_transaction(st.session_state.constructContract, private_key=str(privateKey))
        st.write("#### Contract Signed!")

    c = st.button("Send Contract")
    if c:
        st.session_state.contractTransactionHash = w3.eth.send_raw_transaction(st.session_state.signedContract.rawTransaction)
        st.write("#### Signed Transaction Sent!")
  

    d = st.button("Don't forget your receipt!")
    if d:
    # Don't forget your receipt
        st.session_state.transactionReceipt = w3.eth.waitForTransactionReceipt(st.session_state.contractTransactionHash)
        st.write(st.session_state.transactionReceipt)
    
        st.session_state.irrevocableTrust_contract_instance = w3.eth.contract(address=st.session_state.transactionReceipt.contractAddress, abi=irrevocableTrust_ABI)
    ################################################################################
    # Use the timelock contract functions from Solidity
    # each function that changes contract state must be;
    # paid for, signed, sent, and received(via receipt)
    ################################################################################
    
deposit_amount = st.text_input("Deposit Amount: ")
beneficiary1PrivateKey = st.text_input("Beneficiary 1 Private Key")
# Create contract instance
e = st.button("Deposit")
if e:
    # Transact payable solidity function receiveMoney that moves ETH from wallet to contract
    st.session_state.deposit = st.session_state.irrevocableTrust_contract_instance.functions.deposit().buildTransaction(
    {
    'from': trusteeAddress,
    'value': int(deposit_amount),
    'chainId': 1337,
    'nonce': nonce}
    )
    
    # Sign transaction again
    st.session_state.signed_deposit = w3.eth.account.sign_transaction(st.session_state.deposit, private_key=str(privateKey))
    st.write("#### Deposit Signed!")
    
    # Send transaction
    st.session_state.depositTransactionHash = w3.eth.send_raw_transaction(st.session_state.signed_deposit.rawTransaction)
    st.write("#### Deposit Sent!")
    
    # Get receipt
    st.session_state.depositReceipt = w3.eth.waitForTransactionReceipt(st.session_state.depositTransactionHash)
    st.write("#### Deposit Receipt")
    st.write(st.session_state.depositReceipt)

# Create contract instance
f = st.button("withdraw")
if f:
    # Transact payable solidity function receiveMoney that moves ETH from wallet to contract
    st.session_state.withdrawal = st.session_state.irrevocableTrust_contract_instance.functions.withdraw().buildTransaction(
    {
    'from': beneficiary1Address,
    'value': 0,
    'chainId': 1337,
    'nonce': beneficiary1Nonce}
    )
    
    # Sign transaction again
    st.session_state.signed_withdrawal = w3.eth.account.sign_transaction(st.session_state.withdrawal, private_key=str(beneficiary1PrivateKey))
    st.write("#### Withdrawal Signed!")
    
    # Send transaction
    st.session_state.withdrawalTransactionHash = w3.eth.send_raw_transaction(st.session_state.signed_withdrawal.rawTransaction)
    st.write("#### Withdrawal Sent!")
    
    # Get receipt
    st.session_state.withdrawalReceipt = w3.eth.waitForTransactionReceipt(st.session_state.withdrawalTransactionHash)
    st.write("#### Withdrawal Receipt")
    st.write(st.session_state.withdrawalReceipt)
    
# GETTERS BELOW
g = st.button("View Balance")
if g:
    # View contract's ETH balance (FREE)
    st.session_state.contractBalance = st.session_state.irrevocableTrust_contract_instance.functions.viewContractBalance().call()
    st.write(st.session_state.contractBalance)
