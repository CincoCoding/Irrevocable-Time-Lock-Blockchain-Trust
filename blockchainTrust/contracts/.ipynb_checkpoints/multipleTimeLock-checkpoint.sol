pragma solidity ^0.8.0;

import '@openzeppelin/contracts/token/ERC20/IERC20.sol';

contract Timelock {
    uint public constant duration = 30 seconds;
    uint public end;
    uint public balanceReceived;
    address payable public owner;
    
    constructor(address payable _owner){
        end = block.timestamp + duration;
        owner = _owner;
    }
    function withdraw() public  {
        require(owner == msg.sender);
        require ( block.timestamp >= end, 'too early');
        payable(msg.sender).transfer(address(this).balance);
    }
    function receiveMoney() public payable {
        balanceReceived += msg.value;
    }
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}