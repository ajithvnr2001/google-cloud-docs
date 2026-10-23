---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica/
title: Configure external replicas \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:41.067188+00:00
---

# Configure external replicas  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Configure external replicas Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-external-replica "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica "View this page for the SQL Server database engine")

This page describes how to configure a Cloud SQL instance that replicates to one or more replicas external to Cloud SQL, and how to demote the primary instance in an external replica configuration to reverse the configuration. 

For more information about replication, see [About replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/replication).

## Set up the external replica configuration

### Before you begin

Before you start this task, you must have a Cloud SQL instance and an external MySQL instance that meets the [requirements for external replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#external-read-replicas).

### Source instance requirements

The source instance for an external read replica must be a primary or standalone instance. You can't use a Cloud SQL read replica as the source instance for an external read replica. Read replicas are sometimes recreated from the disk clone of their primary instance and their replication state to an external read replica can't be maintained by the read replica.

### Configure the primary instance

  1. Go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances) in the Google Cloud console.
  2. Enable access on the primary instance for the IP address of the external replica. 

For information about enabling IP access, see [Configuring access for IP connections](https://docs.cloud.google.com/sql/docs/mysql/configure-ip).

  3. Record the public IP address and the public outgoing IP address of the primary instance for later use. You can find these values on the instance's **Overview** page.
  4. Click the Cloud Shell icon ![](https://docs.cloud.google.com/static/sql/images/cloud-shell-icon.png) in the upper right corner.
  5. At the Cloud Shell prompt, use the built-in MySQL client to connect to your primary instance: 
         
         
         gcloud sql connect PRIMARY_INSTANCE_NAME \
         --user=root
            
            

  6. Enter your root password. You should then see the mysql prompt.
  7. Create a special user for replication and grant replication privileges: 
         
         CREATE USER 'REPLICATION_USER'@'%' IDENTIFIED BY 'REPLICATION_USER_PASSWORD';
         GRANT REPLICATION SLAVE ON *.* TO 'REPLICATION_USER'@'%';
            

  8. If you are starting with a new database, create the same database and tables on both the primary and replica instances. For example: 
         
         CREATE DATABASE test;
         
         USE test;
         
         CREATE TABLE replica_test (id SERIAL PRIMARY KEY, data text);
         INSERT INTO replica_test (data) VALUES ('apple'), ('banana'), ('cherry');

  9. If you already have a database on the primary instance, you must create the same on the replica. To do this, export the database from the primary instance to a Cloud Storage bucket and import it into the replica. Learn more about [ Exporting data from Cloud SQL to a SQL dump file in Cloud Storage](https://docs.cloud.google.com/sql/docs/mysql/import-export/exporting#cloud-sql). 



### Configure the external replica

Warning: This procedure overwrites any data hosted in a MySQL database on the replica, including users and passwords, with the settings and data from the primary instance. 

  1. On the machine hosting the replica, seed your new external MySQL instance with the export file you created from the primary instance. 

For example, the following command loads an exported file named `mydump.sql`:
         
         mysql --user=root --password < mydump.sql
         

  2. Determine the server ID for this replica-primary pair. 

The server ID is a numeric value (for example, "3") that must be unique across the external replica configuration (each replica must have a unique server ID).

  3. Add the following options to the replica's `my.cnf` option file: 
         
         [mysqld]
             server-id=[SERVER_ID]
             gtid_mode=ON
             enforce_gtid_consistency=ON
             log_slave_updates=ON
             replicate-ignore-db=mysql
             binlog-format=ROW
             log_bin=mysql-bin
             expire_logs_days=1
             read_only=ON
           

**Note:** You must set `gtid_mode=ON` for all external replicas in a configuration that includes a Cloud SQL primary instance. Changing the default to `gtid_mode=OFF` causes replication with the external server to fail. 

For more information about MySQL replication options, see [Replication and Binary Logging Options](https://dev.mysql.com/doc/refman/8.4/en/replication-options.html).

  4. Restart the `mysqld` process to cause the configuration file to be read.
  5. In a `mysql` client on the replica, enter the following command: 
         
         CHANGE MASTER TO MASTER_HOST='MASTER_IP_ADDRESS', MASTER_USER='REPLICATION_USER',
         MASTER_PASSWORD='REPLICATION_PASSWORD', MASTER_AUTO_POSITION=1;
         

  6. Start replication on the replica: 
         
         START SLAVE;
         

  7. Confirm replication status:
         
         SHOW SLAVE STATUS\G;
         

If you see "Waiting for master to send event", replication is working.




## Demote the primary instance of an external replica

When you have a Cloud SQL instance with an external replica, you can reverse the configuration, which causes these changes to happen:

  * The external replica becomes the new primary instance.
  * The Cloud SQL instance becomes a read replica, replicating from the server that was previously the external replica (now called the source database server).



To reverse the external replica configuration:

  1. Create a [source representation instance](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#config-description).

This instance will represent the source database server to the Cloud SQL replica after the demotion operation completes.
         
         gcloud auth login
         ACCESS_TOKEN="$(gcloud auth print-access-token)"
         curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
              --header 'Content-Type: application/json' \
              --data '{
                  "name": "SOURCE_REPRESENTATION_NAME",
                  "region": "REGION",
                  "databaseVersion": "EXTERNAL_SERVER_DATABASE_VERSION",
                  "onPremisesConfiguration": {
                      "hostPort": "EXTERNAL_SERVER_IP:EXTERNAL_SERVER_PORT"
                  }
              }' \
              -X POST \
              https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances
         

Use the region where you want your Cloud SQL replica to reside.

  2. Start the demotion process. 

Because this API call requires you to provide sensitive information, you should [use a JSON file](https://docs.cloud.google.com/sql/docs/mysql/admin-api#json-file) to provide your data to cURL, rather than providing it on the command line. 

Create the data file:
         
         {
             "demoteMasterContext": {
                 "replicaConfiguration": {
                     "mysqlReplicaConfiguration": {
                         "username": "REPLICATION_USERNAME",
                         "password": "PASSWORD",
                         "caCertificate": "EXTERNAL_SERVER_CA",
                         "clientCertificate": "CLIENT_CERT",
                         "clientKey": "PRIVATE_KEY"
                     }
                 },
                 "masterInstanceName": "SOURCE_REPRESENTATION_NAME",
             },
         }
         

Then, call the API.
         
         curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
              --header 'Content-Type: application/json' \
              --data @PATH_TO_DATA_FILE \
              https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_NAME/demoteMaster
         

For more information about your options for SSL/TLS, see [SSL/TLS options](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssl-options). For more information about the properties used by the `replicaConfiguration` object, see [ Replicating from an External Server](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external#setup).

  3. Wait for the external replica to complete all pending transactions from the primary instance.

When the replica is caught up, the `SHOW SLAVE STATUS` command will show `Seconds Behind Master` as 0, and the `Executed_Gtid_Set` value will be identical between the external replica and the Cloud SQL primary.

  4. Use the `mysql` client to stop replication on the external replica: 
         
         STOP SLAVE
         RESET SLAVE ALL
         

  5. Wait for the Cloud SQL instance to start replicating from the external server, which is now the source database server. 

Running the `SHOW SLAVE STATUS` command on the Cloud SQL instance provides replication status.

  6. When the Cloud SQL instance is successfully replicating from the source database server, set the `read_only` flag on the source database server to `off` and update your applications to point to the source database server. 

**Important:** If the Cloud SQL instance being demoted has existing read replicas and `gtid_mode` is set to `OFF` in the external primary, these replicas are not supported after the demotion. You can delete such replicas before you demote your instance or change `gtid_mode` to `ON` in your external primary before you demote.

## Troubleshoot

Issue | Troubleshooting | Error message: `The slave is connecting ... master has purged binary logs containing GTIDs that the slave requires`. | The primary Cloud SQL instance has automatic backups and binary logs and point-in-time recovery is enabled, so it should have enough logs for the replica to be able to catch up. However, in this case although the binary logs exist, the replica doesn't know which row to start reading from. Create a new dump file using the correct flag settings, and configure the external replica using that file 

  1. Connect to your mysql client [through a Compute Engine instance](https://docs.cloud.google.com/sql/docs/mysql/connect-compute-engine).
  2. [Run mysqldump](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html) and use the `--master-data=1` and `--flush-privileges` flags. **Important: Do not include the`--set-gtid-purged=OFF` flag**. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/import-export/exporting#export-mysqldump).
  3. Ensure that the dump file just created contains the `SET @@GLOBAL.GTID_PURGED='...'` line.
  4. Upload the dump file to a Cloud Storage bucket and [ configure the replica using the dump file](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica#configuring_the_external_replica).

  
---|---  
  
## What's next

  * Learn how to [manage replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas).
  * Learn more about [replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/replication). 
  * Learn more about [MySQL replication](https://dev.mysql.com/doc/refman/8.4/en/replication.html).
  * Learn more about [replication options](https://dev.mysql.com/doc/refman/8.4/en/replication-options.html).
  * Learn more about [checking replication status](https://dev.mysql.com/doc/refman/8.4/en/replication-administration-status.html). 
  * Learn more about [replicating from an external server](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
