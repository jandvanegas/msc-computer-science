//
// Created by javanegas on 18/04/22.
//

#include <iostream>
#include "ResultCode.h"

int ResultCode::getCode() const {return this->code;}
ResultCode::ResultCode() {this->code=0;}
ResultCode::ResultCode(int code) {this->code=code;}
ResultCode::~ResultCode() {std::cout << "Destroying" << std::endl;}

int internalResultCode() {
    ResultCode rc(3);
    return rc.getCode();
}

int main(){
    ResultCode rc(3), rc2;
    internalResultCode();
    std::cout << "The code is: " << rc.getCode() << std::endl;
    std::cout << "The code is: " << rc2.getCode() << std::endl;
}
