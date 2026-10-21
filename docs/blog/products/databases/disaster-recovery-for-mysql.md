---
url: https://docs.cloud.google.com/blog/products/databases/disaster-recovery-for-mysql/
title: Disaster recovery for MySQL | Google Cloud Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:53:48.924623+00:00
---

# Disaster recovery for MySQL | Google Cloud Blog

> Source: https://docs.cloud.google.com/blog/products/databases/disaster-recovery-for-mysql/

Databases

# 

Architecting multi-region database disaster recovery for MySQL

March 7, 2020

  * [](https://x.com/intent/tweet?text=Architecting%20multi-region%20database%20disaster%20recovery%20for%20MySQL%20@googlecloud&url=https://cloud.google.com/blog/products/databases/disaster-recovery-for-mysql)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://cloud.google.com/blog/products/databases/disaster-recovery-for-mysql&title=Architecting%20multi-region%20database%20disaster%20recovery%20for%20MySQL)
  * [](https://www.facebook.com/sharer/sharer.php?caption=Architecting%20multi-region%20database%20disaster%20recovery%20for%20MySQL&u=https://cloud.google.com/blog/products/databases/disaster-recovery-for-mysql)
  * [](mailto:?subject=Architecting%20multi-region%20database%20disaster%20recovery%20for%20MySQL&body=Check%20out%20this%20article%20on%20the%20Cloud%20Blog:%0A%0AArchitecting%20multi-region%20database%20disaster%20recovery%20for%20MySQL%0A%0ACheck%20out%20how%20to%20use%20high%20availability%20and%20disaster%20recovery%20approaches%20to%20keep%20MySQL%20databases%20up%20and%20running.%0A%0Ahttps://cloud.google.com/blog/products/databases/disaster-recovery-for-mysql)



##### Shashank Agarwal

Database Migrations Engineer, Google PSO

##### Christoph Bussler

Solutions Architect, Google Cloud

Enterprises expect extreme reliability of the database infrastructure that’s accessed by their applications. Despite your best intentions and careful engineering, database errors happen, whether that’s machine crashes or network partitioning. Good planning can help you [stay ahead of problems](https://cloud.google.com/solutions/dr-scenarios-planning-guide) and recover more quickly when issues do occur.

This blog shows one approach of deploying a database architecture that implements high availability and disaster recovery for MySQL on Compute Engine, using regional disks as well as load balancers.

Any database architecture must provide approaches to tolerate errors and recover from those errors quickly without losing data. These approaches are expressed in RTO (recovery time objective) and RPO (recovery point objective), which offer ways to set and then measure how long a service can be unavailable, and how far back data should be saved.

After a database error, a database must recover as fast as possible with an RTO as small as possible, ideally in seconds. There must be as little data loss as possible—ideally, none at all. The desired RPO is the last consistent database state.

From a database architecture and deployment viewpoint, this can be accomplished with two distinct concepts: high availability and disaster recovery. Use both at the same time in order to achieve an architecture that’s prepared for the widest range of errors or incidents.

### Creating a resilient database architecture

A high-availability database architecture has database instances in two or more zones. If a server on a zone fails, or the zone becomes inaccessible, the instances in other zones are available to continue the processing. The figure below shows two instances, one in zone zn1, and one in zone zn2. The load balancer in front supports directing traffic to a healthy database instance available for read and write queries.

A disaster recovery architecture adds a second high-availability database setup in a second region. If one of the regions becomes inaccessible or fails, the other region takes over. The figure below shows two regions, primary and DR. Data is replicated from the primary to the DR region so that the DR region can take over from the latest consistent database state. The load balancer in front of the regions directs traffic to the region in charge of the read and write traffic. Here’s how this architecture looks:

![https://storage.googleapis.com/gweb-cloudblog-publish/images/MySQL_database_architecture.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/MySQL_database_architecture.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/MySQL_database_architecture.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/MySQL_database_architecture.max-900x900.jpg)

In addition to the database instance setup, a regional disk is deployed so that data is written simultaneously in two zones, proving fail-safe in the event of zone failure. This is a huge advantage of Google Cloud, allowing you to skip MySQL-level replication within a region. Each write operation to disk is done in two zones synchronously. When the primary instance fails, a standby instance is mounted with regional persistent disk(s), and the database service (MySQL) is then started using the same. This brings the peace of mind of not worrying about replication lag or database state for high availability.

From a disaster recovery process view, the following happens over time during a failure situation:

  * Normal steady state database operation

  * A failure happens and a region becomes unavailable or the database instance inaccessible

  * A decision must be made to fail over or not (in case there is the expectation that the region becomes available soon enough or the instance becomes responsive again)

  * DNS is updated manually, therefore it redirects application traffic to a second region

  * Fallback to the primary region after it becomes available again is optional, as the second region is a fully built-out deployment




From a high-availability process view, the following happens over time during a failure situation:

  * Normal steady state database operation

  * Database instance fails or becomes unavailable

  * Launch the standby instance

  * Mount regional SSD and start database

  * Automatic redirection of application traffic to the standby via load balancer

  * After the failed or unavailable instance becomes available again, a fallback can take place or not




The database architecture shown demonstrates a highly available architecture supporting disaster recovery. With regional disks and load balancers, it is straightforward to provide a resilient database deployment.

Find out more about [load balancers](https://cloud.google.com/load-balancing) and [regional disks](https://cloud.google.com/compute/docs/disks/#repds). Check out general HA and DR processes and detailed steps in the [initial part of the reference guide](https://cloud.google.com/solutions/disaster-recovery-for-microsoft-sql-server). Try it out to become familiar with the architecture as well as the two major failover processes.

Posted in

  * [Databases](https://cloud.google.com/blog/products/databases)
  * [Google Cloud](https://cloud.google.com/blog/products/gcp)



##### Related articles

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/whats_new_data_cloud_fWg4bKK.max-700x700_L5HMKic.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/whats_new_data_cloud_fWg4bKK.max-700x700_L5HMKic.png)Data AnalyticsWhat’s new with Google Data CloudBy The Google Cloud Data Analytics, BI, and Database teams • 15-minute read](https://cloud.google.com/blog/products/data-analytics/whats-new-with-google-data-cloud)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/09_-_Data_Analytics_tFH57V6.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/09_-_Data_Analytics_tFH57V6.max-700x700.jpg)Data AnalyticsManaged Apache Iceberg at scale: How Spanner powers Lakehouse runtime catalogBy Vinod Ramachandran • 8-minute read](https://cloud.google.com/blog/products/data-analytics/lakehouse-runtime-catalog-powered-by-spanner)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/10_-_Databases.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/10_-_Databases.max-700x700.jpg)DatabasesAlloyDB: A unified database engine for hybrid searchBy Kumar Ramamurthy • 10-minute read](https://cloud.google.com/blog/products/databases/simplify-ai-search-with-alloydb-hybrid-search-and-rrf)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/image1_bE1RXzx.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/image1_bE1RXzx.max-700x700.png)DatabasesAnnouncing Spanner queues: Transactional messaging for agentic workloads and beyondBy Nitin Sagar • 5-minute read](https://cloud.google.com/blog/products/databases/spanner-queues-provide-native-transactional-messaging)
