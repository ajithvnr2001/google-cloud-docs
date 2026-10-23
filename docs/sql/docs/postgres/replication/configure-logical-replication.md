---
url: https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication/
title: Set up logical replication and decoding \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:38.729745+00:00
---

# Set up logical replication and decoding  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Set up logical replication and decoding Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

You can use [logical replication and decoding](https://www.postgresql.org/docs/current/static/logicaldecoding.html) features in Cloud SQL for PostgreSQL. These features enable logical replication workflows and change data capture (CDC) workflows.

**Important:** Before using these features, see the Notes and limitations.

For general information about replication, see [About replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/replication).

## Introduction

When PostgreSQL performs logical replication, the changes that are streamed to replicas are extracted from the WAL logs using logical decoding. The decoded changes are independent of the underlying physical storage format. The changes reflect only the changes in data from a SQL level, in terms of INSERTs, UPDATEs, and DELETEs. This independence from the storage layer provides great flexibility and enables a wide array of functionality by consumers of the change streams.

Logical replication is the flagship feature built on logical decoding.

Unlike PostgreSQL's [physical replication](https://www.postgresql.org/docs/current/static/runtime-config-replication.html) feature, which requires both the source and destination databases to be the same version, logical replication enables replication across PostgreSQL major versions. Logical replication in Cloud SQL is supported by the pglogical extension, available in all PostgreSQL versions, and PostgreSQL's native logical replication, added in PostgreSQL 10.

The format in which changes are streamed can be configured with different plugins. This allows for flexible [change data capture](https://en.wikipedia.org/wiki/Change_data_capture) (CDC) architectures. For example, the `[wal2json](https://github.com/eulerto/wal2json)` extension allows streaming all changes in a database to a consumer, formatted as JSON. Cloud SQL supports the built-in `pgoutput` decoder, the [test_decoding](https://www.postgresql.org/docs/current/static/test-decoding.html) contrib module, and `wal2json`. Cloud SQL currently supports both `wal2json` variants of JSON output - `format-version 1` which encodes the whole transaction as a single JSON object and `format-version 2` which outputs one JSON object per command. These plugins enable replication to non-PostgreSQL databases.

## Configure your PostgreSQL instance

**Note:** Changing the flags discussed in this section requires a restart of your instance. To minimize downtime, read this entire section before deciding on your flag settings.

PostgreSQL supports logical decoding by writing additional information to its write-ahead log (WAL).

In Cloud SQL, you enable this feature by setting the `cloudsql.logical_decoding` flag to `on`. This setting is different from the setting used in standard PostgreSQL. If you change an external PostgreSQL instance, you enable this feature by setting the `wal_level` configuration parameter to `logical`.

**Note:** To enable or disable flags in Cloud SQL, use the [standard instructions](https://docs.cloud.google.com/sql/docs/postgres/flags).

If you plan to use the pglogical extension, pglogical must be added to `shared_preload_libraries`. Since Cloud SQL does not allow direct modification of this flag, pglogical is enabled by setting `cloudsql.enable_pglogical` to `on`. (On a VM, sudo apt-get install postgresql-13-pglogical ) and restart the database.

If you are using pglogical to replicate between two PostgreSQL instances, logical decoding only needs to be enabled on the _primary_ instance, and not on the replica instance (unless that instance itself is a primary for other replicas). However, the pglogical extension must be enabled on both instances. For examples of how the terms "primary" and "replica" are used and their meanings, see [About replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/replication).

### Enable network connectivity

Ensure that your primary instances accept connections from the replica instance.

Primary | Replica | Configuration  
---|---|---  
Cloud SQL (public IP) | Cloud SQL (public IP) | Add the replica's outgoing IP address to the primary's [authorized networks](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks).  
Cloud SQL (private IP) | Cloud SQL (private IP) | If both instances are in the same Google Cloud project, then add the [ allocated IP range](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#private_services_access) of the replica's VPC network to the [authorized network](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks) that hosts the instances. To find the allocated IP range in the Google Cloud console:

  1. Navigate to the **VPC networks** page.
  2. Select the VPC network you're using.
  3. Select the **Private service connection** tab.
  4. Select the **Allocated IP ranges** tab.

**Note:** that you don't need to add anything to the authorized networks of either instance if the VPC network's subnet is in the range of 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16, as these subnet blocks are ACL'd on each instance by default.  
External | Cloud SQL | You can use the [Database Migration Service](https://docs.cloud.google.com/database-migration/docs).  
Cloud SQL | External | See [Configure external replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-external-replica) for more information.  
  
#### Get the outgoing IP address of a replica instance

If the replica instance is a Cloud SQL instance and has a public IP address, perform the following steps to get its outgoing IP address.

**Note:** Skip this procedure if you're configuring replication using a private network only. This is because an outgoing IP address isn't necessary for this scenario.**Caution:** Instances that use [high availability (HA)](https://docs.cloud.google.com/sql/docs/postgres/high-availability) can't be used as subscribers,because they don't have a consistent outgoing IP address.

### Console

  1. Open the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances).

  2. Next to the Cloud SQL replica's public IP address, hover over the **More info** tool tip and retrieve the outgoing IP address. Note that the outgoing IP address is _not_ the IP address displayed in the main listing for the replica in the Google Cloud console.




If the replica instance isn't a Cloud SQL instance, refer to the relevant documentation.

For more information about how to get an instance's public IP address, see [Get the Cloud SQL replica's outgoing IP address](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external#outgoing-ip).

### gcloud

You can use the following `gcloud` command:
    
    
    gcloud sql instances describe [REPLICA_NAME] --format="default(ipAddresses)"
    

#### Allow connections

If the primary instance is a Cloud SQL instance, you can allow access from the replica's outgoing IP address by [adding it as an authorized network](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks#authorized-networks).

**Caution:** When you restore a subscriber instance from a backup, the outgoing IP address of the subscriber instance may change. To restart replication after restoring the subscriber instance, you must add the new outgoing IP as an authorized network.

#### Enable replication connections for PostgreSQL 9.6 and earlier

If your primary instance isn't running in Cloud SQL, and is running PostgreSQL 9.6 or earlier, you must ensure that the instance's `[pg_hba.conf](https://www.postgresql.org/docs/9.6/auth-pg-hba-conf.html) ` file is set to accept replication connections. Add the following line to that file, using `all all` for initial testing only. For more security, limit users and IP addresses to just those required, as in this example:
    
    
    host replication all all md5
    

For additional information, see [The pg_hba.conf File](https://www.postgresql.org/docs/13/auth-pg-hba-conf.html).

### Create a replication user

To use logical decoding features, you create a PostgreSQL user with the `REPLICATION` attribute.

**Note:** In standard PostgreSQL, you must provide `SUPERUSER` permissions. When you are using the pglogical extension, the user must have the `cloudsqlsuperuser` role, to later run the `CREATE EXTENSION` command; in Cloud SQL, a user must have the `cloudsqlsuperuser` role to run that command.

#### Examples
    
    
    CREATE USER replication_user WITH REPLICATION
    IN ROLE cloudsqlsuperuser LOGIN PASSWORD 'secret';
    

Alternatively, you can set this attribute on an existing user:
    
    
    ALTER USER existing_user WITH REPLICATION;
    

**Note:** The existing user must have the `CREATE` privilege on each database that the user is trying to replicate.

### PostgreSQL resources

When logical decoding is used, a background process on the primary PostgreSQL instance transforms WAL changes into logical changes, using the selected decoding plugin, and relays them to a consumer (which could even be a non-PostgreSQL instance). This background process is called a WAL sender. The number of concurrent WAL senders that can be active in a PostgreSQL instance is limited by the [max_wal_senders](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-MAX-WAL-SENDERS) flag. This flag defaults to 10 and its limit grows linearly with the memory of your Cloud SQL instance, allowing 8 WAL senders per GB of memory.

To ensure that WAL segments are not discarded before being sent to all consumers, PostgreSQL uses [logical replication slots](https://www.postgresql.org/docs/current/static/logicaldecoding-explanation.html#LOGICALDECODING-REPLICATION-SLOTS) to track which data was sent to which consumer (and physical [replication slots](https://www.postgresql.org/docs/current/static/view-pg-replication-slots.html) for read replicas). The number of replication slots that you can create for a PostgreSQL instance is limited by the [max_replication_slots](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS) flag. This flag defaults to 10 and its limit grows with the memory of your Cloud SQL instance, allowing between 2 and 8 replication slots per GB of memory.

The following table shows the relationship between the maximum memory of a Cloud SQL instance and the maximum replication slots for the instance.

Maximum memory (GB) | Maximum replication slots  
---|---  
4 | 10  
16 | 32  
32 | 128  
64 | 256  
128 | 512  
256 | 1024  
512 | 2048  
512+ | 4096  
**Important:** A slot that's not actively used to track data causes PostgreSQL to hold onto WAL segments indefinitely, causing the disk space to grow indefinitely. Most tools built on logical decoding create and drop replication slots automatically. Unused replication slots can be detected by querying the [`pg_replication_slots`](https://www.postgresql.org/docs/current/static/view-pg-replication-slots.html) system view and filtering on the `active` column. Unused slots can be dropped to remove WAL segments using the [`pg_drop_replication_slot`](https://www.postgresql.org/docs/current/static/functions-admin.html#FUNCTIONS-REPLICATION) command.

There generally is one replication slot and WAL sender per consumer, so these flags should be set to roughly equal values. However, PostgreSQL recommends providing a small buffer for `max_wal_senders` to handle when connections unexpectedly die and new connections are made. Physical replication, as used by Cloud SQL read replicas, also uses a replication slot and WAL sender, so count those when calculating how many of each resource you need.

PostgreSQL native logical replication and pglogical require additional background processes to run, both on the primary and replica instances. The number of background processes that can run is limited by the [max_worker_processes](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES) flag. The default is eight and its limit grows linearly with the memory of your Cloud SQL instance, allowing two additional processes per GB of memory. The exact number of worker processes used with these approaches is explained in their respective sections.

If this flag is set too low, and replication fails with the error message `worker registration failed` in your logs, you likely need to increase the `max_worker_processes` setting.

Note that WAL senders _do not_ count as worker processes. Workers spawned for parallel query execution do count, so if the value of `max_worker_processes` is set too low, you may experience poor performance because PostgreSQL cannot leverage parallel query execution.

Using the [pg_ls_waldir () function](https://www.postgresql.org/docs/current/static/functions-admin.html#FUNCTIONS-ADMIN-GENFILE), you can determine the WAL disk usage. This function is restricted to `cloudsqlsuperuser` users such as the default admin user `postgres`. This function is only available in PostgreSQL version 10 and above.

To calculate the total WAL disk usage:
    
    
    postgres=> select * from pg_ls_waldir();
    

name | size | modification  
---|---|---  
00000001000000000000000A | 16777216 | 2021-08-11 15:16:49+00  
000000010000000000000009 | 16777216 | 2021-08-12 06:23:24+00  
  
(2 rows)
    
    
    postgres=> select pg_size_pretty(sum(size)) as "Total WAL disk usage" from pg_ls_waldir();
    

Total WAL disk usage  
---  
32 MB  
  
(1 row)

### Set up logical replication with an external replica

See [ Configuring external replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-external-replica) for a complete example using pglogical and logical decoding.

### Set up logical replication with pglogical

To set up logical replication with pglogical, logical decoding must be enabled on the primary instance. Set `cloudsql.logical_decoding=on` on the Cloud SQL instance, or `wal_level=logical` on an external instance. Additionally, pglogical must be enabled on both the primary and replica instance; set `cloudsql.enable_pglogical=on` on a Cloud SQL instance, or add pglogical to `shared_preload_libraries` on an external instance. Note that changing these flags requires a restart of both the primary and replica instances.

If you encounter issues with these steps, see Troubleshoot pglogical.

#### Create a user with replication privileges

You need a user with replication privileges and the `cloudsqlsuperuser` role on both the primary and replica instances when using pglogical. Any commands described below should be executed by that user.

#### Install the pglogical extension

You need to install the pglogical extension on both the primary and replica instances. On the primary, the replication user (that is, the user connecting to the database) must install it.
    
    
    CREATE EXTENSION pglogical;
    

#### Create a pglogical node on each instance

A pglogical _node_ represents a physical PostgreSQL instance, and stores connection details for that instance. Both the primary and the replica instance must register themselves as nodes:
    
    
    source-instance$ SELECT pglogical.create_node(
        node_name := 'primary',
        dsn := 'host=<primary-ip> port=5432 dbname=postgres user=replication_user password=secret'
    );
    
    dest-instance$ SELECT pglogical.create_node(
        node_name := 'replica',
        dsn := 'host=<replica-ip> port=5432 dbname=postgres user=replication_user password=secret'
    );
    

#### Create a table with data to replicate

The pglogical extension allows for replicating only a subset of tables to a destination. As an example, we'll create a dummy table on the primary instance and populate it with some data to test:
    
    
    CREATE TABLE replica_test (id SERIAL PRIMARY KEY, data text);
    INSERT INTO replica_test (data) VALUES ('apple'), ('banana'), ('cherry');
    

The table must also be created on the replica instance.

#### Add the table to a replication set

To support replicating different sets of data to different destinations, pglogical has the concept of a replication set. We can add our test table to the default replication set.
    
    
    SELECT pglogical.replication_set_add_table('default', 'replica_test', true);
    

#### Create the pglogical subscription

Create the pglogical subscription on the destination instance by providing connection details to the primary instance.
    
    
    SELECT pglogical.create_subscription(
        subscription_name := 'test_sub',
        provider_dsn := 'host=<primary-ip> port=5432 dbname=postgres user=replication_user password=replicapassword'
    );
    
    SELECT * FROM pglogical.show_subscription_status('test_sub');
    

If the status appears as "replicating", then the setup is successful. Query the `replica_test` table to ensure that data has been replicated. Insert and modify records on the primary instance and verify that they then appear on the replica instance.

On the primary, query the `pg_replication_slots` table to see the replication slot created by the subscription.

#### Cleanup

After your test is successful, drop the subscription on the replica using `pglogical.drop_subscription('test_sub')`. Verify that the replication slot is also dropped on the primary. Otherwise, WAL segments continue to accumulate on the replica instance.

For more about replication sets, partial data replication, DDL replication, other advanced configuration and limitations, see the [pglogical documentation](https://github.com/2ndQuadrant/pglogical).

#### Resource usage

The pglogical extension runs multiple background processes that count towards the `max_worker_processes` limit.

In the steady state, it runs one "supervisor" process when enabled, one "manager" process per PostgreSQL database that has installed the extension (for example, there could be `D` of these), and one "apply" process per pglogical subscription on the replica instance (for example, there could be `S` of these). The extension, however, may spawn additional worker processes when performing an initial sync, and actually does spawn "manager" processes for _every_ database in the instance, but if the database doesn't have the extension installed, it exits immediately.

Therefore, allocate a handful more worker processes than needed in the steady state. Worker processes are used by PostgreSQL for other purposes, such as parallel query processing. If `max_worker_processes` is set too low, replication may silently fail, or PostgreSQL may be unable to perform parallel query processing.

In summary, these settings are recommended:
    
    
    max_worker_processes
      >= 1 + D + 8 (on the source instance)
      >= 1 + D + S + 8 (on the destination instance)
    max_wal_senders >= S + 2 (on the source instance)
    max_replication_slots >= S (on the source instance)
    

#### Troubleshoot pglogical

##### Unable to create the pglogical extension

When trying to install the pglogical extension, you may see the error:
    
    
    ERROR:  pglogical is not in shared_preload_libraries
    

When you install pglogical on a Cloud SQL instance, ensure that you have set `cloudsql.enable_pglogical=on`. If using an external instance, add it directly to the `shared_preload_libraries` flag, for example, `shared_preload_libraries=pg_stat_statements,pglogical`. These modifications require a restart of the primary instance.

##### Unable to create pglogical subscription

When creating a subscription, pglogical first checks that it can use the connection details to connect to the instance. It first tries to create a regular connection, and if this fails, an error occurs: `ERROR: could not connect to the postgresql server`.

If this error occurs, ensure that the primary instance is configured to allow connections from the replica instance, and ensure that the connection details you provided are correct. Additional details are provided about why PostgreSQL was unable to establish a connection.

After creating a regular connection, pglogical tries to make a special replication connection. In PostgreSQL 9.6 and earlier, this type of connection could have a different authentication configuration. You need to update the `pg_hba.conf` file on the source instance if you see this error: `ERROR: could not connect to the postgresql server in replication mode`.

The `pg_hba.conf` file used by Cloud SQL already has the necessary changes; this error only occurs when connecting to an external instance that isn't managed by Cloud SQL.

Alternatively, the replication mode connection may fail if the source instance does not allow enough WAL senders. If you see `FATAL: number of requested standby connections exceeds max_wal_senders`, then increase `max_wal_senders` on the primary instance.

##### pglogical subscription is down

A pglogical subscription may fail to replicate. To address this issue, first ensure that a background process is running on the replica instance. Query `pg_stat_activity` to verify that a `pglogical apply` process is running. If not, check the logs on the destination node. If you see the message `worker registration failed,` you can increase the `max_worker_processes` setting.

Then, ensure a replication slot was created on the primary instance. On the replica instance, the row in `pglogical.subscription` contains the name of the slot the subscription tries to create, and on the primary instance you can query `pg_replication_slots` to verify that the slot was successfully created.

If no replication slot was created, check the logs on the primary instance.

An error of `ERROR: logical decoding requires wal_level >= logical` implies that the `wal_level` flag wasn't set to `logical`. Resolve this by setting `cloudsql.logical_decoding=on`, on the primary instance if it is a Cloud SQL instance.

Alternatively, if the instance is an external instance, set `wal_level=logical`.

Otherwise, you may see `ERROR: all replication slots are in use`, along with the helpful `HINT: Free one or increase max_replication_slots`.

### Set up native PostgreSQL logical replication

Since PostgreSQL 10, PostgreSQL supports native built-in logical replication. To set up native logical replication, logical decoding must be enabled on the primary instance, by setting `cloudsql.logical_decoding=on` on a Cloud SQL instance, or `wal_level=logical` on an external instance. Note that modification of these flags requires a restart of the primary instance.

Ensure that your instances are properly configured (for network connectivity, etc.) by reviewing the sections in Configure your PostgreSQL instance. This page provides steps for a proof-of-concept. If you encounter any issues while following steps in those sections, see Troubleshoot pglogical. For more information, see [Logical Replication](https://www.postgresql.org/docs/current/static/logical-replication.html) in the PostgreSQL documentation.

#### Create a table with data to replicate

Native PostgreSQL logical replication supports an entire database or just individual tables. As an example, we'll create a dummy table on the primary instance and populate it with data to test.
    
    
    CREATE TABLE native_test (id SERIAL PRIMARY KEY, data text);
    INSERT INTO native_test (data) VALUES ('apple'), ('banana'), ('cherry');
    

The table must also be created on the replica instance.

#### Create a publication on the primary instance

Native PostgreSQL logical replication deals with publishers and subscribers. Create a publication of the data in `native_test`:
    
    
    CREATE PUBLICATION pub FOR TABLE native_test;
    

#### Create a subscription on the replica instance

Here is an example of creating a subscription on the replica instance:
    
    
    CREATE SUBSCRIPTION sub
        CONNECTION 'host=<primary-ip> port=5432 dbname=postgres user=replication_user password=replicapassword'
        PUBLICATION pub;
    

Creating the subscription on the replica instance requires the `cloudsqlsuperuser` role. After creating the subscription, query the `native_test` table to verify that the data has appeared in the replica instance.

On the primary, you can query the `pg_replication_slots` table to see the replication slot created by the subscription.

#### Cleanup

Once your test is successful, drop the subscription on the replica using `DROP SUBSCRIPTION sub;`. Verify that the replication slot is also dropped on the primary. Otherwise WAL segments continue to accumulate on the primary instance.

#### Limitations on native PostgreSQL logical replication

Access to the `subconninfo` column of the [pg_subscription](https://www.postgresql.org/docs/current/static/catalog-pg-subscription.html) system table is unavailable.

Running `pg_dump` cannot dump information about subscriptions because it checks whether the connecting user has superuser permissions.

### Receive decoded WAL changes for change data capture (CDC)

As an alternative use case for CDC, logical decoding can stream changes from a PostgreSQL instance. The standard tool used for this is [pg_recvlogical](https://www.postgresql.org/docs/current/static/app-pgrecvlogical.html).

You can use the `pg_recvlogical` tool to create a replication slot and to stream changes tracked by that slot. The format of the changes is determined by your choice of the decoding plugin. You can use:

  * [wal2json](https://github.com/eulerto/wal2json), to stream changes formatted as JSON, or

  * [test_decoding](https://www.postgresql.org/docs/current/static/test-decoding.html), to stream changes formatted with a barebones text format




#### Create replication slot

To create a replication slot, run:
    
    
    pg_recvlogical
      -h <instance_ip> \
      -U <replication_user> \
      -p 5432 \
      -d postgres \
      --slot test_slot \
      --create-slot \
      -P <decoder_plugin>
    

#### Stream changes

In one Cloud Shell terminal, run:
    
    
    pg_recvlogical
      -h <instance_ip> \
      -U <replication_user> \
      -p 5432 \
      -d postgres \
      --slot test_slot \
      --start \
      -f -
    

While in another Cloud Shell terminal, connect to your database and run the following commands:
    
    
    CREATE TABLE cdc_test (id SERIAL PRIMARY KEY, data text);
    INSERT INTO cdc_test (data) VALUES ('apple', 'banana');
    UPDATE cdc_test SET data = 'cherry' WHERE id = 2;
    DELETE FROM cdc_test WHERE id = 1;
    DROP TABLE cdc_test;
    

If you are using the `wal2json` decoder plugin, output similar to the following is displayed in the first Cloud Shell terminal:
    
    
    {"change":[]}
    {"change":[{"kind":"insert","schema":"public","table":"cdc_test","columnnames":["id","data"],"columntypes":["integer","text"],"columnvalues":[1,"apple"]},{"kind":"insert","schema":"public","table":"cdc_test","columnnames":["id","data"],"columntypes":["integer","text"],"columnvalues":[2,"banana"]}]}
    {"change":[{"kind":"update","schema":"public","table":"cdc_test","columnnames":["id","data"],"columntypes":["integer","text"],"columnvalues":[2,"cherry"],"oldkeys":{"keynames":["id"],"keytypes":["integer"],"keyvalues":[2]}}]}
    {"change":[{"kind":"delete","schema":"public","table":"cdc_test","oldkeys":{"keynames":["id"],"keytypes":["integer"],"keyvalues":[1]}}]}
    {"change":[]}
    

If you are using the `test_decoding` decoder plugin, output similar to the following is displayed in the first Cloud Shell terminal:
    
    
    BEGIN 19460
    COMMIT 19460
    BEGIN 19461
    table public.cdc_test: INSERT: id[integer]:1 data[text]:'apple'
    table public.cdc_test: INSERT: id[integer]:2 data[text]:'banana'
    COMMIT 19461
    BEGIN 19462
    table public.cdc_test: UPDATE: id[integer]:2 data[text]:'cherry'
    COMMIT 19462
    BEGIN 19463
    table public.cdc_test: DELETE: id[integer]:1
    COMMIT 19463
    BEGIN 19464
    COMMIT 19464
    

(Your transaction IDs may differ.)

#### Cleanup

After you complete your testing, drop the replication slot you created by running:
    
    
    pg_recvlogical
      -h <instance_ip> \
      -U <replication_user> \
      -p 5432 \
      -d postgres \
      --slot test_slot \
      --drop-slot
    

## Notes and limitations

The notes and limitations in this section apply to the logical replication and decoding features of Cloud SQL for PostgreSQL.

  * Instances that use [high availability (HA)](https://docs.cloud.google.com/sql/docs/postgres/high-availability) can't be used as replication subscribers, because they don't have a consistent outgoing IP address.

  * The `pglogical` extension doesn't work in instances that have [connector enforcement](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances#ConnectorEnforcement) enabled. This limitation doesn't apply to the instances that have [private service access](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access) configured.

  * When you restore an instance that has `cloudsql.logical_decoding` or `cloudsql.enable_pglogical` enabled, and is currently acting as a publisher for logical replication, you must disable replication to all target instances first. Otherwise, restoring to the instance fails with an error, but currently the details of the error are not visible.

  * When you restore a backup of an instance that had `cloudsql.logical_decoding` or `cloudsql.enable_pglogical` enabled (at the time of the backup), and you are restoring it to a new instance, the replication state is not restored to the new instance. You must reconfigure replication manually afterwards.

  * On a Cloud SQL instance with one or more Cloud SQL read replicas (using physical replication), if you enable `cloudsql.logical_decoding` or `cloudsql.enable_pglogical`, those flags are also enabled on the read replica.

    * For Cloud SQL for PostgreSQL versions 15 and earlier, Cloud SQL read replica instances can't act as publishers for logical replication because PostgreSQL doesn't support logical decoding on read replicas for those older versions. However, to ensure that the instances can serve as a replacement for the primary instance in the event of a promotion, the logical flags are still enabled on the read replica instances for these earlier versions.

    * Starting with Cloud SQL for PostgreSQL version 16, Cloud SQL read replica instances can act as publishers for logical replication, if the primary instance has the logical flags set. The logical subscriber can be a Cloud SQL instance or an external instance. However, row deletion and vacuum operations on the primary might delete tuples that are still needed by logical decoding on the read replica. In those cases, the logical replication slot on the read replica is [invalidated](https://github.com/postgres/postgres/commit/6af1793954e8c5e753af83c3edb37ed3267dd179) to avoid inconsistencies.

    * Enabling `cloudsql.logical_decoding` or `cloudsql.enable_pglogical` on the primary instance causes the flags to be enabled on all read replicas, and this causes the primary and read replicas to be restarted in close succession. To avoid this situation and control when each instance is restarted, you can (1) set the flags on each read replica in turn, and only then (2) set the flags on the primary instance.

    * Disabling `cloudsql.logical_decoding` or `cloudsql.enable_pglogical` on the primary instance does **not** cause the flags to be disabled on all read replicas. To disable the flags across the instances, you must perform the inverse of the steps described above: (1) disable the flags on the primary instance and then (2) disable the flags on each read replica in turn.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
