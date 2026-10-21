---
url: https://docs.cloud.google.com/alloydb/docs/export-sql-file/
title: Export a SQL file \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:22.699640+00:00
---

# Export a SQL file  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/export-sql-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Export a SQL file Stay organized with collections  Save and categorize content based on your preferences. 

To back up database schemas and data as a plain-text script of SQL statements, you can export data from AlloyDB for PostgreSQL clusters to a SQL dump file in a Cloud Storage bucket.

For information about migrating an entire database from a supported database server to a new AlloyDB instance, see [Migrate a database to AlloyDB by using Database Migration Service](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quickstart). If you're exporting because you want to create a new instance from the exported file, consider [restoring a cluster from a stored backup](https://docs.cloud.google.com/alloydb/docs/backup/restore).

You can cancel the export of data from AlloyDB for PostgreSQL clusters. For more information, see [Cancel an export operation](https://docs.cloud.google.com/alloydb/docs/cancel-export).

## Before you begin

  * Before you begin an export operation, keep in mind that export operations use database resources, but they don't interfere with standard database operations unless the instance is underprovisioned.
  * Inter-region data transfer charges apply when the target bucket is in a different region than the source cluster. For more information, see [AlloyDB for PostgreSQL pricing](https://docs.cloud.google.com/alloydb/pricing).
  * Compression is enabled if the object name ends with `.gz` extension. The object is then exported in `.gz` format to Cloud Storage.
  * Multiple export operations can run in parallel.



## Required roles and permissions for exporting from AlloyDB

To export data from AlloyDB into Cloud Storage, the user initiating the export must have one of the following Identity and Access Management (IAM) roles:

  * The [AlloyDB Admin](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions) (`roles/alloydb.admin`) role
  * A [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), including the following permissions: 
    * `alloydb.clusters.get`
    * `alloydb.clusters.export`



Additionally, the service account for the AlloyDB cluster must have one of the following roles on the Cloud Storage bucket:

  * The `storage.objectAdmin` or `storage.objectCreator` IAM role
  * A custom role, including the `storage.objects.create` permission



For help with IAM roles, see [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

## Export AlloyDB data to a SQL dump file

When you use AlloyDB to perform an export, whether from the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API, you are using the [`pg_dump`](https://www.postgresql.org/docs/current/static/app-pgdump.html) utility, with the options required to ensure that the resulting export file is valid for import back into AlloyDB.

**Note:** If your data contains large objects or blobs, the export can consume a large amount of memory, which can impact instance performance.

To export data from a database on a AlloyDB cluster to a SQL dump file in a Cloud Storage bucket, follow these steps:

###  gcloud 

  1. Ensure there's an existing Cloud Storage bucket to store the exported file, or [create a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Use [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the AlloyDB service account for the bucket. The format for the service account is as follows:
         
         service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

If you're exporting the file into an existing Cloud Storage bucket that you didn't create, you might need additional IAM permissions in order to grant roles on the bucket. For details, see [Required roles](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#required-roles-managed-buckets).

**Note:** If the Cloud Storage bucket already contains an object with the same name as the file being exported, granting a service account with the `storage.objectAdmin` role overwrites the existing object during the export operation. To avoid overwriting existing objects, grant a less privileged role such as `storage.objectCreator` to the service account.
  3. Export the database to your Cloud Storage bucket. The following lists options for exporting data in a SQL dump format:

     * `--async` (Optional): return immediately, without waiting for the operation in progress to complete.
     * `--tables` (Optional): tables to export from.
     * `--schema-only` (Optional): if set, export only the schema.
     * `--clean-target-objects` (Optional): if set, output commands to `DROP` all the dumped database objects prior to outputting the commands for creating them.
     * `--if-exist-target-objects` (Optional): if set, use `DROP ... IF EXISTS` commands to check for the object's existence before dropping it in `--clean-target-objects` mode.

To use these features, include these options in the `gcloud` command. If you want to export only object definitions (schema) and no data, use the `--schema-only` flag. To specify which tables are to be exported, use the `--tables=TABLE_NAMES` flag. You can specify comma-separated values of table names or wildcard patterns to specify multiple tables.

Otherwise, remove these parameters from the following command:
    
    gcloud alloydb clusters export CLUSTER_NAME \
      --region=REGION \
      --database=DATABASE_NAME \
      --gcs-uri="gs://BUCKET_NAME/OBJECT_NAME" \
      --tables=TABLE_NAMES \
      --schema-only \
      --clean-target-objects \
      --if-exist-target-objects \
      --sql

The `gcloud alloydb clusters export` command doesn't contain triggers or stored procedures, but it does contain views. To export triggers or stored procedures, use the [`pg_dump`](https://www.postgresql.org/docs/current/static/app-pgdump.html) utility.

For more information about using the `gcloud alloydb clusters export` command, see the [`gcloud alloydb clusters export`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/export) command reference page.

  4. If you don't need to retain the IAM role that you set previously, [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) the role.




###  REST v1 

  1. Ensure there's an existing Cloud Storage bucket to store the exported file, or create a new bucket:
         
         gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_NAME --location=LOCATION_NAME

  2. Use [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the AlloyDB service account for the bucket. The format for the service account is as follows:
         
         service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

If you're exporting the file into an existing Cloud Storage bucket that you didn't create, you might need additional IAM permissions in order to grant roles on the bucket. For details, see [Required roles](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#required-roles-managed-buckets).

**Note:** If the Cloud Storage bucket already contains an object with the same name as the file being exported, granting a service account with the `storage.objectAdmin` role overwrites the existing object during the export operation. To avoid overwriting existing objects, grant a less privileged role such as `storage.objectCreator` to the service account.
  3. Export your database.  


Use the following HTTP method and URL:
         
         POST https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID:export

Before you use any of the request data, make the following replacements:

     * PROJECT_ID: the project ID.
     * REGION: the region in which the AlloyDB cluster is deployed.
     * CLUSTER_ID: the cluster ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_SQL_FILE: the path to the SQL dump file.
     * DATABASE_NAME: the name of a database inside the AlloyDB instance.
     * TABLES: tables to export from.
     * SCHEMA_ONLY: if `true`, export only the schema.
     * CLEAN_TARGET_OBJECTS: if `true`, output commands to `DROP` all the dumped database objects prior to outputting the commands for creating them.
     * IF_EXIST_TARGET_OBJECTS: If `true`, use `DROP ... IF EXISTS` commands to check for the object's existence before dropping it in `clean_target_objects` mode.

To use these features, set the values of these parameters to `true`. Otherwise, set their values to `false`. If you want to export only object definitions (schema) and no data, use the `schema_only` flag. To specify which tables are to be exported, use the `tables` field. You can select multiple tables by providing a comma-separated list of table names or by writing wildcard characters in the pattern.

Request JSON body:
    
    {
      "gcs_destination": {
        "uri": "gs://BUCKET_NAME/PATH_TO_SQL_FILE"
      },
      "database": "DATABASE_NAME",
      "sql_export_options": {
        "schema_only": true,
        "tables": [
         "TABLE1",
         "TABLE2"
        ],
        "clean_target_objects": false,
        "if_exist_target_objects": true
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

The following command assumes that you are signed into the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs) which automatically signs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command: 
    
    curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             -d @request.json \
             "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID:export"
       

#### PowerShell (Windows)

The following command assumes that you are signed into the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command: 
    
    $cred = gcloud auth print-access-token
       $headers = @{ "Authorization" = "Bearer $cred" }
    
       Invoke-WebRequest `
         -Method POST `
         -Headers $headers `
         -ContentType: "application/json; charset=utf-8" `
         -InFile request.json `
       -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID:export"| Select-Object -Expand Content
       

You receive a JSON response similar to the following:

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.alloydb.v1.OperationMetadata",
        "createTime": "2024-09-17T06:05:31.244428646Z",
        "target": "projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID",
        "verb": "export",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

  4. If you don't need to retain the IAM role you set previously, remove it.




For the complete list of parameters for the request, see [`clusters.export`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/export).

## What's next

  * Learn how to [export a CSV file](https://docs.cloud.google.com/alloydb/docs/export-csv-file).
  * [Cancel a data export](https://docs.cloud.google.com/alloydb/docs/cancel-export).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
