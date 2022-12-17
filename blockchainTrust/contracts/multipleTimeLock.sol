// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


import '@openzeppelin/contracts/token/ERC20/IERC20.sol';


contract Timelock {

    address payable public trustee;
    address payable beneficiary1;
    address payable beneficiary2;
    

    uint public constant waitingPeriod = 30 seconds;
    uint public endOfWaitingPeriod;
    uint public lastWithdrawalTimestamp;

    uint public amount;
    uint public contractBalance;
 

    constructor(address payable _trustee, address payable _beneficiary1, address payable _beneficiary2){
        endOfWaitingPeriod = block.timestamp + waitingPeriod;
        trustee = _trustee;
        beneficiary1 = _beneficiary1;
        beneficiary2 = _beneficiary2;
        contractBalance = address(this).balance;
    }

    function getInfo() view public returns(address payable, address payable, address payable, uint) {
        return (trustee, beneficiary1,  beneficiary2, contractBalance);
    }

    function setInfo(address payable newTrustee, address payable newBeneficiary1, address payable newBeneficiary2) public {
        trustee = newTrustee;
        beneficiary1 = newBeneficiary1;
        beneficiary2 = newBeneficiary2;
    }

//    function withdraw(address payable recipient) public  {
    function withdraw(uint _amount,address payable _beneficiary1, address payable _beneficiary2) public  {

        amount = _amount;

        require(_beneficiary1 == beneficiary1 || _beneficiary1 == beneficiary2, "One or more members are not in this Trust!");
        require(_beneficiary2 == beneficiary1 || _beneficiary2 == beneficiary2, "One or more members are not in this Trust!");
        
        require(address(this).balance >= amount, "Sorry, your Trust has run out!");
        require (block.timestamp >= endOfWaitingPeriod, "Too Early!");
        require(block.timestamp >= lastWithdrawalTimestamp + waitingPeriod, "Withdrawal interval has not yet passed");
        contractBalance -= amount;
        beneficiary1.transfer(amount/2);
        beneficiary2.transfer(amount/2);
        lastWithdrawalTimestamp = block.timestamp;
    }


    function receiveMoney() public payable {
        contractBalance += msg.value;
    }

    function deposit() public payable {
        contractBalance = address(this).balance;
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }

   //  function() external payable {}

}
