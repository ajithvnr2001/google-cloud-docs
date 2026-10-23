---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/about-cloud-endpoints-frameworks/
title: About Cloud Endpoints Frameworks for Java \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:59.806439+00:00
---

# About Cloud Endpoints Frameworks for Java  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/about-cloud-endpoints-frameworks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  About Cloud Endpoints Frameworks for Java Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the libraries and tools and provides other information to help you get started using Endpoints Frameworks for Java. See [About Endpoints Frameworks](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks) for an architectural overview of Endpoints Frameworks.

## Libraries and tools

Cloud Endpoints Frameworks for the App Engine standard environment provides the following libraries and tools: 

  * The Endpoints Frameworks is available in the [Maven Central Repository](http://search.maven.org/) in the group `com.google.endpoints`. The base required `.jar` file is in the `endpoints-framework` artifact. See [API Javadoc](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc) for details.
  * The [`endpoints`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/endpoints_tool) command-line tool (for Linux), or `endpoints.cmd` (for Windows) that you can use to generate client library bundles and [Discovery documents](https://developers.google.com/discovery/v1/reference/apis), which allow Android apps and other types of client applications to access your API.
  * The [Endpoints Frameworks Maven plugin](https://docs.cloud.google.com/endpoints/docs/frameworks/java/maven-endpoints-frameworks-plugin) and the [Endpoints Frameworks Gradle plugin](https://docs.cloud.google.com/endpoints/docs/frameworks/java/gradle-endpoints-frameworks-plugin), which you use to generate the following: 
    * Client library bundles and Discovery documents.
    * [OpenAPI configuration files](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md), which you use if you want [API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management) functionality such as monitoring, logging, and API key validation.

**Note:** Because the API backend is an App Engine application, developers can use services and features available in the App Engine standard environment, such as [Datastore](https://docs.cloud.google.com/appengine/docs/java/datastore) , [Cloud Storage](https://cloud.google.com/storage/docs/overview) , [Mail](https://docs.cloud.google.com/appengine/docs/java/mail) , [Url fetch](https://docs.cloud.google.com/appengine/docs/java/urlfetch) , [Task queues](https://docs.cloud.google.com/appengine/docs/java/taskqueue) , and so forth. And finally, by using App Engine for the backend, developers are freed from system admin work, load balancing, scaling, and server maintenance.

## Requirements

To use Endpoints Frameworks, follow the process shown in the [Tutorial](https://docs.cloud.google.com/endpoints/docs/frameworks/java/get-started-frameworks-java).

You need to know how to develop the client of your choice, such as JavaScript web clients, or mobile clients, such as Android.

**Note:** You cannot call a Cloud Endpoints API directly from a [push task queue](https://docs.cloud.google.com/appengine/docs/standard/java/taskqueue#push_queues) or a [cron job](https://docs.cloud.google.com/appengine/docs/standard/java/config/cron#Java_calling_google_cloud_endpoints).

## Development process

The general workflow for developing an application using Endpoints Frameworks is:

  1. Create your API project, and then write your API code.
  2. [Annotate](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code) your API, so classes and client libraries are generated from it.
  3. Generate the OpenAPI configuration file and deploy it as described in the [Tutorial](https://docs.cloud.google.com/endpoints/docs/frameworks/java/get-started-frameworks-java).
  4. Optionally, [test your API locally](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy#running_and_testing_api_backends_locally).
  5. [Deploy the API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy).
  6. [Generate the client library](https://docs.cloud.google.com/endpoints/docs/frameworks/java/gen_clients).
  7. Write your client application by using the client library when making calls to the API.



## Getting started

To get started, follow the [Tutorial](https://docs.cloud.google.com/endpoints/docs/frameworks/java/get-started-frameworks-java) to configure, deploy, and send requests to a sample API. Then come back to this section for the information you need to configure, deploy, and test your own API.

## Migrating from Endpoints version 1.0

If you've already developed an API backend using the previous version of Endpoints, follow the [Migration guide](https://docs.cloud.google.com/endpoints/docs/frameworks/java/migrating) to move your app to Endpoints version 2.0.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
