---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-aof-persistence/
title: About AOF persistence \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:41.347300+00:00
---

# About AOF persistence  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-aof-persistence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About AOF persistence Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Append Only File (AOF) persistence for Memorystore for Valkey.

Memorystore for Valkey also supports Redis Database (RDB) persistence, but you must choose either the AOF or the RDB persistence mode, because you can't enable both persistence modes at the same time. For more information about choosing between the two modes, see [Persistence overview](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview).

To ensure that your instance remains resilient during [maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance) or unexpected failures, we recommend that in addition to enabling AOF persistence for the instance, you use a [highly available instance](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas).

To learn how to enable, disable, and monitor AOF persistence, see [Manage persistence](https://docs.cloud.google.com/memorystore/docs/valkey/manage-persistence).

## AOF persistence overview

The AOF persistence mode prioritizes data durability. It durably stores data by recording every write command to a log file called the AOF file. If a system failure or restart occurs, the server replays AOF file commands sequentially to restore your data. Unlike RDB persistence, AOF persistence can't be paused.

If you [enable](https://docs.cloud.google.com/memorystore/docs/valkey/manage-persistence#enable_aof_persistence_for_an_existing_instance) or [disable](https://docs.cloud.google.com/memorystore/docs/valkey/manage-persistence#disable_aof_persistence) AOF persistence for an instance, then you might need to perform maintenance on the instance.

### Sync setting

The sync setting (`appendfsync`) for the AOF persistence mode determines how often the cached data in memory is saved to durable storage. We recommend keeping the sync setting at 1 second, which is the default. Syncing every second provides the best compromise between the instance's performance and the durability of the data.

Before the AOF logs are saved to durable storage, they are stored in memory by the operating system, and if a system failure or restart occurs during this time, the writes in memory can be lost. The sync setting lets you choose how often data is saved to durable storage, and provides the following options:

  * `always` \- This option saves data to storage for every write.
  * `everysec` \- This option saves data to storage every second.
  * `no` \- This option relies on the operating system to flush data to storage on its own schedule, which typically happens every 30 seconds.



Choosing to sync for every write provides the best data durability, however this comes with a performance tradeoff. We recommend syncing every second, which provides both good data durability and performance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
