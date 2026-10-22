---
url: https://docs.cloud.google.com/model-armor/reference/libraries/
title: Model Armor API client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:29:18.499010+00:00
---

# Model Armor API client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/reference/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Reference ](https://docs.cloud.google.com/model-armor/reference/libraries)



Send feedback 

#  Model Armor API client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Model Armor API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## Install the client library

### C#

Install the client library by using one of the following options: 

  * NuGet in Visual Studio Code: 
    1. Enable pre-release packages. For more information, see [Include prerelease package versions](https://code.visualstudio.com/docs/csharp/package-management#_include-prerelease-package-versions) in the Visual Studio Code documentation. 
    2. Add the `Google.Cloud.ModelArmor.V1` package. For more information, see [Add a package](https://code.visualstudio.com/docs/csharp/package-management#_add-a-package) in the Visual Studio Code documentation. 
  * NuGet in Visual Studio: For more information, see [Installation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest#installation). 
  * .NET CLI: 
        
        dotnet add package Google.Cloud.ModelArmor.V1 --version 1.0.0-beta05




For more information, see [Setting Up a C# Development Environment](https://docs.cloud.google.com/dotnet/docs/setup).

### Go
    
    
    go get cloud.google.com/go/modelarmor

For more information, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

### Java

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
        <artifactId>google-cloud-modelarmor</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-modelarmor'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-modelarmor" % "0.40.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    npm install @google-cloud/modelarmor

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### PHP
    
    
    composer require google/cloud-modelarmor

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

### Python
    
    
    pip install --upgrade google-cloud-modelarmor

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

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

### C#

The following list contains links to more resources related to the client library for C#:

  * [API reference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues)
  * [`google-model-armor` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-model-armor%5D+%5Bc%23%5D)
  * [Source code](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/main/modelarmor)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * [`google-model-armor` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-model-armor%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go/tree/main/modelarmor)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/overview)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-java/tree/main/java-modelarmor/issues)
  * [`google-model-armor` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-model-armor%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/google-cloud-java/tree/main/java-modelarmor)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://docs.cloud.google.com/nodejs/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-node/issues)
  * [`google-model-armor` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-model-armor%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-modelarmor)



### PHP

The following list contains links to more resources related to the client library for PHP:

  * [API reference](https://docs.cloud.google.com/php/docs/reference/cloud-modelarmor/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-php/issues)
  * [`google-model-armor` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-model-armor%5D+%5Bphp%5D)
  * [Source code](https://github.com/googleapis/google-cloud-php/tree/main/packages/google-cloud-modelarmor)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-python/issues)
  * [`google-model-armor` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-model-armor%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-modelarmor)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
