---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/dump-file-replication-from-external/
title: Use a dump file to set up replication from external databases \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:50.438976+00:00
---

# Use a dump file to set up replication from external databases  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/dump-file-replication-from-external/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use a dump file to set up replication from external databases Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes the process for setting up replication when you have a dump file that you created from your external server.

You must complete all the steps on this page. When finished, you can administer and monitor the source representation instance the same way as you would any other Cloud SQL instance.

## Before you begin

Before you start, you should have [configured the external server](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setting_up_the_external_server_for_replication), created the [source representation instance](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setup-source-instance), and set up the [Cloud SQL replica](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setup-replica-instance).

## Update permissions for the replication user

The replication user on the external server is configured to accept connections from any host (`%`). You should update this user account so that it can only be used with the Cloud SQL replica. Open a terminal on the external server and enter these commands:

###  mysql Client 
    
    
        UPDATE mysql.user
          SET Host='NEW_HOST'
          WHERE Host='OLD_HOST'
          AND User='USERNAME';
          GRANT REPLICATION SLAVE, EXECUTE
          ON *.* TO 'GCP_USERNAME'@'HOST';
        FLUSH PRIVILEGES;

###  example 
    
    
        UPDATE mysql.user
          SET Host='192.0.2.0'
          WHERE Host='%'
          AND User='replicationUser';
          GRANT REPLICATION SLAVE, EXECUTE
          ON *.* TO 'gcp_user'@'gmail.com';
        FLUSH PRIVILEGES;

Property | Description  
---|---  
NEW_HOST | Specify the outgoing IP of the Cloud SQL replica.  
OLD_HOST | The current value assigned to `Host` that you want to change.  
USERNAME | The replication user account on the external server.  
GCP_USERNAME | The username for the Google Cloud user account.  
HOST | The hostname for the Google Cloud user account.  
  
## Verify your replication settings

After your setup is complete, ensure that the Cloud SQL replica can replicate from the external server.

First, ensure that your external sync settings are correct. To do this, use the commands below to verify:

  * Connectivity between the Cloud SQL replica and external server
  * Replication user privileges
  * Version compatibility
  * The Cloud SQL replica is not already replicating
  * Binlogs are enabled on the external server
  * A global transaction identifier (GTID) is enabled



Open a terminal and enter these commands to verify external sync settings are correct:

###  curl 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data '{
                 "syncMode": "SYNC_MODE",
                 "skipVerification": "SKIP_VERIFICATION"
               }' \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_INSTANCE/verifyExternalSyncSettings

###  example 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data '{
                 "syncMode": "online"
               }' \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/myproject/instances/myreplica/verifyExternalSyncSettings

