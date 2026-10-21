---
url: https://docs.cloud.google.com/vision-ai/docs/search-cli-streaming-warehouse/
title: Search streaming video warehouse data using the command line \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:46.939982+00:00
---

# Search streaming video warehouse data using the command line  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/search-cli-streaming-warehouse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Search streaming video warehouse data using the command line Stay organized with collections  Save and categorize content based on your preferences. 

After you have created a Vision Warehouse, added it to an app, and deployed the app, you can search the data stored in the streaming video warehouse.

## Search streaming video metadata

To search the data ([`assets`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.assets)) in your warehouse ([`corpus`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora)), populate the [`SearchAssetsRequest`](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#searchassetsrequest) with the content that you would like to find. This content comes in a few different formats:

  1. [`criteria`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora/searchAssets#Criteria) \- Text, number, or date content provided by the user.
  2. [`facet_selections`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora/searchAssets#FacetGroup) \- Text content returned by the server, and selected by the user.
  3. [`content_time_ranges`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora/searchAssets#DateTimeRangeArray) \- Date ranges that all returned content must fall in.



In the following example, consider a Warehouse that contains security camera footage from different types of stores across the country. To retrieve all assets for the years 2018 _or_ 2020 tagged with the annotation `"state": "California"`, or the annotation `"state":"Pennsylvania"`, send the following request:

### REST

To search assets, send a POST request by using the [projects.locations.corpora.searchAssets](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora/searchAssets) method. 

In this sample body the [`criteria`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.corpora/searchAssets#Criteria) field use `textArray` values to provide two `txt_values`: "California" and "Pennsylvania". You can also provide search criteria for other data types. You can only specify one type of search criteria in each request. 

#### Additional search criteria options

**Integer ranges (inclusive)**
    
    
        "int_range_array" : {
          "int_ranges": { "start": "5", "end": "10" }
          "int_ranges": { "start": "20", "end": "30" }
        }
        

**Float ranges (inclusive)**
    
    
        "float_range_array" : {
          "float_ranges": { "start": "2.6", "end": "14.3" }
          "float_ranges": { "start": "205.3", "end": "205.8" }
        }
        

**Geolocations (coordinate and radius)**
    
    
        "geo_location_array": {
          "circle_areas": {
            "latitude": "37.4221",
            "longitude": "122.0841",
            "radius_meter": "500"
          },
          "circle_areas": {
            "latitude": "12.46523",
            "longitude": "-95.2146",
            "radius_meter": "100"
          }
        }
        

**Booleans**
    
    
        "bool_value" : {
          "value": "true"
        }
        

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:searchAssets

Request JSON body: 
    
    
    {
      "page_size": "2",
      "content_time_ranges": {
        "date_time_ranges": {
          "start": {
            "year":"2018",
            "month":"1",
            "day":"1",
          },
          "end": {
            "year":"2019",
            "month":"1",
            "day":"1",
          }
        },
        "date_time_ranges": {
          "start": {
            "year":"2020",
            "month":"1",
            "day":"1",
          },
          "end": {
            "year":"2021",
            "month":"1",
            "day":"1",
          }
        }
      },
      "criteria": {
        "field": "state",
        "text_array": {
          "txt_values": "California",
          "txt_values": "Pennsylvania"
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
      "next_page_token": "jfyq45",
      "searchResultItems": [
        {
          "asset": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID1",
          "segments": [
            {
              "startTime": "2020-09-01T02:51:55Z",
              "endTime": "2020-09-01T02:52:09.996016Z"
            }
          ]
        },
        {
          "asset": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID2",
          "segments": [
            {
              "startTime": "2018-09-04T06:31:53Z",
              "endTime": "2018-09-04T0:7:31:53Z"
            }
          ]
        }
      ],
      "facetResults": [
        {
          "facetId": "state",
          "displayName": "State",
          "buckets": [
            {
              "value": {
                "stringValue": "California"
              }
            },
            {
              "value": {
                "stringValue": "Pennsylvania"
              }
            }
          ],
          "bucketType": "FACET_BUCKET_TYPE_VALUE"
        },
        {
          "facetId": "store-type",
          "displayName": "StoreType",
          "buckets": [
            {
              "value": {
                "stringValue": "Sporting Goods"
              }
            },
            {
              "value": {
                "stringValue": "Grocery"
              }
            }
          ],
          "bucketType": "FACET_BUCKET_TYPE_VALUE"
        }
     ]
    }
    

To retrieve the next page of results, pass the original request parameters appended with the returned `next_page_token`.

The `facet_results` array shows content that matched the original query. The response above indicates that one of the security cameras is stationed at a sporting goods store, while the other one is stationed at a grocery store.

To restrict this query to only show the grocery store footage, pass back the same request with a _facet selection_.

**Request JSON body with _facet selection_** :
    
    
    {
      "page_size": "2",
      "content_time_ranges": {
        "date_time_ranges": {
          "start": {
            "year":"2018",
            "month":"1",
            "day":"1",
          },
          "end": {
            "year":"2018",
            "month":"12",
            "day":"31",
          }
        },
        "date_time_ranges": {
          "start": {
            "year":"2020",
            "month":"1",
            "day":"1",
          },
          "end": {
            "year":"2020",
            "month":"12",
            "day":"31",
          }
        }
      },
      "criteria": {
        "field": "state",
        "text_array": {
          "txt_values": "California",
          "txt_values": "Pennsylvania"
        }
      },
      "facet_selections": {
        "facetId": "state",
        "displayName": "State",
        "buckets": {
            "value": {
             "stringValue": "California"
            }
        },
        "buckets": {
          "value": {
            "stringValue": "Pennsylvania"
          }
        },
        "bucketType": "FACET_BUCKET_TYPE_VALUE"
      },**"facet_selections": {
        "facetId": "store-type",
        "displayName": "StoreType",
        "buckets": {
          "value": {
            "stringValue": "Sporting Goods"
          }
        },
        "buckets": {
          "value": {
            "stringValue": "Grocery"
          },
          "selected": "true"
        },**
        "bucketType": "FACET_BUCKET_TYPE_VALUE"
      }
    }

Because the _Grocery_ facet is selected, any response will contain the annotation `"store-type":"Grocery"`.

### Return clip asset metadata when searching

The Gemini Enterprise Agent Platform Vision API also allows users to specify extra clip metadata to return with the search result, using `result_annotation_keys`.

### REST

In this example the user provided annotation key `"camera-location"` is specified in the request body, and the key's value (`"Sunnyvale"`) is provided in the response. 

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:searchAssets

Request JSON body: 
    
    
    {
       "page_size": "2",
       "criteria": {
         "field": "state",
         "text_array": {
           "txt_values": "California",
           "txt_values": "Pennsylvania"
         }
       },**"result_annotation_keys": "camera-location"**
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
      "next_page_token": "jfyq45",
      "searchResultItems": [
        {
          "asset": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID",
          "segments": [
            {
              "startTime": "2020-09-01T02:51:55Z",
              "endTime": "2020-09-01T02:52:09.996016Z"
            }
          ],**"requestedAnnotations": [
            {
              "name": "projects/ PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations/ANNOTATION_ID",
              "userSpecifiedAnnotation": {
                "key": "camera-location",
                "value": {
                   "str_value": "Sunnyvale"
                },
              }
            }
          ]**
      ],
      "facetResults": [
        {
          "facetId": "state",
          "displayName": "State",
          "buckets": [
            {
              "value": {
                "stringValue": "California"
              }
            },
            {
              "value": {
                "stringValue": "Pennsylvania"
              }
            }
          ],
          "bucketType": "FACET_BUCKET_TYPE_VALUE"
        },
        {
          "facetId": "store-type",
          "displayName": "StoreType",
          "buckets": [
            {
              "value": {
                "stringValue": "Sporting Goods"
              }
            },
            {
              "value": {
                "stringValue": "Grocery"
              }
            }
          ],
          "bucketType": "FACET_BUCKET_TYPE_VALUE"
        },
    
     ]
    }
    

### Use criteria to return asset metadata in search

You can specify in search criteria whether to return the matched annotations for each search result item. This feature is supported for limited data schema types: `INTEGER`, `FLOAT`, `BOOLEAN`, `STRING` (`EXACT_SEARCH` only), and the annotation must be on partition-level.

Assume you create the following data schema in a warehouse corpus:
    
    
    {
      "key": "image-classification",
      "schema_details": {
        "type":"STRING",
        "granularity":"GRANULARITY_PARTITION_LEVEL",
        "search_strategy": {
          "search_strategy_type":"EXACT_SEARCH"
        }
      }
    }

Some annotations for `"image-classification"` are ingested to the corpus using streaming video ingestion or a `CreateAnnotation` request.

After there are annotations ingested, you can search for `"image-classification"` and get video results and their corresponding annotations:

### REST

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:searchAssets

Request JSON body: 
    
    
    {
      "page_size": "5",
      "facet_selections": {
        "facet_id": "image-classification",**"fetch_matched_annotations": " true",**
        "bucket_type": "FACET_BUCKET_TYPE_VALUE",
          "buckets": {
            "value": {
              "string_value": "cat"
            },
            "selected" : "true"
          },
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
          "asset": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID",
          "segments": [
            {
              "startTime": "2021-09-01T03:51:55Z",
              "endTime": "2021-09-01T03:52:05Z"
            }
          ],**"annotationMatchingResults": [
            {
              "criteria": {
                "field": "image-classification",
                "textArray": {
                  "txtValues": [
                    "cat"
                  ]
                },
                "fetchMatchedAnnotations": true
              },
              "matchedAnnotations": [
                {
                  "name": "projects/ PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations/ANNOTATION_ID",
                  "userSpecifiedAnnotation": {
                    "key": "image-classification",
                    "value": {
                      "protoAnyValue": {
                        "@type": "type.googleapis.com/google.cloud.visionai.v1.ClassificationPredictionResult",
                        "displayNames": [
                          "cat"
                        ]
                      }
                    },
                    "partition": {
                      "temporalPartition": {
                        "startTime": "2021-09-01T03:51:55Z",
                        "endTime": "2021-09-01T03:52:00Z"
                      }
                    }
                  }
                }
              ]
            }
          ]**,
          "segment": {
            "startTime": "2021-09-01T03:51:55Z",
            "endTime": "2021-09-01T03:52:05Z"
          }
        }
    }
    

### Use global search to return asset metadata in search

Global search provides a place for users to enter search queries, instead of specifying individual criteria. You can search against string-type criteria set to be searchable in its data schema. The matching results are retrieved and returned to you. 

To use this feature, set the `search_query` field in the [`SearchAssetsRequest`](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#searchassetsrequest):

### REST

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:searchAssets

Request JSON body: 
    
    
    {
        "page_size": "2",
        "search_query': "Pennsylvania"
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
      "next_page_token": "jfyq45",
      "searchResultItems": [
      {
        "asset": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID",
        "segments": [
          {
            "startTime": "2020-09-01T02:51:55Z",
            "endTime": "2020-09-01T02:52:09.996016Z"
          }
        ],**"requestedAnnotations": [
          {
            "name": "projects/ PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/assets/ASSET_ID/annotations/ANNOTATION_ID",
            "userSpecifiedAnnotation": {
              "key": "camera-location",
              "value": {
                "str_value": "Sunnyvale"
              },
            }
          }
        ],**
        "facetResults": [
        {
          "facetId": "state",
          "displayName": "State",
          "buckets": [
            {
              "value": {
                "stringValue": "California"
              }
            },
            {
              "value": {
                "stringValue": "Pennsylvania"
              }
            }
          ],
          "bucketType": "FACET_BUCKET_TYPE_VALUE"
        },
        ]
      }
    }
    

### Apply sort spec to order returned-asset metadata in search

You can use the sorting feature to sort search results by user provided `annotation`. This can be useful for sorting results with data schema types that can be ordered, such as string and numeric types. 

To use this feature, specify `schema_key_sorting_strategy`, which requires at least a data schema key and ascending/descending order:

### REST

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:searchAssets

Request JSON body: 
    
    
    {
        "page_size": "2",
        "schemaKeySortingStrategy":
        { "options": 
          { 
            "data_schema_key": "stream-display-name", 
            "sort_decreasing": true
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

You should receive a successful status code (2xx) and an empty response.

## Create search configurations

Vision Warehouse allows users to customize their search experience through search configuration. Search Configuration uses video data - such as user-provided annotations and insights generated by Google Cloud video understanding models - to provide additional search options to the user. For example, if you want to target clips with specific color vehicles from car video data in your warehouse, you can use a specific search configuration for your query.

You can use a [`SearchConfig`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs) to set more granular configuration options.

The following example shows you how to create a [`SearchConfig`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs) resource.

### General guidelines

For all use cases your request must meet the following conditions to execute successfully:

  1. `Request.search_configuration.name` must not already exist.
  2. The [`mapped_fields`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs#searchcriteriaproperty) array must not be empty, and must map to _existing_ user-given annotation keys.
  3. All `mapped_fields` must be of the same type.
  4. All `mapped_fields` must share exact/smart match config.
  5. All `mapped_fields` must share the same granularity.



There are several use cases for creating a `SearchConfig`, each with distinct guidelines you must follow.

### Create a search config with custom search criteria

This section describes how to map a custom operator to one or more user-given annotation keys. In this case you need to satisfy the general guidelines when building your request.

### REST

You must specify your new `SearchConfig` ID at the end of the request URL, _not_ as a field in the request.

The user-given annotation keys in this example are `"player"`, `"coach"`, and `"cheerleader"`.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG: The name of your target `SearchConfig`. 
    * The `SearchConfig` in this example is `person`.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** person

Request JSON body: 
    
    
    {
       "search_criteria_property": {
         "mapped_fields": "player",
         "mapped_fields": "coach",
         "mapped_fields": "cheerleader",
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** person"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** person" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/person",
      "searchCriteriaProperty":
        {
          "mappedFields": [
            "player",
            "coach",
            "cheerleader"
          ]
        }
    }
    

### Create a search config with 1:1 facet mapping

To create a facet for a single user-given annotation key, you must ensure that `Request.search_configuration.facet_property.mapped_fields` contains a single element. This element's value must be a user-given annotation key name.

**Note:** If you want the user-given annotation key to display as a facet name, set `search_config_id==facet_property.mapped_fields[0]`.

The following example shows you how to create a facet mapping for the user-given annotation key `"Location"`.

### REST

You must specify your new `SearchConfig` ID at the end of the request URL, _not_ as a field in the request.

In this example, the request succeeds because the `search_config_id` (`Location`) in the request URL references an existing user-given annotation key, _and_ `mapped_fields` contains exactly one element with a value equal to `search_config_id` (`Location`).

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG: The name of your target `SearchConfig`. 
    * The `SearchConfig` in this example is `Location`.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** Location

Request JSON body: 
    
    
    {
       "facet_property": {
         "mapped_fields": "Location",
         "display_name": "Location",
         "result_size": "5",
         "bucket_type":"FACET_BUCKET_TYPE_VALUE"
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** Location"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** Location" | Select-Object -Expand Content
    
    
    
    

The following requests fail due to not meeting the necessary requirements.

#### Failed requests

**Failed request 1:**
    
    
          curl -X POST \
          -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          -H "Content-Type: application/json; charset=utf-8" \
          https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** Location \
          -d "{
             "facet_property": {
               "mapped_fields": "City", /* City is not equal to search_config_id. */
               "display_name": "City",
               "result_size": "5",
               "bucket_type":"FACET_BUCKET_TYPE_VALUE"
            }
          }"
        

**Failed request 2:**
    
    
          curl -X POST \
          -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          -H "Content-Type: application/json; charset=utf-8" \
          https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** City \
          -d "{
             "facet_property": {
               "mapped_fields": "City", /* City doesn't map to an existing user-given annotation key. */
               "display_name": "City",
               "result_size": "5",
               "bucket_type":"FACET_BUCKET_TYPE_VALUE"
            }
          }"
        

**Failed request 3:**
    
    
          curl -X POST \
          -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          -H "Content-Type: application/json; charset=utf-8" \
          https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** Location \
          -d "{
             "facet_property": {
               "mapped_fields": "Location",
               "mapped_fields": "City", /* mapped_fields contains more than 1 element. */
               "display_name": "Location",
               "result_size": "5",
               "bucket_type":"FACET_BUCKET_TYPE_VALUE"
            }
          }"
        

### Create a search config with a custom 1:1 or more facet mapping

Clients that want to create a mapping between a custom facet value and one or more user-given annotation keys must ensure that:

  1. `Request.search_configuration` must contain a `SearchCriteriaProperty` such that [`Request.search_configuration.search_criteria_property.mapped_fields`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs#searchcriteriaproperty) contains the same elements as [`Request.search_configuration.facet_property.mapped_fields`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs#facetproperty).



### REST

You must specify your new `SearchConfig` ID at the end of the request URL, _not_ as a field in the request.

The following example shows you how to create a facet mapping for the user-given annotation keys `"City"` and `"State"`.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG: The name of your target `SearchConfig`. 
    * The `SearchConfig` in this example is `Location`.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** Location

Request JSON body: 
    
    
    {
      "search_criteria_property": {
         "mapped_fields": "City",
         "mapped_fields": "State",
         "mapped_fields": "Province",
      }
      "facet_property": {
         "mapped_fields": "City",
         "mapped_fields": "State",
         "display_name": "Province",
         "result_size": "5",
         "bucket_type":"FACET_BUCKET_TYPE_VALUE"
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** Location"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** Location" | Select-Object -Expand Content
    
    
    
    

The following requests fail due to not meeting the necessary requirements.

#### Failed requests

**Failed request 1:**
    
    
          curl -X POST \
          -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          -H "Content-Type: application/json; charset=utf-8" \
          https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** Location \
          -d "{
            "facet_property": { /* Request is missing a SearchCriteriaProperty object.*/
               "mapped_fields": "City",
               "mapped_fields": "State",
               "display_name": "Location",
               "result_size": "5",
               "bucket_type":"FACET_BUCKET_TYPE_VALUE"
            }
          }"
        

**Failed request 2:**
    
    
          curl -X POST \
          -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
          -H "Content-Type: application/json; charset=utf-8" \
          https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** Location \
          -d "{
            "search_criteria_property": {
               "mapped_fields": "City",
               "mapped_fields": "State",
            }
            "facet_property": {
               "mapped_fields": "City",
               "mapped_fields": "State",
               "mapped_fields": "Province", /* Province is missing from search_criteria_property. */
               "display_name": "Location",
               "result_size": "5",
               "bucket_type":"FACET_BUCKET_TYPE_VALUE"
            }
          }"
        

### Create a search config with range based facets

Range facets are similar to normal facets, but each facet bucket covers some continuous span. An additional configuration ([`range_facet_config`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs#facetproperty)) gives the system information about these facet bucket ranges.

Range facets are available for:

  1. Integers
  2. Dates



There are three types of range facets:

  1. Fixed range - Each bucket is the same size.
  2. Custom range - Programmable bucket sizes. For example, logarithmic.
  3. Date range - Fixed bucket granularities of `DAY`, `MONTH`, and `YEAR`. This only applies to date range facets.



The same conditions apply as singular facets, with some additional validation regarding the range specification.

#### Fixed range bucket specification

The following example creates a fixed range facet spec for the field `inventory-count`, and results in the buckets: `[-inf, 0), [0, 10), [10, 20), [20, 30), [30, inf]`.

### REST

You must specify your new `SearchConfig` ID at the end of the request URL, _not_ as a field in the request.

This request uses the [`FixedRangeBucketSpec`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs#fixedrangebucketspec) to create multiple buckets with equal granularities.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG: The name of your target `SearchConfig`. 
    * The `SearchConfig` in this example is `inventory-count`.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** inventory-count

Request JSON body: 
    
    
    {
      "facet_property": {
        "mapped_fields": "inventory-count",
        "display_name": "Inventory Count",
        "result_size": "5",
        "bucket_type":"FACET_BUCKET_TYPE_FIXED_RANGE",**"fixed_range_bucket_spec": {
           "bucket_start": {
             "integer_value": 0
           },
           "bucket_granularity": {
             "integer_value": 10
           },
           "bucket_count": 5
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** inventory-count"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** inventory-count" | Select-Object -Expand Content
    
    
    
    

#### Custom range bucket specification

The following example creates a fixed range facet spec for the field `video-views`, and results in the buckets: `[inf, 0), [0, 10), [10, 100), [100, 1000), [1000, 10000), [10000, inf)`.

### REST

You must specify your new `SearchConfig` ID at the end of the request URL, _not_ as a field in the request.

This request uses the [`CustomRangeBucketSpec`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs#CustomRangeBucketSpec) to specify how values are bucketized.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG: The name of your target `SearchConfig`. 
    * The `SearchConfig` in this example is `video-views`.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** video-views

Request JSON body: 
    
    
    {
      "facet_property": {
        "mapped_fields": "video-views",
        "display_name": "Video Views",
        "result_size": "6",
        "bucket_type":"FACET_BUCKET_TYPE_CUSTOM_RANGE",**"custom_range_bucket_spec": {
           "endpoints": {
             "integer_value": 0
           },
           "endpoints": {
             "integer_value": 10
           },
           "endpoints": {
             "integer_value": 100
           },
           "endpoints": {
             "integer_value": 1000
           },
           "endpoints": {
             "integer_value": 10000
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** video-views"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** video-views" | Select-Object -Expand Content
    
    
    
    

#### Date / time range bucket specification

The following example creates a date range spec for the field `film-date` with `DAY` granularity.

### REST

You must specify your new `SearchConfig` ID at the end of the request URL, _not_ as a field in the request.

This request uses the [`DateTimeBucketSpec`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs#DateTimeBucketSpec) to specify how date values are bucketized.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG: The name of your target `SearchConfig`. 
    * The `SearchConfig` in this example is `film-date`.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** film-date

Request JSON body: 
    
    
    {
      "facet_property": {
        "mapped_fields": "film-date",
        "display_name": "Film Date",
        "result_size": "5",
        "bucket_type": "FACET_BUCKET_TYPE_DATETIME",**"datetime_bucket_spec": {
           "granularity": " DAY"
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** film-date"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** film-date" | Select-Object -Expand Content
    
    
    
    

#### Use facet selections to search

After you create these facet buckets you can use them to search the warehouse.

### REST

This request uses [`facetSelections`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora/searchAssets#FacetGroup) objects to specify a group of facet buckets.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID:searchAssets

Request JSON body: 
    
    
    {
       "page_size": "10",**"facet_selections": {**
         "facet_id": "inventory-count",
         "buckets": {
           "range": {
             "end" : {
               "integer_value": 0
             }
           }
         },
         "buckets": {
           "range": {
             "start" : {
               "integer_value": 20
             },
             "end" : {
               "integer_value": 30
             }
           }
         }
       },**"facet_selections": {**
         "facet_id": "video-views",
         "buckets": {
           "range": {
             "start" : {
               "integer_value": 100
             },
             "end" : {
               "integer_value": 1000
             }
           }
         }
       },**"facet_selections": {**
         "facet_id": "film-date",
         "buckets": {
           "range": {
             "start" : {
               "datetime_value": {
                 "year": 2022,
                 "month": 9,
                 "day": 10
               }
             },
             "end" : {
               "datetime_value": {
                 "year": 2022,
                 "month": 9,
                 "day": 11
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
    
    
    
    

## Update a search configuration

To update the current `SearchConfig`, your request must fulfill the following requirements:

  1. [`Request.searchConfig.name`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs#resource:-searchconfig) must already exist.
  2. Request must contain at least one non-empty [`searchCriteriaProperty`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs#searchcriteriaproperty) or [`facetProperty`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs#facetproperty).
  3. The `mappedFields` array must not be empty, and must map to existing user-given annotation keys.
  4. All `mappedFields` must be of the same type.
  5. All `mappedFields` must share the same granularity.
  6. All `mappedFields` must share the same semantic `SearchConfig` match options.



### REST & CMD LINE

The following code sample updates a warehouse search configuration resource using the [`projects.locations.corpora.searchConfigs.patch`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs/patch) method.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT: Your Google Cloud [project ID or project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG_ID: The ID of your target `SearchConfig`. 
  * `"mappedFields"`: One or more existing user-given annotation keys.



HTTP method and URL: 
    
    
    PATCH https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID

Request JSON body: 
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID1",
      "searchCriteriaProperty": {
        "mappedFields": "dataschema2"
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
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID"

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
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID1",
      "searchCriteriaProperty": {
        "mappedFields": [
          "dataschema2"
        ]
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
