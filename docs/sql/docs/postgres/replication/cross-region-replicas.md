---
url: https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas/
title: Promote replicas for regional migration or disaster recovery \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:47.662437+00:00
---

# Promote replicas for regional migration or disaster recovery  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Promote replicas for regional migration or disaster recovery Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/replication/cross-region-replicas "View this page for the SQL Server database engine")

This page describes how to use and promote cross-region read replicas (replicas created in a different region from that of the primary) for regional migration or disaster recovery.

## Overview

There are two common scenarios for promoting cross-region replicas:

  * Regional migration: Perform a planned migration of a database to a different region.
  * Disaster recovery: Fail over a database to another region in the event that the primary's region becomes unavailable.



Both use cases involve setting up cross-region replication and then promoting the replica. The main difference between them is whether the promotion of the replica is planned (in the case of regional migration) or unplanned (a failover to the replica's region is needed to continue operations because the primary has become unavailable).

**Note:** Promoting a replica is done manually and intentionally. It is not the same as [high availability](https://docs.cloud.google.com/sql/docs/postgres/high-availability), where a standby instance (which is not a replica) automatically becomes the primary in case of a failure or zonal outage.

## Regional migration

You can use a cross-region replica to migrate your database to another region with minimal downtime. The general idea is to create a replica in another region, wait until replication catches up, promote it, and then direct clients to the newly promoted instance.

The steps involved in promotion are the same as for [promoting an in-region replica](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas#promote-replica); follow those instructions to ensure that the newly promoted instance has all of the transactions that were committed to the original primary instance. Once you have promoted the replica and verified that the newly promoted instance is working, update all database clients to connect to the new instance.

## Disaster recovery (DR)

Cross-region replicas can be used as part of a disaster recovery procedure. You can promote a cross-region replica to fail over to another region should the primary instance's region become unavailable for an extended period of time.

For more information about disaster recovery, see [About disaster recovery in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery).

### Advanced disaster recovery (DR)

If you are using Cloud SQL Enterprise Plus edition, then you can designate a cross-region read replica as a disaster recovery replica (DR replica) for advanced disaster recovery (DR). With advanced DR, you perform a replica failover to replace the primary instance with the designated DR replica. The old primary instance becomes a replica of the promoted DR replica. You can only perform replica failover to the designated DR replica. You can still promote other read replicas without failover.

To return your deployment to the original state after the replica failover with zero data loss, you can perform a switchover. Since the old primary instance is a replica of the new primary instance, you can switch roles again to restore the old primary instance.

For more information, see [Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery#advanced-dr).

### Verify failover criteria

Because replication is asynchronous, when a region outage occurs and a failover is attempted, some recent transactions that were committed to the primary may be lost (not replicated to the replica). Whenever a primary instance becomes unavailable, the following steps show (1) how to determine the amount of data, if any, that may have been lost in the cross-region failover and (2) how to ensure that the promoted replica reflects as many recent writes as possible.

First, check the `Lag Bytes` values in the [monitoring dashboard](https://console.cloud.google.com/monitoring/dashboards/resourceList/cloudsql_database). When there is a region outage in the region of the primary instance, `Lag Bytes` is reported for the primary instance.

Then, connect to the replica instance with a PostgreSQL client by following the instructions in the [replication status](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas#replication-status) page (see the **psql Client** tab). See the instructions pertaining to the `pg_catalog.pg_last_wal_receive_lsn()` and `pg_catalog.pg_last_wal_replay_lsn()` metrics. Verify that the replica has processed all the transactions it has received from the primary. This ensures that when promoted, the replica reflects all transactions that were received before the primary became unavailable.

### Promote a read replica

Once you determine that the failover criteria are met, you can promote one of the replicas to a writeable, standalone instance. Consider the following scenario:

  * Region A (us-central1) has a High Availability primary instance (db-a-0)
  * Region B (us-west1) has a High Availability cross-region replica (db-b-1) of db-a-0
  * Region C (us-east1) has a cross-region replica (db-c-1) of db-a-0



You could choose to promote db-b-1 in Region B to become a standalone writable instance.

See [Promoting a replica](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas#promote-replica) for detailed instructions.

### Ensure the machine type is appropriate

Ensure that the machine type of the newly promoted instance is appropriate for its workload by [monitoring metrics on the instance](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance) such as CPU and memory usage. If the newly promoted instance is smaller than its former primary instance, we recommend that you resize the promoted instance to match its former primary so that it can handle the same amount of load.

### Enable high availability for the promoted instance

For a disaster recovery configuration, we recommend that you configure the replica that you intend to promote as a high-availability replica. Alternatively, configure the newly promoted instance as high-availability. If you choose not to configure the read replica with high availability, you can also configure the instance with high availability if and when you promote it.

When promoted, read replicas are automatically configured with backups. Configuring a read replica for high availability is done the same way as for a primary instance. For more information, see [configuring the instance for high availability](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#ha-existing).

### Recreate additional replicas

If you promote a replica to become a primary instance, you need to recreate any other replicas of the former primary instance. For example, consider the configuration referenced earlier and repeated here:

  * Region A (us-central1) has a High Availability primary instance (db-a-0)
  * Region B (us-west1) has a cross-region replica (db-b-1) of db-a-0
  * Region C (us-east1) has a cross-region replica (db-c-1) of db-a-0



If the primary instance (db-a-0) becomes unavailable, you can promote the replica in region B to become the primary. To again have additional replicas in regions A and C, delete the old instances (the former primary instance in A, and the replica in C), and [create new read replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica) from the new primary instance in B.

**Note:** You need to use different names for the new replicas. The promoted replica retains its original name.

The resulting configuration would be:

  * Region A (us-central1) now has a cross-region replica (db-a-1)
  * Region B (us-west1) now has the primary instance (db-b-1)
  * Region C (us-east1) now has a new cross-region replica (db-c-2)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
