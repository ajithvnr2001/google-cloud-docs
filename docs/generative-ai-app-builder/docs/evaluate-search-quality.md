---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/evaluate-search-quality/
title: Evaluate search quality \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:28.987507+00:00
---

# Evaluate search quality  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/evaluate-search-quality/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Evaluate search quality Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

As part of your search experience with Agent Search, you can evaluate the quality of your search results for custom search apps using sample query sets.

You can evaluate the performance of custom search apps that contain structured, unstructured, and website data. You cannot evaluate the performance of apps with multiple data stores.

This page explains why, when, and how to evaluate the search quality using the evaluation method.

## Overview

This section describes why and when to perform search quality evaluation. For information on how to perform search quality evaluation, see Process for evaluating search quality.

### Reasons to perform evaluation

Assessment of your search quality provides you metrics that help perform tasks such as the following:

  * At an aggregate-level, gauge your search engine's performance
  * At a query-level, locate patterns to understand potential biases or shortcomings in ranking algorithms
  * Compare historical evaluation results to understand the impact of changes in your search configuration



For a list of metrics, see Understand the results.

### When to perform evaluation

Agent Search extends several search configurations to enhance your search experience. You can perform search quality evaluation after you make the following changes:

  * [Configure serving controls for search](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls)
  * [Tune your search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search)
  * [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings)
  * [Filter search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)
  * [Boost search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results)



You can also run the evaluation tests regularly because the search behavior updates periodically.

## About sample query sets

Sample query sets are used for quality evaluation. The sample query set must adhere to its prescribed format, and it must contain query entries that have the following nested fields:

  * **Queries** : the query whose search results are used to generate the evaluation metrics and determine the search quality. Google recommends using a diverse set of queries that reflects your user's search pattern and behavior.
  * **Targets** : the URI of the document that's expected as a search result of the sample query. To understand the definition of document for structured, unstructured, and website search apps, see [Documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#documents).

When the target documents are compared to the documents retrieved in the search response, performance metrics are generated. Metrics are generated using these two techniques:

    * **Document matching** : the URIs of the target documents are compared with the URIs of the retrieved documents. This determines whether the expected documents are present in the search results. During the comparison, the evaluation API tries to extract the following fields in the following order, and use the first available value to match the target with the retrieved document: 
      * `cdoc_url` in the [`structData`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.struct_data) field of the document definition
      * `uri` in the [`structData`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.struct_data) field of the document definition
      * `link` in the [`derivedStructData`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.derived_struct_data) field of the document definition
      * `url` in the [`derivedStructData`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.derived_struct_data) field of the document definition
    * **Page matching** : when you include page numbers in your sample targets, the evaluation API compares the results at a page-level. This determines whether the pages mentioned in the targets are also cited in the search response. You must enable extractive answers to enable page-level matching. The evaluation API matches the page from the first extractive answer in the search result.



### Purpose of sample query sets

Using the same sample query set for all your search quality evaluations for a given data store ensures a consistent and reliable way to measure the search quality results. This also establishes a fair and repeatable system.

The results from each evaluation are compared to target results for each sample query to calculate different metrics, such as recall, precision, and normalized discounted cumulative gain (NDCG). These quantitative metrics are used to rank the results from different search configurations.

### Quotas and limits

The following limit applies to the sample query sets:

  * Each sample query set can contain a maximum of 20,000 queries.



The following quota applies to the sample query sets:

  * You can create a maximum of 100 sample query sets per project and 500 sample query sets per organization.



