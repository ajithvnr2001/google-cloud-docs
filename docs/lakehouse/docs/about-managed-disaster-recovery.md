---
url: https://docs.cloud.google.com/lakehouse/docs/about-managed-disaster-recovery/
title: About cross-region replication and disaster recovery \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:50.008856+00:00
---

# About cross-region replication and disaster recovery  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/about-managed-disaster-recovery/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  About cross-region replication and disaster recovery Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cross-region replication and disaster recovery for the _Lakehouse runtime catalog_ protects against regional outages. As part of _borderless Lakehouse_ , this capability enables failover for tables that use the _Apache Iceberg REST catalog_ endpoint.

When managing failovers, you can choose between soft failovers for planned testing or hard failovers to quickly restore service.

## How it works

The Lakehouse runtime catalog automatically selects primary and secondary regions for catalog metadata. The primary region processes all table commit metadata and then replicates it to the secondary region for backup.

At any time, especially during a disaster, you can switch the primary and secondary regions for the catalog using the failover operation. This action switches the primary for the catalog and all contained namespaces and tables.

## Cross-region replication

Cross-region replication involves two main components: data replication and metastore replication. The disaster recovery feature builds upon cross-region replication to enable failover.

  * **Data replication** : Cloud Storage [automatically replicates your catalog data](https://docs.cloud.google.com/storage/docs/availability-durability#cross-region-redundancy) across multiple regions when you use a dual-region or multi-region bucket. If a regional outage occurs, your data remains accessible without changes to storage paths.

**Note:** During Preview, catalog metadata replication can occur before Cloud Storage data replication is complete. If a disaster occurs that requires a failover, some tables might point to files that are not yet present in the secondary region, which could require a manual recovery process.
  * **Metastore replication** : For Iceberg REST catalog endpoints, the Lakehouse runtime catalog automatically replicates your metastore when you use a dual-region (or custom dual-region) bucket. Metastore replication begins when you create the catalog. The Lakehouse runtime catalog selects a primary and secondary region from the regions defined in your Cloud Storage configuration. The primary region serves all table commit metadata and replicates it to the secondary region for backup.




## Disaster recovery with failover

The disaster recovery feature lets you switch the primary and secondary regions for a catalog. The failover operation switches the primary region for the catalog and all its namespaces and tables. Failovers have two modes: soft failover and hard failover.

  * **Soft failover** : A soft failover prevents data loss. In this mode, the new primary region begins to accept writes only after all previous data synchronizes from the previous primary region. Use a soft failover for disaster recovery testing or other planned scenarios.

  * **Hard failover** : A hard failover prioritizes availability over data consistency and is designed to restore service. In this mode, the primary region always takes over and accepts write traffic, regardless of the primary region's current state. For example, when using a hard failover, the new primary region can take over even if the previous primary is unreachable.




## Limitations

While this feature is in Preview, the REPLICATION_TIMESTAMP only tracks the catalog metadata, rather than Cloud Storage files. To keep data loss with a lower bound, see the Cloud Storage [Data availability and durability](https://docs.cloud.google.com/storage/docs/availability-durability) documentation.

## What's next

  * [Use cross-region replication and disaster recovery](https://docs.cloud.google.com/lakehouse/docs/use-managed-disaster-recovery) with the Lakehouse runtime catalog endpoint.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
