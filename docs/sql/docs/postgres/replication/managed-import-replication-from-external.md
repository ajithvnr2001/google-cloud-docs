---
url: https://docs.cloud.google.com/sql/docs/postgres/replication/managed-import-replication-from-external/
title: Use a managed import to set up replication from external databases \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:35.817561+00:00
---

# Use a managed import to set up replication from external databases  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/replication/managed-import-replication-from-external/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Use a managed import to set up replication from external databases Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external "View this page for the MySQL database engine") | PostgreSQL | SQL Server

This page describes how to set up and use a managed import for data when replicating from an external server to Cloud SQL.

You must complete all the steps on this page. When finished, you can administer and monitor the source representation instance the same way as you would any other Cloud SQL instance.

## Before you begin

Before you begin, complete these steps:

  1. [Configure the external server](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#setting_up_the_external_server_for_replication).

  2. [Create the source representation instance](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#setup-source-instance).

  3. [Set up the Cloud SQL replica](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#setup-replica-instance).




## Verify your replication settings

After your setup is complete, ensure that the Cloud SQL replica can replicate from the external server.

The following external sync settings must be correct.

  * Connectivity between the Cloud SQL replica and external server
  * Replication user privileges
  * Version compatibility
  * The Cloud SQL replica is not already replicating



To verify these settings, open a Cloud Shell terminal and enter the following commands:

###  curl 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data '{
                 "syncMode": "SYNC_MODE",
                 "syncParallelLevel": "SYNC_PARALLEL_LEVEL",
                 "selectedObjects": "SELECTED_OBJECTS"
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
REGION | The [region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) where the source representation instance resides.  
DATABASE_VERSION | The database version running on your external server. The options are `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `POSTGRES_13`, `POSTGRES_14`, `POSTGRES_15`, `POSTGRES_16`, or `POSTGRES_17`.   
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
  
## Start replication on the external server

After verifying that you can replicate from the external server, start the replication. The speed for performing the replication for the initial import process is up to 500 GB per hour. However, this speed can vary based on the machine tier, data disk size, network throughput, and nature of your database.

###  curl 
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data '{
             "syncMode": "SYNC_MODE",
             "skipVerification": "SKIP_VERIFICATION",
             "syncParallelLevel": "SYNC_PARALLEL_LEVEL"
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
    

Property | Description  
---|---  
SYNC_MODE | Verify that you can keep the Cloud SQL replica and the external server in sync after replication is set up.  
SKIP_VERIFICATION | Whether to skip the built-in verification step before syncing your data. This parameter is recommended only if you have already [verified your replication settings](https://docs.cloud.google.com/sql/docs/postgres/replication/managed-import-replication-from-external#verify-replication).  
SYNC_PARALLEL_LEVEL | Provide a setting that controls the speed at which data from tables of a database are transferred. The following values are available:

  * `min:` Takes the lowest amount of compute resources on the database. This is the slowest speed for transferring data.
  * `optimal:` Provides a balanced performance with an optimal load on the database.
  * `max:` Provides the highest speed for transferring data, but this might cause an increased load on the database.

**Note:** The default value for this parameter is `optimal` because this setting provides a good speed to transfer the data and it has a reasonable impact on the database. We recommend that you use this value.  
PROJECT_ID | The ID of your Google Cloud project.  
REPLICA_INSTANCE_ID | The ID of your Cloud SQL replica.  
  
## Monitor the migration

Once you start replication from the external server, you need to monitor replication. To learn more, see [Monitoring replication](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#monitor_replication). You can then complete your migration.

## Troubleshoot

Consider the following troubleshooting options:

Issue | Troubleshooting | Read replica didn't start replicating on creation. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.   
---|---  
Unable to create read replica - invalidFlagValue error. | One of the flags in the request is invalid. It could be a flag you provided explicitly or one that was set to a default value. First, check that the value of the `max_connections` flag is greater than or equal to the value on the primary. If the `max_connections` flag is set appropriately, [inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.  
Unable to create read replica - unknown error. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error. If the error is: `set Service Networking service account as servicenetworking.serviceAgent role on consumer project`, you can manually create the service account necessary by following the instructions in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).  
Disk is full. | The primary instance disk size can become full during replica creation. [ Edit the primary instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to upgrade it to a larger disk size.   
Disk space increases significantly. | A slot that's not actively used to track data causes PostgreSQL to hold onto WAL segments indefinitely, causing the disk space to grow indefinitely. If you use the [logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) features in Cloud SQL, replication slots are created and dropped automatically. Unused replication slots can be detected by querying the [`pg_replication_slots`](https://www.postgresql.org/docs/current/static/view-pg-replication-slots.html) system view and filtering on the `active` column. Unused slots can be dropped to remove WAL segments using the [`pg_drop_replication_slot`](https://www.postgresql.org/docs/current/static/functions-admin.html#FUNCTIONS-REPLICATION) command.   
The replica instance is using too much memory. | The replica uses temporary memory to cache often-requested read operations, which can lead it to use more memory than the primary instance. Restart the replica instance to reclaim the temporary memory space.  
Replication stopped. | The maximum storage limit was reached and automatic storage increase isn't enabled. [ Edit the instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to enable `automatic storage increase`.  
Replication lag is consistently high. | The write load is too high for the replica to handle. Replication lag takes place when the SQL thread on a replica is unable to keep up with the IO thread. Some kinds of queries or workloads can cause temporary or permanent high replication lag for a given schema. Some of the typical causes of replication lag are: 

  * Slow queries on the replica. Find and fix them.
  * All tables must have a unique/primary key. Every update on such a table without a unique/primary key causes full table scans on th replica.
  * Queries like `DELETE ... WHERE field < 50000000` cause replication lag with row-based replication since a huge number of updates are piled up on the replica.

Some possible solutions include:

  * [ Edit the instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to increase the size of the replica.
  * Reduce the load on the database.
  * Send read traffic to the read replica.
  * Index the tables.
  * Identify and fix slow write queries.
  * Recreate the replica.

  
Errors when rebuilding indexes in PostgreSQL 9.6. | You get an error from PostgreSQL informing you that you need to rebuild a particular index. This can be done only on the primary instance. If you create a new replica instance, you soon get the same error again. [Hash indexes are not propagated to replicas](https://www.postgresql.org/docs/9.6/indexes-types.html) in PostgreSQL versions below 10. If you must use hash indexes, upgrade to PostgreSQL 10+. Otherwise, if you also want to use replicas, don't use hash indexes in PostgreSQL 9.6.  
Query on the primary instance is always running. | After creating a replica, the query `SELECT * from pg_stat_activity where state = 'active' and pid = XXXX and username = 'cloudsqlreplica'` is expected to run continuously on your primary instance.   
Replica creation fails with timeout. | Long-running uncommitted transactions on the primary instance can cause read replica creation to fail. Recreate the replica after stopping all running queries.  
If the primary instance and the replica have [different vCPU sizes](https://docs.cloud.google.com/sql/docs/postgres/instance-settings), then there might be query performance issues because the query optimizer takes vCPU sizes into account. |  To resolve this issue, complete the following steps:

  1. Turn on the [log_duration](https://docs.cloud.google.com/sql/docs/postgres/flags#postgres-l) flag and set the `log_statement` parameter to `ddl`. This provides you with both the queries and the run time on the database. However, depending on your workload, this might cause performance issues.
  2. On both the primary instance and the read replica, run `explain analyze` for the queries.
  3. Compare the query plan and check for differences.

If this is a specific query, then modify the query. For example, you can change the order of the joins to see if you get better performance.  
  
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

  * Learn about [updating an instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance).
  * Learn about [managing replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas).
  * Learn about [monitoring instances](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance).
  * Learn about [promoting your Cloud SQL replica](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas#promote-replica).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
