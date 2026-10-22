---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery/
title: Batch export FHIR resources to BigQuery \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:49.391917+00:00
---

# Batch export FHIR resources to BigQuery  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Batch export FHIR resources to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to batch export FHIR resources to BigQuery for exploration and analysis. The export operation creates one BigQuery table for each FHIR resource type in your FHIR store.

To improve query performance and reduce costs, consider exporting FHIR resources to [partitioned tables](https://docs.cloud.google.com/bigquery/docs/partitioned-tables). For instructions, see Export FHIR resources to partitioned tables.

If you export FHIR resources on a schedule, consider exporting your data incrementally. For instructions, see Incremental exports.

## Setting BigQuery permissions

Before exporting FHIR resources to BigQuery, you must grant additional permissions to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [FHIR store BigQuery permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#fhir_store_bigquery_permissions).

## Understand export behavior

The behavior of the export operation depends on the following:

  * Whether the destination table exists.
  * Whether you set the `force` field.
  * Whether you specify an enum in [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#WriteDisposition). If you specify an enum, don't set the `force` field.



The behavior in each case is as follows:

  * The destination table exists and `force` is set to `true`: the export operation overwrites the existing table
  * The destination table exists and `force` is set to `false`: an error occurs
  * The destination table doesn't exist: the export operation creates a new table, regardless of whether you specify the `force` field
  * The destination table exists and you set `WriteDisposition` to `WRITE_TRUNCATE` or `WRITE_APPEND`: the export operation succeeds instead of returning an error

**Note:** In the destination table, `WRITE_TRUNCATE` deletes existing data and `WRITE_APPEND` appends data.



The operation outputs one BigQuery table for each resource type in the FHIR store.

## Batch export FHIR resources

The following samples show how to export FHIR resources to a BigQuery table.

When specifying the BigQuery destination, use the fully qualified URI:
    
    
    bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID
    

### Console

To export FHIR resources to BigQuery using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the dataset that has the FHIR store with the data you're exporting.

  3. In the same row as the FHIR store, open the **Actions** list and select **Export**.

  4. On the **Export FHIR resources** page that appears, find the **Select a destination** section. Select **BigQuery table**.

  5. In the **Destination table write disposition** section, select one of the following options to determine the behavior of the export operation:

     * **Only export data if the destination tables are empty** : this is equivalent to selecting the `WRITE_EMPTY` enum in `WriteDisposition`.
     * **Append data to the destination tables** : this is equivalent to selecting the `WRITE_APPEND` enum in `WriteDisposition`.
     * **Erase all existing data in destination tables before writing the FHIR resources** : this is equivalent to selecting the `WRITE_TRUNCATE` enum in `WriteDisposition`.
  6. In the **FHIR export configuration** section, click **Browse** to select the BigQuery project and dataset.

  7. In the **Schema type** dropdown, select the output schema for the BigQuery table. The following schemas are available:

     * **Analytics**. A schema based on the [SQL on FHIR](https://github.com/FHIR/sql-on-fhir/blob/master/sql-on-fhir.md) document. Because BigQuery only allows for 10,000 columns per table, schemas are not generated for the `Parameters.parameter.resource`, `Bundle.entry.resource`, and `Bundle.entry.response.outcome` fields.
     * **Analytics V2**. A schema similar to the Analytics schema, with added support for the following: 
       * [Extensions](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-extensions) with multiple values for the same [`url`](https://www.hl7.org/fhir/extensibility-definitions.html#Extension.url)
       * [Contained](http://www.hl7.org/fhir/references.html#contained) FHIR resources
The Analytics V2 schema uses more space in the destination table than the Analytics schema.
  8. Select a depth level in the **Recursive Structure Depth** slider to set the depth for all recursive structures in the output schema. By default, the recursive value is 2.

For more information, see [`recursiveStructureDepth`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#SchemaConfig.FIELDS.recursive_structure_depth).

  9. Click **Export** to export FHIR resources to BigQuery.

  10. To track the status of the operation, click the **Operations** tab. After the operation completes, the following indications appear: 
     * The **Long-running operation status** section has a green check mark under the **OK** heading.
     * The **Overview** section has a green check mark and an **OK** indicator in the same row as the operation ID.
If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**. 



### gcloud

To export FHIR resources to BigQuery, run the [`gcloud healthcare fhir-stores export bq`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq) command.

  1. Export the FHIR resources.

Before using any of the command data below, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the FHIR store's parent dataset
     * FHIR_STORE_ID: the FHIR store ID
     * BIGQUERY_DATASET_ID: the name of the existing BigQuery dataset where you're exporting FHIR resources
     * SCHEMA_TYPE: a value for [`SchemaType`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--schema-type). Use one of the following values: 
       * `analytics`. A schema based on the [SQL on FHIR](https://github.com/FHIR/sql-on-fhir/blob/master/sql-on-fhir.md) document. Because BigQuery only allows for 10,000 columns per table, schemas are not generated for the `Parameters.parameter.resource`, `Bundle.entry.resource`, and `Bundle.entry.response.outcome` fields.
       * `analytics_v2`. A schema similar to `analytics` with added support for the following: 
         * [Extensions](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-extensions) with repeated fields
         * [Contained](http://www.hl7.org/fhir/references.html#contained) FHIR resources

`analytics-v2` uses more space in the destination table than `analytics`.

     * WRITE_DISPOSITION: a value for [`WriteDisposition`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--write-disposition). Use one of the following values: 
       * `write-empty`. Only export data if the destination BigQuery tables are empty.
       * `write-truncate`. Erase all existing data in the BigQuery tables before writing the FHIR resources.
       * `write-append`. Append data to the destination BigQuery tables.
     * FHIR_RESOURCE_TYPE: an optional field. Specify one or more comma-delimited FHIR resource types to only export FHIR resources of those types.
     * SINCE_TIMESTAMP: an optional field. Specify a value in the format `YYYY-MM-DDThh:mm:ss.sss+zz:zz` to only export FHIR resources updated after a specific time. Specify the time to the second and include a time zone. For example, `2015-02-07T13:28:17.239+02:00` and `2017-01-01T00:00:00Z` are valid times.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare fhir-stores export bq FHIR_STORE_ID \
      --location=LOCATION \
      --dataset=DATASET_ID \
      --bq-dataset=bq://PROJECT_ID.BIGQUERY_DATASET_ID \
      --schema-type=SCHEMA_TYPE \
      --write-disposition=WRITE_DISPOSITION \
      --resource-type=FHIR_RESOURCE_TYPE \
      --since=SINCE_TIMESTAMP

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare fhir-stores export bq FHIR_STORE_ID `
      --location=LOCATION `
      --dataset=DATASET_ID `
      --bq-dataset=bq://PROJECT_ID.BIGQUERY_DATASET_ID `
      --schema-type=SCHEMA_TYPE `
      --write-disposition=WRITE_DISPOSITION `
      --resource-type=FHIR_RESOURCE_TYPE `
      --since=SINCE_TIMESTAMP

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare fhir-stores export bq FHIR_STORE_ID ^
      --location=LOCATION ^
      --dataset=DATASET_ID ^
      --bq-dataset=bq://PROJECT_ID.BIGQUERY_DATASET_ID ^
      --schema-type=SCHEMA_TYPE ^
      --write-disposition=WRITE_DISPOSITION ^
      --resource-type=FHIR_RESOURCE_TYPE ^
      --since=SINCE_TIMESTAMP

The response is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations). Long-running operations are returned when method calls might take a substantial amount of time to complete. The command polls the long-running operation, then prints the name of the operation in the `name` field after the export finishes. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    Request issued for: [FHIR_STORE_ID]
    Waiting for operation [projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID] to complete...⠏
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    

  2. To view more details about the operation, run the [`gcloud healthcare operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/describe) and provide the OPERATION_ID from the response.

Before using any of the command data below, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * DATASET_ID: the dataset ID
     * LOCATION: the dataset location
     * OPERATION_ID: the ID returned from the long-running operation

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare operations describe OPERATION_ID \
        --project=PROJECT_ID \
        --dataset=DATASET_ID \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare operations describe OPERATION_ID `
        --project=PROJECT_ID `
        --dataset=DATASET_ID `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare operations describe OPERATION_ID ^
        --project=PROJECT_ID ^
        --dataset=DATASET_ID ^
        --location=LOCATION

You should receive a response similar to the following:

#### Response
    
    done: true
    // If there were any errors, an `error` field displays instead of a `response` field.
    // See [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting) for a list of response codes.
    error: ERROR
      code: ERROR_CODE
      message: DESCRIPTION
    metadata:
      '@type': 'type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata'
      apiMethodName: 'google.cloud.healthcare.v1.fhir.FhirStoreService.ExportResources_bq'
      counter:
        success: 'SUCCESS_COUNT'
        // If there were any failures, they display in the `failure` field.
        failure: 'FAILURE_COUNT'
      createTime: 'YYYY-MM-DDTHH:MM:SS+ZZ:ZZ'
      endTime: 'YYYY-MM-DDTHH:MM:SS+ZZ:ZZ'
      logsUrl: https://console.cloud.google.com/CLOUD_LOGGING_URL
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    // The `response` field only displays if there were no errors.
    response:
      '@type': 'type.googleapis.com/google.cloud.healthcare.v1.fhir.ExportResourcesResponse'
    




### REST

To export FHIR resources to BigQuery, use the [`projects.locations.datasets.fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export) method.

  1. Export the FHIR resources:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the FHIR store's parent dataset
     * FHIR_STORE_ID: the FHIR store ID
     * BIGQUERY_DATASET_ID: the name of the existing BigQuery dataset where you're exporting FHIR resources
     * SCHEMA_TYPE: a value for [`SchemaType`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#schematype). Use one of the following values: 
       * `ANALYTICS`. A schema based on the [SQL on FHIR](https://github.com/FHIR/sql-on-fhir/blob/master/sql-on-fhir.md) document. Because BigQuery only allows for 10,000 columns per table, schemas are not generated for the `Parameters.parameter.resource`, `Bundle.entry.resource`, and `Bundle.entry.response.outcome` fields.
       * `ANALYTICS_V2`. A schema similar to `ANALYTICS` with added support for the following: 
         * [Extensions](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-extensions) with multiple values for the same [`url`](https://www.hl7.org/fhir/extensibility-definitions.html#Extension.url)
         * [Contained](http://www.hl7.org/fhir/references.html#contained) FHIR resources

`ANALYTICS_V2` uses more space in the destination table than `ANALYTICS`

.
     * WRITE_DISPOSITION: a value for [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#writedisposition). Use one of the following values: 
       * `WRITE_EMPTY`. Only export data if the destination BigQuery tables are empty.
       * `WRITE_TRUNCATE`. Erase all existing data in the BigQuery tables before writing the FHIR resources.
       * `WRITE_APPEND`. Append data to the destination BigQuery tables.
     * FHIR_RESOURCE_TYPE: an optional field. Specify one or more comma-delimited FHIR resource types to only export FHIR resources of those types.
     * SINCE_TIMESTAMP: an optional field. Specify a value in the format `YYYY-MM-DDThh:mm:ss.sss+zz:zz` to only export FHIR resources updated after a specific time. Specify the time to the second and include a time zone. For example, `2015-02-07T13:28:17.239+02:00` and `2017-01-01T00:00:00Z` are valid times.

Request JSON body: 
    
    {
      "bigqueryDestination": {
        "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
        "schemaConfig": {
          "schemaType": "SCHEMA_TYPE",
        },
        "writeDisposition": "WRITE_DISPOSITION"
      },
      "_type": "FHIR_RESOURCE_TYPE",
      "_since": "SINCE_TIMESTAMP"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "bigqueryDestination": {
        "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
        "schemaConfig": {
          "schemaType": "SCHEMA_TYPE",
        },
        "writeDisposition": "WRITE_DISPOSITION"
      },
      "_type": "FHIR_RESOURCE_TYPE",
      "_since": "SINCE_TIMESTAMP"
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "bigqueryDestination": {
        "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
        "schemaConfig": {
          "schemaType": "SCHEMA_TYPE",
        },
        "writeDisposition": "WRITE_DISPOSITION"
      },
      "_type": "FHIR_RESOURCE_TYPE",
      "_since": "SINCE_TIMESTAMP"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:export" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) (LRO). Long-running operations are returned when method calls might take additional time to complete. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    
    

  2. Use the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method to get the status of the long-running operation.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * DATASET_ID: the dataset ID
     * LOCATION: the dataset location
     * OPERATION_ID: the ID returned from the long-running operation

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The output is the following. When the response contains `"done": true`, the long-running operation has finished. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.fhir.FhirStoreService.ExportResources_bq",
        "createTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "endTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "logsUrl": "https://console.cloud.google.com/CLOUD_LOGGING_URL"
        "counter": {
          "success": "SUCCESS_COUNT",
          // If there were any failures, they display in the `failure` field.
          "failure": "FAILURE_COUNT"
        }
      },
      "done": true,
      // The `response` field only displays if there were no errors.
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.fhir.ExportResourcesResponse",
        
      },
      // If there were any errors, an `error` field displays instead of a `response` field.
      // See [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting) for a list of response codes.
      "error": {
        "code": ERROR_CODE,
        "message": "DESCRIPTION",
        "details": [
          {
            "@type": "...",
            FIELD1: ...,
            ...
          }
        ]
      }
    }
    




## Export FHIR resources to partitioned tables

To export FHIR resources to BigQuery partitioned tables, set the [`TimePartitioning`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#TimePartitioning) enum in the [`lastUpdatedPartitionConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#SchemaConfig.FIELDS.last_updated_partition_config) field in your FHIR store.

The partitioned tables work like BigQuery [time-unit partitioned tables](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables). Partitioned tables have an added column named `lastUpdated`, which is a duplicate of the `meta.lastUpdated` column which is generated from the `meta.lastUpdated` field in a FHIR resource. BigQuery uses the `lastUpdated` column to partition tables by hour, day, month, or year.

See [Select daily, hourly, monthly, or yearly partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#select_daily_hourly_monthly_or_yearly_partitioning) for recommendations on how to select a partition granularity.

You can't convert existing, non-partitioned BigQuery tables into partitioned tables. If you export Patient resource changes to a non-partitioned `Patients` table, and later create a new FHIR store with table partitioning that exports to the same BigQuery dataset, the Cloud Healthcare API still exports data to the non-partitioned `Patients` table. To start using a partitioned table, delete the existing `Patients` table or use a different BigQuery dataset.

If you add partitioning to an existing FHIR store configuration, you can still export to existing non-partitioned tables. However, partitioning will only take effect on new tables.

**Important:** Partitioning takes effect on existing non-partitioned tables if [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#writedisposition) is set to [`WRITE_TRUNCATE`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#write_truncate), because the destination tables are deleted and recreated with each export.

The following samples show how to export FHIR resources to BigQuery partitioned tables.

### Console

The Google Cloud console and the gcloud CLI don't support this action. Instead, use `curl`, PowerShell, or your preferred language.

### gcloud

The Google Cloud console and the gcloud CLI don't support this action. Instead, use `curl`, PowerShell, or your preferred language.

### REST

To export FHIR resources to BigQuery partitioned tables, use the [`projects.locations.datasets.fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export) method.

  1. Export the FHIR resources:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the FHIR store's parent dataset
     * FHIR_STORE_ID: the FHIR store ID
     * BIGQUERY_DATASET_ID: the name of the existing BigQuery dataset where you're exporting FHIR resources
     * SCHEMA_TYPE: a value for [`SchemaType`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#schematype). Use one of the following values: 
       * `ANALYTICS`. A schema based on the [SQL on FHIR](https://github.com/FHIR/sql-on-fhir/blob/master/sql-on-fhir.md) document. Because BigQuery only allows for 10,000 columns per table, schemas are not generated for the `Parameters.parameter.resource`, `Bundle.entry.resource`, and `Bundle.entry.response.outcome` fields.
       * `ANALYTICS_V2`. A schema similar to `ANALYTICS` with added support for the following: 
         * [Extensions](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-extensions) with multiple values for the same [`url`](https://www.hl7.org/fhir/extensibility-definitions.html#Extension.url)
         * [Contained](http://www.hl7.org/fhir/references.html#contained) FHIR resources

`ANALYTICS_V2` uses more space in the destination table than `ANALYTICS`

.
     * TIME_PARTITION_TYPE: the granularity at which to partition exported FHIR resources. Use one of the following values: 
       * `HOUR`: partition data by hour
       * `DAY`: partition data by day
       * `MONTH`: partition data by month
       * `YEAR`: partition data by year
     * WRITE_DISPOSITION: a value for [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#writedisposition). Use one of the following values: 
       * `WRITE_EMPTY`: only export data if the BigQuery table is empty.
       * `WRITE_TRUNCATE`: erase all existing data in the BigQuery table before writing the DICOM instances.
       * `WRITE_APPEND`: append data to the BigQuery table.

Request JSON body: 
    
    {
      "bigqueryDestination": {
        "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
        "schemaConfig": {
          "schemaType": "SCHEMA_TYPE",
          "lastUpdatedPartitionConfig": {
            "type": "TIME_PARTITION_TYPE"
          }
        },
        "writeDisposition": "WRITE_DISPOSITION"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "bigqueryDestination": {
        "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
        "schemaConfig": {
          "schemaType": "SCHEMA_TYPE",
          "lastUpdatedPartitionConfig": {
            "type": "TIME_PARTITION_TYPE"
          }
        },
        "writeDisposition": "WRITE_DISPOSITION"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "bigqueryDestination": {
        "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
        "schemaConfig": {
          "schemaType": "SCHEMA_TYPE",
          "lastUpdatedPartitionConfig": {
            "type": "TIME_PARTITION_TYPE"
          }
        },
        "writeDisposition": "WRITE_DISPOSITION"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:export" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "version": "FHIR_STORE_VERSION",
      "bigqueryDestination": {
        "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
        "schemaConfig": {
          "schemaType": "SCHEMA_TYPE",
          "lastUpdatedPartitionConfig": {
            "type": "TIME_PARTITION_TYPE"
          }
        },
        "writeDisposition": "WRITE_DISPOSITION"
      }
    }
    

  2. Use the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method to get the status of the long-running operation.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * DATASET_ID: the dataset ID
     * LOCATION: the dataset location
     * OPERATION_ID: the ID returned from the long-running operation

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The output is the following. When the response contains `"done": true`, the long-running operation has finished. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.fhir.FhirStoreService.ExportResources_bq",
        "createTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "endTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "logsUrl": "https://console.cloud.google.com/CLOUD_LOGGING_URL"
        "counter": {
          "success": "SUCCESS_COUNT",
          // If there were any failures, they display in the `failure` field.
          "failure": "FAILURE_COUNT"
        }
      },
      "done": true,
      // The `response` field only displays if there were no errors.
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.fhir.ExportResourcesResponse",
        
      },
      // If there were any errors, an `error` field displays instead of a `response` field.
      // See [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting) for a list of response codes.
      "error": {
        "code": ERROR_CODE,
        "message": "DESCRIPTION",
        "details": [
          {
            "@type": "...",
            FIELD1: ...,
            ...
          }
        ]
      }
    }
    




### Query a partitioned table

To reduce query costs when querying partitioned tables, use the [`WHERE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#where_clause) clause to filter by time units.

For example, suppose that you set the [`PartitionType`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#PartitionType) enum to [`DAY`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#PartitionType.ENUM_VALUES.DAY). To query a `Patients` table for Patient resources that were updated on a specific date, run the following query:
    
    
    SELECT * FROM `PROJECT_ID.BIGQUERY_DATASET.Patients`
      WHERE DATE(lastUpdated) = 'YYYY-MM-DD'

## Incremental exports

You can specify a timestamp to only export FHIR resources added to your FHIR store since a previous successful export. This improves performance and avoids the cost of re-exporting the entire FHIR store, while also ensuring your exported data is always up-to-date.

When calling [`fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export), specify the timestamp in the [`_since`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export#body.request_body.FIELDS.since) field.

## Troubleshooting FHIR export requests

If errors occur during a FHIR export request, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

If the entire operation returns an error, see [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting).

### Cannot convert column from NULLABLE to REPEATED

This error is caused by a repeated extension. To resolve this error, use the [`ANALYTICS_V2`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#SchemaType.ENUM_VALUES.ANALYTICS_V2) schema type. If you're using `ANALYTICS_V2`, you might have a conflict between two extensions, or a conflict between an extension and another field.

Column names are generated from the text after the last `/` character in extension URLs. If an extension URL ends with a value like `/resource_field name`, a conflict can occur. \

To prevent this error from occurring again, don't use extensions if their field names are the same as the resource fields you're populating.

## What's next

  * To learn more about data governance and security in BigQuery, see [Overview of data security and governance](https://docs.cloud.google.com/bigquery/docs/data-governance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
