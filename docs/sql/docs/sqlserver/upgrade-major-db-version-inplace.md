---
url: https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-inplace/
title: Upgrade the database major version in-place \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:45.394421+00:00
---

# Upgrade the database major version in-place  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-inplace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Upgrade the database major version in-place Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to upgrade the database major version by upgrading your Cloud SQL instance in-place rather than [by migrating data](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-migrate).

## Introduction

Database software providers periodically release new major versions that contain new features, performance improvements, and security enhancements. Cloud SQL takes in [new versions](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions) after they're released. After Cloud SQL offers support for a new major version, you can upgrade your instances to keep your database updated.

You can upgrade the database version of an instance in-place or by [migrating data](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-migrate). In-place upgrades are a simpler way to upgrade your instance's major version. You don't need to migrate data or change application connection strings. With in-place upgrades, you can retain the name, IP address, and other settings of your current instance after the upgrade. In-place upgrades don't require you to move data files and can be completed faster. In some cases, the downtime is shorter than what migrating your data entails.

The Cloud SQL for SQL Server in-place upgrade operation uses the [SQL Server upgrade in-place utility](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/choose-a-database-engine-upgrade-method?view=sql-server-ver15#upgrade-in-place). 

## Plan a major version upgrade

  1. Confirm that you have the required role to perform a major version upgrade: [Cloud SQL Owner](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles) or [Cloud SQL Admin](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles).
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

To check which target database versions are available for a major version in-place upgrade, use the [`instances.get`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/get) method of the Cloud SQL Admin API.

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
      major_version: "SQLSERVER_2025_STANDARD"
      name: "SQLSERVER_2025_STANDARD"
      display_name: "SQL Server 2025 Standard"
    }
    
    

### REST v1beta4 

To check which target database versions are available for major version in-place upgrade of an instance, use the [`instances.get`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/get) method of the Cloud SQL Admin API.

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
      major_version: "SQLSERVER_2025_STANDARD"
      name: "SQLSERVER_2025_STANDARD"
      display_name: "SQL Server 2025 Standard"
    }
    
    

For the complete list of the database versions that Cloud SQL supports, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions).

  3. Consider the features offered in each database major version and address incompatibilities.

