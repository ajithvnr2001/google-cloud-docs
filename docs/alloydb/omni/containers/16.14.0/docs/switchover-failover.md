---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/switchover-failover/
title: Switchover and failover with the pglogical replication \u00a0|\u00a0 AlloyDB Omni using containers: 16.14.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:40.533379+00:00
---

# Switchover and failover with the pglogical replication  |  AlloyDB Omni using containers: 16.14.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/switchover-failover/

This page documents AlloyDB Omni version **16.14.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/overview)



Send feedback 

#  Switchover and failover with the pglogical replication Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.14.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/switchover-failover)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/switchover-failover)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/switchover-failover)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/switchover-failover)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/switchover-failover)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/switchover-failover)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/switchover-failover)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/switchover-failover)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/switchover-failover)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/switchover-failover)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/switchover-failover)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/switchover-failover)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/switchover-failover)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/switchover-failover)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/switchover-failover)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/switchover-failover)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/switchover-failover)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/switchover-failover)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/switchover-failover)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/switchover-failover)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/switchover-failover)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/switchover-failover)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/switchover-failover)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/switchover-failover)

This page provides provides information about how to switchover and failover with `pglogical` replication. 

The information on this page applies only to AlloyDB Omni using containers. It does not apply to AlloyDB Omni using the container orchestrator.

## Before you begin

After the `pglogical` replication is set up and there is a viable high availability (HA) and disaster recovery (DR) solution, and recognizing that logical replication does not provide `true` and comprehensive replication of all database objects, you must test this configuration before you start using it.

For more information about the `pglogical` extension, see [About `pglogical`](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/about-pglogical).

For information about data replication using `pglogical`, see [Replicate data between AlloyDB for PostgreSQL and AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/replicate-data-alloydb-omni) and [Replicate data between AlloyDB Omni and other databases](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/replicate-data-omni-other-db).

## Switchover with pglogical replication

Switchover is a controlled process used to switch the roles between the provider and subscriber databases. When you perform a switchover, the roles of the two databases, provider and subscriber, are reversed. The provider becomes the subscriber and the subscriber becomes the provider.

This switchover capability is important for operating system upgrades, PostgreSQL upgrades, or failover testing.

To achieve this in unidirectional replication configurations, you must set up a new provider/subscriber relationship and remove the old provider/subscriber relationship.

