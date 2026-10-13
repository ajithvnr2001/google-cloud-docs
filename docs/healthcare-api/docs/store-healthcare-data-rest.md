---
url: https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest/
title: Quickstart: Store healthcare data with curl and PowerShell \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:42.690786+00:00
---

# Quickstart: Store healthcare data with curl and PowerShell  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store healthcare data with curl and PowerShell

This page shows you how to use the Cloud Healthcare API and `curl` or PowerShell to complete the following tasks: 

  1. Create a Cloud Healthcare API dataset.
  2. Create one of the following data stores inside the dataset:
     * Digital Imaging and Communications in Medicine (DICOM) store
     * Fast Healthcare Interoperability Resources (FHIR) store
     * Health Level Seven International Version 2 (HL7v2) store
  3. Store and inspect a particular type of medical data in the DICOM, FHIR, or HL7v2 store.



If you're only interested in working with one type of data store, you can skip directly to that section of the quickstart after completing the steps in Before you begin and Create a dataset. 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Healthcare API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable healthcare.googleapis.com

  8. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/healthcare.datasetAdmin, roles/healthcare.fhirStoreAdmin, roles/healthcare.dicomStoreAdmin, roles/healthcare.hl7V2StoreAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Cloud Healthcare API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable healthcare.googleapis.com

  15. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/healthcare.datasetAdmin, roles/healthcare.fhirStoreAdmin, roles/healthcare.dicomStoreAdmin, roles/healthcare.hl7V2StoreAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.




## Create a dataset

_Datasets_ contain data stores, and data stores contain healthcare data. To use the Cloud Healthcare API, you must create at least one dataset. 

The following sample shows how to create a dataset named `my-dataset` in the `us-central1` region. You use the dataset throughout this quickstart to create DICOM stores, FHIR stores, and HL7v2 stores.

### REST

  1. Create the dataset using the [`projects.locations.datasets.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/create) method.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets?datasetId=my-dataset"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets?datasetId=my-dataset" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) (LRO). Long-running operations are returned when method calls might take additional time to complete. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    
    

  2. Get the status of the long-running operation using the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `OPERATION_ID`: the ID returned from the long-running operation

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The output is the following. When the response contains `"done": true`, the long-running operation has finished. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.CreateDataset",
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
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.dataset.Dataset",
        "name": "projects/PROJECT_ID/locations/us-central1/datasets/my-dataset",
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
    




To complete this quickstart, choose from one of the following sections:

  * Store and view a DICOM instance
  * Store and view FHIR resources
  * Store and view an HL7v2 message



## Store and view a DICOM instance

This section shows how to complete the following tasks:

  1. Create a DICOM store.
  2. Store a DICOM instance in the DICOM store.
  3. View the DICOM instance's metadata.



The Cloud Healthcare API implements the [DICOMweb](https://www.dicomstandard.org/using/dicomweb) standard to store and access medical imaging data.

### Create a DICOM store

DICOM stores exist inside datasets and hold DICOM instances. The following sample shows how to create a DICOM store named `my-dicom-store`.

### REST

Create a DICOM store using the [`projects.locations.datasets.dicomStores.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores?dicomStoreId=my-dicom-store"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores?dicomStoreId=my-dicom-store" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores/my-dicom-store"
    }
    

