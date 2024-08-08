cmake_minimum_required(VERSION 3.10)
project(texgen)
find_package(yaml-cpp CONFIG REQUIRED)
find_package(inja CONFIG REQUIRED)

add_executable(${PROJECT_NAME} main.cpp document.cpp)
target_link_libraries(${PROJECT_NAME}
                      PUBLIC    yaml-cpp::yaml-cpp
                      PRIVATE   pantor::inja)