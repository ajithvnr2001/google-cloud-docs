---
url: https://docs.cloud.google.com/vision/product-search/docs/operation-status/
title: Getting an operation's status \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:10:12.263237+00:00
---

# Getting an operation's status  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/operation-status/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/product-search/docs/create-product-set-search-products)



Send feedback 

#  Getting an operation's status Stay organized with collections  Save and categorize content based on your preferences. 

Several operations you request are long-running, such as product set creation via bulk import, purging a product set, and purging orphaned products. These types of requests will return a JSON with an operation ID that you can use to get the status of the operation.

For example, a batch delete (`purge`) request returns the following JSON:
    
    
    {
    "name": "projects/project-id/locations/location-id/operations/**bc4e1d412863e626** "
    }

In this case, the operation ID is `bc4e1d412863e626`. The following samples show how to get the status of this operation with this ID.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * OPERATION_ID: The ID of your operation. The ID is the last element of the name of your operation. For example: 
    * operation name: `projects/PROJECT_ID/locations/LOCATION_ID/operations/**bc4e1d412863e626**`
    * operation id: `**bc4e1d412863e626**`



HTTP method and URL: 
    
    
    GET https://vision.googleapis.com/v1/locations/location-id/operations/operation-id

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/locations/location-id/operations/operation-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/locations/location-id/operations/operation-id" | Select-Object -Expand Content

You should see output similar to the following for a completed **product set purge operation** : 
    
    
    {
      "name": "locations/location-id/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.BatchOperationMetadata",
        "state": "SUCCESSFUL",
        "submitTime": "2019-09-04T15:58:39.131591882Z",
        "endTime": "2019-09-04T15:58:43.099020580Z"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.PurgeProductsRequest",
        "parent": "projects/project-id/locations/location-id",**"productSetPurgeConfig": {
          "productSetId": " project-set-id"
        },
        "force": true**
      }
    }

You should see output similar to the following for a completed **purge orphaned products operation** :
    
    
    {
      "name": "locations/location-id/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.BatchOperationMetadata",
        "state": "SUCCESSFUL",
        "submitTime": "2019-09-04T16:08:38.278197397Z",
        "endTime": "2019-09-04T16:08:45.075778639Z"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.PurgeProductsRequest",
        "parent": "projects/project-id/locations/location-id",**"deleteOrphanProducts": true,
        "force": true**
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
