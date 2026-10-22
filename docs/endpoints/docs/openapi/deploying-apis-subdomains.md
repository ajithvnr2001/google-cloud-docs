---
url: https://docs.cloud.google.com/endpoints/docs/openapi/deploying-apis-subdomains/
title: Serving multiple APIs from a domain \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:44.016764+00:00
---

# Serving multiple APIs from a domain  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/deploying-apis-subdomains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Serving multiple APIs from a domain Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/deploying-apis-subdomains "View this page for the Cloud Endpoints gRPC docs")

This page shows you how to run multiple independent APIs on your own custom domain (for example, `example.com`).

## Before you begin

To use a custom domain, follow the instructions in [Verifying a domain name](https://docs.cloud.google.com/endpoints/docs/openapi/verify-domain-name). During that process, you must confirm ownership of the domain. This confirmation lets you deploy and service APIs on any of its subdomains.

For example, if domain ownership is established for `example.com`, service names can include subdomains of `example.com` such as `api.example.com` or `catalog.api.example.com`.

## Deploying an API on a subdomain

The following example deploys the API to the subdomain `first_api.example.com`:

  1. Set the `host` field of your OpenAPI document to `first_api.example.com` and set the other fields as described in [Configuring Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints).

  2. [Deploy the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config).

  3. [Deploy the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend).




Now you can send requests to `first_api.example.com` and view graphs of those requests on the [**Endpoints** > **Services** page](https://console.cloud.google.com/endpoints).

## Deploying your next API

To deploy another API, repeat the preceding steps, changing the subdomain `first_api.example.com` to the subdomain you are using for the next API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
