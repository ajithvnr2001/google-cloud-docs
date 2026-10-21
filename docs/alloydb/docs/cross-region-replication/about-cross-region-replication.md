---
url: https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication/
title: Cross-region replication overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:03.446171+00:00
---

# Cross-region replication overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Cross-region replication overview Stay organized with collections  Save and categorize content based on your preferences. 

To protect your data against regional outages and reduce read latency for geographically distributed users, AlloyDB for PostgreSQL cross-region replication lets you create secondary clusters and instances from a primary cluster in different regions. These secondary clusters and instances function as continuously updated copies of your primary cluster and instance resources.

Key concepts in this page include the following:

  * **Primary cluster.** A read-write cluster in a single region.

  * **Secondary cluster.** A read-only cluster in a different region than the primary, that replicates from the primary cluster asynchronously. In the event of a failure of an AlloyDB primary cluster, you can promote a secondary cluster to a primary cluster.

You can create up to five secondary clusters for a primary cluster. All of the secondary clusters replicate from a single primary cluster. If you promote a secondary cluster, that secondary cluster becomes an independent primary cluster.

  * **Secondary instance.** A read-only leader of a secondary cluster. It is responsible for receiving a replication stream from a primary cluster. The replication stream updates the storage volume in the secondary region based on the storage volume in the primary region. If a secondary cluster is promoted to a primary cluster, the secondary instance becomes the primary instance.

A secondary instance can be either basic (zonal) or high-availability (regional).

The following diagram illustrates how cross-region replication works:




![Example of cross-region replication architecture.](https://docs.cloud.google.com/static/alloydb/images/adb-crr-architecture.png)

**Figure 1.** Example of AlloyDB cross-region replication architecture.

## Benefits

The benefits of cross-region replication on AlloyDB include the following:

  * **Disaster recovery.** In the event the primary cluster's region becomes unavailable, you can promote AlloyDB resources in another region to serve requests.

  * **Reduced downtime.** Support of high availability (HA) on secondary clusters reduces downtime during maintenance events or unplanned outages.

  * **Geographically distributed data.** Distributing the data geographically brings the data closer to you and decreases read latency.

  * **Increased read scaling:** Each cross-region replica (or secondary cluster) can support up to 20 read nodes, allowing you to scale your reads further.

  * **Switchover with zero data loss.** For cross-region replication setups, AlloyDB supports switchover between primary and secondary instance with zero data loss.




## Work with cross-region replication

Working with AlloyDB cross-region replication involves the following tasks:

  * [**Create a secondary cluster.**](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#secondary-cluster-instance) A secondary cluster is a continuously updated copy of your AlloyDB primary cluster.

**Note:** You cannot enable advanced query insights features on secondary clusters.
  * [**View a secondary cluster.**](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#view-secondary-cluster) After you create a secondary cluster, you can view its details in the **Clusters** page in the Google Cloud console.

  * [**Add read pool instances.**](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#read-pools-secondary-cluster) You can add read pool instances to a secondary cluster. If you want to scale your read capacity horizontally, you can add up to 20 read nodes to your secondary cluster.

  * [**Promote a secondary cluster.**](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#promote-secondary-cluster) You can read the data from a secondary cluster, but you can't write to it until you promote it to a fully-featured, standalone primary cluster. When you promote a secondary cluster, the cluster's secondary instance is also promoted as a primary instance with read and write capabilities.

The primary use case for promoting a secondary cluster is disaster recovery. If a regional outage occurs in your primary cluster's region, you can promote your secondary cluster to a standalone primary cluster, and resume serving your application.

  * [**Configure automated and continuous backups.**](https://docs.cloud.google.com/alloydb/docs/backup/configure) By default, AlloyDB automatically copies automated and continuous backup configurations from the primary cluster to a newly created secondary cluster. If you want to use different backup configurations for your secondary cluster, you can modify the backup configuration when you create a secondary cluster.

If your primary cluster uses customer-managed encryption key (CMEK) encryption for backups, do one of the following when you create a secondary cluster:

    * Provide CMEK encryption settings for the secondary cluster's backups.
    * Disable backups for the secondary cluster.



For more information about encrypting your backups with CMEK, see [Use CMEK](https://docs.cloud.google.com/alloydb/docs/use-cmek).

You can modify automated and continuous backup settings for the secondary cluster after its creation.

### Advanced disaster recovery

For advanced disaster recovery scenarios, AlloyDB supports switchover and cross-region failover:

  * [**Perform a cross-region failover.**](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#promote-secondary-cluster) Cross-region failover ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) is an advanced disaster recovery feature that promotes a secondary cluster to primary while automatically recreating the original primary cluster as a new secondary cluster. This feature maintains your replication topology without requiring manual cluster deletion or recreation after the outage is resolved. This simplifies failing back to your original topology after disaster recovery.

  * [**Switchover with zero data loss.**](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#switchover-secondary) Switchover lets you reverse the roles of your primary and secondary cluster with zero data loss. You can perform a switchover to test your disaster recovery setup, fail back to your original topology after an outage, or migrate your workload. When you complete the switchover, the direction of replication is reversed.

If you have multiple secondary clusters, the secondary cluster that receives the switchover command becomes a primary cluster; the previous primary cluster becomes a secondary cluster, replicating from the new primary cluster. All other secondary clusters switch to replicating from the new primary cluster.

There are two common scenarios for switching over your secondary cluster:

    * **Disaster recovery drills.** You can run tests of your disaster recovery processes by switching your application over to another region with zero data loss to simulate a regional outage.
    * **Regional migration.** Perform a planned migration of the AlloyDB resources from their primary region to another region. Switchover ensures the secondary cluster becomes a primary cluster with 0 Recovery Point Objective (RPO), ensuring that the migration does not lose any data. 



## What's next

  * [Work with cross-region replication](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
