#ifndef DOCUMENT_HPP
#define DOCUMENT_HPP

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <memory>
#include <yaml-cpp/yaml.h>

namespace defaultValues
{
    const std::string rootDir = "/home/aprksy/workspace/typesetting/islamic-texts";
    const std::string fileName = "doc.yaml";
    const std::string localDir = rootDir + "/content/ratib-alhaddad";
    const std::string reusablesDir = rootDir + "/reusable";
    const std::string assetsDir = localDir + "/assets";
}

struct DocData
{
    std::string title;
    std::vector<std::string> authors;
    std::string version;
    std::string license;
};

struct Typesetter
{
    std::string name;
    std::string email;
    std::map<std::string, std::string> urls;
};

enum DecorationKind {
    Frame,
    Background,
    Foreground
};

enum ResourceType {
    TeX,
    Pdf,
    Raster,
    Vector
};

struct Content
{
    std::string sourceFile;
    ResourceType type;
};

struct Decoration
{
    Content content;
    DecorationKind kind; 
};

class Document
{
private:
    std::string mFileName,
                mLocalPath,
                mReusablePath,
                mAssetPath;
protected:
    std::unique_ptr<DocData> docData;
    std::unique_ptr<Typesetter> typeSetter;

    void ParseDocSection(YAML::Node doc);
public:
    void Parse();
    void Parse(std::string fileName);
    Document(): Document(defaultValues::fileName) {};
    Document(std::string fileName): Document(fileName, 
                                             defaultValues::localDir, 
                                             defaultValues::reusablesDir, 
                                             defaultValues::assetsDir) {};
    Document(std::string fileName, 
             std::string localPath, 
             std::string reusablePath,
             std::string assetPath): 
                         mFileName(fileName), 
                         mLocalPath(localPath),
                         mReusablePath(reusablePath),
                         mAssetPath(assetPath) {};
    ~Document() {};

    DocData* getDocData() const { return docData.get(); };
};

#endif