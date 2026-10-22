---
url: https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database/
title: Configure your source PostgreSQL database for continuous migrations \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:29.340955+00:00
---

# Configure your source PostgreSQL database for continuous migrations  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Configure your source PostgreSQL database for continuous migrations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure your source database instances for standard homogeneous PostgreSQL migrations. If you want to use quick-start migrations, follow the [ Use quick-start migrations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations#limitations) guide. Quick-start migrations provide a simplified migration flow that uses `pgnative` replication and specialized connectivity based on Private Service Connect interfaces. For more information, see [ About quick-start migrations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations) in the main Database Migration Service documentation.

This page includes sections for every supported source:

  * Self-managed PostgreSQL (on-premises or on a Compute Engine VM)
  * Amazon RDS for PostgreSQL
  * Amazon Aurora for PostgreSQL
  * Microsoft Azure Database for PostgreSQL Flexible Server
  * Cloud SQL for PostgreSQL



## Configure a self-managed PostgreSQL source

To configure a self-managed PostgreSQL source instance (on-premises or hosted on a Compute Engine VM) for your migration process, do the following:

  1. For self-managed PostgreSQL sources, Database Migration Service migrates all databases under your source instance **except** the template databases `template0` and `template1`. 
  2. Ensure that your source instance includes the default `postgres` database. If this database doesn't exist, create it before configuring your migration. 
  3. Configure network client authentication in your `pg_hba.conf` file. Add entries allowing replication connections and database access from the destination Cloud SQL outbound IP address, VPC CIDR range, or reverse SSH bastion host: 
         
         # Allow replication connections
         host  replication  MIGRATION_USER_ACCOUNT_NAME  DESTINATION_IP_OR_CIDR  md5
         # Allow database access
         host  all          MIGRATION_USER_ACCOUNT_NAME  DESTINATION_IP_OR_CIDR  md5

Reload the PostgreSQL configuration to apply the `pg_hba.conf` rules:
         
         SELECT pg_reload_conf();

  4. Verify the PostgreSQL extensions installed on your source databases. Database Migration Service doesn't migrate [extensions that are unsupported by Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extensions). Verify that your source database objects and application queries don't reference unsupported extensions. Remove unsupported extensions and references from your source databases before proceeding. 

The [`pg_cron` extension](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_cron) isn't migrated automatically by Database Migration Service, but is supported in Cloud SQL for PostgreSQL destinations. If you use `pg_cron` in your source database, reinstall and configure it on the destination instance after you promote the migration. 

  5. Create a dedicated migration user account in your source instance and grant it the necessary privileges: 
     1. Connect to the source instance using an administrative account, create the user, and assign the replication role: 
            
            CREATE USER MIGRATION_USER_ACCOUNT_NAME WITH PASSWORD 'PASSWORD';
            ALTER USER MIGRATION_USER_ACCOUNT_NAME WITH REPLICATION;

     2. Grant the migration user account the required permissions for the default `postgres` database as well as every database you want to migrate. Run the following commands on each database for each schema (except for the information schema and schemas starting with `pg_`): 
            
            GRANT USAGE ON SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT USAGE ON SCHEMA pglogical TO PUBLIC;
            GRANT SELECT ON ALL TABLES IN SCHEMA pglogical TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT ON ALL TABLES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT ON ALL SEQUENCES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";

  6. Install the `pglogical` extension on each database you want to migrate, excluding `template0` and `template1`: 
     * _For PostgreSQL version 9.4:_ Run the following command: 
           
           CREATE EXTENSION IF NOT EXISTS pglogical;
           CREATE EXTENSION IF NOT EXISTS pglogical_origin;

     * _For PostgreSQL version 9.5 and later:_ Run the following command: 
           
           CREATE EXTENSION IF NOT EXISTS pglogical;

  7. Verify that your tables have primary keys. For continuous migrations, PostgreSQL logical replication requires tables to have primary keys to replicate `UPDATE` and `DELETE` operations during the Change Data Capture (CDC) phase: 
     * Tables with a primary key replicate all `INSERT`, `UPDATE`, and `DELETE` operations automatically. 
     * For tables that don't have primary keys, Database Migration Service supports migration of only the **initial snapshot and subsequent`INSERT` statements during the CDC phase**. You must migrate `UPDATE` and `DELETE` statements manually. 

