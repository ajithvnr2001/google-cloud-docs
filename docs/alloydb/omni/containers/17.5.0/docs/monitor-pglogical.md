---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/monitor-pglogical/
title: Monitor pglogical replication in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 17.5.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:51:25.045439+00:00
---

# Monitor pglogical replication in AlloyDB Omni  |  AlloyDB Omni for containers: 17.5.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/monitor-pglogical/

This page documents AlloyDB Omni version **17.5.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/overview)



Send feedback 

#  Monitor pglogical replication in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.5.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/monitor-pglogical)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/monitor-pglogical)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/monitor-pglogical)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/monitor-pglogical)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/monitor-pglogical)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/monitor-pglogical)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/monitor-pglogical)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/monitor-pglogical)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/monitor-pglogical)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/monitor-pglogical)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/monitor-pglogical)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/monitor-pglogical)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/monitor-pglogical)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/monitor-pglogical)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/monitor-pglogical)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/monitor-pglogical)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/monitor-pglogical)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/monitor-pglogical)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/monitor-pglogical)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/monitor-pglogical)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/monitor-pglogical)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/monitor-pglogical)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/monitor-pglogical)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/monitor-pglogical)

This page provides provides information about how to monitor and troubleshoot `pglogical` implementations by checking and validating the provider and subscriber databases. 

The information on this page applies only to AlloyDB Omni for containers. It does not apply to AlloyDB Omni for Kubernetes.

## Before you begin

Before you begin to monitor and troubleshoot `pglogical` implementations, check the provider and subscriber databases, understand the `pglogical` implementation, and validate how it is configured.

For more information about the `pglogical` extension, see [About `pglogical`](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/about-pglogical).

For information about data replication using `pglogical`, see [Replicate data between AlloyDB for PostgreSQL and AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/replicate-data-alloydb-omni) and [Replicate data between AlloyDB Omni and other databases](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/replicate-data-omni-other-db).

## Check `pglogical`, replication, and AlloyDB Omni parameter settings

A number of configuration parameters affect the operation of the pglogical extension, and you can check that in the provider and subscriber databases. Note that the parameter values might vary.

  1. Show the current setting of `pglogical`-specific parameters:
         
         SELECT name,
             setting,
             source,
             short_desc
         FROM pg_catalog.pg_settings
         WHERE name LIKE '%pglogical%' AND name NOT LIKE '%alloydb%'
         ORDER BY category, name;
         

  2. Show other logical replication-related parameters:
         
         SELECT name,
             setting,
             source,
             short_desc
         FROM pg_catalog.pg_settings
         WHERE name IN ('wal_level',
                      'max_worker_processes',
                      'max_replication_slots',
                      'max_wal_senders',
                      'shared_preload_libraries',
                      'track_commit_timestamp')
         ORDER BY name;
         

  3. Show AlloyDB Omni-specific parameters:
         
         SELECT name,
             setting,
             source,
             short_desc
         FROM pg_catalog.pg_settings
         WHERE name LIKE '%alloydb%'
         ORDER BY category, name;
         


**Note:** It's recommended that you review the parameter settings on all nodes.

## List nodes in the configuration

  1. List both local and remote nodes in the pglogical replication configuration:
         
         SELECT node_id,
             if_nodeid AS node_id,
             if_name AS node_name,
             if_dsn AS dsn
         FROM pglogical.node_interface
         LEFT JOIN pglogical.local_node ON (node_id = if_nodeid AND node_local_interface = if_id)
         ORDER BY node_name;
         