For more information, see [Quotas and limits](https://docs.cloud.google.com/generative-ai-app-builder/quotas).

### Sample query set format

The query set must conform to the following schema when constructed in JSON format. The query set can contain multiple query entries with one query in each query entry. When presented in newline delimited JSON (NDJSON) format, each query entry must be on a new line.

#### Import from BigQuery and Cloud Storage

The following section provides the sample query set templates for importing from from BigQuery and Cloud Storage.

### Unstructured data

Use the following template to draft a sample query file in JSON format to evaluate unstructured data with metadata.
    
    
    {
      "queryEntry": {
        "query": "SAMPLE_QUERY",
        "targets": [
          {
            "uri": "gs://PATH/TO/CLOUD/STORAGE/LOCATION_1.docx"
          },
          {
            "uri": "gs://PATH/TO/CLOUD/STORAGE/LOCATION_2.pdf",
            "pageNumbers": [
            PAGE_NUMBER_1,
            PAGE_NUMBER_2
            ]
          },
          {
            "uri": "CDOC_URL"
          }
        ]
      }
    }
    

Replace the following:

  * `SAMPLE_QUERY`: the query used to test evaluate the search quality
  * `PATH/TO/CLOUD/STORAGE/LOCATION`: the path to the Cloud Storage location where the expected result resides. This is the value of the `link` field in the [`derivedStructData`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.derived_struct_data) field of the document definition.
  * `PAGE_NUMBER_1`: an optional field to indicate the page numbers in the PDF file where the expected response for the query is located. This is useful when the file has multiple pages.
  * `CDOC_URL`: an optional field to indicate the custom document ID `cdoc_url` field in the document metadata in the Agent Search data store schema. 



### Structured data

Use the following template to draft a sample query file in JSON format to evaluate structured data from BigQuery.
    
    
    {
      "queryEntry": {
        "query": "SAMPLE_QUERY",
        "targets": [
          {
            "uri": "CDOC_URL"
          }
        ]
      }
    }
    

Replace the following:

  * `SAMPLE_QUERY`: the query used to test evaluate the search quality
  * `CDOC_URL`: a required field to indicate the custom `cdoc_url` field for the structured data field in the Agent Search data store schema.



### Website data

Use the following template to draft a sample query file in JSON format to evaluate website content.
    
    
    {
      "queryEntry": {
        "query": "SAMPLE_QUERY",
        "targets": [
          {
            "uri": "WEBSITE_URL"
          }
        ]
      }
    }
    

Replace the following:

  * `SAMPLE_QUERY`: the query used to test evaluate the search quality
  * `WEBSITE_URL`: the target website for the query.



Here's an example of a sample query set in JSON and NDJSON formats:

### JSON
    
    
    [
      {
        "queryEntry": {
          "query": "2018 Q4 Google revenue",
          "targets": [
            {
              "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2018Q4_alphabet_earnings_release.pdf"
            },
            {
              "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/201802024_alphabet_10K.pdf"
            }
          ]
        }
      },
      {
        "queryEntry": {
          "query": "2019 Q4 Google revenue",
          "targets": [
            {
              "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2019Q4_alphabet_earnings_release.pdf"
            }
          ]
        }
      }
    ]
    

### NDJSON
    
    
    {"queryEntry":{"query":"2018 Q4 Google revenue","targets":[{"uri":"gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2018Q4_alphabet_earnings_release.pdf"},{"uri":"gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/201802024_alphabet_10K.pdf"}]}}
    {"queryEntry":{"query":"2019 Q4 Google revenue","targets":[{"uri":"gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2019Q4_alphabet_earnings_release.pdf"}]}}
    

#### Import from local file system

The following section provides the sample query set templates for importing from the local file system.

### Unstructured data

Use the following template to draft a sample query file in JSON format to evaluate unstructured data with metadata.
    
    
    {
      "inlineSource": {
        "sampleQueries": [
          {
            "queryEntry": {
              "query": "SAMPLE_QUERY",
              "targets": [
                {
                  "uri": "gs://PATH/TO/CLOUD/STORAGE/LOCATION_1.docx"
                },
                {
                  "uri": "gs://PATH/TO/CLOUD/STORAGE/LOCATION_2.pdf",
                  "pageNumbers": [
                    PAGE_NUMBER_1,
                    PAGE_NUMBER_2
                  ]
                },
                {
                  "uri": "CDOC_URL"
                }
              ]
            }
          }
        ]
      }
    }
    

Replace the following:

  * `SAMPLE_QUERY`: the query used to test evaluate the search quality
  * `PATH/TO/CLOUD/STORAGE/LOCATION`: the path to the Cloud Storage location where the unstructured data file to be queried resides. This is the value of the `link` field in the [`derivedStructData`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.derived_struct_data) field of the document definition.
  * `PAGE_NUMBER_1`: an optional field to indicate the page numbers where the required response for the query can be located in the PDF file. This is useful if the file has multiple pages.
  * `CDOC_URL`: an optional field to indicate the custom document ID `cdoc_url` field in the document metadata in the Agent Search data store schema. 



### Structured data

Use the following template to draft a sample query file in JSON format to evaluate structured data from BigQuery.
    
    
    {
      "inlineSource": {
        "sampleQueries": [
          {
            "queryEntry": {
              "query": "SAMPLE_QUERY",
              "targets": [
                {
                  "uri": "CDOC_URL"
                }
              ]
            }
          }
        ]
      }
    }
    

Replace the following:

  * `SAMPLE_QUERY`: the query used to test evaluate the search quality
  * `CDOC_URL`: a required field to indicate the custom `cdoc_url` field for the structured data field in the Agent Search data store schema.



### Website data

Use the following template to draft a sample query file in JSON format to evaluate website content.
    
    
    {
      "inlineSource": {
        "sampleQueries": [
          {
            "queryEntry": {
              "query": "SAMPLE_QUERY",
              "targets": [
                {
                  "uri": "WEBSITE_URL"
                }
              ]
            }
          }
        ]
      }
    }
    

Replace the following:

  * `SAMPLE_QUERY`: the query used to test evaluate the search quality
  * `WEBSITE_URL`: the target website for the query.



Here's an example of a sample query set:

### JSON
    
    
    {
      "inlineSource": {
        "sampleQueries": [
          {
            "queryEntry": {
              "query": "2018 Q4 Google revenue",
              "targets": [
                {
                  "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2018Q4_alphabet_earnings_release.pdf"
                },
                {
                  "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/201802024_alphabet_10K.pdf"
                }
              ]
            }
          },
          {
            "queryEntry": {
              "query": "2019 Q4 Google revenue",
              "targets": [
                {
                  "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2019Q4_alphabet_earnings_release.pdf"
                }
              ]
            }
          }
        ]
      }
    }
    

## Process for evaluating search quality

The process of search quality evaluation is as follows:

  1. Create a sample query set.
  2. Import sample query that conforms to the prescribed JSON format.
  3. Run search quality evaluation.
  4. Understand the results.



The following sections give the instructions to perform these steps using REST API methods.

### Before you begin

  * The following limit applies: 
    * At a given time, you can only have a single active evaluation per project.
  * The following quota applies: 
    * You can initiate a maximum of five evaluation requests per day per project. For more information, see [Quotas and limits](https://docs.cloud.google.com/generative-ai-app-builder/quotas).
  * To get page-level metrics, you must enable [extractive answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-answers).



### Create a sample query set

You can create a sample query set and use it to evaluate the quality of the search responses for a given data store. To create a sample query set, do the following.

### REST

The following sample shows how to create the sample query set using the [`sampleQuerySets.create`](https://docs.cloud.google.com/generative-ai-app-builder/docs) method.

  1. Create the sample query set.
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             -H "X-Goog-User-Project: PROJECT_ID" \
             "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/sampleQuerySets?sampleQuerySetId=SAMPLE_QUERY_SET_ID" \
             -d '{
           "displayName": "SAMPLE_QUERY_SET_DISPLAY_NAME"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `SAMPLE_QUERY_SET_ID`: a custom ID for your sample query set.
     * `SAMPLE_QUERY_SET_DISPLAY_NAME`: a custom name for your sample query set.

#### Response

You should receive a JSON response similar to the following:
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID",
      "displayName": "SAMPLE_QUERY_SET_DISPLAY_NAME",
      "createTime": "CREATION_DATETIME"
    }
    




### Import sample query data

After creating the sample query set, import the sample query data. To import the sample query data, you can do any of the following:

  * Import from Cloud Storage: import an NDJSON file from a Cloud Storage location.
  * Import from BigQuery: import BigQuery data from a BigQuery table. To create the BigQuery table from your NDJSON file, see [Loading JSON data from Cloud Storage](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-json).
  * Import from your local file system: create the sample query set in your local file system and import it.



### Cloud Storage

  1. Create the sample query sets that conform to the sample query set format.

  2. Import the JSON file containing the sample query set from a Cloud Storage location using the `sampleQueries.import` method.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/sampleQueries:import" \
         -d '{
           "gcsSource": {
             "inputUris": ["INPUT_FILE_PATH"],
           },
           "errorConfig": {
             "gcsPrefix": "ERROR_DIRECTORY"
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `SAMPLE_QUERY_SET_ID`: the custom ID for your sample query set that you defined during sample query set creation.
     * `INPUT_FILE_PATH`: the path to the Cloud Storage location for your sample query set.
     * `ERROR_DIRECTORY`: an optional field to specify the path to the Cloud Storage location where error files are logged when import errors occur. Google recommends leaving this empty or removing the `errorConfig` field so that Agent Search can automatically create a temporary location.

#### Response

You should receive a JSON response similar to the following. Note the value of `OPERATION_ID`. You need this value in the next step to poll the status of this long-running operation (LRO).
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSampleQueriesMetadata"
      }
    }
    

  3. Get the status of the long-running operation (LRO) using the `operations.get` method. 
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/operations/OPERATION_ID"
         

#### Response

You should receive a JSON response similar to the following. If there are errors and the import failed, the response shows a `failureCount` field to indicate the number of sample queries that failed to import.
         
         {
          "name": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/operations/OPERATION_ID",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSampleQueriesMetadata",
            "createTime": "CREATE_TIME",
            "updateTime": "UPDATE_TIME",
            "successCount": "SUCCESS_COUNT",
            "totalCount": "TOTAL_COUNT"
          },
          "done": true,
          "response": {
            "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSampleQueriesResponse",
            "errorConfig": {
              "gcsPrefix": "gs://PROJECT_NUMBER_us_import/ERROR_CONFIG_FOLDER"
            }
          }
         }
         




