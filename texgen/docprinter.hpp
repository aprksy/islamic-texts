#ifndef DOCPRINTER_HPP
#define DOCPRINTER_HPP

template <typename T>
class DocPrinter: 
{
public:
    virtual void Print(T* data) const = 0;
};


#endif