// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '@openzeppelin/contracts/token/ERC20/IERC20.sol';

contract irrevocableTrust {
    address payable public immutable trustee; // deposits
    address payable public immutable beneficiary1; // withdraws
    address payable public immutable beneficiary2; // withdraws
    
    uint immutable public waitingPeriod; // minimum time between payments to beneficiaries
    uint lastWithdrawalTimestamp; // record the most recent withdrawal's time and date
    uint nextAvailableWithdrawalTime;

    uint depositedAmount;
    uint immutable public paymentPerPayoutPeriod; // how much beneficiaries receive per withdrawal
    
    uint contractBalance;

    // constructor sets up the irrevocableTrust but still needs deposit from trustee
    constructor(address payable _trustee, address payable _beneficiary1, address payable _beneficiary2, uint _paymentPerPayoutPeriod, uint _waitingPeriod){
        trustee = _trustee;
        beneficiary1 = _beneficiary1;
        beneficiary2 = _beneficiary2;

        waitingPeriod = _waitingPeriod;
        paymentPerPayoutPeriod = _paymentPerPayoutPeriod;
        contractBalance = address(this).balance;
    }

    function withdraw() public{
        require(msg.sender == beneficiary1 || msg.sender == beneficiary2, "Only designated beneficiaries may withdraw from the Trust!");
        require(block.timestamp >= lastWithdrawalTimestamp + waitingPeriod, "You are not yet allowed to withdraw!");
        require(address(this).balance >= paymentPerPayoutPeriod, "Insufficient funds!");

        beneficiary1.transfer(paymentPerPayoutPeriod/2); // paymentPerPayoutPeriod(withdrawal) is split equally between beneficiaries
        beneficiary2.transfer(paymentPerPayoutPeriod/2);

        lastWithdrawalTimestamp = block.timestamp; // update for next withdrawal
        nextAvailableWithdrawalTime = lastWithdrawalTimestamp + waitingPeriod;
        contractBalance -= paymentPerPayoutPeriod;      
    }

    function deposit() public payable {
        require(trustee == msg.sender, "Only the trustee may deposit!");

        lastWithdrawalTimestamp = block.timestamp; // update for initial withdrawal wait
        depositedAmount = msg.value;
        contractBalance = address(this).balance;
    }

    // getters
    function viewContractBalance() public view returns (uint) {
        return contractBalance;
    }
    function viewNextAvailableWithdrawalTime() public view returns (uint) { 
        return nextAvailableWithdrawalTime - lastWithdrawalTimestamp;
    }

}
