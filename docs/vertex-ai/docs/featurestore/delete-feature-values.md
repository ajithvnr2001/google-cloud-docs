---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/delete-feature-values/
title: Delete feature values \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:46:05.569530+00:00
---

# Delete feature values  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/delete-feature-values/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Delete feature values Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

To learn more, run the "Example Feature Store workflow with sample data" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb)

You can delete feature values from an entity type in the following ways:

  * Delete feature values from specified entities

  * Delete feature values from specified features within a time range




## Delete feature values from specified entities

You can delete feature values from multiple entities within an entity type. To specify the entities from which you want to delete the feature values, you need to list the entity IDs in a CSV file.

### REST

To delete feature values, send a POST request using the [featurestores.entityTypes.deleteFeatureValues](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/deleteFeatureValues) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region or location where the featurestore is created. For example, `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE: ID of the entity type from which you want to delete the feature values.
  * CSV_FILE_URI: Specify the Cloud Storage URI of the CSV file containing the entity IDs for which you want to delete feature values. The first line of this file should be one of the following: 
    * If you specify the `entity_id_field` parameter, then the first line of the CSV file must be the same as ENTITY_ID_FIELD.
    * If you don't specify the `entity_id_field` parameter, then the first line of the CSV file must be "entity_id".
  * ENTITY_ID_FIELD: (_Optional_) Enter the string specified in the first line of the CSV file at CSV_FILE_URI.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE:deleteFeatureValues

Request JSON body: 
    
    
    {
      "selectEntity": {
        "entityIdSelector": {
          "csv_source": {
            "gcs_source": {
              "uris": [
                "CSV_FILE_URI"
              ]
            },
            "entity_id_field": "ENTITY_ID_FIELD"
          }
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE:deleteFeatureValues"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE:deleteFeatureValues" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/571445526053/locations/us-central1/operations/7688824614775947264",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.DeleteFeatureValuesOperationMetadata",
        "genericMetadata": {
          "createTime": "2022-05-09T16:59:38.128375Z",
          "updateTime": "2022-05-09T16:59:38.128375Z",
          "state": "RUNNING",
          "worksOn": [
            "projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID"
          ]
        }
      }
    }
    

### View request status

To check the status of the POST request, send the following GET request.

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region or location where the featurestore is created. For example, `us-central1`.
  * OPERATION_NAME: The value of the `name` field in the JSON response received from the POST request to delete feature values.



HTTP method and URL: 
    
    
    GET https://LOCATION_ID-aiplatform.googleapis.com/v1/OPERATION_NAME

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/OPERATION_NAME"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/OPERATION_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Delete feature values from specified features within a time range

You can delete feature values from an entity type by specifying the feature IDs and a time range.

**Note:** Using this option permanently deletes the feature values from the specified feature IDs within the specified time range. This might include data from the online storage. If you want to retain any deleted historical data in the online storage, you must re-ingest it.

### REST

To delete feature values from an entity type, send a POST request using the [featurestores.entityTypes.deleteFeatureValues](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/deleteFeatureValues) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region or location where the featurestore is created. For example, `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE: ID of the entity type from which you want to delete the feature values.
  * START_TIME: Specify the start time of the time range.
  * END_TIME: (_Optional_) Specify the end time of the time range.  
**Note:** If you specify the START_TIME without specifying an END_TIME, then the request deletes the feature values from the specified feature IDs until the current time (when the request is sent). 
  * SKIP_ONLINE_STORAGE_DELETE: (_Optional_) To delete feature values from the online storage as well as the offline storage, enter `false`. Otherwise, to delete feature values from the offline storage only, enter `true`. 



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE:deleteFeatureValues

Request JSON body: 
    
    
    {
      "selectTimeRangeAndFeature": {
        "timeRange": {
          "startTime": "START_TIME",
          "endTime": "END_TIME"
        },
        "featureSelector": {
          "idMatcher": {
            "ids": [ "FEATURE_ID", ...]
          }
        },
        "skipOnlineStorageDelete": SKIP_ONLINE_STORAGE_DELETE
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE:deleteFeatureValues"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE:deleteFeatureValues" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/571445526053/locations/us-central1/operations/7688824614775947264",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.DeleteFeatureValuesOperationMetadata",
        "genericMetadata": {
          "createTime": "2022-05-09T16:59:38.128375Z",
          "updateTime": "2022-05-09T16:59:38.128375Z",
          "state": "RUNNING",
          "worksOn": [
            "projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID"
          ]
        }
      }
    }
    

### View request status

To check the status of the POST request, send the following GET request.

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region or location where the featurestore is created. For example, `us-central1`.
  * OPERATION_NAME: The value of the `name` field in the JSON response received from the POST request to delete feature values.



HTTP method and URL: 
    
    
    GET https://LOCATION_ID-aiplatform.googleapis.com/v1/OPERATION_NAME

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/OPERATION_NAME"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/OPERATION_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## What's next

View the [Vertex AI Feature Store quotas and limits](https://docs.cloud.google.com/vertex-ai/quotas#featurestore).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