We recommend that you add primary keys to tables that don't have them before you start the migration. To learn how to generate a query to list tables in a PostgreSQL database without primary keys, or how to manually migrate `UPDATE` and `DELETE` operations, see [ Debugging and other tools](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools#alter-table). 

Alternatively, you can try to use the quick-start migration flow: a simplified migration scenario where you can use `REPLICA IDENTITY` to migrate tables without primary keys. For more information, see the [ Use quick-start migrations](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide) guide. 

  8. _Sources running PostgreSQL version 9.5 and earlier_ : The replication delay metric isn't available for source instances running PostgreSQL versions earlier than 9.6. If you want to use this metric to track migration progress, see [ Enable replication delay](https://docs.cloud.google.com/database-migration/docs/postgres/enable-replication-delay). 
  9. Install the `pglogical` package and configure WAL and replication parameters on your PostgreSQL server: 
     1. Install the `pglogical` package on your database server host operating system. For packages and installation instructions for your distribution, see the [pglogical GitHub repository](https://github.com/2ndQuadrant/pglogical). 
     2. Connect to your PostgreSQL instance using an administrative account and set the following parameters: 
        1. Set `shared_preload_libraries` to include `'pglogical'`: 
               
               ALTER SYSTEM SET shared_preload_libraries = 'pglogical';

If other libraries are already loaded in your instance, append `'pglogical'` to the existing comma-separated list. To view existing libraries, run `SHOW shared_preload_libraries;`.
        2. Set `wal_level` to `'logical'`: 
               
               ALTER SYSTEM SET wal_level = 'logical';

See [`wal_level`](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-WAL-LEVEL) in the PostgreSQL documentation.

        3. Set `wal_sender_timeout` to `0`: 
               
               ALTER SYSTEM SET wal_sender_timeout = 0;

The `0` value disables the timeout mechanism that terminates inactive replication connections. See [`wal_sender_timeout`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT). 

        4. Set `max_replication_slots` to at least the number of databases to migrate multiplied by the number of migration jobs, plus reserves for table synchronization: 

For example, if there are 5 databases on the source instance and you create 2 migration jobs for that source, then the number of replication slots must be at least 5 * 2 = 10, plus the number of replication slots already used on the source by other tasks. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of replication slots and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/database-migration/docs/postgres/migration-job-actions#test) when you create the migration job. 
               
               ALTER SYSTEM SET max_replication_slots = MAX_REPLICATION_SLOTS;

The default value for this parameter is **10**. See [`max_replication_slots`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS). 

        5. Set `max_wal_senders` to at least the value of `max_replication_slots` plus the number of senders already used on your instance: 

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of senders and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/database-migration/docs/postgres/migration-job-actions#test) when you create the migration job. 
               
               ALTER SYSTEM SET max_wal_senders = MAX_WAL_SENDERS;

The default value for this parameter is **10**. See [`max_wal_senders`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-WAL-SENDERS). 

        6. Set `max_worker_processes` to at least the number of databases to migrate plus existing worker processes on your instance. If you plan to use adjusted data dump parallelism settings, account for two additional worker processes per connection (up to a maximum of 20 workers): 
               
               ALTER SYSTEM SET max_worker_processes = MAX_WORKER_PROCESSES;

The default value for this parameter is **8**. See [`max_worker_processes`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES). 

Alternatively, you can make these changes persistent by adding the parameters directly to your `postgresql.conf` configuration file: 
    
    shared_preload_libraries = 'pglogical'
    wal_level = 'logical'
    wal_sender_timeout = 0
    max_replication_slots = MAX_REPLICATION_SLOTS
    max_wal_senders = MAX_WAL_SENDERS
    max_worker_processes = MAX_WORKER_PROCESSES

  10. Restart your PostgreSQL server so that the configuration changes can take effect.



## Configure an Amazon RDS for PostgreSQL source

To configure an Amazon RDS for PostgreSQL source instance for your migration process, do the following:

  1. For Amazon RDS for PostgreSQL sources, Database Migration Service migrates all databases under your source instance **except** the template databases `template0`, `template1`, and the AWS internal database `rdsadmin`. 
  2. Ensure that your source instance includes the default `postgres` database. If this database doesn't exist, create it before configuring your migration. 
  3. Configure your Amazon RDS VPC security group inbound rules. Allow incoming TCP connections on port `5432` from the destination Cloud SQL outbound IP address, VPC CIDR range, or reverse SSH bastion host VM. 
  4. Verify the PostgreSQL extensions installed on your source databases. Database Migration Service doesn't migrate [extensions that are unsupported by Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extensions). Verify that your source database objects and application queries don't reference unsupported extensions. Remove unsupported extensions and references from your source databases before proceeding. 

The [`pg_cron` extension](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_cron) isn't migrated automatically by Database Migration Service, but is supported in Cloud SQL for PostgreSQL destinations. If you use `pg_cron` in your source database, reinstall and configure it on the destination instance after you promote the migration. 

  5. Create a dedicated migration user account in your source instance and grant it the necessary privileges: 
     1. Connect to the source instance using an administrative account, create the user, and grant the AWS-managed `rds_replication` role: 
            
            CREATE USER MIGRATION_USER_ACCOUNT_NAME WITH PASSWORD 'PASSWORD';
            GRANT rds_replication TO "MIGRATION_USER_ACCOUNT_NAME";

     2. Grant the migration user account the required permissions for the default `postgres` database as well as every database you want to migrate. Run the following commands on each database for each schema (except for the information schema and schemas starting with `pg_`): 
            
            GRANT USAGE ON SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT USAGE ON SCHEMA pglogical TO PUBLIC;
            GRANT SELECT ON ALL TABLES IN SCHEMA pglogical TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT ON ALL TABLES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT ON ALL SEQUENCES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";

  6. Install the `pglogical` extension on each database you want to migrate, excluding `template0`, `template1`, and `rdsadmin`: 
     * _For PostgreSQL version 9.4:_ Run the following command: 
           
           CREATE EXTENSION IF NOT EXISTS pglogical;
           CREATE EXTENSION IF NOT EXISTS pglogical_origin;

     * _For PostgreSQL version 9.5 and later:_ Run the following command: 
           
           CREATE EXTENSION IF NOT EXISTS pglogical;

For more details on requirements, see [ Using PostgreSQL extensions with Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.html#Appendix.PostgreSQL.CommonDBATasks.pglogical.requirements-limitations) in the AWS documentation. 

**Note:** The `pglogical` extension can log credentials in plain text in database logs on the source instance. This is a known behavior of the extension itself and is unrelated to Database Migration Service or Cloud SQL. 
  7. Verify that your tables have primary keys. For continuous migrations, PostgreSQL logical replication requires tables to have primary keys to replicate `UPDATE` and `DELETE` operations during the Change Data Capture (CDC) phase: 
     * Tables with a primary key replicate all `INSERT`, `UPDATE`, and `DELETE` operations automatically. 
     * For tables that don't have primary keys, Database Migration Service supports migration of only the **initial snapshot and subsequent`INSERT` statements during the CDC phase**. You must migrate `UPDATE` and `DELETE` statements manually. 

We recommend that you add primary keys to tables that don't have them before you start the migration. To learn how to generate a query to list tables in a PostgreSQL database without primary keys, or how to manually migrate `UPDATE` and `DELETE` operations, see [ Debugging and other tools](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools#alter-table). 

Alternatively, you can try to use the quick-start migration flow: a simplified migration scenario where you can use `REPLICA IDENTITY` to migrate tables without primary keys. For more information, see the [ Use quick-start migrations](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide) guide. 

  8. _Sources running PostgreSQL version 9.5 and earlier_ : The replication delay metric isn't available for source instances running PostgreSQL versions earlier than 9.6. If you want to use this metric to track migration progress, see [ Enable replication delay](https://docs.cloud.google.com/database-migration/docs/postgres/enable-replication-delay). 
  9. Configure a custom DB parameter group and attach it to your instance: 
     1. Create a custom parameter group (see [ Working with DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.Creating) in the AWS documentation) and configure the following parameters: 
        1. Set `shared_preload_libraries` to include `pglogical`.
        2. Set `rds.logical_replication` to `1`. This parameter enables logical WAL logging in Amazon RDS. See [Logical replication for Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication.html). 
        3. Set `wal_sender_timeout` to `0`. The `0` value disables the timeout mechanism that terminates inactive replication connections.
        4. Set `max_replication_slots` to at least the number of databases to migrate multiplied by the number of migration jobs, plus reserves for table synchronization: 

For example, if there are 5 databases on the source instance and you create 2 migration jobs for that source, then the number of replication slots must be at least 5 * 2 = 10, plus the number of replication slots already used on the source by other tasks. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of replication slots and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/database-migration/docs/postgres/migration-job-actions#test) when you create the migration job. 

The default value for this parameter is **10**.

        5. Set `max_wal_senders` to at least the value of `max_replication_slots` plus the number of senders already used on your instance: 

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of senders and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/database-migration/docs/postgres/migration-job-actions#test) when you create the migration job. 

The default value for this parameter is **10**.

        6. Set `max_worker_processes` to at least the number of databases to migrate plus existing worker processes on your instance. If you plan to use adjusted data dump parallelism settings, account for two additional worker processes per connection (up to a maximum of 20 workers): 

The default value for this parameter is **8**.

     2. Attach the parameter group to your RDS DB instance. If you're creating a new instance, you can find this option under **Additional Configuration**. Otherwise, modify the instance to attach the parameter group. 
  10. Restart your Amazon RDS instance so that the parameter group changes can take effect.



## Configure an Amazon Aurora for PostgreSQL source

To configure an Amazon Aurora PostgreSQL source cluster for your migration process, do the following:

  1. For Amazon Aurora for PostgreSQL sources, Database Migration Service migrates all databases under your source cluster **except** the template databases `template0`, `template1`, and the AWS internal database `rdsadmin`. 
  2. Ensure that your source cluster includes the default `postgres` database. If this database doesn't exist, create it before configuring your migration. 
  3. Configure your Amazon Aurora cluster VPC security group inbound rules. Allow incoming TCP connections on port `5432` from the destination Cloud SQL outbound IP address, VPC CIDR range, or reverse SSH bastion host VM. 
  4. Verify the PostgreSQL extensions installed on your source databases. Database Migration Service doesn't migrate [extensions that are unsupported by Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extensions). Verify that your source database objects and application queries don't reference unsupported extensions. Remove unsupported extensions and references from your source databases before proceeding. 

The [`pg_cron` extension](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_cron) isn't migrated automatically by Database Migration Service, but is supported in Cloud SQL for PostgreSQL destinations. If you use `pg_cron` in your source database, reinstall and configure it on the destination instance after you promote the migration. 

  5. Create a dedicated migration user account in your source cluster and grant it the necessary privileges: 
     1. Connect to the source cluster using an administrative account, create the user, and grant the AWS-managed `rds_replication` role: 
            
            CREATE USER MIGRATION_USER_ACCOUNT_NAME WITH PASSWORD 'PASSWORD';
            GRANT rds_replication TO "MIGRATION_USER_ACCOUNT_NAME";

     2. Grant the migration user account the required permissions for the default `postgres` database as well as every database you want to migrate. Run the following commands on each database for each schema (except for the information schema and schemas starting with `pg_`): 
            
            GRANT USAGE ON SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT USAGE ON SCHEMA pglogical TO PUBLIC;
            GRANT SELECT ON ALL TABLES IN SCHEMA pglogical TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT ON ALL TABLES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT ON ALL SEQUENCES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";

  6. Install the `pglogical` extension on each database you want to migrate, excluding `template0`, `template1`, and `rdsadmin`: 
         
         CREATE EXTENSION IF NOT EXISTS pglogical;

**Note:** The `pglogical` extension can log credentials in plain text in database logs on the source instance. This is a known behavior of the extension itself and is unrelated to Database Migration Service or Cloud SQL. 
  7. Verify that your tables have primary keys. For continuous migrations, PostgreSQL logical replication requires tables to have primary keys to replicate `UPDATE` and `DELETE` operations during the Change Data Capture (CDC) phase: 
     * Tables with a primary key replicate all `INSERT`, `UPDATE`, and `DELETE` operations automatically. 
     * For tables that don't have primary keys, Database Migration Service supports migration of only the **initial snapshot and subsequent`INSERT` statements during the CDC phase**. You must migrate `UPDATE` and `DELETE` statements manually. 

We recommend that you add primary keys to tables that don't have them before you start the migration. To learn how to generate a query to list tables in a PostgreSQL database without primary keys, or how to manually migrate `UPDATE` and `DELETE` operations, see [ Debugging and other tools](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools#alter-table). 

Alternatively, you can try to use the quick-start migration flow: a simplified migration scenario where you can use `REPLICA IDENTITY` to migrate tables without primary keys. For more information, see the [ Use quick-start migrations](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide) guide. 

  8. Configure a custom DB cluster parameter group and attach it to your cluster: 
     1. Create a custom DB cluster parameter group and configure the following parameters: 
        1. Set `shared_preload_libraries` to include `pglogical`.
        2. Set `rds.logical_replication` to `1`. This parameter enables logical WAL logging.
        3. Set `wal_sender_timeout` to `0`. The `0` value disables the timeout mechanism that terminates inactive replication connections.
        4. Set `max_replication_slots` to at least the number of databases to migrate multiplied by the number of migration jobs, plus reserves for table synchronization: 

For example, if there are 5 databases on the source instance and you create 2 migration jobs for that source, then the number of replication slots must be at least 5 * 2 = 10, plus the number of replication slots already used on the source by other tasks. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of replication slots and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/database-migration/docs/postgres/migration-job-actions#test) when you create the migration job. 

The default value for this parameter is **10**.

        5. Set `max_wal_senders` to at least the value of `max_replication_slots` plus the number of senders already used on your instance: 

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of senders and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/database-migration/docs/postgres/migration-job-actions#test) when you create the migration job. 

The default value for this parameter is **10**.

        6. Set `max_worker_processes` to at least the number of databases to migrate plus existing worker processes on your instance. If you plan to use adjusted data dump parallelism settings, account for two additional worker processes per connection (up to a maximum of 20 workers): 

The default value for this parameter is **8**.

     2. Attach the DB cluster parameter group to the Aurora DB cluster.
  9. Restart your Amazon Aurora DB cluster so that the parameter group changes can take effect.



## Configure an Microsoft Azure Database for PostgreSQL Flexible Server source

To configure an Microsoft Azure Database for PostgreSQL Flexible Server Flexible Server source instance for your migration process, do the following:

  1. For Microsoft Azure Database for PostgreSQL Flexible Server sources, Database Migration Service migrates all databases under your source instance **except** the Azure system and template databases: `azure_maintenance`, `azure_sys`, `template0`, and `template1`. 
  2. Ensure that your source instance includes the default `postgres` database. If this database doesn't exist, create it before configuring your migration. 
  3. Configure Azure firewall and SSL/TLS settings: 
     1. In Azure networking settings, add firewall rules allowing inbound TCP connections on port `5432` from the destination Cloud SQL outbound IP address, VPC CIDR range, or reverse SSH bastion host VM.
     2. Check the value of the `require_secure_transport` server parameter. By default, Azure databases require SSL/TLS encryption for incoming connections. Depending on the `require_secure_transport` setting, select one of the following encryption settings when you [create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-source-connection-profile): 
        * If `require_secure_transport` is set to `on`, select **Basic** , **TLS** , or **mTLS**.
        * If `require_secure_transport` is set to `off`, select **None**.
  4. Verify the PostgreSQL extensions installed on your source databases. Database Migration Service doesn't migrate [extensions that are unsupported by Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extensions). Verify that your source database objects and application queries don't reference unsupported extensions. Remove unsupported extensions and references from your source databases before proceeding. 

The [`pg_cron` extension](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_cron) isn't migrated automatically by Database Migration Service, but is supported in Cloud SQL for PostgreSQL destinations. If you use `pg_cron` in your source database, reinstall and configure it on the destination instance after you promote the migration. 

  5. Create a dedicated migration user account in your source instance and grant it the necessary privileges: 
     1. Connect to the source instance using an administrative account, create the user, and assign the replication role: 
            
            CREATE USER MIGRATION_USER_ACCOUNT_NAME WITH PASSWORD 'PASSWORD';
            ALTER USER MIGRATION_USER_ACCOUNT_NAME WITH REPLICATION;

     2. Grant the migration user account the required permissions for the default `postgres` database as well as every database you want to migrate. Run the following commands on each database for each schema (except for the information schema and schemas starting with `pg_`): 
            
            GRANT USAGE ON SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT USAGE ON SCHEMA pglogical TO PUBLIC;
            GRANT SELECT ON ALL TABLES IN SCHEMA pglogical TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT ON ALL TABLES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT ON ALL SEQUENCES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";

  6. Install the `pglogical` extension on each database you want to migrate, excluding `azure_maintenance`, `azure_sys`, `template0`, and `template1`: 
     * _For PostgreSQL version 9.4:_ Run the following command: 
           
           CREATE EXTENSION IF NOT EXISTS pglogical;
           CREATE EXTENSION IF NOT EXISTS pglogical_origin;

     * _For PostgreSQL version 9.5 and later:_ Run the following command: 
           
           CREATE EXTENSION IF NOT EXISTS pglogical;

  7. Verify that your tables have primary keys. For continuous migrations, PostgreSQL logical replication requires tables to have primary keys to replicate `UPDATE` and `DELETE` operations during the Change Data Capture (CDC) phase: 
     * Tables with a primary key replicate all `INSERT`, `UPDATE`, and `DELETE` operations automatically. 
     * For tables that don't have primary keys, Database Migration Service supports migration of only the **initial snapshot and subsequent`INSERT` statements during the CDC phase**. You must migrate `UPDATE` and `DELETE` statements manually. 

We recommend that you add primary keys to tables that don't have them before you start the migration. To learn how to generate a query to list tables in a PostgreSQL database without primary keys, or how to manually migrate `UPDATE` and `DELETE` operations, see [ Debugging and other tools](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools#alter-table). 

Alternatively, you can try to use the quick-start migration flow: a simplified migration scenario where you can use `REPLICA IDENTITY` to migrate tables without primary keys. For more information, see the [ Use quick-start migrations](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide) guide. 

  8. _Sources running PostgreSQL version 9.5 and earlier_ : The replication delay metric isn't available for source instances running PostgreSQL versions earlier than 9.6. If you want to use this metric to track migration progress, see [ Enable replication delay](https://docs.cloud.google.com/database-migration/docs/postgres/enable-replication-delay). 
  9. Configure the following server parameters in Azure. For more information, see [Configure server parameters in Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/parameters/how-to-parameters-set-value). 
     1. Set `shared_preload_libraries` to include `pglogical`.
     2. Set `azure.extensions` to include `pglogical`.
     3. Set `wal_level` to `logical`.
     4. Set `wal_sender_timeout` to `0`. The `0` value disables the timeout mechanism that terminates inactive replication connections.
     5. Set `max_replication_slots` to at least the number of databases to migrate multiplied by the number of migration jobs, plus reserves for table synchronization: 

For example, if there are 5 databases on the source instance and you create 2 migration jobs for that source, then the number of replication slots must be at least 5 * 2 = 10, plus the number of replication slots already used on the source by other tasks. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of replication slots and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/database-migration/docs/postgres/migration-job-actions#test) when you create the migration job. 

The default value for this parameter is **10**.

     6. Set `max_wal_senders` to at least the value of `max_replication_slots` plus the number of senders already used on your instance: 

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of senders and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/database-migration/docs/postgres/migration-job-actions#test) when you create the migration job. 

The default value for this parameter is **10**.

     7. Set `max_worker_processes` to at least the number of databases to migrate plus existing worker processes on your instance. If you plan to use adjusted data dump parallelism settings, account for two additional worker processes per connection (up to a maximum of 20 workers): 

The default value for this parameter is **8**.

For more parameter details, see the list of all [Server parameters in Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-server-parameters#customized-options) in the Microsoft documentation. 

  10. Restart your Microsoft Azure Database for PostgreSQL Flexible Server Flexible Server instance so that the server parameter changes can take effect.



## Configure a Cloud SQL for PostgreSQL source

To configure a Cloud SQL for PostgreSQL source instance for your migration process, do the following:

  1. For Cloud SQL for PostgreSQL sources, Database Migration Service migrates all databases under your source instance **except** the template databases `template0` and `template1`. 
  2. Ensure that your source instance includes the default `postgres` database. If this database doesn't exist, create it before configuring your migration. 
  3. If you migrate from a Cloud SQL source instance configured with a private IP address to a Cloud SQL destination instance that uses a non-RFC 1918 address IP range, add the non-RFC 1918 range to the authorized networks of your source instance. For more information, see [ Configure authorized networks](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks). 
  4. Verify the PostgreSQL extensions installed on your source databases. Database Migration Service doesn't migrate [ extensions that are unsupported by Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extensions). Verify that your source database objects and application queries don't reference unsupported extensions. Remove unsupported extensions and references from your source databases before proceeding. 

The [ `pg_cron` extension](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_cron) isn't migrated automatically by Database Migration Service, but it is supported in Cloud SQL for PostgreSQL destinations. If you use `pg_cron` in your source database, reinstall and configure it on the destination instance after you promote the migration. 

  5. Create a dedicated migration user account in your source instance and grant it the necessary privileges: 
     1. Follow the steps on the [ Create a user](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users) page in the Cloud SQL documentation. 
     2. Grant the migration user account the required permissions for the default `postgres` database as well as every database you want to migrate. Run the following commands on each database for each schema (except for the information schema and schemas starting with `pg_`): 
            
            GRANT USAGE ON SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT USAGE ON SCHEMA pglogical TO PUBLIC;
            GRANT SELECT ON ALL TABLES IN SCHEMA pglogical TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT ON ALL TABLES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT ON ALL SEQUENCES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";

  6. Install the `pglogical` extension on each database you want to migrate, excluding `template0` and `template1`: 
     * _For PostgreSQL version 9.4:_ Run the following command: 
           
           CREATE EXTENSION IF NOT EXISTS pglogical;
           CREATE EXTENSION IF NOT EXISTS pglogical_origin;

     * _For PostgreSQL version 9.5 and later:_ Run the following command: 
           
           CREATE EXTENSION IF NOT EXISTS pglogical;

  7. Verify that your tables have primary keys. For continuous migrations, PostgreSQL logical replication requires tables to have primary keys to replicate `UPDATE` and `DELETE` operations during the Change Data Capture (CDC) phase: 
     * Tables with a primary key replicate all `INSERT`, `UPDATE`, and `DELETE` operations automatically. 
     * For tables that don't have primary keys, Database Migration Service migrates the initial snapshot and subsequent `INSERT` statements during the CDC phase. You must migrate `UPDATE` and `DELETE` statements manually. 

We recommend that you add primary keys to tables that don't have them before you start the migration. To learn how to generate a query to list tables in a PostgreSQL database without primary keys, or how to manually migrate `UPDATE` and `DELETE` operations, see [ Debugging and other tools](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools#alter-table). 

Alternatively, you can try to use the quick-start migration flow: a simplified migration scenario where you can use `REPLICA IDENTITY` to migrate tables without primary keys. For more information, see the [ Use quick-start migrations](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide) guide. 

  8. _Sources running PostgreSQL version 9.5 and earlier_ : The replication delay metric isn't available for source instances running PostgreSQL versions earlier than 9.6. If you want to use this metric to track migration progress, see [ Enable replication delay](https://docs.cloud.google.com/database-migration/docs/postgres/enable-replication-delay). 
  9. Configure the following database flags on your Cloud SQL source instance: 
     1. Set `cloudsql.logical_decoding` to `on`.
     2. Set `cloudsql.enable_pglogical` to `on`.
     3. Set `wal_sender_timeout` to `0`. The `0` value disables the timeout mechanism that terminates inactive replication connections. 
     4. Set `max_replication_slots` to at least the number of databases to migrate multiplied by the number of migration jobs, plus reserves for table synchronization 

For example, if there are 5 databases on the source instance and you create 2 migration jobs for that source source, then the number of replication slots must be at least 5 * 2 = 10, plus the number of replication slots already used on the source by other tasks. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of replication slots and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/database-migration/docs/postgres/migration-job-actions#test) when you create the migration job. 

The default value for this flag is **10**. 

     5. Set `max_wal_senders` to at least the value of `max_replication_slots` plus the number of senders already used on your instance. 

For example, if the `max_replication_slots` flag is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be 10 + 2 = 12. If you plan to use adjusted data dump parallelism settings, make sure to increase the number of senders and verify your configuration by [ running the migration job test](https://docs.cloud.google.com/database-migration/docs/postgres/database-migration/docs/postgres/migration-job-actions#test) when you create the migration job. 

The default value for this flag is **10**.

     6. Set `max_worker_processes` to at least the number of databases to migrate plus existing worker processes on your instance. If you plan to use adjusted data dump parallelism settings, account for two additional worker processes per connection (up to a maximum of 20 workers). 

The default value for this flag is **8**. 

For more information on modifying flags, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags) in the Cloud SQL documentation. 

  10. Restart your source Cloud SQL instance so that the database flag changes can take effect. 



## What's next

  * For complete, step-by-step migration walkthroughs, see [ Get started with Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).

  * To plan network connectivity between your source and destination instances, see [ Networking overview](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
