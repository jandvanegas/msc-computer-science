//
// Created by javanegas on 18/04/22.
//

#ifndef HELLOWORLD_RESULTCODE_H
#define HELLOWORLD_RESULTCODE_H


class ResultCode {
private:
    int code;
public:
    int getCode() const;
    char* get_description();
    ResultCode();
    ~ResultCode();
    ResultCode(int);

};


#endif //HELLOWORLD_RESULTCODE_H
