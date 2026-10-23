---
url: https://docs.cloud.google.com/api-gateway/docs/api-hub-overview/
title: Centralize API management using API hub \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:55.590406+00:00
---

# Centralize API management using API hub  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/api-hub-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Centralize API management using API hub

This page describes how to centralize the management of your organization's APIs using Apigee API hub.

## Overview

[Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) provides a centralized catalog, governance, and lifecycle management layer for all your organization's APIs, regardless of where they are deployed. 

Connect API Gateway to API hub to enable seamless publishing of [API metadata](https://docs.cloud.google.com/api-gateway/docs/api-hub-view-apis#api-metadata) from your API Gateway project to API hub. This integration provides a centralized, unified view of your APIs across different gateways, simplifying API discovery, governance, and management.

Key benefits include:

  * **Centralized API discovery:** All your API Gateway APIs are discoverable in API hub alongside APIs from other sources.
  * **Enhanced visibility:** Gain insights into your API landscape with consolidated metadata.
  * **Streamlined management** : Simplify API governance and lifecycle management across your diverse API ecosystem.



## How it works

The API Gateway connection with API hub establishes a secure and automated channel for your API information to flow from your API Gateway project to API hub.

Once connected, API Gateway continuously monitors for changes in your API Gateway APIs (such as new deployments or modifications) and automatically pushes these updates to API hub. This seamless data flow ensures that API hub always reflects an up-to-date and comprehensive view of the APIs managed within API Gateway.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