Property | Description  
---|---  
SYNC_MODE | `verifyExternalSyncSettings` verifies that you can keep the Cloud SQL replica and external server in sync after replication is set up. Sync modes include `EXTERNAL_SYNC_MODE_UNSPECIFIED`, `ONLINE`, and `OFFLINE`.  
SKIP_VERIFICATION | Whether or not to skip the built-in verification step before syncing your data. Only recommended if you have already [verified your replication settings](https://docs.cloud.google.com/sql/docs/mysql/replication/dump-file-replication-from-external#verify-replication).  
PROJECT_ID | The ID of your project in Google Cloud.  
REPLICA_INSTANCE | The ID of your Cloud SQL replica.  
  
## Export your database to a Cloud Storage bucket

You can populate a Cloud SQL replica with a `mysqldump` file located in a Cloud Storage bucket. These conditions apply:

  * You must use the `mysqldump` utility bundled with MySQL.
  * While `mysqldump` is running, do not perform any [DDL operations](https://dev.mysql.com/doc/refman/8.4/en/glossary.html#glos_ddl) on the external server. Doing so could cause inconsistencies in the export file.



To export your database to a Cloud Storage bucket, follow these steps:

  1. In Google Cloud, [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Open a terminal using a client that connects to the external database server and run the following command.



###  mysqldump 
    
    
        mysqldump \
            --host=EXTERNAL_HOST \
            --port=EXTERNAL_PORT \
            --user=USERNAME \
            --password=PASSWORD \
            --databases=DATABASE_LIST  \
            --hex-blob \
            SOURCE_DATA  \
            --no-autocommit \
            --default-character-set=utf8mb4 \
            --single-transaction \
            --set-gtid-purged=on \
            ADD_DROP_TABLE \
            ROUTINES \
            COMPRESS \
            GZIP \
            | gcloud storage cp - gs://BUCKET/DUMP_FILENAME

###  example 
    
    
        mysqldump \
            --host=192.0.2.1 \
            --port=3306 \
            --user=replicationUser \
            --password \
            --databases guestbook journal \
            --hex-blob \
            --master-data=1 \
            --no-autocommit \
            --default-character-set=utf8mb4 \
            --single-transaction \
            --compress \
            | gzip \
            | gcloud storage cp - gs://replica-bucket/external-database.sql.gz

Property | Description  
---|---  
EXTERNAL_HOST | The IPv4 or DNS address for the external server.  
EXTERNAL_PORT | The port for the external server. If the external server is hosted on Cloud SQL, this is `3306`.  
USERNAME | The name of the replication user account or user account on the external server that has database read permissions.  
PASSWORD | Replication user password.  
DATABASE_LIST | Space-separated list of all databases on the external server, except for the system databases (`sys`, `mysql`, `performance_schema`, and `information_schema`). Use the `SHOW DATABASES` MySQL command to list your databases.  
SOURCE_DATA | If you're using an earlier version of MySQL than 8.0.26, then use `--master-data` as the value for this parameter. For versions of MySQL that are 8.0.26 or higher, set the value of this parameter to `--source-data`.  
ADD_DROP_TABLE | If you want to add a `DROP TABLE` statement before each `CREATE TABLE` statement, include `--add-drop-table`.  
ROUTINES | If you want to show stored routines, such as procedures and functions, in the output for dumped databases, include `--routines`.  
COMPRESS | If you want to compress all information sent between the Cloud SQL replica and the external server, use `--compress`.  
GZIP | If you want to compress the dump file even more, use `| gzip`. If your database contains data that does not compress well, such as binary incompressible data or JPG images, don't use this.  
BUCKET | The name of the bucket you created in Step 1 to contain the dump file.  
DUMP_FILENAME | A file with this name is created in your bucket. This file contains the contents of the database on your external server.  
  
## Update the source representation instance with the file path of the Cloud Storage bucket

The source representation instance is a Cloud SQL instance that represents the source database server to the Cloud SQL replica. It's visible in the Google Cloud console and appears the same as a regular Cloud SQL instance, but it contains no data, requires no configuration or maintenance, and doesn't affect billing.

The `source.json` file contains information about the source representation instance.

###  REST 
    
    
    {
      "name": "PRIMARY_INSTANCE_NAME",
      "region": "REGION_NAME",
      "databaseVersion": "DB_NAME_AND_VERSION",
      "onPremisesConfiguration": {
        "hostPort": "IP_ADDRESS_AND_PORT",
        "selectedObjects": "SELECTED_OBJECTS",
        "username": "USERNAME",
        "password": "PASSWORD"
      },
      "dumpFilePath" :"DUMP_FILE_PATH"
    }

###  example 
    
    
    {
      "name": "cloudsql-source-instance",
      "region": "us-central1",
      "databaseVersion": "MYSQL_5_7",
      "onPremisesConfiguration": {
        "hostPort": "192.0.2.0:3306",
        "selectedObjects":[{"database":"db1"}, {"database":"db3"}],
        "username": "replicationUser",
        "password": "486#@%*@"
      },
      "dumpFilePath" :"gs://replica-bucket/source-database.sql.gz"
    }

Property | Description  
---|---  
PRIMARY_INSTANCE_NAME | The name of the Cloud SQL instance that's associated with the source representation instance.  
REGION_NAME | The name of the region that's assigned to the source representation instance.  
DB_NAME_AND_VERSION | The name and version number of the database that's associated with the source representation instance.  
IP_ADDRESS_AND_PORT | The IP address and port number reserved for the source representation instance.  
SELECTED_OBJECTS | An updated comma-separated list of objects, specifying databases that you're migrating from the source representation instance to the destination Cloud SQL instance.  
USERNAME | The username of the source representation instance.  
PASSWORD | The password of the source representation instance.  
DUMP_FILE_PATH | The path of the dump file that contains the contents of the database on your external server.  
  
For a list of the full set of parameters that you can use with the `source.json` file, see [REST Resource: instances](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances).

The `onPremisesConfiguration` parameter contains information that Cloud SQL needs to connect to the on-premises source. For more information about the values of this parameter, see [OnPremisesConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#OnPremisesConfiguration).

After you set up the Cloud SQL replica, you need to update your source representation instance with the file path of the Cloud Storage bucket.

###  REST 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @JSON_PATH \
             -X PATCH \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/SOURCE_REPRESENTATION_INSTANCE

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
JSON_PATH | The path of the `JSON` file that's stored in the Cloud Storage bucket. This file contains data about the source representation instance.  
PROJECT_ID | The ID of your project in Google Cloud.  
SOURCE_REPRESENTATION_INSTANCE | The name of the source representation instance.  
  
## Start replication on the external server

After you have verified that you can replicate from the external server, you are ready to perform the replication.

During the initial import process, do not perform any [DDL operations](https://dev.mysql.com/doc/refman/8.4/en/glossary.html#glos_ddl) on the external server. Doing so could cause inconsistencies during the import. After the import process completes, the replica uses the binary logs on the external server to catch up to the current state of the external server.

Open a terminal, log in using `gcloud`, then enter the `curl` command to replicate from the external server.

###  REST 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data '{
                 "syncMode": "SYNC_MODE",
                 "skipVerification": "SKIP_VERIFICATION"
               }' \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_INSTANCE/startExternalSync

###  example 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data '{
                 "syncMode": "online",
                 "skipVerification": false
               }' \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances/replica-instance/startExternalSync

Property | Description  
---|---  
SYNC_MODE | Verifies that you can keep the Cloud SQL replica and external server in sync after replication is set up.  
SKIP_VERIFICATION | Whether or not to skip the built-in verification step before syncing your data. Only recommended if you have already [verified your replication settings](https://docs.cloud.google.com/sql/docs/mysql/replication/dump-file-replication-from-external#verify-replication).  
PROJECT_ID | The ID of your project in Google Cloud.  
REPLICA_INSTANCE | The ID of your Cloud SQL replica.  
  
### Clean up your storage

If you replicated from a file in a bucket, you can remove this file and bucket. See the Cloud Storage documentation for [Deleting Objects](https://docs.cloud.google.com/storage/docs/deleting-objects) and [Deleting Buckets](https://docs.cloud.google.com/storage/docs/deleting-buckets).

## Proceed with replication

Once you start replication from the external server, you need to monitor replication and then complete your migration. To learn more, see [Monitoring replication](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#monitoring_replication).

## Troubleshoot

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
  * Learn about [promoting your Cloud SQL replica](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#promote-replica) to [promote the replica to a standalone instance and stop replicating from the external server](https://docs.cloud.google.com/sql/docs/mysql/migrate-data#migrating-to-sql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
