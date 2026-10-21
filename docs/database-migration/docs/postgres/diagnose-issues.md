---
url: https://docs.cloud.google.com/database-migration/docs/postgres/diagnose-issues/
title: Diagnose issues for homogeneous migrations to Cloud SQL for PostgreSQL \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:37.040565+00:00
---

# Diagnose issues for homogeneous migrations to Cloud SQL for PostgreSQL  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/diagnose-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Diagnose issues for homogeneous migrations to Cloud SQL for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

The migration job process might incur errors during runtime.

  * Some errors, such as a bad password on the source database, are recoverable, meaning they can be fixed and the migration job resumes automatically.
  * Some are unrecoverable, such as errors in data replication, meaning the migration job needs to be restarted from the beginning.



When an error occurs, the migration job status changes to `Failed`, and the substatus reflects the last status before failure.

To troubleshoot an error, navigate to the failed migration job to view the error and follow the steps outlined in the error message.

To view more details about the error, navigate to Cloud Monitoring using the link on the migration job. The logs are filtered to the specific migration job.

In the following table, you can find some examples of issues and how they can be solved:

For this problem... | The issue might be... | Try this...  
---|---|---  
When you migrate to [an existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance), you receive the following error message: `The destination instance contains existing data or user defined entities (for example databases, tables, or functions). You can only migrate to empty instances. Clear your destination instance and retry the migration job.` | Your destination Cloud SQL instance contains extra data. You can only migrate to existing instances that are empty. See [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations#existing-instance-limitations). | Promote your destination instance to make it a read/write instance, remove the extra data, and re-try the migration job. See Clear extra data from your existing destination instance.   
Failure connecting to the source database instance.  | There was a connectivity issue between the source database instance and the destination instance. | Follow the steps in [Debugging connectivity](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-connectivity).  
Failure running migration job due to incompatible source and destination database versions.  | The source and destination database versions aren't a supported combination. Specifically, the source database version provided is incompatible with the destination database version. | Make sure that the [destination database version](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest) is the same or one major version above the source database version. Then, create a new migration job.  
Data definition languages (DDLs) or data manipulation languages (DMLs) are blocked on the source.  | DDLs that require the `ACCESS EXCLUSIVE` [lock](https://www.postgresql.org/docs/10/explicit-locking.html#LOCKING-TABLES) and are running during the full dump phase are blocked. | During the initial sync process (full dump), DDLs or programs requiring `ACCESS EXCLUSIVE` [locks](https://www.postgresql.org/docs/10/explicit-locking.html#LOCKING-TABLES) such as `ALTER TABLE` or `DROP TABLE` should be avoided on the tables. Otherwise, the DDLs or programs will wait until the initial sync finishes. For example, if a table is still in the initial sync process and an `ALTER TABLE` command is executed on the same table, then the command won't be run and subsequent DDL and DML commands will be blocked until the initial sync finishes.  
Error Message: `No pglogical extension installed on databases (X)` | One or more source databases doesn't have `pglogical` installed. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database#pglogical) to install `pglogical` on the databases on the source instance.  
When migrating to PostgreSQL version 15, after multiple subsequent connection retry attempts one of the following symptoms occur: 

  * You receive a `Cannot connect to invalid database` error message. 
  * The [Storage usage migration job metric](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics) shows no progress after a long time when the migration job is performing the full database dump. 

|  This problem is often attributed to the deadlock issue in the `pglogical` extension. For more information, see the [`pglogical` issue tracker in GitHub](https://github.com/2ndQuadrant/pglogical/issues/418).  | Retry the migration job, or migrate to an intermediate PostgreSQL version first. For more details, see Error message: `Cannot connect to invalid database`.   
Error Message: `Replication user 'x' doesn't have sufficient privileges.` | The user who's using Database Migration Service doesn't have the required privileges to perform the designated operation. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database#pglogical) to ensure that this user has the required privileges.  
Error Message: `Unable to connect to source database server.` | Database Migration Service can't establish a connection to the source database server. | Make sure that the source and destination database instances can communicate with each other, and that you've completed all of the required prerequisites that appeared when you [defined your settings for the migration job](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#src).  
Error Message: `The source database 'wal_level' configuration must be equal to 'logical'.` | The `wal_level` for the source database is set to a value other than `logical`. | Set the `wal_level` to `logical`. See [WAL level configuration](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-WAL-LEVEL).  
Error Message: `The source database 'max_replication_slots' configuration is not sufficient.` | The `max_replication_slots` parameter wasn't configured correctly. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database#pglogical) to set this parameter correctly.  
Error Message: `The source database 'max_wal_senders' configuration is not sufficient.` | The `max_wal_senders` parameter wasn't configured correctly. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database#pglogical) to set this parameter correctly.  
Error Message: `The source database 'max_worker_processes' configuration is not sufficient.` | The `max_worker_processes` parameter wasn't configured correctly. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database#pglogical) to set this parameter correctly.  
Error Message: `Cleanup may have failed on source due to error: generic::unknown: failed to connect to on-premises database.` OR  Error Message: `Error promoting EM replica: finished drop replication with errors.` | The settings needed for replication can't be cleaned up during the promotion of a migration job. | For each database, run commands as a user with the `superuser` privilege. For more information about which commands to run, see Clean up replication slots.  
Error Message: `x509 certificate signed by unknown authority.` | The source CA certificate provided to Database Migration Service might contain only the root certificate. However, the source certificate requires both the root certificate and any intermediate certificates. For example, for Amazon Relational Database Service, using the [rds-ca-2019-root.pem](https://s3.amazonaws.com/rds-downloads/rds-ca-2019-root.pem) certificate might result in this issue. | Create a combined source CA certificate that contains both the root certificate and all required intermediate certificates. For the Amazon Relational Database Service use case, instead of the [rds-ca-2019-root.pem](https://s3.amazonaws.com/rds-downloads/rds-ca-2019-root.pem) certificate, use the [rds-combined-ca-bundle.pem](https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem) certificate.  
Error Message: `ERROR: Out of shared memory HINT: You might need to increase max_locks_per_transaction.` | The value set for the [`max_locks_per_transaction`](https://www.postgresql.org/docs/13/runtime-config-locks.html) parameter isn't sufficient. | Set the value for this parameter to be at least {`max_number_of_tables_per_database`}/(`max_connections` \+ `max_prepared_transactions`).  
Error Message: `ERROR: no data left in message.` | The pglogical package isn't installed correctly on the source instance. | For more information on how to install this package properly, see [Install the pglogical package on the source instance](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database#pglogical).  
Error Message: `Cannot assign TransactionIds during recovery.` | The source that's configured is in recovery mode. | Configure a source that isn't in recovery mode.  
The full dump is slow. | The Cloud SQL destination might be slow in importing large data from the source database. | 

  * When creating the destination, set the data disk size so that it's close to the final size. The full dump phase uses an I/O write-intensive workload, and a larger disk size has a better I/O performance. For more information, see [Block storage performance](https://docs.cloud.google.com/compute/docs/disks/performance).
  * Choose a higher tier for the Cloud SQL destination to get the maximum available network and disk bandwidth.
  * Tune the Cloud SQL destination's [`max_wal_size`](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-MAX-WAL-SIZE) flag. Typically, 32 GB or 64 GB is a good value to set for this flag. Updating this flag doesn't require you to restart the server.

  
Error Message: `subscriber {subscriber_name} initialization failed during nonrecoverable step (d), please try the setup again` | The migration job failed during the full dump phase and the job isn't recoverable. The source database instance was restarted or in recovery mode, or the replication connections ended because of an insufficient value set for the [`wal_sender_timeout`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) parameter. To find the root cause of the problem:

  1. Go to the [Logs Explorer](https://console.cloud.google.com/logs/query) page in the Google Cloud console.
  2. From the resource list, select your Cloud SQL replica. A list of the most recent logs for the replica appears.
  3. From the log file names, select `postgres.log`.
  4. Set the log's severity level to all levels above `Warning`. The first error logs may be the root cause of the failure.

| 

  * Make sure that Database Migration Service can always connect to the source database instance during the full dump phase.
  * Check if the value of the `wal_sender_timeout` parameter is set to a larger number (for example, `0`) on the source database instance.
  * Restart the migration job, and then try again.

  
Error Message: `ERROR: unknown column name {column_name}` | A column was added to a replicated table on the primary node but not on the replica node. |  Only data manipulation language (DML) changes are updated automatically during continuous migrations. Managing data definition language (DDL) changes so that the source and destination databases remain compatible is the responsibility of the user, and can be achieved in two ways:

  * Stop writes to the source database and run the DDL commands in both source and destination. Before running the DDL commands on the destination, grant the `cloudsqlexternalsync` role to the Cloud SQL user applying the DDL changes.
  * Use `pglogical.replicate_ddl_command` to allow DDL commands to be run on the source and destination at a consistent point. The user running the commands must have the same username on both the source and the destination, and should be the superuser or the owner of the artifact being migrated (for example, the table, sequence, view, or database).

See [Continuous migration](https://docs.cloud.google.com/database-migration/docs/postgres/migration-fidelity#continuous_migration) to find examples of using `pglogical.replicate_ddl_command`.  
Error Message: `ERROR: cannot truncate a table referenced in a foreign key constraint` | The user tried to truncate a table that has a foreign key constraint. |  Remove the foreign key constraint first, and then truncate the table.  
Error Message: `ERROR: connection to other side has died` | The replication connection ended because of an insufficient value set for the `wal_sender_timeout` parameter. The error usually occurs during the replication phase after the success of the initial dump. |  Consider increasing the [`wal_sender_timeout`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) parameter value or disable the timeout mechanism by setting its value to `0` on the source database instance.  
Warning Message: `migration job test configuration has returned the following warnings: Some table(s) have limited support.` | Source has tables with limited support, for example tables without primary keys. |  This is a warning message. You can proceed with the migration, but note that unsupported entities (for example tables without primary keys) don't get migrated. For more information, review [Configure your source databases](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database).   
When you migrate selected databases and the migration job is unable to replicate data to one or more databases, a **Failed** status is displayed in the list of databases. | Various migration job errors. | In the **Errors** column, click **View errors** and fix them. You can also remove the failed databases from the migration job. For more information about removing a failed database from a migration job, see [Manage migration jobs](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions).  
  
### Clear extra data from your existing destination instance

When you migrate to [an existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance), you receive the following error message: `The destination instance contains existing data or user defined entities (for example databases, tables, or functions). You can only migrate to empty instances. Clear your destination instance and retry the migration job.`

This issue can occur if your destination instance contains extra data. You can only migrate to existing instances that are empty. See [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations#existing-instance-limitations).

#### Things to try

Clear extra data from your destination instance and start the migration job again by performing the following steps:

  1. [Stop the migration job](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions).
  2. At this point, your destination Cloud SQL instance is in `read-only` mode. [Promote the destination instance](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#promote_the_replica) to gain write access. 
  3. [Connect to your destination Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/connect-overview).
  4. Remove extra data from your destination instance databases. Your destination can only contain system configuration data. Destination databases can't contain user data (such as tables). There are different SQL statements you can run on your databases to find non-system data, for example: 

#### Example SQL statement to retrieve non-system databases (click to expand)
         
         SELECT datname FROM pg_catalog.pg_database
         WHERE datname NOT IN ('cloudsqladmin', 'template1', 'template0', 'postgres');

#### Example SQL statement to retrieve non-system data in the `postgres` database (click to expand)

The `postgres` database is a system database, but it can contain non-system data. Make sure you run these statements on the `postgres` database. If you use the `psql` client to connect to the destination instance, you can switch to another database without resetting your connection by using the [`\connect {database_name_here}`](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMAND-C-LC) command.
         
         SELECT table_schema, table_name FROM information_schema.tables
         WHERE table_schema != 'information_schema' AND table_schema not like 'pg\_%';
         
         SELECT routine_schema, routine_name FROM information_schema.routines
         WHERE routine_schema != 'information_schema' AND routine_schema not like 'pg\_%';
         
         SELECT extname FROM pg_extension WHERE extname != 'plpgsql';
             

  5. [Start the migration job](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions).



* * *

### Clean up replication slots

You see one of the following messages: 

  * `Cleanup may have failed on source due to error: generic::unknown: failed to connect to on-premises database.`
  * `Error promoting EM replica: finished drop replication with errors.`



#### The issue might be

When promoting a Cloud SQL instance, if the source instance isn't reachable from the Cloud SQL instance (for example, the source instance isn't running, or you removed the Cloud SQL instance from the allow list of source instances), then the settings needed for the replication can't be cleaned up during the promotion of a migration job. You must clean up the replication slots manually.

#### Things to try

For each database, run the following commands as a user with the `superuser` privilege:

  1. Get the replication slot names from the error message, and then run the following command to drop the slots, one by one:
         
         SELECT pg_drop_replication_slot('slot_name');

  2. If the replication slot names aren't available in the error message, then run the following command to query for the existing replication slots:
         
         SELECT pg_drop_replication_slot(slot_name) FROM pg_replication_slots WHERE slot_name LIKE '%cloudsql%' AND active = 'f';

  3. If there are no Cloud SQL replicas using the source instance, then run the following command to clean up `pglogical` settings:
         
         SELECT pglogical.drop_node(node_name) FROM pglogical.node WHERE node_name LIKE 'cloudsql';

  4. If the `pglogical` extension isn't needed anymore, then run the following command to uninstall the extension:
         
         DROP EXTENSION IF EXISTS pglogical;




* * *

### Error message: `Cannot connect to invalid database`

When migrating to PostgreSQL version 15, after multiple subsequent connection retry attempts one of the following symptoms occur: 

  * You receive a `Cannot connect to invalid database` error message. 
  * The [Storage usage migration job metric](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics) shows no progress after a long time when the migration job is performing the full database dump. 



#### The issue might be

This problem is often attributed to the deadlock issue in the `pglogical` extension. For more information, see the [`pglogical` issue tracker in GitHub](https://github.com/2ndQuadrant/pglogical/issues/418).

#### Things to try

##### Perform the migration job again with a new destination instance

Try deleting the destination database where you experienced the issue and re-create your migration job. Follow these steps: 

  1. Delete the destination instance where you experienced the problems. See [Delete instances](https://docs.cloud.google.com/sql/docs/postgres/delete-instance) in Cloud SQL for PostgreSQL documentation.
  2. Delete the failed migration job. See [Review a migration job](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions).
  3. Re-create your migration job. See [Create a migration job](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job).



##### Migrate to an intermediate version

Consider migrating to an earlier PostgreSQL version, such as PostgreSQL 14. After a successful migration, you can upgrade to the desired PostgreSQL 15 instance. See [Upgrade the database major version by migrating data](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-migrate) in Cloud SQL for PostgreSQL documentation.

* * *

### Manage users and roles

#### Migrate existing users

Currently, Database Migration Service doesn't support migrating existing users from a source instance into a destination Cloud SQL instance. You can manage this migration by [creating the users in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users) manually.

#### About the `cloudsqlexternalsync` user

During the migration, all objects on the Cloud SQL replica are owned by the `cloudsqlexternalsync` user. After the data is migrated, you can modify the ownership of the objects to other users by completing the following steps:

  * Run the `GRANT cloudsqlexternalsync to {USER}` command.
  * On each database, run the `reassign owned by cloudsqlexternalsync to {USER};` command.
  * To remove the `cloudsqlexternalsync` user, run the `drop role cloudsqlexternalsync` command.



#### Import data into a new Cloud SQL instance

If you first [export data](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-sql) from a Cloud SQL instance that Database Migration Service migrated into Cloud Storage, and then [import the data](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-sql) from Cloud Storage into a stand-alone Cloud SQL instance, the import might fail because the `cloudsqlexternalsync` user doesn't exist on the destination instance.

To mitigate the issue, either [create the `cloudsqlexternalsync` user](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users) on the destination instance or remove the user from the migrated instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
