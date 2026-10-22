---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bigquery-streaming/
title: Streaming FHIR resource changes to BigQuery \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:25.354273+00:00
---

# Streaming FHIR resource changes to BigQuery  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bigquery-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Streaming FHIR resource changes to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure a FHIR store to automatically export FHIR resources to BigQuery tables every time a FHIR resource is created, updated, patched, or deleted. This process is called _BigQuery streaming_.

You can use BigQuery streaming to do the following:

  * Synchronize the data in a FHIR store with a BigQuery dataset in near real time.
  * Perform complex queries on FHIR data without needing to export it to BigQuery every time you want to analyze the data.



To improve query performance and reduce costs, you can configure BigQuery streaming to [partitioned tables](https://docs.cloud.google.com/bigquery/docs/partitioned-tables). For instructions, see Stream FHIR resources to partitioned tables.

## Before you begin

Read [Exporting FHIR resources to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery) to understand how the export process works.

## Limitations

If you [import FHIR resources from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export#importing_fhir_resources), the changes aren't streamed to BigQuery.

## Setting BigQuery permissions

To enable BigQuery streaming, you must grant additional permissions to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [FHIR store BigQuery permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#fhir_store_bigquery_permissions).

## Configure BigQuery streaming on a FHIR store

To enable BigQuery streaming, configure the [`StreamConfigs`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.stream_configs) object in your FHIR store. In `StreamConfigs`, you can configure the [`resourceTypes[]`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#StreamConfig.FIELDS.resource_types) array to control which types of FHIR resources BigQuery streaming applies to. If you don't specify `resourceTypes[]`, BigQuery streaming applies to all FHIR resource types.

For explanations of other configurations available in `StreamConfigs`, such as [`BigQueryDestination`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#BigQueryDestination), see [Exporting FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery#exporting_fhir_resources).

The following samples show how to enable BigQuery streaming on an existing FHIR store.

### Console

To configure BigQuery streaming on an existing FHIR store using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the FHIR store you want to edit.

  3. In the **Data stores** list, click the FHIR store you want to edit.

  4. In the **BigQuery streaming** section, complete the following steps:

     1. Click **Add new streaming configuration**.
     2. In the **New streaming configuration** section, click **Browse** to select the BigQuery dataset where you want changed FHIR resources to be streamed.
     3. In the **Schema type** dropdown, select the output schema for the BigQuery table. The following schemas are available: 
        * **Analytics**. A schema based on the [SQL on FHIR](https://github.com/FHIR/sql-on-fhir/blob/master/sql-on-fhir.md) document. Because BigQuery only allows for 10,000 columns per table, schemas are not generated for the `Parameters.parameter.resource`, `Bundle.entry.resource`, and `Bundle.entry.response.outcome` fields.
        * **Analytics V2**. A schema similar to the Analytics schema, with added support for the following: 
          * [Extensions](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-extensions) with multiple values for the same [`url`](https://www.hl7.org/fhir/extensibility-definitions.html#Extension.url)
          * [Contained](http://www.hl7.org/fhir/references.html#contained) FHIR resources
The Analytics V2 schema uses more space in the destination table than the Analytics schema.
     4. Select a depth level in the **Recursive Structure Depth** slider to set the depth for all recursive structures in the output schema. By default, the recursive value is 2.
     5. In the **Select FHIR resource types** list, select the resource types to stream.
  5. Click **Done** to save the streaming configuration.




### gcloud

The gcloud CLI doesn't support this action. Instead, use the Google Cloud console, `curl`, PowerShell, or your preferred language.

### REST

To configure BigQuery streaming on an existing FHIR store, use the [`projects.locations.datasets.fhirStores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/patch) method.

The following samples do not specify the `resourceTypes[]` array, so BigQuery streaming is enabled for all FHIR resource types.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * BIGQUERY_DATASET_ID: the name of an existing BigQuery dataset where you're streaming FHIR resource changes
  * SCHEMA_TYPE: a value for the [`SchemaType`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#schematype) enum. Use one of the following values: 
    * `ANALYTICS`. A schema based on the [SQL on FHIR](https://github.com/FHIR/sql-on-fhir/blob/master/sql-on-fhir.md) document. Because BigQuery only allows for 10,000 columns per table, schemas are not generated for the `Parameters.parameter.resource`, `Bundle.entry.resource`, and `Bundle.entry.response.outcome` fields.
    * `ANALYTICS_V2`. A schema similar to `ANALYTICS` with added support for the following: 
      * [Extensions](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-extensions) with multiple values for the same [`url`](https://www.hl7.org/fhir/extensibility-definitions.html#Extension.url)
      * [Contained](http://www.hl7.org/fhir/references.html#contained) FHIR resources

`ANALYTICS_V2` uses more space in the destination table than `ANALYTICS`

.
  * WRITE_DISPOSITION: a value for the [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#writedisposition) enum. Use one of the following values: 
    * `WRITE_EMPTY`. Only export data if the destination BigQuery tables are empty.
    * `WRITE_TRUNCATE`. Erase all existing data in the BigQuery tables before writing the FHIR resources.
    * `WRITE_APPEND`. Append data to the destination BigQuery tables.



Request JSON body: 
    
    
    {
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "SCHEMA_TYPE",
            },
            "writeDisposition": "WRITE_DISPOSITION"
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "SCHEMA_TYPE",
            },
            "writeDisposition": "WRITE_DISPOSITION"
          }
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=streamConfigs"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "SCHEMA_TYPE",
            },
            "writeDisposition": "WRITE_DISPOSITION"
          }
        }
      ]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=streamConfigs" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following.

If you configured any fields in the [`FhirStore`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#resource:-fhirstore) resource, they also appear in the response.

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "version": "FHIR_STORE_VERSION",
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "datasetUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID",
            "schemaConfig": {
              "schemaType": "SCHEMA_TYPE",
            },
            "writeDisposition": "WRITE_DISPOSITION"
          }
        }
      ]
    }
    

By default, when you stream FHIR resource changes to BigQuery, a [view](https://docs.cloud.google.com/bigquery/docs/views-intro) is created for each resource streamed. The view has the following properties:

  * It has the same name as the resource and the resource's table in the BigQuery dataset. For example, when you stream a Patient resource, a table named `Patient` is created with a view named `Patientview`.
  * It only contains the current version of the resource, rather than all historical versions.



## Stream FHIR resources to partitioned tables

To export FHIR resources to BigQuery partitioned tables, set the [`TimePartitioning`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#TimePartitioning) enum in the [`lastUpdatedPartitionConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#SchemaConfig.FIELDS.last_updated_partition_config) field in your FHIR store.

The partitioned tables work like BigQuery [time-unit partitioned tables](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables). Partitioned tables have an added column named `lastUpdated`, which is a duplicate of the `meta.lastUpdated` column which is generated from the `meta.lastUpdated` field in a FHIR resource. BigQuery uses the `lastUpdated` column to partition tables by hour, day, month, or year.

See [Select daily, hourly, monthly, or yearly partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#select_daily_hourly_monthly_or_yearly_partitioning) for recommendations on how to select a partition granularity.

You can't convert existing, non-partitioned BigQuery tables into partitioned tables. If you export Patient resource changes to a non-partitioned `Patients` table, and later create a new FHIR store with table partitioning that exports to the same BigQuery dataset, the Cloud Healthcare API still exports data to the non-partitioned `Patients` table. To start using a partitioned table, delete the existing `Patients` table or use a different BigQuery dataset.

If you add partitioning to an existing FHIR store configuration, you can still export to existing non-partitioned tables. However, partitioning will only take effect on new tables.

**Important:** Partitioning takes effect on existing non-partitioned tables if [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#writedisposition) is set to [`WRITE_TRUNCATE`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#write_truncate), because the destination tables are deleted and recreated with each export.

The following samples show how to enable BigQuery streaming to partitioned tables on an existing FHIR store.

### Console

The Google Cloud console and the gcloud CLI don't support this action. Instead, use `curl`, PowerShell, or your preferred language.

### gcloud

The Google Cloud console and the gcloud CLI don't support this action. Instead, use `curl`, PowerShell, or your preferred language.

### REST

To configure BigQuery streaming to partitioned tables on an existing FHIR store, use the [`projects.locations.datasets.fhirStores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/patch) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * BIGQUERY_DATASET_ID: the name of an existing BigQuery dataset where you're streaming FHIR resource changes
  * SCHEMA_TYPE: a value for the [`SchemaType`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#schematype) enum. Use one of the following values: 
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
  * WRITE_DISPOSITION: a value for the [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#writedisposition) enum. Use one of the following values: 
    * `WRITE_EMPTY`. Only export data if the destination BigQuery tables are empty.
    * `WRITE_TRUNCATE`. Erase all existing data in the BigQuery tables before writing the FHIR resources.
    * `WRITE_APPEND`. Append data to the destination BigQuery tables.



Request JSON body: 
    
    
    {
      "streamConfigs": [
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
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "streamConfigs": [
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
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=streamConfigs"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "streamConfigs": [
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
      ]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=streamConfigs" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "version": "FHIR_STORE_VERSION",
      "streamConfigs": [
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
      ]
    }
    

### Query a partitioned table

To reduce query costs when querying partitioned tables, use the [`WHERE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#where_clause) clause to filter by time units.

For example, suppose that you set the [`PartitionType`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#PartitionType) enum to [`DAY`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#PartitionType.ENUM_VALUES.DAY). To query a `Patients` table for Patient resources that changed on a specific date, run the following query:
    
    
    SELECT * FROM `PROJECT_ID.BIGQUERY_DATASET.Patients`
      WHERE DATE(lastUpdated) = 'YYYY-MM-DD'

## Migrate from Analytics to Analytics V2

You can't migrate an existing BigQuery dataset from the `Analytics` schema to the `Analytics V2` schema using any method, including the following:

  * [Changing the schema type](https://docs.cloud.google.com/bigquery/docs/managing-table-schemas) of the table in BigQuery.
  * Changing the schema type in an existing FHIR streaming configuration.



This is because the BigQuery table columns for [FHIR extensions](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-extensions) in the `Analytics` schema have their mode set to `NULLABLE`, whereas those in the `Analytics V2` schema have them set to `REPEATED`. BigQuery doesn't allow changing the mode of a column from `NULLABLE` to `REPEATED`. Therefore, the two schema types are incompatible.

To migrate the schema type of the exported FHIR resources from `Analytics` to `Analytics V2`, you must export the FHIR resources to a new BigQuery dataset using a new streaming configuration with the updated schema type. To do so, perform the following steps:

  1. [Create a new BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets).

  2. [Set permissions for the BigQuery dataset](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery#setting_bigquery_permissions).

  3. [Add a new streaming configuration to the FHIR store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bigquery-streaming#configure_streaming_on_a_fhir_store) with the schema type set to `Analytics V2`.

  4. Backfill existing data by exporting the existing FHIR data using the following settings. See [exporting FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery#exporting_fhir_resources) for instructions on how to configure these settings using the Google Cloud console, the Google Cloud CLI, or the REST API. The following settings apply to the REST API:

     * Set [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#writedisposition) to [`WRITE_APPEND`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#WriteDisposition.ENUM_VALUES.WRITE_APPEND) to append the data to the destination table.
     * Set [`SchemaType`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#schematype) to [`ANALYTICS_V2`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#SchemaType.ENUM_VALUES.ANALYTICS_V2).



The views in BigQuery that correspond to some or all FHIR resources in the original BigQuery dataset might be missing from your new dataset. To troubleshoot this, see Missing FHIR resource view creation.

**Note:** The original BigQuery dataset that uses the `Analytics` schema is unaffected and continues to receive updates from the FHIR store. If you no longer need the original BigQuery dataset, first delete the original streaming configuration with the `Analytics` schema and then delete the original BigQuery dataset.

## Troubleshooting FHIR streaming

If errors occur when resource changes are sent to BigQuery, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

### Cannot convert column from NULLABLE to REPEATED

This error is caused by a repeated extension. To resolve this error, use the [`ANALYTICS_V2`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#SchemaType.ENUM_VALUES.ANALYTICS_V2) schema type. If you're already using `ANALYTICS_V2`, you might have a conflict between two extensions, or a conflict between an extension and another field.

Column names are generated from the text after the last `/` character in extension URLs. If an extension URL ends with a value like `/resource_field name`, a conflict can occur.

To prevent this error from occurring again, don't use extensions if their field names are the same as the resource fields you're populating. 

### Missing FHIR resource view creation

If you [bulk export](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery) a FHIR resource to BigQuery before streaming that FHIR resource, BigQuery does not create views for the FHIR resource.

For example, you might not see any views for Encounter resources in the following situation:

  1. You configure BigQuery streaming on a FHIR store, and then use the REST API to create a Patient resource.

BigQuery creates a table and a view for the Patient resource.

  2. You bulk export Encounter resources to the same BigQuery dataset as the previous step.

BigQuery creates a table for the Encounter resources.

  3. You use the REST API to create an Encounter resource.

After this step, BigQuery views are not created for the Encounter resource.




To resolve this issue, use the following query to [create a view](https://cloud.google.com/bigquery/docs/views#creating_a_view):
    
    
    SELECT
        * EXCEPT (_resource_row_id)
    FROM (
      SELECT
        ROW_NUMBER() OVER(PARTITION BY id ORDER BY meta.lastUpdated DESC, commitTimestamp DESC) as _resource_row_id,
        *
        FROM `PROJECT_ID.BIGQUERY_DATASET_ID.RESOURCE_TABLE` AS p
    ) AS p
    WHERE
      p._resource_row_id=1
      AND
      NOT EXISTS (
      SELECT
        *
      FROM
        UNNEST(p.meta.tag)
      WHERE
        code = 'DELETE');

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * BIGQUERY_DATASET_ID: the ID of the BigQuery dataset where you bulk exported the FHIR resource
  * RESOURCE_TABLE: the name of the table corresponding to the FHIR resource that you want to create views for



After creating the view, you can continue to stream changes to the FHIR resource and the view is updated accordingly.

## What's next

For a tutorial on a use case for streaming FHIR resource changes, see [Stream and synchronize FHIR resources with BigQuery](https://docs.cloud.google.com/healthcare-api/docs/tutorials/fhir-bigquery-streaming-tutorial).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
