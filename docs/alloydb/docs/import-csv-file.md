---
url: https://docs.cloud.google.com/alloydb/docs/import-csv-file/
title: Import a CSV file \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:59.583019+00:00
---

# Import a CSV file  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/import-csv-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Import a CSV file Stay organized with collections  Save and categorize content based on your preferences. 

To load tabular data into an existing database table, you can import a CSV file stored in a Cloud Storage bucket into an AlloyDB for PostgreSQL cluster.

**Note:** If you're migrating an entire database from a supported database server (on-premises, in AWS, or AlloyDB) to a new AlloyDB cluster, you can use [Database Migration Service](https://docs.cloud.google.com/database-migration/docs) instead of exporting and then importing files. If you're exporting because you want to create a new cluster from the exported file, consider [restoring from a stored backup](https://docs.cloud.google.com/alloydb/docs/backup/restore).

You can cancel the import of data into AlloyDB clusters. For more information, see [Cancel an import operation](https://docs.cloud.google.com/alloydb/docs/cancel-import).

## Before you begin

Before you begin an import operation:

  * Make sure that your database has adequate free space.
  * Import operations use database resources, but they don't interfere with normal database operations unless the cluster is under-provisioned.

**Important:** Before starting a large import operation, make sure that at least 25 percent of the disk is free on the cluster. Doing so helps to prevent issues with aggressive autogrowth, which can adversely affect the availability of the cluster. Verify that the CSV file has the expected data and that it's a valid CSV file.

## Required roles and permissions for importing to AlloyDB clusters

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

## Import data from a CSV file to AlloyDB clusters

  * The database and table you are importing into must exist on your AlloyDB cluster. For help with creating a database, see [Create a database](https://docs.cloud.google.com/alloydb/docs/database-create).
  * CSV files must have one line for each row of data and use comma-separated fields.
  * CSV files must not contain a header row. If your CSV file has a header row, remove it before importing.

**Note:** The default behavior for AlloyDB is to import columns in your CSV file in the same order as the table schema. If the order is different in your CSV file or if some columns are skipped, use [CSV Import options](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import) to import from the CSV file to required columns.

To import data to an AlloyDB cluster using a CSV file, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster name to open the **Overview** page for that cluster.

  3. Click **Import**.

  4. In **File format** , select **CSV**.

  5. In **Select source file** , choose whether to upload files from your computer or select a file from a Cloud Storage location.

     1. To upload a file from your computer, do the following:

        1. Select **Upload files from your computer**.
        2. Click **Browse** next to **Select local file** to select a CSV file from your local machine.
        3. Click **Browse** next to **Select Cloud Storage location** to select a Cloud Storage location to store the uploaded local file.
        4. Click **Upload** to upload the file.
     2. To select a CSV file that exists in a Cloud Storage bucket, do the following:

        1. Select **Select file from Google Cloud Storage**.
        2. Click **Browse** next to **bucket-name/file-name** to select a CSV file from a Cloud Storage bucket.
  6. Select the database you want the data to be imported into from the **Database** drop-down menu.

  7. Select the table within the database from the **Table** drop-down menu.

  8. Optional: To specify a user for the import operation, click **Show user options** and enter the username in the **User** field.

  9. To start the import operation, click **Import**.


**Note:** You can import a compressed `.gz` or uncompressed `.csv` file.

###  gcloud 

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Upload the CSV file to your bucket. For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).
  3. Use [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) to grant the `storage.objectViewer` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the AlloyDB service account for the bucket:
         
         service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com

For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

  4. Import the file:
         
         gcloud alloydb clusters import CLUSTER_NAME \
           --region=REGION \
           --gcs-uri=gs://BUCKET_NAME/FILE_NAME \
           --database=DATABASE_NAME \
           --user=USER \
           --csv \
           --table=TABLE_NAME

**Note:** You can import a compressed (`.gz`) or an uncompressed (`.csv`) file.

Replace the following:

     * CLUSTER_NAME: the name of the cluster.
     * REGION: the region in which the AlloyDB cluster is deployed.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * FILE_NAME: the name of the CSV file.
     * DATABASE_NAME: the name of a database inside the cluster.
     * USER: the user for the import operation.
     * TABLE_NAME: the table inside the database.

For more information about using the `import` command, see the [`gcloud alloydb clusters import`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import) command reference page.

  5. If you don't need to keep the IAM permissions that you set previously, remove them using [`gcloud storage buckets remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding).




###  REST v1 

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Upload the CSV file to your bucket. For help with uploading files to buckets, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).
  3. Use [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) to grant the `storage.objectViewer` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the AlloyDB cluster service account for the bucket. The format for the service account is as follows:
         
         service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com

For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

  4. Import the file.

**Note:** You can import a compressed (`.gz`) or an uncompressed (`.csv`) file.

Use the following HTTP method and URL:
         
         POST https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID:import

Before you use any of the request data, make the following replacements:

     * PROJECT_ID: the project ID.
     * LOCATION_ID: the region in which the AlloyDB cluster is deployed.
     * CLUSTER_ID: the cluster ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_CSV_FILE: the path to the CSV file.
     * USER: the user for the import operation.
     * DATABASE_NAME: the name of a database inside the AlloyDB cluster.
     * TABLE_NAME: the table inside the database.
     * COLUMNS (Optional): the columns to import.
     * ESCAPE_CHARACTER (Optional): the character that must appear before a data character that needs to be escaped. The value of this argument must be a character in Hex ASCII Code. For example, `22` represents a double quotation mark.
     * QUOTE_CHARACTER (Optional): the character that encloses values from columns that have a string data type. The value of this argument must be a character in Hex ASCII Code. For example, `22` represents a double quotation mark.
     * FIELD_DELIMITER (Optional): the character that splits column values. The value of this argument must be a character in Hex ASCII Code. For example, `2C` represents a comma.

Request JSON body:
    
    {
      "gcsUri": "gs://BUCKET_NAME/PATH_TO_CSV_FILE",
      "database": "DATABASE_NAME",
      "user": "USER",
      "csvImportOptions": {
        "table": "TABLE_NAME",
        "columns": ["COLUMN1", "COLUMN2"],
        "fieldDelimiter": "FIELD_DELIMITER",
        "quoteCharacter": "QUOTE_CHARACTER",
        "escapeCharacter": "ESCAPE_CHARACTER"
      }
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
      "createTime": "2024-09-17T06:05:31.244428646Z",
      "target": "projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID",
      "verb": "import",
      "requestedCancellation": false,
      "apiVersion": "v1"
     },
     "done": false
    }
    

  5. If you don't need to retain the IAM permissions that you set previously, remove them.

