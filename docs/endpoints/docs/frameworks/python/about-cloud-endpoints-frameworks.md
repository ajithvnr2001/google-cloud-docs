---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/about-cloud-endpoints-frameworks/
title: About Cloud Endpoints Frameworks for Python \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:32.599216+00:00
---

# About Cloud Endpoints Frameworks for Python  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/about-cloud-endpoints-frameworks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  About Cloud Endpoints Frameworks for Python Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the libraries and tools and provides other information to help you get started using Endpoints Frameworks for Python. See [About Endpoints Frameworks](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks) for an architectural overview of Endpoints Frameworks.

## Libraries and tools

Cloud Endpoints Frameworks for the App Engine standard environment provides the following libraries and tools: 

  * The [Frameworks library](https://docs.cloud.google.com/endpoints/docs/frameworks/python/get-started-frameworks-python#installing_the_library).
  * The [`endpointscfg.py`](https://docs.cloud.google.com/endpoints/docs/frameworks/python/endpoints_tool) command-line tool, which you use to generate the following: 
    * Client library bundles and [Discovery documents](https://developers.google.com/discovery/v1/reference/apis), which allow Android apps and other types of client applications to access your API.
    * [OpenAPI configuration files](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md), which you use if you want [API management](https://docs.cloud.google.com/endpoints/docs/frameworks/python/adding-api-management) functionality such as monitoring, logging, and API key validation.

**Note:** Because the API backend is an App Engine application, developers can use services and features available in the App Engine standard environment, such as [Datastore](https://docs.cloud.google.com/appengine/docs/python/datastore), [Cloud Storage](https://cloud.google.com/storage/docs/overview) , [Mail](https://docs.cloud.google.com/appengine/docs/python/mail) , [Url Fetch](https://docs.cloud.google.com/appengine/docs/python/urlfetch) , [Task queues](https://docs.cloud.google.com/appengine/docs/python/taskqueue) , and so forth. And finally, by using App Engine for the backend, developers are freed from system admin work, load balancing, scaling, and server maintenance.

## Requirements

**Important:** Endpoints Frameworks supports only Python 2.7.x. It doesn't support Python 3.x.

To use Endpoints Frameworks, follow the process shown in the [Tutorial](https://docs.cloud.google.com/endpoints/docs/frameworks/python/get-started-frameworks-python).

And finally, you need to know how to develop the client of your choice, such as JavaScript web clients, or mobile clients, such as Android.

**Note:** You cannot call a Cloud Endpoints API directly from a [push task queue](https://docs.cloud.google.com/appengine/docs/standard/python/taskqueue#push_queues) or a [cron job](https://docs.cloud.google.com/appengine/docs/standard/python/config/cron#Python_calling_google_cloud_endpoints).

## Development process

The general workflow for developing an application using Endpoints Frameworks is:

  1. Write your API code first, wrapping the classes and any exposed methods, and creating `Message` classes as described in [Create an Endpoints API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api).
  2. [Create a web server](https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server) to serve your API.
  3. Generate the OpenAPI configuration file and deploy it as described in the [Tutorial](https://docs.cloud.google.com/endpoints/docs/frameworks/python/get-started-frameworks-python).
  4. Optionally, [test your API locally](https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy#testing_an_api_locally).
  5. [Deploy the API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy).
  6. [Generate client libraries](https://docs.cloud.google.com/endpoints/docs/frameworks/python/gen_clients).
  7. Write your client application by using the client libraries when making calls to the API.



## Getting started

To get started, follow the [Tutorial](https://docs.cloud.google.com/endpoints/docs/frameworks/python/get-started-frameworks-python) to configure, deploy, and send requests to a sample API. Then come back to this section for the information you need to configure, deploy, and test your own API.

## Migrating from Endpoints version 1.0

If you've already developed an API backend using the previous version of Endpoints, follow the [Migration guide](https://docs.cloud.google.com/endpoints/docs/frameworks/python/migrating) to move your app to Endpoints version 2.0.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
