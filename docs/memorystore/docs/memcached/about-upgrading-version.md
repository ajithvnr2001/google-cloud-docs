---
url: https://docs.cloud.google.com/memorystore/docs/memcached/about-upgrading-version/
title: About upgrading the Memcached version of an instance \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:51.875018+00:00
---

# About upgrading the Memcached version of an instance  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/about-upgrading-version/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  About upgrading the Memcached version of an instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how your Memorystore for Memcached instance behaves during a version upgrade operation, how an upgrade operation can affect your application, and when you should run an upgrade operation. To learn how to upgrade an instance's Memcached version, see [Upgrade the Memcached version of an instance](https://docs.cloud.google.com/memorystore/docs/memcached/upgrade-memcached-version).

Upgrading an instance has performance and storage implications for your application.

## Best practices for upgrading an instance's Memcached version

Upgrade your instance during periods of low instance traffic to minimize the impact of the full cache flush caused by the upgrade operation. To learn how to monitor instance traffic, see [Monitor Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/monitor-instances).

## Version upgrade behavior

The Memcached instance undergoes a complete cache flush during a version upgrade operation. Multi-node instances are partially available during the upgrade operation. You cannot downgrade the instance to an earlier version once it has been upgraded.

An upgrade operation also causes the nodes to undergo a short connection reset of a couple minutes, or less. Applications should incorporate retry logic in the code to be able to reconnect to the nodes. The discovery endpoint and memcached node endpoints remain the same.

Because of the short term connection break, there may be a small amount of stale or inconsistent data that didn't write or update to the cache for the short amount of time the Memcached node was unavailable.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
