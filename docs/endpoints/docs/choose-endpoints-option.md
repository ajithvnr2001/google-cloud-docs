---
url: https://docs.cloud.google.com/endpoints/docs/choose-endpoints-option/
title: Choosing an Endpoints option \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:13.508174+00:00
---

# Choosing an Endpoints option  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/choose-endpoints-option/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)



Send feedback 

#  Choosing an Endpoints option Stay organized with collections  Save and categorize content based on your preferences. 

To have your API managed by Cloud Endpoints, you have three options depending on where your API is hosted and the type of communications protocol your API uses:

  * [Cloud Endpoints for OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi)
  * [Cloud Endpoints for gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)
  * [Cloud Endpoints Frameworks for the App Engine standard environment](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



This page describes the Endpoints options to help you decide which one is right for you.

## Choosing a computing option

Endpoints supports different Google Cloud computing options that can host your API's backend code. Endpoints works with either the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy) or the [Extensible Service Proxy V2](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) (ESPv2) to provide API management. The following table summarizes the supported computing options:

| **ESP for OpenAPI** | **ESP for gRPC** | **ESPv2 for OpenAPI** | **ESPv2 for gRPC** | **Endpoints Frameworks**  
---|---|---|---|---|---  
**App Engine  
standard environment generation 1** |  |  |  |  |  Java 8 and Python 2.7 runtimes  
**App Engine  
standard environment generation 2** |  |  |  |  |   
**App Engine  
flexible environment** |  |  |  |  |   
**Cloud Run functions** |  |  |  |  |   
**Cloud Run** |  |  |  |  |   
**Knative serving** |  |  |  |  |   
**Compute Engine** |  |  |  |  |   
**GKE** |  |  |  |  |   
**Kubernetes** |  |  |  |  |   
**Other non-Google Cloud** |  |  |  |  |   
  
For a comparison of the features provided by App Engine, GKE, and Compute Engine, see [Choosing a computing option](https://docs.cloud.google.com/docs/choosing-a-compute-option). If you are thinking of using App Engine, you need to choose either the standard or flexible environment. For a comparison of the two environments, see [Choosing an App Engine environment](https://docs.cloud.google.com/appengine/docs/the-appengine-environments).

## About the computing option limitations

Endpoints for OpenAPI and Endpoints for gRPC can use ESP or ESPv2 as a proxy. For non-serverless platforms, ESP or ESPv2 is deployed as a container in front of your application or as a sidecar with your application. For serverless platforms, such as Cloud Run, Cloud Run functions, and App Engine, ESPv2 is deployed as a Cloud Run service as a remote proxy to manage your serverless platform applications.

After you deploy your API's backend code, ESP or ESPv2 intercepts all requests and performs any necessary checks (such as authentication) before forwarding the request to the API backend. When the backend responds, ESP gathers and reports telemetry using [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/overview).

You can view metrics for your API and links to [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) logs and traces on the **Endpoints Services** page in the Google Cloud console.

### App Engine standard generation 1 environment limitations

Endpoints for the App Engine standard generation 1 environment historically used Endpoints Frameworks, which only supports the [Java 8 and Python 2.7 runtime environments](https://docs.cloud.google.com/appengine/docs/standard/runtimes).

Because the App Engine standard environment didn't support multi-container deployments when Endpoints Frameworks was under development, Endpoints Frameworks doesn't use ESP. Instead, Endpoints Frameworks includes a built-in [API gateway](https://wikipedia.org/wiki/API_management) that provides API management features that are comparable to the features that ESP provides for Endpoints for OpenAPI and Endpoints for gRPC.

**Note:** Although Endpoints Frameworks does work with the Java 7 runtime on App Engine standard environment, the [Java 7 runtime was deprecated](https://docs.cloud.google.com/appengine/docs/deprecations/java7) and is scheduled to be shutdown.

### gRPC APIs aren't supported on App Engine or Cloud Run functions

[gRPC](https://grpc.io/about/) is a remote procedure call (RPC) framework that can run on any environment. With gRPC, a client application can directly call methods in a server application on a different machine as if it were a local object. A core feature of gRPC is bi-directional streaming with [HTTP/2-based transport](https://wikipedia.org/wiki/HTTP/2).

App Engine and Cloud Run functions don't support HTTP/2.

## Supported programming languages

  * The [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) is a language-agnostic specification. You can implement your API in any programming language.
  * gRPC provides the [protocol buffer compiler](https://developers.google.com/protocol-buffers/docs/overview), `protoc`, for many major programming languages: C++, C#, Objective-C (for iOS), Dart, Go, Java (including support for Android), Node.js, Python, and Ruby. See the [gRPC FAQ](https://grpc.io/faq/) for the most up-to-date list.
  * Endpoints Frameworks supports only Java 8 and Python 2.7.



## Describing your API

The Endpoints options provide different ways to describe your API.

### Endpoints for OpenAPI

The [OpenAPI Initiative](http://openapis.org/) is an industry-wide effort to standardize the description of REST APIs. Endpoints supports APIs that are described using OpenAPI 2.0 and OpenAPI 3.x of the OpenAPI Specification (formerly the [Swagger Specification](https://swagger.io/docs/specification/about/)). To learn more, see [Supported OpenAPI versions](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview#supported-openapi-versions). You describe the [surface](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#surface) of your API in a JSON or YAML file (referred to as an OpenAPI document). You can implement your API using any publicly available REST framework such as [Django](https://www.djangoproject.com/) or [Jersey](https://jersey.github.io/). If you are unfamiliar with the OpenAPI Specification, see [OpenAPI overview](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview).

For more information, see [Endpoints for OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi).

### Endpoints for gRPC

With gRPC, you define the structure of the data that you want to serialize in a _proto file_ : this is an ordinary text file with a `.proto` extension. You also define the [surface](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#surface) of your API in proto files, with RPC method parameters and return types specified as protocol buffer messages. If you are unfamiliar with gRPC, see [What is gRPC?](https://grpc.io/docs/guides/) in the gRPC documentation.

For more information, see [Endpoints for gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc).

### Endpoints Frameworks

Endpoints Frameworks is a [web framework](https://wikipedia.org/wiki/Web_framework) for the App Engine standard Python 2.7 and Java 8 runtime environments. You add metadata (using annotations in Java or decorators in Python) to your source code. The metadata describes the [surface](https://docs.cloud.google.com/endpoints/docs/frameworks/glossary#surface) of the REST APIs for your application.

For more information, see [Endpoints Frameworks](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks).

## What's next

  * See Endpoints features in action by doing the [Quickstart for Endpoints](https://docs.cloud.google.com/endpoints/docs/deploy-api), which uses scripts to deploy a sample API to the App Engine flexible environment.

  * Get familiar with the deployments steps by doing one of the tutorials for the Endpoints option that you have chosen:

    * [Endpoints for OpenAPI: Tutorials](https://docs.cloud.google.com/endpoints/docs/openapi/tutorials)
    * [Endpoints for gRPC: Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials)
    * [Endpoints Frameworks: Tutorials](https://docs.cloud.google.com/endpoints/docs/frameworks/tutorials)
  * Learn more about Endpoints and ESP:

    * [Endpoints for OpenAPI: About Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints)
    * [Endpoints for gRPC: About Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/about-cloud-endpoints)
    * [Comparing Extensible Service Proxy and Endpoints Frameworks](https://docs.cloud.google.com/endpoints/docs/frameworks/frameworks-extensible-service-proxy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
