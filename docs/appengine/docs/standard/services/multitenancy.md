---
url: https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/
title: Namespaces API for legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:20.397968+00:00
---

# Namespaces API for legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Namespaces API for legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

The Namespaces API makes it easy to compartmentalize your App Engine data. This API is implemented via a new package called the [namespace manager](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/namespace_manager) , and is incorporated in certain namespace-enabled APIs.

When you set a namespace in the namespace manager, these APIs get the current namespace and use it globally. You can explicitly declare a namespace locally, but you need to exercise caution when explicitly declaring namespaces, because you could inadvertently create data leaks and other bugs. Any App Engine request can access any namespace, leaving the application to enforce an access control policy across namespaces.

You can use the Namespaces API to build a wide range of applications. One of the most compelling uses of this API is for multitenant applications, as described below.

## About multitenancy

_Multitenancy_ is the name given to a software architecture in which one instance of an application, running on a remote server, serves many client organizations (also known as _tenants_).

Using a multitenant architecture simplifies administration and provisioning of tenants. You can provide a more streamlined, customized user experience, and also aggregate different silos of data under a single database schema. As a result, your applications become more scalable as well as more cost-effective as you scale. Data becomes easier to segregate and analyze across tenants because all tenants share the same database schema. Different user groups see custom content wrapped within a more efficient application.

## Building a multitenant application with the Namespaces API

Using the Namespaces API, you can easily partition data across tenants simply by specifying a unique namespace string for each tenant. You simply [set the namespace](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy#Setting_the_current_namespace) for each tenant globally using the namespace manager (as opposed to setting it explicitly for a specific request). The namespace-enabled APIs always use this current namespace by default.

The Namespaces API is integrated with Google Workspace, allowing you to use your Google Workspace domain as the current namespace. Because Google Workspace lets you deploy your app to any domain that you own, you can easily [set unique namespaces](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy#Setting_the_current_namespace) for all domains linked to your Google Workspace account.

When designing multitenant applications, you need to prevent data from leaking across namespaces. For more information, please see [Avoiding Data Leaks](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy#Avoiding_data_leaks).

## App Engine APIs that use namespaces

App Engine currently supports namespaces in second-generation runtimes for the following APIs:

  * [Datastore](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy#Using_namespaces_with_the_Datastore)
  * [Memcache](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy#Using_namespaces_with_the_Memcache)
  * [Task Queue](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy#Using_namespaces_with_the_Task_Queue)
  * [Search](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy#Using_namespaces_with_Search)



## Other uses for the Namespace API

While the Namespaces API enables multitenancy on App Engine, it has a number of other uses, including:

  * Compartmentalizing user information
  * Separating admin data from application data
  * Creating separate datastore instances for testing and production
  * Running multiple apps on a single App Engine instance



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
