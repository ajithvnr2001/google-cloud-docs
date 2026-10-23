---
url: https://docs.cloud.google.com/service-infrastructure/docs/quotas/
title: Quotas \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:21.664218+00:00
---

# Quotas  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Resources ](https://docs.cloud.google.com/service-infrastructure/docs/resources)



Send feedback 

#  Quotas Stay organized with collections  Save and categorize content based on your preferences. 

This page contains quota and rate limit information for each version of the following Service Infrastructure APIs:

  * The Service Management API
  * The Service Control API
  * The Service Networking API
  * The Service Consumer Management API

**Note:** For Service Infrastructure quota information for the Service Usage API, see [Quotas](https://docs.cloud.google.com/service-usage/docs/quotas).

## Service Management API Quota

This section describes the quota limits for the Service Management API. To request a quota increase, visit the [**Quotas**](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console.

API Call Type | Limit  
---|---  
All | 120 API calls per minute  
  
## Service Control API Quota

This section describes the quota limits for the Service Control API.

There is a limit of 6,000,000 quota units per minute per [service producer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#producer) project. One quota unit is consumed for each:

  * Call to [`services.check`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check).
  * Operation reported via [`services.report`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report).
  * Call to [`services.allocateQuota`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota).



## Service Networking API Quota

Service Networking private connections are implemented as VPC Network Peering connection and have the same limits. For more information, see the Limits in the [Using VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#limits) documentation.

## Service Consumer Management API Quota

This section describes the quota limits for the Service Consumer Management API. Fill out the [Service Consumer Management API Quota Request](https://goo.gl/forms/A8FZ5bvGP47vlquJ3) form if you need to increase any of the quotas listed in this document.

API Call Type | Limit  
---|---  
Read-only Calls | 120 API calls per minute  
Write Calls | 60 API calls per minute  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
