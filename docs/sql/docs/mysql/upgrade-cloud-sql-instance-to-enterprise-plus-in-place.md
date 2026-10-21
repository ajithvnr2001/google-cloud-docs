---
url: https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place/
title: Upgrade in place \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:53:40.552729+00:00
---

# Upgrade in place  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Upgrade in place Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/upgrade-in-place "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-in-place "View this page for the SQL Server database engine")

This page describes how to perform in-place upgrades and downgrades of your Cloud SQL instances.

## Make in-place changes to a Cloud SQL instance

You can use in-place changes to upgrade or downgrade the edition, machine type, or storage type of your Cloud SQL instance, or to upgrade its database version. Making in-place changes is the easiest and least error-prone way to re-configure an instance.

## Before you begin

Ensure that your instance is running on MySQL version 8.0.31 or later.

If your instance is on an earlier version of MySQL, then you must upgrade to MySQL 8.0.31 or later. For more information, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace) and [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

### Be aware of potential storage changes related to machine type

Different editions support different machine types which use different storage options. High-performance C4 and C4A machine types use [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) storage rather than one of the [persistent disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) options used by older machine types.

When you make a change to the edition or machine type you're using, your storage type may also change, which may result in some downtime and a change in storage costs. When moving to Google Cloud Hyperdisk Balanced, there are additional configuration options that you can specify. For more information, see Storage changes.

### Be aware of PITR transaction log storage changes

If you're upgrading a Cloud SQL Enterprise edition instance that stores the binary logs used for PITR on disk, be aware that the upgrade process to Cloud SQL Enterprise Plus edition moves the storage location of those logs from disk to Cloud Storage. To determine the current location of PITR binary logs for your instance, see [Check the storage location of transaction logs used for PITR](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#check-log-storage-location).

For a full explanation of how in-place upgrades can affect the location of the binary logs, see Changes in storage location of binary logs for PITR.

## Change the edition of an instance in place

This section shows you how to change the edition of your Cloud SQL instance in place to or from Cloud SQL Enterprise Plus edition. Cloud SQL Enterprise Plus edition offers some benefits and performance enhancements that Cloud SQL Enterprise edition does not. For more information about Cloud SQL editions, see [Cloud SQL editions overview](https://docs.cloud.google.com/sql/docs/mysql/editions-intro).

Upgrading to Cloud SQL Enterprise Plus edition takes a few minutes to complete and has near-zero downtime. Switching back to Cloud SQL Enterprise edition will result in a longer downtime. Neither process requires changing the endpoints that your applications connect to.

Use the procedure in this section to upgrade a Cloud SQL Enterprise edition instance to Cloud SQL Enterprise Plus edition, or to downgrade a Cloud SQL Enterprise Plus edition instance to Cloud SQL Enterprise edition.

**Note** : Cloud SQL enables [data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache) for your instance by default during the upgrade process.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Choose a Cloud SQL edition** section, click **Upgrade** if your instance is using the Cloud SQL Enterprise edition, or **Switch to Enterprise** if your instance is using Cloud SQL Enterprise Plus edition.
  5. Use the panel that opens to specify the configuration of your instance using the new edition. See [Options when making in-place changes](#change-options).
  6. Enter your instance ID to confirm these choices and then click either **Upgrade edition** or **Switch edition** depending on whether you're upgrading or downgrading.



You can also start an edition change in the **Instances** page if you select **Edit** in the **Actions** column of the instance.

In addition, if your instance is on Cloud SQL Enterprise edition, you can start an upgrade by clicking the **Upgrade** link beside the edition field in the **Configuration** section of the instance page.

### gcloud

The following [`gcloud sql instance patch`](/sdk/gcloud/reference/sql/instances/patch) code sample shows how to upgrade your instance to Cloud SQL Enterprise Plus edition:
    
    
    gcloud sql instances patch INSTANCE_ID \
      --edition=enterprise-plus \
      --tier=MACHINE_TYPE \
      --project=PROJECT_ID

**Note** : Cloud SQL enables [data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache) for your instance by default during the upgrade process. You can disable it by adding the [`--no-enable-data-cache`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--\[no-\]enable-data-cache) flag. 

Replace the following:

  * PROJECT_ID: the project ID of the instance that you want to upgrade.
  * INSTANCE_ID: name of the instance that you want to upgrade.
  * MACHINE_TYPE: the machine type of the instance that you want to upgrade to. For more information about machine types for Cloud SQL Enterprise Plus edition, see [Machine types for Cloud SQL Enterprise Plus edition instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance#enterprise-plus).



### REST

The following command upgrades your instance to Cloud SQL Enterprise Plus edition and triggers a restart operation.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID of the instance that you want to upgrade.
  * INSTANCE_ID: the instance ID of the instance that you want to upgrade.
  * MACHINE_TYPE: the machine type of the instance that you want to upgrade to. For more information about machine types for Cloud SQL Enterprise Plus edition, see [Machine types for Cloud SQL Enterprise Plus edition instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance#enterprise-plus).

**Note** : Cloud SQL enables [data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache) for your instance by default during the upgrade process. You can disable it by setting the `dataCacheEnabled` parameter as `false`.

HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
          "tier": "MACHINE_TYPE",
          "edition": "ENTERPRISE_PLUS",
          "dataCacheConfig": {
            "dataCacheEnabled": true
          },
      }
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
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

The following command upgrades your instance to Cloud SQL Enterprise Plus edition and triggers a restart operation.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID of the instance that you want to upgrade.
  * INSTANCE_ID: the instance ID of the instance that you want to upgrade.
  * MACHINE_TYPE: the machine type of the instance that you want to upgrade to. For more information about machine types for Cloud SQL Enterprise Plus edition, see [Machine types for Cloud SQL Enterprise Plus edition instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance#enterprise-plus).

**Note** : Cloud SQL enables [data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache) for your instance by default during the upgrade process. You can disable it by setting the `dataCacheEnabled` parameter as `false`.

HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
          "tier": "MACHINE_TYPE",
          "edition": "ENTERPRISE_PLUS",
          "dataCacheConfig": {
            "dataCacheEnabled": true
          },
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Options for in-place changes

Changing the edition of your Cloud SQL instance can require changing its machine series, which in turn affects its storage type.

### Machine changes

When you change editions, you have to change machine type, too. See [Choose a machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview) for more information about the machine series that Cloud SQL supports.

When upgrading from Cloud SQL Enterprise edition to Cloud SQL Enterprise Plus edition, you can choose between the [N2](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n2), [C4A](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4a), and [C4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4) machine series.

When downgrading from Cloud SQL Enterprise Plus edition to Cloud SQL Enterprise edition, you can choose between a [general purpose dedicated-core](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#gp-dedicated-core), and an [N4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n4) machine series.

**Note:** You cannot downgrade back to a Cloud SQL Enterprise edition [general-purpose shared core](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#gp-shared-core) machine series.

You can also change machine type without changing edition. After choosing to edit your instance, go to the **Machine** sub-section of **Machine Configuration** in the **Customize your instance** area. Using the drop-down, you can select a different machine type. You can also choose a different number of VCPUs, and enable or disable the [data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache) if appropriate.

For more general information, see also [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/overview) for the [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series), [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series), [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series), and [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series) machine series.

### Storage changes

If you are changing from a general purpose or an N2 machine series to an N4, C4A, or C4 machine series, your storage will be migrated from [Solid-state drive (SSD)](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#ssd) to [Google Cloud Hyperdisk balanced](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#hyperdisk) storage. This upgrade generally requires minimal downtime.

**Important:** If you switch from an N4, C4, or C4A machine series back to a general purpose dedicated-core or N2 machine series, moving your data from Google Cloud Hyperdisk Balanced storage to solid-state drive (SSD) storage can incur significant downtime. You cannot move to or from Hard-disk drive (HDD) storage.

Google Cloud Hyperdisk Balanced storage can be customized for your use case by setting the following:

  * Storage capacity
  * Provisioned IOPS
  * Provisioned throughput



Google Cloud Hyperdisk Balanced sets default IOPS and throughput values and limits based on your instance's configuration, which includes the machine type and storage capacity. Storage capacity limits the default value, and the machine type sets the maximum value for both IOPS and throughput. See [Choose a storage option](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#hyperdisk) for details.

## Location changes of binary logs for PITR

If your Cloud SQL Enterprise edition instance stores transaction logs for PITR on disk, then starting the upgrade process to Cloud SQL Enterprise Plus edition switches the storage location of these logs to Cloud Storage.

The following conditions apply to the location change:

  * The process takes approximately the duration of the [`transactionLogRetentionDays`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#backupconfiguration) PITR configuration setting to complete the switch to Cloud Storage. 
  * If you have values set for the `expire_logs_days` or `binlog_expire_logs_seconds` flag on your instance, then those values are preserved.
  * During the switch to Cloud Storage, you can't modify the values for the `expire_logs_days` or `binlog_expire_logs_seconds` flags on your instance. 
  * During the switch to Cloud Storage, we recommend that you don't modify the `transactionLogRetentionDays` PITR configuration setting. Even if you do increase `transactionLogRetentionDays`, binary logs won't be retained on disk any longer than the default of 7 days for a Cloud SQL Enterprise edition instance.


  * While the switch is in progress, Cloud SQL only retains logs on disk for the minimum value of one of the following: 
    * The `transactionLogRetentionDays` PITR configuration setting from before the switch, which is 7 days by default.
    * The `expire_logs_days` or `binlog_expire_logs_seconds` flags manually set on your instance.
  * After the switch, Cloud SQL retains the same amount of binary logs on disk that you had before the switch _unless_ you have set the `expire_logs_days` or `binlog_expire_logs_seconds` flags on your instance. If you have set these flags, then Cloud SQL retains binary logs on disk based on the minimum value of the `transactionLogRetentionDays` configuration setting or the value of the flags.



### Cloud SQL Enterprise Plus edition backup and log storage defaults

After the switch to Cloud Storage completes for an instance, Cloud SQL still retains copies of binary logs on disk for replication purposes. Storing binary logs on disk can be useful if you want to browse binary logs with the `mysqlbinlog` utility.

If you configured the `expire_logs_days` and `binlog_expire_logs_seconds` flags on your instance before the upgrade, then the configured values remain intact.

After the switch, since the binary logs that are used to perform PITR are now stored in Cloud Storage, ensure that the values of the flags reflect the retention of transaction logs on disk that you expect. Cloud SQL only retains logs on disk for the minimum value of one of the following:

  * the `transactionLogRetentionDays` PITR configuration setting before switch, 7 days by default
  * the `expire_logs_days` or `binlog_expire_logs_seconds` flags manually set on your instance



If you want to save disk space, then after the upgrade has completed, configure the value of the `expire_logs_days` or `binlog_expire_logs_seconds` flag to the equivalent of 1 day so you can reduce your allocated disk size and disk storage costs. For more information about transaction log storage and PITR, see [Log storage for PITR](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#log-storage-for-pitr).

**Note:** If your instance has a large number of binary logs on disk and you want to save disk space, then we recommend that you reduce the value of the `expire_logs_days` or `binlog_expire_logs_seconds` flag slowly. For example, reduce the value by the equivalent of 1 day each day over several days to avoid purging the binary logs all at once, to prevent any performance impacts.

After the upgrade to Cloud SQL Enterprise Plus edition completes, the default transaction log retention period for all upgraded instances is increased to 14 days. For this increase, and any other increase that you configure for the transaction log retention period, it takes up to the new and increased value to reach the full retention window of PITR. For example, if the old value for transaction log retention days is 7 and the new value is increased to 14, then the window for PITR for the first 7 days after the upgrade is only 7 days. On the 8th day, the window for PITR becomes 8 days, on the 9th day it becomes 9 days, until the retention window is finally increased to 14 days on the 14th day.

In addition, the default number of automated backups is increased from 8 to 15.

If you upgrade to Cloud SQL Enterprise Plus edition after doing a major version upgrade, then you won't be able to perform PITR to a point-in-time that occurs prior to the major version upgrade. This limitation applies even if your retention period covers that time period. You can restore your instance to a point-in-time after you started the major version upgrade.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
