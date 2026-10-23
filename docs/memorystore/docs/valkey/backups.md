---
url: https://docs.cloud.google.com/memorystore/docs/valkey/backups/
title: About backups \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:59.882574+00:00
---

# About backups  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About backups Stay organized with collections  Save and categorize content based on your preferences. 

Backups let you restore your Memorystore for Valkey instances to a specific point in time. In addition, you can use backups to export and analyze data.

Backups are useful for the following scenarios:

  * **Disaster recovery** : use backups as part of a disaster recovery plan. If a disaster occurs, then you can restore your data to a new Memorystore for Valkey instance.

  * **Data migration** : migrate data between different Memorystore for Valkey instances. You can consolidate data or move it to a different region. You can also restore backups from Memorystore for Valkey instances.

  * **Data sharing** : share data between different teams or applications, enabling collaboration, offline data analytics, and data exchange.

  * **Compliance** : create periodic backups of cache data for compliance purposes.




## Backups and backup collections

A _backup_ is a point-in-time snapshot of your data. Backups are organized into backup collections. A _backup collection_ includes all backups for a Memorystore for Valkey instance. If you delete an instance, then Memorystore for Valkey doesn't delete the corresponding backup collection automatically.

You can set a time to live (TTL) for a backup by setting a retention period. After the backup exceeds its TTL, Memorystore for Valkey deletes the backup automatically.

To recover data in a backup, you can [create an instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances) and seed the instance with data from the backup. However, you can't import data into an existing instance.

## Automated and on-demand backups

You can create backups in the following ways:

  * **Automated backups** (Recommended): configure a backup schedule for an instance. As a result, Memorystore for Valkey initiates periodic backups for the instance.

  * **On-demand backups** : initiate a backup operation that begins immediately.




For more information about setting an automated backup schedule or initiating a backup, see [Manage backups](https://docs.cloud.google.com/memorystore/docs/valkey/manage-backups).

## Costs

Based on the size of a backup and the region where the backup is located, you're charged storage costs for the backup. For each backup, there's a minimum 24-hour charge. For more information, see [Memorystore for Valkey pricing](https://cloud.google.com/memorystore/valkey/pricing#backups-pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
