---
url: https://docs.cloud.google.com/billing/v1/prereqs/
title: Prerequisites \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:13:41.974142+00:00
---

# Prerequisites  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/v1/prereqs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  Prerequisites Stay organized with collections  Save and categorize content based on your preferences. 

Before you can start coding your first client application, there are a few things you need to do, if you haven't done them already.

  1. Try out the billing features in the Google Cloud console
  2. Learn REST basics
  3. Learn JSON basics



## Try out the Cloud Billing features in the Google Cloud console

This API documentation assumes that you've used Google Cloud, and that you're familiar with the Cloud Billing features and concepts in the Google Cloud console.

If you're not already familiar with concepts like Cloud Billing Accounts and Google Cloud projects then try out the [user interface](https://console.cloud.google.com/billing) before starting to code.

## Learn REST basics

There are two ways to invoke the Cloud Billing API:

  * Sending HTTP requests and parsing the responses.
  * Using [client libraries](https://docs.cloud.google.com/billing/v1/libraries).



If you decide not to use client libraries, you'll need to understand the basics of REST.

REST is a style of software architecture that provides a convenient and consistent approach to requesting and modifying data.

The term REST is short for "[Representational State Transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)." In the context of Google APIs, it refers to using HTTP verbs to retrieve and modify representations of data stored by Google.

In a RESTful system, resources are stored in a data store; a client sends a request that the server perform a particular action (such as creating, retrieving, updating, or deleting a resource), and the server performs the action and sends a response, often in the form of a representation of the specified resource.

In Google's RESTful APIs, the client specifies an action using an HTTP verb such as `POST`, `GET`, `PUT`, or `DELETE`. It specifies a resource by a globally-unique URI of the following form:
    
    
    https://www.googleapis.com/apiName/apiVersion/resourcePath?parameters
    

Because all API resources have unique HTTP-accessible URIs, REST enables data caching and is optimized to work with the web's distributed infrastructure.

You may find the [method definitions](https://tools.ietf.org/html/rfc7231#section-4.3) in the HTTP 1.1 standards documentation useful; they include specifications for `GET`, `POST`, `PUT`, and `DELETE`.

### REST in the Cloud Billing API

The Cloud Billing API operations map directly to REST HTTP verbs.

The specific formats for Cloud Billing API URIs are:
    
    
    https://www.googleapis.com/billing/v1/resourcePath?parameters
    

The full set of URIs used for each supported operation in the API is summarized in the Cloud Billing API reference documents ([REST](https://docs.cloud.google.com/billing/reference/rest), [RPC](https://docs.cloud.google.com/billing/reference/rpc)).

## Learn JSON basics

The Cloud Billing API returns data in JSON format.

[JSON](http://en.wikipedia.org/wiki/JSON) (JavaScript Object Notation) is a common, language-independent data format that provides a simple text representation of arbitrary data structures. For more information, see [json.org](http://www.json.org/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
