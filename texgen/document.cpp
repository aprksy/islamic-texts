#include "document.hpp"
#include <iostream>
#include <yaml-cpp/yaml.h>

void Document::ParseDocSection(YAML::Node doc)
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
        docData = std::unique_ptr<DocData>(new DocData{title, authors, version, license});

        std::cout << docData->title << std::endl;
        std::cout << "authors size: " << authors.size() << std::endl;
        for (auto author: docData->authors) {
            std::cout << author << std::endl;
        }
        std::cout << docData->version << std::endl;
        std::cout << docData->license << std::endl;

        auto [a, b, c, d] = *getDocData();
        std::cout << a << c << d << std::endl;
    }
    catch(const YAML::ParserException& e)
    {
        std::cerr << e.msg << std::endl;
    }
}

void Document::Parse()
{
    try
    {
        auto doc = YAML::LoadFile(mLocalPath + "/" + mFileName);
        ParseDocSection(doc);
    }
    catch(const YAML::BadFile& e)
    {
        std::cerr << e.msg << std::endl;
    }    
}

void Document::Parse(std::string fileName)
{
    mFileName = fileName;
    Parse();
}
