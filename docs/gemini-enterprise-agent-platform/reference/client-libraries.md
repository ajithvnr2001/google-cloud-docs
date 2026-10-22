---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/client-libraries/
title: Install the Gemini Enterprise Agent Platform client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:45:08.740325+00:00
---

# Install the Gemini Enterprise Agent Platform client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/client-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)



Send feedback 

#  Install the Gemini Enterprise Agent Platform client libraries Stay organized with collections  Save and categorize content based on your preferences. 

Client libraries provide an optimized developer experience for calling the Agent Platform API. The client libraries use each supported language's natural conventions and reduce boilerplate code that you have to write. The following guide explains how to install the libraries and set up authentication for using them in a local development environment.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. Enable the Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  6. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




## Client libraries

Agent Platform provides client libraries for the following languages. Select the language that you want to use.

### C#

Run the following command to add the `Google.Cloud.AIPlatform.V1` package reference to your project file:
    
    
    dotnet add package Google.Cloud.AIPlatform.V1
    

### Try code samples

To view or get individual code samples, go to the [dotnet-aiplatform](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/tree/main/aiplatform/api) GitHub repository.

### Client library documentation

For more information, view the [Agent Platform .NET client library documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest).

### Java

If you are using Maven, add the following to your dependencies:
    
    
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-aiplatform</artifactId>
      <version>3.35.0</version>
    </dependency>
    

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    compile 'com.google.cloud:google-cloud-aiplatform:3.35.0'
    

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-aiplatform" % "3.35.0"
    

### Try code samples

To view or get individual code samples, go to the [java-aiplatform](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/main/aiplatform/src/main/java/aiplatform) GitHub repository.

### Client library documentation

For more information, view the [Agent Platform client library for Java documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/overview).

### Node.js

Before installing the library, prepare your environment for [Node.js development](https://docs.cloud.google.com/nodejs/docs/setup).

Run the following command in your environment to install the client library:
    
    
    npm install @google-cloud/aiplatform
    

### Client library documentation

For more information, view the [Agent Platform client library for Node.js documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest).

### Python

The Gemini Enterprise Agent Platform Python client library is installed when you install the Vertex AI SDK for Python.

For more information, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/install-sdk).

### Go

Before installing the library, [prepare your environment for Go development](https://docs.cloud.google.com/go/docs/setup).

### Review available packages

Review the available Gemini Enterprise Agent Platform API Go packages to determine which package best meets your project's needs:

  * Package [**cloud.google.com/go/vertexai**](https://pkg.go.dev/cloud.google.com/go/vertexai) (**recommended**)

`vertexai` is a human authored package that provides access to common capabilities and features.

This package is recommended as the starting point for most developers building with the Gemini Enterprise Agent Platform API. To access capabilities and features not yet covered by this package, use the auto-generated `aiplatform` instead.

  * Package [**cloud.google.com/go/aiplatform**](https://pkg.go.dev/cloud.google.com/go/aiplatform)

`aiplatform` is an auto-generated package.

This package is intended for projects that require access to Gemini Enterprise Agent Platform API capabilities and features not yet provided by the human authored `vertexai` package.




### Installation

  * Package [**cloud.google.com/go/vertexai**](https://pkg.go.dev/cloud.google.com/go/vertexai) (**recommended**)

Run the following command to install this package in your environment:
        
        go get cloud.google.com/go/vertexai
        

  * Package [**cloud.google.com/go/aiplatform**](https://pkg.go.dev/cloud.google.com/go/aiplatform)

Run the following command to install this package in your environment:
        
        go get cloud.google.com/go/aiplatform
        




### Samples

  * Package [**cloud.google.com/go/vertexai**](https://pkg.go.dev/cloud.google.com/go/vertexai) (**recommended**)

Samples for using this package are available, in the `golang-samples` GitHub repository in the top-level `vertexai` directory:

[github.com/GoogleCloudPlatform/golang-samples](https://github.com/GoogleCloudPlatform/golang-samples/) > [vertexai](https://github.com/GoogleCloudPlatform/golang-samples/tree/main/vertexai)

  * Package [**cloud.google.com/go/aiplatform**](https://pkg.go.dev/cloud.google.com/go/aiplatform)

Samples for using this package are available, in the `golang-samples` GitHub repository in the top-level `aiplatform` directory:

[github.com/GoogleCloudPlatform/golang-samples](https://github.com/GoogleCloudPlatform/golang-samples/) > [aiplatform](https://github.com/GoogleCloudPlatform/golang-samples/tree/main/aiplatform)




### Client library documentation

For more information about the library, see the Agent Platform client library for Go documentation:

  * Package [**cloud.google.com/go/vertexai**](https://pkg.go.dev/cloud.google.com/go/vertexai) (**recommended**)

    * Gemini Enterprise Agent Platform `cloud.google.com/go/vertexai` [API reference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vertexai/latest)
  * Package [**cloud.google.com/go/aiplatform**](https://pkg.go.dev/cloud.google.com/go/aiplatform)

    * Gemini Enterprise Agent Platform `cloud.google.com/go/aiplatform` v1 [API reference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1)
    * Gemini Enterprise Agent Platform `cloud.google.com/go/aiplatform` v1beta1 [API reference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1beta1)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