See SQL Server [discontinued features](https://learn.microsoft.com/en-us/sql/database-engine/discontinued-database-engine-functionality-in-sql-server?view=sql-server-ver16#discontinued-features-in-) and [breaking changes](https://docs.microsoft.com/en-us/sql/database-engine/breaking-changes-to-database-engine-features-in-sql-server-version-15?view=sql-server-ver15).

New major versions introduce incompatible changes that might require you to modify the application code, the schema, or the database settings. Before you can upgrade your database instance, review the release notes of your target major version to determine the incompatibilities that you must address.

**Note:** While upgrading your major version, you can also upgrade your SQL Server edition. For example, you can upgrade from SQL Server 2017 Standard to SQL Server 2019 Enterprise, SQL Server 2022 Enterprise, or SQL Server 2025 Enterprise. If you decide to upgrade your edition, be sure to review Cloud SQL for SQL Server [license pricing](https://cloud.google.com/sql/pricing#sql-licensing).

  4. Test the upgrade with a dry run.

Perform a dry run of the end-to-end upgrade process in a test environment before you upgrade the production database. You can [clone your instance](https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance) to create an identical copy of the data on which to test the upgrade process.

In addition to validating that the upgrade completes successfully, run tests to ensure that the application behaves as expected on the upgraded database.

**Note:** Ensure that you have enough disk space before running a major version upgrade. If you haven't enabled [automatic storage increases](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen), then take note of the disk storage used by the upgraded dry run instance. This helps you determine whether you need to increase the storage capacity for the production instance before upgrading.
  5. Decide on a time to upgrade.

Upgrading requires the instance to become unavailable for a period of time. Plan to upgrade during a time period when database activity is low.




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
     * DATABASE_VERSION: The enum for the database major version, which must be later than the current version. Specify a database version for a major version that is available as an upgrade target for the instance. You can obtain this enum as the first step of Plan for upgrade. If you need a complete list of database version enums, then see [SqlDatabaseEnums](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/SqlDatabaseVersion).
    
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

Use a PATCH request with the [`instances:patch`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/patch) method. 

Before using any of the request data, replace these variables:

     * PROJECT_ID: The ID of the project.
     * INSTANCE_NAME: The name of the instance.

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "databaseVersion": DATABASE_VERSION
    }

Replace DATABASE_VERSION with the enum for the database major version, which must be later than the current version. Specify a database version for a major version that is available as an upgrade target for the instance. You can obtain this enum as the first step of Plan for upgrade. If you need a full list of database version enums, then see [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/SqlDatabaseVersion).

  2. Get the upgrade operation name. 

Use a GET request with the [`operations.list`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/operations/list) method after replacing PROJECT_ID with the ID of the project. 

HTTP method and URL: 
         
         GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations

  3. Monitor the status of the upgrade. 

Use a GET request with the [`operations.get`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/operations/get) method after replacing the following variables:

     * PROJECT_ID: The ID of the project.
     * OPERATION_NAME: The upgrade operation name retrieved in the previous step.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operation/OPERATION_NAME




### Terraform

To upgrade the major version of the database using Terraform, you must set the `database_version` argument in your [`google_sql_database_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance) definition to the target major version. You must use the Terraform provider for Google Cloud version [4.34.0 or later](https://github.com/hashicorp/terraform-provider-google/releases).

The following examples demonstrate a basic `google_sql_database_instance` configuration. To upgrade the major version, set the `database_version` argument to the relevant major version.
    
    
    resource "google_sql_database_instance" "default" {
      name             = "sqlserver-instance"
      region           = "us-central1"
      database_version = "SQLSERVER_2019_STANDARD"
      root_password    = "INSERT-PASSWORD-HERE"
      settings {
        tier = "db-custom-2-7680"
      }
    }

Make the following changes to the Terraform arguments:

  * `database_version`: Set this to the target major version for the upgrade.
  * `deletion_protection`: Defines the root-level Terraform safeguard against instance deletion. 
    * `true`: Prevents Terraform from destroying the instance. Any Terraform operation that plans to delete this resource is blocked.
    * `false`: Allows Terraform to delete the instance.

**Note:** This is different from [GCP-level deletion protection](https://docs.cloud.google.com/sql/docs/sqlserver/deletion-protection#new-instance) (`settings.deletion_protection_enabled`).

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

### Automatic upgrade backups

When you perform a major version upgrade, Cloud SQL automatically makes two on-demand backups, called upgrade backups:

  * The first upgrade backup is the _pre-upgrade backup_ , which is made immediately before starting the upgrade. You can use this backup to restore your database instance to its state on the previous version.
  * The second upgrade backup is the _post-upgrade backup_ , which is made immediately after new writes are allowed to the upgraded database instance.



When you [view your list of backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backing-up#viewbackups), the upgrade backups are listed with type `On-demand`. Upgrade backups are labeled so that you can identify them quickly. For example, if you're upgrading from SQL Server Enterprise 2019 to SQL Server Enterprise 2022 or SQL Server Enterprise 2025, your pre-upgrade backup is labeled as `Pre-upgrade backup, SQLSERVER_2019_ENTERPRISE to SQLSERVER_2022_ENTERPRISE or SQLSERVER_2025_ENTERPRISE.` and your post-upgrade backup is labeled as `Post-upgrade backup, SQLSERVER_2022_ENTERPRISE or SQLSERVER_2025_ENTERPRISE from SQLSERVER_2019_ENTERPRISE.`

As with other on-demand backups, upgrade backups persist until you delete them or delete the instance.

## Upgrade the database compatibility level

The [database compatibility level](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-compatibility-level?view=sql-server-ver16#backwardCompat) determines how the database behaves with respect to the application it serves. The database compatibility level setting ensures [backward compatibility](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-compatibility-level?view=sql-server-ver16#backwardCompat) with earlier versions of SQL Server and relates to Transact-SQL and Query Optimizer changes. When a SQL Server instance database version is upgraded, the compatibility levels of existing databases are preserved, such that the application can continue to operate on the more recent version of SQL Server. Upgrading the compatibility level helps you benefit from new features, query processing improvements, and other changes.

After you've upgraded an instance's database engine version, when the application that the database serves is ready, upgrade the database compatibility level for each database in the instance. When the compatibility level is set to the latest, databases are upgraded with the latest features and improved performance.

**Note:** When you change the compatibility level, the database isn't restarted and you don't incur any downtime.

To upgrade the database compatibility level, perform the following steps:

  1. Identify the [current compatibility level](https://docs.microsoft.com/en-us/sql/relational-databases/databases/view-or-change-the-compatibility-level-of-a-database?view=sql-server-ver16) of your database.

For example, for SQL Server 2017, the default compatibility level is 140. To check the current compatibility level for your database, run the following command in Transact-SQL, after replacing `DATABASE_NAME`

with the name of the database on your SQL Server instance.
         
         USE DATABASE_NAME
         GO
         SELECT compatibility_level
         FROM sys.databases WHERE name = 'DATABASE_NAME'

  2. Determine the target compatibility level.

Identify the default compatibility level designation for your upgraded database version to determine the target compatibility level for your database. For example, for SQL Server 2025, the default compatibility level is 170. See the [table mapping new versions of SQL Server with compatibility levels](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-compatibility-level?view=sql-server-ver16#supported-dbcompats).

  3. Assess the differences between your current and target compatibility levels.

Before you upgrade the compatibility level, study the differences in system behavior between your current compatibility level and your target compatibility level. See the [complete list of the differences between compatibility levels](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-compatibility-level?view=sql-server-ver15#differences-between-compatibility-levels).

  4. Collect a baseline of workload data.

Before upgrading the compatibility level, collect a baseline of workload data by using [SQL Server Query Store](https://docs.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver16), so that you can later identify and address regressed queries. You use Query Store to capture queries and plans for a [typical business cycle](https://docs.microsoft.com/en-us/sql/relational-databases/performance/query-store-usage-scenarios#CEUpgrade) to establish a performance baseline. For a guided workflow, use the [Query Tuning Assistant](https://docs.microsoft.com/en-us/sql/relational-databases/performance/upgrade-dbcompat-using-qta) feature in SQL Server Management Studio.

  5. Upgrade the compatibility level.

To change the compatibility level for the database, run the following command in Transact-SQL, after replacing `DATABASE_NAME`

with the name of the database on your SQL Server instance and `TARGET_COMPATIBILITY_LEVEL` with the target compatibility level.
         
         ALTER DATABASE DATABASE_NAME
         SET COMPATIBILITY_LEVEL = TARGET_COMPATIBILITY_LEVEL;
         GO

  6. Collect upgraded workload data.

Collect upgraded workload data using Query Store for comparison and regression detection.

  7. Address regressed queries.

For the most part, Query Optimizer changes in upgraded compatibility levels improve performance. However, from time to time, certain queries might regress in performance. Query Store's [Regressed Queries](https://docs.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver16#Regressed) feature helps you identify the queries that have regressed and lets you force the last known good query plan. SQL Server also offers [automatic plan correction](https://docs.microsoft.com/en-us/sql/relational-databases/automatic-tuning/automatic-tuning?view=sql-server-ver16#automatic-plan-correction), which can automatically switch to the last known good plan in the event of a query regression. 




## Complete the major version upgrade

After upgrading your primary instance, perform acceptance tests to make sure that the upgraded system performs as expected.

## Troubleshoot a major version upgrade

Cloud SQL returns an error message if you attempt an invalid upgrade command, for example, if your instance contains invalid database flags for the new version.

If your upgrade request fails, check the syntax of your upgrade request. If the request has a valid structure, try looking into the following suggestions.

### View error logs

If any issues occur with a valid upgrade request, then Cloud SQL publishes error logs to `projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fsqlserver.err`. Each log entry contains a label with the instance identifier to help you identify the instance with the upgrade error. Look for such upgrade errors and resolve them.

To view error logs, use the Google Cloud console::

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Operations and logs** pane of the instance **Overview** page, click the **View SQL Server error logs** link.

The [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface) page opens.

  4. View logs as follows:

     * To list all error logs in a project, select the log name in the **Log name** log filter.

For more information on query filters, see [Advanced queries](https://docs.cloud.google.com/logging/docs/view/advanced-queries).

     * To filter the upgrade error logs for a single instance, enter the following query in the **Search all fields** box, after replacing `DATABASE_ID`

with the project ID followed by the instance name in this format: `project_id:instance_name`.
    
    resource.type="cloudsql_database"
    resource.labels.database_id="DATABASE_ID"
    logName : "projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fsqlserver.err"

For example, to filter the upgrade error logs by an instance named `shopping-db` running in the project `buylots`, use the following query filter:
    
    resource.type="cloudsql_database"
     resource.labels.database_id="buylots:shopping-db"
     logName : "projects/buylots/logs/cloudsql.googleapis.com%2Fsqlserver.err"

You can either review all logs reported within a given timeframe, or you can filter logs by severity. A common option for troubleshooting might include selecting the following filters:

     * Emergency
     * Alert
     * Critical
     * Error



## Restore the primary instance to the previous major version

If your upgraded database system doesn't perform as expected, then you might need to restore your primary instance to the previous version. You do so by restoring your pre-upgrade backup to a Cloud SQL recovery instance, which is a new instance running the pre-upgrade version.

To restore a primary instance to the previous version, perform the following steps:

  1. Identify your pre-upgrade backup.

See Automatic upgrade backups.

  2. Create a recovery instance.

[Create a new Cloud SQL instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance) using the major version that Cloud SQL was running when the pre-upgrade backup was made. Set the same [flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags) and [instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings) that the original instance uses.

  3. Restore your pre-upgrade backup.

[Restore](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restoring#restorebackups-another-instance) your pre-upgrade backup to the recovery instance. This might take several minutes to complete.

  4. Add your read replicas.

If you're using read replicas, then add the read replicas individually.

  5. Connect your application.

Having recovered your database system, update your application with details about the recovery instance and its read replicas. You can resume serving traffic on the pre-upgrade version of your database.




## Limitations

This section lists limitations for an in-place major version upgrade.

  * You can't perform an in-place major version upgrade on an [external replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica).
  * During the upgrade to SQL Server 2025, instances with 4 GB of RAM or less might become slow or unresponsive, causing the operation to fail. To help avoid this issue, make sure that your instance has at least 8 GB of RAM before you upgrade. After the upgrade is complete, you can downsize the instance.



## FAQs

The following questions might come up when upgrading the database major version. 

Is my instance unavailable during an upgrade?
    Yes. Your instance remains unavailable for a period of time while Cloud SQL performs the upgrade. 

How long does an upgrade take? 
    

Upgrading a single instance typically takes less than 10 minutes. If your instance configuration has a small number of vCPUs or memory, then your upgrade might take more time.

If your instance hosts too many databases or tables, or your databases are very large, then the upgrade might take hours or even time out because the total upgrade time corresponds to the number of objects in your databases. If you have multiple instances that need to be upgraded, then your upgrade time increases proportionately. 

Can I monitor each step in my upgrade process?
    While Cloud SQL lets you monitor whether an upgrade operation is still in progress, you can't track the individual steps in each upgrade. 

Can I cancel my upgrade after I've started it? 
    No, you can't cancel an upgrade once it has started. If your upgrade fails, Cloud SQL automatically recovers your instance to the previous version. 

What happens to my settings during an upgrade?
    

When you perform an in-place major version upgrade, Cloud SQL retains your database settings, including your instance name, IP address, explicitly configured flag values, and user data. However, the default value of the system variables might change.

To learn more, see [Configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags). If a certain flag or value is no longer supported in your target version, then Cloud SQL automatically removes the flag during the upgrade.

## What's next

  * Learn about [options for connecting to an instance](https://docs.cloud.google.com/sql/docs/sqlserver/external-connection-methods).
  * Learn about [importing and exporting data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export).
  * Learn more about [setting database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
