---
url: https://docs.cloud.google.com/endpoints/docs/grpc/quotas-overview/
title: About quotas \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:18.231419+00:00
---

# About quotas  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/quotas-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  About quotas Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-overview "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Endpoints provides quotas, which let you control the rate at which applications can call your API. Setting a quota lets you specify usage limits to protect your API from an excessive number of requests from calling applications. The excessive requests might have been caused by a typo or from an inefficiently designed system that makes needless calls to your API. Regardless of the cause, blocking traffic from a source once it reaches a certain level is necessary for the overall health of your API. By setting a quota, you ensure that one application cannot negatively impact other applications that use your API.

This page provides an overview of the key functionality provided by quotas.

## Requests are tied to the consumer project

After you configure a quota, Endpoints tracks the number of requests per minute per consumer Google Cloud project. Each application that calls your API must:

  * Have a Google Cloud project.
  * Have [enabled your API](https://docs.cloud.google.com/endpoints/docs/grpc/control-api-callers) in their Google Cloud project. 
  * Send an [API key](https://docs.cloud.google.com/endpoints/docs/grpc/restricting-api-access-with-api-keys) with each request to your API. This lets Endpoints identify the Google Cloud project that the calling application is associated with and to increment the request counter for the Google Cloud project. 



You can either have your API consumers create their own projects in the Google Cloud console, or you can create the projects for them. Because Endpoints enforces quotas per _project_ , you must have one project for each API consumer.

## Limit the number of requests per minute

By setting a quota, you can limit the number of requests per minute to your entire API or only to specific methods. If the client code from a consumer project exceeds the limit that you have configured, the request is rejected before it gets to your API, and an HTTP status code of [`429 too many requests`](https://tools.ietf.org/html/rfc6585#section-4) is returned. Calling applications will need to handle the `429` status code and use [exponential backoff](https://wikipedia.org/wiki/Exponential_backoff) or some other retry logic to decrease the rate of calls to your API.

**The enforced limit has 30% error margin.** Endpoints uses aggregation and batching at the proxy to reduce the runtime request latency. Instead of calling quota server to check available quota for each request, the proxy aggregates and batches the quota calls. As a result, the enforced quota limit is approximate, with a 30% margin of error. For example, if the expected limit is 100 requests per minute, the quota limit enforced could range from 70 requests per minutes to 130 requests per minute.

## Configure one or more quotas

You can configure one or more named quotas and specify a different rate limit for each quota. For example, you could have some methods in your API that are resource-intensive (such as a method that runs a complex query and returns a large list of results), and other methods that are fast and lightweight. You might want to configure two quotas with different rate limits, and associate the resource-intensive methods with one quota, and the lightweight methods with the other quota.

## Configure a cost

When you associate a method with a quota, you always specify a cost for the request. This allows different methods to consume the same quota at different rates. You can use costs as an alternative to configuring different quotas. For example, suppose you configure a quota with a limit of 1000 requests per minute. For the lightweight methods, you configure a cost of 1, which means clients can call the lightweight methods 1000 times per minute. For the resource-intensive methods, you configure a cost of 2, which means that each time the client calls the method, the request counter is incremented by 2, until the limit of 1000 is reached. In effect, this limits the resource-intensive methods to 500 requests per minute.

## Override the configured quota

The **Endpoints** > **Services** page displays the quota configured for each method in your API. If needed, you can override the configured limit for a specific consumer project. To set an override, you need to enter the project number of the consumer project on the **IAM & Admin** > **Quotas & Systems Limits** page. If you don't have access to the consumer project that you want to override, you need to contact someone who has access to obtain the project number.

## What's next

  * [Configuring quotas](https://docs.cloud.google.com/endpoints/docs/grpc/quotas-configure)
  * [Overriding quotas](https://docs.cloud.google.com/endpoints/docs/grpc/quotas-override)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
