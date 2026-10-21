---
url: https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-parallel/
title: Export and import files in parallel \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:42.271708+00:00
---

# Export and import files in parallel  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-parallel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Export and import files in parallel Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-parallel "View this page for the MySQL database engine") | PostgreSQL | SQL Server

This page describes exporting and importing files into Cloud SQL instances in parallel.

**Note:** If you're exporting because you want to create a new instance from the exported file, consider [ restoring from a backup to a different instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring#restorebackups-another-instance) or [cloning the instance](https://docs.cloud.google.com/sql/docs/postgres/clone-instance).

You can verify that the import or export operation for multiple files in parallel completed successfully by [checking the operation's status](https://docs.cloud.google.com/sql/docs/postgres/import-export/checking-status-import-export). You can also cancel the import of data into Cloud SQL instances and the export of data from the instances. For more information about cancelling an import or export operation, see [Cancel the import and export of data](https://docs.cloud.google.com/sql/docs/postgres/import-export/cancel-import-export).

## Before you begin

Before you begin an export or import operation:

  * Ensure that your database has adequate free space. 

Export and import operations use database resources, but they don't interfere with typical database operations unless the instance is under-provisioned.

**Important** : Before starting a large operation, ensure that at least 25 percent of the disk is free on the instance. Doing so helps prevent issues with aggressive autogrowth, which can adversely affect the availability of the instance.
  * Follow the [best practices for exporting and importing data.](https://docs.cloud.google.com/sql/docs/postgres/import-export)
  * After completing an import operation, [verify](https://docs.cloud.google.com/sql/docs/postgres/import-export#verify) the results.



## Export data from Cloud SQL for PostgreSQL to multiple files in parallel

The following sections contain information about exporting data from Cloud SQL for PostgreSQL to multiple files in parallel.

### Required roles and permissions for exporting data from Cloud SQL for PostgreSQL to multiple files in parallel

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

### Export data to multiple files in parallel

You can export data in parallel from multiple files that reside in Cloud SQL to Cloud Storage. The [`gcloud sql export`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/sql) function with the `-parallel` flag uses the [`pg_dump`](https://www.postgresql.org/docs/current/static/app-pgdump.html) utility with the `--jobs` option to export from multiple files. 

If you plan to import your data into Cloud SQL, then follow the instructions provided in [Exporting data from an external database server](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp#external-server) so that your files are formatted correctly for Cloud SQL.

Files exported in parallel from Cloud SQL are compressed twice. While you can import these files back into Cloud SQL without modifications, if you want to import the files to another database using the open-source `pg_dump` utility, you must first decompress the files.

**Note:** If your data contains large objects (blobs), then the export might consume a large amount of memory, impacting instance performance. For help, see [Issues with importing and exporting data](https://docs.cloud.google.com/sql/docs/postgres/known-issues#import-export).

### gcloud

To export data from Cloud SQL to multiple files in parallel, complete the following steps:

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets). 

**Note:** You don't have to create a folder in the bucket. If the folder doesn't exist, then Cloud SQL creates it for you as a part of the process of exporting multiple files in parallel. However, if the folder exists, then it must be empty or the export operation fails.

  2. To find the service account for the Cloud SQL instance that you're exporting files from, use the  
[`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command. 
         
         gcloud sql instances describe INSTANCE_NAME

Replace INSTANCE_NAME with the name of your Cloud SQL instance.

In the output, look for the value that's associated with the `serviceAccountEmailAddress` field.

  3. To grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account, use the `[gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` command. For help with setting IAM permissions, see [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  4. To export data from Cloud SQL to multiple files in parallel, use the [`gcloud sql export sql`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/sql) command: 
         
         gcloud sql export sql INSTANCE_NAME gs://BUCKET_NAME/BUCKET_PATH/FOLDER_NAME \
         --offload \
         --parallel \
         --threads=THREAD_NUMBER \
         --database=DATABASE_NAME \
         --table=TABLE_EXPRESSION
         

Make the following replacements:

     * INSTANCE_NAME: the name of the Cloud SQL instance from which you're exporting files in parallel.
     * BUCKET_NAME: the name of the Cloud Storage bucket.
     * BUCKET_PATH: the path to the bucket where the export files are stored.
     * FOLDER_NAME: the folder where the export files are stored.
     * THREAD_NUMBER: the number of threads that Cloud SQL uses to export files in parallel. For example, if you want to export three files at a time in parallel, then specify `3` as the value for this parameter.
     * DATABASE_NAME (optional): the name of the databases inside of the Cloud SQL instance from which the export is made. If you don't specify a database, then Cloud SQL exports all user databases from the instance. For more information, see Export an entire instance
     * TABLE_EXPRESSION: the tables to export from the specified database.
**Note:** If you want to use serverless exports for up to 2 threads, then use the `offload` parameter. If you want to export multiple files in parallel, then use the `parallel` parameter. Otherwise, remove these parameters from the command.

After the export completes, you should have files in a folder in the Cloud Storage bucket in the `pg_dump` directory format.

  5. If you don't need the IAM role that you set in Required roles and permissions for exporting from Cloud SQL for PostgreSQL, then [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it.



### REST v1

To export data from Cloud SQL to multiple files in parallel, complete the following steps:

  1. Create a Cloud Storage bucket: 
         
         gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_NAME --location=LOCATION_NAME
         

Make the following replacements: 
     * BUCKET_NAME: the name of the bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.
     * PROJECT_NAME: the name of the Google Cloud project that contains the Cloud Storage bucket you're creating. 
     * LOCATION_NAME: the location of the bucket where you want to store the files you're exporting. For example, `us-east1`.

**Note:** You don't have to create a folder in the bucket. If the folder doesn't exist, then Cloud SQL creates it for you as a part of the process of exporting multiple files in parallel. However, if the folder exists, then it must be empty or the export operation fails.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export data from Cloud SQL to multiple files in parallel: 

Before using any of the request data, make the following replacements: 

     * PROJECT_NAME: the name of the Google Cloud project that contains the Cloud Storage bucket you created.
     * INSTANCE_NAME: the name of the Cloud SQL instance from which you're exporting files in parallel. 
     * BUCKET_NAME: the name of the Cloud Storage bucket.
     * BUCKET_PATH: the path to the bucket where the export files are stored.
     * FOLDER_NAME: the folder where the export files are stored.
     * DATABASE_NAME: the name of the database inside of the Cloud SQL instance from which the export is made. If you want to export all user databases from the instance, remove this field from the request body.
     * THREAD_NUMBER: the number of threads that Cloud SQL uses to export files in parallel. For example, if you want to export three files at a time in parallel, then specify `3` as the value for this parameter.
**Note:** The `offload` parameter enables you to use serverless exports for up to 2 threads. The `parallel` parameter enables you to export multiple files in parallel. To use these features, set the values of these parameters to TRUE. Otherwise, set their values to FALSE.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/export

Request JSON body: 
    
    {
     "exportContext":
       {
          "fileType": "SQL",
          "uri": "gs://BUCKET_NAME/BUCKET_PATH/FOLDER_NAME",
          "databases": ["DATABASE_NAME"],
          "offload": [TRUE|FALSE],
          "sqlExportOptions": {
            "parallel": [TRUE|FALSE],
            "threads": [THREAD_NUMBER]
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/export"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/DESTINATION_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/operations/OPERATION_ID",
      "targetProject": "PROJECT_NAME"
    }
    

After the export completes, you should have files in a folder in the Cloud Storage bucket in the `pg_dump` directory format.

  4. If you don't need the IAM role that you set in Required roles and permissions for exporting from Cloud SQL for PostgreSQL, then [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it. 

For the complete list of parameters for the request, see the [Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/export) page. 

### REST v1beta4

To export data from Cloud SQL to multiple files in parallel, complete the following steps:

  1. Create a Cloud Storage bucket: 
         
         gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_NAME --location=LOCATION_NAME

Make the following replacements: 
     * BUCKET_NAME: the name of the bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.
     * PROJECT_NAME: the name of the Google Cloud project that contains the Cloud Storage bucket you're creating. 
     * LOCATION_NAME: the location of the bucket where you want to store the files you're exporting. For example, `us-east1`.

**Note:** You don't have to create a folder in the bucket. If the folder doesn't exist, then Cloud SQL creates it for you as a part of the process of exporting multiple files in parallel. However, if the folder exists, then it must be empty or the export operation fails.

  2. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  3. Export data from Cloud SQL to multiple files in parallel: 

Before using any of the request data, make the following replacements: 

     * PROJECT_NAME: the name of the Google Cloud project that contains the Cloud Storage bucket you created.
     * INSTANCE_NAME: the name of the Cloud SQL instance from which you're exporting files in parallel. 
     * BUCKET_NAME: the name of the Cloud Storage bucket.
     * BUCKET_PATH: the path to the bucket where the export files are stored.
     * FOLDER_NAME: the folder where the export files are stored.
     * DATABASE_NAME: the name of the database inside of the Cloud SQL instance from which the export is made. If you want to export all user databases from the instance, remove this field from the request body.
     * THREAD_NUMBER: the number of threads that Cloud SQL uses to export files in parallel. For example, if you want to export three files at a time in parallel, then specify `3` as the value for this parameter.
**Note:** The `offload` parameter enables you to use serverless exports for up to 2 threads. The `parallel` parameter enables you to export multiple files in parallel. To use these features, set the values of these parameters to TRUE. Otherwise, set their values to FALSE.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/export

Request JSON body: 
    
    {
     "exportContext":
       {
          "fileType": "SQL",
          "uri": "gs://BUCKET_NAME/BUCKET_PATH/FOLDER_NAME",
          "databases": ["DATABASE_NAME"],
          "offload": [TRUE|FALSE],
          "sqlExportOptions": {
            "parallel": [TRUE|FALSE],
            "threads": [THREAD_NUMBER]
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/export"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_NAME/instances/DESTINATION_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_NAME/operations/OPERATION_ID",
      "targetProject": "PROJECT_NAME"
    }
    

After the export completes, you should have files in a folder in the Cloud Storage bucket in the `pg_dump` directory format.

  4. If you don't need the IAM role that you set in Required roles and permissions for exporting from Cloud SQL for PostgreSQL, then [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it.

For the complete list of parameters for the request, see the [Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/export) page. 

### Export and import an entire instance

You can export or import all user databases in an entire instance using a directory-formatted, parallel export.

To export or import an entire instance, use the same commands as shown in the parallel export and parallel import sections, removing the `databases` or `database` field, respectively. If you don't specify a database, Cloud SQL runs a parallel export or import for all user databases in the instance. This excludes system databases and Cloud SQL databases used to manage internal operations.

In a directory-formatted parallel export to Cloud Storage, after the export successfully completes, the data associated with each database is stored in a subdirectory named for each database, similar to the following:
    
    
    gs://example-bucket/test-folder/
        |---- postgres/
        |    |---- 3929.dat.gz (table data file)
        |    |---- toc.dat (metadata file)
        |
        |---- second_database/
        |    |---- 3930.dat.gz
        |    |---- 3931.dat.gz
        |    |---- toc.dat

If you want to run a parallel import for an entire instance, and the instance's files were created outside of Cloud SQL, this subdirectory structure is required in order for the operation to successfully complete.

When the entire instance dump structure is detected, the import database specified in the API is ignored. The operation detects the entire instance's structure from the directory name.

You can't run an entire instance export or import for other file formats.

You can't export or import an entire instance as a single SQL file or CSV file.

## Import data from multiple files in parallel to Cloud SQL for PostgreSQL

The following sections contain information about importing data from multiple files in parallel to Cloud SQL for PostgreSQL.

### Required roles and permissions for importing data from multiple files in parallel to Cloud SQL for PostgreSQL

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

### Import data to Cloud SQL for PostgreSQL

You can import data in parallel from multiple files that reside in Cloud Storage to your database. To do this, use the [`pg_restore`](https://www.postgresql.org/docs/current/static/app-pgrestore.html) utility with the `--jobs` option.

**Note:** If your data contains large objects (blobs), then the import might consume a large amount of memory, impacting instance performance. For help, see [Issues with importing and exporting data](https://docs.cloud.google.com/sql/docs/postgres/known-issues#import-export).

### gcloud

To import data from multiple files in parallel into Cloud SQL, complete the following steps:

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Upload the files to your bucket.

**Note:** Make sure that the files that you're uploading are in the `pg_dump` directory format. For more information, see Export data from multiple files in parallel.

For help with uploading files to buckets, see [Upload objects from files](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. To find the service account for the Cloud SQL instance that you're importing files to, use the  
[`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command. 
         
         gcloud sql instances describe INSTANCE_NAME

Replace INSTANCE_NAME with the name of your Cloud SQL instance.

In the output, look for the value that's associated with the `serviceAccountEmailAddress` field.

  4. To grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account, use the `[gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` utility. For help with setting IAM permissions, see [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).
  5. To import data from multiple files in parallel into Cloud SQL, use the [`gcloud sql import sql`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/sql) command: 
         
         gcloud sql import sql INSTANCE_NAME gs://BUCKET_NAME/BUCKET_PATH/FOLDER_NAME \
         --parallel \
         --threads=THREAD_NUMBER \
         --database=DATABASE_NAME
         

Make the following replacements:

     * INSTANCE_NAME: the name of the Cloud SQL instance to which you're importing files in parallel.
     * BUCKET_NAME: the name of the Cloud Storage bucket.
     * BUCKET_PATH: the path to the bucket where the import files are stored.
     * FOLDER_NAME: the folder where the import files are stored.
     * THREAD_NUMBER: the number of threads that Cloud SQL uses to import files in parallel. For example, if you want to import three files at a time in parallel, then specify `3` as the value for this parameter.
     * DATABASE_NAME: the name of the database inside of the Cloud SQL instance from which the import is made. You must specify only one database.

**Note:** If you want to import multiple files in parallel, then use the `parallel` parameter.

If you use the `parallel` parameter, and you want to drop (clean) database objects before you recreate them, then use the `clean` parameter. If you use the `parallel` parameter, and you want to include the `IF EXISTS` SQL statement with each `DROP` statement that's produced by the `clean` parameter, then use the `if-exists` parameter.

Otherwise, remove these parameters from the command.

If the command returns an error like `ERROR_RDBMS`, then review the permissions; this error is often due to permissions issues.

  6. If you don't need the IAM permissions that you set in Required roles and permissions for importing to Cloud SQL for PostgreSQL, then use `[gcloud storage buckets remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding)` to remove them.



### REST v1 

To import data from multiple files in parallel into Cloud SQL, complete the following steps:

  1. Create a Cloud Storage bucket: 
         
         gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_NAME --location=LOCATION_NAME
         

Make the following replacements: 
     * BUCKET_NAME: the name of the bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.
     * PROJECT_NAME: the name of the Google Cloud project that contains the Cloud Storage bucket you're creating. 
     * LOCATION_NAME: the location of the bucket where you want to store the files you're importing. For example, `us-east1`.
  2. Upload the files to your bucket.

**Note:** Make sure that the files that you're uploading are in the `pg_dump` directory format. For more information, see Export data from multiple files in parallel.

For help with uploading files to buckets, see [Upload objects from files](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).
  4. Import data from multiple files in parallel into Cloud SQL:

Before using any of the request data, make the following replacements: 

     * PROJECT_NAME: the name of the Google Cloud project that contains the Cloud Storage bucket you created.
     * INSTANCE_NAME: the name of the Cloud SQL instance to which you're importing files in parallel. 
     * BUCKET_NAME: the name of the Cloud Storage bucket.
     * BUCKET_PATH: the path to the bucket where the import files are stored.
     * FOLDER_NAME: the folder where the import files are stored.
     * DATABASE_NAME: the name of the database inside of the Cloud SQL instance from which the import is made. You must specify only one database.
     * THREAD_NUMBER: the number of threads that Cloud SQL uses to import files in parallel. For example, if you want to import three files at a time in parallel, then specify `3` as the value for this parameter.

**Note:** The `offload` parameter enables you to use serverless imports for up to 2 threads. The `parallel` parameter enables you to import multiple files in parallel.

If you use the `parallel` parameter, then the `clean` parameter enables you to drop (clean) database objects before you recreate them. If you use the `parallel` parameter, then the `ifExists` parameter enables you to include the `IF EXISTS` SQL statement with each `DROP` statement that's produced by the `clean` parameter.

To use these features, set the values of these parameters to TRUE. Otherwise, set their values to FALSE.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/import

Request JSON body: 
    
    {
      "importContext":
        {
           "fileType": "SQL",
           "uri": "gs://BUCKET_NAME/BUCKET_PATH/FOLDER_NAME",
           "databases": ["DATABASE_NAME"],
           "offload": [TRUE|FALSE],
           "sqlImportOptions": {
             "parallel": [TRUE|FALSE],
             "clean": [TRUE|FALSE],
             "ifExists": [TRUE|FALSE],
             "threads": [THREAD_NUMBER]
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/import"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/DESTINATION_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/operations/OPERATION_ID",
      "targetProject": "PROJECT_NAME"
    }
    

To use a different user for the import, specify the `importContext.importUser` property. 

For the complete list of parameters for the request, see the [Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/import) page. 
  5. If you don't need the IAM permissions that you set in Required roles and permissions for importing to Cloud SQL for PostgreSQL, then use `[gcloud storage buckets remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding)` to remove them.



### REST v1beta4

To import data from multiple files in parallel into Cloud SQL, complete the following steps:

  1. Create a Cloud Storage bucket: 
         
         gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_NAME --location=LOCATION_NAME
         

Make the following replacements: 
     * BUCKET_NAME: the name of the bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.
     * PROJECT_NAME: the name of the Google Cloud project that contains the Cloud Storage bucket you're creating. 
     * LOCATION_NAME: the location of the bucket where you want to store the files you're importing. For example, `us-east1`.
  2. Upload the files to your bucket.

**Note:** Make sure that the files that you're uploading are in the `pg_dump` directory format. For more information, see Export data from multiple files in parallel.

For help with uploading files to buckets, see [Upload objects from files](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Provide your instance with the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for your bucket. For help with setting IAM permissions, see [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).
  4. Import data from multiple files in parallel into Cloud SQL:

Before using any of the request data, make the following replacements: 

     * PROJECT_NAME: the name of the Google Cloud project that contains the Cloud Storage bucket you created.
     * INSTANCE_NAME: the name of the Cloud SQL instance from which you're importing files in parallel. 
     * BUCKET_NAME: the name of the Cloud Storage bucket.
     * BUCKET_PATH: the path to the bucket where the import files are stored.
     * FOLDER_NAME: the folder where the import files are stored.
     * DATABASE_NAME: the name of the database inside of the Cloud SQL instance from which the import is made. You must specify only one database.
     * THREAD_NUMBER: the number of threads that Cloud SQL uses to import files in parallel. For example, if you want to import three files at a time in parallel, then specify `3` as the value for this parameter.

**Note:** The `offload` parameter enables you to use serverless imports for up to 2 threads. The `parallel` parameter enables you to import multiple files in parallel.

If you use the `parallel` parameter, then the `clean` parameter enables you to drop (clean) database objects before you recreate them. If you use the `parallel` parameter, then the `ifExists` parameter enables you to include the `IF EXISTS` SQL statement with each `DROP` statement that's produced by the `clean` parameter.

To use these features, set the values of these parameters to TRUE. Otherwise, set their values to FALSE.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/import

Request JSON body: 
    
    {
       "importContext":
         {
            "fileType": "SQL",
            "uri": "gs://BUCKET_NAME/BUCKET_PATH/FOLDER_NAME",
            "databases": ["DATABASE_NAME"],
            "offload": [TRUE|FALSE],
            "sqlImportOptions": {
              "parallel": [TRUE|FALSE],
              "clean": [TRUE|FALSE],
              "ifExists": [TRUE|FALSE],
              "threads": [THREAD_NUMBER]
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/import"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_NAME/instances/DESTINATION_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_NAME/operations/OPERATION_ID",
      "targetProject": "PROJECT_NAME"
    }
    

To use a different user for the import, specify the `importContext.importUser` property. 

For the complete list of parameters for the request, see the [Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/import) page. 
  5. If you don't need the IAM permissions that you set in Required roles and permissions for importing to Cloud SQL for PostgreSQL, then use `[gcloud storage buckets remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding)` to remove them.



## Limitations

  * If you specify too many threads when you import or export data from multiple files in parallel, then you might use more memory than your Cloud SQL instance has. If this occurs, then an internal error message appears. Check the memory usage of your instance and increase the instance's size, as needed. For more information, see [About instance settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings).

  * When performing an export, commas in database names or table names in the `databases` or `tables` fields aren't supported.

  * Make sure that you have enough disk space for the initial dump file download. Otherwise, a `no space left on disk` error appears.

  * If your instance has only one virtual CPU (vCPU), then you can't import or export multiple files in parallel. The number of vCPUs for your instance can't be smaller than the number of threads that you're using for the import or export operation, and the number of threads must be at least two.

  * Multi-threaded (parallel) imports and exports aren't compatible with single-threaded imports and exports. For example, dump files generated by a single-threaded export can only be imported by single-threaded imports. Similarly, dump files generated by parallel exports can only be imported by parallel imports.



  * The `pg_dump` utility can't chunk any tables that you export. Therefore, if you have one very large table, then it can become a bottleneck for the speed of the export operation.



## What's next

  * Learn how to [check the status of import and export operations](https://docs.cloud.google.com/sql/docs/postgres/import-export/checking-status-import-export).
  * Learn how to [cancel the import and export of data](https://docs.cloud.google.com/sql/docs/postgres/import-export/cancel-import-export).
  * Learn about [best practices for importing and exporting data](https://docs.cloud.google.com/sql/docs/postgres/import-export).
  * Learn about [known issues for imports and exports](https://docs.cloud.google.com/sql/docs/postgres/known-issues#import-export).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
