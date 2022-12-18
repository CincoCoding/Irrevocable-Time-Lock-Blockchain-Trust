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
irrevocableTrust_bytecode = "6101206040523480156200001257600080fd5b5060405162000d1238038062000d1283398181016040528101906200003891906200012e565b8473ffffffffffffffffffffffffffffffffffffffff1660808173ffffffffffffffffffffffffffffffffffffffff1660601b815250508373ffffffffffffffffffffffffffffffffffffffff1660a08173ffffffffffffffffffffffffffffffffffffffff1660601b815250508273ffffffffffffffffffffffffffffffffffffffff1660c08173ffffffffffffffffffffffffffffffffffffffff1660601b815250508060e0818152505081610100818152505047600381905550505050505062000222565b6000815190506200011181620001ee565b92915050565b600081519050620001288162000208565b92915050565b600080600080600060a086880312156200014757600080fd5b6000620001578882890162000100565b95505060206200016a8882890162000100565b94505060406200017d8882890162000100565b9350506060620001908882890162000117565b9250506080620001a38882890162000117565b9150509295509295909350565b6000620001bd82620001c4565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b620001f981620001b0565b81146200020557600080fd5b50565b6200021381620001e4565b81146200021f57600080fd5b50565b60805160601c60a05160601c60c05160601c60e05161010051610a55620002bd60003960008181610353015281816103f2015281816104850152818161051701526105800152600081816101db015281816102e301526104e30152600081816102540152818161044901526106490152600081816101ff015281816103b601526105520152600081816105bb015261066d0152610a556000f3fe6080604052600436106100865760003560e01c8063bf2ac66611610059578063bf2ac66614610123578063d0e30db01461014e578063f3f2f0bc14610158578063fdf97cb214610183578063fe4aaab2146101ae57610086565b80633a2ef9df1461008b5780633ccfd60b146100b65780634f52ccfa146100cd5780635c8de34c146100f8575b600080fd5b34801561009757600080fd5b506100a06101d9565b6040516100ad919061089e565b60405180910390f35b3480156100c257600080fd5b506100cb6101fd565b005b3480156100d957600080fd5b506100e2610550565b6040516100ef9190610803565b60405180910390f35b34801561010457600080fd5b5061010d610574565b60405161011a919061089e565b60405180910390f35b34801561012f57600080fd5b5061013861057e565b604051610145919061089e565b60405180910390f35b6101566105a2565b005b34801561016457600080fd5b5061016d610647565b60405161017a9190610803565b60405180910390f35b34801561018f57600080fd5b5061019861066b565b6040516101a59190610803565b60405180910390f35b3480156101ba57600080fd5b506101c361068f565b6040516101d0919061089e565b60405180910390f35b7f000000000000000000000000000000000000000000000000000000000000000081565b7f000000000000000000000000000000000000000000000000000000000000000073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614806102a257507f000000000000000000000000000000000000000000000000000000000000000073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16145b6102e1576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016102d89061083e565b60405180910390fd5b7f000000000000000000000000000000000000000000000000000000000000000060005461030f91906108ca565b421015610351576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016103489061085e565b60405180910390fd5b7f00000000000000000000000000000000000000000000000000000000000000004710156103b4576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016103ab9061087e565b60405180910390fd5b7f000000000000000000000000000000000000000000000000000000000000000073ffffffffffffffffffffffffffffffffffffffff166108fc60027f000000000000000000000000000000000000000000000000000000000000000061041b9190610920565b9081150290604051600060405180830381858888f19350505050158015610446573d6000803e3d6000fd5b507f000000000000000000000000000000000000000000000000000000000000000073ffffffffffffffffffffffffffffffffffffffff166108fc60027f00000000000000000000000000000000000000000000000000000000000000006104ae9190610920565b9081150290604051600060405180830381858888f193505050501580156104d9573d6000803e3d6000fd5b50426000819055507f000000000000000000000000000000000000000000000000000000000000000060005461050f91906108ca565b6001819055507f0000000000000000000000000000000000000000000000000000000000000000600360008282546105479190610951565b92505081905550565b7f000000000000000000000000000000000000000000000000000000000000000081565b6000600354905090565b7f000000000000000000000000000000000000000000000000000000000000000081565b3373ffffffffffffffffffffffffffffffffffffffff167f000000000000000000000000000000000000000000000000000000000000000073ffffffffffffffffffffffffffffffffffffffff1614610630576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016106279061081e565b60405180910390fd5b426000819055503460028190555047600381905550565b7f000000000000000000000000000000000000000000000000000000000000000081565b7f000000000000000000000000000000000000000000000000000000000000000081565b6000600154905090565b6106a281610985565b82525050565b60006106b5601d836108b9565b91507f4f6e6c79207468652074727573746565206d6179206465706f736974210000006000830152602082019050919050565b60006106f5603a836108b9565b91507f4f6e6c792064657369676e617465642062656e65666963696172696573206d6160008301527f792077697468647261772066726f6d20746865205472757374210000000000006020830152604082019050919050565b600061075b6024836108b9565b91507f596f7520617265206e6f742079657420616c6c6f77656420746f20776974686460008301527f72617721000000000000000000000000000000000000000000000000000000006020830152604082019050919050565b60006107c16013836108b9565b91507f496e73756666696369656e742066756e647321000000000000000000000000006000830152602082019050919050565b6107fd816109b7565b82525050565b60006020820190506108186000830184610699565b92915050565b60006020820190508181036000830152610837816106a8565b9050919050565b60006020820190508181036000830152610857816106e8565b9050919050565b600060208201905081810360008301526108778161074e565b9050919050565b60006020820190508181036000830152610897816107b4565b9050919050565b60006020820190506108b360008301846107f4565b92915050565b600082825260208201905092915050565b60006108d5826109b7565b91506108e0836109b7565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03821115610915576109146109c1565b5b828201905092915050565b600061092b826109b7565b9150610936836109b7565b925082610946576109456109f0565b5b828204905092915050565b600061095c826109b7565b9150610967836109b7565b92508282101561097a576109796109c1565b5b828203905092915050565b600061099082610997565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fdfea2646970667358221220f9c626955050a9577c613eb40de0e72ea4dc5fec94f7a4a59abc151a28f49ffd64736f6c63430008000033"

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

constructContract = 1
signedContract = 2


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
    
    st.session_state.timelock_contract_instance = w3.eth.contract(address=st.session_state.transactionReceipt.contractAddress, abi=irrevocableTrust_ABI)
    ################################################################################
    # Use the timelock contract functions from Solidity
    # each function that changes contract state must be;
    # paid for, signed, sent, and received(via receipt)
    ################################################################################
    
# Create contract instance
e = st.button("Contract Instance")
if e:
    print("hi")
# Transact payable solidity function receiveMoney that moves ETH from wallet to contract
receiveMoneyTransaction = timelock_contract_instance.functions.receiveMoney().buildTransaction(
{
'from': trustee_address,
'value': int(transaction_amount),
'chainId': 1337,
'nonce': nonce + 1}
)

# Sign transaction again
receiveMoneysigned_transaction = w3.eth.account.sign_transaction(receiveMoneyTransaction, private_key=str(private_key))
st.write("#### Receive Money Transaction Signed!")

# Send transaction
receiveMoneytransaction_hash = w3.eth.send_raw_transaction(receiveMoneysigned_transaction.rawTransaction)
st.write("#### Receive Money Transaction Sent!")

# Get receipt
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
timelock_contract_instance.functions.withdraw().transact({"gasPrice": w3.eth.gas_price,"chainId": 1337, "from": trustee_address,"nonce": nonce+2})

