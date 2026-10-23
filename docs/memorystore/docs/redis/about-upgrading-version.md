---
url: https://docs.cloud.google.com/memorystore/docs/redis/about-upgrading-version/
title: About upgrading the Redis version of an instance \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:13.693235+00:00
---

# About upgrading the Redis version of an instance  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/about-upgrading-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  About upgrading the Redis version of an instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how a Memorystore for Redis instance behaves during a version upgrade, how an upgrade affects your application, and when to upgrade. For more information about how to upgrade the instance's version, see [Upgrade the Redis version of an instance](https://docs.cloud.google.com/memorystore/docs/redis/upgrading-instance-version).

Depending on the instance's tier, upgrading the version can have performance and storage implications for your application. Current memory usage also limits when you can upgrade the instance.

## Best practices for upgrading an instance's version

This section provides guidance for upgrading the version of an instance.

  * Upgrade the instance to version 7.0 and later because Certificate Authority rotation no longer drops connections. For more information, see [Certificate Authority rotation](https://docs.cloud.google.com/memorystore/docs/redis/about-in-transit-encryption#certificate_authority_rotation).

  * Before you upgrade, export the instance's data. For more information, see [Export data from a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/export-data).

  * To improve the speed and reliability of the upgrade for Standard Tier instances, perform the upgrade during periods of low instance traffic. For more information about monitoring instance traffic, see [Monitor instances](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances).

  * When you upgrade a Standard Tier instance, keep the instance write load to a minimum. A high write load might cause upgrades to take significantly longer or fail.

  * To manage the memory of the instance during the upgrade, follow our best practices for memory management. For more information, see [Memory management best practices](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices).

  * To understand how the new version affects your application, review the supported versions. For more information, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions).




## Version upgrade behavior

A version upgrade preserves data for both Basic and Standard Tier instances. Upgrading an instance's version causes a short connection reset of a couple of minutes or less, making the instance temporarily unavailable. You might also experience a delay of several minutes where core metrics don't appear.

After the upgrade completes, the instance becomes fully available and metrics reporting resumes. To reconnect to the instance, incorporate retry logic in your application's code. The IP address and connection string remain the same.

Because of the short connection reset, a small amount of stale or inconsistent data might not write to or update the cache while the instance is unavailable.

### Write load during an upgrade

To minimize the performance impact on your application, upgrade the instance during a period of low traffic. A high write load or high memory pressure might cause the upgrade to take significantly longer or fail. For more information, see [Scaling and version upgrade operations](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#scaling_and_version_upgrade_operations).

### Expired keys

When you upgrade a Standard Tier instance, Memorystore for Redis doesn't sync expired keys. If you have expired keys in the instance before you upgrade, then you have fewer keys after the upgrade completes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
