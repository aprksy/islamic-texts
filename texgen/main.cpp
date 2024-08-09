#include <fmt/core.h>
#include "document.hpp"

int main(int argc, char *argv[]) 
{
    fmt::print("loading document... \n");
    auto doc = new DOC::Document();
    doc->parse();
    fmt::print("input parsed \n");

    auto consolePrinter = new DOC::ConsolePrinter();
    doc->print(*consolePrinter);
    delete doc;
    return 0;
}