---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/library/java/
title: Java client library \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:57.269684+00:00
---

# Java client library  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/library/java/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Java client library Stay organized with collections  Save and categorize content based on your preferences. 

This page provides reference documentation and related resources for the Dialogflow CX Java client library. 

Resource | Description  
---|---  
[Library reference](https://cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/overview) | Dialogflow CX Java library reference  
[Language guide](https://cloud.google.com/java/docs/) | General guide for using Java with GCP  
[GitHub repository](https://github.com/googleapis/java-dialogflow-cx) | Source code and additional documentation for this library  
[Quickstart](https://docs.cloud.google.com/dialogflow/cx/docs/quick/api) | Introduction to using this library  
[Stack Overflow](http://stackoverflow.com/search?q=%5Bdialogflow-cx%5D+%5Bjava%5D) | Questions tagged with Dialogflow CX and Java  
  
### Installation

To install the client library: 

**Caution:** The Java client library does not support Android.

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
        <artifactId>google-cloud-dialogflow-cx</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-dialogflow-cx'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-dialogflow-cx" % "0.110.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

## V3Beta1 client library

**Beta**  
The V3Beta1 API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy. The V3Beta1 API is not intended for real-time usage in critical applications. 

Dialogflow's V3Beta1 API offers new features that are not yet available with the V3 API. To use the V3Beta1 client library, specify the V3Beta1 API in your code by using the following import statement:
    
    
    import com.google.cloud.dialogflow.cx.v3beta1.*;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
