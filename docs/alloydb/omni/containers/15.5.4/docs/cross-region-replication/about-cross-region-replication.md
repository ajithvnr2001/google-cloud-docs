---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/about-cross-region-replication/
title: About cross-region replication \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:50:51.846510+00:00
---

# About cross-region replication  |  AlloyDB Omni for containers: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/about-cross-region-replication/

This page documents AlloyDB Omni version **15.5.4** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/overview)



Send feedback 

#  About cross-region replication Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/about-cross-region-replication)

This page provides an overview of AlloyDB for PostgreSQL cross-region replication. 

AlloyDB cross-region replication lets you create secondary clusters and instances from a primary cluster to make the resources available in different regions, in the event of an outage in the primary region. These secondary clusters and instances function as copies of your primary cluster and instance resources.

Key concepts in this page include the following:

  * **Primary cluster.** A read-write cluster in a single region.
  * **Secondary cluster.** A read-only cluster in a different region than the primary, that replicates from the primary cluster asynchronously. In the event of a failure of an AlloyDB primary cluster, you can promote a secondary cluster to a primary cluster.
  * **Secondary instance.** A read-only leader of a secondary cluster. It is responsible for receiving a replication stream from a primary cluster. The replication stream updates the storage volume in the secondary region based on the storage volume in the primary region. If a secondary cluster is promoted to a primary cluster, the secondary instance becomes the primary instance.
  * **Active secondary node.** A node that's part of the secondary instance. This node remains active and responds to requests.
  * **Stand-by secondary node.** A node that's part of the secondary instance. If AlloyDB detects unavailability of the active node, it promotes the standby node to act as the new active node.



## Benefits

The benefits of cross-region replication on AlloyDB include the following:

  * **Disaster recovery.** In the event the primary cluster's region becomes unavailable, you can promote AlloyDB resources in another region to serve requests.

  * **Reduced downtime.** Support of high availability (HA) on secondary clusters reduces downtime during maintenance events or unplanned outages.

  * **Geographically distributed data.** Distributing the data geographically brings the data closer to you and decreases read latency.

  * **Geographic load balancing.** In the event of slow or overloaded connections in one region, you can route traffic to another region.

  * **Improved read performance.** It makes AlloyDB resources available closer to your application's region.

  * **Switchover with zero data loss.** For cross-region replication setups with a single secondary cluster, AlloyDB supports switchover between primary and secondary instance with zero data loss.




## How to work with cross-region replication

Working with AlloyDB cross-region replication involves the following tasks:

  * [**Create a secondary cluster.**](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/work-with-cross-region-replication#secondary-cluster-instance) A secondary cluster is a continuously updated copy of your AlloyDB primary cluster.

  * [**View a secondary cluster.**](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/work-with-cross-region-replication#view-secondary-cluster) After you create a secondary cluster, you can view its details in the **Clusters** page in the Google Cloud console.

  * [**Add read pool instances.**](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/work-with-cross-region-replication#read-pools-secondary-cluster) You can add read pool instances to a secondary cluster. If you want to scale your read capacity horizontally, you can add up to 20 read nodes to your secondary cluster.

  * [**Promote a secondary cluster.**](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/work-with-cross-region-replication#promote-secondary-cluster) If you need to read from or write to the data in a secondary cluster, you must first promote it into a fully-featured, standalone primary cluster. When you promote a secondary cluster, the cluster's secondary instance is also promoted as a primary instance with read and write capabilities.

There are two common scenarios for promoting your secondary cluster to a primary cluster:

    * **Regional migration.** Perform a planned migration of the AlloyDB resources from their primary region to another region.
    * **Disaster recovery.** Rapidly activate the AlloyDB resources in a secondary region in the event that the resources in the primary region become unavailable. Due to replication lag, some data loss might occur.

Promoting a secondary cluster converts it to a standalone cluster with a fully functional primary instance, including read and write capabilities. The promoted cluster no longer replicates the data from the primary cluster it was formerly associated with.

  * [**Switchover with zero data loss.**](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/work-with-cross-region-replication#switchover-secondary) Switchover lets you reverse the roles of your primary and secondary cluster with zero data loss. You can perform a switchover for testing your disaster recovery setup or performing migration of your workload. When you complete the switchover, the direction of replication is reversed.

Switchover with zero data loss is only supported for cross-region replication setups with a single secondary instance.

  * [**Configure automated and continuous backups.**](https://docs.cloud.google.com/alloydb/docs/backup/configure) By default, AlloyDB automatically copies automated and continuous backup configurations from the primary cluster to a newly created secondary cluster. If you don't want this automatic replication, you can modify the backup configuration when you create a secondary cluster.

If your primary cluster uses customer-managed encryption key (CMEK) encryption for backups, take one of these actions during secondary cluster creation:

    * Provide CMEK encryption settings for the secondary cluster's backups.
    * Explicitly disable backups for the secondary cluster.



For more information about encrypting your backups with CMEK, see [Use CMEK](https://docs.cloud.google.com/alloydb/docs/use-cmek)

You can modify automated and continuous backup settings for the secondary cluster after its creation.

## What's next

  * [Work with cross-region replication](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/work-with-cross-region-replication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
