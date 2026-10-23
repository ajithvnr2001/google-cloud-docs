---
url: https://docs.cloud.google.com/sql/docs/postgres/replication/configure-external-replica/
title: Configure external replicas \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:50.999900+00:00
---

# Configure external replicas  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/replication/configure-external-replica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Configure external replicas Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica "View this page for the SQL Server database engine")

This page describes how to configure a Cloud SQL instance that replicates to a replica external to Cloud SQL using the [ pglogical extension](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) with `logical decoding`. 

For more information about replication, see [About replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/replication).

## Set up the external replica configuration

### Before you begin

Before you start this task, you must have a Cloud SQL instance and an external PostgreSQL instance.

**Important:** Instances that use [high availability (HA)](https://docs.cloud.google.com/sql/docs/postgres/high-availability) can't be used as replication subscribers, because they don't have a consistent outgoing IP address.

### Source instance requirements

The source instance for an external read replica must be a primary or standalone instance. You can't use a Cloud SQL read replica as the source instance for an external read replica. Read replicas are sometimes recreated from the disk clone of their primary instance and their replication state to an external read replica can't be maintained by the read replica.

### Configure the primary instance

  1. Go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances) in the Google Cloud console.
  2. Enable access on the primary instance for the IP address of the external replica. 

For information about enabling IP access, see [Configuring access for IP connections](https://docs.cloud.google.com/sql/docs/postgres/configure-ip).

  3. Record the public IP address and the public outgoing IP address of the primary instance for later use. You can find these values on the instance's **Overview** page.
  4. Click the Cloud Shell icon ![](https://docs.cloud.google.com/static/sql/images/cloud-shell-icon.png) in the upper right corner.
  5. At the Cloud Shell prompt, use the built-in PostgreSQL client to connect to your primary instance: 
         
         
         gcloud sql connect PRIMARY_INSTANCE_NAME \
         --user=postgres
            
            

  6. Enter your root password. You should then see the postgres prompt.
  7. Create a PostgreSQL user with the `REPLICATION` attribute. 
         
         CREATE USER REPLICATION_USER WITH REPLICATION IN ROLE cloudsqlsuperuser LOGIN PASSWORD 'REPLICATION_USER_PASSWORD';
            

  8. Install and configure the pglogical extension: 

Edit the Cloud SQL instance to add and set the following flags:

     * `cloudsql.enable_pglogical`
     * `cloudsql.logical_decoding`
     * `max_replication_slots`
     * `max_worker_processes`
     * `max_wal_senders`

For more information about these flags, see the [PostgreSQL resources](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication#postgresql-resources) page.

Restart the database, then login, change to the replication_user, create the `pglogical` extension: 
    
    CREATE EXTENSION pglogical;
       

  9. Create a pglogical node: 

A pglogical _node_ represents a physical PostgreSQL instance, and stores connection details for that instance.
         
         SELECT pglogical.create_node(
           node_name := 'provider',
           dsn := 'host=PRIMARY_PUBLIC_IP_ADDRESS port=5432 dbname=DATABASE_NAME user=REPLICATION_USER password=REPLICATION_USER_PASSWORD'
            );
            

  10. If you are starting with a new database, create the same database and tables on both the primary and replica instances. For example: 
         
         CREATE DATABASE test;
         
         \connect test;
         
         CREATE TABLE replica_test (id SERIAL PRIMARY KEY, data text);
         INSERT INTO replica_test (data) VALUES ('apple'), ('banana'), ('cherry');
         
         CREATE EXTENSION pglogical;

  11. If you already have a database on the primary instance, you must create the same on the replica. To do this, export the database from the primary instance to a Cloud Storage bucket and import it into the replica. Learn more about [ Exporting data from Cloud SQL to a SQL dump file in Cloud Storage](https://docs.cloud.google.com/sql/docs/postgres/import-export/exporting#cloud-sql). 
  12. To support replicating different sets of data to different destinations, pglogical has the concept of a replication set. For example, to add a table to the default replication set: 
         
         SELECT pglogical.replication_set_add_table('default', 'replica_test', true);
            




### Configure the external replica

  1. Create a special user for replication and grant replication privileges: 
         
         CREATE USER REPLICATION_USER WITH REPLICATION SUPERUSER LOGIN PASSWORD 'REPLICATION_USER_PASSWORD';
            

  2. If you are starting with a new database, use the REPLICATION_USER to create the same database and tables on both the primary and replica instances. For example: 
         
         CREATE DATABASE test;
         \connect test;
         CREATE TABLE replica_test (id SERIAL PRIMARY KEY, data text);
         INSERT INTO replica_test (data) VALUES ('apple'), ('banana'), ('cherry');
           

  3. If you are seeding the external replica instance with a file you exported file from the primary instance, download the exported file from Cloud Storage. If your external replica is on a Compute Engine instance, you can download the file using the `gcloud storage` command: 
         
         gcloud storage cp gs://BUCKET_NAME/DUMP_FILE_NAME .
             

  4. Import the file into your database. 
         
         psql --user=postgres --password < DUMP_FILE_NAME.
         

  5. Install `pglogical` according to your OS. For example, on Debian systems running PostgreSQL version 13, `sudo apt-get install postgresql-13-pglogical`. 
  6. Login to the database as the replication_user and set the following parameters: 
         
         ALTER SYSTEM SET shared_preload_libraries = 'pglogical';
         ALTER SYSTEM SET max_replication_slots = #; (where # is the same as you set on the primary).
         ALTER SYSTEM SET max_worker_processes = #; (where # is the same as you set on the primary).
         # Logout of the database and restart it. For example,
         # sudo /etc/init.d/postgresql restart
         # Log back in the database as the replication_user.
         # Since the pglogical extension is created local to each database, you need to
         # execute CREATE EXTENSION pglogical in each database you create, so if you
         # haven't already done that:
         CREATE EXTENSION pglogical;
            
         
         For more information about these flags, see the [PostgreSQL resources](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication#postgresql-resources) page.
         
         
           

  7. Create a pglogical node: 
         
         SELECT pglogical.create_node(
           node_name := 'subscriber',
           dsn := 'host=REPLICA_PUBLIC_IP_ADDRESS port=5432 dbname=DATABASE_NAME user=REPLICATION_USER password=REPLICATION_USER_PASSWORD'
           );
           

  8. Create a pglogical subscription: 
         
         SELECT pglogical.create_subscription(
             subscription_name := 'SUBSCRIPTION_NAME',
             provider_dsn := 'host=PRIMARY_PUBLIC_IP_ADDRESS port=5432 dbname=DATABASE_NAME user=REPLICATION_USER password=REPLICATION_USER_PASSWORD'
         );
           

  9. Check the status of the subscription: 
         
         SELECT * FROM pglogical.show_subscription_status('SUBSCRIPTION_NAME');
            

  10. If the status appears as `replicating`, then the setup is successful. 
  11. Insert some data into the primary and check the replica to make sure the data appears there as well. 



## Troubleshoot

See [Troubleshooting pglogical](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication#troubleshooting-pglogical)

## What's next

  * Learn how to [manage replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas).
  * Learn more about [replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/replication). 
  * Learn more about [PostgreSQL replication](https://www.postgresql.org/docs/current/static/logical-replication.html).
  * Learn more about [replication configuration settings](https://www.postgresql.org/docs/current/static/runtime-config-replication.html). 
  * Learn more about [replicating from an external server](https://docs.cloud.google.com/sql/docs/postgres/replication/replication-from-external).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
