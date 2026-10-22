---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/frameworks-extensible-service-proxy/
title: Comparing Extensible Service Proxy and Cloud Endpoints Frameworks \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:43.545345+00:00
---

# Comparing Extensible Service Proxy and Cloud Endpoints Frameworks  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/frameworks-extensible-service-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Comparing Extensible Service Proxy and Cloud Endpoints Frameworks Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the differences between Endpoints Frameworks for the App Engine standard environment and the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/frameworks/glossary#extensible_service_proxy), which is used in Cloud Endpoints for APIs using [OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi) or [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc). For more information about the Endpoints options, see [Choosing an Endpoints option](https://docs.cloud.google.com/endpoints/docs/choose-endpoints-option).

## Overview

Cloud Endpoints is an API management system that helps you secure, monitor, analyze, and set quotas on your APIs using the same infrastructure Google uses for its own APIs. API management features includes authentication, API keys, monitoring, logging, and tracing independent of the technology used to implement the API. API management functionality is provided through ESP or by using the Endpoints Frameworks.

## Extensible Service Proxy

In Endpoints for OpenAPI and gRPC, API requests are relayed through the Extensible Service Proxy, which validates keys and authentication tokens and sends signals (metrics and logs) by using the [Service Control](https://docs.cloud.google.com/service-control/overview) API. The separation provided by ESP means that you can write the REST or gRPC backend code in any language, and you can use gRPC or any framework that supports API description using OpenAPI.

  * APIs using OpenAPI: The API backend can run on the App Engine flexible environment, Google Kubernetes Engine (GKE), Compute Engine, Kubernetes, or on-premises deployments.

  * APIs using gRPC: The API backend can run on GKE, Compute Engine, Kubernetes, or on-premises deployments.




![ESP architecture](https://docs.cloud.google.com/endpoints/docs/images/esp-architecture.png)

A request is sent on the following path:

  1. A request to your code is received and is sent to ESP.
  2. ESP sends a check request to Service Control.
  3. If you configured your API to require an API key or authentication, Service Control checks to see if the request is permitted and sends a response back to ESP.
  4. If the request isn't permitted, ESP rejects the request. If the request is permitted, it is forwarded to your backend code. Either way, ESP logs information about the request.



[Pricing of Endpoints API management](https://cloud.google.com/endpoints/pricing) depends on the number of calls per month.

## Endpoints Frameworks

For API backends running on the App Engine standard environment, Endpoints Frameworks is available to help developers quickly get started serving an API. Endpoints Frameworks is a [web framework](https://wikipedia.org/wiki/Web_framework) and is an alternative to Python Flask or Java Jersey. Endpoints Frameworks integrates with the Service Control API, meaning a backend that uses Endpoints Frameworks doesn't need to run behind the Extensible Service Proxy.

**Note:** Endpoints Frameworks is the only way to get API management functionality, such as monitoring, logging, and API keys, on the App Engine standard environment. Only the [Python 2.7 and Java 8 runtime environments](https://docs.cloud.google.com/appengine/docs/standard/runtimes) are supported.

![Endpoints Frameworks](https://docs.cloud.google.com/endpoints/docs/images/frameworks-architecture.png)

If you have enabled API Management, a request is sent on the following path:

  1. A request to your code is received and is sent to the Endpoints Management module within Endpoints Frameworks.
  2. The Endpoints Management module sends a check request to Service Control.
  3. If you configured your API to require an API key or authentication, Service Control checks to see if the request is permitted and sends a response back to the Endpoints Management module.
  4. If the request isn't permitted, the Endpoints Management module rejects the request. If the request is permitted, it is forwarded to Endpoints Frameworks. Either way, the Endpoints Management module logs information about the request.
  5. Endpoints Frameworks routes the request to your backend code.



You can use Endpoints Frameworks with or without API management functionality. Use of Endpoints Frameworks without API management functionality is offered at no charge. API management functionality is charged according to the [Endpoints pricing page](https://cloud.google.com/endpoints/pricing).

Endpoints Frameworks is supported only for services running on the App Engine standard environment. On Compute Engine, GKE, App Engine flexible environment, or other environments, your services must run behind ESP.

If the service is running behind ESP, you can write the backend code in any language and framework, such as Python Flask, Java Jersey, or Node.js Express. In such environments, there is no need to use Endpoints Frameworks for API management.

## What's next

  * For information on adding API management:

    * [Java: Adding API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management)
    * [Python: Adding API management](https://docs.cloud.google.com/endpoints/docs/frameworks/python/adding-api-management)
  * For information on removing API management:

    * [Java: Removing API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/remove-api-management)
    * [Python: Removing API management](https://docs.cloud.google.com/endpoints/docs/frameworks/python/remove-api-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
