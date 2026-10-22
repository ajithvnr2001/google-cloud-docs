---
url: https://docs.cloud.google.com/api-gateway/docs/quotas-overview/
title: About quotas \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:01.945775+00:00
---

# About quotas  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/quotas-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About quotas

API Gateway provides quotas, which let you control the rate at which applications can call your API. Setting a quota lets you specify usage limits to protect your API from an excessive number of requests from calling applications. The excessive requests might have been caused by a simple typo or from an inefficiently designed system that makes needless calls to your API. 

Regardless of the cause, blocking traffic from a source once it reaches a certain level is necessary for the overall health of your API. By setting a quota, you ensure that one application cannot negatively impact other applications that use your API.

**Note:** For API Gateway, you control quotas as described in the Cloud Endpoints doc at [About quotas](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-overview).

## Quotas apply to the whole API

You define quota metrics and limits in an API config, but API Gateway applies them to the **API** that owns the API config, not to that API config alone. Each time you create an API config, the metrics and limits it declares replace the ones declared by the API's previous API configs. Only the metrics and limits from the most recently created API config are enforced.

This has two consequences when an API has more than one API config deployed:

  * Changing the _value_ of a limit changes it for every gateway of the API, including gateways that serve an earlier API config.

  * Renaming or removing a _metric_ leaves an invalid quota configuration behind on any gateway that still serves an earlier API config. Requests to the quota-enforced methods of those gateways fail with an HTTP `500` error and the message `Failed to call Service Control Quota.`


**Caution:** Audit your quota metrics and limits to ensure that they are consistent across all active configurations. If you can't keep metric names consistent, update every gateway of the API to the most recently created API config.

To find and correct an invalid quota configuration, see [API request returns an HTTP 500 error for a quota-enforced method](https://docs.cloud.google.com/api-gateway/docs/troubleshoot#invalid_quota_config).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