### BigQuery

  1. Create the sample query sets that conform to the sample query set format.

  2. Import the JSON file containing the sample query set from a BigQuery location using the `sampleQueries.import` method.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/sampleQueries:import" \
         -d '{
           "bigquerySource": {
             "projectId": "PROJECT_ID",
             "datasetId":"DATASET_ID",
             "tableId": "TABLE_ID"
           },
           "errorConfig": {
             "gcsPrefix": "ERROR_DIRECTORY"
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `SAMPLE_QUERY_SET_ID`: the custom ID for your sample query set that you defined during sample query set creation.
     * `DATASET_ID`: the ID of the BigQuery dataset that contains the sample query set.
     * `TABLE_ID`: the ID of your BigQuery table that contains the sample query set.
     * `ERROR_DIRECTORY`: an optional field to specify the path to the Cloud Storage location where error files are logged when import errors occur. Google recommends leaving this empty or removing the `errorConfig` field so that Agent Search can automatically create a temporary location.

#### Response

You should receive a JSON response similar to the following. Note the value of `OPERATION_ID`. You need this value in the next step to poll the status of this long-running operation (LRO).
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSampleQueriesMetadata"
      }
    }
    

  3. Get the status of the long-running operation (LRO) using the `operations.get` method. 
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/operations/OPERATION_ID"
         

