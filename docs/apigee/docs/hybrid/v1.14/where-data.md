---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/where-data/
title: Where is your data stored? \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:46:56.499469+00:00
---

# Where is your data stored?  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/where-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Where is your data stored? Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/where-data.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/where-data.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/where-data.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/where-data.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/where-data.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/where-data.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/where-data.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/where-data.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/where-data.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/where-data.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/where-data.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/where-data.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/where-data.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/where-data.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/where-data.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/where-data.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/where-data.html)



This section explains which data is stored in your local runtime plane for Apigee hybrid, and which data is maintained in the management plane (in the Apigee Cloud).

## Data stored in the runtime plane

You manage the runtime plane services, including data stored in the runtime plane. The following data is stored by the runtime Cassandra (and accessed from or by the management plane through MART):

Type of data | Description  
---|---  
Key management system (KMS) | KMS data includes API products, developers, developer apps, OAuth tokens (including access tokens, refresh tokens, and authorization codes), and API keys.  
Key value map (KVM) | Any data that can be created or managed with KVM policies.  
Quota | Quota definitions, buckets, and counters.  
Environment cache | All cached data.  
  
## Data stored in the management plane

The following data is stored in the management plane:

  * [API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy)
  * [TargetServers](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#baseconfiguration-baseconfigurationelements)
  * [Truststores and keystores](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores)



You create these entities in the management plane (for example, in the hybrid UI or with the [Apigee APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)), and the related data is replicated in the runtime plane by the Synchronizer, which pulls this data down and stores it in the runtime plane where the MP can access it.

For more information, see [Synchronizer](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/what-is-hybrid#synchronizer).

### Management plane data and data residency

If your installation is using [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) you can specify the region in which this data is stored. See [Using data residency with Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/using-data-residency-with-apigee-hybrid). 

## Data sent from the runtime plane to the management plane

The runtime plane sends the following data (asynchronously) to the management plane:

  * Analytics
  * Deployment status events
  * Debug data



## Data sent to Stackdriver for your Google Cloud project

  * Log data
  * Metrics



## Data stored only in the management plane

  * Audit logs
  * RBAC
  * Users



For information about the various types of data generated by the hybrid services, and the mechanisms by which hybrid collects and surfaces this data to you, see [Data collection overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/data-collection-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
