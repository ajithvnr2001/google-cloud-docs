---
url: https://docs.cloud.google.com/memorystore/docs/redis/product-constraints/
title: Product constraints \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:39.238732+00:00
---

# Product constraints  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/product-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  Product constraints Stay organized with collections  Save and categorize content based on your preferences. 

This page describes product constraints that you should take into consideration when planning and implementing your Memorystore for Redis solution.

## Replication backlog for Standard Tier instances

Standard Tier Memorystore for Redis instances reserve 10% of primary-node memory for replication backlog usage. When [monitoring your instance](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances), this backlog appears in the **used memory** metric, even if the instance is empty.

## You can only run one admin operation at a time

Examples of Memorystore for Redis admin operations are resizing, renaming, and changing other Redis instance configurations. Only one of these commands can be run at a time. You will have to wait for any admin operation to complete before you can run another one. During these operations, you can still run Redis commands and access the data in the Redis instance.

## Quotas and limits

For information on the Memorystore for Redis instance capacity quota and API requests quota, see [Quotas and Limits](https://docs.cloud.google.com/memorystore/docs/redis/quotas).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
