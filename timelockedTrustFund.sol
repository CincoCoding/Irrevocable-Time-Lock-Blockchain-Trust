pragma solidity ^0.8.0;

contract Timelock {

    uint public constant duration = 30 seconds;
    uint public end;
    uint public balanceReceived;
    uint public constant withdrawalInterval = 30 seconds;
    uint public lastWithdrawalTimestamp;
    address payable public owner;
    
   

    constructor(address payable _owner){
        end = block.timestamp + duration;
        
        
        owner = _owner;
    }
/* Function to allow money to be deposited */
    function receiveMoney() public payable {
        balanceReceived += msg.value;
    }
/* Function that displays the balance of the contract */
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
/* Function that handles the logic of locking the funds for a specified amount of time, and relocks the funds after each withdrawal has been made*/

    function withdrawAfterTime() public {
        require(owner == msg.sender, "Only the contract owner can make a withdrawal.");
        require(block.timestamp >= lastWithdrawalTimestamp + withdrawalInterval, "Withdrawal interval has not yet passed");
        require ( block.timestamp >= end, "Initial withdrawal interval has not yet passed.");
        lastWithdrawalTimestamp = block.timestamp;
        
        owner.transfer(1 ether);

    }
  
}