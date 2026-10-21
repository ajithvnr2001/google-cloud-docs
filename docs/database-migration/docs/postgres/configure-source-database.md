---
url: https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database/
title: Configure your source \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:39.316384+00:00
---

# Configure your source  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest)



Send feedback 

#  Configure your source Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database "View this page for the MySQL version of Database Migration Service.") | PostgreSQL | [PostgreSQL to AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database "View this page for the PostgreSQL to AlloyDB version of Database Migration Service.")

  


## Overview

Database Migration Service supports continuous migrations from source databases to Cloud SQL destination databases.

Supported source databases for PostgreSQL include: 

  * Amazon RDS 9.6.10+, 10.5+, 11.1+, 12, 13, 14, 15, 16, 17, 18.
  * Amazon Aurora 10.11+, 11.6+, 12.4+, 13.3+, 14.6+, 15.2+, 16, 17, 18.
  * Self-managed PostgreSQL (on premises or on any cloud VM that you fully control) 9.4, 9.5, 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18.
  * Cloud SQL for PostgreSQL 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18.
  * Microsoft Azure Database for PostgreSQL Flexible Server: 11+



Configuring your source requires configuring both the source instance and underlying source databases.

## Configure your source instance

To configure your source instance, follow these steps:

  1. **For Cloud SQL sources:** If you are migrating from a Cloud SQL instance that uses a Private IP connection to a Cloud SQL instance that uses a [non-RFC 1918 address](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) IP range, add the non-RFC 1918 range to the network configuration of your source Cloud SQL instance. See [Configure authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) in Cloud SQL documentation.
  2. Your source instance must include the `postgres` database. If you don't have this database, then create it.
  3. Install the `pglogical` package on the source instance and make sure that it's included in the [ `shared_preload_libraries`](https://www.postgresql.org/docs/current/runtime-config-client.html) variable. See Install the `pglogical` package on the source instance for your environment.

  4. Verify the extensions in your source instance. Database Migration Service doesn't migrate [extensions that are unsupported by Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extensions). The presence of these extensions doesn't block the migration but to ensure a smooth migration process, please verify that your objects or applications don't reference any unsupported extensions. We recommend removing these extensions and references from your source database before you proceed.

  5. **For sources that use the`pg_cron` extension**: The [`pg_cron`](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_cron) extension (or any `cron` settings associated with the extension) isn't migrated by Database Migration Service, but it is supported in Cloud SQL for PostgreSQL destinations. If you use the `pg_cron` extension in your source databases, you can re-install it on your destination instance after the migration is complete.




## Configure your source databases

Database Migration Service migrates **all** databases under your source instance other than the following databases:

  * For on-premise PostgreSQL sources: template databases `template0` and `template1`
  * For Amazon RDS sources: `template0`, `template1`, and `rdsadmin`
  * For Cloud SQL sources: template databases `template0` and `template1`
  * For Microsoft Azure sources: `azure_maintenance`, `azure_sys`, `template0`, `template1`



Do the following on **each database** in your source instance that isn't mentioned above:

  1. **For PostgreSQL version 9.4 sources only** , install the following `pglogical` extensions on each database in your source instance: 

     * `CREATE EXTENSION IF NOT EXISTS pglogical;`
     * `CREATE EXTENSION IF NOT EXISTS pglogical_origin;`
  2. **For all other versions** , install only the `pglogical` extension on each database in your source instance: `CREATE EXTENSION IF NOT EXISTS pglogical`.

  3. For tables that don't have primary keys, Database Migration Service supports migration of the **initial snapshot and`INSERT` statements during the CDC phase**. You should migrate `UPDATE` and `DELETE` statements manually.

