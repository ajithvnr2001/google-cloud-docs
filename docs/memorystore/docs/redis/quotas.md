---
url: https://docs.cloud.google.com/memorystore/docs/redis/quotas/
title: Quotas and limits \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:35.093766+00:00
---

# Quotas and limits  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/redis/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains the current resource capacity limits and per-second API request quotas for Memorystore for Redis.

## Instance limits

Memorystore for Redis enforces the following usage limits:

Limit | Value1  
---|---  
Databases per instance | 16  
Connected clients per instance for Basic Tier | 65,000  
Connected clients per instance for Standard Tier | 65,000  
Connected clients per instance for Standard Tier with read replicas | 65,000 for each node including the primary and read replicas  
  
1 For instances that use both [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/about-in-transit-encryption) and Redis version 6.x or earlier, connection limits can be lower. For more information, see [Connection limits for in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/about-in-transit-encryption#connection_limits_for_in-transit_encryption).

## Regional capacity quota

You can use the default per-project quota for Memorystore for Redis to provision 1 TB of Redis capacity in each region where the service is available.

Quota | Value  
---|---  
Data provisioned per region | 1 TB  
  
For example, if you provision three instances in your project with 300 GB each in `us-central1`, then you consume 900 GB out of the 1-TB quota for `us-central1`. With the default quota, you can provision an additional 100 GB in `us-central1`.

## Per-second API requests quota

**Note:**

  * You cannot request a quota increase for Memorystore for Redis API operations, such as instance `create`, `update`, and `export`. There is no limit to the number of Redis commands you can run, such as Redis `SET`, `GET`, and `DEL`.
  * Follow the [Exponential backoff recommendations](https://docs.cloud.google.com/memorystore/docs/redis/exponential-backoff) to reduce the number of API requests made if an error is encountered.



The per-second quota for Memorystore for Redis API requests/operations is as follows, and is subject to change:

API Requests Quota | Value  
---|---  
Create Redis instance requests per project per minute | 30  
API Requests per minute | 3,000  
  
Create Redis instance requests per project per minute includes create operations (`gcloud redis instances create`).

Memorystore for Redis API operations include:

  * Get operations (`gcloud redis instances describe`)
  * List operations (`gcloud redis instances list`)
  * Create operations (`gcloud redis instances create`)
  * Delete operations (`gcloud redis instances delete`)
  * Import and export operations (`gcloud redis instances import` and `gcloud redis instances export`)
  * Update operations (`gcloud redis instances update`)
  * Upgrade operations (`gcloud redis instances upgrade`)
  * Failover operations (`gcloud redis instances failover`)



This quota is for redis.googleapis.com requests/operations, not OSS Redis protocol/commands. These limits apply to each Google Cloud console project and are shared across all applications and IP addresses using that project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
