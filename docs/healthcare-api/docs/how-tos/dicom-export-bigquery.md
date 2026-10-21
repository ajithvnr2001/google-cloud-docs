---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery/
title: Exporting DICOM metadata to BigQuery \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:01:46.946170+00:00
---

# Exporting DICOM metadata to BigQuery  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Exporting DICOM metadata to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to export DICOM metadata to BigQuery for exploration and analysis. For information on the BigQuery schema that is created when exporting DICOM metadata, see [Understanding the BigQuery DICOM schema](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-bigquery-schema).

## Setting BigQuery permissions

Before exporting DICOM metadata to a BigQuery table, you must grant extra permissions to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [DICOM store BigQuery permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_store_bigquery_permissions).

## Setting the BigQuery destination

When setting the BigQuery destination, use the fully qualified URI, like so: 
    
    
    bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID
    

The behavior of the export operation can vary depending on: 

  * Whether the destination table already exists
  * Whether you have set the `force` field (using the API) or the `--overwrite-table` flag (using the Google Cloud CLI)
  * Whether you have set a value for the [`writeDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores#WriteDisposition) enum. If you use the `writeDisposition` enum, do not set the `force` field.

The behavior in each of these cases is as follows: 
  * If the destination table already exists and `force` is set to `true` or the `--overwrite-table` flag is specified, the export operation overwrites the existing table.
  * If the destination table already exists and `force` is set to `false` or the `--overwrite-table` flag is not specified, an error occurs.
  * If the destination table does not already exist, then a new table is created, regardless of whether you specify the `force` field or the `--overwrite-table` flag.
  * The behavior for `writeDisposition` is described in its [documentation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores#WriteDisposition). The `writeDisposition` enum performs behavior similar to the options when using `force`, with the following exception: if the destination table already exists, and is empty, the export operation completes instead of returning an error.



## Exporting DICOM metadata

The following samples show how to export DICOM metadata to a BigQuery table. In these samples, the DICOM store and the BigQuery table are in the same project. To export DICOM metadata to a BigQuery table in another project, see Exporting DICOM metadata to a different project.

### Console

To export DICOM metadata to a BigQuery table, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the dataset that has the DICOM store with the metadata you're exporting.

  3. In the same row as the DICOM store, open the **Actions** list and select **Export**.

  4. On the **Export DICOM store** page that appears, select **BigQuery table**.

  5. In the **Project** field, click **Browse** , and select your project.

  6. In the **Dataset** list, select the BigQuery dataset where you're exporting DICOM metadata.

  7. In the **Table** field, enter a new table name. BigQuery checks each selection to ensure that the destination table is valid.

  8. In the **Destination table write disposition** section, select one of the following. These options correspond to the [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export#WriteDisposition) enum.

     * **Only export data if the destination table is empty** : Equivalent to [`WRITE_EMPTY`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export#WriteDisposition.ENUM_VALUES.WRITE_EMPTY)
     * **Append data to destination table** : Equivalent to [`WRITE_APPEND`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export#WriteDisposition.ENUM_VALUES.WRITE_EMPTY)
     * **Erase all existing data in the destination table before writing the instances** : Equivalent to [`WRITE_TRUNCATE`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export#WriteDisposition.ENUM_VALUES.WRITE_EMPTY).
  9. Click **Export** to export DICOM metadata to the BigQuery table. 

  10. To track the status of the operation, click the **Operations** tab. After the operation completes, the following indications appear: 
     * The **Long-running operation status** section has a green check mark under the **OK** heading.
     * The **Overview** section has a green check mark and an **OK** indicator in the same row as the operation ID.
If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**. 



### gcloud

To export DICOM metadata to a BigQuery table, run the [`gcloud healthcare dicom-stores export bq`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq) command.

  1. Export the DICOM metadata.

Before using any of the command data below, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the DICOM store's parent dataset
     * DICOM_STORE_ID: the DICOM store ID
     * BIGQUERY_DATASET_ID: the name of an existing BigQuery dataset where you're exporting DICOM metadata
     * BIGQUERY_TABLE_ID: the name of a new or existing table in the BigQuery dataset. If the export operation is creating a new table, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming) for table name requirements.
     * WRITE_DISPOSITION: a value for the [`WriteDisposition`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#--write-disposition) enum. Use one of the following values: 
       * `write-empty`: only export data if the BigQuery table is empty.
       * `write-truncate`: erase all existing data in the BigQuery table before writing the DICOM instances.
       * `write-append`: append data to the BigQuery table.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare dicom-stores export bq DICOM_STORE_ID \
      --location=LOCATION \
      --dataset=DATASET_ID \
      --bq-table=bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID \
      --write-disposition=WRITE_DISPOSITION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare dicom-stores export bq DICOM_STORE_ID `
      --location=LOCATION `
      --dataset=DATASET_ID `
      --bq-table=bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID `
      --write-disposition=WRITE_DISPOSITION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare dicom-stores export bq DICOM_STORE_ID ^
      --location=LOCATION ^
      --dataset=DATASET_ID ^
      --bq-table=bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID ^
      --write-disposition=WRITE_DISPOSITION

The response is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations). Long-running operations are returned when method calls might take a substantial amount of time to complete. The command polls the long-running operation, then prints the name of the operation in the `name` field after the export finishes. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    Request issued for: [DICOM_STORE_ID]
    Waiting for operation [projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID] to complete...⠏
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    

  2. To view more details about the operation, run the [`gcloud healthcare operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/describe) command and provide the OPERATION_ID from the response:

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
      apiMethodName: 'google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData_bq'
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
      '@type': 'type.googleapis.com/google.protobuf.Empty'
    




