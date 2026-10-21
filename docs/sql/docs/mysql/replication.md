---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/
title: About replication in Cloud SQL \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:06.597601+00:00
---

# About replication in Cloud SQL  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  About replication in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/replication "View this page for the SQL Server database engine")

Replication is the ability to create copies of a Cloud SQL instance or an on-premises database, and offload work to the copies. 

## Introduction

The primary reason for using replication is to scale the use of data in a database without degrading performance.

Other reasons include:

  * Migrating data between regions
  * Migrating data between platforms
  * Migrating data from an on-premises database to Cloud SQL



Additionally, a replica could be promoted if the original instance becomes corrupted.

When referring to a Cloud SQL instance, the instance that is replicated is called the _primary instance_ and the copies are called _read replicas_. The primary instance and read replicas reside in Cloud SQL.

When referring to an on-premises database, the replication scenario is called _replicating from an external server_. In this scenario, the database that is replicated is the _source database server_. The copies that reside in Cloud SQL are called _Cloud SQL replicas_. There is also an instance that represents the source database server in Cloud SQL called the _source representation instance_.

In a disaster recovery scenario, you can _promote_ a replica to convert it to a primary instance. This way, you can use it in place of an instance that's in a region that's having an outage. You can also promote a replica to replace an instance that's corrupted.

Cloud SQL supports the following types of replicas:

  * Read replicas
  * Cross-region read replicas
  * Cascading read replicas
  * External read replicas
  * Cloud SQL replicas, when [replicating from an external server](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server)



