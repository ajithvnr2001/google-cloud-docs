---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/data-objects/batch-search/
title: gcloud beta vector-search collections data-objects batch-search \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:59.729782+00:00
---

# gcloud beta vector-search collections data-objects batch-search  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/data-objects/batch-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta vector-search collections data-objects batch-search Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta vector-search collections data-objects batch-search - batch search data objects from a Vector Search collection 
SYNOPSIS
    

`gcloud beta vector-search collections data-objects batch-search` `--collection`=`COLLECTION` `--location`=`LOCATION` `--searches-from-file`=`SEARCHES_FROM_FILE` [[`--rrf-weights`=[`WEIGHT`,…] : `--combine-output-data-fields`=[`DATA_OUTPUT_FIELD`,…] `--combine-output-metadata-fields`=[`METADATA_OUTPUT_FIELD`,…] `--combine-output-vector-fields`=[`VECTOR_OUTPUT_FIELD`,…] `--combine-top-k`=`COMBINE_TOP_K`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Batch search data objects from a Vector Search collection. Searches can be specified in a JSON file via --searches-from-file. 
EXAMPLES
     To batch search data objects from collection `my-collection` in location `us-central1` using searches defined in `searches.json`, run: 
    
    
    gcloud beta vector-search collections data-objects batch-search --collection=my-collection --location=us-central1 --searches-from-file=searches.json

Example `searches.json`: 
    
    
    [
      {
        "semanticSearch": {
          "searchText": "sci-fi movie",
          "searchField": "vector1",
          "topK": 10
        }
      },
      {
        "vectorSearch": {
          "searchField": "vector2",
          "topK": 5,
          "vector": { "values": [0.1, 0.2, 0.3] }
        }
      }
    ]

To request an optional query-time target recall for a search, include `denseScannParams.targetRecall` (a value in [0, 1]) inside that search's `searchHint.indexHint` in the JSON file: 
    
    
    [
      {
        "vectorSearch": {
          "searchField": "plot_embedding",
          "vector": { "values": [0.1, 0.2, 0.3] },
          "topK": 10,
          "searchHint": {
            "indexHint": {
              "name": "projects/my-project/locations/us-central1/collections/my-collection/indexes/my-index",
              "denseScannParams": { "targetRecall": 0.95 }
            }
          }
        }
      }
    ]

REQUIRED FLAGS
    

`--collection`=`COLLECTION`
     The collection to batch search data objects from. 
`--location`=`LOCATION`
     Location of the collection. 
`--searches-from-file`=`SEARCHES_FROM_FILE`
     Path to a JSON file containing a list of searches. Each element in list should be a JSON object representing a Search message, e.g., `{"semanticSearch": {"searchText": "…", "searchField": "…"}}`. Keys must be camelCase as in API definition. Example file content: 
    
    
    [
      {
        "vectorSearch": {
          "vector": {
            "values": [
              1,
              2,
              3,
              4
            ]
          },
          "searchField": "genre_embedding",
          "topK": 10,
          "outputFields": {
            "dataFields": [
              "director",
              "genre",
              "title",
              "year"
            ]
          }
        }
      },
      {
        "semanticSearch": {
          "searchText": "sci-fi movie",
          "searchField": "plot_embedding",
          "taskType": "SEMANTIC_SIMILARITY",
          "topK": 10
        }
      },
      {
        "textSearch": {
          "searchText": "movie 1",
          "dataFieldNames": ["title"],
          "topK": 10
        }
      }
    ]

OPTIONAL FLAGS
    

Combine Results Options 
Ranker 

This must be specified. 

RRF Ranker 
`--rrf-weights`=[`WEIGHT`,…]
     RRF weights for combining results. 
`--combine-output-data-fields`=[`DATA_OUTPUT_FIELD`,…]
     List of data fields to include in combined output. 
`--combine-output-metadata-fields`=[`METADATA_OUTPUT_FIELD`,…]
     List of metadata fields to include in combined output. 
`--combine-output-vector-fields`=[`VECTOR_OUTPUT_FIELD`,…]
     List of vector fields to include in combined output. 
`--combine-top-k`=`COMBINE_TOP_K`
     Top K results to return when combining results. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud vector-search collections data-objects batch-search](https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/data-objects/batch-search)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
