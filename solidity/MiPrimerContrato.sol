// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;

// importaciones 
// interfaces

contract MiPrimerContrato{
    bool public verdaderoOfalso;
    uint numeroSinSigno;
    int numeroConSigno;
    string cadenaDeLetras;
    address public direccionesDeEthereum;

    uint [] estoEsUnVector;
    mapping(address => uint) public estoMapping;

    //eventos

    constructor(uint balance){
        estoMapping[msg.sender] = balance;
    }
    function nombreFuncion(uint resta)external returns(uint) {
        uint value = estoMapping[msg.sender];
        estoMapping[msg.sender] -= resta;
        return value;
    }

    function setDireccionDeEthereum() public {
        direccionesDeEthereum = msg.sender;
    }

    function _setNumber(uint _number) internal {
        numeroSinSigno = _number;
    }
}