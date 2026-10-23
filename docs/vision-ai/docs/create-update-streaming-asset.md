---
url: https://docs.cloud.google.com/vision-ai/docs/create-update-streaming-asset/
title: Create and update a warehouse asset \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:54.224773+00:00
---

# Create and update a warehouse asset  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/create-update-streaming-asset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Create and update a warehouse asset Stay organized with collections  Save and categorize content based on your preferences. 

A connected Vision Warehouse (`corpus`) in a data-ingesting deployed app has one or more media object resources (for example, video resources). These media objects (`asset` resources) contain metadata and resource annotations. Use the following commands to create and update these media objects.

## Create a streaming video warehouse asset

After you have [created a warehouse](https://docs.cloud.google.com/vision-ai/docs/create-manage-streaming-warehouse) (`corpus` resource), you can add one or more video `asset` resources to the warehouse.

### REST & CMD LINE

The following code creates a new asset under the given warehouse (`corpus`) with the option to specify the asset's ID and a TTL.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * ASSET_ID: (Optional) A user-provided value for the asset ID. In this request, the value is added to the request URL in the form: 
    * https://ENDPOINT/v1/[...]/corpora/CORPUS_ID/assets**?asset_id= ASSET_ID**
  * TIME_TO_LIVE: The amount of time to live (TTL) for all assets under a corpus, or the TTL of a specific asset. For example, for a corpus with assets with a TTL of 100 days, provide the value `8640000` (seconds). 



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets

Request JSON body: 
    
    
    {
      "ttl": {
        "seconds": TIME_TO_LIVE
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID",
      "ttl": "TIME_TO_LIVEs"
    }
    

###  Gemini Enterprise Agent Platform Vision SDK 

To send a request to read a model output stream you must [install the Gemini Enterprise Agent Platform Vision SDK](https://docs.cloud.google.com/vision-ai/docs/cloud-environment#install_the_streams_sdk).

When using the `vaictl` command line tool to create an asset you are not able to specify an asset ID or TTL.

Make the following variable substitutions:

  * PROJECT_NUMBER: Your Google Cloud project number.
  * LOCATION_ID: Your location ID. For example, `us-central1`. [Supported regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). [More information](https://docs.cloud.google.com/about/locations).
  * CORPUS_ID: The ID of the target warehouse (`corpus` resource).


    
    
    vaictl --project-id=PROJECT_NUMBER \
    --location-id=LOCATION_ID \
    --service-endpoint=warehouse-visionai.googleapis.com \
    create asset CORPUS_ID
    

After an asset is created you can [ingest video data](https://docs.cloud.google.com/vision-ai/docs/create-manage-streams#ingest-videos) directly into the warehouse for that asset by using the `vaictl` command line tool.

## Update a streaming video warehouse asset

Use the following code sample to update an asset's time-to-live (TTL). You can only update the TTL field.

Use the `updateMask` query parameter in the following code sample to update an asset's TTL. You can use a query parameter to update the TTL field only. The `updateMask` works as follows:

  * If specified, only the fields in the `updateMask` are updated.
  * If update mask value is `*`, the request updates all the fields.
  * If the update mask is not specified, only the fields in the request URL with a value provided in the request body are updated.




### REST & CMD LINE

The following code samples modify an asset's TTL using the [`projects.locations.corpora.assets.patch`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.assets/patch) method.

#### Change a TTL value

This sample uses `?updateMask=ttl` in the request URL, and includes a new `ttl.seconds` value in the request body to update the asset.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * ASSET_ID: The ID of your target asset.
  * `?updateMask=fieldToUpdate`: One of the available fields you can apply an `updateMask` to. Available fields: 
    * Time-to-live (TTL): `?updateMask=ttl`
    * Update all fields: `?updateMask=*`



HTTP method and URL: 
    
    
    PATCH https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID**?updateMask=ttl**

Request JSON body: 
    
    
    {
      "ttl": {
        "seconds": "1"
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID**?updateMask=ttl** "

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID**?updateMask=ttl** " | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID"
    }
    

#### Remove a TTL value

This sample uses `?updateMask=ttl` in the request URL, and includes an empty request body to clear the asset's TTL value.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * ASSET_ID: The ID of your target asset.
  * `?updateMask=fieldToUpdate`: One of the available fields you can apply an `updateMask` to. Available fields: 
    * Time-to-live (TTL): `?updateMask=ttl`
    * Update all fields: `?updateMask=*`



HTTP method and URL: 
    
    
    PATCH https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID**?updateMask=ttl**

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID**?updateMask=ttl** "

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID**?updateMask=ttl** " | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
