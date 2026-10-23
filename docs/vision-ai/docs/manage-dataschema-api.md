---
url: https://docs.cloud.google.com/vision-ai/docs/manage-dataschema-api/
title: Manage data schema \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:47.642833+00:00
---

# Manage data schema  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/manage-dataschema-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Manage data schema Stay organized with collections  Save and categorize content based on your preferences. 

The Vision Warehouse API allows you to manage Vision Warehouse resources using the command line.

## Create a data schema

Image corpus can only create asset level granularity data schema. Streaming video corpus can create both asset level granularity data schema and partition level granularity data schema. Batch video corpus can create both asset level granularity data schema and partition level granularity data schema.

### REST

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
    

### Add custom struct data schema

Custom struct allows users to define more complex containers to hold values and provide search capabilities. To use this feature, the data schema needs to be defined, for example:

### REST

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas

Request JSON body: 
    
    
    {
      "key": "person",
      "schema_details" : {
        "type":"CUSTOMIZED_STRUCT",
        "granularity":"GRANULARITY_ASSET_LEVEL",
        "customized_struct_config": {
          "field_schemas": {
             "name": {
                "type":"STRING",
                "granularity":"GRANULARITY_ASSET_LEVEL",
                "search_strategy": {
                   "search_strategy_type":"EXACT_SEARCH"
                }
             },
             "age": {
                "type":"FLOAT",
                "granularity":"GRANULARITY_ASSET_LEVEL",
                "search_strategy": {
                   "search_strategy_type":"EXACT_SEARCH"
                }
             }
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
      "key": "person",
      "schemaDetails" : {
        "type":"CUSTOMIZED_STRUCT",
        "granularity":"GRANULARITY_ASSET_LEVEL",
        "customized_struct_config": {
          "field_schemas": {
             "name": {
                "type":"STRING",
                "granularity":"GRANULARITY_ASSET_LEVEL",
                "search_strategy": {
                   "search_strategy_type":"EXACT_SEARCH"
                }
             },
             "age": {
                "type":"FLOAT",
                "granularity":"GRANULARITY_ASSET_LEVEL",
                "search_strategy": {
                   "search_strategy_type":"EXACT_SEARCH"
                }
             }
          }
        }
      }
    }
    

After which, we can insert annotations

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * ASSET_ID: The ID of your target asset.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations

Request JSON body: 
    
    
    {
      "user_specified_annotation" : {
        "key": "person",
        "value": {
          "customized_struct_value":{
            "elements" : {
              "name": {
                "str_value":"John"
              },
              "age": {
                "float_value":10.5
              }
            }
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
        "key": "person",
        "value": {
          "customized_struct_value":{
            "elements" : {
              "name": {
                "str_value":"John"
              },
              "age": {
                "float_value":10.5
              }
            }
          }
        }
      }
    }
    

Once the annotation is indexed, a search request can be issued like so:

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:searchAssets

Request JSON body: 
    
    
    {
      "page_size": 10,
      "criteria": {
        "field": "person.name",
        "text_array": {
          "txt_values": "John"
        },
      },
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:searchAssets"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:searchAssets" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "searchResultItems": [
        {
          "asset": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID1",
          "segments": [
            {
              "startTime": "2020-09-01T02:51:55Z",
              "endTime": "2020-09-01T02:52:09.996016Z"
            }
          ],
          "segment": {
            "startTime": "2023-07-07T16:36:10.652575Z",
            "endTime": "2023-07-07T20:30:48.812575Z"
          }
        }
      ]
    }
    

## Update a data schema

### REST & CMD LINE

The following code updates a `dataSchema` using the [`projects.locations.corpora.dataSchemas.patch`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.dataSchemas/patch) method.

This sample uses `?updateMask=schemaDetails.type,schemaDetails.granularity` in the request URL. It includes `schemaDetails.type` and `schemaDetails.granularity` values in the request body to update the data schema.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * DATASCHEMA_ID: The ID of your target data schema.
  * `?updateMask=fieldToUpdate`: One of the available fields you can apply an `updateMask` to. Specify the corresponding new field value in the request body. This new value replaces the existing field value. Available fields: 
    * Key: `?updateMask=key`
    * Schema type: `?updateMask=schemaDetails.type`
    * Schema granularity: `?updateMask=schemaDetails.granularity`
    * Schema search strategy type: `?updateMask=schemaDetails.searchStrategy.searchStrategyType`
    * Update all fields: `?updateMask=*`



HTTP method and URL: 
    
    
    PATCH https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID**?updateMask= schemaDetails.type,schemaDetails.granularity**

Request JSON body: 
    
    
    {
      "key": "original-data-key",
      "schemaDetails": {
        "type":"INTEGER",
        "granularity":"GRANULARITY_PARTITION_LEVEL"
        "searchStrategy": {
          "searchStrategyType": "NO_SEARCH"
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID**?updateMask= schemaDetails.type,schemaDetails.granularity**"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID**?updateMask= schemaDetails.type,schemaDetails.granularity**" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID",
      "key": "original-data-key",
      "schemaDetails": {
        "type": "INTEGER",
        "granularity": "GRANULARITY_PARTITION_LEVEL",
        "searchStrategy": {
          "searchStrategyType": "NO_SEARCH"
        }
      }
    }
    

## List data schema in a corpus

List all `DataSchema` under a specific corpus. The response contains all `DataSchema` resources, each with a `DataSchema` resource name that can be used to get a specific `DataSchema`.

### REST

To list data schema, send a GET request by using the [projects.locations.corpora.dataSchemas.list](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.dataSchemas/list) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    GET https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "dataSchemas": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/KEY_STRING1",
          "key": "KEY_STRING1",
          "schemaDetails": {
            "type": "STRING",
            "granularity": "GRANULARITY_ASSET_LEVEL",
            "searchStrategy": {
              "searchStrategyType": "EXACT_SEARCH"
            }
          }
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/KEY_STRING2",
          "key": "KEY_STRING2",
          "schemaDetails": {
            "type": "PROTO_ANY",
            "granularity": "GRANULARITY_PARTITION_LEVEL",
            "protoAnyConfig": {
              "typeUri": "type.googleapis.com/google.cloud.visionai.v1.VideoActionRecognitionPredictionResult"
            },
            "searchStrategy": {
              "searchStrategyType": "SMART_SEARCH"
            }
          }
        }
      ]
    }
    

## Get a data schema

Get the `DataSchema` of a specific `DataSchema` resource name.

### REST

To get details about a specific data schema, send a GET request by using the [projects.locations.corpora.dataSchemas.get](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.dataSchemas/get) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * DATASCHEMA_ID: The ID of your target data schema.



HTTP method and URL: 
    
    
    GET https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/KEY_STRING",
      "key": "KEY_STRING",
      "schemaDetails": {
        "type": "STRING",
        "granularity": "GRANULARITY_ASSET_LEVEL",
        "searchStrategy": {
          "searchStrategyType": "EXACT_SEARCH"
        }
      }
    }
    

## Delete a data schema

### REST & CMD LINE

The following code sample deletes a warehouse `dataSchema` using the [`projects.locations.corpora.dataSchemas.delete`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.dataSchemas/delete) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * DATASCHEMA_ID: The ID of your target data schema.



HTTP method and URL: 
    
    
    DELETE https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/DATASCHEMA_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

## Modify warehouse schema details (console)

Schema fields are generated from the models through the applications. You can also [add custom fields](https://docs.cloud.google.com/vision-ai/docs/search-cli-streaming-warehouse#create-searchconfig).

After you modify the facetable fields, you can use them to [search](https://docs.cloud.google.com/vision-ai/docs/search-streaming-warehouse) your warehouse.

### Console

  1. Open the **Warehouses** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Warehouses tab](https://console.cloud.google.com/ai/vision-ai/media-warehouse)

  2. Find your warehouse corpus, and select its name. The **Warehouse Details** page appears.

  3. Select the fields you want to enable for search.




![Select facetable search fields in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/select-facetable-fields.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
