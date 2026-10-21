---
url: https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr/
title: Perform point-in-time recovery (PITR) \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:50.518942+00:00
---

# Perform point-in-time recovery (PITR)  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Perform point-in-time recovery (PITR) Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr "View this page for the PostgreSQL database engine") | SQL Server

You can use point-in-time-recovery (PITR) to restore your primary Cloud SQL instances whether the instance is live, or is deleted. PITR lets you restore the instance to a specific point-in-time. A point-in-time recovery always creates a new instance; you cannot perform a PITR to an existing instance.

Cloud SQL provides the following options to restore your instance using PITR:

  * Perform a PITR on a live instance
  * Perform a PITR using the backup vault


  * Perform a PITR on a deleted instance



For performing a PITR on an unavailable or deleted instance, you'll need to find the latest and earliest recovery time.

## Perform a PITR 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Open the more actions menu ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png) for the instance you want to recover and click **Create clone**.
  3. Optionally, on the **Create a clone** page, update the ID of the new clone.
  4. Select **Clone from an earlier point in time**.
  5. Enter a PITR time.
  6. Select **All databases** , or specify a database name.  
If you specify a database name, only one may be selected. By default, PITR is for all databases. 
  7. Click **Create clone**.



### gcloud

Create a clone using PITR.

Replace the following:

  * SOURCE_INSTANCE_NAME \- Name of the instance you're restoring from.
  * NEW_INSTANCE_NAME \- Name for the clone.
  * TIMESTAMP \- UTC timezone for the source instance in RFC 3339 format. For example, 2012-11-15T16:19:00.094Z.


    
    
    gcloud sql instances clone SOURCE_INSTANCE_NAME \
    NEW_INSTANCE_NAME \
    --point-in-time 'TIMESTAMP'

**Note:** By default, point-in-time recovery is for all databases. Optionally, you can specify up to one specific database name as follows: `--database_names 'DATABASE'`

### REST v1

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * target-instance-id: The target instance ID
  * source-instance-id: The source instance ID
  * restore-timestamp The point-in-time to restore up to



In the JSON request, you optionally can specify up to one specific database name as the following: `"databaseNames": "my-database"`

HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/source-instance-id/clone

