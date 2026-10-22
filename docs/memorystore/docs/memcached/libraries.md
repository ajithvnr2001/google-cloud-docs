---
url: https://docs.cloud.google.com/memorystore/docs/memcached/libraries/
title: Set up client libraries \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:28.570299+00:00
---

# Set up client libraries  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/libraries/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/memcached/apis)



Send feedback 

#  Set up client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to install client libraries for the Memorystore for Memcached API so you can connect to the API with the language of your choice.

## Installing the client library

### C++

See [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup) for details about this client library's requirements and install dependencies.

### C#

Install the `Google.Cloud.Memcache.V1` package in Visual Studio. See the Google Cloud .NET Memcached [Installation](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Memcache.V1/index.html#installation) documentation for more details. 

### Go
    
    
    go get cloud.google.com/go/memcache/apiv1

### Java

If you are using Maven with BOM, add this to your pom.xml file
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>20.8.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
     
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-memcache</artifactId>
      </dependency>

If you are using Maven without BOM, add this to your dependencies:
    
    
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-memcache</artifactId>
      <version>0.2.1</version>
    </dependency>

If you are using Gradle, add this to your dependencies:
    
    
      compile 'com.google.cloud:google-cloud-memcache:0.2.1'

If you are using SBT, add this to your dependencies:
    
    
      libraryDependencies += "com.google.cloud" % "google-cloud-memcache" % "0.2.1"

### Node.js
    
    
    npm install @google-cloud/memcache

### Python

For more on setting up your Python development environment, refer to [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup). Mac/Linux 
    
    
    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-memcache

Windows 
    
    
    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-memcache

## Setting up authentication

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




## Additional Resources

### C++

  * [API Reference Documentation](https://docs.cloud.google.com/cpp/docs/reference/memcache/latest)
  * [Source Code](https://github.com/googleapis/google-cloud-cpp)
  * [GitHub Issue Tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D%5Bc%2B%2B%5D)



### C#

  * [API Reference Documentation](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Memcache.V1/index.html)
  * [Source Code](https://github.com/googleapis/google-cloud-dotnet/tree/master/apis/Google.Cloud.Memcache.V1)
  * [GitHub Issue Tracker](https://github.com/googleapis/google-cloud-dotnet/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bc%23%5D)



### Go

  * [API Reference Documentation](https://pkg.go.dev/cloud.google.com/go/memcache/apiv1?tab=doc)
  * [Source Code](https://github.com/googleapis/google-cloud-go/tree/master/memcache/apiv1)
  * [GitHub Issue Tracker](https://github.com/GoogleCloudPlatform/google-cloud-go/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bgo%5D)



### Java

  * [API Reference Documentation](https://cloud.google.com/java/docs/reference/google-cloud-memcache/latest/overview)
  * [Source Code](https://github.com/googleapis/java-memcache)
  * [GitHub Issue Tracker](https://github.com/googleapis/google-cloud-java/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bjava%5D)



### Node.js

  * [API Reference Documentation](https://googleapis.dev/nodejs/memcache/latest/index.html)
  * [Source Code](https://github.com/googleapis/nodejs-memcache)
  * [GitHub Issue Tracker](https://github.com/googleapis/nodejs-memcache/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bnode.js%5D)



### Python

  * [API Reference Documentation](https://pypi.org/project/google-cloud-memcache/)
  * [Source Code](https://github.com/googleapis/python-memcache/)
  * [GitHub Issue Tracker](https://github.com/GoogleCloudPlatform/google-cloud-python/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bpython%5D)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