### Store a DICOM instance

  1. Download the [sample DICOM instance file](https://docs.cloud.google.com/healthcare-api/docs/resources/dicom_00000001_000.dcm) to your machine. The file contains a de-identified patient X-ray.

### curl
         
         curl -O https://cloud.google.com/healthcare-api/docs/resources/dicom_00000001_000.dcm

### PowerShell
         
         Invoke-WebRequest -Uri "https://cloud.google.com/healthcare-api/docs/resources/dicom_00000001_000.dcm" -OutFile $pwd/dicom_00000001_000.dcm

  2. Store the DICOM instance using the [`dicomStores.storeInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/storeInstances) method. This quickstart assumes you're running the command in the same directory where you downloaded the DICOM instance.

### REST

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/dicom" \  
         --data-binary @dicom_00000001_000.dcm \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores/my-dicom-store/dicomWeb/studies"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -InFile dicom_00000001_000.dcm `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores/my-dicom-store/dicomWeb/studies" | Select-Object -Expand Content

The output is the following XML response. In this output:

     * `PROJECT_ID`, `us-central1`, `my-dataset`, `my-dicom-store`: the values you provided when running the command
     * `SOPClassUID`: uniquely identifies the Service-Object Pair (SOP) class
     * `SOPInstanceUID`: uniquely identifies the Service-Object Pair (SOP) instance
     * `STUDY_UID`: uniquely identifies the study instance
     * `SERIES_UID`: uniquely identifies the series instance
     * `INSTANCE_UID`: uniquely identifies the instance

#### Response
    
    <NativeDicomModel>
      <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
        <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores/my-dicom-store/dicomWeb/studies/STUDY_UID</Value>
      </DicomAttribute>
      <DicomAttribute tag="00081199" vr="SQ" keyword="ReferencedSOPSequence">
        <Item number="1">
          <DicomAttribute tag="00081150" vr="UI" keyword="ReferencedSOPClassUID">
            <Value number="1">SOPClassUID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081155" vr="UI" keyword="ReferencedSOPInstanceUID">
            <Value number="1">SOPInstanceUID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
            <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores/my-dicom-store/dicomWeb/studies/STUDY_UID/series/SERIES_UID/instances/INSTANCE_UID</Value>
          </DicomAttribute>
        </Item>
      </DicomAttribute>
    </NativeDicomModel>
    




### View DICOM instance metadata

### REST

View the metadata for the instance using the [`dicomStores.searchForInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForInstances) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of the Google Cloud project that you created or selected in Before you begin



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores/my-dicom-store/dicomWeb/instances"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores/my-dicom-store/dicomWeb/instances" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForInstances). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    [
       {
          "00080005":{
             "vr":"CS",
             "Value":[
                "CODE_STRING"
             ]
          },
          "00080016":{
             "vr":"UI",
             "Value":[
                "UNIQUE_IDENTIFIER"
             ]
          },
          "00080018":{
             "vr":"UI",
             "Value":[
                "UNIQUE_IDENTIFIER"
             ]
          },
          "00080020":{
             "vr":"DA",
             "Value":[
                "DATE_TIME"
             ]
          },
          "00080030":{
             "vr":"TM",
             "Value":[
                "TIME"
             ]
          },
          "00080060":{
             "vr":"CS",
             "Value":[
                "CODE_STRING"
             ]
          },
          "0008103E":{
             "vr":"LO",
             "Value":[
                "LONG_STRING"
             ]
          },
          "00100010":{
             "vr":"PN",
             "Value":[
                {
                   "Alphabetic":"Anonymized"
                }
             ]
          },
       },
    ...
    ]
    

After storing and viewing the DICOM instance in the Cloud Healthcare API, continue to Clean up to avoid incurring charges to your Google Cloud account for the resources used in this page.

For more information on working with DICOM data, see What's next.

## Store and view FHIR resources

This section shows how to complete the following tasks:

  1. Create a FHIR store.
  2. Store a FHIR resource in the FHIR store.
  3. View the FHIR resource's data.



The Cloud Healthcare API implements the [FHIR standard](https://docs.cloud.google.com/healthcare-api/docs/fhir) to store and access FHIR data.

### Create a FHIR store

FHIR stores exist inside datasets and contain FHIR resources. The following sample shows how to create a FHIR store named `my-fhir-store` that uses [FHIR version R4](https://hl7.org/fhir/R4/).

### REST

Create a FHIR store using the [`projects.locations.datasets.fhirStores.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



Request JSON body: 
    
    
    {
      "version": "R4"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "version": "R4"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores?fhirStoreId=my-fhir-store"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "version": "R4"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores?fhirStoreId=my-fhir-store" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores/my-fhir-store",
      "version": "R4"
    }
    

### Store a FHIR resource

### REST

Create a Patient resource in the FHIR store using the [`projects.locations.datasets.fhirStores.fhir.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



Request JSON body: 
    
    
    {
      "name": [
        {
          "use": "official",
          "family": "Smith",
          "given": [
            "Darcy"
          ]
        }
      ],
      "gender": "female",
      "birthDate": "1970-01-01",
      "resourceType": "Patient"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "name": [
        {
          "use": "official",
          "family": "Smith",
          "given": [
            "Darcy"
          ]
        }
      ],
      "gender": "female",
      "birthDate": "1970-01-01",
      "resourceType": "Patient"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores/my-fhir-store/fhir/Patient"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "name": [
        {
          "use": "official",
          "family": "Smith",
          "given": [
            "Darcy"
          ]
        }
      ],
      "gender": "female",
      "birthDate": "1970-01-01",
      "resourceType": "Patient"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores/my-fhir-store/fhir/Patient" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "birthDate": "1970-01-01",
      "gender": "female",
      "id": "PATIENT_ID",
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "name": [
        {
          "family": "Smith",
          "given": [
            "Darcy"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient"
    }
    

### View FHIR resource contents

### REST

View information about the Patient resource using the [`projects.locations.datasets.fhirStores.fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores/my-fhir-store/fhir/Patient"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores/my-fhir-store/fhir/Patient" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores/my-fhir-store/fhir/Patient/PATIENT_ID",
          "resource": {
            "birthDate": "1970-01-01",
            "gender": "female",
            "id": "PATIENT_ID",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "versionId": "MTY5MDQxMDk5ODU1OTkxNTAwMA"
            },
            "name": [
              {
                "family": "Smith",
                "given": [
                  "Darcy"
                ],
                "use": "official"
              }
            ],
            "resourceType": "Patient"
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores/my-fhir-store/fhir/Patient/?"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores/my-fhir-store/fhir/Patient/?"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores/my-fhir-store/fhir/Patient/?"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    

After storing and viewing a FHIR resource in the Cloud Healthcare API, continue to Clean up to avoid incurring charges to your Google Cloud account for the resources used in this page.

For more information on working with FHIR data, see What's next.

## Store and view an HL7v2 message

This section shows how to complete the following tasks:

  1. Create an HL7v2 store.
  2. Store an HL7v2 message in the HL7v2 store.
  3. View the HL7v2 message data.



The HL7v2 implementation in the Cloud Healthcare API aligns with the [HL7v2 standard](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=185).

### Create an HL7v2 store

HL7v2 stores exist inside datasets and hold HL7v2 messages. The following sample shows how to create an HL7v2 store named `my-hl7v2-store`.

### REST

Create an HL7v2 store using the [`projects.locations.datasets.hl7V2Stores.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/hl7V2Stores?hl7V2StoreId=my-hl7v2-store"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/hl7V2Stores?hl7V2StoreId=my-hl7v2-store" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7v2Stores/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/hl7V2Stores/my-hl7v2-store"
    }
    

### Create an HL7v2 message

  1. Download the [sample HL7v2 message file](https://docs.cloud.google.com/static/healthcare-api/docs/resources/hl7v2-sample.json) to your machine:

### curl
         
         curl -O https://cloud.google.com/healthcare-api/docs/resources/hl7v2-sample.json

### PowerShell
         
         Invoke-WebRequest -Uri "https://cloud.google.com/healthcare-api/docs/resources/hl7v2-sample.json" -OutFile $pwd/hl7v2-sample.json

The HL7v2 message contains the following information base-64 encoded in the `data` field of the sample file:
         
         MSH|^~\&|A|SEND_FACILITY|A|A|20180101000000||TYPE^A|20180101000000|T|0.0|||AA||00|ASCII
         EVN|A00|20180101040000
         PID||14^111^^^^MRN|11111111^^^^MRN~1111111111^^^^ORGNMBR
         

  2. Store the HL7v2 message in the HL7v2 store using the [`projects.locations.datasets.hl7V2Stores.messages.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/create) method. This quickstart assumes you're running the command in the same directory where you downloaded the HL7v2 message.

### REST

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         --data-binary @hl7v2-sample.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/hl7V2Stores/my-hl7v2-store/messages"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -InFile hl7v2-sample.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/hl7V2Stores/my-hl7v2-store/messages" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The output is the following. In this output:

     * `PROJECT_ID`, `us-central1`, `my-dataset`, `my-hl7v2-store`: the values you provided in the method call
     * `MESSAGE_ID`: an identifier for the HL7v2 message provided by the Cloud Healthcare API. Note the value of `MESSAGE_ID`. You need this value in the next step.

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/hl7V2Stores/my-hl7v2-store/messages/MESSAGE_ID",
      "data": "TVNIfF5+XCZ8QXxTRU5EX0ZBQ0lMSVRZfEF8QXwyMDE4MDEwMTAwMDAwMHx8VFlQRV5BfDIwMTgwMTAxMDAwMDAwfFR8MC4wfHx8QUF8fDAwfEFTQ0lJDUVWTnxBMDB8MjAxODAxMDEwNDAwMDANUElEfHwxNAExMTFeXl5eTVJOfDExMTExMTExXl5eXk1STn4xMTExMTExMTExXl5eXk9SR05NQlI=",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "1970-01-01T00:00:00Z",
      "patientIds": [
        {
          "value": "14\u0001111",
          "type": "MRN"
        },
        {
          "value": "11111111",
          "type": "MRN"
        },
        {
          "value": "1111111111",
          "type": "ORGNMBR"
        }
      ]
    }
    




### View HL7v2 message contents

Find the `MESSAGE_ID` in the response you received when you created the HL7v2 message.

### REST

View the HL7v2 message details using the [`projects.locations.datasets.hl7V2stores.messages.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/get) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin
  * `HL7V2_MESSAGE_ID`: the ID in the response you received when you created the HL7v2 message



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/hl7V2Stores/my-hl7v2-store/messages/HL7V2_MESSAGE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/hl7V2Stores/my-hl7v2-store/messages/HL7V2_MESSAGE_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/hl7V2Stores/my-hl7v2-store/messages/MESSAGE_ID",
      "data": "TVNIfF5+XCZ8QXxTRU5EX0ZBQ0lMSVRZfEF8QXwyMDE4MDEwMTAwMDAwMHx8VFlQRV5BfDIwMTgwMTAxMDAwMDAwfFR8MC4wfHx8QUF8fDAwfEFTQ0lJDUVWTnxBMDB8MjAxODAxMDEwNDAwMDANUElEfHwxNAExMTFeXl5eTVJOfDExMTExMTExXl5eXk1STn4xMTExMTExMTExXl5eXk9SR05NQlI=",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
      "patientIds": [
        {
          "value": "14\u0001111",
          "type": "MRN"
        },
        {
          "value": "11111111",
          "type": "MRN"
        },
        {
          "value": "1111111111",
          "type": "ORGNMBR"
        }
      ],
      "parsedData": {
        "segments": [
          {
            "segmentId": "MSH",
            "fields": {
              "8.2": "A",
              "11": "0.0",
              "8.1": "TYPE",
              "4": "A",
              "9": "20180101000000",
              "10": "T",
              "17": "ASCII",
              "14": "AA",
              "1": "^~\\&",
              "2": "A",
              "3": "SEND_FACILITY",
              "5": "A",
              "16": "00",
              "0": "MSH",
              "6": "20180101000000"
            }
          },
          {
            "segmentId": "EVN",
            "fields": {
              "0": "EVN",
              "1": "A00",
              "2": "20180101040000"
            }
          },
          {
            "segmentId": "PID",
            "fields": {
              "2.5": "MRN",
              "3[0].1": "11111111",
              "3[0].5": "MRN",
              "3[1].1": "1111111111",
              "3[1].5": "ORGNMBR",
              "0": "PID",
              "2.1": "14\u0001111"
            }
          }
        ]
      }
    }
    

After storing and viewing the HL7v2 message in the Cloud Healthcare API, continue to Clean up to avoid incurring charges to your Google Cloud account for the resources used in this page.

For more information on working with HL7v2 data, see What's next.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

If you created a new project for this quickstart, follow the steps in Delete the project. Otherwise, follow the steps in Delete the dataset.

Optional: Revoke credentials from the gcloud CLI. 
    
    
    gcloud auth revoke

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete the dataset

If you no longer need the dataset created in this quickstart, you can delete it. Deleting a dataset permanently deletes the dataset and any FHIR, HL7v2, or DICOM stores it contains.

### REST

Delete the dataset using the [`projects.locations.datasets.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/delete) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a successful status code (2xx) and an empty response.

## How did it go?

It worked!  **Great!** What did you like about the quickstart? What could we have done better?  Let us know!.  I got stuck.  **We're sorry to hear that.** Let us know what went wrong. We'll want to fix it. 

## What's next

See the following sections for general information on the Cloud Healthcare API and how to perform the tasks in this quickstart using another interface:

  * Read an [overview of Cloud Healthcare API concepts](https://docs.cloud.google.com/healthcare-api/docs/concepts/introduction)
  * [Store healthcare data with client libraries](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library)
  * [Store healthcare data with the Google Cloud console](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-console)
  * [Store healthcare data with the gcloud CLI](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-gcloud)



### DICOM

  * [Create and manage DICOM stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom)
  * [Connect a PACS to the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs)
  * [Use the DICOMweb standard](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb)
  * [Import and export DICOM data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export)



See the [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom) for information on how the Cloud Healthcare API implements the DICOMweb standard.

### FHIR

  * [Create and manage FHIR stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir)
  * [Create and manage FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources)
  * [Import and export FHIR data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export)



See the [FHIR conformance statement](https://docs.cloud.google.com/healthcare-api/docs/fhir) for information on how the Cloud Healthcare API implements the FHIR standard.

### HL7v2

  * [Create and manage HL7v2 stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2)
  * [Create and manage HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages)
  * [Transmit HL7v2 messages over TCP/IP connections](https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter)
  * [Import and export HL7v2 messages using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-import-export)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