#### Response

You should receive a JSON response similar to the following. If there are errors and the import failed, the response shows a failureCount field to indicate the number of sample queries that failed to import.
         
         {
          "name": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/operations/OPERATION_ID",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSampleQueriesMetadata",
            "createTime": "CREATE_TIME",
            "updateTime": "UPDATE_TIME",
            "successCount": "SUCCESS_COUNT",
            "totalCount": "TOTAL_COUNT"
          },
          "done": true,
          "response": {
            "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSampleQueriesResponse",
            "errorConfig": {
              "gcsPrefix": "gs://PROJECT_ID_us_import/ERROR_CONFIG_FOLDER"
            }
          }
         }
         




### Local file system

  1. Create the sample query sets that conform to the sample query set format.

  2. Import the JSON file containing the sample query set from a local file system location using the `sampleQueries.import` method.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/sampleQueries:import" \
         --data @PATH/TO/LOCAL/FILE.json
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `SAMPLE_QUERY_SET_ID`: the custom ID for your sample query set that you defined during sample query set creation.
     * `PATH/TO/LOCAL/FILE.json`: the path to the JSON file that contains the sample query set. 

#### Response

You should receive a JSON response similar to the following. Note the value of `OPERATION_ID`. You need this value in the next step to poll the status of this long-running operation (LRO).
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSampleQueriesMetadata"
      }
    }
    

  3. Get the status of the long-running operation (LRO) using the `operations.get` method. 
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/operations/OPERATION_ID"
         

