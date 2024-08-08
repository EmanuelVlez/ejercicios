// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
import "./Storage.sol";
contract Balaces is Storage{
    address public owner;
    mapping(address user => uint balaces) public balances;

    event Suma(address user,uint value,uint newBalances);

    constructor(){
        owner = msg.sender;
    }

    function suma(uint value) public {
        store(balances[msg.sender]);
        balances[msg.sender] += value;
        emit Suma(msg.sender, value, balances[msg.sender]);
    }

    function resta(uint value) public view returns(uint){
        require(value <= balances[msg.sender]);
        return balances[msg.sender]-value;
    }
}