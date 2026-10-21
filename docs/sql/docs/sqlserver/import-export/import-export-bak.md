---
url: https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak/
title: Export and import using BAK files and transaction log files \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:33.974495+00:00
---

# Export and import using BAK files and transaction log files  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Export and import using BAK files and transaction log files Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes exporting and importing data into Cloud SQL instances using BAK files and importing data into Cloud SQL instances using transaction log files.

**Note:** In Cloud SQL, SQL Server currently supports the export of native BAK files. If you're exporting to create a new instance from the exported file, consider [ restoring from a backup to a different instance](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restoring#restorebackups-another-instance) or [cloning the instance](https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance).

**WARNING!** Don't use a BAK file created from a read-only database or from a database that is in single-user mode. If you import a BAK file created from a read-only database or from a database that's in single-user mode, then an error might occur.

## Before you begin

**Important:** Before starting a large export, ensure that at least 25 percent of the database size is free (on the instance). Doing so helps prevent issues with aggressive autogrowth, which can affect the availability of the instance.

Exports use database resources, but exports don't interfere with normal database operations unless the instance is under-provisioned.

For best practices, see [Best Practices for Importing and Exporting Data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export).

After completing an import operation, [verify](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#verify) the results.

## Export data from Cloud SQL for SQL Server

Cloud SQL supports the export of built-in BAK files.

If you aim to create a new instance from an exported file, then consider [ restoring from a backup to a different instance](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restoring#restorebackups-another-instance) or [cloning the instance](https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance).

Cloud SQL performs a [full backup](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/full-database-backups-sql-server?view=sql-server-ver15) of the selected database during an export operation.

**Note:** For information about striped export, see Use striped export.

### Required roles and permissions for exporting from Cloud SQL for SQL Server

To export data from Cloud SQL into Cloud Storage, the user initiating the export must have one of the following roles:

  * The [Cloud SQL Editor](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles) role 
  * A [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), including the following permissions: 
    * `cloudsql.instances.get`
    * `cloudsql.instances.export`



Additionally, the service account for the Cloud SQL instance must have one of the following roles:

  * The `storage.objectAdmin` Identity and Access Management (IAM) role
  * A custom role, including the following permissions: 
    * `storage.objects.create`
    * `storage.objects.list` (for striped export and transaction log export)
    * `storage.objects.delete` (for striped export and transaction log export)
    * `storage.buckets.get` (for transaction log export only)



For help with IAM roles, see [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

**Note** : The changes that you make to the IAM permissions and roles might take a few minutes to take effect. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

### Export data to a BAK file from Cloud SQL for SQL Server

**Note:** You can't export a [database snapshot](https://docs.microsoft.com/en-us/sql/relational-databases/databases/database-snapshots-sql-server) to a BAK file.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Export**.
  4. In the **File format** section, click **BAK**.
  5. In the **Data to export** section, use the drop-down menu to select the database you want to export from.
  6. In the **Destination** section, select **Browse** to search for a Cloud Storage bucket or folder for your export.
  7. Click **Export** to begin the export.



### gcloud

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Find the service account for the Cloud SQL instance you're exporting from. You can do this running the `gcloud sql instances describe` command. Look for the `serviceAccountEmailAddress` field in the output. 
         
         gcloud sql instances describe INSTANCE_NAME
           

  3. Use `[ gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account. For more information about setting IAM permissions, see [ Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. Export the database: 
         
         gcloud sql export bak INSTANCE_NAME gs://BUCKET_NAME/FILENAME \
         --database=DATABASE_NAME
           

For information about using the `gcloud sql export bak` command, see the [ command reference page](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/export/bak).

  5. If you don't need to retain the IAM role you set previously, then [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it now.



### REST v1

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the export. 
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME

This step isn't required, but strongly recommended, so you don't open up access to any other data.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export your database: 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BUCKET_NAME: the Cloud Storage bucket name
     * PATH_TO_DUMP_FILE: the path to the SQL dump file
     * DATABASE_NAME_1: the name of a database inside the Cloud SQL instance
     * DATABASE_NAME_2: the name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/export

Request JSON body: 
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/export"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  4. If you don't need to retain the IAM role you set previously, then remove it now. 

For the complete list of parameters for the request, see the [instances:export](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/export) page. 

### REST v1beta4

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the export. 
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME
         

This step isn't required, but strongly recommended, so you don't open up access to any other data.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export your database: 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BUCKET_NAME: the Cloud Storage bucket name
     * PATH_TO_DUMP_FILE: the path to the SQL dump file
     * DATABASE_NAME_1: the name of a database inside the Cloud SQL instance
     * DATABASE_NAME_2: the name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/export

Request JSON body: 
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/export"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  4. If you don't need to retain the IAM role you set previously, then [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it now.

For the complete list of parameters for the request, see the [instances:export](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/export) page. 

### Export differential database backups

Before exporting a [differential database backup](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/differential-backups-sql-server?view=sql-server-ver16), you must export a differential base.

If other services or features, such as point-in-time recovery and read replica, trigger a full backup between your full backup export and differential backup export, then you must trigger a full backup export again.

To understand this better, consider the following example:

  1. You raise a full backup request at 7:00 AM.
  2. You enable point-in-time recovery at 9:00 AM. This triggers a full backup on your instance.
  3. You try to take a differential backup at 5:00 PM. This export request fails with an error message because the last full backup was triggered by point-in-time recovery.

**Note:** On an instance enabled with point-in-time recovery, Cloud SQL triggers a daily backup and this daily backup also triggers a full database backup. This means that on an instance enabled with point-in-time recovery, you have to take full backup and differential backup within two consecutive daily backups.   


Cloud SQL doesn't support database export requests with `--differential-base` or `--bak-type=DIFF` on replica instances.

### gcloud

  1. [ Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Find the service account for the Cloud SQL instance from which you're exporting. You can do this running the `gcloud sql instances describe` command. Look for the `serviceAccountEmailAddress` field in the output. 
         
         gcloud sql instances describe INSTANCE_NAME
           

  3. Use `[ gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account. For more information about setting IAM permissions, see [ Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. Export the database as the differential base.
         
         gcloud sql export bak INSTANCE_NAME gs://BUCKET_NAME/DIFFERENTIAL_BASE_FILENAME \
         --database=DATABASE_NAME --differential-base

For information about using the `gcloud sql export bak` command, see the [ command reference page](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/bak).

  5. Export a differential backup.
         
         gcloud sql export bak INSTANCE_NAME gs://BUCKET_NAME/DIFFERENTIAL_BACKUP_FILENAME \
         --database=DATABASE_NAME --bak-type=DIFF
           

For information about using the `gcloud sql export bak` command, see the [ command reference page](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/bak).

  6. If you don't need to retain the IAM role you set previously, then [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it now.



### REST v1

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the export. 
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME

This step isn't required, but strongly recommended, so you don't open up access to any other data.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export your full database backup as the differential base. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BUCKET_NAME: the Cloud Storage bucket name
     * PATH_TO_BAK_FILE: the path to the SQL BAK file
     * DATABASE_NAME: the name of the database inside of the Cloud SQL instance
     * `offload`: to enable and use serverless export, set this value to TRUE **Note:** Serverless export costs extra. See the [pricing page](https://docs.cloud.google.com/sql/pricing#storage-networking-prices).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/export

Request JSON body: 
    
    {
     "exportContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_BAK_FILE",
          "databases": ["DATABASE_NAME"]
          "offload": TRUE | FALSE
          "bakExportOptions": {
            "differentialBase":true
          }
       }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "EXPORT",
      "exportContext": {
        "uri": {uri},
        "databases": [
        DATABASE_NAME
        ],
        "kind": "sql#exportContext",
        "fileType": "BAK",
        "bakExportOptions": {
          "bakType": FULL,
          "differentialBase": true,
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  4. Export a differential backup. 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_dump_file: The path to the SQL dump fle
     * database_name_1: The name of a database inside the Cloud SQL instance
     * database_name_2: The name of a database inside the Cloud SQL instance
     * offload: Enables serverless export. Set to `true` to use serverless export. **Note:** Serverless export costs extra. See the [pricing page](https://docs.cloud.google.com/sql/pricing#storage-networking-prices).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/export

Request JSON body: 
    
    {
     "exportContext":
       {
          "fileType": "BAK",
          "uri": "gs://bucket_name/path_to_dump_file",
          "databases": ["database_name"]
          "offload": true | false
          "bakExportOptions": {
            bakType:"DIFF"
          }
    
        }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "EXPORT",
      "exportContext": {
        "uri": {uri},
        "databases": [
        database_name
        ],
        "kind": "sql#exportContext",
        "fileType": "BAK",
        "bakExportOptions": {
          "bakType": DIFF,
          "differentialBase": false,
        }
      },
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  5. If you don't need to retain the IAM role you set previously, then remove it now. 

For the complete list of parameters for the request, see the [instances:export](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/export) page. 

### REST v1beta4

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the export. 
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME
         

This step isn't required, but strongly recommended, so you don't open up access to any other data.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export your full database backup as the differential base. 

Before using any of the request data, make the following replacements: 

     * project-id: the project ID
     * instance-id: the instance ID
     * bucket_name: the Cloud Storage bucket name
     * path_to_dump_file: the path to the SQL dump fle
     * database_name_1: the name of a database inside the Cloud SQL instance
     * database_name_2: the name of a database inside the Cloud SQL instance
     * offload: to enable and use serverless export, set its value to `true`. **Note:** Serverless export costs extra. For more information, see the [pricing page](https://docs.cloud.google.com/sql/pricing#storage-networking-prices).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export

Request JSON body: 
    
    {
      "exportContext":
        {
           "fileType": "BAK",
           "uri": "gs://bucket_name/path_to_dump_file",
           "databases": ["database_name"]
           "offload": true | false
           "bakExportOptions": {
             "differentialBase":true
           }
    
         }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "EXPORT",
      "exportContext": {
        "uri": {uri},
        "databases": [
        database_name
        ],
        "kind": "sql#exportContext",
        "fileType": "BAK",
        "bakExportOptions": {
          "bakType": FULL,
          "differentialBase": true,
        }
      },
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  4. Export a differential backup: 

Before using any of the request data, make the following replacements: 

     * project-id: the project ID
     * instance-id: the instance ID
     * bucket_name: the Cloud Storage bucket name
     * path_to_dump_file: the path to the SQL dump fle
     * database_name_1: the name of a database inside the Cloud SQL instance
     * database_name_2: the name of a database inside the Cloud SQL instance
     * offload: to enable and use serverless exports, set this value to `true`. **Note:** Serverless export costs extra. For more information, see the [pricing page](https://docs.cloud.google.com/sql/pricing#storage-networking-prices).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export

Request JSON body: 
    
    {
      "exportContext":
        {
           "fileType": "BAK",
           "uri": "gs://bucket_name/path_to_dump_file",
           "databases": ["database_name"]
           "offload": true | false
           "bakExportOptions": {
            bakType:"DIFF"
           }
    
         }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "EXPORT",
      "exportContext": {
        "uri": {uri},
        "databases": [
        database_name
        ],
        "kind": "sql#exportContext",
        "fileType": "BAK",
        "bakExportOptions": {
          "bakType": DIFF,
          "differentialBase": false,
        }
      },
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  5. If you don't need to retain the IAM role you set previously, then [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it now.

For the complete list of parameters for the request, see the [instances:export](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/export) page. 

### Export transaction logs

You can export the transaction logs from Cloud SQL for SQL Server instances that use the [new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture), have [point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr) enabled, and have their logs stored in Cloud Storage.

### gcloud

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the export. 
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME

This step isn't required, but strongly recommended, so you don't open up access to any other data.

  2. Find the service account for the Cloud SQL instance from which you're exporting. You can do this by running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command. Look for the `serviceAccountEmailAddress` field in the output. 
         
         gcloud sql instances describe INSTANCE_NAME
           

  3. Use `[ gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.Admin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account. For more information about setting IAM permissions, see [ Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. Export the transaction logs.
         
         gcloud sql export bak INSTANCE_NAME gs://BUCKET_NAME/FOLDER_PATH
         --export-log-start-time=START_DATE_AND_TIME /
         --export-log-end-time=END_DATE_AND_TIME /
         --database=DATABASE_NAME --bak-type=TLOG
           

**Note:** The `export-log-start-time` and `export-log-end-time` parameters are optional. The values for these parameters must be in the [UTC](https://cdip.ucsd.edu/m/documents/timezones_and_units.html) time zone and have the [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. For example: 2024-05-26T16:19:00:094Z.

If you don't provide a start date and time and an end date and time for the parameters, then Cloud SQL exports all transaction logs within the log retention period in the Cloud Storage bucket. The log retention period can range from 1 to 35 days for Cloud SQL Enterprise Plus edition edition and 1 to 7 days for Cloud SQL Enterprise edition edition.

If you want to export transaction logs continually, then don't use the   
`--export-log-start-time` parameter and always export to the same location in Cloud Storage. Cloud SQL doesn't export any log files that already exist in the destination repeatedly.

For information about using the `gcloud sql export bak` command, see the [ command reference page](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/bak).

  5. If you don't need to retain the IAM role you set previously, then [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it now.



### REST

  1. [ Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)

This step isn't required, but strongly recommended, so you don't open up access to any other data.

  2. Provide your instance with the `storage.Admin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export the transaction logs. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID.
     * INSTANCE_ID: the instance ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * FOLDER_PATH: the path to the folder in the Cloud Storage bucket. Cloud SQL exports the transaction logs to this folder.
     * DATABASE_NAME: the name of the database inside of the Cloud SQL instance.
     * `exportLogStartTime`: the start date and time of the trasnasction logs to export.
     * `exportLogEndTime`: the end date and time of the transaction logs to export.

**Note:** The `exportLogStartTime` and `exportLogEndTime` parameters are optional. The values for these parameters must be in the [UTC](https://cdip.ucsd.edu/m/documents/timezones_and_units.html) time zone and have the [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. For example: 2024-05-26T16:19:00:094Z.

If you don't provide a start date and time and an end date and time for the parameters, then Cloud SQL exports all transaction logs in the Cloud Storage bucket.

If you want to export transaction logs continually, then don't use the   
`exportLogStartTime` parameter and always export to the same location in Cloud Storage. Cloud SQL doesn't export any log files that already exist in the destination repeatedly.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/export

Request JSON body: 
    
    {
     "exportContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/FOLDER_PATH",
          "databases": ["DATABASE_NAME"]
          "bakExportOptions": {
            bakType:"TLOG"
            exportLogStartTime: START_DATE_AND_TIME
            exportLogEndTime: END_DATE_AND_TIME
          }
       }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "EXPORT",
      "exportContext": {
        "uri": {uri},
        "databases": [
        DATABASE_NAME
        ],
        "kind": "sql#exportContext",
        "fileType": "BAK",
        "bakExportOptions": {
          "bakType": TLOG,
          "differentialBase": false,
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  4. If you don't need to retain the IAM role you set previously, then remove it now. 

For the complete list of parameters for the request, see the [instances.export](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/export) page. 

### Use striped export

The advantages of striped export are the following:

  * Reductions in the time needed for operations to complete
  * Databases larger than 5 TB can be exported



A potential disadvantage of using striped export is that the backup, rather than consisting of one file, is split across a set of files. This set is called a "stripe set"; see [Backup devices in a striped media set (a stripe set)](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-transact-sql?view=sql-server-ver16#backup-devices-in-a-striped-media-set-a-stripe-set). In Cloud SQL, you export to an empty folder in Cloud Storage instead of generating a single file. For more information, see How to use striped export.

#### Planning your operations

Striped export can improve the performance of exports. However, if your use case requires a single output file, or if your database is less than 5 TB in size, and if faster performance isn't critical, you may want to use a non-striped export.

If you decide to use striped export, then consider the number of stripes. You can specify this value in your gcloud CLI command or REST API call. However, if you want an optimal number of stripes for performance, or if you don't know a number, omit the number. An optimal number of stripes is set automatically.

The maximum number of stripes currently supported by Cloud SQL for SQL Server is 64.

#### How to use striped export

### gcloud

  1. [ Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Find the service account for the Cloud SQL instance you're exporting from. You can do this by running the `gcloud sql instances describe` command. Look for the `serviceAccountEmailAddress` field in the output. 
         
         gcloud sql instances describe INSTANCE_NAME
           

  3. Use `[ gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account. For more information about setting IAM permissions, see [ Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. To export the database, specify the `--striped` parameter and/or specify a value for `--stripe_count`. Setting a value for `--stripe_count` implies that the `--striped` parameter is intended. An error occurs if you specify `--no-striped` but specify a value for `--stripe_count`: 
         
         gcloud beta sql export bak INSTANCE_NAME \
         gs://BUCKET_NAME/STRIPED_EXPORT_FOLDER \
         --database=DATABASE_NAME --striped --stripe_count=NUMBER
           

For information about using the `gcloud beta sql export bak` command, see the [ command reference page](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/export/bak).

  5. If you don't need to retain the IAM role you set previously, then [ revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it now.



### REST v1

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the export. 
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME

This step isn't required, but strongly recommended, so you don't open up access to any other data.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).
  3. Export your database: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_folder: The path to the folder (in the Cloud Storage bucket) to which to export the striped set to
     * database_name: The name of a database in your Cloud SQL instance
     * true | false: Set to `true` to use striped export. If you specify `true` without specifying a stripe count, an optimal number of stripes is set automatically
     * number_of_stripes: The number of stripes to use. If specified, `striped` is implied as `true`

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/export

Request JSON body: 
    
    {
     "exportContext":
       {
          "fileType": "BAK",
          "uri": "gs://bucket_name/path_to_folder",
          "databases": ["database_name"],
          "bakExportOptions": {
            "striped": true | false,
            "stripe_count": ["number_of_stripes"]
          }
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/export"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2022-09-29T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  4. If you don't need to retain the IAM role you set previously, then remove it now. 

For the complete list of parameters for the request, see the [instances:export](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/export) page. 

### REST v1beta4

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the export. 
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME
         

This step isn't required, but is strongly recommended, so you don't open up access to any other data.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).
  3. Export your database: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_folder: The path to the folder (in the Cloud Storage bucket) to which to export the striped set
     * database_name: The name of a database in your Cloud SQL instance
     * true | false: Set to `true` to use striped export. If you specify `true` without specifying a stripe count, an optimal number of stripes is set automatically
     * number_of_stripes: The number of stripes to use. If specified, `striped` is implied as `true`

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export

Request JSON body: 
    
    {
     "exportContext":
       {
          "fileType": "BAK",
          "uri": "gs://bucket_name/path_to_folder",
          "databases": ["database_name"],
          "bakExportOptions": {
            "striped": true | false,
            "stripe_count": ["number_of_stripes"]
          }
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2022-09-29T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  4. If you don't need to retain the IAM role you set previously, then remove it now. 

For the complete list of parameters for the request, see the [instances:export](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/export) page. 

## Import to Cloud SQL for SQL Server

### Required roles and permissions for importing to Cloud SQL for SQL Server

To import data from Cloud Storage into Cloud SQL, the user initiating the import must have one of the following roles: 

  * The [Cloud SQL Admin](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles) role 
  * A [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), including the following permissions: 
    * `cloudsql.instances.get`
    * `cloudsql.instances.import`



Additionally, the service account for the Cloud SQL instance must have one of the following roles:

  * The `storage.objectAdmin` IAM role
  * A custom role, including the following permissions: 
    * `storage.objects.get`
    * `storage.objects.list` (for striped import only)



For help with IAM roles, see [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

**Note** : The changes that you make to the IAM permissions and roles might take a few minutes to take effect. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

### Import data from a BAK file to Cloud SQL for SQL Server

To use striped import, see Use striped import.

Various import frameworks are available. For example, Cloud SQL for SQL Server supports [ change data capture (CDC)](https://docs.cloud.google.com/sql/docs/sqlserver/replication/enable-cdc) for the following database versions:

  * SQL Server 2017 Standard
  * SQL Server 2017 Enterprise
  * SQL Server 2019 Standard
  * SQL Server 2019 Enterprise
  * SQL Server 2022 Standard
  * SQL Server 2022 Enterprise



When importing a CDC-enabled database, the [KEEP_CDC](https://docs.microsoft.com/en-us/sql/t-sql/statements/restore-statements-arguments-transact-sql?view=sql-server-ver15#change_data_capture_with_option) flag is retained.

**Note:** You can't import a database that was exported from a higher version of SQL Server or import from a higher compatibility level into a lower one. For example, if you exported a SQL Server 2017 version, you can't import it into a SQL Server 2014 version. 

If your instance version is a Microsoft SQL Server Enterprise Edition, then you can import encrypted BAK files.

Microsoft SQL Server Standard Edition instances also import encrypted BAK files, but only through gcloud CLI.

The only supported BAK extensions are `.bak` and `.bak.gz`. GPG encrypted backups are not currently supported.

For the instructions below, prepare to specify a new database; don't create a database before starting the import of your BAK file.

**Note:** Cloud SQL only supports importing a full backup with a single backup set. 

To import data to a Cloud SQL instance using a BAK file:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Import**.
  4. In the **Choose a file to import from** field, enter the path to the bucket and the BAK file to use for the import. 

You can import a compressed (`.gz`) or an uncompressed file.

  5. In the **File format** section, select **BAK**.

If you're importing data into a Cloud SQL Enterprise Plus edition instance, then you can import encrypted BAK files. Cloud SQL Enterprise edition instances also support importing encrypted BAK files, but only through the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To import an encrypted BAK file, do the following:

     1. Select **Encrypted BAK**.
     2. In the **Certificate** field, select the certificate that you want to import. This certificate is issued by a third-party certificate authority (CA).
     3. In the **Private key** field, select the file that contains the private key that you want to import. The _private_ key is used to encrypt and decrypt data that's sent from a source to a destination Cloud SQL instance.
     4. In the **Password** field, enter the password for the private key.
  6. In the **Destination** section, specify the database in your Cloud SQL instance where you want to import the BAK file.
  7. To start the import, click **Import**.



### gcloud

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the import.
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME

This step isn't required, but strongly recommended, so you don't open up access to any other data.

  2. Make sure you have configured the required roles and permissions.
  3. [Upload](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object) the data from the BAK file to the bucket.
  4. Describe the instance that you are importing to: 
         
         gcloud sql instances describe INSTANCE_NAME

  5. Copy the `serviceAccountEmailAddress` field.
  6. Use `[ gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectViewer` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account for the bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  7. Import the data from the file: 
         
         gcloud sql import bak INSTANCE_NAME gs://BUCKET_NAME/FILE_NAME \
         --database=DATABASE_NAME

For encrypted imports, use the following command: 
         
         gcloud sql import bak INSTANCE_NAME gs://BUCKET_NAME/FILE_NAME
         --database=DATABASE_NAME --cert-path=gs://BUCKET_NAME/CERTIFICATE_NAME
          --pvk-path=gs://BUCKET_NAME/KEY_NAME --prompt-for-pvk-password

  8. If you don't need to retain the IAM permissions you set previously, then remove them using [ `gcloud storage buckets remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding). 



### REST v1

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. Import the data from the file: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_bak_file: The path to the BAK file
     * database_name: The name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://bucket_name/path_to_bak_file",
          "database": "database_name"
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

To use a different user for the import, specify the `importContext.importUser` property. 

For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import) page. 
  5. If you don't need to retain the IAM permissions you set previously, then remove the permissions. 



### REST v1beta4

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [ Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. Import the data from the file: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_bak_file: The path to the BAK file
     * database_name: The name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://bucket_name/path_to_bak_file",
          "database": "database_name"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

To use a different user for the import, specify the `importContext.importUser` property. 

For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import) page. 
  5. If you don't need to retain the IAM permissions you set previously, then remove the permissions. 



If you get an error such as `ERROR_RDBMS`, ensure the BAK file exists in the bucket and you have the correct permissions on the bucket. For help configuring access control in Cloud Storage, see [ Create and Manage Access Control Lists](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists).

### Import differential database backups

Before you import a [differential database backup](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/differential-backups-sql-server?view=sql-server-ver16), you need a full backup import and your database must be in the `RESTORING` state after the full backup import.

Cloud SQL doesn't support importing differential database backups on instances that are enabled with point-in-time recovery. This is because importing a database backup with `--no-recovery` is a prerequisite for importing differential database backups. Additionally, you can't enable point-in-time recovery on an instance if the database is in the `RESTORING` state. In the case of import failure, do one of the following to enable point-in-time recovery:

  * Bring the database that's in the `RESTORING` state online by using the `--recovery-only `flag.

  * Remove the database.




To import data to a Cloud SQL instance using a differential database backup, perform the following steps:

### gcloud

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the import.
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME

This step isn't mandatory, but we strongly recommend that you perform it so that you don't open up access to any other data.

  2. Make sure that you've configured the required roles and permissions.
  3. [Upload](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object) the data from the BAK file to the bucket.
  4. Describe the instance that you are importing to: 
         
         gcloud sql instances describe INSTANCE_NAME

  5. Copy the `serviceAccountEmailAddress` field.
  6. Use `[ gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectViewer` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account for the bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  7. Import a full backup with `--no-recovery`.
         
         gcloud sql import bak INSTANCE_NAME gs://BUCKET_NAME/DIFFERENTIAL_BASE_FILENAME \
         --database=DATABASE_NAME --bak-type=FULL --no-recovery

  8. Import a differential database backup.
         
         gcloud sql import bak INSTANCE_NAME gs://BUCKET_NAME/DIFFERENTIAL_BACKUP_FILENAME \
         --database=DATABASE_NAME --bak-type=DIFF --no-recovery

  9. After restoring all the backup files, use the `--recovery-only` flag to bring the imported database online from a `RESTORING` state. Users are strongly encouraged not to use [T-SQL](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recover-a-database-without-restoring-data-transact-sql?view=sql-server-ver16#recovery-only-database-restore) commands to bring the imported database online.
         
         gcloud sql import bak INSTANCE_NAME \
         --database=DATABASE_NAME --recovery-only

  10. If you don't need to retain the IAM permissions you set previously, then remove them using [ `gcloud storage buckets remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding). 



### REST v1

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
**Note** : In the following steps, specify the `importContext.importUser` property to use a different user for the import. For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import) page. 
  4. Import a full backup with `noRecovery`. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID.
     * INSTANCE_ID: the instance ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_BAK_FILE: the path to the BAK file.
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_BAK_FILE",
          "database": "DATABASE_NAME"
          "bakImportOptions": {
            "noRecovery": true,
            "bakType": "FULL",
          }
    
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": DATABASE_NAME,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "noRecovery": true,
          "bakType": FULL,
          "recoveryOnly": false
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  5. Import a differential database backup. 

Before using any of the request data, make the following replacements: 

     * project-id: the project ID
     * instance-id: the instance ID
     * bucket_name: the Cloud Storage bucket name
     * path_to_bak_file: the path to the BAK file
     * database_name: the name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://bucket_name/path_to_bak_file",
          "database": "database_name"
          "bakImportOptions": {
            "bakType": "DIFF",
            "noRecovery": true,
          }
    
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": database_name,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "noRecovery": false,
          "bakType": DIFF,
          "recoveryOnly": false
        }
      },
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  6. After restoring all the backup files, use the `recoveryOnly` flag to bring the imported database online from a `RESTORING` state. Users are strongly encouraged not to use [T-SQL](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recover-a-database-without-restoring-data-transact-sql?view=sql-server-ver16#recovery-only-database-restore) commands to bring the imported database online.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BUCKET_NAME: the Cloud Storage bucket name
     * PATH_TO_BAK_FILE: the path to the BAK file
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_BAK_FILE",
          "database": "DATABASE_NAME"
          "bakImportOptions": {
            "recoveryOnly": true,
          }
    
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET-INSTANCE_ID",
      "status": "PENDING",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": DATABASE_NAME,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "recoveryOnly": true
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  7. If you don't need to retain the IAM permissions you set previously, then remove the permissions. 



### REST v1beta4

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [ Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
**Note** : In the following steps, specify the `importContext.importUser` property to use a different user for the import. For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import) page. 
  4. Import a full backup with`noRecovery`. 

Before using any of the request data, make the following replacements: 

     * PROJECT-ID: the project ID.
     * INSTANCE_ID: the instance ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_BAK_FILE: the path to the BAK file.
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_ID/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_BAK_FILE",
          "database": "DATABASE_NAME"
          "bakImportOptions": {
            "noRecovery": true,
            "bakType": "FULL",
          }
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_ID/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_ID/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": DATABASE_NAME,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "noRecovery": true,
          "bakType": FULL,
          "recoveryOnly": false
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/operations/operation-id",
      "targetProject": "PROJECT-ID"
    }
    

  5. Import a differential database backup. 

Before using any of the request data, make the following replacements: 

     * project-id: the project ID
     * instance-id: the instance ID
     * bucket_name: the Cloud Storage bucket name
     * path_to_bak_file: the path to the BAK file
     * database_name: the name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://bucket_name/path_to_bak_file",
          "database": "database_name"
          "bakImportOptions": {
            "bakType": "DIFF",
            "noRecovery": true,
          }
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": database_name,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "noRecovery": false,
          "bakType": DIFF,
          "recoveryOnly": false
        }
      },
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  6. After restoring all the backup files, use the `recoveryOnly` flag to bring the imported database online from a `RESTORING` state. Users are strongly encouraged not to use [T-SQL](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recover-a-database-without-restoring-data-transact-sql?view=sql-server-ver16#recovery-only-database-restore) commands to bring the imported database online.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BUCKET_NAME: the Cloud Storage bucket name
     * PATH_TO_BAK_FILE: the path to the BAK file
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_BAK_FILE",
          "database": "DATABASE_NAME"
          "bakImportOptions": {
            "recoveryOnly": true,
          }
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": DATABASE_NAME,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "recoveryOnly": true
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  7. If you don't need to retain the IAM permissions you set previously, remove the permissions. 



If you get an error such as `ERROR_RDBMS`, then ensure that the BAK file exists in the bucket and you have the correct permissions on the bucket. For help configuring access control in Cloud Storage, see [ Create and Manage Access Control Lists](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists).

### Import transaction log backups

A [transaction log](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver16#Characteristics) is a record of your database's transactions and the modifications made by each transaction. You can use it to re-establish database consistency in the event of a system failure.

**Note** : 

  * Cloud SQL doesn't support striped import of transaction log backups.
  * Cloud SQL doesn't support importing transaction log backups on instances that are enabled with point-in-time recovery. This is because importing a database backup with `--no-recovery` is a prerequisite for importing transaction log backups. Additionally, you can't enable point-in-time recovery on an instance if the database is in the `RESTORING` state. In the case of import failure, do one of the following to enable point-in-time recovery: 
    * Bring the database that's in the `RESTORING` state online by using the `--recovery-only `flag.
    * Remove the database.



To import data to a Cloud SQL instance using a transaction log backup, perform the following steps:

### gcloud

  1. [ Optional: Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the import.
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME

  2. [Upload](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object) the backup files to the bucket.
  3. Describe the instance that you are importing to: 
         
         gcloud sql instances describe INSTANCE_NAME

  4. Copy the `serviceAccountEmailAddress` field.
  5. Use `[ gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectViewer` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account for the bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  6. Import a full backup using the `--no-recovery` parameter. Ensure that your database is in the `RESTORING` state after the full backup import.
         
         gcloud sql import bak INSTANCE_NAME gs://BUCKET_NAME/BACKUP_FILENAME \
         --database=DATABASE_NAME --bak-type=FULL --no-recovery

  7. Optional: [Import a differential backup](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#import_diff). 
  8. Import a transaction log backup. 
         
         gcloud sql import bak INSTANCE_NAME gs://BUCKET_NAME/BACKUP_FILENAME \
         --database=DATABASE_NAME --bak-type=TLOG
         --stop-at=STOP_AT_TIMESTAMP --stop-at-mark=STOP_AT_MARK_NAME
         --no-recovery

Replace the following: 
     * INSTANCE_NAME: the instance name.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * BACKUP_FILENAME: the name of your backup file.
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance.
     * STOP_AT_TIMESTAMP: the timestamp at which the transaction log import must stop. This is an optional field and the value must use the [RFC 3339 format](https://www.ietf.org/rfc/rfc3339.txt).
     * STOP_AT_MARK_NAME: the [ marked transaction](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/use-marked-transactions-to-recover-related-databases-consistently?view=sql-server-ver16) at which the transaction log import must stop. This is an optional field and can take any string as its value. If the value is in the format `lsn:log-sequence-number`, then the transaction log import stops at the given [ log sequence number](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recover-to-a-log-sequence-number-sql-server?view=sql-server-ver16#LSNs). 
Repeat this step until all transaction log backups are imported. 
  9. After restoring all the backup files, use the `--recovery-only` flag to bring the imported database online from a `RESTORING` state. Users are strongly encouraged not to use [T-SQL](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recover-a-database-without-restoring-data-transact-sql?view=sql-server-ver16#recovery-only-database-restore) commands to bring the imported database online.
         
         gcloud sql import bak INSTANCE_NAME \
         --database=DATABASE_NAME --recovery-only

  10. If you don't need to retain the IAM permissions you set previously, then remove them using [ `gcloud storage buckets remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding). 



### REST v1

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import) page. 
  4. Import a full backup with `noRecovery`. Ensure that your database is in the `RESTORING` state after the full backup import. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID.
     * INSTANCE_ID: the instance ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_BAK_FILE: the path to the BAK file.
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_BAK_FILE",
          "database": "DATABASE_NAME"
          "bakImportOptions": {
            "noRecovery": true,
            "bakType": "FULL",
          }
    
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": DATABASE_NAME,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "noRecovery": true,
          "bakType": FULL,
          "recoveryOnly": false
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  5. Optional: [Import a differential backup](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#import_diff-v1). 
  6. Import a transaction log backup. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID.
     * INSTANCE_ID: the instance ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_TLOG_FILE: the path to the transaction log file.
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance.
     * STOP_AT_TIMESTAMP: the timestamp at which the transaction log import must stop. This is an optional field and the value must use the [RFC 3339 format](https://www.ietf.org/rfc/rfc3339.txt).
     * STOP_AT_MARK_NAME: the [ marked transaction](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/use-marked-transactions-to-recover-related-databases-consistently?view=sql-server-ver16) at which the transaction log import must stop. This is an optional field and can take any string as its value. If the value is in the format `lsn:log-sequence-number`, then the transaction log import stops at the given [ log sequence number](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recover-to-a-log-sequence-number-sql-server?view=sql-server-ver16#LSNs). 

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_TLOG_FILE",
          "database": "DATABASE_NAME"
          "bakImportOptions": {
            "bakType": "TLOG",
            "stopAt": STOP_AT_TIMESTAMP,
            "stopAtMark": STOP_AT_MARK_NAME,
            "noRecovery": true,
          }
    
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": DATABASE_NAME,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "noRecovery": false,
          "bakType": TLOG,
          "recoveryOnly": false
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

Repeat this step until all transaction log backups are imported. 
  7. After restoring all the backup files, use the `recoveryOnly` flag to bring the imported database online from a `RESTORING` state. Users are strongly encouraged not to use [T-SQL](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recover-a-database-without-restoring-data-transact-sql?view=sql-server-ver16#recovery-only-database-restore) commands to bring the imported database online.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BUCKET_NAME: the Cloud Storage bucket name
     * PATH_TO_BAK_FILE: the path to the BAK file
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_BAK_FILE",
          "database": "DATABASE_NAME"
          "bakImportOptions": {
            "recoveryOnly": true,
          }
    
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET-INSTANCE_ID",
      "status": "PENDING",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": DATABASE_NAME,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "recoveryOnly": true
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  8. If you don't need to retain the IAM permissions you set previously, then remove the permissions. 



### REST v1beta4

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [ Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
**Note** : In the following steps, specify the `importContext.importUser` property to use a different user for the import. For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import) page. 
  4. Import a full backup with `noRecovery`. Ensure that your database is in the `RESTORING` state after the full backup import. 

Before using any of the request data, make the following replacements: 

     * PROJECT-ID: the project ID.
     * INSTANCE_ID: the instance ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_BAK_FILE: the path to the BAK file.
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_ID/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_BAK_FILE",
          "database": "DATABASE_NAME"
          "bakImportOptions": {
            "noRecovery": true,
            "bakType": "FULL",
          }
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_ID/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_ID/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": DATABASE_NAME,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "noRecovery": true,
          "bakType": FULL,
          "recoveryOnly": false
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/operations/operation-id",
      "targetProject": "PROJECT-ID"
    }
    

  5. Optional: [Import a differential backup](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#import_diff-v1beta4). 
  6. Import a transaction log backup. Here, `stopAt` and `stopAtMark` are optional fields. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID.
     * INSTANCE_ID: the instance ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_BAK_FILE: the path to the BAK file.
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance.
     * STOP_AT_TIMESTAMP: the timestamp at which the transaction log import must stop. This is an optional field and the value must use the [RFC 3339 format](https://www.ietf.org/rfc/rfc3339.txt).
     * STOP_AT_MARK_NAME: the [ marked transaction](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/use-marked-transactions-to-recover-related-databases-consistently?view=sql-server-ver16) at which the transaction log import must stop. This is an optional field and can take any string as its value. If the value is in the format `lsn:log-sequence-number`, then the transaction log import stops at the given [ log sequence number](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recover-to-a-log-sequence-number-sql-server?view=sql-server-ver16#LSNs). 

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_BAK_FILE",
          "database": "DATABASE_NAME"
          "bakImportOptions": {
            "bakType": "TLOG",
            "stopAt": STOP_AT_TIMESTAMP,
            "stopAtMark":STOP_AT_MARK_NAME,
            "noRecovery": true,
          }
    
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": DATABASE_NAME,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "noRecovery": false,
          "bakType": TLOG,
          "recoveryOnly": false
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

Repeat this step until all transaction log backups are imported. 
  7. After restoring all the backup files, use `recoveryOnly` to bring the imported database online.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BUCKET_NAME: the Cloud Storage bucket name
     * PATH_TO_BAK_FILE: the path to the BAK file
     * DATABASE_NAME: the name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://BUCKET_NAME/PATH_TO_BAK_FILE",
          "database": "DATABASE_NAME"
          "bakImportOptions": {
            "recoveryOnly": true,
          }
        }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "IMPORT",
      "importContext": {
        "uri": {uri},
        "database": DATABASE_NAME,
        "kind": "sql#importContext",
        "fileType": "BAK",
        "bakImportOptions": {
          "recoveryOnly": true
        }
      },
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  8. If you don't need to retain the IAM permissions you set previously, then remove the permissions. 



### Use striped import

The advantages of striped import are the following:

  * Reductions in the time needed for operations to complete
  * Databases larger than 5 TB can be imported

**Note:** Striped import does not support the import of encrypted columns.

A potential disadvantage of using striped import is that all of the files in the striped set (rather than a single file) must be uploaded to the same folder in your Cloud Storage bucket, before you perform the import.

#### Planning your operations

In most use cases, striped import enables better performance with no disadvantages. However, if you can't back up to a striped set from a given instance, or if your database is less than 5 TB, and if faster performance is not critical, you may want to use a non-striped import.

#### How to use striped import

### gcloud

  1. [ Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for the import.
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME

This step isn't required, but strongly recommended, so you don't open up access to any other data.

  2. Make sure you have configured the required IAM roles and permissions.
  3. [Create](https://docs.cloud.google.com/storage/docs/folders#tool) a new folder in your bucket.
  4. To import the database, [ upload](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object) the files of the striped set (of the database) to the new folder. Ensure that all the files are uploaded to the folder, and that the folder contains no extra files.
  5. Describe the instance you are exporting from: 
         
         gcloud sql instances describe INSTANCE_NAME

  6. Copy the `serviceAccountEmailAddress` field.
  7. Use `[ gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectViewer` [ IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account for the bucket. For more information about setting IAM permissions, see [ Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  8. Import the data from the folder. The difference from a non-striped import is the following: The URI links to the name of the folder to which the stripe set was uploaded, rather than to a single file, and you specify the `--striped` parameter: 
         
         gcloud beta sql import bak INSTANCE_NAME gs://BUCKET_NAME/FOLDER_NAME \
         --database=DATABASE_NAME --striped

  9. If you don't need to retain the IAM permissions you set previously, then remove them using [ `gcloud storage buckets remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding). 



### REST v1

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. Import the data from the file: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_folder: The path to the folder (in the Cloud Storage bucket) where the stripe set is located
     * database_name: The name of a database to create in your Cloud SQL instance
     * true | false: Set to `true` to use striped import

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://bucket_name/path_to_folder",
          "database": "database_name",
          "bakImportOptions": {
            "striped": true | false
          }
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2022-09-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

To use a different user for the import, specify the `importContext.importUser` property. 

For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import) page. 
  5. If you don't need to retain the IAM permissions you set previously, then remove the permissions. 



### REST v1beta4

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For more information about setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. Import the data from the file: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_folder: The path to the folder (in the Cloud Storage bucket) where the stripe set is located
     * database_name: The name of a database to create in your Cloud SQL instance
     * true | false: Set to `true` to use striped import

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "BAK",
          "uri": "gs://bucket_name/path_to_folder",
          "database": "database_name",
          "bakImportOptions": {
            "striped": true | false
          }
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2022-09-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

To use a different user for the import, specify the `importContext.importUser` property. 

For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import) page. 
  5. If you don't need to retain the IAM permissions you set previously, then remove the permissions. 



If you get an error such as `ERROR_RDBMS`, then ensure that the table exists. If the table exists, then confirm that you have the correct permissions on the bucket. For help configuring access control in Cloud Storage, see [ Create and Manage Access Control Lists](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists).

## What's next

  * Learn how to [check the status of import and export operations](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/checking-status-import-export).
  * Learn more about [best practices for importing and exporting data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export).
  * [Known issues for imports and exports](https://docs.cloud.google.com/sql/docs/sqlserver/known-issues#import-export).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
