import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import web3

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# The Load_Contract Function
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/timeLock_abi.json')) as f:
        artwork_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi
    )

    return contract

contract = load_contract()


################################################################################
# Move and Display Funds
################################################################################
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

transaction_amount = st.text_input("Transaction Amount")

# Send money from trustee to benificiaries
## NOTE: USE PYTHON DRY STANDARD HERE AND ABOVE
if st.button("Send Money"):
    w3.eth.sendTransaction({"from": str(trustee_address), "to": str(benificiary1_address), "value": int(transaction_amount) })
    w3.eth.sendTransaction({"from": str(trustee_address), "to": str(benificiary2_address), "value": int(transaction_amount) })



















# ################################################################################
# # Display ouputs tests
# ################################################################################
# st.markdown("## getBalance")
# 
# tokens = contract.functions.getBalance().call()
# 
# st.write(f"This address owns {tokens} ETH. ")
# 
# 
# ################################################################################
# # Display ouputs tests
# ################################################################################
# 
# if st.button("receiveMoney"):
#     
#     st.markdown("## receiveMoney")
#     
#     tokens2 = contract.functions.receiveMoney().call()
#     
#     st.write(f"{tokens2}")
# 
# 
# ################################################################################
# # Display ouputs tests
# ################################################################################
# 
# if st.button("Withdraw"):
#     
#     st.markdown("## Withdraw")
#     
#     tokens3 = contract.functions.withdraw().call()
#     
#     st.write(f"{tokens3}")
#     
# ################################################################################
# # Display button test
# ################################################################################
# if st.button("Display"):
# 
#     st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.J5bwL1q6MkKxAl8goxvinQHaD4%26pid%3DApi&f=1&ipt=2b1d4fde012dae21280d3787977dfdbec9bfc71863f0342153f9cd576b0015d4&ipo=images")
# 
# ################################################################################
# # Display ouputs tests
# ################################################################################
# 

