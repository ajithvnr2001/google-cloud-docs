---
url: https://docs.cloud.google.com/memorystore/docs/redis/initiate-manual-failover/
title: Initiate a manual failover \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:39.038153+00:00
---

# Initiate a manual failover  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/initiate-manual-failover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Initiate a manual failover Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** You can only initiate a manual failover using the gcloud CLI tool.

This page describes how to initiate a **manual failover** for a standard tier Memorystore for Redis instance. The manual failover feature allows you to test how normal failovers affect your application.

For an overview of this feature, see [Manual failover](https://docs.cloud.google.com/memorystore/docs/redis/manual-failover-overview).

## Initiating a failover

**Warning:** Using the `--data-protection-mode=force-data-loss` mode may cause significant data loss. See [Manual failover](https://docs.cloud.google.com/memorystore/docs/redis/manual-failover-overview) to learn the appropriate scenarios for using the `force-data-loss` mode.

  1. Open a terminal window

  2. Use the `gcloud config` command to set your default project: 
         
         gcloud config set core/project PROJECT_ID
         

  3. Use the following command to initiate a failover: 
         
         gcloud redis instances failover INSTANCE_NAME
         




## Optional data protection mode

The two available data protection modes are:

  * `limited-data-loss` mode (default).
  * `force-data-loss` mode.



To set the data protection mode, use one of the following commands:
    
    
    gcloud redis instances failover INSTANCE_NAME --data-protection-mode=limited-data-loss
    

or
    
    
    gcloud redis instances failover INSTANCE_NAME --data-protection-mode=force-data-loss
    

## How data protection modes work

The `limited-data-loss` mode minimizes data loss by verifying that the difference in data between the primary and replica is below 30 MB before initiating the failover. The offset on the primary is incremented for each byte of data that must be synchronized to its replicas. In the `limited-data-loss` mode, the failover will abort if the greatest offset delta between the primary and each replica is 30MB or greater. If you can tolerate more data loss and want to aggressively execute the failover, try setting the data protection mode to `force-data-loss`.

The `force-data-loss` mode employs a chain of failover strategies to aggressively execute the failover. It does not check the offset delta between the primary and replicas before initiating the failover; you can potentially lose more than 30MB of data changes.

See [Manual failover](https://docs.cloud.google.com/memorystore/docs/redis/manual-failover-overview) for additional information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