For the complete list of parameters for the request, see [`clusters.import`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/import).




## Customize CSV format and import the file

You can customize the CSV format and import the file when the CSV file contains non-default field delimiter, or quote or escape characters. To import a CSV file with a non-default format, you must provide the same formatting options in the request.

Use the following gcloud CLI and REST API examples to help you customize your CSV file format.

###  gcloud 
    
    
    gcloud alloydb clusters import CLUSTER_NAME \
      --region=REGION \
      --database=DATABASE_NAME \
      --gcs-uri='gs://BUCKET_NAME/PATH_TO_CSV_FILE' \
      --user=USERNAME \
      --table=TABLE_NAME \
      --columns=COLUMNS \
      --field-delimiter='2C' \
      --quote-character='22' \
      --escape-character='5C' \
      --csv

###  REST v1 

The equivalent REST API request body looks similar to the following:
    
    
    {
     "gcsUri": "gs://BUCKET_NAME/PATH_TO_CSV_FILE",
     "database": "DATABASE_NAME",
     "user": "USER",
     "csvImportOptions": {
         "table": "TABLE_NAME",
         "columns": ["COLUMN1", "COLUMN2"],
         "escapeCharacter": "5C",
         "quoteCharacter": "22",
         "fieldDelimiter": "2C"
     }
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/import#body.HTTP_TEMPLATE) is constructed for this task, see the [APIs Explorer on the `clusters.import` page](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/import).

**Note:** If you use custom format options in your import commands, make sure that you create the exported file with the same options.

If you get an error like `INVALID_ARGUMENT`, make sure that the table exists. If the table exists, confirm that you have the correct permissions on the bucket. For help configuring access control in Cloud Storage, see [Create and Manage Access Control Lists](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists).

## Check the status of an import operation

To check the status of an import operation, follow these steps:

###  gcloud 

Run the following using the [gcloud alloydb operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/describe) command:
    
    
    gcloud alloydb operations describe OPERATION_ID --region=REGION

The status of these operations is in the `STATUS` field.

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

  * Learn how to [import a SQL file](https://docs.cloud.google.com/alloydb/docs/import-sql-file).
  * Learn how to [cancel an import operation](https://docs.cloud.google.com/alloydb/docs/cancel-import).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