**Note:** During the switchover process, if the old configuration is still in use, then WAL files begin to build up on the old provider node. See the [`wal_keep_size`](https://www.postgresql.org/docs/16/runtime-config-replication.html) parameter for more information on how past log file segments are retained for standby databases.

### Build the new provider/subscriber configuration

**Note:** To achieve a clean switchover, some application downtime must be incurred.

  1. Stop the application from writing to the provider system to prevent further database changes, and check the replication lag to ensure all transactions are replayed on the subscriber node:
         
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
         

When all the lag fields display zero, then the replication is up to date and database is ready for a switchover.

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
         

  2. Convert the subscriber database to a provider database:

     1. Stop the existing subscriber subscription.
     2. Add the replication set, if required.
     3. Add the necessary tables into the replication set.
     4. Build a new subscriber subscription in the new subscriber database.
     5. Redirect the applications to the new provider.
  3. Stop the subscription on the existing subscriber database, which becomes the new provider:
         
         SELECT pglogical.alter_subscription_disable(SUBSCRIPTION_NAME);
         

  4. (Optional) Create a replication set that matches with the definition of the original provider database. This is not required if you're using the default replication sets:
         
         SELECT pglogical.create_replication_set(REPLICATION_SET_NAME);
         

  5. Add tables to that replication set:
         
         SELECT pglogical.replication_set_add_table(REPLICATION_SET_NAME, TABLE_NAME);
         

Replace the following:

     * REPLICATION_SET_NAME: The name of the replication set.
     * TABLE_NAME: The table name of a schema owner. For example, `ARRAY['public']`.`
  6. On the new subscriber database, which was previously the provider database, create the new subscription with the `synchronize_data` option set to `false` to prevent the initial table load:
         
         SELECT pglogical.create_subscription (
                    subscription_name := '<subscription name>',
                    replication_sets := array['default'],
                    synchronize_data := false,
                    provider_dsn := 'host=<hostname or IP> port=5432 
                    dbname=<db name> user=pglogical_replication password=<password>');
         

  7. Check whether the subscription is working on the provider node:
         
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
         

  8. If the replication is working, change application connection strings to use the new provider database and restart the application tiers.




If you change the data on the old provider node after the subscriber is stopped, then these changes are not replicated and it results in data loss. If there are unreplicated data changes on the original provider database or if the original provider, which is the new subscriber, is not in a state that's consistent with the new provider database, which is the old subscriber, you must build the new subscriber database completely.

### Remove the old provider and subscription

If you want unidirectional replication, you must remove the old provider/subscriber configuration.

  1. Remove the old subscription on the new provider:
         
         SELECT pglogical.drop_subscription('<subscription name>')
         

  2. Remove the replication set on the new subscriber or remove all the tables from replication set:
         
         SELECT pglogical.drop_replication_set('<replication set name>')
         
         
         SELECT pglogical.replication_set_remove_table('<replication set name>','<table name>')
         




### Bidirectional replication

To switch over without incurring downtime, or to ensure that no data is lost due to unplanned data changes, you must use bidirectional replication. When you implement bidirectional replication, consider the conflict resolution unless strict controls are in place to prevent write access to both nodes at the same time.

You can set up the conflict resolution configuration by using the following `pglogical.conflict_resolution` settings:

  * `error`: the subscriber stops when a conflict is detected.
  * `apply_remote`: always apply the incoming changes irrespective of the data on the subscriber database. This is the default setting.
  * `keep_local`: always ignore the conflicting incoming data and discard the conflicting change.
  * `last_update_wins`: the version of the data with the latest commit timestamp is the data that is committed
  * `first_update_wins`: the version of the data with the oldest timestamp is the data that is committed



To set up bidirectional replication, set up the provider and subscriber so that replication happens both ways. The original subscriber also becomes a provider with the same replication set as the original provider. See [Create a table and add it to the default replication set on the AlloyDB for PostgreSQL provider database](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/replicate-data-alloydb-omni#create-add-table) to create a replication set that duplicates the original replication set on the initial provider database.

On the original provider, you must add a new subscriber. See [Create a node and subscription on the AlloyDB Omni subscriber database](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/replicate-data-alloydb-omni#create-node) to create a new subscriber ensuring that the `synchronize_data` parameter for the command `pglogical.create_subscription` is set to `false`. This avoids the initial table copy of the data.

## Failover with pglogical replication

Failover occurs when the provider database becomes unavailable for any reason, and you must switch the application to use the subscriber database.

**Note:** If there was any lag present when the provider database became unavailable, it might result in data loss unless `synchronous_commit` is switched on.

To prevent any duplicate data from accidentally being applied to the failed-over subscriber database, you must disable the subscription. This ensures that changes from a restored provider are not applied by mistake when the provider becomes available again.

  1. Stop the subscriber, `test_sub_1`:
         
         SELECT pglogical.alter_subscription_disable(`test_sub_1`);
         

  2. Check the status is set to `disabled`:
         
         SELECT pglogical.show_subscription_status('test_sub_1');
         

The output is similar to the following:
         
         show_subscription_status                                                                           
         ----------------------------------------------------------------------------
         (test_sub1,disabled,subscriber,"host=10.45.0.108 port=5432 dbname=my_test_db user=pglogical_replication",subscriber,{failover_set},{all})
         

  3. Check the disabled keyword in the status output.

  4. Build a new provider/subscriber configuration to maintain high availability and disaster recovery ability.

  5. [Create a new replication set](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/replicate-data-alloydb-omni#create-add-table) containing all the tables that were originally replicated so that a new subscriber is built when the old provider database is recovered and is converted into a new subscriber or a new subscriber is built.

  6. [Set up the subscriber](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/replicate-data-alloydb-omni#create-node).

  7. Set up this database as the new subscriber if you can recover the old provider database to the time of the failure. Use the same steps to create a subscription, and set the `synchronize_data` parameter for the `pglogical.create_subscription` command to `false` to avoid the initial table copy.

  8. Remove the old provider configuration on the recovered node to avoid a WAL file build-up.

  9. If you're using the old provider database, either drop the complete replication set or remove all the tables from the replication set one by one:
         
         SELECT pglogical.drop_replication_set('<replication set name>')
         
         
         SELECT pglogical.replication_set_remove_table('<replication set name>','<table name>')
         

  10. Switch the application to write to the new node.




## What's next

  * [Replicate data between AlloyDB for PostgreSQL and AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/replicate-data-alloydb-omni)
  * [Replicate data between AlloyDB Omni and other databases](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/replicate-data-omni-other-db)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
