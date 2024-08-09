#include <iostream>
#include <fmt/core.h>
#include <fmt/ranges.h>
#include "document.hpp"
#include <yaml-cpp/yaml.h>

void DOC::Document::parseInfoSection(YAML::Node doc)
{
    try
    {
        auto data = doc["document"];
        auto title = data["title"].as<std::string>();
        auto authors = std::vector<std::string>(); 
        for (auto el: data["authors"]) {
            authors.push_back(el.as<std::string>());
        }
        auto version = data["version"].as<std::string>();
        auto license = data["license"].as<std::string>();
        info = std::shared_ptr<DOC::Info>(new DOC::Info{title, authors, version, license});
    }
    catch(const YAML::ParserException& e)
    {
        std::cerr << e.msg << std::endl;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }
}

void DOC::Document::parseTypesetterSection(YAML::Node doc)
{
}

void DOC::Document::parse()
{
    try
    {
        auto doc = YAML::LoadFile(mLocalPath + "/" + mFileName);
        parseInfoSection(doc);
    }
    catch(const YAML::BadFile& e)
    {
        std::cerr << e.msg << std::endl;
    }    
}

void DOC::Document::parse(std::string fileName)
{
    mFileName = fileName;
    parse();
}

void DOC::Document::print(Visitor& printer)
{
    printer.visit(*info.get());
}

void DOC::ConsolePrinter::visit(Info &info)
{
    fmt::print("title\t: {}\n", info.title);
    fmt::print("authors\t: {}\n", info.authors);
    fmt::print("version\t: {}\n", info.version);
    fmt::print("license\t: {}\n", info.license);
}

void DOC::ConsolePrinter::visit(Typesetter &typesetter)
{
}

void DOC::ConsolePrinter::visit(Content &content)
{
}

void DOC::ConsolePrinter::visit(Decoration &decoration)
{
}