#### Response

You should receive a JSON response similar to the following. If there are errors and the import failed, the response shows a failureCount field to indicate the number of sample queries that failed to import. 
         
         {
          "name": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/operations/OPERATION_ID",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSampleQueriesMetadata",
            "createTime": "CREATE_TIME",
            "updateTime": "UPDATE_TIME",
            "successCount": "SUCCESS_COUNT",
            "totalCount": "TOTAL_COUNT"
          },
          "done": true,
          "response": {
            "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSampleQueriesResponse",
            "errorConfig": {
              "gcsPrefix": "gs://PROJECT_ID_us_import/ERROR_CONFIG_FOLDER"
            }
          }
         }
         




### Run search quality evaluation

After importing the sample query data into the sample query sets, follow these steps to run the search quality evaluation.

### REST

  1. Initiate a search quality evaluation.

**Note:** You can evaluate the search performance of an app and you can evaluate the search performance of a data store. For the following procedure, Google recommends evaluating search performance of the app.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/evaluations" \
         -d '{
          "evaluationSpec": {
            "querySetSpec": {
              "sampleQuerySet": "projects/PROJECT_ID/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID"
            },
            "searchRequest": {
              "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search"
            }
          }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `SAMPLE_QUERY_SET_ID`: the custom ID for your sample query set that you defined during sample query set creation.
     * `APP_ID`: the ID of the Agent Search app whose search quality you want to evaluate.

#### Response

You should receive a JSON response similar to the following. Note the value of `EVALUATION_ID`. You need this value in the next step to poll the status of the evaluation, which is a long-running operation (LRO).
    
    {
     "name": "projects/PROJECT_NUMBER/locations/global/operations/OPERATION_ID",
     "done": true,
     "response": {
       "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.Evaluation",
       "name": "projects/PROJECT_NUMBER/locations/global/evaluations/EVALUATION_ID",
       "evaluationSpec": {
         "querySetSpec": {
           "sampleQuerySet": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID"
         },
         "searchRequest": {
           "servingConfig": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search"
         }
       },
       "state": "PENDING"
     }
    }
    

  2. Monitor progress of the evaluation.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/evaluations/EVALUATION_ID"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `EVALUATION_ID`: the ID for your evaluation job that was returned in the previous step when you initiated the evaluation.

#### Response

You should receive a JSON response similar to the following. The status of the evaluation is shown as `PENDING` until the evaluation is complete.
    
    {
    "name": "projects/PROJECT_NUMBER/locations/global/evaluations/EVALUATION_ID",
    "evaluationSpec": {
      "querySetSpec": {
        "sampleQuerySet": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID"
      },
      "searchRequest": {
        "servingConfig": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search"
      }
    },
    "state": "PENDING"
    "createTime": "CREATION_DATETIME"
    }
    

  3. Retrieve the aggregate results.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/evaluations/EVALUATION_ID"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `EVALUATION_ID`: the ID for your evaluation job that was returned in the previous step when you initiated the evaluation.

#### Response

