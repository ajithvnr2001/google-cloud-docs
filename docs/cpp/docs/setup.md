---
url: https://docs.cloud.google.com/cpp/docs/setup/
title: Setting up a C++ development environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:16.152057+00:00
---

# Setting up a C++ development environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Guides ](https://docs.cloud.google.com/cpp/docs/setup)



Send feedback 

#  Setting up a C++ development environment Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to prepare your local machine for [C++](https://isocpp.org/) development, including developing C++ apps that run on Google Cloud.

If you already have a development environment set up, see [C++ and Google Cloud](https://docs.cloud.google.com/cpp) to get an overview of how to run C++ apps on Google Cloud.

## Objectives

  * Install a [supported version of C++](https://docs.cloud.google.com/cpp/docs/supported-cpp-versions) compatible with Google Cloud.
  * Install a C++ build system.
  * Install an editor (optional).
  * Install the Google Cloud CLI (optional).
  * Install the Cloud Client Libraries for C++ (optional).
  * Set up authentication.



## Installing C++

C++'s installation instructions vary by operating system. Follow the guide for the operating system you're running in your development environment, macOS, Windows, or Linux.

### macOS

  1. You can get a C++ compiler by installing [Xcode's command-line tools](https://developer.apple.com/library/content/technotes/tn2339/_index.html).
         
         xcode-select --install
         

  2. After the installation is complete, verify that your compiler is available as `c++`:
         
         c++ --version
         




### Windows

  1. To install a C++ compiler in a Windows environment, download the Microsoft's "Visual Studio" from the [Visual Studio website](https://visualstudio.microsoft.com/vs/features/cplusplus/). This will download a full IDE, including an editor, debugger and build systems.

  2. To access your C++ compiler follow the C++ section in Visual Studio's [Getting Started](https://visualstudio.microsoft.com/vs/getting-started/) guide.




### Linux

Most (if not all) Linux distributions include [GCC](https://gcc.gnu.org/) as their primary C++ compiler. Many Linux distributions also include [CLang](https://clang.llvm.org/) as an alternative C++ compiler. The C++ client libraries support both.

  1. To install C++ in a Linux environment, install the appropriate packages for your distribution. For Debian and Ubuntu, this package is [g++](https://packages.debian.org/stable/devel/g++).

Install these packages using the following commands:
         
         sudo apt update
         sudo apt install g++
         

  2. After the installations are complete, verify that you have `g++` installed:
         
         g++ --version
         




## Install a C++ Build System compatible with Google Cloud

To use C++ effectively you will want a build system and package manager that supports the Cloud Client Libraries for C++. The client libraries support multiple such build systems and package managers.

### CMake with vcpkg

  1. Your operating system may provide packages for [CMake](https://cmake.org/) installed. If it does not, install it from the [CMake download page](https://cmake.org/download/)

  2. To install vcpkg, see [Get Started with vcpkg](https://vcpkg.io/en/getting-started.html)




### CMake with Conda

  1. Your operating system may provide packages for [CMake](https://cmake.org/) installed. If it does not, install it from the [CMake download page](https://cmake.org/download/)

  2. To install Conda, see the [Installation section](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) in Conda's User Guide.




### Bazel

  1. To install Bazel, see [Installing Bazel](https://bazel.build/install)



### Other

If you need to use a different build system or package manager the C++ client libraries repository include instructions to [build from source](https://github.com/googleapis/google-cloud-cpp/blob/main/doc/packaging.md).

## Install an editor

There are many [editors and IDEs](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments#C/C++) with C++ support. Pick one that fits your needs. Consider these features as you make your selection:

  * Fully integrated debugging capabilities
  * Syntax highlighting
  * Code completion



## Install the Google Cloud CLI

The [Google Cloud CLI](https://docs.cloud.google.com/sdk) is a set of tools for Google Cloud. It contains the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud) and [`bq`](https://docs.cloud.google.com/bigquery/docs/bq-command-line-tool) command-line tools used to access Compute Engine, Cloud Storage, BigQuery, and other services from the command line. You can run these tools interactively or in your automated scripts.

## Install the Cloud Client Libraries for C++

The [Cloud Client Libraries for C++](https://github.com/googleapis/google-cloud-cpp/) is the idiomatic way for C++ developers to integrate with Google Cloud services, such as Spanner and Cloud Storage. 

For example, to install the package for an individual API, such as the Cloud Storage API, do the following:

### CMake with vcpkg

  1. Add `google-cloud-cpp` as dependency to your `vcpkg.json` file:
         
         {
             "name": "setup-cpp-vcpkg",
             "version-string": "unversioned",
             "description": "Setting up C++ for Google Cloud with CMake and vcpkg",
             "dependencies": [
                 {"name": "google-cloud-cpp", "default-features": false, "features": ["storage"]}
             ]
         }
         

  2. Edit your `CMakeLists.txt` file to require the library
         
         find_package(google_cloud_cpp_storage REQUIRED)

  3. Add this dependency to your targets
         
         target_link_libraries(hello_world PUBLIC google-cloud-cpp::storage)

  4. Configure CMake using the vcpkg toolchain. This will automatically download, and compile `google-cloud-cpp` and its dependencies.
         
         cmake -S . -B [build directory] \
             -DCMAKE_TOOLCHAIN_FILE=[vcpkg location]/scripts/buildsystems/vcpkg.cmake
         




### CMake with Conda

  1. Install the dependencies using Conda:
         
         conda config --add channels conda-forge
         conda config --set channel_priority strict
         conda install -y -c conda-forge cmake ninja cxx-compiler google-cloud-cpp libgoogle-cloud

  2. Edit your `CMakeLists.txt` file to require the library
         
         find_package(google_cloud_cpp_storage REQUIRED)

  3. Add this dependency to your targets
         
         target_link_libraries(hello_world PUBLIC google-cloud-cpp::storage)

  4. Configure CMake within your Conda environment..
         
         cmake -S . -B [build directory]
         




### Bazel

  1. In your `WORKSPACE` file add the follow command to download the Cloud Client Libraries for C++ source code:
         
         load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
         
         http_archive(
             name = "google_cloud_cpp",
             sha256 = "db69dd73ef4af8b2e816d80ded04950036d0e0dccc274f8c3d3ed1d7f5692a1b",
             strip_prefix = "google-cloud-cpp-2.32.0",
             url = "https://github.com/googleapis/google-cloud-cpp/archive/v2.32.0.tar.gz",
         )

  2. In your `WORKSPACE` file call the Starlark functions to load recursive dependencies:
         
         load("@google_cloud_cpp//bazel:workspace0.bzl", "gl_cpp_workspace0")
         
         gl_cpp_workspace0()
         
         load("@google_cloud_cpp//bazel:workspace1.bzl", "gl_cpp_workspace1")
         
         gl_cpp_workspace1()
         
         load("@google_cloud_cpp//bazel:workspace2.bzl", "gl_cpp_workspace2")
         
         gl_cpp_workspace2()
         
         load("@google_cloud_cpp//bazel:workspace3.bzl", "gl_cpp_workspace3")
         
         gl_cpp_workspace3()
         
         load("@google_cloud_cpp//bazel:workspace4.bzl", "gl_cpp_workspace4")
         
         gl_cpp_workspace4()
         
         load("@google_cloud_cpp//bazel:workspace5.bzl", "gl_cpp_workspace5")
         
         gl_cpp_workspace5()

  3. In your `BUILD` file use the Cloud Storage library:
         
         cc_binary(
             name = "hello_world",
             srcs = ["hello_world.cc"],
             deps = ["@google_cloud_cpp//:storage"],
         )




## Set up authentication

To use the Cloud Client Libraries in a local development environment, set up Application Default Credentials.

If you're using a local shell, then create local authentication credentials for your user account: 
    
    
    gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

## What's next

  * Get more information about [authentication](https://docs.cloud.google.com/docs/authentication).
  * Learn more about [C++ on Google Cloud](https://docs.cloud.google.com/cpp).
  * Browse the [documentation for Google Cloud products](https://cloud.google.com/products).
  * Clone the [C++ samples repository from GitHub](https://github.com/GoogleCloudPlatform/cpp-samples).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
