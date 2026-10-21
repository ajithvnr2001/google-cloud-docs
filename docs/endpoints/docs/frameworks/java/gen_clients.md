---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/gen_clients/
title: Generating a client library \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:20.161656+00:00
---

# Generating a client library  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/gen_clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Generating a client library Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to generate a client library from your backend API. Any Java or Android app can use this library to call the API.

To create iOS clients for your API, we recommend that you use [Google APIs Objective-C Client Library for REST APIs](https://github.com/google/google-api-objectivec-client-for-rest/wiki).

## Before you begin

  * [Set up your development environment](https://docs.cloud.google.com/endpoints/docs/frameworks/java/set-up-environment).
  * Make sure you have properly [annotated](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code) your API.



## Generating the client library

The following instructions demonstrate how to use the Cloud Endpoints Frameworks [Apache Maven](https://docs.cloud.google.com/endpoints/docs/frameworks/java/maven-endpoints-frameworks-plugin) and [Gradle](https://docs.cloud.google.com/endpoints/docs/frameworks/java/gradle-endpoints-frameworks-plugin) plugins to generate a Gradle client bundle from the sample Maven project [Getting started with Endpoints](https://docs.cloud.google.com/endpoints/docs/frameworks/java/quickstart-frameworks-java).

To generate a client library:

  1. Build your API

  2. Run the Endpoints Frameworks command-line tool similarly to the following:

### Maven
         
         mvn endpoints-framework:clientLibs

### Gradle
         
         gradle endpointsClientLibs

Wait for the tool to generate the library; on success the tool displays a message similar to this one:

### Maven
         
         API client library written to target/client-libs/echo-v1-java.zip

### Gradle
         
         API client library written to build/endpointsClientLibs/echo-v1-java.zip

  3. Unzip the file by using the unzip utility, or use another ZIP-compatible unarchiving utility:
         
         unzip ./echo-v1-java.zip
         

  4. Change directory:
         
         cd echo
         

  5. Build the client library:

### Maven
         
         mvn clean package

The output is in the `target/` directory. The exact filename depends on the version of the Java client. It is something similar to `echo-v1-1.23.0-SNAPSHOT.jar`.

### Gradle
         
         gradle build

The output is in the `build/libs` directory. The exact filename depends on the version of the Java client. It is something similar to `echo-v1-1.23.0-SNAPSHOT.jar`.

  6. Add the client library JAR to your Java or Android app.

  7. Repeat these steps every time you modify your API code.




## What's next

  * [Call the backend API from an Android app](https://docs.cloud.google.com/endpoints/docs/frameworks/java/calling-from-android).
  * [Learn more about Cloud Endpoints Frameworks for App Engine](https://docs.cloud.google.com/endpoints/docs/frameworks/java).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
