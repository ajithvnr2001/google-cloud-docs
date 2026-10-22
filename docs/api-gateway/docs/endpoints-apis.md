---
url: https://docs.cloud.google.com/api-gateway/docs/endpoints-apis/
title: Deploy Cloud Endpoints APIs on API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:07.536035+00:00
---

# Deploy Cloud Endpoints APIs on API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/endpoints-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy Cloud Endpoints APIs on API Gateway

[Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs) is an API management system that helps you secure, monitor, analyze, and set quotas on your APIs. Endpoints uses the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) or [Extensible Service Proxy V2 (ESPv2)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) to host your APIs.

When using Endpoints, you have three options for how you define your API:

  * [Cloud Endpoints for OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi)
  * [Cloud Endpoints for gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)
  * [Cloud Endpoints Frameworks for the App Engine standard environment](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



## Develop APIs with API Gateway

Both Endpoints and API Gateway supports API that are described using the OpenAPI specification, [OpenAPI 2.0](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) or [OpenAPI 3.x](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md). If you have used OpenAPI to define your Endpoints APIs, this means that you can also deploy your Endpoints APIs on API Gateway.

**Note:** API Gateway also supports Cloud Run APIs described with gRPC service definitions and configurations.

## Deploy Endpoints OpenAPI specs on API Gateway

API Gateway supports the same OpenAPI spec definition format and options as supported by [Cloud Endpoints for OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi). That means you can use the same security, quota, and other definitions from your Endpoints OpenAPI specs to define an API in API Gateway.

The only difference between Endpoints and API Gateway is how they process the `host` property in the OpenAPI spec definition:

  * **In Endpoints** , set the `host` property to the hostname portion of the URL created when you deployed ESP or ESPv2, where ESP or ESPv2 is the service used to host your Endpoints API.
  * **In API Gateway** , omit the `host` or set it to the DNS name of the deployed API. API providers often set it to the DNS name when sharing the OpenAPI spec with their API consumers. However, API Gateway does not enforce the value of the `host` property.



For example, the following is a portion of an OpenAPI definition used by Endpoints to define an API to access a backend service deployed on Cloud Run functions: 

### OpenAPI 2.0
    
    
    swagger: '2.0'
    info:
      title: Cloud Endpoints + GCF
      description: Sample API on Cloud Endpoints with a Google Cloud Functions backend
      version: 1.0.0
    host: HOST
    schemes:
      - https
      ...

### OpenAPI 3.x
    
    
    openapi: 3.0.4
    info:
      title: Cloud Endpoints + GCF
      description: Sample API on Cloud Endpoints with a Google Cloud Functions backend
      version: 1.0.0
    servers:
    - url: https://HOST
      x-google-endpoint: {}
    ...

For more on creating the OpenAPI spec for your API definition, see [OpenAPI overview](https://docs.cloud.google.com/api-gateway/docs/openapi-overview).

## What's next

  * [API Gateway Deployment Model](https://docs.cloud.google.com/api-gateway/docs/deployment-model)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
