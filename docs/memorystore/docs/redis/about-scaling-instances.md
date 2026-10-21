---
url: https://docs.cloud.google.com/memorystore/docs/redis/about-scaling-instances/
title: About scaling instances \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:29.065803+00:00
---

# About scaling instances  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/about-scaling-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  About scaling instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how your Memorystore for Redis instance behaves during scaling. To learn how to scale a Redis instance, see [Scale Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/scaling-instances).

Depending on the instance's tier, scaling an instance has performance and storage implications for your application. There are also some limitations to scaling instances based on the amount of memory that is currently in use. This page describes how scaling an instance can affect your application and when you can scale an instance.

## Best practices for scaling an instance

  * For Standard Tier instances, to increase the speed and reliability of your scaling operation, scale your instance during periods of low instance traffic. To learn how to monitor instance traffic, see [Monitoring Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances).

  * When reducing a Standard Tier instance's capacity, you must choose a size greater than the amount of data being stored or scaling fails.

    * For example, if your have a 10 GB instance that has 5.5 GB of data stored in it, you can resize the instance to a minimum of 6 GB. The amount of storage your instance uses is visible on its details page in the Google Cloud console.



## Instance scaling behavior

During scaling for both Basic and Standard Tier instances, data is preserved. When you scale an instance, the instance undergoes a short connection reset of a couple of minutes or less. We recommend that applications incorporate retry logic in the code so that they can reconnect to the instance. The IP address and connection string remain the same.

Additionally, there might be a gap of several minutes when the [core metrics](https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances#monitoring-instances-console) for the instance don't appear. Aside from the brief connection reset, the instance remains available during this time, and metrics reporting resumes after the time interval completes. There might be a small amount of stale or inconsistent data that doesn't write or update to the cache for the short amount of time that the instance is unavailable.

If you issue a write during the connection break, Memorystore returns the error `READONLY You can't write against a read only replica`. This error is transient, and only lasts a few seconds. It resolves once the scaling operation completes.

### Write load when scaling

You should scale an instance during a period of low instance traffic to minimize the performance impact on your application. A high write load, or high memory pressure, can cause an scaling operation to take significantly longer and can cause the operation to fail. For more information see [Scaling and version upgrade operations](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#scaling_and_version_upgrade_operations).

### Expired keys

When you scale a Standard Tier instance, expired keys are not synced. If you have expired keys in your Redis instance before you scale, you will have fewer keys after the instance is scaled.

## Best practices

To help you scale the capacity for your instance, we recommend the following best practices:

  * **Choose when to scale** : to increase the speed and reliability of scaling your instance, scale it during low periods of traffic. To learn how to monitor instance traffic, see [Monitor instances](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances).
  * **Account for stored data when scaling in** : if you scale in your instance, then you must choose a size that's greater than the amount of data that the instance stores. For example, if you have a 10-GB instance that has 5.5 GB of stored data, then resize the instance to 6 GB or greater.
  * **Retry when you can't scale** : resource availability changes frequently. If you can't scale your instance because of a temporary resource constraint, then try to scale the instance later.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
