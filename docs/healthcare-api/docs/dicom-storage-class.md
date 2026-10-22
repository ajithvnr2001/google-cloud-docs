---
url: https://docs.cloud.google.com/healthcare-api/docs/dicom-storage-class/
title: DICOM storage classes \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:42.624172+00:00
---

# DICOM storage classes  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/dicom-storage-class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  DICOM storage classes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage DICOM data in the Cloud Healthcare API using different storage classes. Choosing the right storage class can help you reduce costs and meet regulatory requirements for data retention.

This page is intended for technical users already familiar with DICOM and the Cloud Healthcare API.

## Overview

DICOM storage classes function similarly to [Cloud Storage storage classes](https://docs.cloud.google.com/storage/docs), offering different cost and performance characteristics based on how frequently you access your data and how long you need to store it. For more information about each storage class, see [Class descriptions](https://docs.cloud.google.com/storage/docs/storage-classes).

You might want to change the storage class of DICOM objects depending on how often you access the object or how long the object needs to be kept. For example:

  * You can move rarely accessed DICOM images from Standard storage to Nearline or Coldline storage to save on billing costs.
  * You can move patient data that needs to be kept for legal reasons to Archive storage, which is the cheapest and most durable storage class.



### Available DICOM storage classes

You can use the following storage classes for your DICOM objects:

  * Standard (Default)
  * Nearline
  * Coldline
  * Archive



### Storage class pricing

Each storage class has its own pricing structure. Changing the storage class of your DICOM objects might impact your billing costs. For more information, see the following:

  * [DICOM data storage pricing](https://cloud.google.com/healthcare-api/pricing#dicom_data_storage)
  * [DICOM data retrieval pricing](https://cloud.google.com/healthcare-api/pricing#dicom_data_retrieval)



## Change storage class for individual DICOM objects

You can change the storage class of DICOM objects at the study, series, or instance level.

The following samples show how to change the storage class of a DICOM instance.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles:

**Permissions**

  * `healthcare.dicomStores.dicomWebWrite`



**Roles**

  * [Healthcare DICOM Store Administrator (`roles/healthcare.dicomStoreAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.dicomEditor)



You can ask your administrator to grant you these Identity and Access Management roles. For instructions on granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [Control access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access#using_cloud_iam_with_datasets). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note** : If you created a Google Cloud project for this guide, then, as the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which has the permissions. You don't need to be granted any additional IAM roles. 

### REST

  1. Change the storage class of the DICOM instance using the [`projects.locations.datasets.dicomStores.studies.series.instances.setBlobStorageSettings`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.dicomWeb.studies/setBlobStorageSettings) method.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the DICOM store's parent dataset
     * `DICOM_STORE_ID`: the DICOM store ID
     * `STUDY_INSTANCE_UID`: the study instance unique identifier
     * `SERIES_INSTANCE_UID`: the series instance unique identifier
     * `INSTANCE_UID`: the instance unique identifier 
     * `STORAGE_CLASS`: the storage class for the DICOM instance. One of `STANDARD`, `NEARLINE`, `COLDLINE`, or `ARCHIVE`.

Request JSON body: 
    
    {
      "blobStorageSettings": {
        "blobStorageClass": "STORAGE_CLASS"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "blobStorageSettings": {
        "blobStorageClass": "STORAGE_CLASS"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID:setBlobStorageSettings"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "blobStorageSettings": {
        "blobStorageClass": "STORAGE_CLASS"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID:setBlobStorageSettings" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances/setBlobStorageSettings). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) (LRO). Long-running operations are returned when method calls might take additional time to complete. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    
    

  2. Get the status of the long-running operation using the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the DICOM store's parent dataset
     * `OPERATION_ID`: the ID returned from the long-running operation

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

The output is the following. When the response contains `"done": true`, the LRO has finished. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.storageinfo.StorageInfoService.SetBlobStorageSettings",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL,
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty"
      }
    }
    




## Change storage class for multiple objects using a filter file

The following sections show how to create and use a filter file to change the storage class of DICOM objects based on a filter criteria.

### Filter file requirements

  * Each line in the filter file defines the study, series, or instance and uses the format `/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID`.
  * You can truncate a line to specify the level at which the filter works. For example, you can select an entire study by specifying `/studies/STUDY_INSTANCE_UID`, or you can select an entire series by specifying `/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID`.



Consider the following filter file:
    
    
    /studies/1.123.456.789
    /studies/1.666.333.111/series/123.456
    /studies/1.666.333.111/series/567.890
    /studies/1.888.999.222/series/123.456/instances/111
    /studies/1.888.999.222/series/123.456/instances/222
    /studies/1.888.999.222/series/123.456/instances/333
    

This example filter file applies to the following:

  * The entire study with the study instance UID as `1.123.456.789`
  * Two separate series with series instance UIDs as `123.456` and `567.890` in the study `1.666.333.111`
  * Three individual instances with instance IDs as `111`, `222`, and `333` in the study `1.888.999.222` and series `123.456`



### Create a filter file using BigQuery

To create a filter file using BigQuery, you must first [export the metadata of your DICOM store to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery). The exported metadata shows you the study, series, and instance UIDs of the DICOM data in your DICOM store.

After exporting the metadata, complete the following steps:

  1. Run a query to return the UIDs of the study, series, and instances you want to add to the filter file.

For example, the following query shows how to concatenate the study, series, and instance UIDs to match the filter file format requirements:
         
         SELECT CONCAT
             ('/studies/', StudyInstanceUID, '/series/', SeriesInstanceUID, '/instances/', SOPInstanceUID)
         FROM
             [PROJECT_ID:BIGQUERY_DATASET.BIGQUERY_TABLE]

  2. Optional: If the query returns a large result set that exceed the [maximum response size](https://docs.cloud.google.com/bigquery/quotas#query_jobs), [save the query results to a new destination table](https://docs.cloud.google.com/bigquery/docs/writing-results#large-results) in BigQuery.

  3. Save the query results to a file and export it to Cloud Storage. If you saved your query results to a new destination table in Step 2, see [Exporting table data](https://docs.cloud.google.com/bigquery/docs/exporting-data) to export the table's contents to Cloud Storage.

  4. Edit the exported file as necessary, and include it your request to change the storage class of multiple DICOM objects.




### Create a filter file manually

To create a filter file manually, do the following:

  1. Create a filter file containing the DICOM objects you're filtering on.
  2. Upload the filter file to Cloud Storage. For instructions, see [Upload objects from a file system](https://docs.cloud.google.com/storage/docs/uploading-objects).



### Use a filter file

The following samples show how to apply a filter file when changing the storage class of DICOM objects.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles:

**Permissions**

  * `healthcare.dicomStores.dicomWebWrite`



**Roles**

  * [Healthcare DICOM Store Administrator (`roles/healthcare.dicomStoreAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.dicomEditor)



Grant the [**Storage Object Viewer** (`storage.objectViewer`)](https://docs.cloud.google.com/healthcare-api/docs/permissions-healthcare-api-gcp-products#dicom_store_cloud_storage_permissions) role to the **Cloud Healthcare Service Agent** service account.

You can ask your administrator to grant you these Identity and Access Management roles. For instructions on granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [Control access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access#using_cloud_iam_with_datasets). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note** : If you created a Google Cloud project for this guide, then, as the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which has the permissions. You don't need to be granted any additional IAM roles. 

### REST

  1. Change the storage class of the DICOM instances in the filter file using the [`projects.locations.datasets.dicomStores.studies.series.instances.setBlobStorageSettings`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.dicomWeb.studies/setBlobStorageSettings) method.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the DICOM store's parent dataset
     * `DICOM_STORE_ID`: the DICOM store ID
     * `STORAGE_CLASS`: the storage class for the DICOM objects. One of `STANDARD`, `NEARLINE`, `COLDLINE`, or `ARCHIVE`.
     * `CLOUD_STORAGE_BUCKET`: the name of the Cloud Storage bucket containing the filter file
     * `FILTER_FILE_PATH`: the fully qualified URI to the filter file in the Cloud Storage bucket

Request JSON body: 
    
    {
      "blobStorageSettings": {
        "blobStorageClass": "STORAGE_CLASS"
      },
      "filterConfig": {
        "resourcePathsGcsUri": "gs://CLOUD_STORAGE_BUCKET/FILTER_FILE_PATH"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "blobStorageSettings": {
        "blobStorageClass": "STORAGE_CLASS"
      },
      "filterConfig": {
        "resourcePathsGcsUri": "gs://CLOUD_STORAGE_BUCKET/FILTER_FILE_PATH"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:setBlobStorageSettings"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "blobStorageSettings": {
        "blobStorageClass": "STORAGE_CLASS"
      },
      "filterConfig": {
        "resourcePathsGcsUri": "gs://CLOUD_STORAGE_BUCKET/FILTER_FILE_PATH"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:setBlobStorageSettings" | Select-Object -Expand Content

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) (LRO). Long-running operations are returned when method calls might take additional time to complete. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    
    

  2. Get the status of the long-running operation using the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the DICOM store's parent dataset
     * `OPERATION_ID`: the ID returned from the long-running operation

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

The output is the following. When the response contains `"done": true`, the LRO has finished. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.storageinfo.StorageInfoService.SetBlobStorageSettings",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL,
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty"
      }
    }
    




## View a DICOM object's storage class

You can view the storage class of DICOM objects at the study, series, or instance level.

The following sections describe how to view the storage class of a DICOM instance.

### Get storage class information for a DICOM object

The following samples show how to use the [`instances.getStorageInfo`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.dicomWeb.studies.series.instances/getStorageInfo) method to view the storage class of DICOM objects.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles:

**Permissions**

  * `healthcare.dicomStores.dicomWebRead`



**Roles**

  * [Healthcare DICOM Viewer (`roles/healthcare.dicomStoreViewer`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.dicomViewer)



You can ask your administrator to grant you these Identity and Access Management roles. For instructions on granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [Control access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access#using_cloud_iam_with_datasets). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note** : If you created a Google Cloud project for this guide, then, as the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which has the permissions. You don't need to be granted any additional IAM roles. 

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `STUDY_INSTANCE_UID`: the study instance unique identifier
  * `SERIES_INSTANCE_UID`: the series instance unique identifier
  * `INSTANCE_UID`: the instance unique identifier 



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID:getStorageInfo"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID:getStorageInfo" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.dicomWeb.studies.series.instances.getStorageInfo). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID"
    }
    

### Query exported DICOM metadata in BigQuery

You can [export DICOM metadata to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery) and then run queries to view the storage classes of your exported DICOM objects.

The following query shows how to retrieve the study instance UID, series instance UID, instance UID, storage size, and storage class of up to 1,000 DICOM instances from a BigQuery dataset:
    
    
    SELECT StudyInstanceUID, SeriesInstanceUID, SOPInstanceUID, BlobStorageSize, StorageClass
    FROM PROJECT_ID:BIGQUERY_DATASET.BIGQUERY_TABLE
    LIMIT 1000

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `BIGQUERY_DATASET`: the parent BigQuery dataset of the table containing the exported DICOM metadata
  * `BIGQUERY_TABLE`: the BigQuery table containing the exported DICOM metadata



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
