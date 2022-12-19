# Irrevocable-Time-Lock-Blockchain-Trust

Group Project 3 - December 19, 2022 - UMN Fintech

## Team Members
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
    <li><a href="#contact">Contributors</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Irrevocable Time Lock Trust][Irrevocable_Time_Lock_Trust]](https://github.com/CincoCoding/Irrevocable-Time-Lock-Blockchain-Trust/blob/Kyle/baby-trust-pic-edit.png)

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

* [![Solidity][Solidity.io]][Solidity-url]
* [![Python][Python.org]][Python-url]
* [![Streamlit][Streamlit.io]][Steamlit-url]
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
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Current Usage

The irrevocable time-lock can be set to many different time periods, and restricts any withdrawel before the time has elapsed.  The initial deposit is also variable.  The contract also restricts all entities involved (trustee, beneficiaries, time-lock) to be unchanged once submitted and signed.


## Future Usage

This project is the foundational work for a larger future project idea.  As of now there are only two beneficiaries, but could be expanded to more.  In the future there could also be automation added to the payout time-lock.  An additional feature that could be added is that of interest or APR return to the trust and therefore beneficiaries.


<p align="right">(<a href="#readme-top">back to top</a>)</p>