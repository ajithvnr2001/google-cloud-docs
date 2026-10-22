---
url: https://docs.cloud.google.com/healthcare-api/docs/fhir-store-metrics/
title: View FHIR store metrics \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:42.440110+00:00
---

# View FHIR store metrics  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/fhir-store-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  View FHIR store metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the following metrics about a FHIR store:

  * The types of FHIR resources in the FHIR store
  * The number of each type of resource
  * The size of the data in the FHIR store
  * The size of the data version history in the FHIR store



You can use the metrics to do the following:

  * Estimate future costs based on current usage.
  * Track how the FHIR store is growing and changing over time.
  * Ensure that the number of FHIR resources in a FHIR store matches the number you [imported](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export), [created using a bundle](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bundles), or [de-identified](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-deidentify).



When you add or change FHIR resources, the resources are added to the FHIR store asynchronously. There might be a delay between when you make a change and when it appears in the metrics.

The following examples show how to view the metrics about a FHIR store.

### Console

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the FHIR store whose metrics you want to view. The **Data stores** page is displayed.

  3. In the **Data stores** list, select the FHIR store whose metrics you want to view. The **Data store details** page is displayed.

  4. Click the **Metrics** tab. The tab shows the following metrics:

     * **Total number of resource types**
     * **Total number of resources**
     * **Total size of all resources**
     * **Total size of all versioned resources**
  5. View and filter metrics in the **Metrics** table. After you filter metrics, select a FHIR resource type to view information about all resources of that type in the [FHIR viewer](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search#using_the_fhir_viewer).




### gcloud

Run the [`gcloud healthcare fhir-stores metrics`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/metrics) command.

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores metrics FHIR_STORE_ID \
      --project=PROJECT_ID \
      --location=LOCATION \
      --dataset=DATASET_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores metrics FHIR_STORE_ID `
      --project=PROJECT_ID `
      --location=LOCATION `
      --dataset=DATASET_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores metrics FHIR_STORE_ID ^
      --project=PROJECT_ID ^
      --location=LOCATION ^
      --dataset=DATASET_ID

You should receive a response similar to the following:

#### Response
    
    
    metrics:
    - count: 'FHIR_RESOURCE_TYPE_COUNT'
      resourceType: FHIR_RESOURCE_TYPE
      structuredStorageSizeBytes: 'FHIR_RESOURCE_TYPE_SIZE'
      versionedStorageSizeBytes: 'FHIR_RESOURCE_TYPE_VERSIONED_SIZE'
    ...
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID
    

### REST

Use the [`fhirStores.getFHIRStoreMetrics`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/getFHIRStoreMetrics) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:getFHIRStoreMetrics"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:getFHIRStoreMetrics" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/getFHIRStoreMetrics). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "metrics": [
        {
          "resourceType": "FHIR_RESOURCE_TYPE",
          "count": "FHIR_RESOURCE_TYPE_COUNT",
          "structuredStorageSizeBytes": "FHIR_RESOURCE_TYPE_SIZE",
          "versionedStorageSizeBytes": "FHIR_RESOURCE_TYPE_VERSIONED_SIZE"
        },
        ...
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
