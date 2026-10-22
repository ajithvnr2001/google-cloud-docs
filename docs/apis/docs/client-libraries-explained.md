---
url: https://docs.cloud.google.com/apis/docs/client-libraries-explained/
title: Client libraries and Cloud APIs explained \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:19.012757+00:00
---

# Client libraries and Cloud APIs explained  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/docs/client-libraries-explained/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Client libraries and Cloud APIs explained Stay organized with collections  Save and categorize content based on your preferences. 

Client libraries let you access Google Cloud APIs programmatically with less boilerplate code by handling authentication and low-level server communication. This document explains the following methods for interacting with Google Cloud APIs:

  * Cloud Client Libraries (recommended)
  * Google API Client Libraries
  * The Firebase development platform
  * Your own client code



To find client library information for a specific Google Cloud product, see the client libraries section within that product's documentation.

## Cloud Client Libraries

While you can use Google Cloud APIs directly by making raw requests to the server, [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) provide simplifications that significantly reduce the amount of code you need to write. Cloud Client Libraries are the recommended option for accessing Cloud APIs programmatically, because they use the latest client library model and:

  * Provide idiomatic code in each language to make Google Cloud APIs intuitive to use.
  * Provide a consistent style across client libraries to simplify working with multiple Google Cloud services.
  * Handle all the low-level details of communication with the server, including [authenticating with Google](https://docs.cloud.google.com/docs/authentication/client-libraries).
  * Can be installed using familiar package management tools such as `npm` and `pip`.
  * In some cases, give you performance benefits by using gRPC. For more information, see gRPC APIs.



The installation instructions and reference materials for Cloud Client Libraries depend on the specific Google Cloud API and the programming language you are using. To find this information, see the documentation for the specific Google Cloud product. Most products include a "Client Libraries" section in their documentation, which provides language-specific guidance, installation steps, and links to the detailed API reference.

You can find the documentation for a specific product by browsing the [Google Cloud API library](https://docs.cloud.google.com/apis).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

## Google API Client Libraries

If Cloud Client Libraries aren't available for your preferred language for a specific API, you can use the [Google API Client Libraries](https://developers.google.com/api-client-library/). These are an earlier type of client library provided by Google.

You might also use these libraries if you're upgrading a project that already uses them. These libraries:

  * Provide access to the API's REST interface only; gRPC is not supported.
  * Have auto-generated interface code that might not be as idiomatic as the Cloud Client Libraries.
  * Handle all the low-level details of communication with the server, including [authenticating with Google](https://docs.cloud.google.com/docs/authentication/client-libraries).
  * Can be installed using familiar package management tools such as `npm` and `pip`.



## Use the Firebase development platform

Firebase is Google's platform of services designed to support your entire app development lifecycle. It provides cross-platform SDKs to help you and AI agents build and run apps for Apple platforms, Android, the web, Flutter, Unity, and C++.

For information on the supported Google Cloud APIs and how to get started with Firebase, see the [Firebase documentation](https://firebase.google.com/docs).

## Use your own client code

If you're an experienced developer and Cloud Client Libraries don't meet your specific needs, you can write your own custom code to access the service's lower-level service APIs directly.

### REST/HTTP APIs

All Google Cloud APIs expose a JSON/REST interface. If you need to write your own custom code to directly access the REST API using a third-party HTTP client library, you can find out more about how Google Cloud APIs work with different HTTP versions and implementations in the [HTTP Guidelines](https://docs.cloud.google.com/apis/docs/http).

### gRPC APIs

gRPC is a language-neutral, platform-neutral, open source, remote procedure call (RPC) system initially developed at Google. You can find out more at [grpc.io](http://www.grpc.io/). gRPC-enabled Google Cloud APIs generally have both REST and RPC interfaces, so rather than just using JSON over HTTP to talk to the REST interface, gRPC-enabled API clients can also use [protocol buffers](https://developers.google.com/protocol-buffers/) and gRPC over HTTP2 to talk to the RPC interface. You can find out if an API is gRPC-enabled by checking its APIs and Reference section.

If a Google Cloud API is gRPC-enabled, you can generate your own gRPC client libraries for it in any gRPC-supported language. To do this, you'll need the API's [protocol buffers](https://developers.google.com/protocol-buffers/) service definition (typically available from [the repository on GitHub](https://github.com/googleapis/googleapis)).

You can then follow the instructions for your preferred language on [grpc.io](http://www.grpc.io/) to generate and use your client.

If you don't want to generate your own gRPC code, you can still benefit from gRPC: a growing number of Cloud Client Libraries for gRPC-enabled APIs use gRPC "under the hood" to communicate with Google's servers. This is significantly more efficient in terms of throughput and CPU usage—accessing an API using gRPC can increase throughput per CPU by as much as a factor of 10 compared to the JSON REST API. Google plans to upgrade as many Cloud Client Libraries as possible to gRPC; in the meantime, you'll still get all the other advantages of Google's client library code.

## Other ways to access Cloud APIs

If you don't want to access an API programmatically, you can access some of the same functionality using the tools in [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) or using the [Google Cloud console](https://console.cloud.google.com/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
