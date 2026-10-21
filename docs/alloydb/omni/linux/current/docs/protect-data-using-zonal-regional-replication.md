---
url: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/protect-data-using-zonal-regional-replication/
title: Protect your data using zonal and regional replication \u00a0|\u00a0 AlloyDB Omni using RPM: Current (18.3.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:54:31.360696+00:00
---

# Protect your data using zonal and regional replication  |  AlloyDB Omni using RPM: Current (18.3.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/protect-data-using-zonal-regional-replication/

This page documents AlloyDB Omni version **18.3.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)



Send feedback 

#  Protect your data using zonal and regional replication Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/protect-data-using-zonal-regional-replication)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/protect-data-using-zonal-regional-replication)

This page describes the AlloyDB Omni Premium Availability reference architecture, which includes data protection using zonal replication in a region (high availability), and adds disaster recovery (DR) protection using asynchronous streaming across large geographic boundaries. 

This reference architecture is best suited for the following use cases:

  * You need regional protection in addition to your zonal protection for your mission-critical applications.



This availability reference architecture incorporates read replicas within the region for HA and across regions for DR. This multi-region deployment safeguards against significant disruptions, including widespread power failures and large-scale natural disasters.

## Availability reference architecture considerations

When you're evaluating this availability reference architecture, consider the following factors:

  * Network latency and bandwidth within the region and across regions
  * Geographical placement of databases and application servers
  * Strategy for offloading read-only workloads to replicas
  * Deploy high availability in the remote DR region



Read-only load balancing might be required, especially if you use regional application servers, so that requests are forwarded to the closest database for the fastest response. For more information, see [Request routing to a multi-region classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https).

Extra monitoring might be required for cross-region replication to ensure that replication lag doesn't start to increase due to transaction load or network capacity.

To ensure that your DR is successful, make sure that you perform thorough DR testing. It's important to test application functionality and throughput if there are any high latency network connections between applications servers and the database.

## In-region HA and cross-region DR architectures

Figure 1 shows a suggested HA and DR configuration with three read-replica standby databases in three availability zones and two regions.

**Note:** While the illustrations in this document show Google Cloud physical location-related concepts such as _Zone_ and _Region_ , AlloyDB Omni can be deployed in any cloud or any customer-managed environment. Consequently, terms such as "data center" or "city" might be more suitable to accurately represent your environments.

![AlloyDB Omni with backups and cross-region high availability options](https://docs.cloud.google.com/static/alloydb/omni/linux/current/docs/images/alloydb-omni-ref-arch-premium.png)

**Figure 1.** AlloyDB Omni with backups and cross-region high availability options.

As Figure 1 illustrates, synchronous streaming replication to local (within the same region) replicas provides high availability, while asynchronous streaming replication to a geographically separated remote replica provides regional disaster recovery protection. In the entire configuration, only the primary instance can perform read-write operations while the other replicas can serve read queries.

Configure the replication from the primary to in-region replicas in synchronous mode while the replication to the cross-region replicas are to be configured in asynchronous mode to avoid the latency to impact the primary write performance. In the event of a regional failure, this setup might lead to a non-zero RPO. However, this setup enables a faster RTO in case of a failure. This is because the primary database doesn't need to wait for confirmation from remote standby databases before committing transactions.

It's possible to have additional cross-region backups take backups from the read-replica databases and thus add redundancy to the backups taken from the primary database.

### Read replica backups

Consider the following:

  * If your remote backup might be susceptible to region failure, then you need to initiate extra backups in the alternative regions.
  * If you require backup redundancy, you need to take regional read replica backups.



### Read replica location to support multi-zone availability

### Migration from an HA-only to HA and DR architecture

## Implementation

When you choose an availability reference architecture, keep in mind the following benefits, limitations, and options.

### Benefits

  * Protects from zonal and instance failures
  * Protects from regional failures
  * RTO reduced when the database experiences a regional failure



### Limitations

  * You can reduce RPO for regional recovery with synchronous replication, but this approach causes additional latency for transaction performance. For DR and remote region replication, we recommend that you use only asynchronous replication.
  * Configuring PostgreSQL WAL streaming in synchronous mode offers zero data loss (`RPO=0`) during normal operation or typical failovers. However, this approach doesn't protect against data loss in specific double-fault situations, such as when all standby instances are lost or become unreachable from the primary, and this is immediately followed by a primary restart.



### Data protection options

  * The [Standard Availability Architecture](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/protect-data-using-backups) for backup and recovery options.
  * The [Enhanced Availability Architecture](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/protect-data-using-zonal-replication) for high availability options.



## What's next

  * [AlloyDB Omni availability reference architecture overview](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/database-availability-reference-architecture-overview).
  * [AlloyDB Omni Standard Availability](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/protect-data-using-backups).
  * [AlloyDB Omni Enhanced Availability](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/protect-data-using-zonal-replication).
  * [Work with cross-data-center replication](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/cross-data-center-replication/work-with-cross-data-center-replication).
  * [Request routing to a multi-region classic Application Load Balancer.](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
