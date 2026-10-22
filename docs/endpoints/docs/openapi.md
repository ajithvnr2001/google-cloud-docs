---
url: https://docs.cloud.google.com/endpoints/docs/openapi/
title: Cloud Endpoints for OpenAPI \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:06.090246+00:00
---

# Cloud Endpoints for OpenAPI  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Cloud Endpoints for OpenAPI Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Endpoints is an API management system that helps you secure, monitor, analyze, and set quotas on your APIs using the same infrastructure Google uses for its own APIs. Endpoints works with the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) and the [Extensible Service Proxy V2](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) (ESPv2) to provide API management. You can find out more about Endpoints, ESP, and ESPv2 in [About Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints).

Endpoints supports APIs that are described using OpenAPI 2.0 and OpenAPI 3.x of the OpenAPI Specification (formerly the [Swagger Specification](https://swagger.io/docs/specification/about/) (formerly known as the Swagger spec)—the industry standard for defining REST APIs.

If you are unfamiliar with the OpenAPI Specification, see [OpenAPI Overview](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview). To learn more about supported versions, see [Supported OpenAPI versions](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview#supported-openapi-versions).

This documentation set shows you how to use Endpoints with OpenAPI. For documentation on the other Endpoints options, see [All Endpoints Docs](https://docs.cloud.google.com/endpoints/docs).

To get started, we recommend the following path through the documentation:

  1. To see Endpoints features in action, do the [Quickstart for Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/deploy-api), which uses scripts to deploy a sample API to the App Engine flexible environment.

  2. Now you need to decide which compute platform you want to use for your API. To help you make that decision, see [Choosing a Computing Option](https://docs.cloud.google.com/docs/choosing-a-compute-option), and see the Supported compute platforms section below.

  3. After you have decided on the backend for your API, walk through a [tutorial](https://docs.cloud.google.com/endpoints/docs/openapi/tutorials) for your preferred compute platform.




## Supported compute platforms

Endpoints for OpenAPI depends on either ESP or ESPv2 for API management. Both ESP and ESPv2 are Open Source projects and are available to you in the following ways:

  * A container in Artifact Registry. 
    * See the [ESP release notes](https://github.com/cloudendpoints/esp/releases) for the current ESP Docker image.
    * See the [ESPv2 release notes](https://docs.cloud.google.com/github.com/GoogleCloudPlatform/esp-v2/releases) for the current ESPv2 Docker image.
  * Source code in GitHub. 
    * See the [ESP README](https://github.com/cloudendpoints/esp/blob/master/README.md) for details on building ESP.
    * See the [ESPv2 README](https://github.com/GoogleCloudPlatform/esp-v2/blob/master/README.md) for details on building ESPv2.



You can run the ESP container on the following:

  * App Engine flexible environment
  * Compute Engine
  * Kubernetes, including Google Kubernetes Engine
  * A [Linux or macOS computer or another platform](https://docs.cloud.google.com/endpoints/docs/openapi/running-esp-localdev)



You can run the ESPv2 container on the following:

  * App Engine
  * Cloud Run functions
  * Cloud Run
  * Knative serving
  * GKE
  * Compute Engine
  * Kubernetes



See [About Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints) for more.

On the [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible), ESP is automatically deployed for you when you add a few lines to your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/reference/app-yaml) file. For more information, see [Deploying your API and ESP](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend#deploying_your_api_and_esp). ESPv2 does not support App Engine flexible environment.

For the [App Engine standard generation 1 environment](https://docs.cloud.google.com/appengine/docs/standard), you must use [Endpoints Frameworks](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks). If you instead deploy the container to one of the compute options above, you can proxy to either generation of App Engine standard runtime.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
