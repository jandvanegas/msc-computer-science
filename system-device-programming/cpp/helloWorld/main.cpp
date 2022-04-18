#include <iostream>

int main(int argc, char **args) {
    int vi;
    float vf;
    if (argc != 1) { // First argument is the name of the program by default
        std::cerr << "Parameter Error!" << std::endl;
    }
    std::cout << "Insert variables" << std::endl;
    std::cin >> vi >> vf;
    std::cout << "Values: " << vi << " " << vf << std::endl;
    return 0 ;
}