You should receive a JSON response similar to the following. The status of the evaluation is shown as `PENDING` until the evaluation is complete.
    
    {
     "name": "projects/PROJECT_NUMBER/locations/global/evaluations/EVALUATION_ID",
     "evaluationSpec": {
       "querySetSpec": {
         "sampleQuerySet": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID"
       },
       "searchRequest": {
         "servingConfig": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search"
       }
     },
     "qualityMetrics": {
       "docRecall": {
         "top1": DOC_RECALL_TOP_1,
         "top3": DOC_RECALL_TOP_3,
         "top5": DOC_RECALL_TOP_5,
         "top10": DOC_RECALL_TOP_10
       },
       "docPrecision": {
         "top1": DOC_PRECISION_TOP_1,
         "top3": DOC_PRECISION_TOP_3,
         "top5": DOC_PRECISION_TOP_5,
         "top10": DOC_PRECISION_TOP_10
       },
       "docNdcg": {
         "top1": DOC_NDCG_TOP_1,
         "top3": DOC_NDCG_TOP_3,
         "top5": DOC_NDCG_TOP_5,
         "top10": DOC_NDCG_TOP_10
       },
       "pageRecall": {
         "top1": PAGE_RECALL_TOP_1,
         "top3": PAGE_RECALL_TOP_3,
         "top5": PAGE_RECALL_TOP_5,
         "top10": PAGE_RECALL_TOP_10
       },
       "pageNdcg": {
         "top1": PAGE_NDCG_TOP_1,
         "top3": PAGE_NDCG_TOP_3,
         "top5": PAGE_NDCG_TOP_5,
         "top10": PAGE_NDCG_TOP_10
        }
      },
     "state": "SUCCEEDED",
     "error": {},
     "createTime": "CREATION_DATETIME",
     "endTime": "END_DATETIME"
    }
    

  4. Retrieve query-level results.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/evaluations/EVALUATION_ID:listResults"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `EVALUATION_ID`: the ID for your evaluation job that was returned in the previous step when you initiated the evaluation.

#### Response

You should receive a JSON response similar to the following. The status of the evaluation is shown as `PENDING` until the evaluation is complete.
    
    {
     "evaluationResults": [
       {
         "sampleQuery": {
           "name": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/sampleQueries/QUERY_ID_1",
           "queryEntry": {
             "query": "SAMPLE_QUERY_1",
             "targets": [
               {
                 "uri": "URI_1"
               }
             ]
           }
         },
         "qualityMetrics": {
           "docRecall": {
             "top1": DOC_RECALL_TOP_1,
             "top3": DOC_RECALL_TOP_3,
             "top5": DOC_RECALL_TOP_5,
             "top10": DOC_RECALL_TOP_10
           },
           "docPrecision": {
             "top1": DOC_PRECISION_TOP_1,
             "top3": DOC_PRECISION_TOP_3,
             "top5": DOC_PRECISION_TOP_5,
             "top10": DOC_PRECISION_TOP_10
           },
           "docNdcg": {
             "top1": DOC_NDCG_TOP_1,
             "top3": DOC_NDCG_TOP_3,
             "top5": DOC_NDCG_TOP_5,
             "top10": DOC_NDCG_TOP_10
           },
           "pageRecall": {
             "top1": PAGE_RECALL_TOP_1,
             "top3": PAGE_RECALL_TOP_3,
             "top5": PAGE_RECALL_TOP_5,
             "top10": PAGE_RECALL_TOP_10
           },
           "pageNdcg": {
             "top1": PAGE_NDCG_TOP_1,
             "top3": PAGE_NDCG_TOP_3,
             "top5": PAGE_NDCG_TOP_5,
             "top10": PAGE_NDCG_TOP_10
            }
          }
       },
       {
         "sampleQuery": {
           "name": "projects/PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/sampleQueries/QUERY_ID_2",
           "queryEntry": {
             "query": "SAMPLE_QUERY_2",
             "targets": [
               {
                 "uri": "URI_2"
               }
             ]
           }
         },
         "qualityMetrics": {
           "docRecall": {
             "top1": DOC_RECALL_TOP_1,
             "top3": DOC_RECALL_TOP_3,
             "top5": DOC_RECALL_TOP_5,
             "top10": DOC_RECALL_TOP_10
           },
           "docPrecision": {
             "top1": DOC_PRECISION_TOP_1,
             "top3": DOC_PRECISION_TOP_3,
             "top5": DOC_PRECISION_TOP_5,
             "top10": DOC_PRECISION_TOP_10
           },
           "docNdcg": {
             "top1": DOC_NDCG_TOP_1,
             "top3": DOC_NDCG_TOP_3,
             "top5": DOC_NDCG_TOP_5,
             "top10": DOC_NDCG_TOP_10
           },
           "pageRecall": {
             "top1": PAGE_RECALL_TOP_1,
             "top3": PAGE_RECALL_TOP_3,
             "top5": PAGE_RECALL_TOP_5,
             "top10": PAGE_RECALL_TOP_10
           },
           "pageNdcg": {
             "top1": PAGE_NDCG_TOP_1,
             "top3": PAGE_NDCG_TOP_3,
             "top5": PAGE_NDCG_TOP_5,
             "top10": PAGE_NDCG_TOP_10
            }
          }
       }
     ]
    }
    




