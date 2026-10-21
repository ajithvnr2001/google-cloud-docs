---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external/
title: Use a managed import to set up replication from external databases \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:05.142721+00:00
---

# Use a managed import to set up replication from external databases  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use a managed import to set up replication from external databases Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/managed-import-replication-from-external "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to set up and use a managed import for data when replicating from an external server to Cloud SQL.

You must complete all the steps on this page. When finished, you can administer and monitor the source representation instance the same way as you would any other Cloud SQL instance.

## Before you begin

Before you begin, complete these steps:

  1. [Configure the external server](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setting_up_the_external_server_for_replication).

  2. [Create the source representation instance](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setup-source-instance).

  3. [Set up the Cloud SQL replica](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setup-replica-instance).




## Update privileges for the replication user

The replication user on the external server is configured to accept connections from any host (`%`). Update this user account so that it can be used only with the Cloud SQL replica.

### Required privileges

There are four types of combinations of migrations and dumps.

  * **Type 1** : Continuous migration and managed dump
  * **Type 2** : Continuous migration and manual dump
  * **Type 3** : One-time migration and managed dump
  * **Type 4** : One-time migration and manual dump



The privileges for each type of migration and dump combination are listed below.

###  Type 1 

The user account must have the follow privileges:

  * [REPLICATION SLAVE](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_replication-slave)
  * [EXECUTE](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_execute)
  * [SELECT](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_replication-select)
  * [SHOW VIEW](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_show-view)
  * [REPLICATION CLIENT](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_replication-client)
  * [RELOAD](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_reload)
  * [TRIGGER](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_trigger)
  * **(For migrating from Amazon RDS and Amazon Aurora only)** [LOCK TABLES](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_lock_tables)



For MySQL version 8.0 and later, it's recommend to skip the `BACKUP ADMIN` privilege for optimal performance.

**Note:** For more information about these privileges, see [Privileges provided by MySQL](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html).

###  Type 2 

The user account must have the follow privileges:

  * [REPLICATION SLAVE](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_replication-slave)
  * [EXECUTE](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_execute)

**Note:** For more information about these privileges, see [Privileges provided by MySQL](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html).

###  Type 3 

The user account must have the follow privileges:

  * [SELECT](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_replication-select)
  * [SHOW VIEW](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_show-view)
  * [TRIGGER](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_trigger)
  * **(From migrating from sources with`GTID_MODE = ON` setting only)** [RELOAD](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_reload)



For MySQL version 8.0 and above, it's recommend to skip the `BACKUP ADMIN` privilege for optimal performance.

**Note:** For more information about these privileges, see [Privileges provided by MySQL](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html).

###  Type 4 

No privileges are required.

**Note:** For more information about these privileges, see [Privileges provided by MySQL](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html).

### Update privileges

To update privileges, open a terminal on the external server and enter the following commands.

###  mysql Client

For GTID: 
    
    
        UPDATE mysql.user
          SET Host='NEW_HOST'
          WHERE Host='OLD_HOST'
          AND User='USERNAME';
        GRANT REPLICATION SLAVE, EXECUTE, SELECT, SHOW VIEW, REPLICATION CLIENT,
        RELOAD ON _._ TO
        'USERNAME'@'HOST';
        FLUSH PRIVILEGES;

For binlog: 
    
    
        UPDATE mysql.user
        SET Host='NEW_HOST'
        WHERE Host='OLD_HOST'
        AND User='USERNAME';
        GRANT REPLICATION SLAVE, EXECUTE, SELECT, SHOW VIEW, REPLICATION CLIENT,
        RELOAD ON _._ TO 'GCP_USERNAME'@'HOST';
        FLUSH PRIVILEGES;

###  example 
    
    
    UPDATE mysql.user
      SET Host='192.0.2.0'
      WHERE Host='%'
      AND User='replicationUser';
    GRANT REPLICATION SLAVE, EXECUTE, SELECT, SHOW VIEW, REPLICATION CLIENT,
    RELOAD ON *.* TO 'username'@'host.com';
    FLUSH PRIVILEGES;
    