Request JSON body: 
    
    
    {
      "cloneContext":
      {
        "kind": "sql#cloneContext",
        "destinationInstanceName": "target-instance-id",
        "pointInTime": "restore-timestamp"
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/source-instance-id/clone"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/source-instance-id/clone" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE",
      "name": "operation-id",
      "targetId": "target-instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * target-instance-id: The target instance ID
  * source-instance-id: The source instance ID
  * restore-timestamp The point-in-time to restore up to



In the JSON request, you optionally can specify up to one specific database name as the following: `"databaseNames": "my-database"`

HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/source-instance-id/clone

Request JSON body: 
    
    
    {
      "cloneContext":
      {
        "kind": "sql#cloneContext",
        "destinationInstanceName": "target-instance-id",
        "pointInTime": "restore-timestamp"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/source-instance-id/clone"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/source-instance-id/clone" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE",
      "name": "operation-id",
      "targetId": "target-instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Perform a PITR using the backup vault

If your Cloud SQL instance is enabled to use [enhanced backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#enhanced-backups), then you can perform point-in-time-recovery for your instance using the backup vault.

**Note:** If you're using Terraform or the Cloud SQL API to perform PITR and your instance uses enhanced backups, then Cloud SQL uses the PITR settings from the instance's associated backup plan.

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Open the more actions menu ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png) for the instance you want to recover and click **Create clone**.

  3. Select **Clone from an earlier point in time**.

  4. Enter a PITR time.

  5. Click **Create clone**.




###  gcloud 

To perform a PITR on an instance from the backup vault, you'll need to find the `data-source` for the backup that is nearest to the time you want to perform the PITR. To find the backup, see [List all the backups in the backup vault for an instance](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backing-up#list-backup-vault). Once you've identified the backup, run the following command to perform the PITR:
    
    
    gcloud sql instances point-in-time-restore DATA_SOURCE \
        TARGET_INSTANCE_NAME \
        'PITR_TIMESTAMP' \
        --project=TARGET_PROJECT \
        --region=REGION
    

Replace the following:

  * `DATA_SOURCE`: the path of the `data-source` for the source instance that is closest to the PITR timestamp you want to recover to.
  * `TARGET_INSTANCE_NAME`: the name for the new instance that is created by the PITR operation.
  * `PITR_TIMESTAMP`: the UTC timestamp for the source instance PITR log you want to restore your instance to, in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format. For example, 2025-11-15T16:19:00.094Z.
  * `TARGET_PROJECT`: the project ID for the new instance.
  * `REGION`: the region of the target instance. This field is required if the data source of the source instance is located in a multi-region. The target instance region must be the same as the region of the source instance.



###  REST v1 

To perform point-in-time recovery using a data source from the backup vault, use the [`instances.pointInTimeRestore`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/pointInTimeRestore) method with a POST request.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of the project where you want to create the new instance.
  * DATASOURCE: the Backup and DR data source you want the service to use for the point-in-time restore operation.
  * PITR_TIMESTAMP: the UTC timestamp for the source instance PITR log you want to restore your instance to, in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format. For example, 2012-11-15T16:19:00.094Z.
  * TARGET_INSTANCE_NAME: the name of the instance created by the PITR operation.
  * REGION: the region of the target instance. This field is required if the data source of source instance is located in a multi-region. The target instance region must be the same as the region of the source instance.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID:pointInTimeRestore

Request JSON body: 
    
    
    {
      "datasource": "DATASOURCE",
      "pointInTime": "PITR_TIMESTAMP",
      "targetInstanceName": "TARGET_INSTANCE_NAME",
      "region": "REGION"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID:pointInTimeRestore"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID:pointInTimeRestore" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CLONE",
      "name": "OPERATION_ID",
      "targetId": "TARGET_INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

To perform point-in-time recovery using a data source from the backup vault, use the [`instances.pointInTimeRestore`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/pointInTimeRestore) method with a POST request.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of the project where you want to create the new instance.
  * DATASOURCE: the Backup and DR data source you want the service to use for the point-in-time restore operation.
  * PITR_TIMESTAMP: the UTC timestamp for the source instance PITR log you want to restore your instance to, in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format. For example, 2012-11-15T16:19:00.094Z.
  * TARGET_INSTANCE_NAME: the name of the instance created by the PITR operation.
  * REGION: the region of the target instance. This field is required if the data source of source instance is located in a multi-region. The target instance region must be the same as the region of the source instance.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID:pointInTimeRestore

Request JSON body: 
    
    
    {
      "datasource": "DATASOURCE",
      "pointInTime": "PITR_TIMESTAMP",
      "targetInstanceName": "TARGET_INSTANCE_NAME",
      "region": "REGION"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID:pointInTimeRestore"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID:pointInTimeRestore" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CLONE",
      "name": "OPERATION_ID",
      "targetId": "TARGET_INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Perform a cross-project PITR

With enhanced backups, you can restore a Cloud SQL instance to a project other than the one where either the source instance or backup vault is located.

Cross-project PITR is supported only through the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and REST APIs.

To perform a cross-project PITR, do one of the following:

  * If you're using the gcloud CLI, set the `--project` flag to the project where you want to create the target instance.

  * If you're using REST APIs, set the `PROJECT_ID` field to the project where you want to create the target instance.




## Perform PITR on a deleted instance

To use PITR to restore a deleted instance, you'll need:

  * the PITR timestamp (`timestamp`) you want to restore your instance to
  * the target instance name
  * the time the source instance was deleted (`source-instance-deletion-time`)



You can use PITR on a deleted instance using gcloud CLI or the Cloud SQL API only. For more information, see [Restore a deleted instance using a PITR](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore#deleted-instance).

###  gcloud 

###  Standard backup 

**Find your PITR window**

To find your deleted instance's PITR window, get the earliest and latest recovery time for your instance. You can select anytime timestamp in this window to perform a PITR.

**Find source instance deletion**

The `source-instance-deletion-time` and `log-retention-days` for the deleted instance are stored with the retained backups for your instance after deletion. To find a list of all available backups for your deleted instance, see [List retained backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/manage-retained-backups#gcloud_1).

Once you identify the backup you want to use, use the [gcloud sql backups describe](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command to get the `source-instance-deletion-time`.

**Restore using a PITR**

To restore your deleted instance using a PITR, run the following command:
    
    
    gcloud sql instances clone SOURCE_INSTANCE_NAME \
    NEW_INSTANCE_NAME \
    --point-in-time='PITR_TIMESTAMP' \
    --source-instance-deletion-time=SOURCE_INSTANCE_DELETION_TIMESTAMP
    

Replace the following:

  * `SOURCE_INSTANCE_NAME`: the name of the source instance that you want to restore.
  * `NEW_INSTANCE_NAME`: the name of the new instance.
  * `PITR_TIMESTAMP`: the UTC timestamp for the source instance PITR log you want to restore your instance to, in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format. For example, 2012-11-15T16:19:00.094Z.
  * `SOURCE_INSTANCE_DELETION_TIMESTAMP`: the UTC timestamp for the time that the source instance was deleted, in RFC 3339 format. For example, 2012-11-15T16:19:00.094Z.



###  Enhanced backup 

**Find your PITR window**

To find your deleted instance's PITR window, get the earliest and latest recovery time for your instance. You can select anytime timestamp in this window to perform a PITR.

**Find the data source**

The data source for the deleted instance are stored with the retained backups for your instance after deletion. To find these values for your deleted instance, see [List all the backups in the backup vault for your instance](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/manage-enhanced-backups#list-backups).

**Restore using a PITR**

To restore your deleted instance using a PITR, run the following command:
    
    
    gcloud sql instances point-in-time-restore DATA_SOURCE \
        TARGET_INSTANCE_NAME \
        'PITR_TIMESTAMP' \
        --project=TARGET_PROJECT \
        --region=REGION
    

Replace the following:

  * `DATA_SOURCE`: the path of the `data-source` for the backup that is closest to the PITR timestamp you want to recover to.
  * `TARGET_INSTANCE_NAME`: the name for the new instance that is created by the PITR operation.
  * `PITR_TIMESTAMP`: the UTC timestamp for the source instance PITR log you want to restore your instance to, in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format. For example, 2025-11-15T16:19:00.094Z.
  * `TARGET_PROJECT`: the project ID for the new instance.
  * `REGION`: the region of the target instance. This field is required if the data source of the source instance is located in a multi-region. The target instance region must be the same as the region of the source instance.



###  REST v1 

**Find your PITR window**

To find your deleted instance's PITR window, get the earliest and latest recovery time for your instance. You can select anytime timestamp in this window to perform a PITR.

**Find source instance deletion time and log retention days**

The `source-instance-deletion-time` and `log-retention-days` for the deleted instance are stored with the retained backups for your instance after deletion. To find these values for your deleted instance, see [List retained backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/manage-retained-backups#rest-v1).

**Restore using a PITR**

Before using any of the request data, make the following replacements: 

  * project-id: the project ID
  * target-instance-id: the target instance ID
  * source-instance-id: the source instance ID
  * source-instance-deletion-time: the deletion time of the source instance
  * restore-timestamp the point-in-time which you want to restore the instance



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/source-instance-id/clone

Request JSON body: 
    
    
    {
      "cloneContext":
      {
        "kind": "sql#cloneContext",
        "destinationInstanceName": "target-instance-id",
        "sourceInstanceDeletionTime: "source-instance-deletion-time",
        "pointInTime": "restore-timestamp"
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/source-instance-id/clone"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/source-instance-id/clone" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CLONE",
      "name": "operation-id",
      "targetId": "target-instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

###  REST v1beta4 

**Find your PITR window**

To find your deleted instance's PITR window, get the earliest and latest recovery time for your instance. You can select anytime timestamp in this window to perform PITR.

**Find source instance deletion time and log retention days**

The `source-instance-deletion-time` and `log-retention-days` for the deleted instance are stored with the retained backups for your instance after deletion. To find these values for your deleted instance, see [List retained backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/manage-retained-backups#rest-v1beta4).

**Restore using PITR**

Before using any of the request data, make the following replacements: 

  * project-id: the project ID
  * target-instance-id: the target instance ID
  * source-instance-id: the source instance ID
  * source-instance-deletion-time: the deletion time of the source instance
  * restore-timestamp the point-in-time which you want to restore the instance



In the JSON request, you optionally can specify up to one specific database name as the following: `"databaseNames": "my-database"`

HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/source-instance-id/clone

Request JSON body: 
    
    
    {
      "cloneContext":
      {
        "kind": "sql#cloneContext",
        "destinationInstanceName": "target-instance-id",
        "sourceInstanceDeletionTime: "source-instance-deletion-time",
        "pointInTime": "restore-timestamp"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/source-instance-id/clone"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/source-instance-id/clone" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE",
      "name": "operation-id",
      "targetId": "target-instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Get the earliest and latest recovery time

For an available instance, you can perform a PITR to any timestamp in the instance's PITR window. The PITR window starts a the earliest recovery time and ends at the latest recovery time. If the instance is unavailable and the instance logs are stored in [Cloud Storage](https://docs.cloud.google.com/storage/docs), or the instance was deleted and had [PITR retention enabled](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore#deleted-instance), then you can retrieve the earliest and latest recovery time, and perform the PITR to any timestamp in that window. In all cases, you can restore the instance to a different primary or secondary zone by providing values for the preferred zones.

###  gcloud 

**Unavailable instance**

To get the earliest and latest time to which you can recover a Cloud SQL instance that's not available, run the following command:
    
    
    gcloud sql instances get-latest-recovery-time INSTANCE_NAME
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance you want to find the latest recovery time for.



**Deleted instance**

To get the earliest and latest time to which you can recover a Cloud SQL deleted instance to, run the following command:
    
    
    gcloud sql instances get-latest-recovery-time INSTANCE_NAME \
        --source-instance-deletion-time='SOURCE_INSTANCE_DELETION_TIMESTAMP'
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance you want to find the latest recovery time for.
  * `SOURCE_INSTANCE_DELETION_TIMESTAMP`: the UTC timestamp for the time that the source instance was deleted, in RFC 3339 format. For example, 2012-11-15T16:19:00.094Z.



###  REST v1 

**Unavailable instance**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_NAME: the name of the instance for which you're querying for the latest recovery time



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#getLatestRecoveryTime",
      "earliestRecoveryTime": "2023-06-10T17:23:59.648821586Z",
      "latestRecoveryTime": "2023-06-20T17:23:59.648821586Z"
    }
    

**Deleted instance**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_NAME: the name of the source instance for which you're querying for the latest recovery time
  * SOURCE_INSTANCE_DELETION_TIME: the time that the source instance was deleted



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#getLatestRecoveryTime",
      "earliestRecoveryTime": "2023-06-10T17:23:59.648821586Z",
      "latestRecoveryTime": "2023-06-20T17:23:59.648821586Z"
    }
    

###  REST v1beta4 

**Unavailable instance**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_NAME: the name of the instance for which you're querying for the latest recovery time



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#getLatestRecoveryTime",
      "earliestRecoveryTime": "2023-06-10T17:23:59.648821586Z",
      "latestRecoveryTime": "2023-06-20T17:23:59.648821586Z"
    }
    

**Deleted instance**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_NAME: the name of the source instance for which you're querying for the latest recovery time
  * SOURCE_INSTANCE_DELETION_TIME: the time that the source instance was deleted



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/getLatestRecoveryTime" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#getLatestRecoveryTime",
      "earliestRecoveryTime": "2023-06-10T17:23:59.648821586Z",
      "latestRecoveryTime": "2023-06-20T17:23:59.648821586Z"
    }
    

## Troubleshoot

Issue | Troubleshooting |  `argument --point-in-time: Failed to parse date/time:  
Unknown string format: 2021-0928T30:54:03.094;  
received: 2021-0928T30:54:03.094Z` OR `Invalid value at 'body.clone_context.point_in_time'  
(type.googleapis.com/google.protobuf.Timestamp), Field 'pointInTime',  
Invalid time format: Failed to parse input,` | The timestamp you provided is invalid.  
---|---  
`HTTP Error 400: Successful backup required for carrying out the operation was not found.` OR `Successful backup required for carrying out the operation was not found. or Time where no backups can be found.` | The timestamp that you provided is for a time where backups or when binlog coordinates could not be found.  
  
## What's next

  * [Configure flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags) on your clone



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
