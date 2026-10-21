---
url: https://docs.cloud.google.com/memorystore/docs/redis/upgrade-redis-version/
title: Upgrade the Redis version of an instance \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:51.362140+00:00
---

# Upgrade the Redis version of an instance  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/upgrade-redis-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Upgrade the Redis version of an instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to upgrade the Redis version of a Memorystore for Redis instance. For a list of available versions, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions). For more information about instance behavior during an upgrade operation, see [Version upgrade behavior](https://docs.cloud.google.com/memorystore/docs/redis/version-upgrade-behavior).

## Upgrading the instance version

**Important:** You can upgrade the version of an instance to any newer version. For example `3.2` to `7.0`.

### Console

  1. Go to the Memorystore for Redis page in the Google Cloud console   
[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)
  2. Click the instance ID of the instance you want to upgrade
  3. In the **Configuration** section, next to **Redis Version** , click **UPGRADE**
  4. Click the **UPGRADE** button in the dialog to upgrade your instance



### gcloud

To upgrade the Redis version of your instance, enter the following command, replacing variables with appropriate values:
    
    
    gcloud redis instances upgrade instance-id --redis-version=version --region=region

Where:

  * instance-id is your instance ID
  * version is the version you want to upgrade to: 
    * Acceptable values are: `redis_4_0`, `redis_5_0`, `redis_6_x`, `redis_7_0`, and `redis_7_2`
  * region is the region in which the instance is provisioned



For example:
    
    
    gcloud redis instances upgrade myinstance --redis-version=redis_7_0 --region=us-central1

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
