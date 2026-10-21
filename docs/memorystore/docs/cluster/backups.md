---
url: https://docs.cloud.google.com/memorystore/docs/cluster/backups/
title: Backups overview \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:11.786623+00:00
---

# Backups overview  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Backups overview Stay organized with collections  Save and categorize content based on your preferences. 

Backups give you the ability to restore data to a point in the past, as well as to export and analyze data. Backups are useful for the following scenarios:

  * **Disaster recovery** : use backups as part of a disaster recovery plan. In the event of a disaster, you can restore data to a new cluster in Memorystore for Redis Cluster. Backup schedules provide more robust protection than ad hoc exports.

  * **Data migration** : migrate data between different clusters to consolidate resources or move data to a different region.

  * **Data sharing** : share data across different teams or applications to enable collaboration, offline data analytics, and data exchange.

  * **Compliance** : create periodic backups of cache data to meet compliance requirements.




You can't import Memorystore for Redis Cluster backups into Memorystore for Redis instances because they contain multiple RDB files.

## Backups and backup collections

A backup is a point-in-time snapshot of your data. You can organize backups into backup collections. A backup collection includes all backups for a cluster. When you delete a cluster, Memorystore for Redis Cluster doesn't delete the corresponding backup collection automatically.

You can set a time to live (TTL) on a backup by configuring a retention period. After a backup exceeds its TTL, Memorystore for Redis Cluster deletes it automatically.

To recover data from a backup, you must create a cluster and restore the data to it. You can't import backup data into an existing cluster.

## Automated and on-demand backups

You can initiate backups in the following ways:

  * **Automated backups** (Recommended): configure a backup schedule to initiate periodic backups for a cluster.

  * **On-demand backups** : initiate a backup operation that begins immediately.




To learn how to set an automated backup schedule or to initiate a backup, see [Manage backups](https://docs.cloud.google.com/memorystore/docs/cluster/manage-backups).

## Pricing

You're charged storage costs for each backup based on its size. For each backup, you're charged a minimum of 24 hours. For more information, see [Memorystore for Redis Cluster pricing](https://docs.cloud.google.com/memorystore/cluster/pricing#backups-pricing).

## What's next

  * Learn how to [manage backups](https://docs.cloud.google.com/memorystore/docs/cluster/manage-backups).
  * Learn about [persistence](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