By using [connector enforcement](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#ConnectorEnforcement), you can enforce using only the Cloud SQL Auth Proxy or Cloud SQL Language Connectors to connect to Cloud SQL instances. With connector enforcement, Cloud SQL rejects direct connections to the database. You can't create read replicas for an instance that has connector enforcement enabled. Similarly, if an instance has read replicas, then you can't enable connector enforcement for the instance.

This limitation doesn't apply to the instances that have [private service access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access) configured. You can also use [Database Migration Service](https://docs.cloud.google.com/database-migration/docs/mysql) for continuous replication from a source database server to Cloud SQL. 

Cloud SQL doesn't support replication between two external servers. However, Cloud SQL supports [global transaction identifier (GTID)-based replication](https://dev.mysql.com/doc/mysql-replication-excerpt/5.6/en/replication-gtids-concepts.html). GTIDs uniquely identify each transaction on the server and within a replication setup. Because each transaction has a unique identifier, the MySQL server can keep track of the transactions that it has run. A GTID uses absolute coordinates so the replica of a Cloud SQL instance can point to its primary instance, and you don't have to specify a filename for the binary log or a position in the `CHANGE MASTER` statement. There are fewer errors with replicas and with point-in-time recovery. Because of these benefits, you can't disable GTID-based replication in Cloud SQL. 

**Note:** Don't use a replica as the source for systems like Datastream or Kafka. If a read replica becomes unhealthy, downstream systems reading from it, including Datastream or Kafka, can experience disruptions and fail to stream data correctly. Cloud SQL automatically recreates the read replica to ensure minimal impact. However, recreating a replica requires you to re-initialize your downstream systems to resume ingestion from the newly re-created replica.

## Read replicas

You use a read replica to offload work from a Cloud SQL instance. The read replica is an exact copy of the primary instance. Data and other changes on the primary instance are updated in almost real time on the read replica.

Read replicas are read-only; you cannot write to them. The read replica processes queries, read requests, and analytics traffic, thus reducing the load on the primary instance.

**Note:** We recommend that you limit the number of _direct_ read replicas of your primary instance to 10 or fewer. If you need additional replicas, then you can create cascading read replicas.**Note:** Active long-running transactions might affect the creation of read replicas. We recommend creating a read replica under the following conditions: 

  * When the instance is under low traffic demands.
  * After long-running transactions complete.



You [connect](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip) to a replica directly using its connection name and IP address. If you're connecting to a replica using a private IP address, you don't need to create an additional VPC private connection for the replica because the connection is inherited from the primary instance.

For information about how to create a read replica, see [ Creating read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica). For information about managing a read replica, see [ Managing read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas).

**Note:** Read replicas don't provide failover capability. To provide failover capability for an instance, see [Configuring an instance for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-ha).

As a best practice, put read replicas in a different zone than the primary instance when you use HA on your primary instance. This practice ensures that read replicas continue to operate when the zone that contains the primary instance has an outage. See the [Overview of high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability) for more information.

### Selecting an appropriate machine type

Read replicas can have a different number of vCPUs and memory from that of the primary. You should [monitor metrics on your instance](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance) such as CPU and memory usage to ensure that the replica instance is sized correctly for its workload, especially if it is smaller than the primary instance. A replica instance that is undersized is more prone to poor performance, such as frequent out-of-memory (OOM) events.

#### Storage capacity on read replicas

When a primary instance is resized, all of its read replicas are resized, if needed, so that they have at least as much storage capacity as the updated primary instance.

## Cross-region read replicas

Cross-region replication lets you create a read replica in a different region from the primary instance. You create a cross-region read replica the same way as you [create an in-region replica](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica).

Cross-region replicas:

  * Improve read performance by making replicas available closer to your application's region.
  * Provide additional disaster recovery capability to guard against a regional failure.
  * Let you migrate data from one region to another.



See [Promoting replicas for regional migration or disaster recovery](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas) for more information about cross-region replicas.

## Cascading read replicas

Cascading replication lets you create a read replica under another read replica in the same or a different region. The following scenarios are use cases for using cascading replicas:

  * **Disaster recovery** : You can use a cascading hierarchy of read replicas to simulate the topology of your primary instance and its read replicas. During an outage, your selected read replica is promoted to primary and the read replicas under the new primary continue to replicate and are ready for use.
  * **Performance improvements** : Reduce the burden on the primary instance by offloading replication work to multiple read replicas.
  * **Scale Reads** : You can have more replicas to share the read load.
  * **Cost reduction** : You can reduce networking costs by using a single cascading replica with cross-region replication in other regions.



### Terminology

  * **Cascading replica** : A read replica that can have its own replica.
  * **Levels** : You can create levels of replicas in a cascading replica hierarchy. For example, if you add four replicas to an instance, those four replicas are at the same level.
  * **Sibling instances** : Multiple replicas that replicate from the same primary instance. Siblings are at the same level in the replica hierarchy. A replica can officially have up to eight siblings.
  * **Leaf replica** : A read replica that does not have any replicas of its own. In a multi-level replication hierarchy, the leaf replica is the last level.
  * **Promote** An action that converts a replica, at any level in the hierarchy, into a primary instance. When promoted, the replica's cascading replica hierarchy is retained.



### Configure cascading replicas

Cascading replicas let you add read replicas to any existing replicas. You can add up to four levels of replicas, including the primary instance. When you promote the replica at the top of a cascading replica hierarchy, it becomes a primary instance and its cascading replicas continue to replicate.

To plan your configuration, you need to have a goal for what the read replicas intend to do. The next two sections describe the configurations for disaster recovery and multi-region replication.

#### Disaster recovery

To understand how cascading replicas help you recover quickly during an outage, consider the following replication scenario:

### Configuration

![Depicts cascading replica configuration with the cascading
             replica in a separate region](https://docs.cloud.google.com/static/sql/images/cascading-replica-config.png)

### Outage

![Depicts promotion or replica during an outage](https://docs.cloud.google.com/static/sql/images/cascading-replica-outage.png)

### Promotion

![Depicts the new instance with replicas](https://docs.cloud.google.com/static/sql/images/cascading-replica-promote.png)

If you want to use an instance in Region B in a disaster recovery configuration and have:

  * Replicas in the same region attached to the primary instance (Replica A)
  * Replicas in other regions (Cascading Replica) attached to the primary.



You can create read replicas under the cascading replica in Region B.

On the **Outage** tab, if there's an outage in Region A, the cascading replica is promoted to a primary instance. It already has read replicas underneath it, reducing the recovery time objective (RTO).

On the **Promote** tab, you see that when a cascading replica is promoted, its replicas are also promoted and continue to replicate under it.

#### Multi-region replication

Another use case for cascading replicas is to distribute read capacity to a second region in a cost-efficient manner. Cascading replicas C and D can be created that replicate from Replica B. Clients can distribute read queries across replicas B, C, and D to reduce the load on each replica. The cost of cross-region network traffic is incurred only once, from the primary instance to Replica B. Replication from B to C and D uses in-region network transfer, which is free.

You can create a hierarchy of up to four instances using cascading replicas for multi-region replication:

Primary A → Replica B → Replica C and Replica D

### Restrictions

  * You can't delete a replica that has replicas under it. To delete the replica, you must start with the leaf replicas and work your way upward through the hierarchy.
  * Circular region dependency isn't supported. To have the replica of a cascading replica in the same region as the primary instance, the cascading replica must also be in the same region.



## External read replicas

External read replicas are external MySQL instances that replicate from a Cloud SQL primary instance. For example, a MySQL instance running on Compute Engine is considered an external instance.

External read replicas have the following restrictions:

  * The primary for the external replica cannot be a Cloud SQL read replica.
  * Replicating to a MySQL instance hosted by another cloud platform might not be possible; check the documentation from the other provider. For example, setting the configuration field `replicate-ignore-db` is required, and cloud providers where this is not allowed aren't supported. See [ Configuring external replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica#configuring_the_external_replica) for other required configuration fields.
  * If replication is interrupted for a few hours, for example by a network or server outage, the replica falls behind the primary. The replica catches up once it reconnects to the primary and starts replicating again. However, if replication is interrupted for longer than Cloud SQL replication logs are preserved (seven backups), you must delete the replica and create a new one.
  * The data flowing from the primary to the external replica is charged as outbound data transfer. See the [pricing](https://cloud.google.com/sql/pricing) page for data transfer pricing for your Cloud SQL instance type.
  * If you create an external read replica for an instance, and enforce using only the Cloud SQL Auth Proxy or Cloud SQL Language Connectors to connect to an instance that has [private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access#configure-access) configured for it, then you must add the replica's subnet ranges to the primary instance's [authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks). You must configure all ranges as authorized networks of the Cloud SQL instance.

### gcloud

To set IP authorization for an instance to allow traffic from IP address ranges of an external read replica, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:
        
        gcloud sql instances patch \
        --authorized-networks=IP_ADDRESS_RANGE_1/24,IP_ADDRESS_RANGE_2/24

Replace IP_ADDRESS_RANGE_1 and IP_ADDRESS_RANGE_2 with the IP address ranges of your external read replica.

### REST

Before using any of the request data, make the following replacements: 

    * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
    * INSTANCE_NAME: the name of your Cloud SQL instance
    * IP_ADDRESS_RANGE_1: the first IP address range of your external read replica
    * IP_ADDRESS_RANGE_2: the second IP address range of your external read replica

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "kind": "sql#instance",
      "name": INSTANCE_NAME,
      "project": PROJECT_ID,
      "settings": {
        "ipConfiguration": {
          "authorizedNetworks": [{"kind": "sql#aclEntry", "value": "IP_ADDRESS_RANGE_1/24"}, {"kind": "sql#aclEntry", "value": "IP_ADDRESS_RANGE_2/24"}]},
      "kind": "sql#settings"
      }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    




## Replication use cases

The following use cases apply for each type of replication.

Name | Primary | Replica | Benefits and use cases | More information  
---|---|---|---|---  
Read replica | Cloud SQL instance | Cloud SQL instance | 

  * Additional read capacity
  * Analytics target

| 

  * [Creating read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica)
  * [Managing read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas)
  * [Replication metrics](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance)
  * [Replication lag](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-lag)
  * [Read replica indexes](https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes)

  
Cross-region read replica | Cloud SQL instance | Cloud SQL instance | 

  * Additional read capacity
  * Analytics target
  * Additional disaster recovery capability
  * Improve read performance
  * Migrate data between regions

| 

  * [Creating read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica)
  * [Managing read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas)
  * [Replication metrics](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance)

  
External read replica | Cloud SQL standalone or primary instance | MySQL instance external to Cloud SQL | 

  * Reduced latency for external connections
  * Analytics target
  * Migration path to other platforms

| 

  * [ Configure external replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica)

  
Replication from an external server | MySQL instance external to Cloud SQL | Cloud SQL for MySQL instance | 

  * Migration path to Cloud SQL
  * Data replication to Google Cloud
  * Analytics target

| 

  * [ Replicating from an external server](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external)

  
  
## Prerequisites for creating a read replica

Before you can create a read replica of a primary Cloud SQL instance, the instance must meet the following requirements:

  * Automated backups must be enabled.
  * Binary logging must be enabled which requires point-in-time recovery to be enabled. Learn more about the impact of these logs.
  * At least one backup must have been created after binary logging was enabled.



Additional requirements for the external replica:

  * The MySQL version of the replica must be the same or higher than the MySQL version of the primary instance. [Learn more](https://dev.mysql.com/doc/refman/8.4/en/replication-compatibility.html).
  * For security, you must configure SSL/TLS on your primary instance. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl).

**Note:** For information about using parallel replication for performance improvements, see [ Configuring parallel replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#configuring-parallel-replication).

## Impact of enabling binary logging

You must enable point-in-time recovery to enable binary logging on the primary instance to support read replicas. This has the following impacts:

  * Performance overhead 

Cloud SQL uses row-based replication with MySQL flags `sync_binlog=1` and `innodb_support_xa=true`. Therefore, an additional disk [fsync](https://en.wikipedia.org/wiki/Fsync) is required for each write operation, which reduces performance.

  * Storage overhead 

Storage of the binary logs is charged at the same rate as regular data. The binary logs are automatically truncated to the age of the oldest automated backup. Cloud SQL retains the most recent seven automated backups, and all on-demand backups. The size of the binary logs, and therefore the amount charged, depends on the workload. For example, a write-heavy workload consumes more binary log space than a read-heavy workload.

You can see the size of binary logs by using the [ SHOW BINARY LOGS](https://dev.mysql.com/doc/refman/8.4/en/show-binary-logs.html) MySQL command.

When backups are taken, the logs are stored in the backup along with the data.




## Binary logging on read replicas

  * Binary logging is supported on read replica instances (MySQL 5.7 and 8.0 only). You enable binary logging on a replica with the same [API commands](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#enablingpitr) as on the primary, using the instance name of the replica instead of the name of the primary instance. Note that the terms `enable binary logging` and `enable point-in-time recovery` are interchangeable. 

Binary logging durability on the replica (but not on the primary) instance can be set with the [`sync_binlog`](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-s) flag, which controls how often the MySQL server synchronizes the binary log to disk. 

Binary logging can be enabled on a replica even when backup is disabled on the primary. 

If a replica that has this value set is promoted to a standalone server, then the setting is reset to the safe value `1` on the standalone server. 



## Billing

  * A read replica is charged at the same rate as a standard Cloud SQL instance. There is no charge for the data replication. 
  * For external replicas, the data flowing from the primary to the external replica is charged as data transfer. See the [pricing](https://cloud.google.com/sql/pricing) page for data transfer pricing for your Cloud SQL instance type. 
  * Pricing for a cross-region read replica is the same as for creating a new Cloud SQL instance in the region. Refer to [Cloud SQL instance pricing](https://cloud.google.com/sql/pricing#instance-pricing) and select the appropriate region. In addition to the regular cost associated with the instance, a cross-region replica incurs cross-region data transfer charges for replication logs sent from the primary instance to the replica instance, as described in [Network Egress Pricing](https://cloud.google.com/sql/pricing#network-egress-pricing).



## Quick reference for Cloud SQL read replicas

Topic | Discussion  
---|---  
Backups | You cannot configure backups on the replica.  
Cores and memory | Read replicas can use a different number of cores and amount of memory from those of the primary instance.   
Deleting the primary instance | Before you can delete a primary instance, you must promote all of its read replicas to standalone instances or delete the read replicas.  
Deleting the replica | When you delete a replica, there is no impact on the status of the primary instance.  
Disabling binary logging | Before you can disable binary logs on a primary instance, you must promote or delete all of its read replicas.  
Failover | A primary instance can failover to a replica only if the replica is a DR replica. Read replicas are unable to failover in any way during an outage.  
High availability | Read replicas allow you to enable [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability) on the replicas.  
Load balancing | Cloud SQL doesn't provide load balancing between replicas. You can choose to implement load balancing for your Cloud SQL instance. You can also use [connection pooling](https://docs.cloud.google.com/sql/docs/mysql/manage-connections) to distribute queries across replicas with your load balancing setup for better performance.  
Maintenance windows | Read replicas share maintenance windows with the primary instance. The replicas follow the maintenance settings for the primary instance, including the maintenance window, rescheduling, and the deny maintenance period. During maintenance, Cloud SQL updates all read replicas first before updating the primary instance.  
Multiple read replicas | Cloud SQL supports cascading replicas. As a result, you can create up to 10 replicas for a single primary instance and create replicas of those replicas, up to four levels including the primary instance.   
Parallel replication | For information about using parallel replication for performance improvements, see [ Configuring parallel replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#configuring-parallel-replication).  
Private IP | If you're connecting to a replica using a private IP address, you don't need to create an additional VPC private connection for the replica, as it is inherited from the primary instance.  
Restoring the primary instance | You cannot restore the primary instance of a replica while the replica exists. Before restoring an instance from a backup, or performing a point-in-time recovery on it, you must [ promote](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#promote-replica) or delete all of its replicas.  
Settings | The MySQL settings of the primary instance are propagated to the replica, including root password and changes to the user table. CPU and memory changes are not propagated to the replica.  
Stopping a replica | You cannot `stop` a replica. You can `restart`, `delete`, or `disable replication` on it, but you cannot stop it as you can a primary instance.  
Upgrading a replica | Read replicas can experience a disruptive upgrade at any time.  
User tables | You cannot make changes on the replica. All user changes must be done on the primary instance.  
  
## What's next

  * Learn how to [create a read replica](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica). 
  * Learn how to [configure an external replica configuration](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica).
  * Learn how to [replicate your data from an external server](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external).
  * Learn how to [configure an external server configuration](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external).
  * Learn about [replication in MySQL](https://dev.mysql.com/doc/refman/8.4/en/replication.html). 
  * Learn how to [configure an instance for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-ha).
  * Learn about [Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
