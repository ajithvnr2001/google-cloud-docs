---
url: https://docs.cloud.google.com/sql/docs/mysql/high-availability/
title: About high availability \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:36.495917+00:00
---

# About high availability  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/high-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  About high availability Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/high-availability "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability "View this page for the SQL Server database engine")

This page is an overview of the high availability (HA) configuration for Cloud SQL instances. To configure a new instance for HA, or to enable HA on an existing instance, see [Enabling and disabling high availability on an instance](https://docs.cloud.google.com/sql/docs/mysql/configure-ha).

## HA configuration overview

The purpose of an HA configuration is to reduce downtime when a zone or instance becomes unavailable. This might happen during a zonal outage, or when there's a hardware issue. With HA, your data continues to be available to client applications.

The HA configuration provides data redundancy. A Cloud SQL instance configured for HA is also called a _regional instance_ and has a primary and secondary zone within the configured region*. Within a regional instance, the configuration is made up of a _primary instance_ and a _standby instance_. Through [synchronous replication](https://docs.cloud.google.com/compute/docs/disks#repds) to each zone's persistent disk, all writes made to the primary instance are replicated to disks in both zones before a transaction is reported as committed. In the event of an instance or zone failure, the standby instance becomes the new primary instance. Users are then rerouted to the new primary instance. This process is called a _failover_.

**Note:** There are cases where Cloud SQL issues a restart instead of a failover. When this happens, you see **Restart** as an operation on the instance when you view the **Operations and logs** pane on the instance **Overview** page or on the instance **Operations** page. For example, the database can restart when a resource is exhausted, such as when an instance runs out of memory. To avoid downtime due to memory issues, see [Optimize high memory consumption](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage).**Warning:** Moving an instance to a [different zone](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#impact) causes instance downtime. The operation involves data replication across zones, meaning downtime duration scales directly with the size of the instance's disk.

After a failover, the instance that received the failover continues to be the primary instance, even after the original instance comes back online. After the zone or instance that experienced an outage becomes available again, the original primary instance is destroyed and recreated. Then it becomes the new standby instance. If a failover occurs in the future, the new primary will fail over to the original instance in the original zone.

If you need to have the primary instance in the zone that had the outage, you can do a _failback_. A failback performs the same steps as the failover, only in the opposite direction, to reroute traffic back to the original instance. To perform a failback, use the procedure in [Initiating failover](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#test).

Regional persistent disk support for Cloud SQL HA configuration that has at least one dedicated CPU has full [Service Level Agreement (SLA)](https://cloud.google.com/sql/sla) coverage. An HA-configured instance costs twice as much as a standalone instance. This price includes CPU, RAM, and storage. For more information, see the [pricing page](https://cloud.google.com/sql/pricing).

* For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

You can create an account to evaluate how Cloud SQL performs in real-world scenarios. New customers also get $300 in free credits to spend on Cloud SQL to run, test, and deploy workloads. You won't be charged until you upgrade.

Sign up to [ try Cloud SQL for free](https://console.cloud.google.com/freetrial?redirectPath=/sql).

![Diagram overview of the Cloud SQL HA configuration. Described in text below.](https://docs.cloud.google.com/static/sql/images/ha-config.png)

### Read replicas

If availability is a consideration for your read replicas, you can enable HA on the replicas. When you promote such a replica to become a primary instance, it's already set up as a highly available instance.

During a zonal outage, traffic stops to read replicas in that zone. After the zone becomes available again, any read replicas in the zone resume replication from the primary instance. If read replicas are not located in a zone that is undergoing an outage, they connect to the standby instance when it becomes the primary instance.

As a best practice, consider putting some of your read replicas in a different zone from the primary and standby instances. For example, if you have a primary instance in zone A and a standby instance in zone B, put a read replica in zone C to improve your reliability. This practice ensures that read replicas continue to operate even if the zone for the primary instance goes down. You should also add business logic in the client application to send reads to the primary instance when read replicas are unavailable.

**Note:** The standby instance cannot be used for read queries. This differs from the Cloud SQL for MySQL legacy HA configuration.

## Failover overview

If an HA-configured instance becomes unresponsive, Cloud SQL automatically switches to serving data from the standby instance. To see if a failover has occurred, check your [operation log](https://docs.cloud.google.com/sql/docs/mysql/logging#logs) failover history.

Learn more about how to [build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries). If you need more detailed information about an operation, such as the user who performed the operation, you must [ enable audit logging](https://docs.cloud.google.com/sql/docs/mysql/audit-logging#enabling_audit_logging).

Click the tabs to see how failover affects your instance.

### Normal

![Diagram of healthy instance before failover](https://docs.cloud.google.com/static/sql/images/ha-config-replica.svg)

### Failover

![Diagram of instance when failover occurs](https://docs.cloud.google.com/static/sql/images/ha-failover2.svg)

### Post-Failover

![Diagram of instance after failover](https://docs.cloud.google.com/static/sql/images/post-ha.svg)

### Failback

![Diagram of instance after failback](https://docs.cloud.google.com/static/sql/images/ha-config-replica.svg)

### Process

The following process occurs:

  * The primary instance or zone fails.

Each second, the heartbeat system detects whether the primary instance is healthy. If multiple heartbeats aren't detected, failover is initiated.

  * The standby instance now serves data upon reconnection.

Through a shared static IP address with the primary instance, the standby instance now serves data from the secondary zone.


**Note:** If failover occurs, read replicas outside of the outage zone don't change zones; they continue to serve data even if they are in a different zone than the primary instance.**Note:** When a failover occurs, you can expect the instance to be unavailable for about sixty seconds. This duration might differ based on your Cloud SQL environment. See [Initiating failover](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#test).

### Requirements

For Cloud SQL to allow a failover, the configuration must meet the following requirements:

  * The primary instance must be in a normal operating state (not stopped, undergoing maintenance, or performing a long-running Cloud SQL instance operation such as a backup operation).
  * The secondary zone and standby instance must both be in a healthy state. When the standby instance is unresponsive, failover operations are blocked. After Cloud SQL repairs the standby instance and the secondary zone is available, Cloud SQL allows failover.

**Note:** If both the primary and standby instances are unresponsive, Cloud SQL does not allow failover.

## Backup and restore

Automated backups and point-in-time recovery must be enabled for high-availability instances, excluding read replicas.

## Recovery options for standalone instances

Cloud SQL doesn't recover standalone instances from a zonal outage automatically. To re-establish an instance that isn't configured for high availability to a healthy zone, you must restore any zonal instances manually. You can recover a standalone instance from a zonal outage manually by using one of the following options:

  1. Perform point-in-time recovery on the instance to a new instance that you create. To use this option, you must have enabled PITR on the zonal instance prior to the zonal outage. The transaction logs for the instance must be stored in Cloud Storage. If the transaction logs are stored on disk, then you can switch them to Cloud Storage. To use this option, follow the steps in [Perform PITR on an unavailable instance](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#pitr-instance-not-available).

  2. If the instance has a read replica in a different zone, then you can promote that read replica to replace the standalone instance that's experiencing the zonal outage. To use this option, follow the steps in [Promote a replica](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#promote-replica)




For both options, the following considerations apply:

  * Some recent transactions committed on the primary instance might not appear on the newly recovered instance. The interval of time where transactions might have been lost is the recovery point objective (RPO).

    * For PITR recovery, the RPO is typically five minutes or less.
    * For read replica promotion, the RPO varies based on the database workload. For more information on how to monitor and reduce replication lag, see [Replication lag](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-lag).
  * After you perform either of the restoration options, you must reconfigure any clients of the instances that experience the zonal outage because the recovered instances will have different IP addresses and connection names.




## Applications and instances

There is no difference in working with non-HA and HA instances, so your application does not need to be configured in any particular way. When failover occurs, any existing connections to the primary instance and read replicas are closed, and it will take approximately 60 seconds for connections to the primary instance to be reestablished. Your application reconnects using the same connection string or IP address, so you do not need to update your application after failover.

To see exactly how your applications are affected by failover, [manually initiate failover](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#test).

## Maintenance downtime

Maintenance events affect primary instances configured with HA in the same way as other instances. You can expect primary instances to be down for a brief period of time. For more information on how maintenance affects HA instances, see [How maintenance works](https://docs.cloud.google.com/sql/docs/mysql/maintenance#how_maintenance_works). To minimize impact to your service, change [maintenance settings](https://docs.cloud.google.com/sql/docs/mysql/maintenance#management) to control when downtime occurs.

## Performance

Regional persistent disk performance depends on many factors. Your input/output operations per second (IOPS) might be reduced with regional persistent disk in comparison to the zonal persistent disk. Look at [VM instance type](https://docs.cloud.google.com/compute/docs/machine-types) size and your workload input and output. Another metric to note is that the latency for regional persistent disk with [solid-state drives (SSD)](https://en.wikipedia.org/wiki/Solid-state_drive) is higher than it would be for a zonal persistent disk with SSD. This implies that that if your workload is not a streaming workload and is latency sensitive, it can't reach the IOPS limit as regional persistent disk with SSD has higher latency than a zonal persistent disk with SSD. This is because of the synchronous replication of the data across multiple zones involved in a regional persistent disk to provide multiple copies of data across the zones in a region.

## Legacy MySQL high availability option

The legacy process for adding high availability to MySQL instances uses a failover replica. The legacy functionality isn't available in the Google Cloud console. See [Legacy configuration: Creating a new instance configured for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha#ha-create-legacy) or [Legacy configuration: Configuring an existing instance for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha#ha-existing-legacy).

**Important:** As of January 13, 2025, the legacy configuration for high availability (HA) is deprecated for all instances. You can't create instances with legacy high availability configuration, and you can't enable legacy high availability configuration on any existing instances. In addition, after January 13, 2025, legacy high availability instances are no longer covered by the [Cloud SQL SLA](https://cloud.google.com/sql/sla).   
  
We recommend that you update your remaining legacy high availability instances to the current high availability configuration. You can do so by following the instructions in [Update an instance from legacy to current high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha#update-from-legacy). Starting on May 1, 2025, Cloud SQL will begin updating any instances that use the legacy high availability configuration to use the current regional persistent disk-based high availability configuration automatically. 

## What's next

  * [Enable and disable high availability on an instance](https://docs.cloud.google.com/sql/docs/mysql/configure-ha).
  * [Initiate failover](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#test).
  * [Learn more about managing your database connections](https://docs.cloud.google.com/sql/faq#connections).
  * Learn more about [regions and zones](https://docs.cloud.google.com/sql/docs/instance-locations) in Cloud SQL.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
