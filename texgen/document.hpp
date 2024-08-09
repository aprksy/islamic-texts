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

// start namespace DOC
namespace DOC
{

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

class Info;
class Typesetter;
class Content;
class Decoration;

class Visitor
{
public:
    virtual void visit(Info& info) = 0;
    virtual void visit(Typesetter& typesetter) = 0;
    virtual void visit(Content& content) = 0;
    virtual void visit(Decoration& decoration) = 0;
};

class Element
{
public:
    virtual void accept(Visitor* visitor) = 0;
};

class Info: public Element
{
public:
    std::string title;
    std::vector<std::string> authors;
    std::string version;
    std::string license;

    Info(std::string _title,
         std::vector<std::string> _authors,
         std::string _version,
         std::string _license): 
            title(_title),
            authors(_authors),
            version(_version),
            license(_license) {};
    void accept(Visitor* visitor) override { visitor->visit(*this); };
};

class Typesetter: public Element
{
public:
    std::string name;
    std::string email;
    std::map<std::string, std::string> urls;

    Typesetter(std::string _name,
               std::string _email,
               std::map<std::string, std::string> _urls): 
                    name(_name),
                    email(_email),
                    urls(_urls) {};
    void accept(Visitor* visitor) override { visitor->visit(*this); };
};

class Content: public Element
{
public:
    std::string sourceFile;
    ResourceType type;

    Content(std::string _sourceFile, 
            ResourceType _type): sourceFile(_sourceFile), type(_type) {};
    void accept(Visitor* visitor) override { visitor->visit(*this); };
};

class Decoration: public Element
{
    Content content;
    DecorationKind kind; 

    void accept(Visitor* visitor) override { visitor->visit(*this); };
};

class Document
{
private:
    std::string mFileName,
                mLocalPath,
                mReusablePath,
                mAssetPath;
protected:
    std::shared_ptr<Info> info;
    std::shared_ptr<Typesetter> typesetter;

    void parseInfoSection(YAML::Node doc);
    void parseTypesetterSection(YAML::Node doc);
public:
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

    Info* getInfo() const { return info.get(); };
    Typesetter* getTypesetter() const { return typesetter.get(); }

    void parse();
    void parse(std::string fileName);
    void print(Visitor& printer);
};

class ConsolePrinter: public Visitor
{
    void visit(Info& info) override;
    void visit(Typesetter& typesetter) override;
    void visit(Content& content) override;
    void visit(Decoration& decoration) override;
};

}
// end namespace DOC

#endif