---
url: https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-sql/
title: Export and import using SQL dump files \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:53.706347+00:00
---

# Export and import using SQL dump files  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Export and import using SQL dump files Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-sql "View this page for the SQL Server database engine")

This page describes exporting and importing data into Cloud SQL instances using SQL dump files.

**Note:** If you're migrating an entire database from a supported database server (on-premises, in AWS, or Cloud SQL) to a new Cloud SQL instance, you can use [Database Migration Service](https://docs.cloud.google.com/database-migration/docs) instead of exporting and then importing files. If you're exporting to create a new instance from the exported file, consider [ restoring from a backup to a different instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring#restorebackups-another-instance) or [cloning the instance](https://docs.cloud.google.com/sql/docs/postgres/clone-instance).

You can cancel the import of data into Cloud SQL instances and the export of data from the instances. This data is contained in SQL dump files. For more information about cancelling an import or export operation, see [Cancel the import and export of data](https://docs.cloud.google.com/sql/docs/postgres/import-export/cancel-import-export).

## Before you begin

**Important:** Before starting a large export, ensure that at least 25 percent of the database size is free (on the instance). Doing so helps prevent issues with aggressive autogrowth, which can affect the availability of the instance.

Exports use database resources, but they do not interfere with normal database operations unless the instance is under-provisioned.

For best practices, see [Best Practices for Importing and Exporting Data](https://docs.cloud.google.com/sql/docs/postgres/import-export).

After completing an import operation, [verify](https://docs.cloud.google.com/sql/docs/postgres/import-export#verify) the results.

## Export data from Cloud SQL for PostgreSQL

### Required roles and permissions for exporting from Cloud SQL for PostgreSQL

To export data from Cloud SQL into Cloud Storage, the user initiating the export must have one of the following roles:

  * The [Cloud SQL Editor](https://docs.cloud.google.com/sql/docs/postgres/iam-roles) role 
  * A [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), including the following permissions: 
    * `cloudsql.instances.get`
    * `cloudsql.instances.export`



Additionally, the service account for the Cloud SQL instance must have one of the following roles:

  * The `storage.objectAdmin` Identity and Access Management (IAM) role
  * A custom role, including the following permissions: 
    * `storage.objects.create`
    * `storage.objects.list` (for exporting files in parallel only)
    * `storage.objects.delete` (for exporting files in parallel only)



For help with IAM roles, see [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

**Note** : The changes that you make to the IAM permissions and roles might take a few minutes to take effect. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

### Export to a SQL dump file from Cloud SQL for PostgreSQL

When you use Cloud SQL to perform an export, whether from the Google Cloud console, the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the API, you are using the [`pg_dump`](https://www.postgresql.org/docs/current/static/app-pgdump.html) utility, with the options required to ensure that the resulting export file is valid for import back into Cloud SQL. 

If you plan to import your data into Cloud SQL, you must follow the instructions provided in [Exporting data from an external database server](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp#external-server) so that your SQL dump file is formatted correctly for Cloud SQL.

**Note:** If your data contains large objects (blobs), the export can consume a large amount of memory, impacting instance performance. For help, see [Known Issues](https://docs.cloud.google.com/sql/docs/postgres/known-issues#import-export).

To export data from a database on a Cloud SQL instance to a SQL dump file in a Cloud Storage bucket:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Export**.
  4. In the **File format** section, click **SQL** to create a SQL dump file.
  5. In the **Data to export** section, use the **Database** drop-down menu to select the database you want to export from.
  6. Optional: Select **Offload export to a temporary instance** to allow other operations to occur while the export is ongoing.
  7. In the **Destination** section, select **Browse** to search for a Cloud Storage bucket or folder for your export.
  8. Click **Export** to begin the export.



### gcloud

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Find the service account for the Cloud SQL instance you're exporting from. You can do this running the `gcloud sql instances describe` command. Look for the `serviceAccountEmailAddress` field in the output. 
         
         gcloud sql instances describe INSTANCE_NAME
           

  3. Use `[gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account. For help with setting IAM permissions, see [ Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. Export the database to your Cloud Storage bucket: 

**Note** : If you want to use serverless exports, then use the `offload` parameter. If you want to include the `DROP <object>` SQL statement that's required to drop (clean) database objects before you import them, then use the `clean` parameter. If you want to include the `IF EXISTS` SQL statement with each `DROP` statement that's produced by the `clean` parameter, then use the `if-exists` parameter.

Otherwise, remove these parameters from the following command.
         
         gcloud sql export sql INSTANCE_NAME gs://BUCKET_NAME/sqldumpfile.gz \
         --database=DATABASE_NAME \
         --offload
           

The `export sql` command does not contain triggers or stored procedures, but does contain views. To export triggers and/or stored procedures, use the [pg_dump](https://www.postgresql.org/docs/current/static/app-pgdump.html) tool. 

For more information about using the `export sql` command, see the [`sql export sql`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/sql) command reference page.

  5. If you do not need to retain the IAM role you set previously, [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it now.



### REST v1

  1. Create a bucket for the export: 
         
         gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_NAME --location=LOCATION_NAME

This step is not required, but strongly recommended, so you do not open up access to any other data.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export your database: 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BUCKET_NAME: the Cloud Storage bucket name
     * PATH_TO_DUMP_FILE: the path to the SQL dump file
     * DATABASE_NAME_1: the name of a database inside the Cloud SQL instance
     * DATABASE_NAME_2: the name of a database inside the Cloud SQL instance

**Note** : If you want to use serverless exports, then use the `offload` parameter. If you want to include the `DROP <object>` SQL statement that's required to drop (clean) database objects before you import them, then use the `clean` parameter. If you want to include the `IF EXISTS` SQL statement with each `DROP` statement that's produced by the `clean` parameter, then use the `ifExists` parameter.

To use these features, set the values of these parameters to `TRUE`. Otherwise, set their values to `FALSE`. 

Serverless exports costs extra. See the [pricing page](https://cloud.google.com/sql/pricing#storage-networking-prices).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/export

Request JSON body: 
    
    {
      "exportContext":
        {
           "fileType": "SQL",
           "uri": "gs://BUCKET_NAME/PATH_TO_DUMP_FILE",
           "databases": ["DATABASE_NAME"],
           "offload": TRUE | FALSE,
           "sqlExportOptions": {
            "clean": [TRUE|FALSE],
            "ifExists": [TRUE|FALSE]
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
    

  4. If you do not need to retain the IAM role you set previously, remove it now. 

For the complete list of parameters for the request, see the [instances:export](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/export) page. 

### REST v1beta4

  1. Create a bucket for the export: 
         
         gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_NAME --location=LOCATION_NAME
         

This step is not required, but strongly recommended, so you do not open up access to any other data.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export your database: 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BUCKET_NAME: the Cloud Storage bucket name
     * PATH_TO_DUMP_FILE: the path to the SQL dump file
     * DATABASE_NAME_1: the name of a database inside the Cloud SQL instance
     * DATABASE_NAME_2: the name of a database inside the Cloud SQL instance

**Note** : If you want to use serverless exports, then use the `offload` parameter. If you want to include the `DROP <object>` SQL statement that's required to drop (clean) database objects before you import them, then use the `clean` parameter. If you want to include the `IF EXISTS` SQL statement with each `DROP` statement that's produced by the `clean` parameter, then use the `ifExists` parameter.

To use these features, set the values of these parameters to `TRUE`. Otherwise, set their values to `FALSE`. 

Serverless exports costs extra. See the [pricing page](https://cloud.google.com/sql/pricing#storage-networking-prices).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/export

Request JSON body: 
    
    {
       "exportContext":
         {
            "fileType": "SQL",
            "uri": "gs://BUCKET_NAME/PATH_TO_DUMP_FILE",
            "databases": ["DATABASE_NAME"],
            "offload": TRUE | FALSE,
            "sqlExportOptions": {
             "clean": [TRUE|FALSE],
             "ifExists": [TRUE|FALSE]
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
    

  4. If you do not need to retain the IAM role you set previously, [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it now.

For the complete list of parameters for the request, see the [instances:export](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/export) page. 

## Import data to Cloud SQL for PostgreSQL

### Required roles and permissions for importing to Cloud SQL for PostgreSQL

To import data from Cloud Storage into Cloud SQL, the user initiating the import must have one of the following roles: 

  * The [Cloud SQL Admin](https://docs.cloud.google.com/sql/docs/postgres/iam-roles) role 
  * A [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), including the following permissions: 
    * `cloudsql.instances.get`
    * `cloudsql.instances.import`



Additionally, the service account for the Cloud SQL instance must have one of the following roles:

  * The `storage.objectAdmin` IAM role
  * A custom role, including the following permissions: 
    * `storage.objects.get`
    * `storage.objects.list` (for importing files in parallel only)



For help with IAM roles, see [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

**Note** : The changes that you make to the IAM permissions and roles might take a few minutes to take effect. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

### Import a SQL dump file to Cloud SQL for PostgreSQL

SQL files are plain text files with a sequence of SQL commands.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Import**.
  4. In the **File format** section, select **SQL**.
  5. In the **Select source file** section, enter the path to the bucket and SQL dump file to use for the import, browse to an existing file, or upload a local file. 

You can import a compressed (`.gz`) or an uncompressed (`.sql`) file.

  6. In the **Destination** section, select the database that you want the data to be imported into.

This causes Cloud SQL to run the `USE DATABASE` statement before the import.

If your SQL dump file includes a `USE DATABASE` statement, it overrides the database you set in the Google Cloud console.
  7. If you want to specify a user to perform the import, select the user.

If your import file contains statements that must be performed by a specific user, use this field to specify that user. 

  8. Click **Import** to start the import.



### gcloud

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  2. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Describe the instance you are importing to: 
         
         gcloud sql instances describe INSTANCE_NAME

  4. Copy the `serviceAccountEmailAddress` field.
  5. Use `[gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account for the bucket. 
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
           --member=serviceAccount:SERVICE-ACCOUNT \
           --role=roles/storage.objectAdmin
           

For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  6. Import the database: 
         
         gcloud sql import sql INSTANCE_NAME gs://BUCKET_NAME/IMPORT_FILE_NAME \
         --database=DATABASE_NAME

For information about using the `import sql` command, see the [`sql import sql`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/sql) command reference page.

If the command returns an error like `ERROR_RDBMS`, review the permissions; this error is often due to permissions issues.

  7. If you do not need to retain the IAM permissions you set previously, remove them using `[gcloud storage buckets remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding)`. 



### REST v1 

  1. Create a SQL dump file. The linked instructions set certain flags that make the dump file compatible with Cloud SQL. 

     * If you are importing data from an on-premises PostgreSQL server:
       1. Create a SQL dump file using the instructions in [Exporting data using pg_dump](https://docs.cloud.google.com/sql/docs/postgres/import-export/exporting#external-server).
       2. Create a bucket in Cloud Storage using the instructions in [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).
       3. Upload the SQL dump file to the Cloud Storage bucket using the procedure in [Upload objects](https://docs.cloud.google.com/storage/docs/uploading-objects).
  2. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  3. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  4. Provide your instance with the `storage.objectAdmin` and `objectViewer` [IAM roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).
  5. Import your dump file: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_sql_file: The path to the SQL file
     * database_name: The name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "SQL",
          "uri": "gs://bucket_name/path_to_sql_file",
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

For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/import) page. 
  6. If you do not need to retain the IAM permissions you set previously, remove them now. 



### REST v1beta4

  1. Create a SQL dump file. The linked instructions set certain flags that make the dump file compatible with Cloud SQL. 

     * If you are importing data from an on-premises PostgreSQL server:
       1. Create a SQL dump file using the instructions in [Exporting data using pg_dump](https://docs.cloud.google.com/sql/docs/postgres/import-export/exporting#external-server).
       2. Create a bucket in Cloud Storage using the instructions in [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).
       3. Upload the SQL dump file to the Cloud Storage bucket using the procedure in [Upload objects](https://docs.cloud.google.com/storage/docs/uploading-objects).
  2. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets)
  3. Upload the file to your bucket.

For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  4. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).
  5. Import your dump file: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * bucket_name: The Cloud Storage bucket name
     * path_to_sql_file: The path to the SQL file
     * database_name: The name of a database inside the Cloud SQL instance

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/import

Request JSON body: 
    
    {
     "importContext":
       {
          "fileType": "SQL",
          "uri": "gs://bucket_name/path_to_sql_file",
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

For the complete list of parameters for the request, see the [instances:import](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/import) page. 
  6. If you do not need to retain the IAM permissions you set previously, remove them now. 



## What's next

  * Learn how to [check the status of import and export operations](https://docs.cloud.google.com/sql/docs/postgres/import-export/checking-status-import-export).
  * Learn more about [best practices for importing and exporting data](https://docs.cloud.google.com/sql/docs/postgres/import-export).
  * Learn more about [Cloud Storage](https://docs.cloud.google.com/storage/docs).
  * [Known issues for imports and exports](https://docs.cloud.google.com/sql/docs/postgres/known-issues#import-export).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