If the `node_id` column is `NOT NULL`, then that's the local node.

  2. Review the `dsn` information in detail. Any incorrect or outdated connection string information can result in replication failures. For information about `dsn` troubleshooting, see [Troubleshoot subscription replication](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/monitor-pglogical#troubleshoot).




## Check the subscription status and table replication point

The subscription status is always verified from the subscriber database. The subscription shows a status of `initializing` or `replicating`". It also shows a status of `down`. For more information about the `down` status, see [Troubleshoot subscription replication](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/monitor-pglogical#troubleshoot).

  1. List the subscriptions, their current status and settings, in the current database:
         
         SELECT s.sub_name AS subscription_name,
             n1.node_name AS origin_name,
             n2.node_name AS target_name,
             x.status,
             sub_slot_name,
             sub_replication_sets,
             sub_forward_origins,
             sub_apply_delay,
             sub_force_text_transfer,
             sub_enabled AS enabled
         FROM pglogical.subscription s,
             (SELECT subscription_name, status FROM pglogical.show_subscription_status()) AS x,
             pglogical.node n1,
             pglogical.node n2
         WHERE s.sub_origin = n1.node_id
         AND s.sub_target = n2.node_id
         AND s.sub_name = x.subscription_name
         ORDER BY s.sub_name;
         

The output is similar to the following:
         
         -[ RECORD 1 ]-----------+--------------------------------------
         subscription_id         | 3072625608
         subscription_name       | test_sub_1
         origin_name             | provider
         target_name             | subscriber
         status                  | replicating
         sub_slot_name           | pgl_my_test_db_provider_test_sub_1
         sub_replication_sets    | {default,default_insert_only,ddl_sql}
         sub_forward_origins     | {all}
         sub_apply_delay         | 00:00:00
         sub_force_text_transfer | f
         enabled                 | t
         my_test_db=#
         

  2. List that tables that are currently replicated and their current log sequence number (LSN) by the subscription:
         
         SELECT sync_nspname||'.'||sync_relname AS table_name,
             sync_status,
             sync_statuslsn
         FROM pglogical.local_sync_status
         WHERE sync_relname IS NOT NULL
         ORDER BY table_name;
         

The output is similar to the following:
         
         table_name      | sync_status | sync_statuslsn
         ---------------------+-------------+----------------
         public.test_table_1 | r           | 0/B891BC0
         (1 row)
         
         my_test_db=#
         

The `sync_statuslsn` column shows to which LSN the table is synchronized. You can compare this to the LSN at the provider database to gauge replication lag.

  3. Check the replication status for a specific table:
         
         SELECT * FROM pglogical.show_subscription_table('test_sub_1','test_table_1');
         




## Verify replication set details on the provider

  1. List the current replication sets in the provider database and check the items that are replicated:
         
         SELECT set_name,
             node_name,
             replicate_insert,
             replicate_update,
             replicate_delete,
             replicate_truncate
         FROM pglogical.replication_set
         JOIN pglogical.node ON set_nodeid = node_id
         ORDER BY set_name, node_name;
         

  2. List tables and sequences that are replicated:
         
         -- Table details:
         SELECT set_name,
             set_reloid AS table_name,
             set_att_list,
             set_row_filter
         FROM pglogical.replication_set
         NATURAL JOIN pglogical.replication_set_table
         ORDER BY set_name, table_name;
         
         -- Sequence details:
         SELECT set_name,
             set_seqoid AS sequence_name
         FROM pglogical.replication_set
         NATURAL JOIN pglogical.replication_set_seq
         ORDER BY set_name, sequence_name;
         




## Check the replication information and slot lag on the provider

  1. Check the status of each subscriber by generating the `pg_stat_replication` view on the provider database:
         
         SELECT application_name,
             state,
             sync_state,
             client_addr,
             client_hostname,
             pg_wal_lsn_diff(pg_current_wal_lsn(),sent_lsn) AS sent_lag,
             pg_wal_lsn_diff(sent_lsn,flush_lsn) AS receiving_lag,
             pg_wal_lsn_diff(flush_lsn,replay_lsn) AS replay_lag,
             pg_wal_lsn_diff(pg_current_wal_lsn(),replay_lsn) AS total_lag,
             now()-reply_time AS reply_delay
         FROM pg_stat_replication
         ORDER BY client_hostname;
         

The output is similar to the following:
         
         -[ RECORD 1 ]----+------------------------------
         application_name | test_sub_1
         state            | streaming
         sync_state       | async
         client_addr      | 10.45.0.80
         client_hostname  |
         sent_lag         | 0
         receiving_lag    | 0
         replay_lag       | 0
         total_lag        | 0
         reply_delay      | 00:00:26.203433
         
         my_test_db=#
         

**Caution:** Ensure that you're reviewing only the `pglogical` entries. Correlate the `application_name` column to the subscription name from the subscriber database.
  2. Take note of the `reply_delay` column, which shows the time when it received the last update from the subscriber database.

  3. Monitor replication lag of the replication slot on the provider because `pglogical` creates replication slots on the provider database:
         
         SELECT slot_name,
             slot_type,
             database,
             active,
             COALESCE(pg_wal_lsn_diff(pg_current_wal_lsn(),restart_lsn),0) AS restart_lag,
             COALESCE(pg_wal_lsn_diff(pg_current_wal_lsn(),confirmed_flush_lsn),0) AS confirmed_flush_lag
         FROM pg_replication_slots
         WHERE plugin like '%pglogical%'
         ORDER BY slot_name;
         

The output is similar to the following:
         
         -[ RECORD 1 ]-------+-----------------------------------
         slot_name           | pgl_my_test_db_provider_test_sub_1
         slot_type           | logical
         database            | my_test_db
         active              | t
         restart_lag         | 56
         confirmed_flush_lag | 0
         
         my_test_db=#
         

**Important:** Other tools and extensions have the ability to create replication slots. You must ensure that the replication slot that's reviewed corresponds to a `pglogical` replication set. This is covered by the plugin such as `'%pglogical%'` query predicate.



## Troubleshooting subscription replication

The subscription that's checked on the subscriber database must show a status of `replicating` or `initializing` if the subscription is recently created. If the status is `down`, then a problem has occurred.

The `down` status is usually shown after replication has attempted to initiate, but has failed. This is due to connectivity issues caused by the `dsn` setting, or missing database permissions, which is either at the provider or subscriber.

Use Log Explorer and inspect the PostgreSQL log files in Google Cloud when Google Cloud AlloyDB is one of the endpoints, for additional information that might indicate the cause of the problem. The log files provide details of the problem, including specific details on missing permissions.

  1. Check the PostgreSQL log on your AlloyDB Omni server:

###  Docker 
         
         docker logs CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

###  Podman 
         
         podman logs CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

  2. Troubleshoot the `dsn` setting and ensure that network connectivity isn't the source of the problem:

     1. Copy the `dsn` connection string and try a manual connection using `psql` and the same string. If the `psql` session cannot connect, it indicates the following: 
        * A networking issue.
        * An incorrect IP address, username, or password.
        * A blocking firewall.
        * The other cluster's `pg_hba.conf` file is not properly configured.
  3. Resynchronize a table if you don't want to drop and re-create the subscription after taking corrective actions:
         
         SELECT pglogical.alter_subscription_resynchronize_table(subscription_name := 'test_sub_1',relation := 'table_name');
         

**Caution:** This function truncates the table.
  4. Alternatively, drop your subscription and re-create it:
         
         SELECT pglogical.drop_subscription(subscription_name := 'test_sub_1');
         




## What's next

  * [Switchover and failover with `pglogical` replication](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/switchover-failover)
  * [Replicate data between Google Cloud AlloyDB and AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/replicate-data-alloydb-omni)
  * [Replicate data between AlloyDB Omni and other databases](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/replicate-data-omni-other-db)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
