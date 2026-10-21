---
url: https://docs.cloud.google.com/healthcare-api/docs/dicom-store-metrics/
title: View DICOM store, DICOM study, and DICOM series metrics \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:14.442293+00:00
---

# View DICOM store, DICOM study, and DICOM series metrics  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/dicom-store-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  View DICOM store, DICOM study, and DICOM series metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view DICOM store, DICOM study, and DICOM series metrics. You can use these metrics to do the following:

  * Estimate future costs based on current usage.
  * Track how a DICOM store grows and changes over time.
  * Ensure that the number of DICOM instances matches the number that you [imported](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export).



Modifications to DICOM data, such as storing or deleting the data, are asynchronous. There might be a delay between when you modify the data and when the modifications are shown in the DICOM store metrics.

## Storage types

Several metrics show the size, in bytes, of the following [data storage](https://cloud.google.com/healthcare-api/pricing#data_storage) classes:

Blob storage
    Unstructured DICOM data and DICOM data that uses _blob bytes_.
Structured storage
    Non-blob storage data, such as searchable metadata.

## View DICOM store metrics

The following samples show how to view DICOM store metrics.

### Console

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the DICOM store whose metrics you want to view.

  3. In the **Data stores** list, select the DICOM store whose metrics you want to view. The **Data store details** page is displayed.

  4. Click the **Metrics** tab.

The tab shows the following metrics on a scorecard:

     * **Total number of studies**
     * **Total number of series**
     * **Total number of instances**
     * **Structured storage size of all instances**
     * **Blob storage size of all instances**
     * **Total size of all instances**

The metrics table contains the following columns:

Column | Description  
---|---  
`ID` | The study IDs and the series IDs. Expand a study entry to view the series within the study.  
`Number of series` | The number of series within a study.  
`Number of instances` | The number of instances within a study or within a series.  
`Structured size` | The size of the structured data in the study or the series.  
`Blob size` | The size of the blob data in the study or the series.  
  5. To filter the table data, enter the study ID in the **Filter** field.




### REST

Use the [`dicomStores.getDICOMStoreMetrics`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/getDICOMStoreMetrics) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:getDICOMStoreMetrics"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:getDICOMStoreMetrics" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/getDICOMStoreMetrics). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID",
      "studyCount": "STUDY_COUNT",
      "seriesCount": "SERIES_COUNT",
      "instanceCount": "INSTANCE_COUNT",
      "structuredStorageSizeBytes": "STRUCTURED_STORAGE_BYTES",
      "blobStorageSizeBytes": "BLOB_STORAGE_BYTES",
    }
    

## View DICOM studies metrics

The following samples show how to view DICOM studies metrics.

### Console

To view DICOM study metrics in the Google Cloud console, see [View DICOM store metrics](https://docs.cloud.google.com/healthcare-api/docs/dicom-store-metrics#dicom-store-get-metrics-console).

### REST

Use the [`dicomStores.studies.getStudyMetrics`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.dicomWeb.studies/getStudyMetrics) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `STUDY_UID`: the DICOMweb study unique identifier (UID)



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_UID:getStudyMetrics"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_UID:getStudyMetrics" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.dicomWeb.studies/getStudyMetrics). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "study": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_UID",
      "seriesCount": "SERIES_COUNT",
      "instanceCount": "INSTANCE_COUNT",
      "structuredStorageSizeBytes": "STRUCTURED_STORAGE_BYTES",
      "blobStorageSizeBytes": "BLOB_STORAGE_BYTES"
    }
    

## View DICOM series metrics

The following samples show how to view DICOM series metrics.

### Console

To view DICOM series metrics in the Google Cloud console, see [View DICOM store metrics](https://docs.cloud.google.com/healthcare-api/docs/dicom-store-metrics#dicom-store-get-metrics-console).

### REST

Use the [`dicomStores.dicomWeb.studies.series.getSeriesMetrics`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.dicomWeb.studies.series/getSeriesMetrics) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `STUDY_UID`: the DICOMweb study unique identifier (UID)
  * `SERIES_UID`: the DICOMweb series unique identifier (UID)



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_UID/series/SERIES_UID:getSeriesMetrics"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_UID/series/SERIES_UID:getSeriesMetrics" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.dicomWeb.studies.series/getSeriesMetrics). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "series": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_UID/series/SERIES_UID",
      "structuredStorageSizeBytes": "STRUCTURED_STORAGE_BYTES",
      "blobStorageSizeBytes": "BLOB_STORAGE_BYTES",
      "instanceCount": "INSTANCE_COUNT"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
