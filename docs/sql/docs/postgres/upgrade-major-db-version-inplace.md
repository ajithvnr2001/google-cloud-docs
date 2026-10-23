---
url: https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace/
title: Upgrade the database major version in-place \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:00.622143+00:00
---

# Upgrade the database major version in-place  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Upgrade the database major version in-place Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-inplace "View this page for the SQL Server database engine")

This page describes how to upgrade the database major version by upgrading your Cloud SQL instance in-place rather than [by migrating data](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-migrate).

## Introduction

Database software providers periodically release new major versions that contain new features, performance improvements, and security enhancements. Cloud SQL takes in [new versions](https://docs.cloud.google.com/sql/docs/postgres/db-versions) after they're released. After Cloud SQL offers support for a new major version, you can upgrade your instances to keep your database updated.

You can upgrade the database version of an instance in-place or by [migrating data](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-migrate). In-place upgrades are a simpler way to upgrade your instance's major version. You don't need to migrate data or change application connection strings. With in-place upgrades, you can retain the name, IP address, and other settings of your current instance after the upgrade. In-place upgrades don't require you to move data files and can be completed faster. In some cases, the downtime is shorter than what migrating your data entails.

The Cloud SQL for the PostgreSQL in-place upgrade operation uses the [`pg_upgrade`](https://www.postgresql.org/docs/14/static/pgupgrade.html) utility. 

## Plan a major version upgrade

  1. Confirm that you have the required role to perform a major version upgrade: [Cloud SQL Owner](https://docs.cloud.google.com/sql/docs/postgres/iam-roles) or [Cloud SQL Admin](https://docs.cloud.google.com/sql/docs/postgres/iam-roles).
  2. Choose a target major version.

### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

To check the database versions that you can target for an in-place upgrade on your instance, do the following:

     1. Run the following command.
    
    gcloud sql instances describe INSTANCE_NAME
       

Replace INSTANCE_NAME with the name of the instance.

     2. In the output of the command, locate the section that is labeled `upgradableDatabaseVersions`.
     3. Each subsection returns a database version that is available for upgrade. In each subsection, review the following fields.
        * `majorVersion`: the major version that you can target for the in-place upgrade.
        * `name`: the database version string that includes the major version.
        * `displayName`: the display name for the database version. 

### REST v1

To check which target database versions are available for a major version in-place upgrade, use the [`instances.get`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/get) method of the Cloud SQL Admin API.

Before using any of the request data, make the following replacements: 

     * INSTANCE_NAME: The instance name.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    upgradableDatabaseVersions:
    
    {
      major_version: "POSTGRES_15_0"
      name: "POSTGRES_15_0"
      display_name: "PostgreSQL 15.0"
    }
    
    

### REST v1beta4 

To check which target database versions are available for major version in-place upgrade of an instance, use the [`instances.get`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/get) method of the Cloud SQL Admin API.

Before using any of the request data, make the following replacements: 

     * INSTANCE_NAME: The instance name.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    upgradableDatabaseVersions:
    
    {
      major_version: "POSTGRES_15_0"
      name: "POSTGRES_15_0"
      display_name: "PostgreSQL 15.0"
    }
    
    

For the complete list of the database versions that Cloud SQL supports, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/postgres/db-versions).

  3. Consider the features offered in each database major version and address incompatibilities.

     * [PostgreSQL 18](https://www.postgresql.org/docs/18/release-18.html)
     * [PostgreSQL 17](https://www.postgresql.org/docs/17/release-17.html)
     * [PostgreSQL 16](https://www.postgresql.org/docs/16/release-16.html)
     * [PostgreSQL 15](https://www.postgresql.org/docs/15/release-15.html)
     * [PostgreSQL 14](https://www.postgresql.org/docs/14/static/release-14.html)
     * [PostgreSQL 13](https://www.postgresql.org/docs/13/static/release-13.html)
     * [PostgreSQL 12](https://www.postgresql.org/docs/12/static/release-12.html)
     * [PostgreSQL 11](https://www.postgresql.org/docs/11/static/release-11.html)
     * [PostgreSQL 10](https://www.postgresql.org/docs/10/static/release-10.html)

New major versions introduce incompatible changes that might require you to modify the application code, the schema, or the database settings. Before you can upgrade your database instance, review the release notes of your target major version to determine the incompatibilities that you must address.

  4. Perform the precheck for upgrades.

  5. Test the upgrade with a dry run.

Perform a dry run of the end-to-end upgrade process in a test environment before you upgrade the production database. You can [clone your instance](https://docs.cloud.google.com/sql/docs/postgres/clone-instance) to create an identical copy of the data on which to test the upgrade process.

In addition to validating that the upgrade completes successfully, run tests to ensure that the application behaves as expected on the upgraded database.

**Note:** Ensure that you have enough disk space before running a major version upgrade. If you haven't enabled [automatic storage increases](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen), then take note of the disk storage used by the upgraded dry run instance. This helps you determine whether you need to increase the storage capacity for the production instance before upgrading.
  6. Decide on a time to upgrade.

Upgrading requires the instance to become unavailable for a period of time. Plan to upgrade during a time period when database activity is low.




## Prepare for a major version upgrade

Before you upgrade, complete the following steps.

  1. Check the `LC_COLLATE` value for the `template` and `postgres` databases. The character set for each database must be `en_US.UTF8`.

If the `LC_COLLATE` value for the `template` and `postgres` databases isn't `en_US.UTF8`, then the major version upgrade fails. To fix this, if either database has a character set other than `en_US.UTF8`, then change the `LC_COLLATE` value to `en_US.UTF8` before you perform the upgrade.

To change the encoding of a database:

     1. Dump your database.
     2. Drop your database.
     3. Create a new database with the different encoding (for this example, `en_US.UTF8`).
     4. Reload your data.

Another option is to rename the database:

     1. Close all connections to the database.
     2. Rename the database.
     3. Update your application configurations to use the new database name.
     4. Create a new, empty database with the default encoding.

We recommend that you perform these steps on a cloned instance before applying them to a production instance.

  2. Manage your remaining [PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions). 

Most extensions work on the upgraded database major version. Drop any extensions that are no longer supported in your target version. For example, drop the `chkpass` extension if you're upgrading to PostgreSQL 11 or later versions.

You can upgrade [PostGIS](https://docs.cloud.google.com/sql/docs/postgres/extensions#postgis) and its related extensions to their latest supported versions manually.

Sometimes, upgrading from PostGIS versions 2.x can create a situation where there are leftover database objects that aren't associated with the PostGIS extension. This can block the upgrade operation. For information about resolving this issue, see [Fixing a broken postgis raster install](https://postgis.net/documentation/tips/tip-removing-raster-from-2-3/).

Sometimes, upgrading to PostGIS version 3.1.7 or later can't complete due to objects using deprecated functions. This can block the upgrade operation. To check the upgrade status, run `SELECT PostGIS_full_version();`. If there are warnings present, then drop any objects using the deprecated functions and update the PostGIS extension to any intermediate or higher version. After you complete these actions, run the `SELECT PostGIS_full_version();` command again. Verify that no warnings appear. Then, proceed with the upgrade operation.

To learn more about upgrading your PostGIS extensions, see [Upgrading PostGIS](https://postgis.net/workshops/postgis-intro/upgrades.html#upgrading-postgis). For issues associated with upgrading PostGIS, see Check the version of your PostgreSQL instance. 
  3. Manage your custom database flags. Check the names of any custom database flags that you configured for your PostgreSQL instance. For issues associated with these flags, see Check the custom flags for your PostgreSQL instance.
  4. When performing an upgrade from one major version to another, attempt to connect to each database to see if there are any compatibility issues. Ensure that your databases can connect to each other. Check the `datallowconn` field for each database to ensure that a connection is allowed. A `t` value means that it's allowed, and an `f` value indicates that a connection can't be established.
  5. If you use the [Datadog](https://www.datadoghq.com/) installation to upgrade your Cloud SQL instance to PostgreSQL 10 or later versions, then before you perform the upgrade, drop the [pg_stat_activity()](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW) function. 
  6. Manage instances with a high number of objects.

The time required for an in-place major version upgrade depends on the number of database objects in the instance. Instances with a very large number of objects, particularly tables and indexes, might experience considerably longer upgrade times. This increases the risk of the operation timing out. Cloud SQL is optimized for instances with up to around 100,000 relations. If your instance exceeds this, the upgrade is not blocked, but it's considered less reliable and is more likely to take an extended period or fail after a 6-hour timeout.

If your instance contains a high object count, then do the following before starting the major upgrade process:

     1. Audit and drop unused objects: Identify and remove any empty tables, tables used only for testing, or any other database objects (schemas, views, functions) that are no longer needed.
     2. Optimize table structures: 
        * If you use table partitioning, then an excessive number of partitions might contribute to a high relation count. In this case, evaluate how to reduce the number of partitions that you're using.
        * Consider migrating historical or infrequently accessed data to a [different data storage option](https://cloud.google.com/products/storage). This might reduce the number of active tables or the size and complexity of existing ones.
     3. Run an upgrade test: Perform a dry run of the upgrade on a clone of your production instance. This lets you get a realistic estimate of the time required and helps you to uncover any potential issues. This estimate is especially crucial for databases with high object counts.

By reducing the overall object count and complexity, you can reduce the risks and downtime associated with major version upgrades.

  7. Manage instances with Large Objects (LOBs).

The in-place upgrade process uses the PostgreSQL `pg_upgrade` utility. This process can take a significant amount of time if the database contains a very large number of LOBs, potentially leading to upgrade failure due to timeout.

To check the number of Large Objects in your database, connect to your database instance using a PostgreSQL client, such as `psql` and run the following query:
         
         SELECT count(*) AS total_large_objects FROM pg_largeobject_metadata;
           

If your instance contains greater than 30 million LOBs, then your instance has an increased risk of timeout. For such instances, consider the following actions before starting an upgrade:

     1. **Clean up orphaned Large Objects:** PostgreSQL doesn't automatically remove LOBs that are no longer referenced. Use the [`vacuumlo`](https://www.postgresql.org/docs/current/vacuumlo.html) utility, which is part of the `contrib` module, to remove orphaned LOBs. You need to run this command from a client machine that can connect to your Cloud SQL instance. 
        * Install the `postgresql-contrib` package on your client machine if you don't have `vacuumlo`.
        * Run the following command to perform a dry run to see which LOBs would be deleted: 
              
              vacuumlo -h INSTANCE_IP -U DATABASE_USER --dry-run DATABASE_NAME
                        

Replace `INSTANCE_IP`, `DATABASE_USER`, and `DATABASE_NAME` with your instance details. You're prompted for the user's password.
        * Run the following command to remove the identified LOBs: 
              
              vacuumlo -h INSTANCE_IP -U DATABASE_USER DATABASE_NAME
                        

After running `vacuumlo`, recheck the LOB count to confirm that the cleanup was successful.
     2. **Manually delete Large Objects:** Review your application's data retention policies and remove any LOBs that are no longer necessary.
     3. **Increase instance resources:** Temporarily or permanently [increase the instance's vCPUs and memory](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#machine-type-2ndgen). This provides more resources for the `pg_upgrade` process.
     4. **Migrate your data:** If the LOB count cannot be reduced sufficiently, then consider upgrading by [migrating your data](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-migrate). You can create a custom approach using `pg_dump` and `pg_restore` specifically for LOBs. Standard logical replication methods might not fully support LOBs, potentially requiring additional steps and downtime for LOB migration.
  8. **Warning:** The in-place major version upgrade process for PostgreSQL deletes all existing [logical replication slots](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) on the instance. If you don't recreate these slots after the upgrade is complete, replication streams will be disrupted.

Record the information that you'll need to recreate all the logical replication slots on the instance, including slots used by `pglogical`, PostgreSQL built-in logical replication, Datastream, or any other logical decoding consumer.




## Known limitations

The following limitations affect in-place major version upgrades for Cloud SQL for PostgreSQL:

  * You can't perform an in-place major version upgrade on an [external replica](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-external-replica).
  * Upgrading instances that have more than 1,000 databases from one version to another might take a long time and time out.
  * Use the `select * from pg_largeobject_metadata;` statement to query for the number of large objects in each PostgreSQL database of your Cloud SQL instance. If the result from all of your databases is more than 10 million large objects, then the upgrade fails. Cloud SQL rolls back to the previous version of your database.
  * Before you perform an in-place major version upgrade to PostgreSQL 16 and later, upgrade the [PostGIS](https://docs.cloud.google.com/sql/docs/postgres/extensions#postgis) extension for all of your databases to version 3.4.0. For PostgreSQL 18, upgrade to PostGIS version 3.6.0.
  * Before you perform an in-place major version upgrade to PostgreSQL 17, upgrade the [`rdkit`](https://github.com/rdkit/rdkit/tree/master/Code/PgSQL/rdkit) extension for all of your databases to version 4.6.1.
  * Before you perform an in-place major version upgrade to PostgreSQL 16, 17, or 18, upgrade the [`pg_squeeze`](https://github.com/cybertec-postgresql/pg_squeeze) extension for all of your databases to version 1.6, 1.7, or 1.8 respectively.
  * If you're using PostgreSQL versions 9.6, 10, 11, or 12, then version 3.4.0 of the PostGIS extension isn't supported. Therefore, to perform an in-place major version upgrade to PostgreSQL 16 and later, you must first upgrade to an intermediate version of PostgreSQL (versions 13, 14, or 15).
  * If you install the [`pg_ivm`](https://github.com/sraoss/pg_ivm) extension for your instance, then you can't perform a major version upgrade. To fix this, uninstall this extension and then perform the upgrade. For more information about the extensions, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

  * If you enable the [vacuum_defer_cleanup_age](https://postgresqlco.nf/doc/en/param/vacuum_defer_cleanup_age/) and [force_parallel_mode](https://postgresqlco.nf/doc/en/param/force_parallel_mode/) flags, then you can't perform a major version upgrade. To fix this, delete these flags and then perform the upgrade. For more information about the flags, including how to delete them, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

**Note:** For PostgreSQL 16 and later, the `vacuum_defer_cleanup_age` flag is deprecated and the `force_parallel_mode` flag is renamed to [`debug_parallel_query`](https://postgresqlco.nf/doc/en/param/debug_parallel_query/). 



## Assess upgrade readiness for your instance

Cloud SQL lets you run a precheck on your instance before a major version upgrade. This precheck is a long-running operation (LRO) that checks if your instance is ready for an upgrade. It helps find potential problems like incompatibilities, configuration issues, or data problems prior to the upgrade operation.

The precheck either confirms your instance can be upgraded, or lists issues you need to fix first and their solutions. These issues might be due to incompatible extensions, unsupported dependencies, or data format problems. 

Cloud SQL can run the precheck process in parallel with your workload. Running the precheck before you perform a major version upgrade can help prevent an upgrade failure.

When you run the precheck, one of the following happens:

  * **No issues found** : the precheck finished successfully, and no problems were found.
  * **Issues found** : the precheck finished successfully, but it found errors that will block your upgrade. The issues must be resolved prior to the upgrade.
  * **Warnings found** : the precheck finished successfully and found warnings. Review the warnings. We recommend that you address any issues before you proceed with the upgrade.



Depending on the precheck's results, you can either proceed with the upgrade or fix the identified issues before upgrading.

### Limitations

When using the major version upgrade precheck, consider the following limitations:

  * The instance state must be set to `RUNNING`.


  * The instance must be a primary instance. precheck doesn't support replica instances.


  * The instance must not have any blocking operations pending. If a blocking operation is pending, then the precheck results in an error with the following message:
        
        Operation failed because another operation was already in progress. Try
        your request after the current operation is complete.
        

  * The precheck needs to connect to all databases on the instance. If a database is inaccessible, locked, or unresponsive, then the precheck might fail or show errors. We recommend running the precheck when database load is low.




### Before you begin

  * Make sure the Cloud SQL Admin API is enabled for your instance.
  * Confirm you have the `cloudsql.instances.preCheckMajorVersionUpgrade` [IAM permission](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions).



### Perform the precheck

To perform the major version upgrade precheck, do the following:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance you want to perform the precheck on. To open the **Overview** page of the instance, click the instance name.
  3. Click **Edit**.
  4. In the **Instance info** , click **Validate Upgrade**.
  5. In the **Validate upgrade** dialogue, select the database version to upgrade to, and then click **Validate**. 

The precheck operation begins. Monitor the status of the precheck operation in the **Operations** notification drawer.

  6. Once the precheck operation is complete, a new window opens called **Validate upgrade results**. This window contains the findings of the precheck process. The results might be one of the following: 
     * If the precheck operation contains no errors, then click **Upgrade page** to begin the upgrade process.
     * If the precheck operation contains `info` messages, then review the findings. When you're ready to upgrade, click **Upgrade page** to begin the upgrade process.
     * If the precheck contains `warning` messages, then review the findings. We recommend that you resolve these warnings before proceeding with the upgrade, but these messages don't block the upgrade process.
     * If the precheck operation contains `errors`, then review the findings. Resolve the errors then rerun the precheck process. All errors must be resolved before you begin the upgrade process.



### gcloud

  1. Use the [`gcloud sql instances pre-check-major-version-upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/pre-check-major-version-upgrade) to run the precheck:
         
         gcloud  sql instances pre-check-major-version-upgrade INSTANCE_NAME \
           --target-database-version=TARGET_DATABASE_VERSION \
           --project=PROJECT_ID \
           [--async]
            

Replace the following:

     * INSTANCE_NAME: the name of the instance.
     * TARGET_DATABASE_VERSION: the major version you want to upgrade your instance to. To find the database version, see [Plan an upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#plan-upgrade).
     * PROJECT_ID: the ID of your Google Cloud project.

Optional: Use the `--async` flag to run the command asynchronously.

  2. If you use the `--async` flag to run the `pre-check-major-version-upgrade` command asynchronously, then do the following:

     1. Get the precheck operation name: 

Use the [`gcloud sql operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/list) command with the `--instance` flag:
            
            gcloud sql operations list --instance=INSTANCE_NAME

Replace the following:

        * INSTANCE_NAME: the name of the instance.
     2. Monitor the status of the precheck.

Use the [`gcloud sql operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/describe) command:
            
            gcloud sql operations describe OPERATION_NAME

Replace the following:

        * OPERATION_NAME: the precheck operation name retrieved in the previous step.
  3. If you don't run the `pre-check-major-version-upgrade` command asynchronously, then wait for the precheck to complete to view the results.



### REST v1

  1. Run the precheck.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * TARGET_DATABASE_VERSION: The major version to upgrade to. To find a list of available database versions, see [Plan an upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#plan-upgrade).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/preCheckMajorVersionUpgrade

Request JSON body: 
    
    {
      "preCheckMajorVersionUpgradeContext": {
        "targetDatabaseVersion": "TARGET_DATABASE_VERSION"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/preCheckMajorVersionUpgrade"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/preCheckMajorVersionUpgrade" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "message": "Precheck description of finding",
      "message_type": "ERROR",
      "actions_required": [
        "Precheck action required to fix the finding"
      ]
    }
    

  2. Get the precheck operation name.

Use the `GET` request with [`operations.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/operations/list) method after replacing `PROJECT_ID` with the ID of the project.
         
         GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
  3. Monitor the status of the precheck.

Use the `GET` request with [`operations.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/operations/list) method:
         
         GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operation/OPERATION_NAME

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * OPERATION_NAME: the precheck operation name retrieved in the previous step.



### REST v1beta4

  1. Run the precheck.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * TARGET_DATABASE_VERSION: the major version to upgrade to. To find a list of available database versions, see [Plan an upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#plan-upgrade).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/preCheckMajorVersionUpgrade

Request JSON body: 
    
    {
      "preCheckMajorVersionUpgradeContext": {
        "targetDatabaseVersion": "TARGET_DATABASE_VERSION"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/preCheckMajorVersionUpgrade"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/preCheckMajorVersionUpgrade" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "message": "Precheck description of finding",
      "message_type": "ERROR",
      "actions_required": [
        "Precheck action required to fix the finding"
      ]
    }
    

  2. Get the precheck operation name.

Use the `GET` request with [`operations.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations/list) method after replacing `PROJECT_ID` with the ID of the project.
         
         GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
  3. Monitor the status of the precheck.

Use the `GET` request with [`operations.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations/list) method:
         
         GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operation/OPERATION_NAME

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * operation_name: the precheck operation name retrieved in the previous step.



### Review precheck findings

After the precheck finishes, your instance is either ready for upgrade, or it has issues that need your attention.

#### Ready for upgrade

If the precheck finishes successfully and the `preCheckResponse` array is empty, it means no issues or warnings were found. Your instance is ready for the major version upgrade. To continue, see Perform the major version upgrade.

#### Not ready for upgrade

If the precheck ran successfully and the `preCheckResponse` array contains issues, your instance isn't ready for the upgrade and needs attention. The identified issues might or might not block the upgrade. These issues are noted in the `preCheckResponse` with the following message types:

Type | Description | Blocking upgrade?  
---|---|---  
`INFO` | An informational message. | No  
`WARNING` |  A potential issue was found, but it doesn't block the upgrade. Cloud SQL recommends reviewing and addressing the warning before upgrading to ensure full compatibility.  |  No   
`ERROR` | A critical issue that blocks the upgrade was found. These issues might cause the upgrade to fail. You must resolve them before upgrading your instance. | Yes  
If your instance only has `INFO` or `WARNING` messages, you can upgrade it, but you might have issues after the upgrade. We recommend reviewing the message details and resolving the issue before upgrading. If your instance has `ERROR` messages, you must resolve these issues before upgrading. 

Each issue type includes a `message` and an `actions_required` field. Review each issue to understand its type and how to resolve it. For more information about common issues and their solutions, see Common major version upgrade precheck errors.

After you resolve the issues, re-run the precheck to confirm your instance is ready for the upgrade. Then, proceed with upgrading your instance once the precheck is clear.

## Perform the major version upgrade

You can upgrade the major version of a single Cloud SQL instance, or you can upgrade the major version of a primary instance and include all of its replicas in the upgrade, including cascading replicas and cross-region replicas.

### Upgrade the major version of a single instance

When you initiate an upgrade operation for a single instance, Cloud SQL does the following:

  1. Checks the configuration of your instance to ensure that the instance is compatible for an upgrade.
  2. After Cloud SQL verifies the configuration, then Cloud SQL makes the instance unavailable.
  3. Makes a pre-upgrade backup.
  4. Performs the upgrade on the instance.
  5. Makes your instance available.
  6. Makes a post-upgrade backup.

**Note:** If you use read replicas and choose not to include replicas with your major version upgrade, then you must upgrade the read replicas _before_ you upgrade the primary instance. After you upgrade a replica, you can't roll back the database version of the replica. The replicated databases of an upgraded replica are available only after you upgrade the primary instance. 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Instance info** section, click the **Upgrade** button and confirm that you want to go to the upgrade page.
  5. On the **Choose a database version** page, click the **Database version for upgrade** list and select one of the available database major versions.
  6. Click **Continue**.
  7. In the **Instance ID** box, enter the name of the instance and then click the **Start upgrade** button.

The operation takes several minutes to complete. 

Verify that the upgraded database major version appears below the instance name on the instance **Overview** page. 

### gcloud

  1. Start the upgrade. 

Use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command with the `--database-version` flag. 

Before running the command, replace the following: 

     * INSTANCE_NAME: The name of the instance.
     * DATABASE_VERSION: The enum for the database major version, which must be later than the current version. Specify a database version for a major version that is available as an upgrade target for the instance. You can obtain this enum as the first step of Plan for upgrade. If you need a complete list of database version enums, then see [SqlDatabaseEnums](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/SqlDatabaseVersion).
    
    gcloud sql instances patch INSTANCE_NAME \
    --database-version=DATABASE_VERSION

Major version upgrades take several minutes to complete. You might see a message indicating that the operation is taking longer than expected. You can either ignore this message or run the [`gcloud sql operations wait`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/wait) command to dismiss the message. 

  2. Get the upgrade operation name. 

Use the [`gcloud sql operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/list) command with the `--instance` flag. 

Before running the command, replace the following: * INSTANCE_NAME: the name of the instance. 
         
         gcloud sql operations list --instance=INSTANCE_NAME

  3. Monitor the status of the upgrade. 

Use the [`gcloud sql operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/describe) command. 

Before running the command, replace the OPERATION variable with the upgrade operation name retrieved in the previous step. 
         
         gcloud sql operations describe OPERATION




### REST v1

  1. Start the in-place upgrade. 

Use a PATCH request with the [`instances:patch`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/patch) method. 

Before using any of the request data, replace these variables:

     * PROJECT_ID: The ID of the project.
     * INSTANCE_NAME: The name of the instance.

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "databaseVersion": DATABASE_VERSION
    }

Replace DATABASE_VERSION with the enum for the database major version, which must be later than the current version. Specify a database version for a major version that is available as an upgrade target for the instance. You can obtain this enum as the first step of Plan for upgrade. If you need a full list of database version enums, then see [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/SqlDatabaseVersion).

  2. Get the upgrade operation name. 

Use a GET request with the [`operations.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/operations/list) method after replacing PROJECT_ID with the ID of the project. 

HTTP method and URL: 
         
         GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations

  3. Monitor the status of the upgrade. 

Use a GET request with the [`operations.get`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/operations/get) method after replacing the following variables:

     * PROJECT_ID: The ID of the project.
     * OPERATION_NAME: The upgrade operation name retrieved in the previous step.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operation/OPERATION_NAME




### Terraform

To upgrade the major version of the database using Terraform, you must set the `database_version` argument in your [`google_sql_database_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance) definition to the target major version. You must use the Terraform provider for Google Cloud version [4.34.0 or later](https://github.com/hashicorp/terraform-provider-google/releases).

The following examples demonstrate a basic `google_sql_database_instance` configuration. To upgrade the major version, set the `database_version` argument to the relevant major version.
    
    
    resource "google_sql_database_instance" "default" {
      name             = "postgres-instance"
      region           = "us-central1"
      database_version = "POSTGRES_14"
      settings {
        tier = "db-custom-2-7680"
      }
    }

Make the following changes to the Terraform arguments:

  * `database_version`: Set this to the target major version for the upgrade.
  * `deletion_protection`: Defines the root-level Terraform safeguard against instance deletion. 
    * `true`: Prevents Terraform from destroying the instance. Any Terraform operation that plans to delete this resource is blocked.
    * `false`: Allows Terraform to delete the instance.

**Note:** This is different from [GCP-level deletion protection](https://docs.cloud.google.com/sql/docs/postgres/deletion-protection#new-instance) (`settings.deletion_protection_enabled`).

#### Review the Terraform Plan

Before applying any changes, always run `terraform plan` and carefully inspect the output. The symbols next to the resource name indicate how Terraform will apply the changes:

  * `~` Update in-place: This symbol indicates Terraform will modify the existing instance. This is the expected and safe outcome for an in-place major version upgrade when changing `database_version`.
  * `+/-` Recreate (Force Replacement): This symbol means Terraform plans to destroy the current instance and create a new one. **Warning:** If `+/-` appears next to your `google_sql_database_instance` resource after changing `database_version`, don't proceed with `terraform apply`. This will delete your instance and all of its data.
    * If `deletion_protection` is set to `true`, Terraform will error out and block this dangerous replacement. You would need to explicitly set `deletion_protection = false` in your configuration and run `terraform apply` again to update the state, before a subsequent `apply` would allow the destroy and recreate.
    * If `deletion_protection` is set to `false`, `terraform apply` would proceed with the data loss.

Instances can be scheduled for replacement (deletion and recreation) due to a configuration change or an unsupported upgrade path for in-place modification. If you find an instance is scheduled to be deleted and recreated, you should immediately stop and investigate the reason behind the scheduled replacement before it proceeds.




After you review the `terraform plan` output to ensure that it only indicates an in-place update (`~`) for the database version change, apply the configuration

To apply your Terraform configuration in a Google Cloud project, complete the steps in the following sections.

## Prepare Cloud Shell

  1. Launch [Cloud Shell](https://shell.cloud.google.com/).
  2. Set the default Google Cloud project where you want to apply your Terraform configurations. 

You only need to run this command once per project, and you can run it in any directory.
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.




## Prepare the directory

Each Terraform configuration file must have its own directory (also called a _root module_).

  1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must have the `.tf` extension—for example `main.tf`. In this tutorial, the file is referred to as `main.tf`. 
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

  2. If you are following a tutorial, you can copy the sample code in each section or step.

Copy the sample code into the newly created `main.tf`.

Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 

  3. Review and modify the sample parameters to apply to your environment.
  4. Save your changes.
  5. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option: 
         
         terraform init -upgrade




## Apply the changes

  1. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.

  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the "Apply complete!" message.

  3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them. 

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

When you place an in-place upgrade request, Cloud SQL first performs a pre-upgrade check. If Cloud SQL determines that your instance isn't ready for an upgrade, then your upgrade request fails with a message suggesting how you can address the issue. See also Troubleshoot a major version upgrade.

**Note:** Cloud SQL automatically provisions your instance on the default minor version.

### Include replicas in the major version upgrade

If your primary instance has replicas, then you can include all replicas in the upgrade. Cloud SQL can upgrade all replicas of the primary instance, including cross-region replicas and cascading replicas.

When you include replicas in a major version upgrade, Cloud SQL does the following:

  1. Checks the configuration of your primary instance and replicas to ensure that the instance and replicas are compatible for an upgrade.
  2. Makes your primary instance unavailable.
  3. Makes a pre-upgrade backup of the primary instance.
  4. Stops replication for all replicas.
  5. Performs the upgrade on the primary instance.
  6. If the upgrade on the primary instance is successful, then the primary instance becomes available again and restarts replication.
  7. Cloud SQL takes a post-upgrade backup of the primary instance.
  8. Cloud SQL proceeds to upgrade all replicas.



Even if the major version upgrade of a replica fails, the primary instance continues to be available.

To include replicas in a major version upgrade, you can't use the Google Cloud console or Terraform. You can only use [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API.

### gcloud

  1. Start the upgrade. 

Use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command with the `--database-version` and the `--include-replicas-for-major-version-upgrade` flags.

Before running the command, replace the following: 

     * INSTANCE_NAME: the name of the primary instance.
     * DATABASE_VERSION: the enum for the database major version, which must be later than the current version. Specify a database version for a major version that is available as an upgrade target for the instance. You can obtain this enum as the first step of Plan for upgrade. If you need a complete list of database version enums, then see [SqlDatabaseEnums](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/SqlDatabaseVersion).
    
    gcloud sql instances patch INSTANCE_NAME \
      --database-version=DATABASE_VERSION \
      --include-replicas-for-major-version-upgrade

Major version upgrades take several minutes to complete. You might see a message indicating that the operation is taking longer than expected. You can either ignore this message or run the [`gcloud sql operations wait`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/wait) command to dismiss the message. Upgrading replicas can take several minutes to complete. To check the status of the upgrade, do the following: 

  2. Get the upgrade operation name. 

Use the [`gcloud sql operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/list) command with the `--instance` flag. 

Before running the command, replace the INSTANCE_NAME variable with the name of the instance. 
         
         gcloud sql operations list --instance=INSTANCE_NAME

  3. Monitor the status of the upgrade. 

Use the [`gcloud sql operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/describe) command. 

Before running the command, replace the OPERATION variable with the upgrade operation name retrieved in the previous step. 
         
         gcloud sql operations describe OPERATION




### REST

  1. Start the in-place upgrade. 

Use a PATCH request with the [`instances:patch`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/patch) method. 

Before using any of the request data, replace these variables:

     * PROJECT_ID: the ID of the project.
     * INSTANCE_NAME: the name of the instance.

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "databaseVersion": DATABASE_VERSION
      "includeReplicasForMajorVersionUpgrade": true
    }

     * Replace DATABASE_VERSION with the enum for the database major version, which must be later than the current version. Specify a database version for a major version that is available as an upgrade target for the instance. You can obtain this enum as the first step of Plan for upgrade. If you need a full list of database version enums, then see [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/SqlDatabaseVersion).
     * In the `includeReplicasForMajorVersionUpgrade` field, specify `true`.
  2. Get the upgrade operation name. 

Use a GET request with the [`operations.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/operations/list) method after replacing PROJECT_ID with the ID of the project. 

HTTP method and URL: 
         
         GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations

  3. Monitor the status of the upgrade. 

Use a GET request with the [`operations.get`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/operations/get) method after replacing the following variables:

     * PROJECT_ID: the ID of the project.
     * OPERATION_NAME: the upgrade operation name retrieved in the previous step.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operation/OPERATION_NAME




### Automatic upgrade backups

When you perform a major version upgrade, Cloud SQL automatically makes two on-demand backups, called upgrade backups:

  * The first upgrade backup is the _pre-upgrade backup_ , which is made immediately before starting the upgrade. You can use this backup to restore your database instance to its state on the previous version.
  * The second upgrade backup is the _post-upgrade backup_ , which is made immediately after new writes are allowed to the upgraded database instance.



When you [view your list of backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backing-up#viewbackups), the upgrade backups are listed with type `On-demand`. Upgrade backups are labeled so that you can identify them quickly. For example, if you're upgrading from PostgreSQL 14 to PostgreSQL 15, your pre-upgrade backup is labeled `Pre-upgrade backup, POSTGRES_14 to POSTGRES_15.` and your post-upgrade backup is labeled `Post-upgrade backup, POSTGRES_14 to POSTGRES_15.`

As with other on-demand backups, upgrade backups persist until you delete them or delete the instance. If you have PITR enabled, you can't delete your upgrade backups while they're in your retention window. If you need to delete your upgrade backups, you must disable PITR or wait until your upgrade backups are no longer in your retention window.

## Cancel the major version upgrade

You can cancel an in-place major version upgrade operation, but only while the instance is performing the actual version upgrade.

**Note:** If you use read replicas and choose to include replicas with your major version upgrade, you can't cancel the major version upgrade.

### Cancellation window

A major version upgrade involves a sequence of steps. You can only cancel during the main upgrade phase.

  1. Initialization: Cloud SQL prepares the instance and its resources. You can't cancel during this phase.

  2. Main upgrade phase: Cloud SQL actively upgrades your data to the new major version. You can only cancel during this phase.

  3. Finalization: the instance completes the upgrade and performs final verifications.




To determine when your instance has entered the cancellable phase, check for the availability of upgrade logs. Upgrade logs are available at `projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fpostgres-upgrade.log`

When log entries begin to appear in this log file, the main upgrade phase is active, and you can cancel the operation.

### Perform cancellation

To cancel an in-place major version upgrade, you need the ID of the operation. You must specify this ID in the `gcloud` or REST API command so that Cloud SQL knows which operation to cancel.

You can use the `gcloud` or REST API commands to cancel a major version upgrade operation.

###  gcloud 

  1. Get the upgrade operation ID.

Use the [`gcloud sql operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/list) command with the `--instance` flag:
         
         gcloud sql operations list --instance=INSTANCE_NAME
         

Replace the following:

     * INSTANCE_NAME: the name of the instance.
  2. Cancel the upgrade.

Use the [`gcloud sql operations cancel`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/cancel) command:
         
         gcloud sql operations cancel OPERATION_ID
         

Replace the following:

     * OPERATION_ID: the operation ID retrieved in the previous step.
  3. Check the cancelled status.

Use the [`gcloud sql operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/describe) command:
         
         gcloud sql operations describe OPERATION_ID
         

Replace the following:

     * OPERATION_ID: the operation ID retrieved in the first step.



###  REST v1 

  1. Get the upgrade operation ID.

Use the GET request with [`operations.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/operations/list) method after replacing `PROJECT_ID` with the ID of the project.
         
         GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
  2. Cancel the upgrade.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project.
     * OPERATION_ID: the operation ID retrieved in the previous step.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID/cancel

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID/cancel"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID/cancel" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {}
    

This REST API call doesn't return any response.

  3. Check the cancelled status.

Use the GET request with [`operations.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/operations/list) method:
         
         GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * OPERATION_ID: the operation ID retrieved in the first step.



###  REST v1beta4 

  1. Get the upgrade operation ID.

Use the GET request with [`operations.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations/list) method after replacing `PROJECT_ID` with the ID of the project.
         
         GET https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
  2. Cancel the upgrade.




Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project.
  * OPERATION_ID: the operation ID retrieved in the previous step.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID/cancel

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID/cancel"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID/cancel" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {}
    

This REST API call doesn't return any response.

  1. Check the cancelled status.

Use the GET request with [`operations.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations/list) method:
         
         GET https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * OPERATION_ID: the operation ID retrieved in the first step.



If your cancellation request is accepted, then Cloud SQL stops the ongoing upgrade process and begins reverting your instance to its original state.

**Note:** Cancellation isn't instantaneous. Triggering a cancellation doesn't immediately restore access to your instance. The instance remains unavailable while Cloud SQL performs the necessary rollback steps to return the system to its pre-upgrade state.

### Troubleshoot cancellation

Issue | Troubleshooting  
---|---  
Error message: `The operation OPERATION_ID cannot be canceled at the moment. Please retry in approximately 5-10 minutes` | The upgrade has not yet reached the cancellable window. Wait a few minutes and try cancelling again.  
Error message: `The operation OPERATION_ID cannot be cancelled as it has passed the cancellable state. The operation is in its final stage and should complete soon.` | The upgrade process has crossed the cancellable window. Cancellation is no longer possible, and the upgrade should finish shortly.  
Error message: `You can't cancel operation OPERATION_ID because it isn't in progress.` | The operation has already finished, either successfully or with a failure, and can no longer be canceled.  
Error messages:

  * `You can't cancel operation OPERATION_ID because Cloud SQL doesn't support the cancellation of this OPERATION_TYPE operation.`
  * `The operation OPERATION_ID cannot be cancelled.`

| This error usually occurs when you pass the wrong OPERATION_ID to the cancel command—specifically, the ID of an operation type that doesn't support cancellation. Verify that you're using the OPERATION_ID associated with the in-place database major version upgrade you want to cancel.  
  
If the cancellation failed after the cancel request was accepted, you should restore your instance from the pre-upgrade backup automatically taken at the start of the process. If issues persist, contact [Google Cloud support](https://docs.cloud.google.com/sql/docs/postgres/getting-support).

## Complete the major version upgrade

After you finish upgrading your primary instance, perform the following steps to complete your upgrade:

  1. Refresh the database statistics. 

Run `ANALYZE` on your primary instance to update the system statistics after the upgrade. Accurate statistics make sure that the PostgreSQL query planner processes queries optimally. Missing statistics can lead to bad query plans, which in turn might degrade performance and take up excessive memory. 

  2. Perform acceptance tests. 

Run tests to make sure that the upgraded system performs as expected. 

  3. To avoid disruption of replication streams, recreate your instance's logical replication slots using the information that you recorded before starting the upgrade (see Prepare for a major version upgrade). 



## Troubleshoot a major version upgrade

Cloud SQL returns an error message if you attempt an invalid upgrade command, for example, if your instance contains invalid database flags for the new version.

If your upgrade request fails, check the syntax of your upgrade request. If the request has a valid structure, try looking into the following suggestions.

### View error logs

If any issues occur with a valid upgrade request, then Cloud SQL publishes error logs to `projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fpostgres-upgrade.log`. Each log entry contains a label with the instance identifier to help you identify the instance with the upgrade error. Look for such upgrade errors and resolve them.

To view error logs, use the Google Cloud console::

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Operations and logs** pane of the instance **Overview** page, click the **View PostgreSQL error logs** link.

The [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface) page opens.

  4. View logs as follows:

     * To list all error logs in a project, select the log name in the **Log name** log filter.

For more information on query filters, see [Advanced queries](https://docs.cloud.google.com/logging/docs/view/advanced-queries).

     * To filter the upgrade error logs for a single instance, enter the following query in the **Search all fields** box, after replacing `DATABASE_ID`

with the project ID followed by the instance name in this format: `project_id:instance_name`.
    
    resource.type="cloudsql_database"
    resource.labels.database_id="DATABASE_ID"
    logName : "projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fpostgres-upgrade.log"

For example, to filter the upgrade error logs by an instance named `shopping-db` running in the project `buylots`, use the following query filter:
    
    resource.type="cloudsql_database"
     resource.labels.database_id="buylots:shopping-db"
     logName : "projects/buylots/logs/cloudsql.googleapis.com%2Fpostgres-upgrade.log"

You can either review all logs reported within a given timeframe, or you can filter logs by severity. A common option for troubleshooting might include selecting the following filters:

     * Emergency
     * Alert
     * Critical
     * Error



Log entries with the `pg_upgrade_dump` prefix indicate that an upgrade error had occurred. For example:
    
    
    pg_upgrade_dump: error: query failed: ERROR: out of shared memory
    HINT: You might need to increase max_locks_per_transaction.
    

Additionally, log entries labeled with a `.txt` secondary filename might list other errors that you might want to resolve before attempting the upgrade again.

All filenames are found in the `postgres-upgrade.log` file. To locate a filename, look at the `labels.FILE_NAME` field.

Filenames that might contain errors to resolve include:

  * `tables_with_oids.txt:` This file contains tables that are listed with object identifiers (OIDs). Either delete the tables or modify them so that they don't use OIDs.
  * `tables_using_composite.txt:` This file contains tables that are listed using system-defined composite types. Either delete the tables or modify them so that they don't use these composite types.
  * `tables_using_unknown.txt:` This file contains tables that are listed using the `UNKNOWN` data type. Either delete the tables or modify them so that they don't use this data type.
  * `tables_using_sql_identifier.txt:` This file contains tables that are listed using the `SQL_IDENTIFIER` data type. Either delete the tables or modify them so that they don't use this data type.
  * `tables_using_reg.txt:` This file contains tables that are listed using the `REG*` data type (for example, `REGCOLLATION` or `REGNAMESPACE`). Either delete the tables or modify them so that they don't use this data type.
  * `postfix_ops.txt:` This file contains tables that are listed using postfix (right-unary) operators. Either delete the tables or modify them so that they don't use these operators.



### Check the memory

If the instance has insufficient shared memory, you might see this error message: `ERROR: out of shared memory.` This error is more likely to occur if you have in excess of 10,000 tables.

Before you attempt an upgrade, set the value of the [`max_locks_per_transaction`](https://www.postgresql.org/docs/current/static/runtime-config-locks.html#GUC-MAX-LOCKS-PER-TRANSACTION) flag to approximately twice the number of tables in the instance. The instance is restarted when you change the value of this flag.

### Check the connections capacity

If your instance has insufficient connection capacity, you might see this error message: `ERROR: Insufficient connections.`

Cloud SQL recommends that you increase the [`max_connections`](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-MAX-CONNECTIONS) flag value by the number of databases in your instance. The instance is restarted when you change the value of this flag.

### Check for an ambiguous column reference

Cloud SQL automatically performs a pre-upgrade check to identify user-defined views that depend on system catalog views, such as `pg_stat_activity` or `pg_stat_replication`. The column structure of these system catalog views can change between major PostgreSQL versions. If you have views that `select *` or rely on the column order of these system views, then they might become incompatible after an upgrade, resulting in an error, such as `ERROR: column reference "column_name" is ambiguous`.

The pre-upgrade check detects such views by checking for dependencies. If incompatible views are found, the upgrade process is stopped and an error message is displayed. This message lists the incompatible views in each database that need to be addressed.

**Example Error Message**

  * For `pg_stat_activity` related issues: 
        
        Please remove the following usages of views that depend on functions returning
        data types of pg_stat_activity before attempting an upgrade:
        (database: my_db, schema name: public, view name: my_stat_activity_view)

  * For `pg_stat_replication` related issues:
        
        Please remove the following usages of views that depend on functions returning
        data types of pg_stat_replication before attempting an upgrade:
        (database: my_db, schema name: public, view name: my_replication_stats_view)




To resolve such issues and proceed with the upgrade: 1\. Identify the views listed in the pre-upgrade check error message.

  1. Drop these views using `DROP VIEW view_name;`.

  2. Retry the major version upgrade.

  3. Once the upgrade is complete, recreate the views. Ensure the new view definitions are compatible with the schema of the system catalog views in the current PostgreSQL version. You might need to explicitly list columns instead of using `select *` to avoid future issues.




For a more-detailed example of the problem and further insights, see this [stack overflow discussion](https://stackoverflow.com/questions/77378569/column-is-ambiguous)

### Check for SRFs in CASE statements

If you're upgrading your instance from PostgreSQL 9.6 and using set returning functions in your CASE statements, then you might see this error message `ERROR: set-returning functions are not allowed in CASE`. This issue occurs as from version 10 onwards using set-returning functions in CASE statements is disallowed.

To resolve this issue and upgrade your instance successfully, ensure that any CASE statements utilizing set-returning functions are modified to avoid their use before retrying the upgrade. Some commonly used SRFs include the following: 

  * unnest()
  * generate_series()
  * array_agg()
  * regexp_split_to_table()
  * jsonb_array_elements()
  * json_array_elements()
  * sonb_each()
  * json_each()



### Check views created on custom casts

If you have a view created on a custom cast, then an error message similar to the following appears: `ERROR: cannot cast type <type_1> to <type_2>`. This issue occurs because of permission issues on custom created casts.

To resolve this issue, update your instance to `[PostgreSQL version].R20240910.01_02`

For more information, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance).

### Check event trigger ownership

In Cloud SQL, all event triggers must be owned by a user with the `cloudsqlsuperuser` role. Cloud SQL performs a pre-upgrade check to validate ownership of all event triggers. If an event trigger is owned by a user who lacks the `cloudsqlsuperuser` role, then the upgrade process is halted and you might get an error message, such as:
    
    
    Please ensure that the owners of all event triggers have the cloudsqlsuperuser
    role assigned to them before attempting an upgrade:
    (database: your_db, triggerName your_trigger, owner: non_super_user)

To resolve this issue, either change the owner of the event trigger to a user that has the `cloudsqlsuperuser` role, such as `postgres`, or grant the `cloudsqlsuperuser` role to the current owner.

To identify event triggers with owners lacking the required role, run the following command:
    
    
    SELECT
      t.evtname AS trigger_name,
      r.rolname AS current_owner
    FROM pg_event_trigger t
    JOIN pg_roles r ON t.evtowner = r.oid
    WHERE NOT pg_has_role(r.rolname, 'cloudsqlsuperuser', 'member');

The results show any event trigger with an owner who doesn't have the `cloudsqlsuperuser` role.

### Check generated columns from unlogged tables

If you have an unlogged table which has generated columns you might see the error message `ERROR: unexpected request for new relfilenumber in binary upgrade mode`. This issue occurs due to discrepancies in the persistence characteristics between tables and their sequences for generated columns.

To address this issue, do the following:

  1. Drop unlogged tables: if possible, drop any unlogged tables that are linked to generated columns. Make sure that data loss can be safely mitigated before proceeding.
  2. Convert to permanent tables: temporarily, convert unlogged tables to permanent tables using the following steps: 
     1. Convert the table to a logged table `ALTER TABLE  SET LOGGED;`
     2. Perform major version upgrade
     3. Convert the table back to an unlogged table `ALTER TABLE  SET UNLOGGED`



You can identify all such tables by using the following query :
    
    
    SELECT
      relnamespace::regnamespace,
      c.relname AS table_name,
      a.attname AS column_name,
      a.attidentity AS identity_type
    FROM
      pg_catalog.pg_class c
      JOIN pg_catalog.pg_attribute a ON a.attrelid = c.oid
    WHERE
      a.attidentity IN ('a', 'd') AND c.relkind = 'r' AND c.relpersistence = 'u'
    ORDER BY c.relname, a.attname;

### Check the custom flags for your PostgreSQL instance

If you're upgrading to a PostgreSQL instance, version 14 or higher, then check the names of any custom [database flags that you configured](https://docs.cloud.google.com/sql/docs/postgres/flags) for the instance. This is because PostgreSQL [placed additional restrictions on allowed names for custom parameters](https://github.com/postgres/postgres/blob/master/src/backend/utils/misc/guc.c).

The first character of a custom database flag must be alphabetic (A-Z or a-z). All subsequent characters can be alphanumeric, the underscore (_) special character, or the dollar sign ($) special character.

### Remove extensions

If you're upgrading your Cloud SQL instance, then you might see this error message: `pg_restore: error: could not execute query: ERROR: role "16447" does not exist`.

To resolve this issue, follow these steps:

  1. Remove the [`pg_stat_statements`](https://www.postgresql.org/docs/current/pgstatstatements.html) and [`pgstattuple`](https://www.postgresql.org/docs/current/pgstattuple.html) extensions.
  2. Perform the upgrade.
  3. Reinstall the extensions.



### MVU operation running for a longer duration

There are two underlying tasks associated with a major version upgrade:

  * **Precheck operation** : Returns a timeout error if not finished within three hours.
  * **Upgrade operation** : Returns a timeout error if not finished within six hours.



If the instance has an ongoing `MAJOR_VERSION_UPGRADE` operation for a length of time longer than expected, then [investigate the PostgreSQL error logs](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#view-error-logs). This might be caused by common issues such as:

  * A large number of tables, views, or indexes
  * Insufficient resources such as CPU or memory
  * Major transactions blocking the shutdown of databases for the upgrade process to begin. You can use the Google Cloud console to check current processes.



## Common major version upgrade precheck errors

Issues found by the [major version upgrade precheck](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#precheck) fall into these categories:

  * Incompatible extensions: These are Cloud SQL for PostgreSQL extensions on your instance that don't work with the new major version.

  * Unsupported dependencies: These are dependencies that either aren't supported by the new major version or need updates to work with it.

  * Database incompatibilities: These are problems with your database or data that might happen after a major version upgrade. This includes differences in database structures, data types, encoding, collation, or system catalog changes specific to the new version.




### Incompatible extensions

The following table lists common errors related to incompatible extensions that the major version upgrade precheck might find:

Type | Error example | Resolution  
---|---|---  
Unsupported or deprecated extension | `Your installation contains unsupported extensions for the new version. These extensions must be removed before attempting an upgrade: (database: %s, Extension name: %s)` | Remove the extension from all databases that use it with `DROP EXTENSION $extension_name;`.  
Incompatible extension version | `Your installation contains incompatible version extensions. These extensions must be upgraded to a compatible version before attempting an upgrade: (database: %s, Extension name: %s)` | Update the extension to a version that works with your target Cloud SQL for PostgreSQL version. For compatible versions, see [Configure Cloud SQL for PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).  
`PostGIS` unpackaged files | `PostGIS version upgrade has not been completed, unpackaged raster files present. Follow the steps at https://postgis.net/documentation/tips/tip-removing-raster-from-2-3/ to fix before major version upgrade.` | Clean up the unpackaged raster files.  
`PostGIS` deprecated functions | `PostGIS version upgrade has not been completed, deprecated functions present. Please drop all objects using deprecated functions and upgrade to a different version of PostGIS before major version upgrade.` | Find and remove or change any database objects that use deprecated `PostGIS` functions before upgrading the `PostGIS` extension.  
Extension ownership | `Please ensure that the owner of the postgres_fdw extension has the cloudsqlsuperuser role assigned to them before attempting an upgrade: (database: my_db, extension name: postgres_fdw, owner: some_user)` | Change the extension owner using `ALTER EXTENSION postgres_fdw OWNER TO postgres;`.  
  
### Unsupported dependencies

The following table lists common errors related to unsupported dependencies that the major version upgrade precheck might find:

Type | Error example | Resolution  
---|---|---  
Event trigger ownership | `Please ensure that the owners of all event triggers have the cloudsqlsuperuser role assigned to them before attempting an upgrade: (database: your_db, triggerName your_trigger, owner: non_super_user)` | Connect to the identified database using `psql` or Cloud SQL Studio and change the trigger's owner to a `postgres` user.  
Uncommitted prepared statements | `Please commit/rollback the following usages of 'Uncommitted Prepared Statements'... (database: my_db, gid: my_prepared_xact)` | Either commit or roll back the prepared statement.  
Deprecated flags | ` Your installation contains deprecated flags for the new version . These flags must be removed before attempting an upgrade: (database: %s, Flag name: %s)` | [Remove the database flag](https://docs.cloud.google.com/sql/docs/postgres/flags#config) from the instance configuration.  
  
### Database incompatibilities

The following table lists common errors related to data format incompatibilities that the major version upgrade precheck might find:

Type | Error example | Resolution  
---|---|---  
Unknown data type | `Please remove the following usages of 'Unknown' data types before attempting an upgrade: (database: my_db, relation: my_table, attribute: my_column)` | Remove the column or table, or change the table's data type using `ALTER TABLE my_table ALTER COLUMN my_column TYPE TEXT;`.  
`reg*` data type | `Please remove the following usages of 'reg*' data types before attempting an upgrade: (database: my_db, relation: my_table, attribute: my_column)` | Remove the column or change its data type.  
Removed data type | `Please remove the following usages of 'sql_identifier' data types before attempting an upgrade: ...` | Convert to `TEXT`, `timestamptz`, or another suitable data type.  
`​​aclitem` Internal Format | `Please remove the following usages of 'aclitem' data types before attempting an upgrade: ...` | Stop using `aclitem` in your database table definitions.  
System-defined composite data types | `Please remove the following usages of 'composite' data types before attempting an upgrade: (database: my_db, relation: my_table, attribute: my_column)` | Change the identified columns to use a user-defined composite type or a standard data type. System composite types may not be consistent across major versions.  
Tables with `OIDS` | `Please remove the following usages of tables with OIDs before attempting an upgrade: (database: my_db, relation: my_table)` | Update the table using ` ALTER TABLE my_table SET WITHOUT OIDS;`.  
User-defined `postfix` operators | `Please remove the following usages of 'postfix operators' before attempting an upgrade: (database: my_db, operation id: 12345, operation namespace: public, operation name: !!, type namespace: public, type name: mytype)` | Remove the custom `postfix` operators. You might need to rewrite your code to use prefix operators or function calls instead.  
Incompatible polymorphic functions | `Please remove the following usages of 'incompatible polymorphic' functions before attempting an upgrade: (database: my_db, object kind: function, object name: public.my_poly_func)` | Remove or change the function to remove incompatible polymorphic functions. This might mean adjusting function signatures or logic to work with Cloud SQL for PostgreSQL 14 and later.  
User-defined encoding conversions | `Please remove the following usages of user-defined encoding conversions before attempting an upgrade: (database: my_db, namespace name: public, encoding conversions name: my_encoding_conv)` | Remove the user-defined encoding conversion. You might need to recreate it after the upgrade with a signature that works with the new version.  
Check for an ambiguous column reference | Cloud SQL automatically checks for user-defined views that rely on system catalog views. The column structure of these system catalog views might change between major versions.  
  
`Please remove the following usages of views that depend on functions returning data types of pg_stat_activity before attempting an upgrade: (database: my_db, schema name: public, view name: my_stat_activity_view) ` | Find the views listed in the error message and remove them using the `DROP VIEW` command. After the upgrade, recreate the views.  
Unlogged tables with generated columns or logged sequences | `Please drop the following usages of 'Unlogged Tables with Logged Sequence' before attempting an upgrade: (database: your_db, table name: problematic_table)` | You can either convert the table to `LOGGED`, or remove it using the `DROP TABLE` command. Recreate the table after the upgrade.  
Fix the empty search path issue | `Please update the search path of the 'll_to_earth' function (database: your_db, search path: )` | The `earthdistance` extension uses `earth` and `cube types` without specifying the function's search path. Update the search path using `ALTER FUNCTION ll_to_earth SET search_path = public;`.  
  
## Restore the primary instance to the previous major version

If your upgraded database system doesn't perform as expected, then you might need to restore your primary instance to the previous version. You do so by restoring your pre-upgrade backup to a Cloud SQL recovery instance, which is a new instance running the pre-upgrade version.

To restore a primary instance to the previous version, perform the following steps:

  1. Identify your pre-upgrade backup.

See Automatic upgrade backups.

  2. Create a recovery instance.

[Create a new Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance) using the major version that Cloud SQL was running when the pre-upgrade backup was made. Set the same [flags](https://docs.cloud.google.com/sql/docs/postgres/flags) and [instance settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings) that the original instance uses.

  3. Restore your pre-upgrade backup.

[Restore](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring#restorebackups-another-instance) your pre-upgrade backup to the recovery instance. This might take several minutes to complete.

  4. Add your read replicas.

If you're using read replicas, then add the read replicas individually.

  5. Connect your application.

Having recovered your database system, update your application with details about the recovery instance and its read replicas. You can resume serving traffic on the pre-upgrade version of your database.




## FAQs

The following questions might come up when upgrading the database major version. 

Is my instance unavailable during an upgrade?
    Yes. Your instance remains unavailable for a period of time while Cloud SQL performs the upgrade. 

How long does an upgrade take? 
    

Upgrading a single instance typically takes less than 10 minutes. If your instance configuration has a small number of vCPUs or memory, then your upgrade might take more time.

If your instance hosts too many databases or tables, or your databases are very large, then the upgrade might take hours or even time out because the total upgrade time corresponds to the number of objects in your databases. If you have multiple instances that need to be upgraded, then your upgrade time increases proportionately. If you include replicas in your upgrade, then the upgrade operation can take up to an hour to complete, depending on the number of replicas that your primary instance has. 

Can I monitor each step in my upgrade process?
    While Cloud SQL lets you monitor whether an upgrade operation is still in progress, you can't track the individual steps in each upgrade. 

Can I cancel my upgrade after I've started it? 
    Yes, but only under specific conditions. You can cancel the operation during the main upgrade phase. See cancel the major version upgrade for details on how to identify the cancellable window. Additionally, cancellation is **not supported** if you include read replicas with the primary instance. To retain the ability to cancel, you must upgrade without including read replicas. 

What happens to my settings during an upgrade?
    

When you perform an in-place major version upgrade, Cloud SQL retains your database settings, including your instance name, IP address, explicitly configured flag values, and user data. However, the default value of the system variables might change. For example, the default value of the `password_encryption` flag in PostgreSQL 13 and earlier is `md5`. When you upgrade to PostgreSQL 14, the default value of this flag changes to `scram-sha-256`.

To learn more, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags). If a certain flag or value is no longer supported in your target version, then Cloud SQL automatically removes the flag during the upgrade, provided the flag hasn't been set by you. If you have configured a flag that isn't supported in the target version, then you must remove the flag before you upgrade.

## What's next

  * Learn about [options for connecting to an instance](https://docs.cloud.google.com/sql/docs/postgres/external-connection-methods).
  * Learn about [importing and exporting data](https://docs.cloud.google.com/sql/docs/postgres/import-export).
  * Learn more about [setting database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
