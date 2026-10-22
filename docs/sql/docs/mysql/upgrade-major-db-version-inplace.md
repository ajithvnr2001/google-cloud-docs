---
url: https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace/
title: Upgrade the database major version in-place \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:48.521941+00:00
---

# Upgrade the database major version in-place  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Upgrade the database major version in-place Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-inplace "View this page for the SQL Server database engine")

This page describes how to upgrade the database major version by upgrading your Cloud SQL instance in-place rather than [by migrating data](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate).

## Introduction

Database software providers periodically release new major versions that contain new features, performance improvements, and security enhancements. Cloud SQL takes in [new versions](https://docs.cloud.google.com/sql/docs/mysql/db-versions) after they're released. After Cloud SQL offers support for a new major version, you can upgrade your instances to keep your database updated.

You can upgrade the database version of an instance in-place or by [migrating data](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate). In-place upgrades are a simpler way to upgrade your instance's major version. You don't need to migrate data or change application connection strings. With in-place upgrades, you can retain the name, IP address, and other settings of your current instance after the upgrade. In-place upgrades don't require you to move data files and can be completed faster. In some cases, the downtime is shorter than what migrating your data entails.

For MySQL 8.0.15 and earlier, the MySQL in-place upgrade operation uses the [`mysql_upgrade`](https://dev.mysql.com/doc/refman/8.0/en/mysql-upgrade.html) utility. For MySQL 8.0.16 and later, the MySQL in-place upgrade operation is handled by the [`MySQL server`](https://dev.mysql.com/doc/refman/8.4/en/mysqld.html) process. For more information about the in-place upgrade operation, see [What the MySQL Upgrade Process Upgrades](https://dev.mysql.com/doc/refman/8.4/en/upgrading-what-is-upgraded.html). 

## Plan a major version upgrade

  1. Confirm that you have the required role to perform a major version upgrade: [Cloud SQL Owner](https://docs.cloud.google.com/sql/docs/mysql/iam-roles) or [Cloud SQL Admin](https://docs.cloud.google.com/sql/docs/mysql/iam-roles).
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
        * `name`: the database version string that includes the major version. For Cloud SQL for MySQL, this field also includes the minor version of the database.
        * `displayName`: the display name for the database version. 

### REST v1

To check which target database versions are available for a major version in-place upgrade, use the [`instances.get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/get) method of the Cloud SQL Admin API.

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
      major_version: "MYSQL_8_0"
      name: "MYSQL_8_0_36"
      display_name: "MySQL 8.0.36"
    }
    
    

### REST v1beta4 

To check which target database versions are available for major version in-place upgrade of an instance, use the [`instances.get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/get) method of the Cloud SQL Admin API.

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
      major_version: "MYSQL_8_0"
      name: "MYSQL_8_0_36"
      display_name: "MySQL 8.0.36"
    }
    
    

For the complete list of the database versions that Cloud SQL supports, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/mysql/db-versions).

  3. Consider the features offered in each database major version and address incompatibilities.

     * [MySQL 9.7](https://dev.mysql.com/doc/refman/9.7/en/upgrading-from-previous-series.html)
     * [MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/upgrading-from-previous-series.html)
     * [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html)
     * [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/upgrading-from-previous-series.html)

New major versions introduce incompatible changes that might require you to modify the application code, the schema, or the database settings. Before you can upgrade your database instance, review the release notes of your target major version to determine the incompatibilities that you must address.

After upgrading to a later version, the default value of some system variables might change. For example, the default value of `character_set_server` in MySQL 5.6 and MySQL 5.7 is `utf8`. When you upgrade to MySQL 8.0, the default value of `character_set_server` changes to `utf8mb4`. To revert to `utf8`, you must manually change the database flag value to its old value. See [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags) for more information. Most of the default value changes are done by the MySQL Community (see more at [Upgrade Server Defaults](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-server-defaults)).

**Note:** You can upgrade only from one major version to the next. MySQL doesn't support skipping major versions. You can't upgrade directly from MySQL 5.6 to MySQL 8.0 or from MySQL 5.7 to MySQL 8.4.
  4. Perform the precheck for upgrades.

  5. Test the upgrade with a dry run.

Perform a dry run of the end-to-end upgrade process in a test environment before you upgrade the production database. You can [clone your instance](https://docs.cloud.google.com/sql/docs/mysql/clone-instance) to create an identical copy of the data on which to test the upgrade process.

In addition to validating that the upgrade completes successfully, run tests to ensure that the application behaves as expected on the upgraded database.

**Note:** Ensure that you have enough disk space before running a major version upgrade. If you haven't enabled [automatic storage increases](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen), then take note of the disk storage used by the upgraded dry run instance. This helps you determine whether you need to increase the storage capacity for the production instance before upgrading.
  6. Decide on a time to upgrade.

Upgrading requires the instance to become unavailable for a period of time. Plan to upgrade during a time period when database activity is low.




## Prepare for a major version upgrade

Before you upgrade, complete the following steps:

  1. If you're upgrading from MySQL 8.0 to MySQL 8.4, then all new users that you create after the upgrade use the `caching_sha2_password` authentication plugin instead of the deprecated `mysql_native_password` plugin. You can also update existing user accounts to use the `caching_sha2_password` authentication plugin. **Important:** BigQuery federated queries don't support the `caching_sha2_password` authentication plugin. If you want to use BigQuery to query your MySQL 8.4 database, don't update the authentication plugin from `caching_sha2_password` to `mysql_native_password`. For more details, see [Troubleshooting](https://docs.cloud.google.com/bigquery/docs/cloud-sql-federated-queries#troubleshooting). To change your existing database user accounts to use the `caching_sha2_password` authentication plugin, use the following command: 
         
         ALTER USER 'username'@'%'
         IDENTIFIED WITH caching_sha2_password BY 'user_password';
              

Replace username and user_password with the values for the built-in authentication database user account that you're updating. 
  2. Check disk space and instance machine type.

Major version upgrades require additional disk space and memory to store the upgraded tables and new data dictionary. Insufficient disk space causes the upgrade to fail and roll back to the original version. Cloud SQL recommends that you have a minimum of 100 KB in memory for each table.

**Note:** You can temporarily increase memory by changing the machine type before running the major version upgrade. To learn more, see [changing the machine type](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen).



### Required configuration for using MySQL 8.4 or later with the Cloud SQL Auth Proxy

When using MySQL 8.4 or later with the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy), you must configure your application database configuration with the MySQL configuration setting `allowPublicKeyRetrieval=true`. You must upgrade your client applications with this configuration before you upgrade the database version.

For example, if you're using the `mysql` client, then use `--get-server-public-key` flag:
    
    
    mysql -u username -p --get-server-public-key
    

If you're using the Java programming language, then use the following:
    
    
    config.setJdbcUrl("jdbc:mysql://" + dbHost + ":" + dbPort + "/" + dbName);
    config.addDataSourceProperty("allowPublicKeyRetrieval", "true");
    

## Assess upgrade readiness for your instance

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud SQL lets you run a precheck on your instance before a major version upgrade. This precheck is a long-running operation (LRO) that checks if your instance is ready for an upgrade. It helps find potential problems like incompatibilities, configuration issues, or data problems prior to the upgrade operation.

The precheck runs the [MySQL Shell upgrade checker utility](https://dev.mysql.com/doc/mysql-shell/8.4/en/mysql-shell-utilities-upgrade.html) to check whether your instance is ready for an upgrade to the next major version. If the instance isn't ready, then the utility lists issues that you need to fix before you start the upgrade. These issues are due to known incompatibilities between the two major versions. 

Cloud SQL can run the precheck process in parallel with your workload. Running the precheck before you perform a major version upgrade can help prevent an upgrade failure.

**Note:** We recommend that you run the precheck during non-peak operational hours to avoid a potential timeout of the precheck operation. Precheck utilizes instance CPU and memory because precheck validates the compatibility of objects in the system. To minimize the impact on resource usage, you can perform precheck first on a replica instance.

When you run the precheck, one of the following happens:

  * **No issues found** : the precheck finished successfully, and no problems were found.
  * **Issues found** : the precheck finished successfully, but it found errors that will block your upgrade. The issues must be resolved prior to the upgrade.
  * **Warnings found** : the precheck finished successfully and found warnings. Review the warnings. We recommend that you address any issues before you proceed with the upgrade.



Depending on the precheck's results, you can either proceed with the upgrade or fix the identified issues before upgrading.

### Limitations

When using the major version upgrade precheck, consider the following limitations:

  * The instance state must be set to `RUNNING`.


  * The instance must not have any blocking operations pending. If a blocking operation is pending, then the precheck results in an error with the following message:
        
        Operation failed because another operation was already in progress. Try
        your request after the current operation is complete.
        

  * The precheck needs to connect to all databases on the instance. If a database is inaccessible, locked, or unresponsive, then the precheck might fail or show errors. We recommend running the precheck when database load is low.



  * Precheck checks the compatibility of the upgrade between [consecutive major versions of Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/db-versions). For example, you can run precheck for the upgrade between MySQL 5.7 and MySQL 8.0, the upgrade between MySQL 8.0 and MySQL 8.4, and then the upgrade between MySQL 8.4 and MySQL 9.7.

Precheck doesn't support checking a minor version upgrade within the same major version. For example, you can't perform a precheck for an upgrade from MySQL 8.0.31 to 8.0.45.

  * Precheck is limited to three hours. If the precheck operation exceeds the three-hour limit, then the process times out and is canceled automatically.

  * The MySQL Shell upgrade checker utility might not detect all incompatibilities during the precheck process. It's still possible for your upgrade to fail. It's also possible for some unaddressed warnings to block a major version upgrade.




### Before you begin

  * Make sure the Cloud SQL Admin API is enabled for your instance.
  * Confirm you have the `cloudsql.instances.preCheckMajorVersionUpgrade` [IAM permission](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions).



### Perform the precheck

To perform the major version upgrade precheck, do the following:

### gcloud

  1. Use the [ `gcloud beta sql instances pre-check-major-version-upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/pre-check-major-version-upgrade) to run the precheck:
         
         gcloud beta sql instances pre-check-major-version-upgrade INSTANCE_NAME \
           --target-database-version=TARGET_DATABASE_VERSION \
           --project=PROJECT_ID \
           [--async]
            

Replace the following:

     * INSTANCE_NAME: the name of the instance.
     * TARGET_DATABASE_VERSION: the major version you want to upgrade your instance to. To find the database version, see [Plan an upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#plan-upgrade).
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



### REST v1beta4

  1. Run the precheck.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * TARGET_DATABASE_VERSION: the major version to upgrade to. To find a list of available database versions, see [Plan an upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#plan-upgrade).

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

Use the `GET` request with [`operations.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations/list) method after replacing `PROJECT_ID` with the ID of the project.
         
         GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
  3. Monitor the status of the precheck.

Use the `GET` request with [`operations.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations/list) method:
         
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
`WARNING` |  A potential issue was found. Cloud SQL recommends reviewing and addressing the warning before upgrading to ensure full compatibility.  |  Yes   
`ERROR` | A critical issue that blocks the upgrade was found. These issues might cause the upgrade to fail. You must resolve them before upgrading your instance. | Yes  
If your instance only has `INFO` messages, you can upgrade it, but you might have issues after the upgrade. We recommend reviewing the message details and resolving the issue before upgrading. If your instance has `ERROR` or `WARNING` messages, you must resolve these issues before upgrading. 

Each issue type includes a `message` and an `actions_required` field. Review each issue to understand its type and how to resolve it. For more information about common issues and their solutions, see Common major version upgrade precheck errors.

After you resolve the issues, re-run the precheck to confirm your instance is ready for the upgrade. Then, proceed with upgrading your instance once the precheck is clear.

### Cancel a major version upgrade precheck

You can cancel a major version upgrade precheck operation for Cloud SQL for MySQL.

**Note:** You can only cancel a precheck operation that you request independently before the major version upgrade. You can't cancel any precheck processes that are running as part of the major version upgrade.

#### Before you begin

To cancel the major version upgrade precheck, you need the ID of the precheck operation. You need to specify this ID in the `gcloud` or REST API command so that Cloud SQL knows which operation to cancel.

The operation ID is returned in the `name` field of the response.

You can also find the operation ID by making an [`operations.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations/list) call on the Cloud SQL instance.

#### Perform cancellation

You can use the `gcloud` or REST API commands to cancel a precheck operation.

###  gcloud 

  1. Get the precheck operation ID.

Use the [`gcloud sql operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/list) command with the `--instance` flag:
         
         gcloud sql operations list --instance=INSTANCE_NAME
         

Replace the following:

     * INSTANCE_NAME: the name of the instance.
  2. Cancel the precheck.

Use the [`gcloud sql operations cancel`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/cancel) command:
         
         gcloud sql operations cancel OPERATION_ID
         

Replace the following:

     * OPERATION_ID: the operation ID retrieved in the previous step.



###  REST v1beta4 

  1. Get the precheck operation ID.

Use the GET request with [`operations.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations/list) method after replacing `PROJECT_ID` with the ID of the project.
         
         GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
  2. Cancel the precheck.

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




#### Check the cancelled status

You can use `gcloud` or REST API commands to check the status of a cancelled precheck operation.

###  gcloud 

  1. Check the cancelled status.

Use the [`gcloud sql operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/describe) command:
         
         gcloud sql operations describe OPERATION_ID
         

Replace the following:

     * OPERATION_ID: the operation ID of the cancelled precheck.



###  REST v1beta4 

  1. Check the cancelled status.

Use the GET request with [`operations.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations/list) method:
         
         GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * OPERATION_ID: the operation ID of the cancelled precheck.



#### Troubleshoot cancellation

Issue | Troubleshooting  
---|---  
Error message: `You can't cancel operation OPERATION_ID because this operation isn't in progress.` | You're trying to cancel a precheck operation that's completed, failed, or already cancelled. If the operation is running, you can cancel it.  
Error message: `You can't cancel operation OPERATION_ID because Cloud SQL doesn't support the cancellation of an OPERATION_TYPE operation.` | This error usually occurs when you pass the wrong OPERATION_ID to the cancel command—specifically, the ID of an operation type that doesn't support cancellation. Verify that you're using the OPERATION_ID associated with the major version upgrade precheck you want to cancel.  
Error message: `The OPERATION_TYPE operation isn't cancelled. Wait and retry in a few seconds.` | Cloud SQL can't cancel the precheck operation at this time. Try again in a few seconds. If the problem persists, contact [Cloud Customer Care](https://docs.cloud.google.com/support).  
  
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

**Note:** If you use read replicas and choose not to include replicas with your major version upgrade, then you must upgrade the read replicas _before_ you upgrade the primary instance. After you upgrade a replica, you can't roll back the database version of the replica. The replicated databases of an upgraded replica are available only after you upgrade the primary instance.  When you upgrade to MySQL 8.0, Cloud SQL automatically provisions your instance on the default minor version. 

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
     * DATABASE_VERSION: The enum for the database major version, which must be later than the current version. Specify a database version for a major version that is available as an upgrade target for the instance. You can obtain this enum as the first step of Plan for upgrade. If you need a complete list of database version enums, then see [SqlDatabaseEnums](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).
    
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

Use a PATCH request with the [`instances:patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method. 

Before using any of the request data, replace these variables:

     * PROJECT_ID: The ID of the project.
     * INSTANCE_NAME: The name of the instance.

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "databaseVersion": DATABASE_VERSION
    }

Replace DATABASE_VERSION with the enum for the database major version, which must be later than the current version. Specify a database version for a major version that is available as an upgrade target for the instance. You can obtain this enum as the first step of Plan for upgrade. If you need a full list of database version enums, then see [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).

  2. Get the upgrade operation name. 

Use a GET request with the [`operations.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations/list) method after replacing PROJECT_ID with the ID of the project. 

HTTP method and URL: 
         
         GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations

  3. Monitor the status of the upgrade. 

Use a GET request with the [`operations.get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations/get) method after replacing the following variables:

     * PROJECT_ID: The ID of the project.
     * OPERATION_NAME: The upgrade operation name retrieved in the previous step.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operation/OPERATION_NAME




### Terraform

To upgrade the major version of the database using Terraform, you must set the `database_version` argument in your [`google_sql_database_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance) definition to the target major version. You must use the Terraform provider for Google Cloud version [4.34.0 or later](https://github.com/hashicorp/terraform-provider-google/releases).

The following examples demonstrate a basic `google_sql_database_instance` configuration. To upgrade the major version, set the `database_version` argument to the relevant major version.
    
    
    resource "google_sql_database_instance" "default" {
      name             = "mysql-instance"
      region           = "us-central1"
      database_version = "MYSQL_8_0"
      settings {
        tier = "db-n1-standard-2"
      }
    }

Make the following changes to the Terraform arguments:

  * `database_version`: Set this to the target major version for the upgrade.
  * `deletion_protection`: Defines the root-level Terraform safeguard against instance deletion. 
    * `true`: Prevents Terraform from destroying the instance. Any Terraform operation that plans to delete this resource is blocked.
    * `false`: Allows Terraform to delete the instance.

**Note:** This is different from [GCP-level deletion protection](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection#new-instance) (`settings.deletion_protection_enabled`).

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
     * DATABASE_VERSION: the enum for the database major version, which must be later than the current version. Specify a database version for a major version that is available as an upgrade target for the instance. You can obtain this enum as the first step of Plan for upgrade. If you need a complete list of database version enums, then see [SqlDatabaseEnums](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).
    
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

Use a PATCH request with the [`instances:patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method. 

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

     * Replace DATABASE_VERSION with the enum for the database major version, which must be later than the current version. Specify a database version for a major version that is available as an upgrade target for the instance. You can obtain this enum as the first step of Plan for upgrade. If you need a full list of database version enums, then see [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).
     * In the `includeReplicasForMajorVersionUpgrade` field, specify `true`.
  2. Get the upgrade operation name. 

Use a GET request with the [`operations.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations/list) method after replacing PROJECT_ID with the ID of the project. 

HTTP method and URL: 
         
         GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations

  3. Monitor the status of the upgrade. 

Use a GET request with the [`operations.get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations/get) method after replacing the following variables:

     * PROJECT_ID: the ID of the project.
     * OPERATION_NAME: the upgrade operation name retrieved in the previous step.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operation/OPERATION_NAME




### Automatic upgrade backups

When you perform a major version upgrade, Cloud SQL automatically makes two on-demand backups, called upgrade backups:

  * The first upgrade backup is the _pre-upgrade backup_ , which is made immediately before starting the upgrade. You can use this backup to restore your database instance to its state on the previous version.
  * The second upgrade backup is the _post-upgrade backup_ , which is made immediately after new writes are allowed to the upgraded database instance.



When you [view your list of backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#viewbackups), the upgrade backups are listed with type `On-demand`. Upgrade backups are labeled so that you can identify them quickly. For example, if you're upgrading from MySQL 5.7 to MySQL 8.0, then your pre-upgrade backup is labeled `Pre-upgrade backup, MYSQL_5_7 to MYSQL_8_0.` and your post-upgrade backup `Post-upgrade backup, MYSQL_8_0 from MYSQL_5_7.` If you're upgrading from MySQL 8.0 to MySQL 8.4, then your pre-upgrade backup is labeled `Pre-upgrade backup, MYSQL_8_0 to MYSQL_8_4.` and your post-upgrade backup `Post-upgrade backup, MYSQL_8_4 from MYSQL_8_0.` If you're upgrading from MySQL 8.4 to MySQL 9.7, then your pre-upgrade backup is labeled `Pre-upgrade backup, MYSQL_8_4 to MYSQL_9_7.` and your post-upgrade backup is labeled `Post-upgrade backup, MYSQL_9_7 from MYSQL_8_4.`

As with other on-demand backups, upgrade backups persist until you delete them or delete the instance. If you have PITR enabled, you can't delete your upgrade backups while they're in your retention window. If you need to delete your upgrade backups, you must disable PITR or wait until your upgrade backups are no longer in your retention window.

## Complete the major version upgrade

After you've finished upgrading your primary instance, perform the following steps to complete your upgrade: 

  1. Perform acceptance tests.

Run tests to confirm that your upgraded system is performing as expected.

  2. Optional: Update user privileges.

MySQL 8.0 has new changes to the security and account management systems. For more information, see [ What is New in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html). 

Cloud SQL for MySQL has adopted these changes and enhanced the user privileges associated with the [`cloudsqlsuperuser`](https://docs.cloud.google.com/sql/docs/mysql/users#cloudsqlsuperuser) role. Users that were created in the MySQL 5.7 version of the instance might not have the same privileges as users created in MySQL 8.0 directly. For example, users that upgrade from MySQL 5.7 to MySQL 8.0 don't have the `CONNECTION_ADMIN` privilege. As a result, they can't run the `KILL` command on sessions from other users. To learn how to update user privileges, refer to the procedure in this section.

If you upgrade from MySQL 8.0 to MySQL 8.4, then there are additional changes to user privileges, including the addition of privileges introduced in MySQL 8.4 and the removal of privileges that existed in MySQL 8.0. For more information, see [MySQL 8.4 user privileges (`cloudsqlsuperuser`)](https://docs.cloud.google.com/sql/docs/mysql/users#cloudsqlsuperuser-84).

You can update user privileges in either MySQL 8.0, MySQL 8.4, or MySQL 9.7 by doing the following:

     1. [Create a user](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating) with the `cloudsqlsuperuser` role granted, by default. 

     2. Use this user to connect to the instance so that you can update the privileges of other users.

For example, to check the privileges that users have, run the following command:
            
            SHOW GRANTS for 'admin'@'%',

To grant privileges to a user, such as the privilege to use the `KILL` command to end connections, run the following command: 
            
            GRANT CONNECTION_ADMIN ON *.* to 'admin'@'%';

To apply the `cloudsqlsuperuser` role to the `admin'@'%` user, run the following command: 
            
            GRANT 'cloudsqlsuperuser' to 'admin'@'%';

  3. Optional: Create a backup.

Although Cloud SQL automatically creates a backup after you upgrade your primary instance, Cloud SQL recommends that you create a backup on your own so that you can recover your database, if necessary.

  4. Optional: If you have upgraded to Cloud SQL for MySQL 8.4 or MySQL 9.7, then also update all your connectors, clients, and MySQL shells to MySQL 8.4 or MySQL 9.7.



## Troubleshoot a major version upgrade

Cloud SQL returns an error message if you attempt an invalid upgrade command, for example, if your instance contains invalid database flags for the new version.

If your upgrade request fails, check the syntax of your upgrade request. If the request has a valid structure, try looking into the following suggestions.

### View error logs

If any issues occur with a valid upgrade request, then Cloud SQL publishes error logs to `projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fmysql.err`. Each log entry contains a label with the instance identifier to help you identify the instance with the upgrade error. Look for such upgrade errors and resolve them.

To view error logs, use the Google Cloud console::

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Operations and logs** pane of the instance **Overview** page, click the **View MySQL error logs** link.

The [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface) page opens.

  4. View logs as follows:

     * To list all error logs in a project, select the log name in the **Log name** log filter.

For more information on query filters, see [Advanced queries](https://docs.cloud.google.com/logging/docs/view/advanced-queries).

     * To filter the upgrade error logs for a single instance, enter the following query in the **Search all fields** box, after replacing `DATABASE_ID`

with the project ID followed by the instance name in this format: `project_id:instance_name`.
    
    resource.type="cloudsql_database"
    resource.labels.database_id="DATABASE_ID"
    logName : "projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fmysql.err"

For example, to filter the upgrade error logs by an instance named `shopping-db` running in the project `buylots`, use the following query filter:
    
    resource.type="cloudsql_database"
     resource.labels.database_id="buylots:shopping-db"
     logName : "projects/buylots/logs/cloudsql.googleapis.com%2Fmysql.err"

You can either review all logs reported within a given timeframe, or you can filter logs by severity. A common option for troubleshooting might include selecting the following filters:

     * Emergency
     * Alert
     * Critical
     * Error

You might experience some known issues during precheck and upgrade from MySQL version 5.7 to MySQL 8.0. For help troubleshooting these issues, see [Troubleshooting in-place major version upgrade to MySQL 8.0](https://docs.cloud.google.com/sql/docs/mysql/troubleshooting-in-place-major-version-upgrade-to-8.0).




### MVU operation running for a longer duration

There are two underlying tasks associated with a major version upgrade:

  * **Precheck operation** : Returns a timeout error if not finished within three hours.
  * **Upgrade operation** : Returns a timeout error if not finished within six hours.



If the instance has an ongoing `MAJOR_VERSION_UPGRADE` operation for a length of time longer than expected, then [investigate the MySQL error logs](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#view-error-logs). This might be caused by common issues such as:

  * A large number of tables, views, or indexes
  * Insufficient resources such as CPU or memory
  * Major transactions blocking the shutdown of databases for the upgrade process to begin. You can use the Google Cloud console to check current processes.



### Common major version upgrade precheck errors

Common issues found in upgrades from MySQL 5.7 to MySQL 8.0 can include:

  * Addition of new reserved keywords, such as `RANKS`, `GROUPS`, `FUNCTION`, in stored procedures, triggers, and other database objects. See [Keywords and Reserved Words](https://dev.mysql.com/doc/refman/8.0/en/keywords.html) for more information.
  * Invalid UTF Characters in table definitions.
  * Uncommitted XA transitions that must be committed (using the `XA COMMIT` statement) or rolled back (using the `XA ROLLBACK` statement).
  * Foreign key constraint in names longer than 64 characters.
  * Spatial data type in a mixed index of columns. For more information, see [Spatial Data Type](https://dev.mysql.com/doc/refman/8.0/en/spatial-type-overview.html).



For help troubleshooting error and known issues during the MySQL 5.7 to MySQL 8.0 precheck, see [Troubleshooting in-place major version upgrade to MySQL 8.0](https://docs.cloud.google.com/sql/docs/mysql/troubleshooting-in-place-major-version-upgrade-to-8.0). For more information about common MySQL issues, see [Preparing your installation for upgrade](https://dev.mysql.com/doc/refman/8.0/en/upgrade-prerequisites.html) and [Upgrading to MySQL 8.0?](https://dev.mysql.com/blog-archive/upgrading-to-mysql-8-0-here-is-what-you-need-to-know/).

Common issues found in upgrades from MySQL 8.0 to MySQL 8.4 can include:

  * Outdated replication terminology. The terms `MASTER` and `SLAVE` are completely removed from MySQL 8.4. 

If you still use any commands or configurations with these terms, then you must replace or remove them. For more information about the removal and replacement of these terms, see [What Is New in MySQL 8.4 since MySQL 8.0](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html#mysql-nutshell-removals). 




Common issues found in upgrades from MySQL 8.4 to MySQL 9.7 can include:

  * If you have enabled `cloudsql_vector` for your instance, then you can't have a secondary non-vector index on a column that has any Cloud SQL vector embeddings prior to the upgrade. You might receive the following error message: 

` Non-vector secondary indexes are disallowed on vector columns when cloudsql_vector is enabled.`

To resolve this issue, drop the secondary index before you upgrade to MySQL 9.7.

  * You have existing vector embeddings in your Cloud SQL 8.4 database, but you have turned `cloudsql_vector` to `off`. As part of the upgrade to MySQL 9.7, all vector data is migrated to the community MySQL format instead of the `VARBINARY` format used by Cloud SQL for MySQL 8.4 and earlier databases. To help ensure that the vector data is migrated correctly, you can update the `cloudsql_vector` flag to `on` and proceed with the upgrade to MySQL 9.7. The upgrade process migrates your vector data to the community-based format. Alternatively, you can keep the `cloudsql_vector` flag set to `off` and delete the vector data manually in your MySQL 8.4 database before you upgrade.
  * You have remaining built-in database user accounts that use the `mysql_native_password` plugin. The plugin is removed completely from Cloud SQL for MySQL 9.7. If any user accounts use the `mysql_native_password` plugin, then those accounts aren't able to connect to your database. You must change any remaining accounts to use the `caching_sha2_password` plugin before you upgrade to Cloud SQL for MySQL 9.7.



## Restore the primary instance to the previous major version

If your upgraded database system doesn't perform as expected, then you might need to restore your primary instance to the previous version. You do so by restoring your pre-upgrade backup to a Cloud SQL recovery instance, which is a new instance running the pre-upgrade version.

To restore a primary instance to the previous version, perform the following steps:

  1. Identify your pre-upgrade backup.

See Automatic upgrade backups.

  2. Create a recovery instance.

[Create a new Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance) using the major version that Cloud SQL was running when the pre-upgrade backup was made. Set the same [flags](https://docs.cloud.google.com/sql/docs/mysql/flags) and [instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings) that the original instance uses.

  3. Restore your pre-upgrade backup.

[Restore](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring#restorebackups-another-instance) your pre-upgrade backup to the recovery instance. This might take several minutes to complete.

  4. Add your read replicas.

If you're using read replicas, then add the read replicas individually.

  5. Connect your application.

Having recovered your database system, update your application with details about the recovery instance and its read replicas. You can resume serving traffic on the pre-upgrade version of your database.




## Limitations

This section lists limitations for an in-place major version upgrade.

  * You can't perform an in-place major version upgrade on an [external replica](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica).
  * Upgrading instances from MySQL 5.7 to MySQL 8.0 that have more than 512,000 tables might take a long time and timeout.
  * Upgrading instances from MySQL 8.0 to MySQL 8.4 that have more than 512,000 tables might take a long time and timeout.
  * When upgrading from MySQL 8.0 to MySQL 8.4, if you have upgraded a replica to MySQL 8.4 but not the primary instance, then it's possible to create a new user account on a non-upgraded primary instance with the deprecated `mysql_native_password` authentication plugin. To avoid this situation, make sure that you upgrade the primary instance immediately after upgrading the replicas, or only create new user accounts on the primary instance by using the following command.
        
        CREATE USER 'USERNAME'@'%' IDENTIFIED WITH caching_sha2_password BY 'PASSWORD';

Replace USERNAME and PASSWORD with appropriate values.




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
    No, you can't cancel an upgrade once it has started. If your upgrade fails, Cloud SQL automatically recovers your instance to the previous version. 

What happens to my settings during an upgrade?
    

When you perform an in-place major version upgrade, Cloud SQL retains your database settings, including your instance name, IP address, explicitly configured flag values, and user data. However, the default value of the system variables might change. For example, the default value of the `character_set_server` flag in MySQL 5.7 is `utf8`. When you upgrade to MySQL 8.0, the default value of the flag changes to `utf8mb4`. To revert it to `utf8`, set the flag value back to previous value.

To learn more, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags). If a certain flag or value is no longer supported in your target version, then Cloud SQL automatically removes the flag during the upgrade.

What can I do if replication breaks after I upgrade a replica?

    

If replication breaks after you upgrade a replica, then Cloud SQL rolls back the replica to the MySQL major version of the primary instance. You can upgrade the replica again, but if the issue persists, then replication might break again. For this reason, we recommend that you include your replicas when you perform a major version upgrade instead of upgrading each replica separately.

If the replica isn't rolled back to the same major version as your primary instance, then you have two options:

  1. Delete the broken replica, create a new replica, and upgrade the new replica.

If the upgrade fails again, it's likely caused by incompatible changes added to the primary instance when it was upgraded. Troubleshoot the upgrade to locate the issue, fix the primary instance, and try to upgrade the replica. For more information, see troubleshoot.

  2. Upgrade the primary instance

If the replica thread is not working, then the upgrade operation on the primary instance recreates the replicas.




Why did my upgraded replica roll back to the previous major version?
    

If an upgrade is unsuccessful, then the replica is rolled back to the primary instance's version. You can upgrade the replica again but if the issue persists, you can check the `mysql.err` log on the replica to find the source. Search for keywords such as `[REPL]... failed executing transaction.... end_log_pos...; Failure Reason`. 

If the error message contains `Access denied for AuthId....` with user privilege changes, there is likely a query being executed using MySQL 5.7 user privileges on mysql and sys schemas, and might fail due to the changes to the security and account management systems in MySQL 8.0. To resolve this issue, you must stop the queries on the primary instance before upgrading the primary instance to the new version and then retry the replica upgrade. Cloud SQL recommends that you temporarily stop all such queries in the primary instance as well before upgrading to the new version as it might lead to a similar issue.

If you don't see the the failure reason, such as ` Access denied for AuthID....` in the MySQL logs, then your issue is likely caused by new incompatible data that might have been added to the primary instance after the replica had been upgraded. See prepare for a major version upgrade on how to fix incompatibility issues before upgrading again.

## What's next

  * Learn about [options for connecting to an instance](https://docs.cloud.google.com/sql/docs/mysql/external-connection-methods).
  * Learn about [importing and exporting data](https://docs.cloud.google.com/sql/docs/mysql/import-export).
  * Learn more about [setting database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
