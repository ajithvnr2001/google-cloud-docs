---
url: https://docs.cloud.google.com/memorystore/docs/redis/libraries/
title: Set up client libraries \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:45.255985+00:00
---

# Set up client libraries  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  Set up client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to install client libraries for the Memorystore for Redis API so you can connect to the API with the language of your choice.

## Installing the client library

### C++

See [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup) for details about this client library's requirements and install dependencies.

### C#

Install the Google.Cloud.Redis.V1 package in Visual Studio 

### Go
    
    
    go get cloud.google.com/go/redis/apiv1

### Java

If you are using Maven, add this to your pom.xml file: 
    
    
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-redis</artifactId>
        <version>0.62.0-alpha</version>
    </dependency>

If you are using Gradle, add this to your dependencies:
    
    
    compile 'com.google.cloud:google-cloud-redis:0.62.0-alpha'

If you are using SBT, add this to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-redis" % "0.62.0-alpha"

If you're using VS Code, IntelliJ, or Eclipse, you can add client libraries to your project using these IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/intellij/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/vscode/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

### Node.js
    
    
    npm install @google-cloud/redis

### PHP
    
    
    composer require google/cloud-redis

### Python

For more on setting up your Python development environment, refer to [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup). 
    
    
    pip install --upgrade google-cloud-redis

### Ruby
    
    
    gem install google-cloud-redis

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

  * [API Reference Documentation](https://docs.cloud.google.com/cpp/docs/reference/redis/latest)
  * [Source Code](https://github.com/googleapis/google-cloud-cpp)
  * [GitHub Issue Tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D%5Bc%2B%2B%5D)



### C#

  * [API Reference Documentation](http://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Redis.V1/#googlecloudredisv1)
  * [Source Code](https://github.com/googleapis/google-cloud-dotnet/tree/master/apis/Google.Cloud.Redis.V1)
  * [GitHub Issue Tracker](https://github.com/googleapis/google-cloud-dotnet/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bc%23%5D)



### Go

  * [API Reference Documentation](https://godoc.org/cloud.google.com/go/redis/apiv1)
  * [Source Code](https://github.com/GoogleCloudPlatform/google-cloud-go/tree/master/redis/apiv1)
  * [GitHub Issue Tracker](https://github.com/GoogleCloudPlatform/google-cloud-go/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bgo%5D)



### Java

  * [API Reference Documentation](https://cloud.google.com/java/docs/reference/google-cloud-redis/latest/overview)
  * [Source Code](https://github.com/googleapis/google-cloud-java/tree/main/java-redis)
  * [GitHub Issue Tracker](https://github.com/googleapis/google-cloud-java/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bjava%5D)



### Node.js

  * [API Reference Documentation](https://googleapis.dev/nodejs/redis/latest)
  * [Source Code](https://github.com/googleapis/nodejs-redis)
  * [GitHub Issue Tracker](https://github.com/googleapis/nodejs-redis/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bnode.js%5D)



### PHP

  * [API Reference Documentation](https://docs.cloud.google.com/php/docs/reference/cloud-redis/latest)
  * [Source Code](https://github.com/GoogleCloudPlatform/google-cloud-php/tree/master/Redis)
  * [GitHub Issue Tracker](https://github.com/GoogleCloudPlatform/google-cloud-php/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bphp%5D)



### Python

  * [API Reference Documentation](https://docs.cloud.google.com/python/docs/reference/redis/latest)
  * [Source Code](https://github.com/googleapis/python-redis)
  * [GitHub Issue Tracker](https://github.com/GoogleCloudPlatform/google-cloud-python/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bpython%5D)



### Ruby

  * [API Reference Documentation](https://googleapis.dev/ruby/google-cloud-redis/latest/Google/Cloud/Redis/V1.html)
  * [Source Code](https://github.com/GoogleCloudPlatform/google-cloud-ruby)
  * [GitHub Issue Tracker](https://github.com/GoogleCloudPlatform/google-cloud-ruby/issues)
  * [Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-memorystore%5D+%5Bruby%5D)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
