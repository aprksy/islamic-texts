#include <iostream>
#include "document.hpp"

int main(int argc, char *argv[]) 
{
    std::cout << "loading document... " << std::endl;
    auto doc = new Document();
    doc->Parse();
    std::cout << "input parsed " << std::endl;
    delete doc;
    return 0;
}