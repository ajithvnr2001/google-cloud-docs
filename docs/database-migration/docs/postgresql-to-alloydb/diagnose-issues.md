---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/diagnose-issues/
title: Diagnose issues in PostgreSQL to AlloyDB migrations \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:21.840360+00:00
---

# Diagnose issues in PostgreSQL to AlloyDB migrations  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/diagnose-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Resources ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/resources)



Send feedback 

#  Diagnose issues in PostgreSQL to AlloyDB migrations Stay organized with collections  Save and categorize content based on your preferences. 

## Troubleshoot migration errors

The migration job process might incur errors during runtime.

  * Some errors, such as a bad password on the source database, are recoverable, meaning they can be fixed and the migration job resumes automatically.
  * Some are unrecoverable, such as errors in data replication, meaning the migration job needs to be restarted from the beginning.



When an error occurs, the migration job status changes to `Failed`, and the substatus reflects the last status before failure.

To troubleshoot an error, navigate to the failed migration job to view the error and follow the steps outlined in the error message.

To view more details about the error, navigate to Cloud Monitoring using the link on the migration job. The logs are filtered to the specific migration job.

In the following table, you can find some examples of issues and how they can be solved:

Symptom | Possible causes | Things to try  
---|---|---  
Failure connecting to the source database instance.  | There was a connectivity issue between the source database instance and the destination instance. | Follow the steps in [Debugging connectivity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/debugging-connectivity).  
Failure running migration job due to incompatible source and destination database versions.  | The source and destination database versions aren't a supported combination. Specifically, the source database version provided is incompatible with the destination database version. | Make sure that the [destination database version](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest) is the same or one major version above the source database version. Then, create a new migration job.  
Data definition languages (DDLs) or data manipulation languages (DMLs) are blocked on the source.  | DDLs that require the `ACCESS EXCLUSIVE` [lock](https://www.postgresql.org/docs/10/explicit-locking.html#LOCKING-TABLES) and are running during the full dump phase are blocked. | During the initial sync process (full dump), DDLs or programs requiring `ACCESS EXCLUSIVE` [locks](https://www.postgresql.org/docs/10/explicit-locking.html#LOCKING-TABLES) such as `ALTER TABLE` or `DROP TABLE` should be avoided on the tables. Otherwise, the DDLs or programs will wait until the initial sync finishes. For example, if a table is still in the initial sync process and an `ALTER TABLE` command is executed on the same table, then the command won't be run and subsequent DDL and DML commands will be blocked until the initial sync finishes.  
Error Message: `No pglogical extension installed on databases (X)` | One or more source databases doesn't have `pglogical` installed. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database#pglogical) to install `pglogical` on the databases on the source instance.  
Error Message: `Replication user 'x' doesn't have sufficient privileges.` | The user who's using Database Migration Service doesn't have the required privileges to perform the designated operation. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database#pglogical) to ensure that this user has the required privileges.  
Error Message: `Unable to connect to source database server.` | Database Migration Service can't establish a connection to the source database server. | Make sure that the source and destination database instances can communicate with each other, and that you've completed all of the required prerequisites that appeared when you [defined your settings for the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job#src).  
Error Message: `The source database 'wal_level' configuration must be equal to 'logical'.` | The `wal_level` for the source database is set to a value other than `logical`.  | Set the `wal_level` to `logical`.  
Error Message: `The source database 'max_replication_slots' configuration is not sufficient.` | The `max_replication_slots` parameter wasn't configured correctly. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database#pglogical) to set this parameter correctly.  
Error Message: `The source database 'max_wal_senders' configuration is not sufficient.` | The `max_wal_senders` parameter wasn't configured correctly. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database#pglogical) to set this parameter correctly.  
Error Message: `The source database 'max_worker_processes' configuration is not sufficient.` | The `max_worker_processes` parameter wasn't configured correctly. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database#pglogical) to set this parameter correctly.  
Error Message: `Cleanup may have failed on source due to error: generic::unknown: failed to connect to on-premises database.` OR  Error Message: `Error promoting EM replica: finished drop replication with errors.` | The settings needed for replication can't be cleaned up during the promotion of a migration job. | For each database, run commands as a user with the `superuser` privilege. For more information about which commands to run, see Clean up replication slots.  
Error Message: `x509 certificate signed by unknown authority.` | The source CA certificate provided to Database Migration Service might contain only the root certificate. However, the source certificate requires both the root certificate and any intermediate certificates. For example, for Amazon Relational Database Service, using the [rds-ca-2019-root.pem](https://s3.amazonaws.com/rds-downloads/rds-ca-2019-root.pem) certificate might result in this issue. | Create a combined source CA certificate that contains both the root certificate and all required intermediate certificates. For the Amazon Relational Database Service use case, instead of the [rds-ca-2019-root.pem](https://s3.amazonaws.com/rds-downloads/rds-ca-2019-root.pem) certificate, use the [rds-combined-ca-bundle.pem](https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem) certificate.  
Error Message: `ERROR: Out of shared memory HINT: You might need to increase max_locks_per_transaction.` | The value set for the [`max_locks_per_transaction`](https://www.postgresql.org/docs/13/runtime-config-locks.html) parameter isn't sufficient. | Set the value for this parameter to be at least {`max_number_of_tables_per_database`}/(`max_connections` \+ `max_prepared_transactions`).  
Error Message: `ERROR: no data left in message.` | The pglogical package isn't installed correctly on the source instance. | For more information on how to install this package properly, see [Install the pglogical package on the source instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database#pglogical).  
Error Message: `Cannot assign TransactionIds during recovery.` | The source that's configured is in recovery mode. | Configure a source that isn't in recovery mode.  
The full dump is slow. | The AlloyDB destination might be slow in importing large data from the source database. | 

  * Choose a higher tier for the AlloyDB destination to get the maximum available network and disk bandwidth.
  * Tune the AlloyDB destination's `[max_wal_size](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-MAX-WAL-SIZE)` flag. Typically, 32 GB or 64 GB is a good value to set for this flag. Updating this flag doesn't require you to restart the server.

  
Error Message: `subscriber {subscriber_name} initialization failed during nonrecoverable step (d), please try the setup again` | The migration job failed during the full dump phase and the job isn't recoverable. The source database instance was restarted or in recovery mode, or the replication connections ended because of an insufficient value set for the [`wal_sender_timeout`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) parameter.  To find the root cause of the problem:

  1. Go to the [Logs Explorer](https://console.cloud.google.com/logs/query) page in the Google Cloud Console.
  2. From the resource list, select your AlloyDB instance. A list of the most recent logs for the instance appears.
  3. From the log file names, select `postgres.log`.
  4. Set the log's severity level to all levels above `Warning`. The first error logs may be the root cause of the failure.

| 

  * Make sure that Database Migration Service can always connect to the source database instance during the full dump phase.
  * Check if the value of the `wal_sender_timeout` parameter is set to a larger number (for example, `0`) on the source database instance.
  * Restart the migration job, and then try again.

  
Error Message: `ERROR: unknown column name {column_name}` | A column was added to a replicated table on the primary node but not on the replica node.  |  Only data manipulation language (DML) changes are updated automatically during continuous migrations. Managing data definition language (DDL) changes so that the source and destination databases remain compatible is the responsibility of the user, and can be achieved in two ways:

  * Stop writes to the source database and run the DDL commands in both source and destination. Before running the DDL commands on the destination, grant the `cloudsqlexternalsync` role to the Cloud SQL user applying the DDL changes.
  * Use the `pglogical.replicate_ddl_command` to allow DDL commands to be run on the source and destination at a consistent point. The user running the commands must have the same username on both the source and the destination, and should be the superuser or the owner of the artifact being migrated (for example, the table, sequence, view, or database).
See [Continuous migration](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-fidelity#continuous_migration) to find the examples of using the `pglogical.replicate_ddl_command.` 
  
Error Message: `ERROR: cannot truncate a table referenced in a foreign key constraint` | The user tried to truncate a table that has a foreign key constraint. |  Remove the foreign key constraint first, and then truncate the table.  
Error Message: `ERROR: connection to other side has died` | The replication connection ended because of an insufficient value set for the `wal_sender_timeout parameter`. The error usually occurs during the replication phase after the success of the initial dump. |  Consider increasing the [`wal_sender_timeout`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) parameter value or disable the timeout mechanism by setting its value to `0` on the source database instance.  
When you migrate selected databases and the migration job is unable to replicate data to one or more databases, a **Failed** status is displayed in the list of databases. | Various migration job errors. | In the **Errors** column, click **View errors** and fix them. You can also remove the failed databases from the migration job. For more information about removing a failed database from a migration job, see [Manage migration jobs](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions).  
  
### Clean up replication slots

You see one of the following messages: 

  * `Cleanup may have failed on source due to error: generic::unknown: failed to connect to on-premises database.`
  * `Error promoting EM replica: finished drop replication with errors.`



#### Possible causes

When promoting a AlloyDB instance, if the source instance isn't reachable from the AlloyDB instance (for example, the source instance isn't running, or you removed the AlloyDB instance from the allow list of source instances), then the settings needed for the replication can't be cleaned up during the promotion of a migration job. You must clean up the replication slots manually.

#### Things to try

For each database, run the following commands as a user with the `superuser` privilege:

  1. Get the replication slot names from the error message, and then run the following command to drop the slots, one by one:
         
         select pg_drop_replication_slot({slot_name});

  2. If the replication slot names aren't available in the error message, then run the following command to query for the existing replication slots:
         
         select pg_drop_replication_slot(slot_name) from pg_replication_slots where slot_name like '%alloydb%' and active = 'f';

  3. If there are no AlloyDB replicas using the source instance, then run the following command to clean up `pglogical` settings:
         
         select pglogical.drop_node(node_name) from pglogical.node where node_name like 'alloydb';

  4. If the `pglogical` extension isn't needed anymore, then run the following command to uninstall the extension:
         
         DROP EXTENSION IF EXISTS pglogical;




### Delete orphaned AlloyDB clusters in bootstrapping mode

In rare edge cases, you might find that your migration job has been deleted, while the associated AlloyDB cluster hasn't, and is still in the bootstrapping mode. It is possible to delete the cluster using [AlloyDB's gcloud command for deleting a cluster](https://docs.cloud.google.com/alloydb/docs/cluster-delete#procedure), combined with the `--force` option.

Note that deleting a bootstrapping cluster while it's being used by a migration job results in undefined behavior.

### Manage users and roles

#### Migrate existing users

Currently, Database Migration Service doesn't support migrating existing users from a source instance into a destination AlloyDB instance. You can manage this migration by [creating the users in AlloyDB](https://docs.cloud.google.com/alloydb/docs/database-users/about) manually.

#### About the `alloydbexternalsync` user

During the migration, all objects on the AlloyDB primary are owned by the `alloydbexternalsync` user. After the data is migrated, you can modify the ownership of the objects to other users by completing the following steps:

  * Run the `GRANT alloydbexternalsync to {USER}` command.
  * On each database, run the `reassign owned by alloydbexternalsync to {USER};` command.
  * To remove the `alloydbexternalsync` user, run the `drop role alloydbexternalsync` command.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
