---
url: https://docs.cloud.google.com/cortex/quotas/
title: Quotas and system limits \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:47.349462+00:00
---

# Quotas and system limits  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Resources ](https://docs.cloud.google.com/cortex/docs/resources-v7)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and system limits

This document lists the quotas and system limits that apply to Google Cloud Cortex Framework.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

## Quotas

Cortex Framework is built on top of different Google Cloud products. For detailed information, see the respective Google Cloud products quotas pages:

  * [Cloud Storage](https://docs.cloud.google.com/storage/quotas)
  * [BigQuery](https://docs.cloud.google.com/bigquery/quotas)
  * [Secret Manager](https://docs.cloud.google.com/secret-manager/quotas)
  * [Cloud Build](https://docs.cloud.google.com/build/quotas)
  * [Dataflow](https://docs.cloud.google.com/dataflow/quotas)
  * [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/quotas)
  * [BigQuery](https://docs.cloud.google.com/bigquery/quotas)
  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/quotas)
  * [Vertex AI](https://docs.cloud.google.com/vertex-ai/quotas)



When installing multiple Cortex Framework workloads, you need to increase the following Cloud Build quotas:

Resource | Description | Default limit | Can be increased | Scope  
---|---|---|---|---  
CPU | Number of concurrent Build and Operation Get requests | 600 | Yes. When this quota is filled, it can be increased up to 1200. | Per minute  
CPU | Number of concurrent Build and Operation Get requests | 600 | Yes. When this quota is filled, it can be increased up to 1200. | Per user  
  
## Request a quota adjustment

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
