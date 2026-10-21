---
url: https://docs.cloud.google.com/memorystore/docs/memcached/quotas/
title: Quotas and limits \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:01:01.706659+00:00
---

# Quotas and limits  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/quotas/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/memcached/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains the resource capacity limits and per-second API request quotas for Memorystore for Memcached.

**Note:** There is no limit or quota for the total number of queries/operations made to your Memcached instance.

## Regional limits

Limit | Value  
---|---  
Nodes per region | 100  
vCPUs available per region | 2000  
Total memory available per region | 10 TiB  
  
To request a higher quota for a region, see [Regional capacity quota increases](https://docs.cloud.google.com/memorystore/docs/memcached/quotas#regional_capacity_quota_increases).

## Node limits

Limit | Value  
---|---  
Connected clients per node. | 65,000  
  
## Management operations quota

The per-second quota for management operations (instance `create`, `delete`, `update` etc.) for Memorystore for Memcached is as follows, and is subject to change:

Management API Requests Quota | Value  
---|---  
API read requests per 100s | 500 (5 QPS)  
API write requests per 100s | 500 (5 QPS)  
  
This quota is for `memcache.googleapis.com` requests/operations, not OSS Memcached protocol/commands. These limits apply to each Google Cloud console project and are shared across all applications and IP addresses using that project.

### Regional quota increases

To request a higher regional capacity for your project, follow these steps:

  1. Go to the **Quotas** page in the Google Cloud console.   
[Quotas](https://console.cloud.google.com/iam-admin/quotas)
  2. From the **Services** drop down, select **Memorystore for Memcached API**.
  3. From the list of quotas, click the checkbox next to your desired quota for your desired region.
  4. Click the **Edit Quotas** button.
  5. In the edit pane, enter your contact information, then click **Next**.
  6. Enter your desired quota, then click **Done**.
  7. Click **Submit request**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
