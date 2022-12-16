//SPDX-License-Identifier: MIT

pragma solidity ^0.5.0;

contract CustomerAccount {
    address payable owner;
    bool isNewAccount;
    uint public accountBalance;
    address payable authorizedRecipient;
    uint public constant duration = 30 seconds;
    uint public end;
    uint public balanceReceived;
    uint public constant withdrawalInterval = 30 seconds;
    uint public lastWithdrawalTimestamp;

    function getInfo() view public returns(address, address payable) {
        return (owner, authorizedRecipient);
    }

    function setInfo(address payable newOwner, address payable newAuthorizedRecipient) public {
        owner = newOwner;
        authorizedRecipient = newAuthorizedRecipient;
    }

    function sendRemittance(uint amount, address payable recipient) public {
        require(recipient == owner || recipient == authorizedRecipient, "The recipient address is not authorized!");
        recipient.transfer(amount);
        accountBalance = address(this).balance;
    }

    function deposit() public payable {
        accountBalance = address(this).balance;
    }

    function withdrawAfterTime() public {
        require(owner == msg.sender, "Only the contract owner can make a withdrawal.");
        require(block.timestamp >= lastWithdrawalTimestamp + withdrawalInterval, "Withdrawal interval has not yet passed");
        require ( block.timestamp >= end, "Initial withdrawal interval has not yet passed.");
        lastWithdrawalTimestamp = block.timestamp;
        
        owner.transfer(1 ether);

    }
  