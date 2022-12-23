<a name="readme-top"></a>

### Irrevocable-Time-Lock-Blockchain-Trust

Group Project 3 - December 19, 2022 - UMN Fintech

### Group Members
- David Garcia 
- Luke Turner
- Kyle Jensen

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![Irrevocable Time Lock Trust](./moreInfo/babyTrustPic.png)

The primary goal of our project is to create a blockchain wallet with a time-lock that acts as an irrevocable trust.  

It pays out to two beneficiaries from a privately held trust wallet via smart contract.  Upon submitting and signing the contract to the blockchain these options will become immutable and unchanging.  Following this, the contract will pay out only after the designated time-lock to the specified beneficiaries.

Adjustable Features:
* Transaction Amount
* Time-Lock Interval
* Primary Wallet Address (Trustee)
* Receiving Wallet Addresses (Beneficiaries)
* Number of Smart Contracts
* Receipt Data


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- BUILT WITH -->
## Built With

* [![Solidity][Solidity.io]][Solidity-url]
* [![Python][Python.org]][Python-url]
* [![Streamlit][Streamlit.io]][Streamlit-url]
* [![Ganache][Trufflesuite.com]][Ganache-url]
* [![Json][Json.org]][Json-url]
* [![Remix][Remix.ethereum.org]][Remix-url]
* [![Ethereum][Ethereum.org]][Ethereum-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Before running or installing anything else, the following libraries need to be installed.
* streamlit
  ```sh
  pip install streamlit
  ```
  
* web3
  ```sh
  pip install web3==5.17
  ```


### Installation


1. Download and quick install Ganach at: [https://trufflesuite.com/ganache/](https://trufflesuite.com/ganache/)
2. Clone the repo
   ```sh
   git clone https://github.com/CincoCoding/Irrevocable-Time-Lock-Blockchain-Trust.git
   ```
   
### Running Streamlit

1. Open Ganache with access to wallets
2. Locate the 'streamlitApp.py' file
3. Run the app in terminal using the command
   ```sh
   streamlit run streamlitApp.py
   ```
4. Choose Trustee and copy 'Private Key' from Ganache and paste into the applicable area
5. Choose Beneficiary 1 and copy 'Private Key' from Ganache and paste into the applicable area
6. Choose Beneficiary 2 and copy 'Private Key' from Ganache and paste into the applicable area
7. Choose Deposit amount
8. Choose time period for Time-Lock function
9. Create Contract
10. Send Contract
11. Sign Contract
12. Wait alloted Time-Lock amount of time, then withdraw using the correct wallets (Beneficiary 1 and Beneficiary 2)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage

## Current Usage

The irrevocable time-lock can be set to many different time periods, and restricts any withdrawel before the time has elapsed.  The initial deposit is also variable.  The contract also restricts all entities involved (trustee, beneficiaries, time-lock) to be unchanged once submitted and signed.


## Future Usage

This project is the foundational work for a larger future project idea.  As of now there are only two beneficiaries, but could be expanded to more.  In the future there could also be automation added to the payout time-lock.  An additional feature that could be added is that of interest or APR return to the trust and therefore beneficiaries.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: baby-trust-pic-edit.png
[Solidity.io]: https://img.shields.io/badge/solidity-363636?style=for-the-badge&logo=solidity&logoColor=white
[Solidity-url]: https://www.solidity.io/
[Python.org]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=61DAFB
[Python-url]: https://www.python.org/
[Streamlit.io]: https://img.shields.io/badge/streamlit.io-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=4FC08D
[Streamlit-url]: https://streamlit.io/
[Trufflesuite.com]: https://img.shields.io/badge/ganache-icon?style=for-the-badge&logo=ganache&logoColor=white
[Ganache-url]: https://trufflesuite.com/ganache/
[Json.org]: https://img.shields.io/badge/Json-000000?style=for-the-badge&logo=json&logoColor=FF3E00
[Json-url]: https://www.json.org/json-en.html
[Remix.ethereum.org]: https://img.shields.io/badge/Remix-000000?style=for-the-badge&logo=remix&logoColor=white
[Remix-url]: https://remix.ethereum.org/
[Ethereum.org]: https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=ethereum&logoColor=white
[Ethereum-url]: https://ethereum.org/en/