Property | Description  
---|---  
NEW_HOST | Specify the outgoing IP of the Cloud SQL replica.  
OLD_HOST | The current value assigned to `Host` that you want to change.  
USERNAME | The replication user account on the external server.  
GCP_USERNAME | The username for the user account.  
HOST | The hostname for the user account.  
  
## Verify your replication settings

After your setup is complete, ensure that the Cloud SQL replica can replicate from the external server.

The following external sync settings must be correct.

  * Connectivity between the Cloud SQL replica and external server
  * Replication user privileges
  * Version compatibility
  * The Cloud SQL replica is not already replicating
  * Binlogs are enabled on the external server
  * GTID is enabled if you are trying to do an external sync from an RDS external server and are using a Google Cloud bucket



To verify these settings, open a Cloud Shell terminal and enter the following commands:

###  curl 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data '{
                 "syncMode": "SYNC_MODE",
                 "syncParallelLevel": "SYNC_PARALLEL_LEVEL",
                 "selectedObjects": "SELECTED_OBJECTS",
                 "mysqlSyncConfig": {
                   "initialSyncFlags": "SYNC_FLAGS"
                 }
               }' \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_INSTANCE_ID/verifyExternalSyncSettings

###  example 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data '{
                 "syncMode": "online",
                 "syncParallelLevel": "optimal",
                 "selectedObjects":[{"database":"db1"}, {"database":"db2"}]
               }' \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/myproject/instances/myreplica/verifyExternalSyncSettings

###  example w/ sync flags 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data '{
                 "syncMode": "online",
                 "syncParallelLevel": "optimal",
                 "selectedObjects":[{"database":"db1"}, {"database":"db2"}],
                 "mysqlSyncConfig": {
                     "initialSyncFlags": [{"name": "max-allowed-packet", "value": "1073741824"}, {"name": "hex-blob"}, {"name": "compress"}]
                 }
               }' \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances/replica-instance/verifyExternalSyncSettings

These calls return a list of type `sql#externalSyncSettingErrorList`.

If the list is empty, then there are no errors. A response without errors appears like this:
    
    
      {
        "kind": "sql#externalSyncSettingErrorList"
      }

Property | Description  
---|---  
SYNC_MODE | Ensure that you can keep the Cloud SQL replica and the external server in sync after replication is set up. Sync modes include `EXTERNAL_SYNC_MODE_UNSPECIFIED`, `ONLINE`, and `OFFLINE`.  
SYNC_PARALLEL_LEVEL | Verify the setting that controls the speed at which data from tables of a database are transferred. The following values are available:

  * `min:` Takes the lowest amount of compute resources on the database. This is the slowest speed for transferring data.
  * `optimal:` Provides a balanced performance with an optimal load on the database.
  * `max:` Provides the highest speed for transferring data, but this might cause an increased load on the database.