### Understand the results

The following table describes the metrics that are returned in your evaluation results.

Name | Description | Requirements   
---|---|---  
`docRecall` | Recall per document, at various top-k cutoff levels. Recall is the fraction of relevant documents retrieved out of all relevant documents. For example, `top5` value signifies the following: For a single query, if 3 out of 5 relevant documents are retrieved in the top-5, the `docRecall` can be calculated as 3/5 or 0.6. | The sample query must contain the URI field.  
`pageRecall` | Recall per page, at various top-k cutoff levels. Recall is the fraction of relevant pages retrieved out of all relevant pages. For example, `top5` value signifies the following: For a single query, if 3 out of 5 relevant pages are retrieved in the top-5, the `pageRecall` can be calculated as 3/5 = 0.6 | 

  * The sample query must contain the URI and pages fields.
  * Extractive answers must be enabled.

  
`docNdcg` | Normalized discounted cumulative gain (NDCG) per document, at various top-k cutoff levels. NDCG measures the ranking quality, giving higher relevance to top results. The NDCG value can be calculated for each query according to [Normalized DCG](https://en.wikipedia.org/wiki/Discounted_cumulative_gain#Normalized_DCG). | The sample query must contain the URI field.  
`pageNdcg` | Normalized discounted cumulative gain (NDCG) per page, at various top-k cutoff levels. NDCG measures the ranking quality, giving higher relevance to top results. The NDCG value can be calculated for each query according to [Normalized DCG](https://en.wikipedia.org/wiki/Discounted_cumulative_gain#Normalized_DCG). | 

  * The sample query must contain the URI and pages fields.
  * Extractive answers must be enabled.

  
`docPrecision` | Precision per document, at various top-k cutoff levels. Precision is the fraction of retrieved documents that are relevant. For example, `top3` value signifies the following: For a single query, if 4 out of 5 retrieved documents in the top-5 are relevant, the `docPrecision` value can be calculated as 4/5 or 0.8. | The sample query must contain the URI field.  
  
Based on the values of these supported metrics, you can perform the following tasks:

  * Analyze aggregated metrics: 
    * Examine overall metrics like average recall, precision, and normalized discounted cumulative gain (NDCG). These metrics provide a high-level view of your search engine's performance.
  * Review query-level results: 
    * Drill down into individual queries to identify specific areas where the search engine performs well or poorly.
    * Look for patterns in the results to understand potential biases or shortcomings in the ranking algorithms.
  * Compare results over time: 
    * Run evaluations regularly to track changes in search quality over time.
    * Use historical data to identify trends and assess the impact of any changes you make to your search engine.



## What's next

  * Use Cloud Scheduler to set up scheduled quality evaluation. For more information, see [Use authentication with HTTP targets](https://docs.cloud.google.com/scheduler/docs/http-target-auth).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
