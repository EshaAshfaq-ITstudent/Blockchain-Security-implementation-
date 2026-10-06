// SPDX-License-Identifier: MIT
pragma solidity ^0.8.37;

contract VulnerableContract {
    address public owner;
    mapping(address => uint256) public balances;

    constructor() {
        owner = msg.sender;
    }

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount);
        (bool success,) = msg.sender.call{value: amount}("");
        balances[msg.sender] -= amount;
    }

    function changeOwner(address newOwner) public {
        owner = newOwner;
    }

    function execute(address target, bytes calldata data) public {
        target.call(data);
    }

    function emergencyWithdraw() public {
        payable(msg.sender).transfer(address(this).balance);
    }
}