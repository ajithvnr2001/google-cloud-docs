---
url: https://docs.cloud.google.com/alloydb/docs/export-csv-file/
title: Export a CSV file \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:10.129029+00:00
---

# Export a CSV file  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/export-csv-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Export a CSV file Stay organized with collections  Save and categorize content based on your preferences. 

To extract table or query data for use in external tools and environments, you can export data from AlloyDB for PostgreSQL clusters to a Cloud Storage bucket in CSV format.

For information about migrating an entire database from a supported database server to a new AlloyDB instance, see [Migrate a database to AlloyDB by using Database Migration Service](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quickstart). If you're exporting because you want to create a new instance from the exported file, consider [restoring a cluster from a stored backup](https://docs.cloud.google.com/alloydb/docs/backup/restore).

You can cancel the export of data from AlloyDB for PostgreSQL clusters. For more information, see [Cancel an export operation](https://docs.cloud.google.com/alloydb/docs/cancel-export).

## Before you begin

  * Before you begin an export operation, keep in mind that export operations use database resources, but they don't interfere with standard database operations unless the instance is underprovisioned.
  * `SELECT_QUERY` can contain comments or leading and trailing whitespaces. Comments are ignored and white spaces are trimmed before running the export query.
  * Inter-region data transfer charges apply when the target bucket is in a different region than the source cluster. For more information, see [AlloyDB for PostgreSQL pricing](https://docs.cloud.google.com/alloydb/pricing).
  * Multiple export operations can run in parallel.
  * Compression is enabled if the object name ends with `.gz` extension. The object is then exported in `.gz` format to Cloud Storage.
  * Only ASCII characters in hex code (with or without the `0x` prefix) are allowed for character values in CSV options like `field_delimiter`, `quote_character`, and `escape_character`.



## Required roles and permissions for exporting from AlloyDB

To export data from AlloyDB into Cloud Storage, the user initiating the export must have one of the following Identity and Access Management (IAM) roles:

  * The [AlloyDB Admin](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions) (`roles/alloydb.admin`) role
  * A [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), including the following permissions: 
    * `alloydb.clusters.get`
    * `alloydb.clusters.export`



Additionally, the service account for the AlloyDB cluster must have one of the following roles:

  * The `storage.objectAdmin` IAM role
  * A custom role, including the following permissions: 
    * `storage.objects.create`



For help with IAM roles, see [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

## Export data to a CSV file

During a CSV export, you can specify the schemas to export. All schemas at the database level are eligible for export.

**Note:** AlloyDB uses double quotation marks (hex value `22`) as the default escape character. This can be a problem for databases where values for `NULL` are entered as string literals.

You can use the gcloud CLI or the REST API to customize your CSV file format.

###  gcloud 

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. Use [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the AlloyDB service account for the bucket. The format for the service account is as follows:
         
         service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com

For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

**Note:** If an existing object has the same name as the one that's being exported to the Cloud Storage bucket, then granting the `objectAdmin` role to the service account results in the older object being replaced. To avoid this, you can grant the service account the less privileged permission `storage.objectCreator`, which can't replace existing objects.
  3. Export the database to your Cloud Storage bucket.

Run the export CSV command: [`gcloud alloydb clusters export`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/export).

The following list describes options for exporting data in a CSV format:

     * `--select-query` (Required): The select query used to extract the data.
**Note:** While in transit, the query might be processed in intermediate locations other than the location of the target instance.
     * `--async` (Optional): return immediately, without waiting for the operation in progress to complete.
     * `--field-delimiter` (Optional): specifies the character that separates columns in each row (line) of the file. The default is a comma. The value of this argument must be a character in hex ASCII code.
     * `--quote-character` (Optional): Specifies the quoting character to be used when a data value is quoted. The default is a double quotation mark. The value of this argument must be a character in hex ASCII code.
     * `--escape-character` (Optional): Specifies the character that must appear before a data character that needs to be escaped. The default is the same as `--quote-character`. The value of this argument must be a character in hex ASCII code.

To use these features, include these options in the gcloud CLI command.

Otherwise, remove these parameters from the following command:
    
    gcloud alloydb clusters export CLUSTER_NAME \
      --region=REGION \
      --database=DATABASE_NAME \
      --gcs-uri="gs://BUCKET_NAME/OBJECT_NAME" \
      --select-query=SELECT_QUERY \
      --field-delimiter=FIELD_DELIMITER \
      --quote-character=QUOTE_CHARACTER \
      --escape-character=ESCAPE_CHARACTER \
      --csv

  4. If you don't need to retain the IAM role that you set previously, [revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-console) it.




###  REST v1 

  1. Create a bucket for the export:
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION_NAME --project=PROJECT_NAME

  2. Use [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) to grant the `storage.objectAdmin` [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the AlloyDB service account for the bucket. The format for the service account is as follows:
         
         service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com

For help with setting IAM permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

**Note:** In the case where there already exists an object of the same name as the one being exported in the Cloud Storage bucket, granting the `objectAdmin` role to the service account will result in the older object being replaced. To avoid this, you can grant the less privileged permission `storage.objectCreator` to the service account, which can't replace already existing objects.
  3. Export your database.  


Use the following HTTP method and URL:
         
         POST https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID:export

Before you use any of the request data, make the following replacements:

     * PROJECT_ID: the project ID.
     * REGION: the region in which the AlloyDB cluster is deployed.
     * CLUSTER_ID: the cluster ID.
     * BUCKET_NAME: the Cloud Storage bucket name.
     * PATH_TO_CSV_FILE: the path to the CSV file.
     * DATABASE_NAME: the name of a database inside the AlloyDB cluster.
     * SELECT_QUERY: the SQL query for the export.

**Note:** While in transit, the query might be processed in intermediate locations other than the location of the target instance.
     * ESCAPE_CHARACTER (Optional): the character that must appear before a data character that needs to be escaped. The value of this argument must be a character in Hex ASCII Code. For example, `22` represents a double quotation mark.

     * QUOTE_CHARACTER (Optional): the character that encloses values from columns that have a string data type. The value of this argument must be a character in Hex ASCII Code. For example, `22` represents a double quotation mark.

     * FIELD_DELIMITER (Optional): the character that splits column values. The value of this argument must be a character in Hex ASCII Code. For example, `2C` represents a comma.

Request JSON body:
    
    {
      "gcs_destination": {
        "uri": "gs://BUCKET_NAME/PATH_TO_CSV_FILE"
      },
      "database": "DATABASE_NAME",
      "csv_export_options": {
        "select_query": "SELECT_QUERY",
        "escape_character": "ESCAPE_CHARACTER",
        "quote_character": "QUOTE_CHARACTER",
        "field_delimiter": "FIELD_DELIMITER"
      }
    }
    

To send your request, use one of these options:




#### curl (Linux, macOS, or Cloud Shell)

The following command assumes that you signed into the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    
           curl -X POST \
                 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                 -H "Content-Type: application/json; charset=utf-8" \
                 -d @request.json \
                 "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID:export"
      

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
          -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID:export"| Select-Object -Expand Content
      

You receive a JSON response similar to the following:

#### Response
    
    
        {
         "name": "projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID",
         "metadata": {
          "@type": "type.googleapis.com/google.cloud.alloydb.v1.OperationMetadata",
          "createTime": "2024-09-17T06:05:31.244428646Z",
          "target": "projects/PROJECT_ID/locations/REGION/clusters/TARGET_CLUSTER",
          "verb": "export",
          "requestedCancellation": false,
          "apiVersion": "v1"
         },
         "done": false
        }
      

If you don't need to retain the IAM permissions that you set previously, remove them.

For the complete list of parameters for the request, see [`clusters.export`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/export).

## Customize the format of a CSV export file

You can use the gcloud CLI or the REST API to customize your CSV file format. When you perform an export, you can specify the following formatting options:

**CSV option** | **Default value** | **gcloud flag** | **REST API property** | **Description**  
---|---|---|---|---  
Escape | The default is the same as the `QUOTE` value. | `--escape-character` | `escape_character` | Character that appears before a data character that needs to be escaped.  
Quote | `"22"`  
ASCII hex code for a double quotation mark. | `--quote-character` | `quote_character` | Specifies the quoting character to be used when a data value is quoted.  
Field delimiter | `"2C"`  
ASCII hex code for comma. | `--field-delimiter` | `field_delimiter` | Character that splits column values.  
  
Use the following gcloud CLI and REST API examples to customize your CSV export file format:

###  gcloud 
    
    
    gcloud alloydb clusters export CLUSTER_NAME \
      --region=REGION \
      --database=DATABASE_NAME \
      --gcs-uri='gs://BUCKET_NAME/PATH_TO_CSV_FILE' \
      --select-query=SELECT_QUERY \
      --field-delimiter='2C' \
      --quote-character='22' \
      --escape-character='5C' \
      --csv

###  REST v1 

The equivalent REST API request body looks similar to the following:
    
    
    {
      "gcs_destination": {
        "uri": "gs://BUCKET_NAME/PATH_TO_CSV_FILE"
      },
      "database": "DATABASE_NAME",
      "csv_export_options": {
        "select_query": "SELECT_QUERY",
        "escape_character": "5C",
        "quote_character": "22",
        "field_delimiter": "2C"
      }
    }
    

By default, the CSV export creates a standard CSV output. If you need more options than those provided by AlloyDB, you can use the following statement in a [`psql` client](https://docs.cloud.google.com/alloydb/docs/connect-psql):
    
    
    \copy TABLE_NAME TO 'CSV_FILE_NAME.csv' WITH
      (FORMAT csv, ESCAPE 'ESCAPE_CHARACTER', QUOTE 'QUOTE_CHARACTER',
      DELIMITER 'DELIMITER_CHARACTER', ENCODING 'UTF8', NULL 'NULL_MARKER_STRING');
    

## What's next

  * Learn how to [export a SQL dump file](https://docs.cloud.google.com/alloydb/docs/export-sql-file).
  * [Cancel an export operation](https://docs.cloud.google.com/alloydb/docs/cancel-export).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
