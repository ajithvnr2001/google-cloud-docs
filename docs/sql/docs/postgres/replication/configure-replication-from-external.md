---
url: https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external/
title: Configure Cloud SQL and the external server for replication \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:41.745611+00:00
---

# Configure Cloud SQL and the external server for replication  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Configure Cloud SQL and the external server for replication Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external "View this page for the MySQL database engine") | PostgreSQL | SQL Server

This page describes how to configure your external server for replication to Cloud SQL, create a source representation instance on Cloud SQL, and replicate the data to Cloud SQL. You need to go through all the steps on this page before proceeding to the replication steps.

An alternative to the steps described on this page is the [Database Migration Service](https://docs.cloud.google.com/database-migration/docs), which offers continuous replication or one-time database migration from an external server to Cloud SQL.

[Fast migration for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/faq#data-migration) is now available. This feature improves the performance of data migrations from an external source to a destination Cloud SQL instance.

## Before you begin

Before configuring replication, review the following prerequisites and terminology.

### Terminology

  * **External server.** The PostgreSQL server external to Cloud SQL that you want to replicate data from. It's also referred to as the source database or the external database server. It can be another Cloud SQL instance or any other database server, such as on-premises or Amazon Relational Database Service (RDS).

  * **Source representation instance.** A mock of a Cloud SQL instance that represents the external server to the Cloud SQL replica. It's visible in the Google Cloud console and appears like a regular Cloud SQL instance, but it doesn't contain data, require configuration or maintenance, or affect billing.

  * **Cloud SQL replica.** The Cloud SQL instance that replicates from the external server. Also known as the external primary read replica.

  * **Replication user account.** The PostgreSQL user account on the external server with sufficient permissions to allow replication between the external server and the Cloud SQL replica.

  * **Managed import.** The process of importing data directly from the external server to the Cloud SQL replica. In this situation, Cloud SQL connects to the external server using the replication user account and runs the data dump directly on the external server to import data to the Cloud SQL replica.




### Set up a Google Cloud project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  8. Make sure you have the Cloud SQL Admin, Storage Admin, and Compute Viewer roles on your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)




### Install the Google Cloud SDK

To configure replication, [install Google Cloud SDK](https://docs.cloud.google.com/sdk/install) for your external server. You might want to install the SDK on your external server unless it's already installed elsewhere.

## Set up the external server for replication

Cloud SQL supports continuous migrations from source databases to Cloud SQL destination databases.

Supported source databases for PostgreSQL include:

  * Self-managed PostgreSQL (on premises or on any cloud VM that you fully control) 9.4, 9.5, 9.6, 10, 11, 12, 13, 14, 15, 16, 17, and 18
  * Amazon RDS 9.6.10+, 10.5+, 11.1+, 12, 13, 14, 15, 16, 17, and 18.
  * Amazon Aurora 10.11+, 11.6+, 12.4+, 13.3+, 14.6+, 15.2+, 16, and 17.
  * Microsoft Azure Database for PostgreSQL Flexible Server 11 and later
  * Cloud SQL 9.6, 10, 11, 12, 13, 14, 15, 16, 17, and 18



Configuring your source requires configuring both the source instance and underlying source databases.

### External server checklist

If the Cloud SQL replica is enabled with a private IP address because the outgoing private IP address isn't static, configure the external server's firewall to allow the internal IP range allocated for the [private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) of the VPC network that the Cloud SQL replica uses as its private network.

The source database server's firewall must be configured to allow the entire **internal IP range** allocated for the **private service connection** of the VPC network that the Cloud SQL destination instance uses as the **privateNetwork** field of its [**ipConfiguration** settings](https://docs.cloud.google.com/sql/docs/postgres/replication/replication-from-external#setup-replica-instance).

To find the **internal IP range** :

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)

  2. Select the VPC network that you want to use.

  3. Click the **Private service connection** tab.




## Configure your source instance

To configure your source instance, follow these steps:

  1. If your source instance does not include the `postgres` database, create it.
  2. [Install the pglogical package](https://github.com/2ndQuadrant/pglogical) on the source instance.
  3. Set the following parameters, as needed.

     1. If the source PostgreSQL instance is Amazon RDS, then include these parameters in [ a new parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.Creating) and attach the parameter group to the instance.

        * If the source is Cloud SQL, set the `cloudsql.logical_decoding` and `cloudsql.enable_pglogical` flags to `on`. 

To enable flags in Cloud SQL, see [Configuring database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

**Note:** The `pglogical` extension can log credentials in plain text on the source instance. This behavior is caused by the extension, and is unrelated to Cloud SQL.
        * Set `shared_preload_libraries` to include `pglogical` by using the following command:
              
              ALTER SYSTEM SET shared_preload_libraries = 'pglogical';
                    

**Note:** To view a list of the existing libraries for your instance, run the `show shared_preload_libraries` command.
        * Set `wal_level` to `logical` by using the following command:
              
              ALTER SYSTEM SET wal_level = 'logical';
                  

If the source PostgreSQL instance is Amazon RDS, to enable WAL logs at the `logical` level, set the `rds.logical_replication` parameter to `1`.

        * Set `wal_sender_timeout` to `0` by using the following command:
              
              ALTER SYSTEM SET wal_sender_timeout = 0;

The value `0` disables the timeout mechanism that's used to terminate inactive replication connections. 

        * Set [max_replication_slots](https://www.postgresql.org/docs/current/static/runtime-config-replication.html) to the maximum number of replication slots that the source instance can support. Use the following command, after replacing MAX_REPLICATION_SLOTS with the number:
              
              ALTER SYSTEM SET max_replication_slots = MAX_REPLICATION_SLOTS;

Cloud SQL requires one slot for each database that's migrated. Specify at least the number of subscriptions expected to connect, with some reserves for table synchronization.

For example, if the source instance has 5 databases and 2 migration jobs are created for the source, then the number of replication slots must be at least 5 * 2 = 10, in addition to the number of replication slots that you already use. 

        * Set [max_wal_senders](https://www.postgresql.org/docs/current/static/runtime-config-replication.html) to at least the same as `max_replication_slots`, in addition to the number of senders already used on your instance. Use the following command, replacing MAX_WAL_SENDERS with the total number of WAL sender processes running simultaneously:
              
              ALTER SYSTEM SET max_wal_senders = MAX_WAL_SENDERS;

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12.

        * Set [max_worker_processes](https://www.postgresql.org/docs/current/static/runtime-config-resource.html) to at least the number of databases in the source instance, in addition to the number of worker processes already used on your instance. Use the following command, after replacing MAX_WORKER_PROCESSES with the total number:
              
              ALTER SYSTEM SET max_worker_processes = MAX_WORKER_PROCESSES;

     2. If the source PostgreSQL instance is Microsoft Azure Database for PostgreSQL Flexible Server, then perform the following actions to support migrating data from an external server to a Cloud SQL instance: 
        * Set `shared_preload_libraries` to include `pglogical` by using the following command:
              
              ALTER SYSTEM SET shared_preload_libraries = 'pglogical';
                    

**Note:** To view a list of the existing libraries for your instance, run the `show shared_preload_libraries` command.
        * Set `wal_level` to `logical`. For more information, see [Logical replication and logical decoding in Azure Database for PostgreSQL - Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-logical).
        * Set [max_replication_slots](https://www.postgresql.org/docs/current/static/runtime-config-replication.html) to the maximum number of replication slots that the source instance can support. Use the following command, after replacing MAX_REPLICATION_SLOTS with the number:
              
              ALTER SYSTEM SET max_replication_slots = MAX_REPLICATION_SLOTS;

Cloud SQL requires one slot for each database that's migrated. Specify at least the number of subscriptions expected to connect, with some reserves for table synchronization.

For example, if the source instance has 5 databases and 2 migration jobs are created for the source, then the number of replication slots must be at least 5 * 2 = 10, in addition to the number of replication slots that you already use. 

        * Set [max_wal_senders](https://www.postgresql.org/docs/current/static/runtime-config-replication.html) to at least the same as `max_replication_slots`, in addition to the number of senders already used on your instance. Use the following command, replacing MAX_WAL_SENDERS with the total number of WAL sender processes running simultaneously:
              
              ALTER SYSTEM SET max_wal_senders = MAX_WAL_SENDERS;

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12.

        * Set [max_worker_processes](https://www.postgresql.org/docs/current/static/runtime-config-resource.html) to at least the number of databases in the source instance, in addition to the number of worker processes already used on your instance. Use the following command, after replacing MAX_WORKER_PROCESSES with the total number:
              
              ALTER SYSTEM SET max_worker_processes = MAX_WORKER_PROCESSES;

        * Set [azure.extensions](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external/) to include `pglogical`. For more information, see [Server parameters in Azure Database for PostgreSQL - Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-server-parameters). 

**Note:** By default, Microsoft Azure has the `require_secure_transport` parameter set to `on`. In this case, when you use [Database Migration Service](https://docs.cloud.google.com/database-migration/docs) to create your source connection profile for Microsoft Azure, specify either **Server-only authentication** or **Server-client authentication** for the SSL/TLS configuration. If a connection is made over a public network (by using IP allowlists), then SSL/TLS encryption can be used to connect between Microsoft Azure and Cloud SQL securely.

If the `require_secure_transport` parameter is set to `off`, then specify **None** for the SSL/TLS configuration. The Cloud SQL destination instance connects to the source Microsoft Azure database without encryption.

The parameters that you're setting in this step apply to a PostgreSQL database server that's running. You can also make these changes persistent by including them in the `postgresql.conf` file. 

  4. If the Cloud SQL replica will use a private IP, configure the external server's firewall to allow the internal IP range allocated for the [private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) of the VPC network of the replica.
  5. To apply the configuration changes, restart the source instance.



### Enable replication delay monitoring for PostgreSQL versions preceding 9.6

If you're migrating from a PostgreSQL version lower than 9.6, then the replication delay metric isn't available by default. You can use one of three alternatives to track this metric and ensure minimal downtime when you promote the database:

  * **Option 1** : Enable the Cloud SQL external server to track the replication delay by granting access to a specific query. Using a user with the `SUPERUSER` privilege, perform the following:

    1. Define the following function to allow the external server to query for the replication delay.
           
           CREATE OR REPLACE FUNCTION pg_stat_replication_user()
           RETURNS TABLE (
           pid               integer                  ,
           usesysid          oid                      ,
           username          name                     ,
           application_name  text                     ,
           client_addr       inet                     ,
           client_hostname   text                     ,
           client_port       integer                  ,
           backend_start     timestamp with time zone ,
           backend_xmin      xid                      ,
           state             text                     ,
           sent_location     pg_lsn                   ,
           write_location    pg_lsn                   ,
           flush_location    pg_lsn                   ,
           replay_location   pg_lsn                   ,
           sync_priority     integer                  ,
           sync_state        text
           )
           LANGUAGE SQL
           SECURITY DEFINER
           AS $$
            SELECT *
            FROM pg_catalog.pg_stat_replication;
           $$;
           

    2. Grant the `EXECUTE` permission to the user by running the following commands:

       1. `REVOKE EXECUTE ON FUNCTION pg_stat_replication_user() FROM public;`
       2. `GRANT EXECUTE ON FUNCTION pg_stat_replication_user() to {replication_user};`
  * **Option 2** : Grant the `SUPERUSER` privilege directly to the user used to connect to the source instance. This allows the external server to read the replication delay directly.

  * **Option 3** : Track the replication delay independently by using the following query:

**Note:** For PostgreSQL versions earlier than 10, run this command as a `superuser`.
        
        SELECT current_timestamp, application_name,
            pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.sent_location) AS sent_location_lag,
            pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.write_location) AS write_location_lag,
            pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.flush_location) AS flush_location_lag,
            pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.replay_location) AS replay_location_lag
            FROM pg_stat_replication
            WHERE application_name like 'cloudsql%';
          

In this option, Cloud SQL doesn't reflect the replication delay metric in the graphs or API responses.




## Configure your source databases

The Cloud SQL external server migrates all databases under your source instance other than the following:

  * For on-premise sources: template databases `template0` and `template1`
  * For Amazon RDS sources: `template0`, `template1`, and `rdsadmin`
  * For Cloud SQL sources: template databases `template0` and `template1`



Do the following on each database in your source instance that isn't included in the preceding list:

  1. To install the `pglogical` extension, run the following command on every database on your source instance:
         
         CREATE EXTENSION IF NOT EXISTS pglogical

For tables that don't have primary keys, Cloud SQL supports the migration of the initial snapshot and `INSERT` statements during the change data capture (CDC) phase. Migrate `UPDATE` and `DELETE` statements manually.

**Note:** See [Debugging and other tools](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools) to learn how to generate a query to list tables in a PostgreSQL database without primary keys. You must [ alter these tables](https://www.postgresql.org/docs/current/static/sql-altertable.html) so that they have a primary key each. For tables that don't have primary keys, only the initial snapshot and `INSERT` statements are migrated.

**Note:** For PostgreSQL 9.4, install the `pglogical_origin` extension on every database by running the following commands:
         
         CREATE EXTENSION IF NOT EXISTS pglogical_origin;
         CREATE EXTENSION IF NOT EXISTS pglogical;

  2. Connect to the instance and run the following commands to set privileges for the user on each of the migrated databases, as well as the default `postgres` database.

The user that you use to connect to the source instance is configured as the user in the [Connection Profiles](https://console.cloud.google.com/dbmigration/connection-profiles) page. You can create a new user or reuse an existing one.

     * On all schemas on each database to migrate, except for the information schema and schemas starting with `pg_`, run the following command:
           
           GRANT USAGE on SCHEMA schema to username;
           GRANT SELECT on ALL SEQUENCES in SCHEMA schema to username;
           GRANT SELECT on ALL TABLES in SCHEMA schema to username;

     * On each database to migrate, run the following command:
           
           GRANT USAGE on SCHEMA pglogical to PUBLIC;

     * To get replication information from source databases, run the following command on all databases:
           
           GRANT SELECT on ALL TABLES in SCHEMA pglogical to username;

**Note:** If the following error message appears, then you can ignore it.

` postgres=> GRANT SELECT on ALL TABLES in SCHEMA pglogical to demo;  
ERROR: permission denied for table node_interface `
     * If your source is Amazon RDS, then run the following command:
           
           GRANT rds_replication to username;

If your source is Microsoft Azure Database for PostgreSQL version earlier than 14, then run the following command:
           
           GRANT SELECT on ALL TABLES in SCHEMA pglogical to username;

You can ignore an error that appears on the `pglogical.node` interface.

If your source is Microsoft Azure Database for PostgreSQL version 14 and later, then run the following command:
           
           GRANT pg_read_all_data to username;

Otherwise, run the following command:
           
           ALTER USER username with REPLICATION;




## Set up a source representation instance

The source representation instance references the external server. It contains only the request data from the external server. Create the request data and use it in a `curl` command that creates the source representation instance in Cloud SQL.

### Create the request data

The request data contains basic information about your external server in JSON format. The request data can be configured for a Cloud SQL replica on a public or private network and should contain this information.

If you want to migrate a subset of databases from the source representation instance to the destination Cloud SQL instance, then use the `selectedObjects` parameter to specify the database names. If you don't use this parameter or provide an empty list as the value for the parameter, then all databases are migrated from the source to the destination.

###  source.json 
    
    
        {
          "name": "SOURCE_NAME",
          "region": "REGION",
          "databaseVersion": "DATABASE_VERSION",
          "onPremisesConfiguration": {
            "selectedObjects": "SELECTED_OBJECTS",
            "hostPort": "SOURCE_HOST",
            "username": "USERNAME",
            "password": "PASSWORD",
            "caCertificate": "SOURCE_CERT",
            "clientCertificate": "CLIENT_CERT",
            "clientKey": "CLIENT_KEY"
          }
        }

###  managed import example 
    
    
    // example of source.json for external server that
    // - initiates replication from a Cloud SQL managed import
    // - doesn't use SSL/TLS
    
    {
      "name": "cloudsql-source-instance",
      "region": "us-central1",
      "databaseVersion": "POSTGRES_9_6",
      "onPremisesConfiguration": {
        "selectedObjects":[{"database":"db1"}, {"database":"db2"}],
        "hostPort": "192.0.2.0:5423",
        "username": "replicationUser",
        "password": "486#@%*@"
      }
    }
    

Property | Description  
---|---  
SOURCE_NAME | The name of the source representation instance to create.  
REGION | The [region](https://docs.cloud.google.com/sql/docs/postgres/locations) where you want the source representation instance to reside.  
DATABASE_VERSION | The database version running on your external server. The options are `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `POSTGRES_13`, `POSTGRES_14`, `POSTGRES_15`, `POSTGRES_16`, or `POSTGRES_17`.  
SELECTED_OBJECTS | A comma-separated list of objects, containing the databases that you're migrating from the source representation instance to the destination Cloud SQL instance.  
SOURCE HOST | The IPv4 address and port for the external server, or the DNS address for the external server. If the external server is hosted on Cloud SQL, then the port is `5432`.  
USERNAME | The replication user account on the external server.  
PASSWORD | The password for the replication user account.  
BUCKET | The name of the bucket that contains the dump file. Include only if you're setting up replication with a dump file that exists in a Cloud Storage bucket.  
DUMP_FILE | A file in the bucket that contains the data from the external server.  
CLIENT_CA_CERT | The CA certificate on the external server. Include only if SSL/TLS is used on the external server.  
CLIENT_CERT | The client certificate on the external server. Required only for [server-client authentication](https://docs.cloud.google.com/sql/docs/postgres/replication/external-server#ssltls_configuration). Include only if SSL/TLS is used on the external server.  
CLIENT_KEY | The private key file for the client certificate on the external server. Required only for [server-client authentication](https://docs.cloud.google.com/sql/docs/postgres/replication/external-server#ssltls_configuration). Include only if SSL/TLS is used on the external server.  
SSL_OPTION | Whether SSL/TLS encryption is used to establish a connection between the source Microsoft Azure database and the destination Cloud SQL database. You can specify the following values for this parameter:

  * `SSL_OPTION_UNSPECIFIED:` the destination database connects to the source database without encryption.
  * `DISABLED:` SSL is deactivated when the replica connects to the source database.
  * `REQUIRE:` SSL is required for the replica to connect to the source database.
  * `VERIFY_CA:` use this parameter to specify whether server-only authentication or server-client authentication is used as part of the SSL/TLS encryption to connect between the source and destination databases. To use server-only authentication, for the `SOURCE_CERT` variable, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed the external server's certificate. To use server-client authentication, make the following replacements:
    * `SOURCE_CERT:` provide the certificate of the CA that signed the source database server's certificate 
    * `CLIENT_CERT:` provide the certificate that the destination database uses to authenticate against the source database server
    * `CLIENT_KEY:` provide the private key associated with the client certificate

**Note:** For more information about server-only authentication and server-client authentication, see [Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-source-connection-profile).The default value for this parameter is `SSL_OPTION_UNSPECIFIED`.  
  
### Create a source representation instance

Before you start this step, create a JSON file that contains your source request data.

Then, to create the source representation instance in Cloud SQL, open a terminal and run the following commands:

###  curl 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @JSON_PATH \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances

###  example 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @./source.json \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances

Property | Description  
---|---  
PROJECT_ID | The ID for your project in Google Cloud.  
JSON_PATH | The path to the `JSON` file that contains the request data for the external server.  
  
## Update a source representation instance

If you update the [request data](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#create-source-request) from the external server, you can update the existing source representation instance to use the modified values.

### Modify the request data

Update the request data to include any fields that have changed. This includes the `hostPort`, `username`, `password`, `caCertificate`, `clientCertificate`, and `clientKey` fields. After updating the request data, use it in a `curl` command to update the instance in Cloud SQL.

To update the databases that you want to migrate from the source representation instance, update the list of database names that are associated with the `selectedObjects` parameter. If you don't use this parameter or provide an empty list as the value for the parameter, then all databases are migrated from the source to the destination.

The following example shows updating the `username` and `password` fields with a different username and password:

###  source.json 
    
    
        {
          "name": "SOURCE_NAME",
          "region": "REGION",
          "databaseVersion": "DATABASE_VERSION",
          "onPremisesConfiguration": {
            "selectedObjects": "SELECTED_OBJECTS",
            "username": "NEW_USERNAME",
            "password": "NEW_PASSWORD"
          }
        }

###  managed import example 
    
    
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
REGION | The [region](https://docs.cloud.google.com/sql/docs/postgres/locations) where the source representation instance resides.  
DATABASE_VERSION | The database version running on your external server. The options are `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `POSTGRES_13`, `POSTGRES_14`, `POSTGRES_15`, `POSTGRES_16`, or `POSTGRES_17`.  
SELECTED_OBJECTS | An updated comma-separated list of objects, containing databases that you're migrating from the source representation instance instance to the destination Cloud SQL instance.  
NEW_USERNAME | The new replication user account on the external server.  
NEW_PASSWORD | The password for the new account.  
  
### Modify a source representation instance

Before you start this step, create a JSON file that contains your modified request data.

Then, to modify the source representation instance in Cloud SQL, open a terminal and run the following commands:

###  curl 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @JSON_PATH \
             -X PATCH \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/SOURCE_NAME

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
PROJECT_ID | The ID for your project in Google Cloud.  
JSON_PATH | The path to the `JSON` file that contains the request data for the external server.  
SOURCE_NAME | The name of the source representation instance.  
  
## Set up a Cloud SQL replica

The Cloud SQL replica eventually contains the data from the external server. In this step, you create the request data and use it in a `curl` command that creates the Cloud SQL replica in Cloud SQL.

### Create the request data

The request data contains basic information about your external server and Cloud SQL replica in JSON format. The request data can be configured for a Cloud SQL replica on a public or private network and should contain this information:

###  replica.json 
    
    
        {
            "settings": {
                "tier": "TIER",
                "dataDiskSizeGb": "DISK_SIZE",
                "ipConfiguration": {
                    "ipv4Enabled": "PUBLIC_IP_STATUS",
                    "privateNetwork": "projects/PROJECT_ID/global/networks/NETWORK_NAME"
                 },
                 "availabilityType": "AVAILABILITY_TYPE"
            },
            "masterInstanceName": "SOURCE_REPRESENTATION_INSTANCE_NAME",
            "region": "SOURCE_REGION",
            "databaseVersion": "DATABASE_VERSION",
            "name": "REPLICA_NAME"
        }

###  example 
    
    
        {
            "settings": {
                "tier": "db-custom-4-15360",
                "dataDiskSizeGb": "100"
            },
            "masterInstanceName": "source-instance",
            "region": "us-central1",
            "databaseVersion": "POSTGRES_16",
            "name": "replica-instance"
        }

Property | Description  
---|---  
TIER | The [type of machine](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#settings-2ndgen) to host your replica instance. If you don't know which machine type to use, start with `db-custom-2-7680`. You can [change its size and other supported values](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#settings-2ndgen) later if needed.  
DISK_SIZE | The storage size for the Cloud SQL replica, in GB.  
PUBLIC_IP_STATUS | Determines whether the instance is assigned a public IP address. By default, the value of this property is `true`. To turn off the assignment of a public IP address for the replica, set the value to `false`. If your project has the [`constraints/sql.restrictPublicIp` organization policy](https://docs.cloud.google.com/sql/docs/postgres/org-policy/org-policy) enabled, then to create the Cloud SQL replica, you must set the value of the `ipv4Enabled` property to `false`. For more information about turning off public IP address assignment, see [Disable public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip#disable-public).  
PROJECT_ID | If the Cloud SQL replica is on a private network, then include the `privateNetwork` property in the `replica.json` file. For PROJECT_ID, specify the ID of your project in Google Cloud.  
NETWORK_NAME | The name of the private network to use with the Cloud SQL replica.  
AVAILABILITY_TYPE | The availability type of the Cloud SQL replica. By default, the value is `ZONAL`. To make the replica HA, set the value to `REGIONAL`. To learn about the allowed values, see [SqlAvailabilityType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances#sqlavailabilitytype).   
After you create an external server HA replica, you cannot change it to a non-HA replica. This is true conversely as well. You cannot change an external server non-HA replica to an HA replica.   
Manual failover might lead to unrecoverable migration if attempted when the instance is still loading the initial data, or to temporary downtime if the instance is already replicating from the source. Check the [replication status](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas#replication-status).  
SOURCE_REPRESENTATION_INSTANCE_NAME | The name of the source representation instance.  
SOURCE_REGION | The region assigned to the source representation instance.  
DATABASE_VERSION | The database version to use with the Cloud SQL replica. The options for this version are `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `POSTGRES_13`, `POSTGRES_14`, `POSTGRES_15`, `POSTGRES_16`, or `POSTGRES_17`. Match the database version running on your external server, or set the value to no more than one version later.  
REPLICA_NAME | The name of the Cloud SQL replica to create.  
  
### Create the Cloud SQL replica

Before you start this step, create a JSON file that contains your replica request data. Then, to create a Cloud SQL replica, open a Cloud Shell terminal and run these commands:

###  curl 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @JSON_PATH \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances

###  example 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @./replica.json \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances

Property | Description  
---|---  
PROJECT_ID | The ID of your project in Google Cloud, which must be the same as that of the source instance.  
JSON_PATH | The path to the `JSON` file that contains the request data for the Cloud SQL replica.  
  
### Verify your setup

To ensure your instances were set up correctly, go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances).

You should see your source representation instance and the Cloud SQL replica, in a listing similar to the following:

Instance ID | Type | Public IP  
---|---|---  
(-) source-representation-instance | Database external primary | 10.68.48.3:5432  
replica-instance | Database read replica | 34.66.48.59  
  
Also make sure that you have the `cloudsql.instances.migrate` permission on the Cloud SQL replica. This permission is included in the `cloudsql.admin` or `cloudsql.editor` [IAM roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles).

### Set the default user password and add other user accounts to the Cloud SQL replica

After you create the Cloud SQL replica, set the password for the default user. You can also add other user accounts to the replica, if required. You can't import database user accounts from the external server, but you can recreate the user accounts on the Cloud SQL replica. Do these activities before you replicate from the external server.

To set the password for the default user, use the [ `gcloud sql users set-password`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/set-password) command as follows.
    
    
    gcloud sql users set-password postgres \
    --instance=INSTANCE_NAME \
    --password=PASSWORD

Replace INSTANCE_NAME with the name of the instance and PASSWORD with your selected password before running the command.

To create user accounts on the replica, see [Create and manage users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users). 

### Get the Cloud SQL replica's outgoing IP address

You can use the outgoing IP address of the Cloud SQL replica to create a secure connection between the external server and the Cloud SQL replica. You won't be charged for this IP address.

###  Console 

To get the outgoing IP address for the replica, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Next to the Cloud SQL replica's public IP address, hold the pointer over the **More info** tooltip and retrieve the outgoing IP address.

Note that the outgoing IP address is not the IP address displayed in the main listing for the replica in the Google Cloud console.




###  gcloud 

To get the outgoing IP address for the replica, run the following command:
    
    
    gcloud sql instances describe REPLICA_NAME --format="default(ipAddresses)"
    

Property | Description  
---|---  
REPLICA_NAME | The name of the Cloud SQL replica whose outgoing public IP address you want to retrieve.  
  
### Allow incoming connections on the external server

The Cloud SQL replica needs to connect to the external server for replication to succeed. You must configure the network firewall for your external server to accept connections from the Cloud SQL replica's outgoing IP address if the following conditions apply:

  * The external server is behind a firewall or some other network restriction.
  * Your Cloud SQL replica is using a public IP.



To connect to the Cloud SQL replica, you use the replica's primary IP address. This IP address is displayed in the Google Cloud console.

### Update the source representation instance to allow replication to the Cloud SQL replica

After you set up the source representation instance for the Cloud SQL replica, you might need to [update the source representation instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance). For example, these scenarios require an update to your configurations:

  * The host, port, or IP of the external server changes.
  * You want to use a different PostgreSQL replication user.
  * The password of the PostgreSQL replication user changes.
  * The SSL certificates used to securely connect to the external server change.



## Seed the Cloud SQL replica

For the initial loading of data from the external server into the Cloud SQL replica, use a managed import. It uses a service that extracts data from the external server and imports it into the Cloud SQL instance directly. For more information, see [Using a managed import to set up replication from external databases](https://docs.cloud.google.com/sql/docs/postgres/replication/managed-import-replication-from-external).

## Monitor replication

When the Cloud SQL replica finishes the initial data load, it connects to the external server and applies all updates that were made after the export operation. [Confirm your replication status](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas#check_replication_status).

It's important to check the replication status before promoting the replica to a standalone instance. If the replication process isn't successfully completed, a promoted replica doesn't have all the changes from your external server.

If replication delay is not trending toward 0, [take steps to address it](https://docs.cloud.google.com/sql/docs/postgres/troubleshooting#highlag). You might want to check these metrics: `/postgresql/external_sync/initial_sync_complete`, `postgresql/external_sync/max_replica_byte_lag`, and `database/replication/state`. View the list of [Cloud SQL metrics](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics). 

If you want to migrate a subset of databases from the source representation instance to the destination Cloud SQL instance, then check the following per-database metrics:

Metric | Description  
---|---  
`per_database/postgresql/external_sync/initial_sync_complete` | Understand the migration phase of a database. If the value for this metric is `0`, then the database is still part of the initial data dump. If the value is `1`, then the database has completed the initial data dump and is in the change data capture (CDC) phase.  
`per_database/postgresql/external_sync/replication_byte_lag` | Know the replication lag for a database (in bytes).  
  
After the Cloud SQL replica has caught up with the external server and there's no replication delay on the Cloud SQL replica, connect to your database. Run the appropriate database commands to make sure that the contents are as expected when compared with the external server. Retain your external server until the necessary validations are done.

## Set up a cascading replica

After migration, you can create cascading read replicas under your Cloud SQL replica before promoting the Cloud SQL replica.

To create a cascading replica, run the following commands:

### Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the **Replicas** tab for the replica that will act as a parent for the replica that you want to create.
  3. Click **Create replica**.
  4. On the **Create read replica** page, update the instance ID, and any other configuration options, including the name, region, and zone.
  5. Click **Create**. 

Cloud SQL creates a replica. You're returned to the instance page for the parent replica.

  6. Follow steps 4-6 for each new cascading replica that you want to create.



### gcloud

  1. Create the new replica by specifying your Cloud SQL replica as the primary instance using the [`--master-instance-name`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) flag: 
         
         gcloud sql instances create REPLICA_NAME \
               --master-instance-name=PARENT_REPLICA_NAME \

Replace the following:  

     * REPLICA_NAME: the unique ID for the replica that you are creating
     * PARENT_REPLICA_NAME: the name of the Cloud SQL replica
  2. After the replica is created, you can see that the changes made to the primary instance are replicated through all the replicas in the cascading replicas chain.




### curl

  1. To create a replica under the parent replica, edit the following JSON code sample and save it to a file called `request.json`: 
         
         {
           "masterInstanceName": "EXTERNAL_SERVER_REPLICA_NAME",
           "project": "PROJECT_ID",
           "name": "REPLICA_NAME",
           "region": "REPLICA_REGION",
           "settings":
             {
               "tier": "MACHINE_TYPE",
             }
         }

  2. Run the following command: 
         
         curl -X POST
         -H "Authorization: Bearer "$(gcloud auth print-access-token)
         -H "Content-Type: application/json; charset=utf-8"
         -d @request.json
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"




## Promote the replica

Promote your replica by following these steps:

  1. [Promote the replica to a primary instance](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas#promote-replica). 
  2. [Add read replicas to your instance](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica#create-2nd-gen).
  3. Optional: [Configure your instance for high availability (HA)](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#ha-existing). To prevent additional downtime, you can enable HA while [setting up a replica](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setup-replica-instance) by setting `AVAILABILITY_TYPE` to `REGIONAL`.



## Limitations

  * If you install extensions on your external databases that Cloud SQL doesn't support, then when you migrate the databases to a destination instance, Cloud SQL won't migrate these extensions. To ensure a smooth migration, verify that no objects or applications reference the extensions. Before proceeding with the migration, we recommend removing the extensions along with any references to the extensions from the selected databases on the source instance.

For more information about the extensions that Cloud SQL supports, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

  * If you install the [`pg_cron`](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_cron) extension on your external source databases, then when you migrate the databases to a destination instance, Cloud SQL doesn't migrate the extension or any `cron` settings associated with the extension. After you migrate the databases and promote the replica, Google recommends that you re-enable the `pg_cron` extension on each migrated database.

  * You can't migrate data from version 11 of a source Microsoft Azure server to version 11 of a destination Cloud SQL for PostgreSQL instance. To resolve this, migrate the data to a Cloud SQL instance that has a version of 12 or later.

  * You can't directly promote a cascading read replica under an external server replica. First, promote the external server replica to a primary instance, and then promote the cascading read replica.




## What's next

  * Learn how to use a [managed import to set up replication from external databases](https://docs.cloud.google.com/sql/docs/postgres/replication/managed-import-replication-from-external).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
