---
url: https://docs.cloud.google.com/billing/docs/how-to/budget-api-prereqs/
title: Cloud Billing Budget API Prerequisites \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:13:32.155400+00:00
---

# Cloud Billing Budget API Prerequisites  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/budget-api-prereqs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  Cloud Billing Budget API Prerequisites Stay organized with collections  Save and categorize content based on your preferences. 

Before you start coding your first Cloud Billing budget application, there are a few things you need to do, if you haven't done them already.

## Try out the Cloud Billing features in the Google Cloud console

This API documentation assumes that you've used Google Cloud, and that you're familiar with the Cloud Billing features and concepts in the Google Cloud console. If you're not already familiar with concepts like Cloud Billing accounts, Google Cloud projects, Google Cloud products, and Cloud Billing budgets and alerts, read the following before starting to code:

  * [Overview of Cloud Billing concepts](https://docs.cloud.google.com/billing/docs/concepts)
  * [Manage your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account)
  * [View the projects linked to a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked)
  * [Overview of budgets and budget alert rules](https://docs.cloud.google.com/billing/docs/how-to/budgets)
  * [Manage spend cap budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps)
  * [Access control for the Cloud Billing Budget API](https://docs.cloud.google.com/billing/docs/access-control)



After you are familiar with the Cloud Billing features and concepts, try out the [Google Cloud console user interface](https://console.cloud.google.com/).

## Key Cloud Billing concepts

  * Each individual Cloud Billing account can have [several thousand budgets](https://docs.cloud.google.com/billing/quotas) associated with it at a time. See [Quotas and limits](https://docs.cloud.google.com/billing/quotas) for the current limits and additional information.
  * A budget is linked to only one Cloud Billing account at a time.
  * A single Cloud Billing account is linked to, and pays for, one or more Google Cloud projects.
  * A Google Cloud project is linked to only one Cloud Billing account at a time.
  * You can create **alerts-only budgets** to monitor your costs for an entire Cloud Billing account, including all the Google Cloud projects paid for by that billing account. You can also define the scope of alerts-only budgets using [granular budget filters](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope) to monitor specific slices of your costs. Filters include Google Cloud projects, services, the budget's time period, and other filters applicable to your Cloud Billing account.
  * You can create **spend cap budgets** to cap your spend on an [eligible service](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#eligible-services) in a specified Google Cloud project. When the spend cap is enforced, new usage of the service in the specified project is paused until the spend cap is lifted.



## Learn REST basics

There are two ways to invoke the Cloud Billing Budget API:

  * Sending HTTP requests and parsing the responses.
  * Using [client libraries](https://docs.cloud.google.com/billing/docs/reference/budget/libraries) (recommended).



If you decide not to use client libraries, you'll need to understand the basics of REST.

REST is a style of software architecture that provides a convenient and consistent approach to requesting and modifying data.

The term REST is short for "[Representational State Transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)." In the context of Google APIs, it refers to using HTTP verbs to retrieve and modify representations of data stored by Google.

In a RESTful system, resources are stored in a data store; a client sends a request that the server perform a particular action (such as creating, retrieving, updating, or deleting a resource), and the server performs the action and sends a response, often in the form of a representation of the specified resource.

In Google's RESTful APIs, the client specifies an action using an HTTP verb such as `POST`, `GET`, `PUT`, or `DELETE`. It specifies a resource by a globally-unique URI of the following form:
    
    
    https://www.googleapis.com/apiName/apiVersion/resourcePath?parameters
    

Because all API resources have unique HTTP-accessible URIs, REST enables data caching and is optimized to work with the web's distributed infrastructure.

You may find the [method definitions](https://tools.ietf.org/html/rfc7231#section-4.3) in the HTTP 1.1 standards documentation useful; they include specifications for `GET`, `POST`, `PUT`, and `DELETE`.

### REST in the Cloud Billing Budget API

The Cloud Billing Budget API operations map directly to REST HTTP verbs.

The specific formats for Cloud Billing Budget API URIs are:
    
    
    https://billingbudgets.googleapis.com/v1/resourcePath?parameters
    

The full set of URIs used for each supported operation in the API is summarized in the Cloud Billing Budget API [REST reference documents](https://docs.cloud.google.com/billing/docs/reference/budget/rest).

## Learn JSON basics

The Cloud Billing Budget API returns data in JSON format.

[JSON](http://en.wikipedia.org/wiki/JSON) (JavaScript Object Notation) is a common, language-independent data format that provides a simple text representation of arbitrary data structures. For more information, see [json.org](http://www.json.org/).

[ Previous arrow_back  Get started with the Budget API  ](https://docs.cloud.google.com/billing/docs/how-to/budget-api-overview)

[ Next Setup  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/budget-api-setup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
