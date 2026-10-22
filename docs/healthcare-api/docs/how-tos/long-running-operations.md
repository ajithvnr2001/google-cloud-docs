---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations/
title: Managing long-running operations \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:37.015236+00:00
---

# Managing long-running operations  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Managing long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage the lifecycle of a Cloud Healthcare API long-running operation (LRO).

When an API method might take a long time to complete, it can return an [`Operation`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations#resource:-operation) to the client. The client can use the `Operation` interface to retrieve the status of the API method asynchronously by polling the operation. LROs in the Cloud Healthcare API adhere to the [Google Cloud LRO design pattern](https://docs.cloud.google.com/apis/design/design_patterns#long_running_operations).

The Cloud Healthcare API creates LROs for several methods, such as [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import). When `projects.locations.datasets.fhirStores.import` is called, the Cloud Healthcare API creates an LRO to track the import status. The LRO has a unique identifier that you can use to view the status of the LRO.

LROs are managed at the dataset level. If you are calling a method that returns an LRO, like [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import), you can view the status of the LRO by sending a request containing the LRO ID to the parent dataset of the FHIR store where the import is occurring.

In addition to the REST API, the following sources generate long-running operations when you call the methods listed in Methods that return an LRO:

  * The [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare)
  * The [Cloud Healthcare API](https://console.cloud.google.com/healthcare) page in the Google Cloud console



You can manage your Cloud Healthcare API LROs using the Google Cloud console, the Google Cloud CLI, or the REST API.

The record of an LRO is kept for approximately 30 days after the LRO finishes, meaning that you cannot view or list an LRO after that point.

## Methods that return an LRO

The following methods return an LRO.

Consent management methods:

  * [`projects.locations.datasets.consentStores.queryAccessibleData`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/queryAccessibleData)



Dataset methods:

  * [`projects.locations.datasets.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/create)
  * [`projects.locations.datasets.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/deidentify)



DICOM methods:

  * [`projects.locations.datasets.dicomStores.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/deidentify)
  * [`projects.locations.datasets.dicomStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export)
  * [`projects.locations.datasets.dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/import)
  * [`projects.locations.datasets.dicomStores.studies.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies/delete)
  * [`projects.locations.datasets.dicomStores.studies.series.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series/delete)



FHIR methods:

  * [`projects.locations.datasets.fhirStores.bulkDelete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/bulkDelete)
  * [`projects.locations.datasets.fhirStores.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/deidentify)
  * [`projects.locations.datasets.fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export)
  * [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import)



HL7v2 methods:

  * [`projects.locations.datasets.hl7V2Stores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export)
  * [`projects.locations.datasets.hl7V2Stores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/import)



## Getting details about an LRO

The following samples show how to get details about an LRO.

The version of the Cloud Healthcare API shown in the response when getting details about an LRO is the same as the API version of the method that initiated the LRO.

### Console

After calling a method using either the gcloud CLI or the API that returns an LRO, you can view details about the LRO in the Google Cloud console.

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the name of the dataset containing the LRO you want to view.

  3. Click **Operations**.

  4. To view error logs for the operation in Cloud Logging, click **Actions** and then click **View details in Cloud Logging**. For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

  5. To view more details about the operation, click a running operation ID. The **Long-running Operation Details** page is displayed. The page shows the following information:

     * The progress of the LRO
     * The details of the LRO, such as the operation ID and the method that invoked the LRO
     * A subset of log entries



### gcloud

Suppose that you receive the following response after calling [`gcloud healthcare dicom-stores deidentify`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/deidentify):
    
    
    Request issued for: [DATASET_ID]
    Waiting for operation [OPERATION_ID] to complete...
    

The response shows that the Cloud Healthcare API created an LRO with an operation ID. You can also retrieve the operation ID by listing long-running database operations. The command continues to run until it finishes, after which it outputs the following:
    
    
    Request issued for: [DATASET_ID]
    Waiting for operation [OPERATION_ID] to complete...done
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID
    

To get details about the LRO, run the [`gcloud healthcare operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/describe) command.

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
      apiMethodName: 'google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyDicomStore'
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
      '@type': 'type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary'
    

### REST

Suppose that you receive the following response after calling [`projects.locations.datasets.dicomStores.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/deidentify):
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The `name` value in the response shows that the Cloud Healthcare API created an LRO named `projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID`. You can also retrieve the LRO name by listing LROs.

To get the status of the LRO, use the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method. To poll an LRO, repeatedly call the `projects.locations.datasets.operations.get` method until the operation finishes. Use a backoff between each poll request, such as 10 seconds.

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
        "apiMethodName": "google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyDicomStore",
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
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        
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
    

## Listing LROs

The following samples show how to list the LROs in a dataset.

### Console

To view a list of all LROs in a dataset in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the name of the dataset containing the LRO you want to view.

  3. Click **Operations**.




A list of LROs in the dataset and their status displays. To view the error logs in Cloud Logging, click the more information icon in the last column and then click **View details in Cloud Logging**. For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

### gcloud

To list the LROs in a dataset, run the [`gcloud healthcare operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/list) command.

Before using any of the command data below, make the following replacements: 

  * DATASET_ID: the dataset ID
  * LOCATION: the dataset location



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare operations list --dataset=DATASET_ID --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare operations list --dataset=DATASET_ID --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare operations list --dataset=DATASET_ID --location=LOCATION

You should receive a response similar to the following:

#### Response
    
    
    ID             LOCATION     DONE
    OPERATION_ID   LOCATION {TRUE|FALSE}
    ...
    

### REST

To list the LROs in a dataset, use the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * DATASET_ID: the dataset ID
  * LOCATION: the dataset location



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "operations": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
            "apiMethodName": "google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyDicomStore",
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
            "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary"
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
        },
        ...
      ]
    }
    

## Cancelling an LRO

The following samples show how to cancel an LRO in a dataset.

**Important:** Cancelling an LRO doesn't roll back any part of the operation that has already completed.

### Console

To cancel an LRO in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the name of the dataset containing the LRO you want to view.

  3. Click **Operations**.

  4. In the same row as the LRO you want to cancel, open the **Actions** list and click **Stop Operation**.




### REST

To cancel an LRO, use the [`projects.locations.datasets.operations.cancel`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/cancel) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * DATASET_ID: the dataset ID
  * LOCATION: the dataset location
  * OPERATION_ID: the ID returned from the long-running operation



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID:cancel"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID:cancel" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/cancel). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {}
    

**Important:** A cancelled operation can stay in a `"cancelRequested": true` state before it is completely cancelled.

To view the status of the cancel request, use the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method.

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

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "API_METHOD_NAME",
        "createTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "endTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "cancelRequested": true,
        "logsUrl": "https://console.cloud.google.com/CLOUD_LOGGING_URL"
        "counter": {
          "success": "SUCCESS_COUNT",
          // If there were any failures, they display in the `failure` field.
          "failure": "FAILURE_COUNT"
        }
      },
      "done": true,
      "error": {
        "code": 1,
        "message": "Operation cancelled by user. Any progress already completed by the operation will not be reverted."
      }
    }
    

### Cancelling multiple LROs

To cancel multiple LROs, complete the following steps:

  1. Call the [`operations.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/list) method to get the names of the operations in a dataset.
  2. Call the [`operations.cancel`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/cancel) method on each operation.



Google provides a [Python script](https://github.com/GoogleCloudPlatform/healthcare/blob/master/operations/cancel_all_ops.py) that you can use to cancel all operations for a given dataset.

## Troubleshooting LROs

When a LRO fails, its response includes a [canonical Google Cloud error code](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto). The following table provides an explanation of the cause for each code and a recommendation for how to handle the code. For many errors, the recommended action is to try the request again using exponential backoff. For information on how to implement exponential backoff in the Cloud Healthcare API, see [Retry failed requests](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#retry-failed).

Code | Enum | Description | Recommended action  
---|---|---|---  
1 | `CANCELLED` | The operation was cancelled, typically by the caller. | Re-run the operation if desired.  
2 | `UNKNOWN` | This error might be returned when a `Status` value received from another address space belongs to an error space that is not known in this address space. If an API's error doesn't return enough information, the error might be converted to this error. | Retry with exponential backoff.  
3 | `INVALID_ARGUMENT` | The client specified an invalid argument. This error differs from `FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system, such as a malformed file name. | Don't retry without fixing the problem.  
4 | `DEADLINE_EXCEEDED` | The deadline expired before the operation could complete. For operations that change the state of the system, this error might be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire. | Retry with exponential backoff.  
5 | `NOT_FOUND` | Some requested entity, such as a FHIR resource, was not found. | Don't retry without fixing the problem.  
6 | `ALREADY_EXISTS` | The entity that a client attempted to create, such as a DICOM instance, already exists. | Don't retry without fixing the problem.  
7 | `PERMISSION_DENIED` | The caller doesn't have permission to execute the specified operation. This error code doesn't imply the request is valid or the requested entity exists or satisfies other preconditions. | Don't retry without fixing the problem.  
8 | `RESOURCE_EXHAUSTED` | Some resource has been exhausted, such as a per-project quota. See [Best practices for quota management](https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management) for recommended actions. | Retry with exponential backoff. Quota might become available over time.  
9 | `FAILED_PRECONDITION` | The operation was rejected because the system is not in a state required for the operation's execution. For example, the directory to be deleted is non-empty, or an `rmdir` operation is applied to a non-directory. | Don't retry without fixing the problem.  
10 | `ABORTED` | The operation was aborted, typically due to a concurrency issue such as a sequencer check failure or transaction abort. | Retry with exponential backoff.  
11 | `OUT_OF_RANGE` | The operation was attempted past the valid range, such as seeking or reading past end-of-file. Unlike `INVALID_ARGUMENT`, this error indicates a problem that may be fixed if the system state changes. | Don't retry without fixing the problem.  
12 | `UNIMPLEMENTED` | The operation isn't implemented or isn't supported/enabled in the Cloud Healthcare API. | Don't retry.  
13 | `INTERNAL` | Internal errors. This indicates that an unexpected error was encountered in processing on the underlying system. | Retry with exponential backoff.  
14 | `UNAVAILABLE` | The Cloud Healthcare API is currently unavailable. This is most likely a transient condition, which can be corrected by retrying with a backoff. Note that it is not always safe to retry non-idempotent operations. | Retry with exponential backoff.  
15 | `DATA_LOSS` | Unrecoverable data loss or corruption. | Contact your system administrator. The system administrator might want to contact a [support representative](https://docs.cloud.google.com/support/docs#contacting_technical_support) if data loss or corruption occurred.  
16 | `UNAUTHENTICATED` | The request doesn't have valid authentication credentials for the operation. | Don't retry without fixing the problem.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
