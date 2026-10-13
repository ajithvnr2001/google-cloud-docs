---
url: https://docs.cloud.google.com/transcoder/docs/reference/libraries/
title: Transcoder API client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:59.593225+00:00
---

# Transcoder API client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/reference/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Reference ](https://docs.cloud.google.com/transcoder/docs/apis)



Send feedback 

#  Transcoder API client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Transcoder API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## Install the client library

### C++

See [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup) for details about this client library's requirements and install dependencies.

### C#

If you are using Visual Studio 2017 or higher, open nuget package manager window and type the following: 
    
    
    Install-Package Google.Cloud.Video.Transcoder.V1 -Version 2.9.0

If you are using .NET Core command-line interface tools to install your dependencies, run the following command:
    
    
    dotnet add package Google.Cloud.Video.Transcoder.V1 --version 2.9.0

For more information, see [Setting Up a C# Development Environment](https://docs.cloud.google.com/dotnet/docs/setup).

### Go
    
    
    go get cloud.google.com/go/video/transcoder/apiv1

For more information, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

### Java

If you are using Maven, add this to your pom.xml file: 
    
    
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-video-transcoder</artifactId>
        <version>1.51.0</version>
    </dependency>

If you are using Gradle, add this to your dependencies:
    
    
    compile group: 'com.google.cloud', name: 'google-cloud-video-transcoder', version: '1.51.0'

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    npm i @google-cloud/video-transcoder

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### PHP
    
    
    composer require google/cloud

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

### Python
    
    
    pip install --upgrade google-cloud-video-transcoder

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

### Ruby
    
    
    gem install google-cloud-video-transcoder

For more information, see [Setting Up a Ruby Development Environment](https://docs.cloud.google.com/ruby/docs/setup).

## Set up authentication

To authenticate calls to Google Cloud APIs, client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

For production environments, the way you set up ADC depends on the service and context. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

For a local development environment, you can set up ADC with the credentials that are associated with your Google Account:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




## Additional resources

### C++

The following list contains links to more resources related to the client library for C++:

  * [API reference](https://docs.cloud.google.com/cpp/docs/reference/video/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [`google-cloud-transcoder` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-transcoder%5D%5Bc%2B%2B%5D)
  * [Source code](https://github.com/googleapis/google-cloud-cpp)



### C#

The following list contains links to more resources related to the client library for C#:

  * [API reference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues)
  * [`google-cloud-transcoder` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-transcoder%5D+%5Bc%23%5D)
  * [Source code](https://github.com/googleapis/google-cloud-dotnet)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://pkg.go.dev/cloud.google.com/go/video/transcoder)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * [`google-cloud-transcoder` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-transcoder%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-java/issues)
  * [`google-cloud-transcoder` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-transcoder%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/google-cloud-java)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://cloud.google.com/nodejs/docs/reference/video-transcoder/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-node/issues)
  * [`google-cloud-transcoder` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-transcoder%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/googleapis/google-cloud-node)



### PHP

The following list contains links to more resources related to the client library for PHP:

  * [API reference](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-php/issues)
  * [`google-cloud-transcoder` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-transcoder%5D+%5Bphp%5D)
  * [Source code](https://github.com/googleapis/google-cloud-php)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://pypi.org/project/google-cloud-video-transcoder)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/python-video-transcoder/issues)
  * [`google-cloud-transcoder` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-transcoder%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/python-video-transcoder)



### Ruby

The following list contains links to more resources related to the client library for Ruby:

  * [API reference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues)
  * [`google-cloud-transcoder` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-transcoder%5D+%5Bruby%5D)
  * [Source code](https://github.com/googleapis/google-cloud-ruby)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
