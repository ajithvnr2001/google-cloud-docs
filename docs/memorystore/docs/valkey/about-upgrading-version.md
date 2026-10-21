---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-upgrading-version/
title: About upgrading the Valkey version of an instance \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:19.283781+00:00
---

# About upgrading the Valkey version of an instance  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-upgrading-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About upgrading the Valkey version of an instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the following information:

  * Best practices for upgrading the version of a Memorystore for Valkey instance
  * How the instance behaves during a version upgrade



For more information about upgrading the instance's version, see [Upgrade the Valkey version of an instance](https://docs.cloud.google.com/memorystore/docs/valkey/upgrade-valkey-version).

## Best practices for upgrading an instance's version

This section provides guidance for upgrading the version of an instance.

**Important** : Upgrading the instance version is irreversible. You can't downgrade the instance to an earlier version.

  * Before you upgrade, we recommend creating a backup of the instance's data. For more information, see [Create an on-demand backup](https://docs.cloud.google.com/memorystore/docs/valkey/manage-backups#create-on-demand-backup).

  * To improve the speed and reliability of the upgrade, perform it during periods of low instance traffic. For more information about monitoring instance traffic, see [Monitor instances](https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances).

  * To manage the memory of the instance during the upgrade, make sure that you follow our best practices for memory management. For more information, see [Memory management best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#memory_management_best_practices).

  * To understand how the new version impacts your application, review the supported versions. For more information, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions).




## Version upgrade behavior

Memorystore for Valkey upgrades the version of an instance by updating all of the instance's nodes. This process is similar to a maintenance operation. For more information, see [Create-before-destroy lifecycle strategy](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#create-before-destroy-lifecycle-strategy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