**Note:** The default value for this parameter is `optimal` because this setting provides a good speed to transfer the data and it has a reasonable impact on the database. We recommend that you use this value.  
SYNC_FLAGS | A list of initial sync flags to verify. Only recommended if you plan on using custom sync flags when replicating from the source. For a list of allowed flags, see [Initial sync flags](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external#sync-flags).  
SELECTED_OBJECTS | A comma-separated list of objects, specifying databases that you're migrating from the source representation instance to the destination Cloud SQL instance. If you don't use this parameter or provide an empty list as the value for the parameter, then all databases are migrated from the source to the destination.  
PROJECT_ID | The ID of your Google Cloud project.  
REPLICA_INSTANCE_ID | The ID of your Cloud SQL replica.  
  
## Update a source representation instance

To update the databases that you want to migrate from the source representation instance to the destination Cloud SQL instance, update the list of database names that are associated with the `selectedObjects` parameter. If you don't use this parameter or provide an empty list as the value for the parameter, then all databases are migrated from the source to the destination.

###  source.json 
    
    
        {
          "name": "SOURCE_NAME",
          "region": "REGION",
          "databaseVersion": "DATABASE_VERSION",
          "onPremisesConfiguration": {
            "selectedObjects": "SELECTED_OBJECTS",
            "username": "USERNAME",
            "password": "PASSWORD"
          }
        }

###  example 
    
    
    // example of source.json for external server that
    // - initiates replication from a Cloud SQL managed import
    // - doesn't use SSL/TLS
    
    {
      "name": "cloudsql-source-instance",
      "region": "us-central1",
      "databaseVersion": "POSTGRES_9_6",
      "onPremisesConfiguration": {
        "selectedObjects":[{"database":"db1"}, {"database":"db3"}],
        "username": "newReplicationUser",
        "password": "525#@%*@"
      }
    }
    

Property | Description  
---|---  
SOURCE_NAME | The name of the source representation instance.  
REGION | The [region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) where the source representation instance resides.  
DATABASE_VERSION | The database version running on your external server. The options are `MYSQL_5_6`, `MYSQL_5_7`, `MYSQL_8_0`, or `MYSQL_8_4`  
SELECTED_OBJECTS | An updated comma-separated list of objects, specifying databases that you're migrating from the source representation instance instance to the destination Cloud SQL instance.  
USERNAME | The replication user account on the external server.  
PASSWORD | The password for the account.  
  
Then, to modify the source representation instance in Cloud SQL, open a Cloud Shell terminal and enter the following commands:

###  curl 
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data @JSON_PATH \
         -X PATCH \
         https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/SOURCE_NAME
    

###  example 
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data @./source.json \
         -X PATCH \
         https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances/cloudsql-source-instance
    

Property | Description  
---|---  
JSON_PATH | The path to the `JSON` file that contains the request data for the external server.  
PROJECT_ID | The ID of your Google Cloud project.  
SOURCE_NAME | The name of the source representation instance.  
  
## Global read lock permission

If you don't have permission to access the global read lock on the external server, as might be the case with Amazon RDS and Amazon Aurora, pause writes to your server as described in the following steps:

  1. Go to the [Logs Explorer](https://console.cloud.google.com/logs/query), and select your Cloud SQL replica from the resource list. You should see a list of the most recent logs for your Cloud SQL replica. Ignore them for now.
  2. Open a terminal and enter the commands in [Start replication on the external server](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external#replicate-source-server) to replicate from the external server.
  3. Return to the Logs Explorer. When you see the log as follows, stop writing to the database on your external server. In most cases, this is required only for a few seconds.
         
         DUMP_IMPORT(START): Start importing data, please pause any write to the
            external primary database.
         

  4. When you see the following log entry in Logs Explorer, re-enable writing to the database on your external server.
         
         DUMP_IMPORT(SYNC): Consistent state on primary and replica. Writes to the
            external primary may resume.
         




## Start replication on the external server

After verifying that you can replicate from the external server, start the replication. The speed for performing the replication for the initial import process is up to 500 GB per hour. However, this speed can vary based on the machine tier, data disk size, network throughput, and nature of your database.

**Caution:** When you initiate an import from a database on a managed service, such as Amazon RDS or Amazon Aurora, Cloud SQL instructs you to stop writes for a few seconds so that the data dump is consistent. To avoid downtime for writes to your managed service primary instance, you can select a read replica as your replication source instead of the primary instance. During the phase when stopping writes is required, you can temporarily stop replication to the source read replica and then resume replication once the stop writes phase is over.

During the initial import process, do not perform any [DDL operations](https://dev.mysql.com/doc/refman/8.4/en/glossary.html#glos_ddl) on the external server. Doing so could cause inconsistencies during the import. After the import process completes, the replica uses the binary logs on the external server to catch up to the current state of the external server.

###  curl 
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data '{
             "syncMode": "SYNC_MODE",
             "skipVerification": "SKIP_VERIFICATION",
             "syncParallelLevel": "SYNC_PARALLEL_LEVEL",
             "mysqlSyncConfig": {
               "initialSyncFlags": "SYNC_FLAGS"
             }
           }' \
         -X POST \
         https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_INSTANCE_ID/startExternalSync
    

###  example 
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data '{
             "syncMode": "online",
             "syncParallelLevel": "optimal"
           }' \
         -X POST \
         https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances/replica-instance/startExternalSync
    

###  example w/ sync flags 
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data '{
             "syncMode": "online",
             "syncParallelLevel": "optimal"
             "skipVerification": false,
             "mysqlSyncConfig": {
                 "initialSyncFlags": [{"name": "max-allowed-packet", "value": "1073741824"}, {"name": "hex-blob"}, {"name": "compress"}]
                 }
           }' \
         -X POST \
         https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances/replica-instance/startExternalSync
    

Property | Description  
---|---  
SYNC_MODE | Verify that you can keep the Cloud SQL replica and the external server in sync after replication is set up.  
SKIP_VERIFICATION | Whether to skip the built-in verification step before syncing your data. This parameter is recommended only if you have already [verified your replication settings](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external#verify-replication).  
SYNC_PARALLEL_LEVEL | Provide a setting that controls the speed at which data from tables of a database are transferred. The following values are available:

  * `min:` Takes the lowest amount of compute resources on the database. This is the slowest speed for transferring data.
  * `optimal:` Provides a balanced performance with an optimal load on the database.
  * `max:` Provides the highest speed for transferring data, but this might cause an increased load on the database.

**Note:** The default value for this parameter is `optimal` because this setting provides a good speed to transfer the data and it has a reasonable impact on the database. We recommend that you use this value.  
SYNC_FLAGS | A list of initial sync flags to verify. Only recommended if you plan on using custom sync flags when replicating from the source. For a list of allowed flags, see [Initial sync flags](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external#sync-flags).  
PROJECT_ID | The ID of your Google Cloud project.  
REPLICA_INSTANCE_ID | The ID of your Cloud SQL replica.  
  
### Initial sync flags

To migrate with custom database flags, you can use the following allowed flags:

  * \--add-drop-database
  * \--add-drop-table
  * \--add-drop-trigger
  * \--add-locks
  * \--allow-keywords
  * \--all-tablespaces
  * \--apply-slave-statements
  * \--column-statistics
  * \--comments
  * \--compact
  * \--compatible
  * \--complete-insert
  * \--compress
  * \--compression-algorithms
  * \--create-options
  * \--default-character-set
  * \--delayed-insert
  * \--disable-keys
  * \--dump-date
  * \--events
  * \--extended-insert
  * \--fields-enclosed-by
  * \--fields-escaped-by
  * \--fields-optionally-enclosed-by
  * \--fields-terminated-by
  * \--flush-logs
  * \--flush-privileges
  * \--force
  * \--get-server-public-key
  * \--hex-blob
  * \--ignore-error
  * \--ignore-read-lock-error
  * \--ignore-table
  * \--insert-ignore
  * \--lines-terminated-by
  * \--lock-all-tables
  * \--lock-tables
  * \--max-allowed-packet
  * \--net-buffer-length
  * \--network-timeout
  * \--no-autocommit
  * \--no-create-db
  * \--no-create-info
  * \--no-data
  * \--no-defaults
  * \--no-set-names
  * \--no-tablespaces
  * \--opt
  * \--order-by-primary
  * \--pipe
  * \--quote-names
  * \--quick
  * \--replace
  * \--routines
  * \--secure-auth
  * \--set-charset
  * \--shared-memory-base-name
  * \--show-create-skip-secondary-engine
  * \--skip-opt
  * \--ssl-cipher
  * \--ssl-fips-mode
  * \--ssl-verify-server-cert
  * \--tls-ciphersuites
  * \--tls-version
  * \--triggers
  * \--tz-utc
  * \--verbose
  * \--xml
  * \--zstd-compression-level



For allowed values, see the [MySQL public docs](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html).

## Monitor the migration

Once you start replication from the external server, you need to monitor replication. To learn more, see [Monitoring replication](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#monitor_replication). You can then complete your migration.

## Troubleshoot

Consider the following troubleshooting options:

Issue | Troubleshooting | Read replica didn't start replicating on creation. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.   
---|---  
Unable to create read replica - invalidFlagValue error. | One of the flags in the request is invalid. It could be a flag you provided explicitly or one that was set to a default value. First, check that the value of the `max_connections` flag is greater than or equal to the value on the primary. If the `max_connections` flag is set appropriately, [inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.  
Unable to create read replica - unknown error. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error. If the error is: `set Service Networking service account as servicenetworking.serviceAgent role on consumer project`, you can manually create the service account necessary by following the instructions in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).  
Disk is full. | The primary instance disk size can become full during replica creation. [ Edit the primary instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to upgrade it to a larger disk size.   
The replica instance is using too much memory. | The replica uses temporary memory to cache often-requested read operations, which can lead it to use more memory than the primary instance. Restart the replica instance to reclaim the temporary memory space.  
Replication stopped. | The maximum storage limit was reached and automatic storage increase isn't enabled. [ Edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to enable `automatic storage increase`.  
Replication lag is consistently high. | The write load is too high for the replica to handle. Replication lag takes place when the SQL thread on a replica is unable to keep up with the IO thread. Some kinds of queries or workloads can cause temporary or permanent high replication lag for a given schema. Some of the typical causes of replication lag are: 

  * Slow queries on the replica. Find and fix them.
  * All tables must have a unique/primary key. Every update on such a table without a unique/primary key causes full table scans on th replica.
  * Queries like `DELETE ... WHERE field < 50000000` cause replication lag with row-based replication since a huge number of updates are piled up on the replica.

Some possible solutions include:

  * [ Configure parallel replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#configuring-parallel-replication).
  * Set the [innodb_flush_log_at_trx_commit](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-i) flag on the read replica to 2. See [Tips for working with flags](https://docs.cloud.google.com/sql/docs/mysql/flags#tips) for more information about this flag.
  * [ Edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to increase the size of the replica.
  * Reduce the load on the database.
  * Send read traffic to the read replica.
  * Index the tables.
  * Identify and fix slow write queries.
  * Recreate the replica.

  
Replication lag suddenly spikes. | This is caused by long-running transaction(s). When a transaction (single statement or multi-statements) commits on the source instance, the start time of the transaction is recorded in the binary log. When the replica receives this binlog event, it compares that timestamp with the current timestamp to calculate replication lag. Hence, a long-running transaction on the source would result in an immediate large replication lag on the replica. If the amount of row changes in the transaction is large, the replica would also spend a long time to execute it. During the time, replication lag is increasing. Once the replica finishes this transaction, the catch up period would depend on the write workload on the source and the replica's processing speed. To avoid a long transaction, some possible solutions include:

  * Break the transaction into multiple small transactions 
  * Chunk a single large write query into smaller batches 
  * Try to separate long SELECT queries from a transaction mixed with DMLs 

  
Changing parallel replication flags results in an error. | An incorrect value is set for one of or more of these flags. On the primary instance that's displaying the error message, set the parallel replication flags:

  1. Modify the `binlog_transaction_dependency_tracking` and `transaction_write_set_extraction`flags: 
     * `binlog_transaction_dependency_tracking=COMMIT_ORDER`
     * `transaction_write_set_extraction=OFF`
  2. Add the `slave_pending_jobs_size_max` flag: `slave_pending_jobs_size_max=33554432`
  3. Modify the `transaction_write_set_extraction` flag: `transaction_write_set_extraction=XXHASH64`
  4. Modify the `binlog_transaction_dependency_tracking` flag: `binlog_transaction_dependency_tracking=WRITESET`

  
Replica creation fails with timeout. | Long-running uncommitted transactions on the primary instance can cause read replica creation to fail. Recreate the replica after stopping all running queries.  
  
Additionally, for MySQL, also consider the following options: 

Issue | Troubleshooting | `Lost connection to MySQL server during query when dumping table`. | The source may have become unavailable, or the dump contained packets too large. Make sure the external primary is available to connect. You can also modify the values of the [net_read_timeout](https://dev.mysql.com/doc/refman/8.4/en/server-system-variables.html#sysvar_net_read_timeout) and [net_write_timeout](https://dev.mysql.com/doc/refman/8.4/en/server-system-variables.html#sysvar_net_write_timeout) flags on the source instance to stop the error. For more information on the allowable values for these flags, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags). To learn more about using `mysqldump` flags for managed import migration, see [ Allowed and default initial sync flags](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external#sync-flags)  
---|---  
Initial dump fails with timeout or lost connection errors (for example, `Dump timeout` or `Lost connection to MySQL server`). | This error can occur if one or more DDL statements interact with the parallel dump process, causing the process to wait indefinitely. **Resolution:** Don't execute DDL statements on the source database during the initial dump phase. Before you execute any DDL statements, restart the migration and wait for the initial dump phase to complete.  
The initial data migration was successful, but no data is being replicated. | One possible root cause could be your source database has defined replication flags which result in some or all database changes not being replicated over. Make sure the replication flags such as `binlog-do-db`, `binlog-ignore-db`, `replicate-do-db` or `replicate-ignore-db` are not set in a conflicting way. Run the command `show master status` on the primary instance to see the current settings.  
The initial data migration was successful but data replication stops working after a while. | Things to try:

  * Check the [ replication metrics](https://console.cloud.google.com/monitoring/dashboards/resourceList/cloudsql_database) for your replica instance in the Cloud Monitoring section of the Google Cloud console.
  * The errors from the MySQL IO thread or SQL thread can be found in [Cloud Logging](https://console.cloud.google.com/logs) in the `mysql.err` log files.
  * The error can also be found when connecting to the replica instance. Run the command `SHOW REPLICA STATUS`, and check for the following fields in the output: 
    * `Replica_IO_Running`
    * `Replica_SQL_Running`
    * `Last_IO_Error`
    * `Last_SQL_Error`

If you find the error `Unknown database DATABASE_NAME on query. Error_code: MY-001049`, then replication has failed due to a replicated SQL statement attempting to reference a database that wasn't selected for the migration. To recover replication, determine whether the error based on the message is due to DDL on one of the following objects:

  * An event or routine. You can run [`CALL mysql.skipReplicationError()`](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures#skipReplicationError) on the replica, which will prevent the event or routine from being replicated and resume replication.
  * A foreign key constraint or view. After you determine on which database the object modified by the statement resides, you have two options for recovery. You can either remove the database from the selected databases that are being migrated, or you can run [`CALL mysql.skipReplicationError()`](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures#skipReplicationError) on the replica to resume replication while skipping the constraint or propagation of the view to the replica.

  
`mysqld check failed: data disk is full`. | The data disk of the replica instance is full. Increase the disk size of the replica instance. You can either manually increase the disk size or enable auto storage increase.  
  
### Review your replication logs

When you verify your replication settings, logs are produced.

You can view these logs by following these steps:

  1. Go to the Logs Viewer in the Google Cloud console. 

[Go to the Logs Viewer](https://console.cloud.google.com/logs?resource=cloudsql_database)

  2. Select the Cloud SQL replica from the **Instance** dropdown.
  3. Select the `replication-setup.log` log file.



If the Cloud SQL replica is unable to connect to the external server, confirm the following:

  * Any firewall on the external server is configured to allow connections from the Cloud SQL replica's outgoing IP address.
  * Your SSL/TLS configuration is correct.
  * Your replication user, host, and password are correct.



## What's next

  * Learn about [updating an instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance).
  * Learn about [managing replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas).
  * Learn about [monitoring instances](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance).
  * Learn about [promoting your Cloud SQL replica](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#promote-replica).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
