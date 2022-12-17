// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


import '@openzeppelin/contracts/token/ERC20/IERC20.sol';


contract Timelock {
    address payable public trustee;
    address payable beneficiary1;
    address payable beneficiary2;
    
    uint public initialWithdrawalTime;
    uint public waitingPeriod;
    uint public endOfWaitingPeriod;
    uint public lastWithdrawalTimestamp;

    // maybe remove
    uint public contractBalance;

    uint trustSize;
    uint paymentPerPayoutPeriod;
    uint numberOfPayments;
    uint finalPaymentTime;


    constructor(address payable _trustee, address payable _beneficiary1, address payable _beneficiary2, uint _paymentPerPayoutPeriod, uint _waitingPeriod){
        trustee = _trustee;
        beneficiary1 = _beneficiary1;
        beneficiary2 = _beneficiary2;
                
        waitingPeriod = _waitingPeriod;
        
        paymentPerPayoutPeriod = _paymentPerPayoutPeriod;

        initialWithdrawalTime = block.timestamp;
        endOfWaitingPeriod = block.timestamp + waitingPeriod;

        numberOfPayments = trustSize/(paymentPerPayoutPeriod);
        finalPaymentTime = initialWithdrawalTime + (numberOfPayments * waitingPeriod);

        contractBalance = address(this).balance;
    }


    function withdraw() public{
        require(msg.sender == beneficiary1 || msg.sender == beneficiary2, "Only beneficiaries may withdraw from the Trust!");
        require(address(this).balance >= paymentPerPayoutPeriod, "Insufficient funds!");
        require(block.timestamp >= lastWithdrawalTimestamp + waitingPeriod, "You are not yet allowed to withdraw!");
        
        beneficiary1.transfer(paymentPerPayoutPeriod/2);
        beneficiary2.transfer(paymentPerPayoutPeriod/2);

        lastWithdrawalTimestamp = block.timestamp;
        contractBalance -= paymentPerPayoutPeriod;
        
    }


    function deposit() public payable {
        require(trustee == msg.sender, "Only the trustee may deposit!");
        contractBalance = address(this).balance;
        lastWithdrawalTimestamp = block.timestamp;
        trustSize = msg.value;
    }

     // function() external payable {}

}
