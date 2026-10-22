---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bulk-delete/
title: Bulk-deleting FHIR resources \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:50.064398+00:00
---

# Bulk-deleting FHIR resources  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bulk-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Bulk-deleting FHIR resources Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to bulk-delete FHIR resources from a FHIR store using a long-running operation.

You can delete multiple FHIR resources in a single operation based on filters like resource type and last updated time, or by providing a list of specific resource IDs in a Cloud Storage file. This is useful for data lifecycle management and cost savings.

## Before you begin

Before you can bulk-delete FHIR resources, ensure the following:

  * You must have the `healthcare.fhirStores.bulkDelete` permission on the FHIR store.
  * If you specify a `gcsDestination`, the **Cloud Healthcare Service Agent** service account must have the `roles/storage.objectAdmin` role on the destination bucket. For more information, see [FHIR store Cloud Storage permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#fhir_store_cloud_storage_permissions).
  * If you specify a `gcsSource`, the **Cloud Healthcare Service Agent** service account must have the `roles/storage.objectViewer` role on the source bucket. For more information, see [Bulk-deleting FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/permissions-healthcare-api-gcp-products#bulk-delete-fhir-resources).



## Bulk-deleting FHIR resources

To bulk-delete FHIR resources, use the `projects.locations.datasets.fhirStores.bulkDelete` method.

This method returns a long-running operation (LRO). You can track the status of the LRO using the operation name returned by the API call.

The following sample shows how to make a `POST` request to bulk-delete all `Observation` and `Encounter` resources in a FHIR store that were last updated before a specific timestamp.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the FHIR store's parent dataset
  * `FHIR_STORE_ID`: the FHIR store ID



Request JSON body: 
    
    
    {
      "type": "Observation,Encounter",
      "versionConfig": "ALL",
      "until": "2025-01-01T00:00:00Z",
      "gcsDestination": {
        "uriPrefix": "gs://BUCKET/DIRECTORY"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "type": "Observation,Encounter",
      "versionConfig": "ALL",
      "until": "2025-01-01T00:00:00Z",
      "gcsDestination": {
        "uriPrefix": "gs://BUCKET/DIRECTORY"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:bulkDelete"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "type": "Observation,Encounter",
      "versionConfig": "ALL",
      "until": "2025-01-01T00:00:00Z",
      "gcsDestination": {
        "uriPrefix": "gs://BUCKET/DIRECTORY"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:bulkDelete" | Select-Object -Expand Content

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations). Note the value of OPERATION_ID. You need this value in the next step. 

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

### Bulk-deleting FHIR resources by resource ID

To delete a specific list of FHIR resources, set the `gcsSource.uri` field to the Cloud Storage location of one or more files that contain the resource IDs to delete.

The input files must meet the following requirements:

  * Each line contains one resource in the format `RESOURCE_TYPE/RESOURCE_ID`, for example `Patient/8af1cf10-0fec-4bb3-bde1-77f56a3d8281`. Raw resource IDs without a resource type aren't supported.
  * The URI must point to a single file, such as `gs://BUCKET/ids.txt`, or a wildcard pattern, such as `gs://BUCKET/DIRECTORY/*.ndjson`. The URI can't be a bucket or a directory that ends in `/`.



The following content is an example of a valid input file:
    
    
    Patient/8af1cf10-0fec-4bb3-bde1-77f56a3d8281
    Observation/2c9d4a3e-6b1f-4e2a-9f0d-1a2b3c4d5e6f
    Encounter/7f3e2d1c-0b9a-4c8d-8e7f-6a5b4c3d2e1f
    

Note the following behavior:

  * The `gcsSource` field can't be used together with the `type` or `until` filters. If you specify `gcsSource` together with either filter, the request fails.
  * You can use `gcsSource` with `versionConfig` and `gcsDestination`.
  * Blank lines are ignored. Lines that don't match the `RESOURCE_TYPE/RESOURCE_ID` format or that contain an unsupported resource type are skipped, and the operation continues.
  * Resource IDs that don't exist in the FHIR store are skipped.
  * Don't modify or delete the input files until the operation completes.



The following sample shows how to make a `POST` request to bulk-delete the FHIR resources listed in a Cloud Storage file.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the FHIR store's parent dataset
  * `FHIR_STORE_ID`: the FHIR store ID
  * `BUCKET/PATH_TO_IDS_FILE`: the Cloud Storage location of the file, or wildcard pattern, that lists the resources to delete in the format `RESOURCE_TYPE/RESOURCE_ID`



Request JSON body: 
    
    
    {
      "versionConfig": "ALL",
      "gcsSource": {
        "uri": "gs://BUCKET/PATH_TO_IDS_FILE"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "versionConfig": "ALL",
      "gcsSource": {
        "uri": "gs://BUCKET/PATH_TO_IDS_FILE"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:bulkDelete"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "versionConfig": "ALL",
      "gcsSource": {
        "uri": "gs://BUCKET/PATH_TO_IDS_FILE"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:bulkDelete" | Select-Object -Expand Content

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations). Note the value of OPERATION_ID. You need this value in the next step. 

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

### Viewing the LRO status

To view the status of the bulk-delete operation, use the `operations.get` method with the operation name returned from the `bulkDelete` call.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the FHIR store's parent dataset
  * `OPERATION_ID`: the ID returned from the long-running operation



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1alpha2/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1alpha2/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns a response with the status of the operation in JSON format: 

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1beta1.fhir.FhirStoreService.BulkDelete",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty"
      }
    }
    

### Tracking deleted resources

When the bulk-delete operation completes, if a `gcsDestination` was specified, a summary file is generated in Cloud Storage. This file contains a list of the resource IDs for the **current version** resources that were deleted during the operation.

## Limitations

Referential integrity is not guaranteed during a bulk-delete operation. It is recommended to use this operation only when referential integrity is not required or is known to be satisfied after the operation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
