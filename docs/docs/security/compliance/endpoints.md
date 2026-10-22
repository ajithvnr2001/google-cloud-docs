---
url: https://docs.cloud.google.com/docs/security/compliance/endpoints/
title: Google Cloud API endpoint overview \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:59.353488+00:00
---

# Google Cloud API endpoint overview  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Google Cloud API endpoint overview Stay organized with collections  Save and categorize content based on your preferences. 

An API endpoint, or service endpoint, is a URL that specifies the network address of a Google Cloud API service, such as `bigquery.googleapis.com`. Google Cloud services allow access to resources using different types of API endpoints, including regional, multi-regional, global, and locational. Support for each type of endpoint depends on the service.

This document briefly describes each type of endpoint to provide clarity about how they differ and guidance about which type of endpoint to use.

## Regional endpoints

Regional API endpoints provide access to Google Cloud services through an API endpoint that is scoped to a single Google Cloud region. Traffic sent to a regional endpoint is processed and TLS terminated entirely within the specified region.

For most Google Cloud services, you can use regional endpoints to work with regional resources within the specified region. Operations on global resources, multi-regional resources, and out-of-region regional resources are typically not supported from the regional endpoint.

Regional API endpoints specify the location as a subdomain. Public regional endpoints have the following format:

`SERVICE.REGION.rep.googleapis.com`

  * `SERVICE`: the name of the Google Cloud service, such as `storage`, `compute`, or `bigquery`.
  * `REGION`: the Google Cloud region name, such as `us-central1` or `europe-west1`.



Private regional API endpoints have the following format:

`SERVICE.REGION.p.rep.googleapis.com`

  * `SERVICE`: the name of the Google Cloud service, such as `storage`, `compute`, or `bigquery`.
  * `REGION`: the Google Cloud region name, such as `us-central1` or `europe-west1`.
  * `.p.`: indicates a private target intended for Private Service Connect connectivity.



## Multi-regional endpoints

Multi-regional API endpoints provide access to Google Cloud services through an API endpoint that is scoped to a set of Google Cloud regions within the same country, such as the United States, India, or Canada, or jurisdiction, such as the European Union. Traffic sent to a multi-regional endpoint is processed and TLS terminated entirely within the specified jurisdiction.

For most Google Cloud services, you can use multi-regional endpoints to work with multi-regional resources within the specified multi-region. Operations on global resources, regional resources, and multi-regional resources from other jurisdictions are typically not supported.

Multi-regional API endpoints specify the jurisdiction as a subdomain. Public multi-regional endpoints have the following format:

`SERVICE.MULTI_REGION.rep.googleapis.com`

  * `SERVICE`: the name of the Google Cloud service, such as `storage`, `compute`, or `bigquery`.
  * `MULTI_REGION`: the Google Cloud multi-region name, such as `us` or `eu`.



Private multi-regional API endpoints have the following format:

`SERVICE.MULTI_REGION.p.rep.googleapis.com`

  * `SERVICE`: the name of the Google Cloud service, such as `storage`, `compute`, or `bigquery`.
  * `MULTI_REGION`: the Google Cloud name of the multi-region, such as `us` or `eu`.
  * `.p.`: indicates a private target intended for Private Service Connect connectivity.



## Global endpoints

Global API endpoints don't specify the location in the URL hostname. These globally scoped endpoints provide high-availability service endpoints that terminate the TLS session as close to the client as possible, which minimizes latency when serving API calls from a dispersed client population over the internet. However, these endpoints don't provide any regional isolation or data residency compliance.

For applications that can handle global dependencies and need fast performance from Google's global network, you can use global endpoints.

Global endpoints have the following format:

`SERVICE.googleapis.com`

Where `SERVICE` is the name of the Google Cloud service, such as `storage`, `compute`, or `bigquery`.

## Locational endpoints

**Note:** Locational API endpoints are supported by a limited number of services, and their availability varies.

Regional API endpoints are replacing locational endpoints. Locational endpoints are regional or multi-regional service hostnames that you can use to access data in a given location.

However, locational endpoints don't support the following features:

  * Data residency compliant connections from on-premises through the internet
  * Failure domain isolation



Locational endpoints specify the location in the URL hostname and have the following format:

`LOCATION-SERVICE.googleapis.com`

  * `LOCATION`: the Google Cloud region name, such as `us-central1`, `europe-west1`, or `us`.
  * `SERVICE`: the name of the Google Cloud service, such as `storage`, `compute`, or `bigquery`.



## Reference documentation

  * Use the [Google Cloud CLI to manage regional endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints).
  * See the [`regionalEndpoints` REST documentation](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints).



## What's next

  * Learn [about regional and multi-regional endpoints](https://docs.cloud.google.com/docs/security/compliance/about-regional-endpoints).
  * [Access regional Google APIs through backends](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls).
  * See the Google Cloud [supported regional service endpoints](https://docs.cloud.google.com/docs/security/compliance/regional-service-endpoints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