### REST

To export DICOM metadata to a BigQuery table, use the [`projects.locations.datasets.dicomStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export) method.

  1. Export the DICOM metadata.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the DICOM store's parent dataset
     * DICOM_STORE_ID: the DICOM store ID
     * BIGQUERY_DATASET_ID: the name of an existing BigQuery dataset where you're exporting DICOM metadata
     * BIGQUERY_TABLE_ID: the name of a new or existing table in the BigQuery dataset. If the export operation is creating a new table, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming) for table name requirements.
     * WRITE_DISPOSITION: a value for the [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export#WriteDisposition) enum. Use one of the following values: 
       * `WRITE_EMPTY`: only export data if the BigQuery table is empty.
       * `WRITE_TRUNCATE`: erase all existing data in the BigQuery table before writing the DICOM instances.
       * `WRITE_APPEND`: append data to the BigQuery table.

Request JSON body: 
    
    {
      "bigqueryDestination": {
          "tableUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID",
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
          "tableUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID",
          "writeDisposition": "WRITE_DISPOSITION"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "bigqueryDestination": {
          "tableUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID",
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:export" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

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
        "apiMethodName": "google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData_bq",
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
        "@type": "type.googleapis.com/google.protobuf.Empty",
        
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
    




## Exporting DICOM metadata to a different project

**Note:** In this section, the terms _different project_ and _destination project_ are synonymous.

To export DICOM metadata from a DICOM store in one project to a BigQuery dataset in another project, first see [Exporting DICOM metadata to a different project permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_export_different_project) for information on how to set IAM permissions in the destination project.

### gcloud

To export DICOM metadata from a DICOM store in one project to a BigQuery table in another project, use the [`gcloud healthcare dicom-stores export bq`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq) command.

  1. Export the DICOM metadata.

Before using any of the command data below, make the following replacements: 

     * SOURCE_PROJECT_ID: the ID of the source Google Cloud project
     * SOURCE_LOCATION: the source dataset location
     * SOURCE_DATASET_ID: the source DICOM store's parent dataset
     * SOURCE_DICOM_STORE_ID: the source DICOM store ID
     * DESTINATION_PROJECT_ID: the ID of the different project
     * DESTINATION_BIGQUERY_DATASET_ID: the name of an existing BigQuery dataset in the destination project where you're exporting DICOM metadata
     * DESTINATION_BIGQUERY_TABLE_ID: the name of a new or existing table in the BigQuery dataset. If the export operation is creating a new table, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming) for table name requirements.
     * WRITE_DISPOSITION: a value for the [`WriteDisposition`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#--write-disposition) enum. Use one of the following values: 
       * `write-empty`: only export data if the BigQuery table is empty.
       * `write-truncate`: erase all existing data in the BigQuery table before writing the DICOM instances.
       * `write-append`: append data to the BigQuery table.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare dicom-stores export bq SOURCE_DICOM_STORE_ID \
      --project=SOURCE_PROJECT_ID \
      --location=SOURCE_LOCATION \
      --dataset=SOURCE_DATASET_ID \
      --bq-table=bq://DESTINATION_PROJECT_ID.DESTINATION_BIGQUERY_DATASET_ID.DESTINATION_BIGQUERY_TABLE_ID \
      --write-disposition=WRITE_DISPOSITION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare dicom-stores export bq SOURCE_DICOM_STORE_ID `
      --project=SOURCE_PROJECT_ID `
      --location=SOURCE_LOCATION `
      --dataset=SOURCE_DATASET_ID `
      --bq-table=bq://DESTINATION_PROJECT_ID.DESTINATION_BIGQUERY_DATASET_ID.DESTINATION_BIGQUERY_TABLE_ID `
      --write-disposition=WRITE_DISPOSITION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare dicom-stores export bq SOURCE_DICOM_STORE_ID ^
      --project=SOURCE_PROJECT_ID ^
      --location=SOURCE_LOCATION ^
      --dataset=SOURCE_DATASET_ID ^
      --bq-table=bq://DESTINATION_PROJECT_ID.DESTINATION_BIGQUERY_DATASET_ID.DESTINATION_BIGQUERY_TABLE_ID ^
      --write-disposition=WRITE_DISPOSITION

The response is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations). Long-running operations are returned when method calls might take a substantial amount of time to complete. The command polls the long-running operation, then prints the name of the operation in the `name` field after the export finishes. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    Request issued for: [SOURCE_DICOM_STORE_ID]
    Waiting for operation [projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID] to complete...⠏
    name: projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID
    

  2. To view more details about the operation, run the [`gcloud healthcare operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/describe) command and provide the OPERATION_ID from the response:

Before using any of the command data below, make the following replacements: 

     * SOURCE_PROJECT_ID: the ID of the source Google Cloud project
     * SOURCE_LOCATION: the source dataset location
     * SOURCE_DATASET_ID: the source dataset ID
     * OPERATION_ID: the ID returned from the long-running operation

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare operations describe OPERATION_ID \
        --project=SOURCE_PROJECT_ID \
        --dataset=SOURCE_DATASET_ID \
        --location=SOURCE_LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare operations describe OPERATION_ID `
        --project=SOURCE_PROJECT_ID `
        --dataset=SOURCE_DATASET_ID `
        --location=SOURCE_LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud healthcare operations describe OPERATION_ID ^
        --project=SOURCE_PROJECT_ID ^
        --dataset=SOURCE_DATASET_ID ^
        --location=SOURCE_LOCATION

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
      apiMethodName: 'google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData_bq'
      counter:
        success: 'SUCCESS_COUNT'
        // If there were any failures, they display in the `failure` field.
        failure: 'FAILURE_COUNT'
      createTime: 'YYYY-MM-DDTHH:MM:SS+ZZ:ZZ'
      endTime: 'YYYY-MM-DDTHH:MM:SS+ZZ:ZZ'
      logsUrl: https://console.cloud.google.com/CLOUD_LOGGING_URL
    name: projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID
    // The `response` field only displays if there were no errors.
    response:
      '@type': 'type.googleapis.com/google.protobuf.Empty'
    




### REST

To export DICOM metadata from a DICOM store in one project to a BigQuery table in another project, use the [`projects.locations.datasets.dicomStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export) method.

  1. Export the DICOM metadata.

Before using any of the request data, make the following replacements: 

     * SOURCE_PROJECT_ID: the ID of the source Google Cloud project
     * SOURCE_LOCATION: the source dataset location
     * SOURCE_DATASET_ID: the source DICOM store's parent dataset
     * SOURCE_DICOM_STORE_ID: the source DICOM store ID
     * DESTINATION_PROJECT_ID: the ID of the different project
     * DESTINATION_BIGQUERY_DATASET_ID: the name of an existing BigQuery dataset in the destination project where you're exporting DICOM metadata
     * DESTINATION_BIGQUERY_TABLE_ID: the name of a new or existing table in the BigQuery dataset. If the export operation is creating a new table, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming) for table name requirements.
     * WRITE_DISPOSITION: a value for the [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export#WriteDisposition) enum. Use one of the following values: 
       * `WRITE_EMPTY`: only export data if the BigQuery table is empty.
       * `WRITE_TRUNCATE`: erase all existing data in the BigQuery table before writing the DICOM instances.
       * `WRITE_APPEND`: append data to the BigQuery table.

Request JSON body: 
    
    {
      "bigqueryDestination": {
          "tableUri": "bq://DESTINATION_PROJECT_ID.DESTINATION_BIGQUERY_DATASET_ID.DESTINATION_BIGQUERY_TABLE_ID",
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
          "tableUri": "bq://DESTINATION_PROJECT_ID.DESTINATION_BIGQUERY_DATASET_ID.DESTINATION_BIGQUERY_TABLE_ID",
          "writeDisposition": "WRITE_DISPOSITION"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/dicomStores/SOURCE_DICOM_STORE_ID:export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "bigqueryDestination": {
          "tableUri": "bq://DESTINATION_PROJECT_ID.DESTINATION_BIGQUERY_DATASET_ID.DESTINATION_BIGQUERY_TABLE_ID",
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
        -Uri "https://healthcare.googleapis.com/v1/projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/dicomStores/SOURCE_DICOM_STORE_ID:export" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) (LRO). Long-running operations are returned when method calls might take additional time to complete. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

  2. Use the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method to get the status of the long-running operation.

Before using any of the request data, make the following replacements: 

     * SOURCE_PROJECT_ID: the ID of the source Google Cloud project
     * SOURCE_LOCATION: the source dataset location
     * SOURCE_DATASET_ID: the source dataset ID
     * OPERATION_ID: the ID returned from the long-running operation

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The output is the following. When the response contains `"done": true`, the long-running operation has finished. 

#### Response
    
    {
      "name": "projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData_bq",
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
        "@type": "type.googleapis.com/google.protobuf.Empty",
        
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
    




## Exporting DICOM metadata using filters

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, when you export DICOM files to Cloud Storage, all of the DICOM files in the specified DICOM store are exported. Similarly, when you export DICOM metadata to BigQuery, the metadata for all of the DICOM data in the specified DICOM store is exported. 

You can export a subset of DICOM data or metadata using a filter. You define the filter in a _filter file_. 

###  Configuring filter files 

A filter file defines which DICOM files to export to Cloud Storage or BigQuery. You can configure filter files at the following levels: 

  * At the study level
  * At the series level
  * At the instance level



The filter file is made up of multiple lines with each line defining the study, series, or instance you want to export. Each line uses the format `/studies/STUDY_UID[/series/SERIES_UID[/instances/INSTANCE_UID]]`. 

If a study, series, or instance is not specified in the filter file when you pass in the filter file, that study, series, or instance will not be exported. 

Only the `/studies/STUDY_UID` portion of the path is required. You can export an entire study by specifying `/studies/STUDY_UID`, or you can export an entire series by specifying `/studies/STUDY_UID/series/SERIES_UID`. 

Consider the following filter file. The filter file will result in one study, two series, and three individual instances being exported: 
    
    
    /studies/1.123.456.789
    /studies/1.666.333.111/series/123.456
    /studies/1.666.333.111/series/567.890
    /studies/1.888.999.222/series/123.456/instances/111
    /studies/1.888.999.222/series/123.456/instances/222
    /studies/1.888.999.222/series/123.456/instances/333
    

### Creating a filter file using BigQuery

You typically create a filter file by first exporting the metadata from a DICOM store to BigQuery. This lets you use BigQuery to view the study, series, and instance UIDs of the DICOM data in your DICOM store. You can then complete the following steps: 

  1. Query for the study, series, and instance UIDs you are interested in. For example, after exporting DICOM metadata to BigQuery, you could run the following query to concatenate the study, series, and instance UIDs to a format that's compatible with the filter file requirements: 
         
         SELECT CONCAT
             ('/studies/', StudyInstanceUID, '/series/', SeriesInstanceUID, '/instances/', SOPInstanceUID)
         FROM
             [PROJECT_ID:BIGQUERY_DATASET.BIGQUERY_TABLE]

  2. If the query returns a large result set, you can materialize a new table by [saving the query results to a destination table in BigQuery](https://docs.cloud.google.com/bigquery/docs/writing-results#large-results). 
  3. If you saved the query results to a destination table, you can save the contents of the destination table to a file and export it to Cloud Storage. For steps on how to do so, see [Exporting table data](https://docs.cloud.google.com/bigquery/docs/exporting-data). The exported file is your filter file. You use the location of the filter file in Cloud Storage when specifying the filter in the export operation. 



### Creating a filter file manually

You can create a filter file with custom content and [upload it to a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects). You use the location of the filter file in Cloud Storage when specifying the filter in the export operation. The following sample shows how to upload a filter file to a Cloud Storage bucket using the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command: 
    
    
    gcloud storage cp FILTER_FILE gs://BUCKET

### Passing in the filter file

After you create a filter file, you can call the DICOM export operation and pass in the filter file using the REST API. The following samples show how to export DICOM metadata using a filter.

### gcloud

**Note:** Exporting DICOM metadata to a BigQuery table using a filter using the Google Cloud CLI is only available in beta.

To export DICOM metadata to a BigQuery table using a filter, run the [`gcloud beta healthcare dicom-stores export bq`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/dicom-stores/export/bq) command.

  1. Export the DICOM metadata.

Before using any of the command data below, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the DICOM store's parent dataset
     * DICOM_STORE_ID: the DICOM store ID
     * BIGQUERY_DATASET_ID: the name of an existing BigQuery dataset where you're exporting DICOM metadata
     * BIGQUERY_TABLE_ID: the name of a new or existing table in the BigQuery dataset. If the export operation is creating a new table, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming) for table name requirements.
     * BUCKET: the name of the Cloud Storage bucket containing the filter file. If the filter file is in a directory, include the directory in the path.
     * FILTER_FILE: the location and name of the filter file in a Cloud Storage bucket
     * WRITE_DISPOSITION: a value for the [`WriteDisposition`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/bq#--write-disposition) enum. Use one of the following values: 
       * `write-empty`: only export data if the BigQuery table is empty.
       * `write-truncate`: erase all existing data in the BigQuery table before writing the DICOM instances.
       * `write-append`: append data to the BigQuery table.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta healthcare dicom-stores export bq DICOM_STORE_ID \
      --location=LOCATION \
      --dataset=DATASET_ID \
      --bq-table=bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID \
      --filter-config-gcs-uri=gs://BUCKET/FILTER_FILE \
      --write-disposition=WRITE_DISPOSITION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta healthcare dicom-stores export bq DICOM_STORE_ID `
      --location=LOCATION `
      --dataset=DATASET_ID `
      --bq-table=bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID `
      --filter-config-gcs-uri=gs://BUCKET/FILTER_FILE `
      --write-disposition=WRITE_DISPOSITION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta healthcare dicom-stores export bq DICOM_STORE_ID ^
      --location=LOCATION ^
      --dataset=DATASET_ID ^
      --bq-table=bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID ^
      --filter-config-gcs-uri=gs://BUCKET/FILTER_FILE ^
      --write-disposition=WRITE_DISPOSITION

The response is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations). Long-running operations are returned when method calls might take a substantial amount of time to complete. The command polls the long-running operation, then prints the name of the operation in the `name` field after the export finishes. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    Request issued for: [DICOM_STORE_ID]
    Waiting for operation [projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID] to complete...⠏
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    

  2. To view more details about the operation, run the [`gcloud healthcare operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/describe) command and provide the OPERATION_ID from the response:

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
      apiMethodName: 'google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData_bq'
      counter:
        success: 'SUCCESS_COUNT'
        // If there were any failures, they display in the `failure` field.
        failure: 'FAILURE_COUNT'
      createTime: 'YYYY-MM-DDTHH:MM:SS+ZZ:ZZ'
      endTime: 'YYYY-MM-DDTHH:MM:SS+ZZ:ZZ'
      logsUrl: https://console.cloud.google.com/CLOUD_LOGGING_URL
    name: projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID
    // The `response` field only displays if there were no errors.
    response:
      '@type': 'type.googleapis.com/google.protobuf.Empty'
    




### REST

To export DICOM metadata to a BigQuery table using a filter, use the [`projects.locations.datasets.dicomStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export) method.

  1. Export the DICOM metadata.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the DICOM store's parent dataset
     * DICOM_STORE_ID: the DICOM store ID
     * BIGQUERY_DATASET_ID: the name of an existing BigQuery dataset where you're exporting DICOM metadata
     * BIGQUERY_TABLE_ID: the name of a new or existing table in the BigQuery dataset. If the export operation is creating a new table, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming) for table name requirements.
     * BUCKET: the name of the Cloud Storage bucket containing the filter file. If the filter file is in a directory, include the directory in the path.
     * FILTER_FILE: the location and name of the filter file in a Cloud Storage bucket
     * WRITE_DISPOSITION: a value for the [`WriteDisposition`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export#WriteDisposition) enum. Use one of the following values: 
       * `WRITE_EMPTY`: only export data if the BigQuery table is empty.
       * `WRITE_TRUNCATE`: erase all existing data in the BigQuery table before writing the DICOM instances.
       * `WRITE_APPEND`: append data to the BigQuery table.

Request JSON body: 
    
    {
      "bigqueryDestination": {
          "tableUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID",
          "writeDisposition": "WRITE_DISPOSITION"
      },
      "filterConfig": {
          "resourcePathsGcsUri": "gs://BUCKET/FILTER_FILE"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "bigqueryDestination": {
          "tableUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID",
          "writeDisposition": "WRITE_DISPOSITION"
      },
      "filterConfig": {
          "resourcePathsGcsUri": "gs://BUCKET/FILTER_FILE"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "bigqueryDestination": {
          "tableUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID",
          "writeDisposition": "WRITE_DISPOSITION"
      },
      "filterConfig": {
          "resourcePathsGcsUri": "gs://BUCKET/FILTER_FILE"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:export" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

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
      "name": "projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData_bq",
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
        "@type": "type.googleapis.com/google.protobuf.Empty",
        
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
    




## Querying and analyzing DICOM data in BigQuery

After exporting the DICOM metadata to a BigQuery table, you can run sample queries to get more details about the metadata. The following samples show how to run queries for some common use cases.

### Searching across metadata

Suppose that you want to search across a large amount of metadata that is difficult to search for in other systems, such as a Picture Archiving and Communication System (PACS) or Vendor Neutral Archive (VNA). The following query shows how to query on a patient's `PatientID` value and use the DICOMweb path to retrieve specific image instances. The sample uses the [chc-nih-chest-xray.nih_chest_xray.nih_chest_xray](https://console.cloud.google.com/bigquery?p=chc-nih-chest-xray&t=nih_chest_xray&d=nih_chest_xray&page=table) table from the [NIH Chest X-ray dataset](https://docs.cloud.google.com/healthcare-api/docs/resources/public-datasets/nih-chest).
    
    
    #standardSQL
    SELECT CONCAT('/dicomWeb/studies/', StudyInstanceUID, '/series/', SeriesInstanceUID, '/instances/', SOPInstanceUID) as DICOMwebPath
    FROM `chc-nih-chest-xray.nih_chest_xray.nih_chest_xray`
    WHERE PatientID = '19045';
    

The query returns the studies associated with the patient. The following response uses JSON formatting:
    
    
    [
      {
        "DICOMwebPath": "/dicomWeb/studies/1.3.6.1.4.1.11129.5.5.169629990647803559688464142879817265366193/series/1.3.6.1.4.1.11129.5.5.141990184899344268273968625887396932057061/instances/1.3.6.1.4.1.11129.5.5.162448513493627342869165322873398445570578"
      },
      {
        "DICOMwebPath": "/dicomWeb/studies/1.3.6.1.4.1.11129.5.5.114160532832901355654444239008681456919023/series/1.3.6.1.4.1.11129.5.5.178361108150351071908200174504411112440700/instances/1.3.6.1.4.1.11129.5.5.145959606905209488520697484018030440952428"
      },
      {
        "DICOMwebPath": "/dicomWeb/studies/1.3.6.1.4.1.11129.5.5.177801331756958922168115732894519725643007/series/1.3.6.1.4.1.11129.5.5.134128639331055702643451404466208677561042/instances/1.3.6.1.4.1.11129.5.5.148534317486838863760908141408862094292875"
      },
      {
        "DICOMwebPath": "/dicomWeb/studies/1.3.6.1.4.1.11129.5.5.119570482687494886334491471870663517807852/series/1.3.6.1.4.1.11129.5.5.148050768676645373034111775531663876425927/instances/1.3.6.1.4.1.11129.5.5.111153708388576066195389700503245704293300"
      },
      {
        "DICOMwebPath": "/dicomWeb/studies/1.3.6.1.4.1.11129.5.5.144704399171290022427247626928443085419319/series/1.3.6.1.4.1.11129.5.5.190285793344339390593165731988543561416633/instances/1.3.6.1.4.1.11129.5.5.110245902713751842026864359179754889505217"
      },
      {
        "DICOMwebPath": "/dicomWeb/studies/1.3.6.1.4.1.11129.5.5.172276126220388966649736649950361623806435/series/1.3.6.1.4.1.11129.5.5.171512371498506519035489729484464872160452/instances/1.3.6.1.4.1.11129.5.5.111721417729733087384317002785068394901165"
      }
    ]
    

### Querying for the latest studies

Suppose that you want to populate a PACS reading worklist with the latest studies from your dataset.

The following query shows how to retrieve and display the latest studies along with instance counts and surrounding metadata. The sample uses the [bigquery-public-data.idc_v5.dicom_metadata](https://console.cloud.google.com/marketplace/product/bigquery-public-data/nci-idc-data) table from the [TCIA dataset](https://docs.cloud.google.com/healthcare-api/docs/resources/public-datasets/idc).
    
    
    #standardSQL
    SELECT
      MIN(CONCAT(StudyDate, ' ', StudyTime)) as StudyDateTime, MIN(PatientID) as PatientID, StudyInstanceUID, COUNT(*) as InstanceCount
    FROM
     `bigquery-public-data.idc_v5.dicom_metadata` AS dicom
    GROUP BY StudyInstanceUID
    ORDER BY StudyDateTime DESC
    LIMIT 10;
    

The query returns the following information:

  * The 10 latest studies that entered the system and when they entered the system
  * The patient associated with each study
  * The study's UID
  * The number of instances associated with the study



The following response uses JSON formatting:
    
    
    [
      {
        "StudyDateTime": "2021-07-11 00:38:22",
        "PatientID": "C3L-01924",
        "StudyInstanceUID": "1.3.6.1.4.1.5962.99.1.2466232160.763753303.1625963902816.3.0",
        "InstanceCount": "4"
      }, {
        "StudyDateTime": "2021-07-10 23:52:10",
        "PatientID": "C3L-01924",
        "StudyInstanceUID": "1.3.6.1.4.1.5962.99.1.2463459463.1074873794.1625961130119.3.0",
        "InstanceCount": "4"
      }, {
        "StudyDateTime": "2021-07-10 23:31:13",
        "PatientID": "C3L-02513",
        "StudyInstanceUID": "1.3.6.1.4.1.5962.99.1.2462202516.1453336368.1625959873172.3.0",
        "InstanceCount": "7"
      }, {
        "StudyDateTime": "2021-07-10 23:25:17",
        "PatientID": "C3L-01924",
        "StudyInstanceUID": "1.3.6.1.4.1.5962.99.1.2461846936.496969835.1625959517592.3.0",
        "InstanceCount": "4"
      }, {
        "StudyDateTime": "2021-07-10 22:35:16",
        "PatientID": "C3L-02515",
        "StudyInstanceUID": "1.3.6.1.4.1.5962.99.1.2458845347.1905567435.1625956516003.3.0",
        "InstanceCount": "6"
      }, {
        "StudyDateTime": "2021-07-10 21:49:46",
        "PatientID": "C3L-02515",
        "StudyInstanceUID": "1.3.6.1.4.1.5962.99.1.2456116127.1264613559.1625953786783.3.0",
        "InstanceCount": "7"
      }, {
        "StudyDateTime": "2021-07-10 21:46:04",
        "PatientID": "C3L-02513",
        "StudyInstanceUID": "1.3.6.1.4.1.5962.99.1.2455894080.1705479047.1625953564736.3.0",
        "InstanceCount": "6"
      }, {
        "StudyDateTime": "2021-07-10 21:13:30",
        "PatientID": "C3L-01924",
        "StudyInstanceUID": "1.3.6.1.4.1.5962.99.1.2453939652.2052768474.1625951610308.3.0",
        "InstanceCount": "4"
      }, {
        "StudyDateTime": "2021-07-10 21:10:17",
        "PatientID": "C3L-02515",
        "StudyInstanceUID": "1.3.6.1.4.1.5962.99.1.2453746219.164669562.1625951416875.3.0",
        "InstanceCount": "6"
      }, {
        "StudyDateTime": "2021-07-10 20:05:48",
        "PatientID": "C3L-02513",
        "StudyInstanceUID": "1.3.6.1.4.1.5962.99.1.2449877792.1996682667.1625947548448.3.0",
        "InstanceCount": "6"
      }
    ]
    

## Limitations and additional behavior

If the DICOM tag does not have a supported type in BigQuery (listed in [Excluded VRs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-bigquery-schema#excluded_vrs)), it is listed in a separate column (called `DroppedTags.TagName`) in the destination BigQuery table.

## Troubleshooting DICOM export requests

If errors occur during a DICOM export metadata to BigQuery request, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
