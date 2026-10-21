---
url: https://docs.cloud.google.com/dataproc-metastore/docs/version-policy/
title: Dataproc Metastore version support \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:00.089233+00:00
---

# Dataproc Metastore version support  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/version-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Dataproc Metastore version support Stay organized with collections  Save and categorize content based on your preferences. 

This page lists common integrations that Dataproc Metastore supports and the versions of the integrations that you can use.

## Apache Hive Metastore version support

When you [create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service), you can select the Hive metastore version to use in your service. If you don't select a version, Dataproc Metastore uses Hive version 3.1.2 by default.

Dataproc Metastore supports the following stable Hive patch versions:

  * 3.1.2
  * 2.3.6
  * 2.2.0
  * 1.2.2



### Upstream end-of-life version support

When a Hive Metastore version reaches end of life, it no longer receives upstream contributions. These end-of-life versions have limited support for the following:

  * Performance improvements.
  * Fixes for security issues.
  * New feature requests.



### Hive version support window

When Dataproc Metastore adds support for a new version of Hive, the previous versions are still supported for the following periods of time.

Months after initial Hive version release | New services | Existing services  
---|---|---  
0-12 | Supported | Supported  
12-24 | Not Supported | Supported  
24+ | Not supported | Not supported  
  
After a Hive version is deprecated, it's no longer supported.

## Managed Service for Apache Spark version support

When you [create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service), you can attach a Managed Service for Apache Spark cluster to your service.

Dataproc Metastore supports the following stable versions of Managed Service for Apache Spark:

Dataproc Metastore | Managed Service for Apache Spark  
---|---  
3.1.2 | 2._x_ and 1.5*  
2.3.6 | 1.5  
  
* Using Managed Service for Apache Spark version 1.5 with Dataproc Metastore 3.1.2 might result in backward compatibility issues. If you need to use these versions together, we recommend that you use the [auxiliary versions](https://docs.cloud.google.com/dataproc-metastore/docs/auxiliary-versions) feature. To support these versions together, you should set your primary version to Dataproc Metastore 3.1.2 and the auxiliary version to 2.3.6.

Managed Service for Apache Spark 3.x versions are incompatible with Dataproc Metastore.

## What's next

  * [Release channels](https://docs.cloud.google.com/dataproc-metastore/docs/release-channel)
  * [Service tiers](https://docs.cloud.google.com/dataproc-metastore/docs/service-tier)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
