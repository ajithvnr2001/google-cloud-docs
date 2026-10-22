---
url: https://docs.cloud.google.com/apis/docs/overview/
title: Google Cloud APIs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:43.752180+00:00
---

# Google Cloud APIs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)



Send feedback 

#  Google Cloud APIs Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud APIs are programmatic interfaces that let you integrate compute, networking, storage, and machine learning services into your applications. You can call these network APIs over JSON HTTP or gRPC endpoints, typically using tools such as client libraries or the Google Cloud CLI.

## About Cloud APIs

Cloud APIs are exposed as network API services to customers, such as [Cloud Pub/Sub API](https://docs.cloud.google.com/pubsub). Each Cloud API typically runs on one or more subdomains of `googleapis.com`, such as `pubsub.googleapis.com`, and provides both JSON HTTP and gRPC interfaces to clients over public internet and Virtual Private Cloud (VPC) networks. Clients can send HTTP and gRPC requests to Cloud API endpoints directly or by using client libraries.

Cloud APIs are part of the [Google Enterprise APIs](https://docs.cloud.google.com/apis/docs/resources/enterprise-apis) category in the Google Cloud console [API Library](https://console.cloud.google.com/apis/library/browse?filter=category:enterprise-api).

There are two kinds of Google Cloud APIs:

  * _Resource-based APIs_ , which use the project associated with the resources being accessed for billing and quota.

  * _Client-based APIs_ , which use the project associated with the client accessing the resources for billing and quota.




## Accessing Cloud APIs

You can access Cloud APIs from server applications with our [client libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained) in many popular programming languages, from mobile apps via the [Firebase SDKs](https://firebase.google.com/docs), or by using third-party clients. You can also access Cloud APIs with the [Google Cloud CLI](https://docs.cloud.google.com/sdk), [Google Cloud console](https://console.cloud.google.com/), or [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).

If you are new to Cloud APIs, see [Getting Started](https://docs.cloud.google.com/apis/docs/getting-started) on how to use Cloud APIs.

### Supporting HTTP and gRPC

All Cloud APIs provide a simple JSON HTTP interface that you can call directly or via [Google API Client Libraries](https://developers.google.com/api-client-library). Most Cloud APIs also provide a [gRPC](https://grpc.io) interface you can call via [Google Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries), which provide better performance and usability. You can also use third-party clients.

For more information about our client libraries, see [Client Libraries Explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

For more information about authentication for using Google APIs, see [Authentication methods at Google](https://docs.cloud.google.com/docs/authentication) and [Authentication for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

### TLS encryption

All Cloud APIs accept only secure requests using TLS encryption.

  * If you are using one of our client libraries, in-transit encryption is handled for you by the library.
  * If you are using your own gRPC client, you need to authenticate with Google (which requires TLS) following the instructions in the [gRPC authentication guide](https://grpc.io/docs/guides/auth/).
  * If you are creating your own HTTP client, see our [HTTP guidelines](https://docs.cloud.google.com/apis/docs/http).



You can find out more about how traffic to Google Cloud services is secured in our [Encryption in Transit](https://docs.cloud.google.com/security/encryption-in-transit) security guide.

### Private Service Connect

Enterprise customers often want to access Cloud APIs privately for security and compliance reasons. You can use Private Service Connect to set up and manage such access within your VPC networks.

For more information, see [Configuring Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).

### Step-by-step examples

See the following step-by-step guides that use the client libraries for some popular APIs:

  * [Cloud Billing Budget API with Node.js](https://console.cloud.google.com/?tutorial=billing--budget--billing-budget-api-nodejs).
  * [Cloud Billing Budget API with Python](https://console.cloud.google.com/?tutorial=billing--budget--billing-budget-api-python).
  * [Cloud Logging with Node.js](https://console.cloud.google.com/?tutorial=logging--logging-nodejs).
  * [Cloud Logging with Python](https://console.cloud.google.com/?tutorial=logging--logging-python).
  * [Cloud Logging with Go](https://console.cloud.google.com/?tutorial=logging--logging-go).
  * [Cloud Logging with Java](https://console.cloud.google.com/?tutorial=logging--logging-java).
  * [Speech-to-Text with Node.js](https://console.cloud.google.com/?tutorial=speech-to-text--speech-to-text-nodejs).
  * [Speech-to-Text with Python](https://console.cloud.google.com/?tutorial=speech-to-text--speech-to-text-python).
  * [Speech-to-Text with Go](https://console.cloud.google.com/?tutorial=speech-to-text--speech-to-text-go).
  * [Speech-to-Text with Java](https://console.cloud.google.com/?tutorial=speech-to-text__speech-to-text-java).



## API Design Guide

Regardless of the interface type, all Cloud APIs use resource-oriented design principles as described in our [API Design Guide](https://docs.cloud.google.com/apis/design), which ensures Cloud APIs to have a simple and consistent developer experience. You can reference our API Design Guide to have a better understanding of Cloud APIs.

If you want to study the interface definition of Cloud APIs, you can visit the [Google APIs](https://github.com/googleapis/googleapis) repository on GitHub.

## Capping your usage

Cloud APIs are shared among millions of developers and users. To ensure fair usage and minimize abuse risks, all Cloud APIs are enforcing rate limits and resource quotas on usage, commonly known as quotas. You can also use these quotas to control your spending on Google Cloud products by reducing your own quota limits. If you need more quotas than the default limits, you need to file quota increase requests.

For more information, see [Capping API usage](https://docs.cloud.google.com/apis/docs/capping-api-usage).

## Monitoring your usage

Most Cloud APIs provide you with detailed information on your project's usage of that API, including traffic levels, error rates, and latencies. It helps you to quickly triage problems with applications that use Cloud APIs. You can view this information in the Google Cloud [API Dashboard](https://console.cloud.google.com/apis/dashboard) in the Google Cloud console. You can also create custom dashboards and alerts in Cloud Monitoring.

For more information, see [Monitoring API usage](https://docs.cloud.google.com/apis/docs/monitoring).

## Google Enterprise APIs

Google Enterprise APIs are high-stability APIs, ready for enterprise use with support options available.

For more information, see [Google Enterprise APIs](https://docs.cloud.google.com/apis/docs/resources/enterprise-apis).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
