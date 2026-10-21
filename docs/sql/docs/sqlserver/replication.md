---
url: https://docs.cloud.google.com/sql/docs/sqlserver/replication/
title: About replication in Cloud SQL \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:55.270867+00:00
---

# About replication in Cloud SQL  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  About replication in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication "View this page for the PostgreSQL database engine") | SQL Server

Replication is the ability to create copies of a Cloud SQL instance and offload work to the copies.

**Important:** Before using this feature, **review thelimitations**.

## Introduction

The primary reason for using replication is to scale the use of data in a database without degrading performance.

**Note:** Although this page is primarily concerned with specific read replica scenarios, you can set up replication from external databases (external to Cloud SQL) to Cloud SQL. For example, see [Migrating data from SQL Server 2017 to Cloud SQL for SQL Server using snapshot replication](https://cloud.google.com/solutions/migrating-data-from-sql-server-to-cloud-sql-for-sql-server).

Other reasons for replication include migrating data between regions.

Additionally, if an original instance is corrupted, a replica could be promoted to a standalone instance (in which case, existing replicas wouldn't consider that instance as primary).

**Note:** This page applies to replicas of a Cloud SQL instance. To set up a Cloud SQL instance to act as a publisher to an external subscriber, see [Configure external replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica).

When referring to a Cloud SQL instance, the instance that is replicated is called the _primary instance_ and the copies are called _read replicas_. The primary instance and read replicas all reside in Cloud SQL.

**Note:** SQL Server replication is implemented using [ SQL Server Read Scale Availability Groups](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/read-scale-availability-groups?view=sql-server-linux-2017#read-scale-availability-groups-without-cluster). 

When the first replica is created:

  * The primary instance is set to the full recovery model for all databases on the primary instance.
  * A temporary disk is created, and a full backup is taken and stored on the temporary disk. The temporary disk is deleted after the replica creation process is complete.

**Note:** Normal storage billing rates apply to the temporary disk.



If, in the time period of the first replica creation, the user switches to the [simple recovery model](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server), then the replica creation fails.

The following apply to databases added to the primary instance after the replicas are created:

  * The databases are added to the availability groups automatically and are populated in the replicas using [auto-seeding](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/automatic-seeding-secondary-replicas?view=sql-server-ver15).
  * Each replica creation invokes a full (full recovery model) backup of databases on the primary instance. Logins and server objects created after the replica creation aren't automatically replicated. To transfer new logins to an existing replica, use the [`sp_help_revlogin`](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) stored procedure.



Cloud SQL supports the following types of replicas:

  * Read replicas
  * Cross-region read replicas
  * Cascading read replicas



By using [connector enforcement](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#ConnectorEnforcement), you can enforce using only the Cloud SQL Auth Proxy or Cloud SQL Language Connectors to connect to Cloud SQL instances. With connector enforcement, Cloud SQL rejects direct connections to the database. You can't create read replicas for an instance that has connector enforcement enabled. Similarly, if an instance has read replicas, then you can't enable connector enforcement for the instance.

This limitation doesn't apply to the instances that have [private service access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access) configured.

Cloud SQL doesn't support replication between two external servers. 

**Note:** Don't use a replica as the source for systems like Datastream or Kafka. If a read replica becomes unhealthy, downstream systems reading from it, including Datastream or Kafka, can experience disruptions and fail to stream data correctly. Cloud SQL automatically recreates the read replica to ensure minimal impact. However, recreating a replica requires you to re-initialize your downstream systems to resume ingestion from the newly re-created replica.

## Read replicas

You use a read replica to offload work from a Cloud SQL instance. The read replica is an exact copy of the primary instance. Data and other changes on the primary instance are updated in almost real time on the read replica.

Read replicas are read-only; you cannot write to them. The read replica processes queries, read requests, and analytics traffic, thus reducing the load on the primary instance. You can have up to 8 read replicas per primary instance.

**Note:** Active long-running transactions might affect the creation of read replicas. We recommend creating a read replica under the following conditions: 

  * When the instance is under low traffic demands.
  * After long-running transactions complete.



You [connect](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip) to a replica directly using its connection name and IP address. If you're connecting to a replica using a private IP address, you don't need to create an additional VPC private connection for the replica because the connection is inherited from the primary instance.

For information about how to create a read replica, see [ Creating read replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica). For information about managing a read replica, see [ Managing read replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/manage-replicas).

**Note:** Read replicas don't provide failover capability. To provide failover capability for an instance, see [Configuring an instance for high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha).

As a best practice, put read replicas in a different zone than the primary instance when you use HA on your primary instance. This practice ensures that read replicas continue to operate when the zone that contains the primary instance has an outage. See the [Overview of high availability](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability) for more information.

### Selecting an appropriate machine type

Read replicas can have a different number of vCPUs and memory from that of the primary. You should [monitor metrics on your instance](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-instance) such as CPU and memory usage to ensure that the replica instance is sized correctly for its workload, especially if it is smaller than the primary instance. A replica instance that is undersized is more prone to poor performance, such as frequent out-of-memory (OOM) events.

#### Storage capacity on read replicas

When a primary instance is resized, all of its read replicas are resized, if needed, so that they have at least as much storage capacity as the updated primary instance.

## Cross-region read replicas

Cross-region replication lets you create a read replica in a different region from the primary instance. You create a cross-region read replica the same way as you [create an in-region replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica).

In the case of SQL Server read replicas, it is assumed that the replica is in the same virtual network as the primary replica, or that they communicate using Public IP. 

Cross-region replicas:

  * Improve read performance by making replicas available closer to your application's region.
  * Provide additional disaster recovery capability to guard against a regional failure.
  * Let you migrate data from one region to another.



See [Promoting replicas for regional migration or disaster recovery](https://docs.cloud.google.com/sql/docs/sqlserver/replication/cross-region-replicas) for more information about cross-region replicas.

## Cascading read replicas

**Note:** This feature is available with Cloud SQL Enterprise Plus edition only. For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro). 

Cascading replication lets you create a read replica under another read replica in the same or a different region. Cascading replicas are implemented using [distributed availability groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/distributed-availability-groups?view=sql-server-ver16). Some use cases for cascading replicas are as follows:

  * **Disaster recovery** : you can use a cascading hierarchy of read replicas to simulate the topology of your primary instance and its read replicas. During an outage, your selected read replica is promoted to primary and the read replicas under the new primary continue to replicate and are ready for use. The old primary becomes a secondary of the new primary when it becomes available, and you can switch back to the old primary once it recovers using a switchover. For more information about using cascading replicas for disaster recovery, see [About disaster recovery](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery).
  * **Performance improvement** : Reduce the burden on the primary instance by offloading replication work to multiple read replicas.
  * **Scale reads** : You can have more replicas to share the read load.
  * **Cost reduction** : You can reduce networking costs by using a single cascading replica with cross-region replication in other regions.



### Terminology

  * **Cascadable replica** : A cross-region read replica that can be used for switchover and replica failover operations in [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery#advanced_disaster_recovery) with Cloud SQL for SQL Server.
  * **Cascading replica** : A read replica that can have its own replica.
  * **Levels** : You can create levels of replicas in a cascading replica hierarchy. For example, if you add four replicas to an instance, those four replicas are at the same level.
  * **Sibling instances** : Multiple replicas that replicate from the same primary instance. Siblings are at the same level in the replica hierarchy. A replica can officially have up to eight siblings.
  * **Leaf replica** : A read replica that does not have any replicas of its own. In a multi-level replication hierarchy, the leaf replica is the last level.
  * **Promote** An action that converts a replica, at any level in the hierarchy, into a primary instance. When promoted, the replica's cascading replica hierarchy is retained.



### Configure cascading replicas

Cascading replicas let you add read replicas to any existing replicas. You can add up to four levels of replicas, including the primary instance. When you promote the replica at the top of a cascading replica hierarchy, it becomes a primary instance and its cascading replicas continue to replicate.

For more information on configuring distributed availability groups, see [Configure an Always On distributed availability group](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/configure-distributed-availability-groups?view=sql-server-ver16&tabs=automatic).

### Restrictions

  * You can't delete a replica that has replicas under it. To delete the replica, you must start with the leaf replicas and work your way upward through the hierarchy.
  * Circular region dependency isn't supported. To have the replica of a cascading replica in the same region as the primary instance, the cascading replica must also be in the same region.


  * You must create cascadable replicas in a different region than the region of the primary instance. Then you can create cascading replicas in the same region as the cascadable replica.



## Replication use cases

The following use cases apply for each type of replication.

Name | Primary | Replica | Benefits and use cases | More information  
---|---|---|---|---  
Read replica | Cloud SQL instance | Cloud SQL instance | 

  * Additional read capacity
  * Analytics target
  * Improve read performance
  * Export from replicas

| 

  * [Creating read replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica)
  * [Managing read replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/manage-replicas)
  * [Replication metrics](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-instance)

  
Cross-region read replica | Cloud SQL instance | Cloud SQL instance | 

  * Additional read capacity
  * Analytics target
  * Additional disaster recovery capability
  * Improve read performance
  * Migrate data between regions

| 

  * [Creating read replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica)
  * [Managing read replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/manage-replicas)
  * [Replication metrics](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-instance)

  
SQL Server replication | Instance external to Cloud SQL | Cloud SQL for SQL Server instance | 

  * Migration path to Cloud SQL
  * Replication from an external server to Cloud SQL
  * Replication from Cloud SQL to an external server
  * Replication between Cloud SQL instances
  * Data replication to Google Cloud
  * Analytics target

| 

  * [ Migrating data from SQL Server 2017 to Cloud SQL for SQL Server using snapshot replication](https://cloud.google.com/solutions/migrating-data-from-sql-server-to-cloud-sql-for-sql-server)

  
  
## Billing

  * A read replica is charged at the same rate as a standard Cloud SQL instance. There is no charge for the data replication. 
  * Pricing for a cross-region read replica is the same as for creating a new Cloud SQL instance in the region. Refer to [Cloud SQL instance pricing](https://cloud.google.com/sql/pricing#instance-pricing) and select the appropriate region. In addition to the regular cost associated with the instance, a cross-region replica incurs cross-region data transfer charges for replication logs sent from the primary instance to the replica instance, as described in [Network Egress Pricing](https://cloud.google.com/sql/pricing#network-egress-pricing).



## Quick reference for Cloud SQL read replicas

Topic | Discussion  
---|---  
Backups | You cannot configure backups on the replica.  
Cores and memory | Read replicas can use a different number of cores and amount of memory from those of the primary instance.   
Deleting the primary instance | Before you can delete a primary instance, you must promote all of its read replicas to standalone instances or delete the read replicas.  
Deleting the replica | When you delete a replica, there is no impact on the status of the primary instance.  
Deleting a replicated database | You can delete a replicated SQL Server database using the Google Cloud console or the `gcloud` command, and the deletion automatically propagates to the replicas. You cannot delete a replicated SQL Server database using T-SQL commands.  
Failover | A primary instance can failover to a replica only if the replica is a DR replica. Read replicas are unable to failover in any way during an outage.  
Load balancing | Cloud SQL does not provide load balancing between replicas.  
Maintenance windows | Read replicas share maintenance windows with the primary instance. The replicas follow the maintenance settings for the primary instance, including the maintenance window, rescheduling, and the deny maintenance period. During maintenance, Cloud SQL updates all read replicas first before updating the primary instance.  
Multiple read replicas | You can create up to 8 read replicas for a single primary instance.   
Private IP | If you're connecting to a replica using a private IP address, you don't need to create an additional VPC private connection for the replica, as it is inherited from the primary instance.  
Restoring the primary instance | You cannot restore the primary instance of a replica while the replica exists. Before restoring an instance from a backup, or performing a point-in-time recovery on it, you must [ promote](https://docs.cloud.google.com/sql/docs/sqlserver/replication/manage-replicas#promote-replica) or delete all of its replicas.  
Settings | The settings of the primary instance are propagated to the replica, including changes to the data about users who can access the instance.   
Stopping a replica | You cannot `stop` a replica. You can `restart` or `delete` it, but you cannot stop it as you can a primary instance.  
Upgrading a replica | Read replicas can experience a disruptive upgrade at any time.  
User tables | You cannot make changes on the replica. All user changes must be done on the primary instance.  
  
## Limitations

  * This feature only applies to the following versions of Cloud SQL for SQL Server:

    * SQL Server 2017 Enterprise
    * SQL Server 2019 Enterprise
    * SQL Server 2022 Enterprise
  * Cloud SQL doesn't support [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery) replicas in the same region. If you want to create a read replica in the same region as the source, then you can only promote the read replica to a new primary instance.

  * Cascading replicas are available with Cloud SQL Enterprise Plus edition only.

  * You can't create a cascading replica from the Google Cloud console.

  * If any sign-ins exist on the primary instance when Cloud SQL creates the replica, then Cloud SQL copies them to the new replica. After this occurs, if you add sign-ins to the primary, then Cloud SQL doesn't automatically propagate them to existing replicas. However, you can manually transfer new logins to existing replicas by using the [`sp_help_revlogin`](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) stored procedure.

  * You must monitor your replica using T-SQL and/or SQL Server Management Studio.

  * Before deleting a database, you must close your database connections.

  * When you create a replica, the primary instance can contain no databases in single-user mode. Otherwise, replica creation fails.

  * To create a replica, the primary instance must meet the following requirements:

    * Must not contain databases in single-user mode.
    * Must not contain databases in an `OFFLINE` state.
    * Must not contain databases in read-only mode.
    * Must not contain databases with auto-close enabled.
    * Must not be used as a [distribution database](https://learn.microsoft.com/en-us/sql/relational-databases/replication/distribution-database?view=sql-server-ver17).
    * Must not have push transactional replication enabled.
    * Must not be a [database snapshot](https://learn.microsoft.com/en-us/sql/relational-databases/databases/database-snapshots-sql-server?view=sql-server-ver17).

If the primary instance doesn't meet the necessary requirements, then replica creation fails and the following error message is returned:
    
    Instance is not eligible for replica creation...
    

  * Replication can't be configured on an instance configured with [external replication](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica).




## What's next

  * Learn how to [create a read replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica). 
  * Learn how to [configure an instance for high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha).
  * Learn about [Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