See [Debugging and other tools](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools) to learn how to generate a query to list tables in a PostgreSQL database without primary keys. For each database table that you find that doesn't have a primary key and the table isn't part of the databases that aren't migrated, you should [ alter the table so that it has a primary key](https://www.postgresql.org/docs/current/sql-altertable.html) or [follow this process](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools#find_tables_without_primary_keys_pks). For tables that don't have primary keys, only the initial snapshot and `INSERT` statements are migrated.

  4. The USER you're using to connect to the source instance (which will be configured as the user in the [Connection Profiles](https://console.cloud.google.com/dbmigration/connection-profiles) page) must have certain privileges on each of the migrated databases, as well as the default `postgres` database. You can create a new user or reuse an existing one. To set these privileges, connect to the instance and run the following commands:

     1. `GRANT USAGE on SCHEMA SCHEMA to USER` on all schemas (aside from the information schema and schemas starting with "pg_") on each database to migrate.
     2. `GRANT USAGE on SCHEMA pglogical to PUBLIC;` on each database to migrate.
     3. `GRANT SELECT on ALL TABLES in SCHEMA pglogical to USER` on all databases to get replication information from source databases.
     4. `GRANT SELECT on ALL TABLES in SCHEMA SCHEMA to USER` on all schemas (aside from the information schema and schemas starting with "pg_") on each database to migrate.
     5. `GRANT SELECT on ALL SEQUENCES in SCHEMA SCHEMA to USER` on all schemas (aside from the information schema and schemas starting with "pg_") on each database to migrate.
     6. If your source is **Amazon RDS** , then run the following command: 
        1. `GRANT rds_replication to USER`
     7. If your source isn't **Amazon RDS** , then run the following command: 
        1. `ALTER USER USER with REPLICATION` role



## Install the `pglogical` package on the source instance

This section describes how to configure the `pglogical` package and the applicable parameters, depending on your source instance.

