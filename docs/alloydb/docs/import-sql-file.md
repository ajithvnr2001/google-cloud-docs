---
url: https://docs.cloud.google.com/alloydb/docs/import-sql-file/
title: Import a SQL file \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:43.430687+00:00
---

# Import a SQL file  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/import-sql-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Import a SQL file Stay organized with collections  Save and categorize content based on your preferences. 

To reconstruct a database from a plain-text script of SQL commands, you can import a SQL file stored in a Cloud Storage bucket into an AlloyDB for PostgreSQL cluster.

**Note:** If you're migrating an entire database from a supported database server (on-premises, in AWS, or AlloyDB) to a new AlloyDB cluster, you can use [Database Migration Service](https://docs.cloud.google.com/database-migration/docs) instead of exporting and then importing files. If you're importing because you want to create a new cluster from the imported file, consider [restoring from a backup to a different cluster](https://docs.cloud.google.com/alloydb/docs/backup/restore).

You can cancel the import of data into AlloyDB clusters. For more information, see [Cancel an import operation](https://docs.cloud.google.com/alloydb/docs/cancel-import).

When importing SQL dump files, make sure that the PostgreSQL version from which the dump was created is compatible with your AlloyDB instance's PostgreSQL version. Importing a dump file from a higher version to a lower version might fail due to incompatible SQL syntax.

## Before you begin

Before you begin an import operation:

  * Ensure that your database has adequate storage quota.
  * Import operations use database resources, but they don't interfere with normal database operations unless the cluster is under-provisioned.



## Required roles and permissions for importing to AlloyDB

To import data from Cloud Storage into AlloyDB, the user initiating the import must have one of the following roles:

  * The [AlloyDB Admin](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions) role
  * A [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), including the following permissions: 
    * `alloydb.clusters.get`
    * `alloydb.clusters.import`



Additionally, the service account for the AlloyDB cluster must have one of the following roles:

  * The `storage.objectViewer` IAM role
  * A custom role, including the following permissions: 
    * `storage.objects.get`



For help with IAM roles, see [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

**Note:** The changes that you make to the IAM permissions and roles might take a few minutes to take effect. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Import a SQL file to AlloyDB clusters

To import data to an AlloyDB cluster using a SQL file, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster name to open the **Overview** page for that cluster.

  3. Click **Import**.

  4. In **File format** , select **SQL**.

  5. In **Select source file** , choose whether to upload files from your computer or select a file from a Cloud Storage location.

     1. To upload a file from your computer, do the following:

        1. Select **Upload files from your computer**.
        2. Click **Browse** next to **Select local file** to select a SQL file from your local machine.
        3. Click **Browse** next to **Select Cloud Storage location** to select a Cloud Storage location to store the uploaded local file.
        4. Click **Upload** to upload the file.
     2. To select a SQL file that exists in a Cloud Storage bucket, do the following:

        1. Select **Select file from Google Cloud Storage**.
        2. Click **Browse** next to **bucket-name/file-name** to select a SQL file from a Cloud Storage bucket.
  6. Select the database you want the data to be imported into from the **Database** drop-down menu.

If your SQL dump file includes a `\connect` (or `\c`) meta-command, it overrides the target database that you select in the Google Cloud console.

  7. Optional: To specify a user for the import operation, click **Show user options** and enter the username in the **User** field.

  8. To start the import operation, click **Import**.


**Note:** You can import a compressed `.gz` or uncompressed `.sql` file.

###  gcloud 

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Upload the SQL file to your bucket. For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

  3. Use [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) to grant the `storage.objectViewer` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the AlloyDB cluster service account for the bucket:
         
         service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com

For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

  4. Import the file:
         
         gcloud alloydb clusters import CLUSTER_NAME \
           --region=REGION \
           --database=DATABASE_NAME \
           --gcs-uri='gs://BUCKET_NAME/PATH_TO_SQL_FILE' \
           --user=USERNAME \
           --sql

**Note:** You can import a compressed (`.gz`) or an uncompressed (`.sql`) file.

Replace the following:

     * CLUSTER_NAME: the name of the cluster.
     * REGION: the region in which the AlloyDB cluster is deployed.
     * DATABASE_NAME: the name of a database inside the cluster.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_SQL_FILE: the path to the SQL file.
     * USERNAME: the user for the import operation.

If the command returns an error like `PERMISSION_DENIED`, review the permissions.

For information about using the `import` command, see the [`gcloud alloydb clusters import`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import) command reference page.

  5. If you don't need to keep the IAM permissions that you set previously, remove them using [`gcloud storage buckets remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding).




###  REST v1 

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Upload the SQL file to your bucket. For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).
  3. Use [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) to grant the `storage.objectViewer` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the AlloyDB cluster service account for the bucket. The format for the service account is as follows:
         
         service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com

For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

  4. Import your SQL file.

**Note:** You can import a compressed (`.gz`) or an uncompressed (`.sql`) file.

Use the following HTTP method and URL:
         
         POST https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID:import

Before you use any of the request data, make the following replacements:

     * PROJECT_ID: the project ID.
     * LOCATION_ID: the region in which the AlloyDB cluster is deployed.
     * CLUSTER_ID: the cluster ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_SQL_FILE: the path to the SQL file.
     * USER: the user to use for the import.
     * DATABASE_NAME: the name of a database inside the AlloyDB cluster.

Request JSON body:
    
    {
       "gcsUri": "gs://BUCKET_NAME/PATH_TO_SQL_FILE",
       "database": "DATABASE_NAME",
       "user": "USER",
       "sqlImportOptions": {}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

The following command assumes that you signed into the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             -d @request.json \
             "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID:import"
    

#### PowerShell (Windows)

The following command assumes that you signed into the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -InFile request.json `
      -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID:import"| Select-Object -Expand Content
    

You receive a JSON response similar to the following:

#### Response
    
    {
     "name": "projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID",
     "metadata": {
      "@type": "type.googleapis.com/google.cloud.alloydb.v1.OperationMetadata",
      "createTime": "2025-01-04T13:12:32.363393723Z",
      "target": "projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID",
      "verb": "import",
      "requestedCancellation": false,
      "apiVersion": "v1"
     },
     "done": false
    }
    

To use a different user for the import, specify the user property.

  5. If you don't need to retain the IAM permissions that you set previously, remove them.

For the complete list of parameters for the request, see [`clusters.import`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/import).




## Check the status of an import operation

To check the status of an import operation, follow these steps:

###  gcloud 

Run the following using the [`gcloud alloydb operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/describe) command:
    
    
    gcloud alloydb operations describe OPERATION_ID --region=REGION

You can also list details of a specific operation or cancel a specific operation. For more information about this command, see the [`gcloud alloydb operations`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations) command reference page.

###  REST v1 

Use the `GET` method and the following URL:
    
    
    GET https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID
    

For more information, see [`get`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.operations/get).

Before you use any of the request data, make the following replacements:

  * REGION: the region in which the AlloyDB cluster is deployed.
  * PROJECT_ID: the project ID.
  * OPERATION_ID: the ID of the import operation. For more information, see Before you begin.



To send your request, expand one of these options:

#### _curl (Linux, macOS, or Cloud Shell)_

The following command assumes that you signed into the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list).

Execute the following command:
    
    
      curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID
     

#### _PowerShell (Windows)_

The following command assumes that you signed into the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command:
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method GET `
      -Headers $headers `
      -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID" | Select-Object -Expand Content
    

If successful, the response body contains an instance of [`Operation`](https://docs.cloud.google.com/alloydb/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation). 

## What's next

  * Learn how to [import a CSV file](https://docs.cloud.google.com/alloydb/docs/import-csv-file).
  * Learn how to [cancel an import operation](https://docs.cloud.google.com/alloydb/docs/cancel-import).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
