---
url: https://docs.cloud.google.com/vision-ai/docs/image-warehouse-creation/
title: Create and update an Image Warehouse \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:04.571888+00:00
---

# Create and update an Image Warehouse  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/image-warehouse-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Create and update an Image Warehouse Stay organized with collections  Save and categorize content based on your preferences. 

An Image Warehouse is where you can storage and manage your images, as well as annotations on images.

## Create an Image Warehouse

First, you need to create a corpus.

### REST & CMD LINE

Creates a corpus resource under the given project with the option to specify the `Corpus` display name and description.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * DISPLAY_NAME: Display name for the warehouse.
  * WAREHOUSE_DESCRIPTION: The description of the warehouse (`corpus`).



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora

Request JSON body: 
    
    
    {
      "display_name": "DISPLAY_NAME",
      "description": "WAREHOUSE_DESCRIPTION",
      "type": "IMAGE",
      "search_capability_setting": {
        "search_capabilities": {
          "type": "EMBEDDING_SEARCH"
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/warehouseoperations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.CreateCorpusMetadata"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.Corpus",
        "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID",
        "displayName": "DISPLAY_NAME",
        "description": "WAREHOUSE_DESCRIPTION",
        "type": "IMAGE",
        "search_capability_setting": {
          "search_capabilities": {
            "type": "EMBEDDING_SEARCH"
          }
        }
      }
    }
    

### Create data schema

If you want to import annotations, you need to create a corresponding data schema before calling the Import API.

### REST & CMD LINE

This sample shows you how to create a data schema in an existing corpus.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * DATASCHEMA_KEY: This key must match the key of a user-specified annotation and unique inside a `corpus`. For example, `data-key`.
  * ANNOTATION_DATA_TYPE: The data type of the annotation. Available values are: 
    * `DATA_TYPE_UNSPECIFIED`
    * `INTEGER`
    * `FLOAT`
    * `STRING`
    * `DATETIME`
    * `GEO_COORDINATE`
    * `PROTO_ANY`
    * `BOOLEAN`

For more information, see the [API reference documentation](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.dataSchemas#datatype). 

  * ANNOTATION_GRANULARITY: The granularity of the annotations under this `dataSchema`. Available values are: 
    * `GRANULARITY_UNSPECIFIED` \- Unspecified granularity.
    * `GRANULARITY_ASSET_LEVEL` \- Asset-level granularity (annotations must not contain temporal partition information for the media asset). 
    * `GRANULARITY_PARTITION_LEVEL` \- Partition-level granularity (annotations must contain temporal partition information for the media asset). 
  * SEARCH_STRATEGY: One of the available enum values. The types of search strategies to be applied on the annotation key. Available values are: 
    * `NO_SEARCH`
    * `EXACT_SEARCH`
    * `SMART_SEARCH`



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas

Request JSON body: 
    
    
    {
      "key": "DATASCHEMA_KEY",
      "schema_details": {
        "type": "ANNOTATION_DATA_TYPE",
        "granularity": "ANNOTATION_GRANULARITY",
        "search_strategy": {
          "search_strategy_type": "SEARCH_STRATEGY"
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID",
      "key": "data-key",
      "schemaDetails": {
        "type": "BOOLEAN",
        "granularity": "GRANULARITY_ASSET_LEVEL",
        "searchStrategy": {
          "search_strategy_type": "EXACT_SEARCH"
        }
      }
    }
    

## Import assets to an image corpus

Import assets (and optionally annotations) to an existing corpus under the given project.

The Cloud Storage file for the ImportAsset request needs to be in JSONL format. In the file, each line corresponds to one asset and will be converted into `InputImageAsset` proto. For example,
    
    
    {"gcsUri":"gs://test/test1.png","assetId":"asset1","annotations":[{"key":"title","value":{"strValue":"cat"}}]}
    {"gcsUri":"gs://test/test2.png","assetId":"asset2","annotations":[{"key":"title","value":{"strValue":"dog"}}]}
    {"gcsUri":"gs://test/test3.png","assetId":"asset3","annotations":[{"key":"title","value":{"strValue":"rabbit"}}]}
    

### REST & CMD LINE

This sample shows you how to import assets (and optionally annotations) to a corpus resource under the given project.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets:import

Request JSON body: 
    
    
    {
      "parent": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID,
      "assets_gcs_uri": GCS_URI
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets:import"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets:import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/operations/OPERATION_ID",
    }
    

w

## Analyze assets in the corpus

To prepare for image search, AnalyzeCorpus needs to be run in order to generate the embedding signals from images.

### REST & CMD LINE

This sample shows you how to perform AnalyzeCorpus on a corpus resource.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:analyze

Request JSON body: 
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:analyze"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:analyze" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/operations/OPERATION_ID",
    }
    

## Create an index

### REST & CMD LINE

This sample shows you how to create an index on a corpus resource.

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
    

## Create an index endpoint

### REST & CMD LINE

This sample shows you how to create an index endpoint.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * INDEX_ENDPOINT_ID: (_Optional_) A user-provided value for the index endpoint ID. In this request, the value is added to the request URL in the form: 
    * https://REGIONALIZED_ENDPOINT/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/indexEndpoints**?index_endpoint_id= INDEX_ENDPOINT_ID**



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/indexEndpoints

Request JSON body: 
    
    
    {
      "display_name": "DISPLAY_NAME",
      "description": "DESCRIPTION",
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/indexEndpoints"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/indexEndpoints" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/indexEndpoints/INDEX_ENDPOINT_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.CreateIndexEndpointMetadata"
      }
    }
    

## Deploy index to index endpoint

### REST & CMD LINE

This sample shows you how to deploy an index to an index endpoint resource.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * INDEX_ENDPOINT_ID: The ID of your target index endpoint.
  * CORPUS_ID: The ID of your target corpus.
  * INDEX_ID: The ID of your target index.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/indexEndpoints/INDEX_ENDPOINT_ID**:deployIndex**

Request JSON body: 
    
    
    {
      "deployedIndex": {
        "index": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID"
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/indexEndpoints/INDEX_ENDPOINT_ID**:deployIndex** "

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/indexEndpoints/INDEX_ENDPOINT_ID**:deployIndex** " | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/indexEndpoints/INDEX_ENDPOINT_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.DeployIndexMetadata",
        "deployedIndex": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/indexes/INDEX_ID"
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