**Note:** You can get the correct values for these parameters by [ running a migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job. During this test, Database Migration Service can verify your settings and suggest the correct values.

### On-premise or self-managed PostgreSQL

  1. [Install](https://github.com/2ndQuadrant/pglogical) the pglogical package on the server.
  2. Connect to the instance and set the following parameters, as needed: 
     * `shared_preload_libraries` must include `pglogical`.

To set this parameter, run the `ALTER SYSTEM SET shared_preload_libraries = 'pglogical,[any other libraries in your instance]';` command.

To obtain the existing libraries for your instance, run the `show shared_preload_libraries` command.

     * Set `wal_level` to `logical`.

To set this parameter, run the `ALTER SYSTEM SET wal_level = 'logical';` command.

     * Set `wal_sender_timeout` to `0`.

To set this parameter, run the `ALTER SYSTEM SET wal_sender_timeout = 0;` command, where `0` disables the timeout mechanism that's used to terminate inactive replication connections.

     * [max_replication_slots](https://www.postgresql.org/docs/current/runtime-config-replication.html) defines the maximum number of replication slots the source instance can support. It must be set to at least the number of subscriptions expected to connect, plus some reserves for table synchronization.

Database Migration Service requires one slot for each database that's migrated (which is all of the databases under the source instance).

For example, if there are 5 databases on the source instance and if there are 2 migration jobs created for the source, then the number of replication slots must be at least 5 * 2 = 10, plus the number of replication slots already used by you. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of replication slots and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job. 

To set this parameter, run the `ALTER SYSTEM SET max_replication_slots = #;` command, where # represents the maximum number of replication slots. 

     * [max_wal_senders](https://www.postgresql.org/docs/current/runtime-config-replication.html) should be set to at least the same as `max_replication_slots`, plus the number of senders already used on your instance.

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of senders and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job. 

To set this parameter, run the `ALTER SYSTEM SET max_wal_senders = #;` command, where # represents the number of WAL sender processes running simultaneously. 
     * [max_worker_processes](https://www.postgresql.org/docs/current/runtime-config-resource.html) should be set to at least the same number of databases that Database Migration Service is going to migrate (which is all of the databases under the source instance), plus the number of `max_worker_processes` already used on your instance. 

If you plan to use adjusted data dump parallelism settings, make sure to increase the number of worker processes and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job. 

To set this parameter, run the `ALTER SYSTEM SET max_worker_processes = #;` command, where # represents the number of databases that will be migrated. 

The parameters that you're setting in this step apply to a PostgreSQL database server that's running. You can also make these changes persistent by adding the following lines of code to the `postgresql.conf` file:

     * `shared_preload_libraries = 'pglogical';`
     * `wal_level = 'logical';`
     * `wal_sender_timeout = 0;`
     * `max_replication_slots = #;`
     * `max_wal_senders = #;`
     * `max_worker_processes = #;`
  3. To apply the configuration changes, **restart the source instance**.
  4. Configure network access and client authentication. Configuring network connectivity includes modifying the `postgresql.conf` and `pg_hba.conf` to allow incoming connections from the destination instance to your source database server. For detailed step-by-step instructions and command examples, see [Configure private IP connectivity](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpc-peering). 



### Microsoft Azure Database for PostgreSQL

To configure your Microsoft Azure Database for PostgreSQL source, follow these steps:

  1. Install [the pglogical package](https://github.com/2ndQuadrant/pglogical) on your server.
  2. **For PostgreSQL version 9.4 sources only** , install the following `pglogical` extensions on each database in your source instance:

     * `CREATE EXTENSION IF NOT EXISTS pglogical;`
     * `CREATE EXTENSION IF NOT EXISTS pglogical_origin;`
  3. **For all other versions** , install the `pglogical` extension on each database in your source instance: `CREATE EXTENSION IF NOT EXISTS pglogical`.

  4. Configure the required server parameters on your source by using the Microsoft Azure portal. For more information, see [Configure server parameters in Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-configure-server-parameters-using-portal) and [Server parameters in Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-server-parameters#customized-options) in the Microsoft documentation.

Configure the following parameters:

     * Set **`shared_preload_libraries`** to include **`pglogical`**.
     * Set **`azure.extensions`** to include **`pglogical`**.
     * Set **`wal_level`** to **`logical`**.
     * Set **`max_replication_slots`** to at least the number of subscriptions expected to connect, plus some reserves for table synchronization.

The `max_replication_slots` parameter defines the maximum number of replication slots the source instance can support.

Database Migration Service requires one slot for each database that's migrated (which is all of the databases under the source instance).

For example, if there are 5 databases on the source instance and if there are 2 migration jobs created for the source, then the number of replication slots must be at least 5 * 2 = 10, plus the number of replication slots already used by you. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of replication slots and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job. 

     * Set **`max_wal_senders`** to at least the same as **`max_replication_slots`** , plus the number of senders already used on your instance.

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12.

If you plan to use adjusted data dump parallelism settings, make sure to increase the number of senders and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job. 

     * Set **`max_worker_processes`** to at least the same number of databases that Database Migration Service is going to migrate (which is all of the databases under the source instance), plus the number of `max_worker_processes` already used on your instance.

If you plan to use adjusted data dump parallelism settings, make sure to increase the number of worker processes and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job. 

  5. Check the value of your **`require_secure_transport`** setting.

By default, Microsoft Azure databases require [SSL/TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) encryption for all incoming connections. Depending on the `require_secure_transport` value, use one of the following encryption settings when you [create the source connection profile](https://cloud.google.com/database-migration/docs/postgres/create-source-connection-profile):

     * If `require_secure_transport` is set to `on`, select **Basic** , **TLS** , or **mTLS**.
     * If `require_secure_transport` is set to `off`, select **None**.
  6. To apply the configuration changes, **restart the source instance**.



### Amazon RDS PostgreSQL

  1. Install the `pglogical` extension on your source database.

For more information, see [ Using PostgreSQL extensions with Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.html#Appendix.PostgreSQL.CommonDBATasks.pglogical.requirements-limitations) in the Amazon RDS documentation.

  2. Configure the source instance using [parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication). 

     1. [Create a new parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.Creating). In the parameter group:
        * Make sure the `shared_preload_libraries` parameter includes `pglogical`.
        * Set the `rds.logical_replication` parameter to 1. This will enable WAL logs at the 'logical' level.
        * Set the `wal_sender_timeout` parameter to 0. This will disable the timeout mechanism that's used to terminate inactive replication connections.
        * Set the [max_replication_slots](https://www.postgresql.org/docs/current/runtime-config-replication.html) parameter. This parameter defines the maximum number of replication slots the source instance can support. It must be set to at least the number of subscriptions expected to connect, plus some reserves for table synchronization.

Database Migration Service requires one slot for each database that's migrated (which is all of the databases under the source instance).

For example, if there are 5 databases on the source instance and if there will be 2 migration jobs created for the source, then the number of replication slots must be at least 5 * 2 = 10, plus the number of replication slots already used by you. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of replication slots and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job.

The default value for this parameter is **10**.

        * Set the [max_wal_senders](https://www.postgresql.org/docs/current/runtime-config-replication.html) parameter to at least the same as `max_replication_slots`, plus the number of senders already used on your instance.

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of senders and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job. 

The default value for this parameter is **10**.

        * Set the [max_worker_processes](https://www.postgresql.org/docs/current/runtime-config-resource.html) source parameter to at least the same number of databases that Database Migration Service is going to migrate (which is all of the databases under the source instance), plus the number of `max_worker_processes` already used on your instance. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of worker processes and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job. 

The default value for this parameter is **8**.

     2. Attach the parameter group to the instance. If you're creating a new instance, then you can find this option under **Additional Configuration**.

Otherwise, modify the instance to attach the parameter group.

  3. To apply the configuration changes, **restart the source instance**.


Note: The `pglogical` extension can log credentials in plain text on the source instance. This behavior is caused by the extension itself, and is unrelated to either Database Migration Service or Cloud SQL.

### Cloud SQL for PostgreSQL

Enable logical replication and decoding for the source database by configuring the following flags:

All settings in this section are configured using flags in Cloud SQL. To enable flags in Cloud SQL, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags). 

  1. Set the `cloudsql.logical_decoding` and `cloudsql.enable_pglogical` flags to `on`. 
  2. Set the [max_replication_slots](https://www.postgresql.org/docs/current/runtime-config-replication.html) flag. This flag defines the maximum number of replication slots that the source instance can support. It must be set to at least the number of subscriptions expected to connect, plus some reserves for table synchronization.

Database Migration Service requires one slot for each database that's migrated (which is all of the databases under the source instance).

For example, if there are 5 databases on the source instance and if there will be 2 migration jobs created for the source, then the number of replication slots must be at least 5 * 2 = 10, plus the number of replication slots already used by you. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of replication slots and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job.

The default value for this flag is **10**.

  3. Set the [max_wal_senders](https://www.postgresql.org/docs/current/runtime-config-replication.html) flag to at least the same as `max_replication_slots`, plus the number of senders already used on your instance.

For example, if the `max_replication_slots` flag is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of senders and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job. 

The default value for this flag is **10**.

  4. Set the [ max_worker_processes](https://www.postgresql.org/docs/current/runtime-config-resource.html) source flag to at least the same number of databases that Database Migration Service is going to migrate (which is all of the databases under the source instance), plus the number of `max_worker_processes` already used on your instance. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of worker processes and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#test-create) when you create the migration job.

The default value for this flag is **8**.

  5. Set the [ `wal_sender_timeout`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) parameter to `0`. The `0` value disables the timeout mechanism that terminates inactive replication connections. 

  6. **Restart your source instance** so that the configuration changes that you made to the flags can take effect.



## Enable replication delay monitoring for PostgreSQL version earlier than 9.6

If you're migrating from a PostgreSQL version earlier than 9.6, then the replication delay metric isn't available by default. The following alternatives allow you to track this metric to ensure minimal downtime when you promote the database:

  * **Option 1** : Enable Database Migration Service to track the replication delay by granting access to a specific query. Using a user with the `SUPERUSER` privilege, perform the following:

    1. Define the following function to allow Database Migration Service to query for the replication delay.
           
           CREATE OR REPLACE FUNCTION pg_stat_replication_user()
           RETURNS TABLE (
           pid               integer                  ,
           usesysid          oid                      ,
           username          name                    ,
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
           

    2. Grant the `EXECUTE` permission to the USER by running the following commands:

       1. `REVOKE EXECUTE ON FUNCTION pg_stat_replication_user() FROM public;`
       2. `GRANT EXECUTE ON FUNCTION pg_stat_replication_user() to {replication_user};`
  * **Option 2** : Grant the `SUPERUSER` privilege directly to the USER used to connect to the source instance. This will allow Database Migration Service to read the replication delay directly.

  * **Option 3** : Track the replication delay independently by using the following query:

For PostgreSQL versions earlier than 10, run this command as a `superuser`.
        
        SELECT current_timestamp, application_name,
            pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.sent_location) AS sent_location_lag,
            pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.write_location) AS write_location_lag,
            pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.flush_location) AS flush_location_lag,
            pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.replay_location) AS replay_location_lag
            FROM pg_stat_replication
            WHERE application_name like 'cloudsql%';
          

In this option, Database Migration Service won't reflect the replication delay metric in the graphs or API responses.




[ Previous arrow_back  Get set up  ](https://docs.cloud.google.com/database-migration/docs/postgres/setup)

[ Next Create a source connection profile  arrow_forward  ](https://docs.cloud.google.com/database-migration/docs/postgres/create-source-connection-profile)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


