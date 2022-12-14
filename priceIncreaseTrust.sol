// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/ERC20.sol";
contract PriceConsumerV3 {
    AggregatorV3Interface internal priceFeed;
    ERC20 public erc20;
    address payable public owner;
    uint balanceReceivedUSD;
    /**
     * Network: Goerli
     * Aggregator: ETH/USD
     * Address: 0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e
     */
    constructor(address payable _owner){
        priceFeed = AggregatorV3Interface(
            0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e
        );
        owner = _owner;
        erc20 = ERC20(address(this));
        
    }
  
    /**
     * Returns the latest price
     */
    function getLatestPrice() public view returns (int) {
        (
            ,
            /*uint80 roundID*/ int price /*uint startedAt*/ /*uint timeStamp*/ /*uint80 answeredInRound*/,
            ,
            ,
        ) = priceFeed.latestRoundData();
        return price;
    }
    
      function getContractBalance() public view returns (uint) {
        int price = getLatestPrice();
        uint thisContractsEthBalance = address(this).balance;
        uint thisContractsUSDBalance = thisContractsEthBalance * uint(price);
        return thisContractsUSDBalance;
    }
    
    function receiveMoney() public payable {
        int price = getLatestPrice();
        balanceReceivedUSD = (uint(price)) * msg.value;
    }
    function withdraw() public{
        require(owner == msg.sender);
        require (getContractBalance() >= (balanceReceivedUSD* 2), 'Value has not increased, withdrawal restricted.');
        
        payable(msg.sender).transfer(address(this).balance);
    
    }
}