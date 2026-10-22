---
url: https://docs.cloud.google.com/compute/docs/api/prereqs/
title: Prerequisites \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:25.803078+00:00
---

# Prerequisites  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/api/prereqs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Prerequisites Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the prerequisites for using the Compute Engine API.

Before you can start coding your first client application, there are a few things you need to do, if you haven't done them already.

## Get a Google Account

You need a [Google Account](https://www.google.com/accounts/NewAccount) to access the Compute Engine API. If you have an existing account, then you already have access.

You may also want a separate Google Account for testing purposes.

## Sign up and try out Compute Engine

To get started, you can create a VM instance on Compute Engine by using one of the following guides: 

  * [Create a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance)
  * [Create a Windows VM](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance)



Before you continue, it's important to become familiar with Compute Engine. The API documentation assumes that you have used Compute Engine and you're familiar with web programming concepts and web data formats.

## Learn about authentication

There are different ways to authenticate to Compute Engine depending on how you access the API. For more information, see [Authenticate to Compute Engine](https://docs.cloud.google.com/compute/docs/authentication).

## Learn about REST

There are two ways to invoke the API:

  * Sending HTTP requests and parsing the responses.
  * Using [client libraries](https://docs.cloud.google.com/compute/docs/api/libraries).



If you decide not to use client libraries, you'll need to understand the basics of REST.

### REST basics

REST is a style of software architecture that provides a convenient and consistent approach to requesting and modifying data.

The term REST is short for "[Representational State Transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)." In the context of Google APIs, it refers to using HTTP verbs to retrieve and modify representations of data stored by Google.

In a RESTful system, resources are stored in a data store; a client sends a request that the server perform a particular action (such as creating, retrieving, updating, or deleting a resource), and the server performs the action and sends a response, often in the form of a representation of the specified resource.

In Google's RESTful APIs, the client specifies an action using an HTTP verb such as `POST`, `GET`, `PUT`, or `DELETE`. It specifies a resource by a globally-unique URI of the following form:
    
    
    https://www.googleapis.com/apiName/apiVersion/resourcePath?parameters
    

Because all API resources have unique HTTP-accessible URIs, REST enables data caching and is optimized to work with the web's distributed infrastructure.

You may find the [method definitions](https://tools.ietf.org/html/rfc7231#section-4.3) in the HTTP 1.1 standards documentation useful; they include specifications for `GET`, `POST`, `PUT`, and `DELETE`.

### REST in the Compute Engine API

The Compute Engine API operations map directly to REST HTTP verbs.

The Compute Engine API uses the following format for URIs:
    
    
    https://www.googleapis.com/compute/API_VERSION/RESOURCE_PATH

The URI contains the following values: 

  * `API_VERSION`: the API version that you want to use, which corresponds to the [launch stage](https://cloud.google.com/products#product-launch-stages) of a Compute Engine resource as follows: 
    * For resources in GA: `v1`
    * For resources in Public Preview: `beta`
    * For resources in Private Preview: `alpha`
  * `RESOURCE_PATH`: the path to the specific Compute Engine resource—for example, `projects/example-project/aggregated/instances`. To see available resources for each API version, see the following: 
    * [Compute Engine API v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1)
    * [Compute Engine API beta](https://docs.cloud.google.com/compute/docs/reference/rest/beta)
    * [Compute Engine API alpha](https://docs.cloud.google.com/compute/docs/reference/rest/alpha) ([Preview](https://cloud.google.com/products#product-launch-stages))



If you want to include query parameters, then include them in the URI after a question mark (`?`):
    
    
    https://www.googleapis.com/compute/API_VERSION/RESOURCE_PATH**? QUERY_PARAMETERS**

In the URI, QUERY_PARAMETERS is a list of query parameters, separated by ampersands (`&`)—for example, `format=json**&** filter=zone=us-central1-a`. 

## Learn about the JSON data format

The Compute Engine API returns data in JSON format.

[JSON](http://en.wikipedia.org/wiki/JSON) (JavaScript Object Notation) is a common, language-independent data format that provides a simple text representation of arbitrary data structures. For more information, see [json.org](http://www.json.org/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
