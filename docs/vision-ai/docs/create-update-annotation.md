---
url: https://docs.cloud.google.com/vision-ai/docs/create-update-annotation/
title: Create a warehouse asset annotation \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:51.887492+00:00
---

# Create a warehouse asset annotation  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/create-update-annotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)



Send feedback 

#  Create a warehouse asset annotation Stay organized with collections  Save and categorize content based on your preferences. 

Media objects (`asset` resources) in a warehouse (`corpus`) contain metadata and `annotation` resources. These `annotation` resources represent a key-value mapping of content in an `asset`.

## Create a warehouse asset annotation

You must complete the following steps _before_ you can create an annotation for an asset:

  * Create an `asset` resource in a warehouse
  * Create a `dataSchema` with the same key to indicate the data type of the `annotation` value



An `annotation` can optionally have a temporal partition associated with it. For example, if an `annotation` applies to the whole `asset`, you can omit any temporal partition associated with it. Similarly, if an `annotation` applies to only a specific part of a video `asset`, you can supply the time range of the `asset` when creating the `annotation`.

### Create an annotation with no temporal partition

If an annotation applies to the entirety of a video `asset` you don't have to provide a temporal partition for it. Use the following sample to create a user provided `annotation` for a whole `asset` (no video time period specified).

### REST

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * ASSET_ID: The ID of your target asset.
  * ANNOTATION_ID: (Optional) A user-provided value for the annotation ID. In this request, the value is added to the request URL in the form: 
    * https://ENDPOINT/v1/[...]/corpora/CORPUS_ID/assets/ASSET_ID/annotations**?annotation_id= ANNOTATION_ID**



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations

Request JSON body: 
    
    
    {
      "user_specified_annotation":{
        "key": "camera-location",
        "value": {
          "str_value": "Sunnyvale"
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations/ANNOTATION_ID",
      "userSpecifiedAnnotation": {
        "key": "camera-location",
        "value": {
          "strValue": "Sunnyvale"
        }
      }
    }
    

### Create an annotation with a temporal partition

If an annotation applies to only part of a video `asset` you can provide a time range for the target video portion. Use the following sample to create a user provided `annotation` for a specific time period of a video `asset` using a temporal partition.

### REST

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * ASSET_ID: The ID of your target asset.
  * ANNOTATION_ID: (Optional) A user-provided value for the annotation ID. In this request, the value is added to the request URL in the form: 
    * https://ENDPOINT/v1/[...]/corpora/CORPUS_ID/assets/ASSET_ID/annotations**?annotation_id= ANNOTATION_ID**



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations

Request JSON body: 
    
    
    {
      "user_specified_annotation": {
        "key": "object-detected",
        "value": {
          "str_value": "cat"
        },**"partition": {
          "temporal_partition": {
            "start_time": {
              "seconds": " 1630464728"
            },
            "end_time": {
              "seconds": "1630464729"
            }
          }
        }**
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations/ANNOTATION_ID",
      "userSpecifiedAnnotation": {
        "key": "object-detected",
        "value": {
          "strValue": "cat"
        },
        "partition": {
          "temporalPartition": {
            "startTime": "2022-09-14T20:33:09Z",
            "endTime": "2022-09-14T20:33:39Z"
          }
        }
      }
    }
    

## Update an annotation (no temporal partition)

**Caution:** The update operation is only available for annotations with no temporal partition.

### REST

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * ASSET_ID: The ID of your target asset.
  * ANNOTATION_ID: The ID of your target annotation.



HTTP method and URL: 
    
    
    PATCH https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations/ANNOTATION_ID

Request JSON body: 
    
    
    {
     "user_specified_annotation":{
        "key": "camera-location",
        "value": {
          "str_value": "UPDATED_FIELD_VALUE"
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations/ANNOTATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations/ANNOTATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations/ANNOTATION_ID",
      "userSpecifiedAnnotation": {
        "key": "camera-location",
        "value": {
          "strValue": "UPDATED_FIELD_VALUE"
        }
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
