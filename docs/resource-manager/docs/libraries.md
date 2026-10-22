---
url: https://docs.cloud.google.com/resource-manager/docs/libraries/
title: Install client libraries \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:12.351919+00:00
---

# Install client libraries  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Install client libraries Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Resource Manager API is built on HTTP and JSON, so any standard HTTP client can send requests to it and parse the responses.

However, the Google API client libraries provide better language integration, improved security, and support for making calls that require user authorization. The client libraries are available in a number of programming languages; by using them you can avoid the need to manually set up HTTP requests and parse the responses.

To get started, select the programming language that you are using for development.

### Go

Get the latest [Cloud Resource Manager API client library for Go](https://github.com/google/google-api-go-client). Read the client library's [developer's guide](https://github.com/google/google-api-go-client).

### Java

This page contains information about getting started with the Cloud Resource Manager API by using the Google API Client Library for Java. For more information, see the following documentation:

  * Browse the [Javadoc reference for the Cloud Resource Manager API](https://googleapis.dev/java/google-api-services-cloudresourcemanager/latest/).
  * Read the [Developer's Guide for the Google API Client Library for Java](https://github.com/googleapis/google-api-java-client/).



## Add the client library to your project

Select your build environment (Maven or Gradle) from the following tabs:

Maven

Add the following to your `pom.xml` file:

See [all versions available on the Maven Central Repository](http://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22com.google.apis%22%20AND%20a%3A%22google-api-services-cloudresourcemanager%22).

Gradle

Add the following to your `build.gradle` file:

See [all versions available on the Maven Central Repository](http://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22com.google.apis%22%20AND%20a%3A%22google-api-services-cloudresourcemanager%22).

### JavaScript

Read the client library's [developer's guide](https://docs.cloud.google.com/api-client-library/javascript/start/start-js).

### .NET

This page contains information about getting started with the Cloud Resource Manager API by using the Google API Client Library for .NET. For more information, see the following documentation:

  * Browse the [.NET reference documentation for the Cloud Resource Manager API](https://googleapis.dev/dotnet/Google.Apis/latest/api/Google.Apis.html).
  * Read the [Developer's guide for the Google API Client Library for .NET](https://docs.cloud.google.com/api-client-library/dotnet/get_started).



## Downloading the library

Install the NuGet package: [Google.Apis](https://www.nuget.org/packages/Google.Apis).

### Node.js

Get the latest [Cloud Resource Manager API client library for Node.js](https://github.com/google/google-api-nodejs-client/). Read the client library's [developer's guide](https://github.com/google/google-api-nodejs-client/).

### Obj-C

Get the latest [Cloud Resource Manager API client library for Objective-C](https://github.com/google/google-api-objectivec-client-for-rest). Read the client library's [developer's guide](https://github.com/google/google-api-objectivec-client-for-rest/wiki).

### PHP

Get the latest [Cloud Resource Manager API client library for PHP](https://github.com/google/google-api-php-client). Read the client library's [developer's guide](https://docs.cloud.google.com/api-client-library/php).

### Python

This page contains information about getting started with the Cloud Resource Manager API by using the Google API Client Library for Python (v1/v2). For more information, see the following documentation:

  * Browse the [PyDoc reference for the Cloud Resource Manager API](https://googleapis.github.io/google-api-python-client/docs/dyn/cloudresourcemanager_v1.html).
  * Read the [Developer's guide for the Google API Client Library for Python (v1/v2)](https://docs.cloud.google.com/api-client-library/python).



## System requirements

  * Operating systems: 
    * Linux
    * macOS X
    * Windows
  * [The v1 client library requires Python 2.7 or higher. The v2 client library requires 3.7 or higher.](http://python.org/download/)



## Install the client library

You can either use a package manager or manually download and install the Python client library:

### Managed install

Use pip or setuptools to manage your installation. You might need to run `sudo` first.

  * [pip](http://pypi.python.org/pypi/pip) (preferred): 
        
        pip install --upgrade google-api-python-client

  * [Setuptools](http://pypi.python.org/pypi/setuptools): 
        
        easy_install --upgrade google-api-python-client




### Manual install

  1. [Download the latest client library for Python](https://pypi.python.org/pypi/google-api-python-client/).
  2. Unpack the code.
  3. Install: 
         
         python setup.py install




### App Engine

Because the Python client libraries aren't installed in the [App Engine Python runtime environment](https://cloud.google.com/appengine/docs/python/), you must [ copy them into your application](https://cloud.google.com/appengine/docs/python/tools/libraries27#vendoring) just like third-party libraries.

### Ruby

This page contains information about getting started with the Cloud Resource Manager API by using the Google API Client Library for Ruby. For more information, see the following documentation:

  * Read the [Get started guide for the Google API Client Library for Ruby](https://docs.cloud.google.com/api-client-library/ruby/start/get_started).



## Install the `google-api-client` gem

Depending on your system, you might need to prepend these commands with `sudo`. 

If you haven't installed the Google API Client Library for Ruby before, install by using `RubyGems`: 
    
    
    gem install google-api-client

If you already have the gem installed, update to the latest version: 
    
    
    gem update -y google-api-client

## Get started with the Google API Client Library for Ruby

To learn how to make your first request, see the [Get started guide](https://docs.cloud.google.com/api-client-library/ruby/start/get_started). 

## Available Cloud Resource Manager API versions

The table below lists the versions of the Cloud Resource Manager API that are available. Resource Manager API methods are split between each of the versions listed below. You can try out the methods available in each version from right within your browser by using the APIs Explorer.

Version | Access method | Description  
---|---|---  
v1 | [APIs Explorer](https://developers.google.com/apis-explorer/#p/cloudresourcemanager/v1/) | The v1 Resource Manager API contains methods related to managing projects and organizations.  
v1beta1 | [APIs Explorer](https://developers.google.com/apis-explorer/#p/cloudresourcemanager/v1beta1/) | The v1beta1 Resource Manager API contains experimental versions of the v1 API methods.  
v2 | [APIs Explorer](https://developers.google.com/apis-explorer/#p/cloudresourcemanager/v2/) | The v2 Resource Manager API contains methods related to managing folders.  
v2beta1 | [APIs Explorer](https://developers.google.com/apis-explorer/#p/cloudresourcemanager/v2beta1/) | The v2beta1 Resource Manager API contains experimental versions of the v2 API methods.  
v3 | [APIs Explorer](https://developers.google.com/apis-explorer/#p/cloudresourcemanager/v3/) | The v3 Resource Manager API contains methods related to managing projects, folders, organizations, liens, and tags.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
