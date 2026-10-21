---
url: https://docs.cloud.google.com/vision-ai/docs/manage-indexes-api/
title: Manage indexes \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:46.773024+00:00
---

# Manage indexes  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/manage-indexes-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Manage indexes Stay organized with collections  Save and categorize content based on your preferences. 

A Vision Warehouse index (available to image and batch video verticals) is a corpus-level resource that is a managed representation of analyzed [assets](https://docs.cloud.google.com/vision-ai/docs/manage-assets-api) and [annotations](https://docs.cloud.google.com/vision-ai/docs/manage-annotations-api). An index can be viewed as a dataset of embedding vectors and semantic restrictions that represents the meaning of the media content. Indexes can be deployed into [index endpoints](https://docs.cloud.google.com/vision-ai/docs/manage-index-endpoints-api) for search.

When you create an index on a `corpus`, the index will include all [analyzed](https://docs.cloud.google.com/vision-ai/docs/manage-assets-api) assets and all existing annotations in the corpus. For any assets or annotations that you add after creating the index, you need to analyze the corpus or those assets again and update the index to include them in the index.

## Create a warehouse index

**Note:** The `CreateIndex` batch operation performs initial resource provisioning and batch processing of the entire corpus, which can be time consuming.

### REST

To create an index resource, send a POST request by using the [`projects.locations.corpora.indexes.create`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes/create) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * INDEX_ID: (_Optional_) A user-provided value for the index ID. In this request, the value is added to the request URL in the form: 
    * https://REGIONALIZED_ENDPOINT/v1/[...]/corpora/CORPUS_ID/indexes**?index_id= INDEX_ID**



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes

Request JSON body: 
    
    
    {
      "display_name": "DISPLAY_NAME",
      "description": "INDEX_DESCRIPTION",
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.CreateIndexMetadata"
      }
    }
    

## Update a warehouse index

The UpdateIndex API allows updating the metadata fields of the index, like `display_name` and `description`, as well as the underlying index contents (`assets` and their `annotations`).

The `update_mask` field in the request, also known as the field mask, is used to specify the fields to be overwritten in the Index resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field of the resource will be overwritten if it is in the mask. Empty field mask is not allowed. If the mask is "*", it triggers a full update of the index, and also a whole rebuild of index data.

### REST

To update an index resource, send a PATCH request by using the [`projects.locations.corpora.indexes.patch`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes/patch) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * INDEX_ID: The ID of your target index.
  * `?update_mask=fieldToUpdate`: List of the available fields you want to apply an `update_mask` to. Specify the corresponding values for the new fields in the request body. This new value replaces the existing field value. You can specify multiple fields as comma separated values. Available fields: 
    * Display name: `?update_mask=display_name`
    * Description: `?update_mask=description`
    * Update underlying index data: `?update_mask=entire_corpus`
    * Update all fields: `?update_mask=*`



HTTP method and URL: 
    
    
    PATCH https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID**?update_mask=display_name,entire_corpus**

Request JSON body: 
    
    
    {
      "display_name": "DISPLAY_NAME",
      "entire_corpus": true
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID**?update_mask=display_name,entire_corpus** "

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID**?update_mask=display_name,entire_corpus** " | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.UpdateIndexMetadata"
      }
    }
    

### Streaming index updates

The `IndexAsset` and `RemoveIndexAsset` APIs allow [streaming updates](https://docs.cloud.google.com/vision-ai/docs/batch-video-warehouse-creation#index-asset) to indexes. These APIs are only supported on the Vision Warehouse for batch videos.

**Note:** The `UpdateIndex` batch operation processes the entire corpus, which can be time consuming. Reduce the frequency of the `UpdateIndex` operation as much as possible. For Batch Video Warehouse, you can use streaming index to update a small number of assets with much lower latency.

## List indexes in a warehouse

### REST

To list indexes under a corpus, send a GET request by using the [projects.locations.corpora.indexes.list](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes/list) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    GET https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "indexes": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID_1",
          "display_name": "DISPLAY_NAME_1",
          "description": "DESCRIPTION_1",
          "entireCorpus": true,
          "state": "CREATED"
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID_2",
          "display_name": "DISPLAY_NAME_2",
          "description": "DESCRIPTION_2",
          "entireCorpus": true,
          "state": "CREATED"
        }
      ]
    }
    

## Get an index

### REST

To get details about an index, send a GET request using the [projects.locations.corpora.indexes.get](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes/get) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * INDEX_ID: The ID of your target index.



HTTP method and URL: 
    
    
    GET https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID",
      "display_name": "DISPLAY_NAME",
      "description": "DESCRIPTION",
      "entireCorpus": true,
      "state": "CREATED"
    }
    

## View assets under an index

### REST

To get details on the assets present under an index, send a GET request using the [projects.locations.corpora.indexes.viewAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes/viewAssets) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * INDEX_ID: The ID of your target index.
  * PAGE_SIZE: (_Optional_) The number of results to return. 
  * PAGE_TOKEN: (_Optional_) The `nextPageToken` that was provided by the previous call response. This can be used to get the next page of the results. 



HTTP method and URL: 
    
    
    GET https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID**:viewAssets**?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID**:viewAssets**?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID**:viewAssets**?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "indexedAssets": [
        {
          "index": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID",
          "asset": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID_1"
        },
        {
          "index": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID",
          "asset": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID_2"
        }
      ],
      "nextPageToken": "NEXT_PAGE_TOKEN"
    }
    

### View indexed assets with a filter

You can provide a list of comma-separated asset IDs using the `filter` field in the [projects.locations.corpora.indexes.viewAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes/viewAssets) method to filter through all the assets under an index and only show the provided assets.

### REST

To list and filter assets present under an index, send a GET request using the [projects.locations.corpora.indexes.viewAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes/viewAssets) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * INDEX_ID: The ID of your target index.
  * PAGE_SIZE: (_Optional_) The number of results to return. 
  * PAGE_TOKEN: (_Optional_) The `nextPageToken` that was provided by the previous call response. This can be used to get the next page of the results. 
  * ASSET_ID_FILTER: (_Optional_) A comma-separated list of asset IDs you want filtered in the returned list. For example: 
    * `?filter=ASSET_ID_1"`
    * `?filter=ASSET_ID_1,ASSET_ID_2"`



HTTP method and URL: 
    
    
    GET https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID**:viewAssets**?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN&filter=ASSET_ID_FILTER

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID**:viewAssets**?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN&filter=ASSET_ID_FILTER"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID**:viewAssets**?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN&filter=ASSET_ID_FILTER" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "indexedAssets": [
        {
          "index": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID",
          "asset": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID_1"
        },
        {
          "index": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID",
          "asset": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID_2"
        }
      ],
      "nextPageToken": "NEXT_PAGE_TOKEN"
    }
    

## Delete an index

An index can only be deleted if it is not deployed to an `indexEndpoint`. Follow the [undeploying index](https://docs.cloud.google.com/vision-ai/docs/manage-index-endpoints-api#undeploy-index) guide prior to deleting a deployed index.

### REST

To delete an index resource, send a DELETE request using the [projects.locations.corpora.indexes.delete](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes/delete) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * INDEX_ID: The ID of your target index.



HTTP method and URL: 
    
    
    DELETE https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID/operations/OPERATION_ID",
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
