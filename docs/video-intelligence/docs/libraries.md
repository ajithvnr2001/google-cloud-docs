---
url: https://docs.cloud.google.com/video-intelligence/docs/libraries/
title: Client libraries \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:38.926419+00:00
---

# Client libraries  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/libraries/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Reference ](https://docs.cloud.google.com/video-intelligence/docs/apis)



Send feedback 

#  Client libraries Stay organized with collections  Save and categorize content based on your preferences. 

While you can use Video Intelligence by making direct requests, we provide client libraries for several popular languages. Video Intelligence client libraries are built on [Google Cloud Client Libraries](https://cloud.google.com/apis/docs/cloud-client-libraries). This common infrastructure provides functionality for API-specific library implementations, but it also provides types and methods that you may use directly when using any Cloud API. 

## Available client libraries

Video Intelligence provides client libraries and guides for the following languages: 

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

This page provides reference documentation and related resources for the Video Intelligence Python client library. 

Resource | Description  
---|---  
[Library reference](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest) | Video Intelligence Python library reference  
[Language guide](https://cloud.google.com/python/docs/) | General guide for using Python with GCP  
[GitHub repository](https://github.com/googleapis/python-videointelligence) | Source code and additional documentation for this library  
[Quickstart](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-client-libraries) | Introduction to using this library  
[Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-video%5D+%5Bpython%5D) | Questions tagged with Video Intelligence and Python  
  
### Installation

To install the client library: 
    
    
    pip install --upgrade google-cloud-videointelligence

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

This page provides reference documentation and related resources for the Video Intelligence Java client library. 

Resource | Description  
---|---  
[Library reference](https://cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/overview) | Video Intelligence Java library reference  
[Language guide](https://cloud.google.com/java/docs/) | General guide for using Java with GCP  
[GitHub repository](https://github.com/googleapis/java-video-intelligence) | Source code and additional documentation for this library  
[Quickstart](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-client-libraries) | Introduction to using this library  
[Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-video%5D+%5Bjava%5D) | Questions tagged with Video Intelligence and Java  
  
### Installation

To install the client library: 

If you are using [Maven](https://maven.apache.org/), add the following to your `pom.xml` file. For more information about BOMs, see [The Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.90.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-video-intelligence</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-video-intelligence'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-video-intelligence" % "2.98.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

This page provides reference documentation and related resources for the Video Intelligence Node.js client library. 

Resource | Description  
---|---  
[Library reference](https://googleapis.dev/nodejs/video/latest/index.html) | Video Intelligence Node.js library reference  
[Language guide](https://cloud.google.com/nodejs/docs/) | General guide for using Node.js with GCP  
[GitHub repository](https://github.com/googleapis/nodejs-video-intelligence/) | Source code and additional documentation for this library  
[Quickstart](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-client-libraries) | Introduction to using this library  
[Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-video%5D+%5Bnode.js%5D) | Questions tagged with Video Intelligence and Node.js  
  
### Installation

To install the client library: 

For more information, see [Setting Up a Node.js Development Environment](https://cloud.google.com/nodejs/docs/setup). 
    
    
    npm install @google-cloud/video-intelligence

### C++

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

This page provides reference documentation and related resources for the Video Intelligence C++ client library. 

Resource | Description  
---|---  
[Library reference](https://docs.cloud.google.com/cpp/docs/reference/videointelligence/latest) | Video Intelligence C++ library reference  
[Language guide](https://cloud.google.com/cpp/) | General guide for using C++ with GCP  
[GitHub repository](https://github.com/googleapis/google-cloud-cpp) | Source code and additional documentation for this library  
[Quickstart](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-client-libraries) | Introduction to using this library  
[Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-video%5D+%5Bcpp%5D) | Questions tagged with Video Intelligence and C++  
  
### Installation

To install the client library: 

For more information, see [Setting Up a C++ Development Environment](https://docs.cloud.google.com/cpp/docs/setup). 

### Go

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

This page provides reference documentation and related resources for the Video Intelligence Go client library. 

Resource | Description  
---|---  
[Library reference](https://godoc.org/cloud.google.com/go/videointelligence/apiv1) | Video Intelligence Go library reference  
[Language guide](https://cloud.google.com/go/docs/) | General guide for using Go with GCP  
[GitHub repository](https://github.com/googleapis/google-cloud-go) | Source code and additional documentation for this library  
[Quickstart](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-client-libraries) | Introduction to using this library  
[Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-video%5D+%5Bgo%5D) | Questions tagged with Video Intelligence and Go  
  
### Installation

To install the client library: 

For more information, see [Setting Up a Go Development Environment](https://cloud.google.com/go/docs/setup). 
    
    
    go get cloud.google.com/go/videointelligence/apiv1

### PHP

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

This page provides reference documentation and related resources for the Video Intelligence PHP client library. 

Resource | Description  
---|---  
[Library reference](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.153.0/videointelligence/readme) | Video Intelligence PHP library reference  
[Language guide](https://cloud.google.com/php/docs/) | General guide for using PHP with GCP  
[GitHub repository](https://github.com/googleapis/google-cloud-php/tree/master/VideoIntelligence) | Source code and additional documentation for this library  
[Quickstart](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-client-libraries) | Introduction to using this library  
[Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-video%5D+%5Bphp%5D) | Questions tagged with Video Intelligence and PHP  
  
### Installation

To install the client library: 
    
    
    composer require google/cloud-videointelligence

### Ruby

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

The Ruby client libraries for Video Intelligence are currently released as Beta.

This page provides reference documentation and related resources for the Video Intelligence Ruby client library. 

Resource | Description  
---|---  
[Library reference](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence.html) | Video Intelligence Ruby library reference  
[Language guide](https://cloud.google.com/ruby/docs/) | General guide for using Ruby with GCP  
[GitHub repository](https://github.com/googleapis/google-cloud-ruby/tree/master/google-cloud-video_intelligence) | Source code and additional documentation for this library  
[Quickstart](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-client-libraries) | Introduction to using this library  
[Stack Overflow](http://stackoverflow.com/search?q=%5Bgoogle-cloud-video%5D+%5Bruby%5D) | Questions tagged with Video Intelligence and Ruby  
  
### Installation

To install the client library: 

For more information, see [Setting Up a Ruby Development Environment](https://cloud.google.com/ruby/docs/setup). 
    
    
    gem install google-cloud-video_intelligence

## Authentication and access control

The Video Intelligence quickstart guides provide basic information on authentication and access control. For more detailed information, see the following: 

  * [Authentication methods](https://docs.cloud.google.com/docs/authentication)
  * [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
