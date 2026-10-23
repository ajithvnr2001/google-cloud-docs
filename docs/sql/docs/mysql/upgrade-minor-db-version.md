---
url: https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version/
title: Upgrade the database minor version of MySQL 8.0 \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:41.215975+00:00
---

# Upgrade the database minor version of MySQL 8.0  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Upgrade the database minor version of MySQL 8.0 Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

Cloud SQL for MySQL supports multiple minor versions of MySQL 8.0 and provisions MySQL 8.0 instances on the default minor version, which is one minor version earlier than the latest minor version.

With each new minor version, database providers release new features, security patches, bug fixes, and performance improvements.

MySQL 8.0 doesn't support downgrading.

**Note:** To upgrade the major version of a Cloud SQL for MySQL database, see [Upgrade the database major version by migrating data](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate) or [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace).

## Automatic upgrade

Cloud SQL supports the automatic minor version upgrade of Cloud SQL for MySQL 8.0 instances that are running MySQL version 8.0.35 or later.

When automatic minor version upgrade is enabled, a Cloud SQL for MySQL 8.0 instance is upgraded automatically to the **[default minor version](https://docs.cloud.google.com/sql/docs/mysql/db-versions#database-version-support)** of Cloud SQL for MySQL 8.0 during its [regularly scheduled maintenance update](https://docs.cloud.google.com/sql/docs/mysql/maintenance). You're no longer required to perform minor version upgrades manually to keep your Cloud SQL for MySQL instance up-to-date with the latest security patches and bug fixes released by the MySQL community.

Automatic minor version upgrade occurs only during regularly scheduled maintenance events, not during self-service maintenance.

**Caution:** Once automatic minor version upgrade is enabled, you can't disable automatic minor version upgrade for an instance.

### Enable automatic upgrade for new instances

**Note:** All existing Cloud SQL for MySQL 8.0 instances initially created without a database minor version (`databaseVersion=MYSQL_8_0`) and that are now running MySQL 8.0.35 or later have been enabled with automatic minor version upgrade. To check an existing instance, see Check for automatic minor upgrade enablement.

When creating a new Cloud SQL for MySQL 8.0 instance, consider the following regarding automatic minor version upgrades:

  * If you create a new Cloud SQL for MySQL 8.0 instance without selecting a minor version, then the instance is enabled with automatic minor version upgrade by default.

  * If you create a Cloud SQL for MySQL 8.0 instance and select a minor version of 8.0.35 or later, then you can [enable automatic minor version upgrade](https://docs.cloud.google.com/sql/docs/mysql/create-instance#specify_the_database_minor_version_for_mysql_80) during its creation.

  * If you create a Cloud SQL for MySQL 8.0 instance and select a minor version of 8.0.34 or earlier, then you can't enable automatic minor version upgrade. You must perform a manual minor version upgrade of the instance.




### Enable automatic upgrade for existing instances

If your existing instance is already installed with Cloud SQL for MySQL 8.0.35 or later, then you can enable automatic minor upgrade for your instance.

Use the following steps to enable automatic upgrades on an existing MySQL 8.0 instance. This procedure doesn't upgrade your instance. The instance will receive automatic minor version upgrades during its next scheduled maintenance event.

### Console

To enable MySQL 8.0 automatic upgrades for an existing instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Customize your instance** section, select **Enable automatic minor version upgrades**.
  5. Click **Save**.



### gcloud

To enable MySQL 8.0 automatic upgrades for an existing instance, do the following:

  1. Run the following command:
    
    gcloud sql instances patch INSTANCE_NAME \
       --enable-auto-upgrade-minor-version
      

Replace INSTANCE_NAME with the name of the instance.

  2. Check the metadata of the instance by running the following command:
    
    gcloud sql instances describe INSTANCE_NAME
      

Replace INSTANCE_NAME with the name of the instance.

In the output, look for the `DatabaseType` field, and verify that the value is updated to `MYSQL_8_0`.




### Check for automatic minor upgrade enablement

To check whether your instance is enabled for automatic minor version upgrade, run the following command:
    
    
    gcloud sql instances describe INSTANCE_NAME \
    --project=PROJECT_ID
    

Replace INSTANCE_NAME with the name of the instance and PROJECT_ID with the project ID of the instance. In the output of the command, locate the following fields.

  * `databaseVersion`: the value must be `MYSQL_8_0`
  * `databaseInstalledVersion`: the value must be a minor version equal or greater than `MYSQL_8_0_35`



## Manual upgrade

This section describes how to upgrade the minor version of a Cloud SQL for MySQL 8.0 instance manually. If you're running a Cloud SQL for MySQL version 8.0.34 or earlier, then you must upgrade the minor version of Cloud SQL for MySQL manually.

**Note:** After you upgrade your instance to Cloud SQL for MySQL version 8.0.35 manually, you can enable automatic minor version upgrade.

Before upgrading to a new MySQL 8.0 minor version, familiarize yourself with the changes. See [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/). If you use Cloud SQL for MySQL 5.6 or 5.7, Cloud SQL automatically manages your instance's minor version. When you provision a new instance, Cloud SQL automatically configures your instance with the latest database version available. During routine maintenance, Cloud SQL automatically upgrades your instance to the latest supported version.

To upgrade the database minor version of your MySQL 8.0 instance, you need to update the instance with your preferred minor version, which must be greater than the installed minor version. You can't revert to an unspecified minor version after an instance has been provisioned.

If you're running a Cloud SQL Enterprise Plus edition instance, then the minor version upgrade completes with [near-zero downtime](https://docs.cloud.google.com/sql/docs/mysql/availability#near-zero-downtime).

### Before you upgrade manually

Cloud SQL supports minor version upgrade for MySQL 8.0 instances. MySQL 8.0 doesn't allow downgrades. So, before you upgrade your primary instance, follow these steps to ensure that your data is safe.

  1. **Choose the target minor version of the database**.

### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

To check which minor versions of the database are available for an in-place upgrade, do the following:

     1. Run the following command.
    
    gcloud sql instances describe INSTANCE_NAME
       

Replace INSTANCE_NAME with the name of the instance.

     2. In the output of the command, locate the section that is labeled `upgradableDatabaseVersions`.
     3. Each subsection returns a database version that is available for upgrade. In each subsection, review the following field.
        * `name`: the database version string that includes the database major and minor version that you can target for the Cloud SQL for MySQL minor version in-place upgrade.

### REST v1

To check which minor versions of the database are available for an in-place upgrade, use the [`instances.get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/get) method of the Cloud SQL Admin API.

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

To check which minor versions of the database are available for an in-place upgrade, use the [`instances.get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/get) method of the Cloud SQL Admin API.

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

  2. **Test your upgrade in a staging environment.**

     1. Create a clone of your production instance to serve as a staging instance. This creates a new database instance, with the same major and minor versions.

     2. Perform a minor version upgrade on the staging instance.

     3. Run workload tests to verify that the upgrade was successful and that your application performs as expected. When testing is successful, proceed to upgrade your read replica instances.

  3. **Upgrade your read replica instances.**

     1. Upgrade all read replicas in the database to the target minor version.

     2. Verify that your application works as expected.

  4. **Back up your primary instance.**

As with any significant database update, make a backup of your primary instance.




### Upgrade the minor version

You can specify the database minor version of an existing instance by using `gcloud` or the REST API. Perform minor version upgrades at a time when the database isn't in use. If your instance requires a restart, then as a result, your instance experiences some downtime. Cloud SQL Enterprise Plus edition instances experience near-zero downtime. If the installed version is higher than the requested version, then the request is rejected.

**Note:** Concurrent updates, such as updating the disk size or the memory of an instance, aren't permitted while upgrading the database minor version.

### gcloud

Use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command with the `--database-version` flag. 

Replace the following variables before running the command: 

  * INSTANCE_NAME: The name of the instance.
  * DATABASE_VERSION: The database version of the instance. If you don't specify this flag, the default major version is used.


    
    
    gcloud sql instances patch INSTANCE_NAME \
       --database-version=DATABASE_VERSION

### REST v1

Use a PATCH request with the [ instances:patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method and the `databaseVersion` flag. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID
  * INSTANCE_ID: The instance ID
  * DATABASE_VERSION: The database version to upgrade to.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "databaseVersion": "DATABASE_VERSION"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2022-07-17T20:23:15.540Z",
      "operationType": "UPDATE",
      "name": "fa3f7304-ccf6-4d2f-a6f5-24df00000032",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/fa3f7304-ccf6-4d2f-a6f5-24df00000032",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Use a PATCH request with the [ instances:patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) method and the `databaseVersion` flag. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID
  * INSTANCE_ID: The instance ID
  * DATABASE_VERSION: The database version to upgrade to.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "databaseVersion": "DATABASE_VERSION"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2022-07-17T20:23:15.540Z",
      "operationType": "UPDATE",
      "name": "fa3f7304-ccf6-4d2f-a6f5-24df00000032",
      "targetId": "INSTANCE-ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/fa3f7304-ccf6-4d2f-a6f5-24df00000032",
      "targetProject": "PROJECT_ID"
    }
    

## Check the database minor installed version

When you [view the instance summary information](https://docs.cloud.google.com/sql/docs/mysql/instance-info#info), the database minor installed version is visible in the Configuration section.

## Roll back an upgrade

While testing an upgrade, if you notice an issue, you might want to roll back your database to recover the database instance running the previous minor version.

To restore a pre-upgrade backup, complete the following steps:

  1. Provision a recovery database instance on the previous minor version.
  2. Configure settings on the recovery database instance to the pre-upgrade state.
  3. Restore the pre-upgrade backup you took to the recovery instance.

**Note:** When [restoring an instance from a backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring#restorebackups) to a target instance, the installed version of the backup is compared to the installed version of the target database instance. Because MySQL 8.0 doesn't allow downgrades, if the backup has an installed version greater than that of the target, the restore request is rejected.

As an alternative to restoring a backup, [perform a point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#perform-pitr) and create a new instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
