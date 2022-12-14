pragma solidity ^0.8.0;

import '@openzeppelin/contracts/token/ERC20/IERC20.sol';

contract Timelock {
    uint public constant duration = 30 seconds;
    uint public constant payableDuration = 15 seconds;
    uint public end;
    uint public balanceReceived;
    address payable public owner;
    uint256 public withdrawalInterval = 30 seconds;
    uint256 public lastWithdrawalTimestamp;
   

    constructor(address payable _owner){
        end = block.timestamp + duration;
        
        
        owner = _owner;
    }

    function receiveMoney() public payable {
        balanceReceived += msg.value;
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }

    function withdrawAfterTime() public {
        require(owner == msg.sender);
        require(block.timestamp >= lastWithdrawalTimestamp + withdrawalInterval, "Withdrawal interval has not yet passed");
        require ( block.timestamp >= end, 'too early');
        lastWithdrawalTimestamp = block.timestamp;
        
        owner.transfer(1 ether);

    }
  
}