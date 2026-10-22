---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/import-index-data-from-big-query/
title: Import index data from BigQuery \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:46:00.422951+00:00
---

# Import index data from BigQuery  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/import-index-data-from-big-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Import index data from BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide explains how to import index data from BigQuery into Vector Search with the `ImportIndex` API, streamlining the process of populating Vector Search indexes directly from your BigQuery tables that contain vector embeddings.

## Preparing BigQuery data for import

Before importing index data, your BigQuery table must have the following columns:

  * **Unique identifiers** : This column contains unique identifiers for each data point. It is mapped to the `id` field in Vector Search.

  * **Vector embeddings** : This column contains the vector embeddings, represented as a repeated `FLOAT` field. It is mapped to the embedding field in Vector Search.




Optionally, you can include the following columns:

  * **Restricts** : These are columns for string and numeric restricts, which lets you filter your data during searches.

  * **Metadata** : These are columns of metadata to be returned with Vector Search index query results.




## Preparing Vector Search index for import

Once you've prepared your BigQuery data, ensure the destination Vector Search index:

  * **Exists in Vector Search within your project** : This index serves as the destination for your imported data. The index must be created within your project.

  * **Is set to overwrite or append data** : During the import process, you have the option to either overwrite the existing data within your Vector Search index or append the data imported from BigQuery. Overwriting replaces the current data points with the imported data. Appending adds the new data to the existing index.

  * **Matches dimensionality** : The dimensionality of the embeddings stored in your BigQuery data must be identical to the dimensionality configured for your Vector Search index.




## Specifying the `ImportIndexRequest`

Before importing data from BigQuery, create an `ImportIndexRequest` object that specifies the target index, whether to overwrite existing data, and the configuration for connecting to BigQuery. Send this request object to the `ImportIndex` API.

The following is an example of an `ImportIndexRequest` in JSON format:
    
    
    {
      "name": "projects/[PROJECT_ID]/locations/[LOCATION]/indexes/[INDEX_ID]",
      "isCompleteOverwrite": true,
      "config": {
        "bigQuerySourceConfig": {
          "tablePath": "bq://[PROJECT_ID].[DATASET_ID].[TABLE_ID]",
          "datapointFieldMapping": {
            "idColumn": "[ID_COLUMN_NAME]",
            "embeddingColumn": "[EMBEDDING_COLUMN_NAME]",
            "restricts": [
              {
                "namespace": "[RESTRICT_NAMESPACE]",
                "allowColumn": ["[RESTRICT_ALLOW_COLUMN_NAME]"],
                "denyColumn": ["[RESTRICT_DENY_COLUMN_NAME]"]
              }
            ],
            "numericRestricts": [
              {
                "namespace": "[RESTRICT_NAMESPACE]",
                "valueColumn": "[RESTRICT_VALUE_COLUMN_NAME]",
                "valueType": "INT"
              }
            ],
            "metadataColumns": ["METADATA_COLUMN1", "METADATA_COLUMN2", ...]
          }
        }
      }
    }
    

  * **`name`** : The full resource name of the Vector Search index where you want to import the data.

  * **`isCompleteOverwrite`** : A boolean that indicates whether to overwrite existing data in the index. Set to `true` to replace existing data.

  * **`config`** : Contains the configuration for the BigQuery source.

    * **`bigquerySourceConfig`** : Specifies the details for connecting to your BigQuery table.

    * **`tablePath`** : The full path to your BigQuery table in the format `bq://[PROJECT_ID].[DATASET_ID].[TABLE_ID]`.

    * **`datapointFieldMapping`** : Maps the columns in your BigQuery table to the fields in Vector Search.

      * **`idColumn`** : The name of the column containing unique identifiers.

      * **`embeddingColumn`** : The name of the column containing vector embeddings.

      * **`restricts`** : (Optional) Specifies string restricts.

      * **`namespace`** : The namespace for the restrict.

      * **`allowColumn`** : The array containing column name(s) for allowed values for the restrict.

      * **`denyColumn`** : The array containing column name(s) for denied values for the restrict.

      * **`numericRestricts`** : (Optional) Specifies numeric restricts.

      * **`namespace`** : The namespace for the numeric restrict.

      * **`value_column`** : The name of the column containing numeric values.

      * **`value_type`** : The type of the numeric value such as `INT`, `FLOAT`, or `DOUBLE`.

      * **`metadataColumns`** : (Optional) Metadata fields to include with the feature embedding. These metadata fields can be retrieved from the index search results, but they don't affect the search itself. For example, filtering cannot be performed on metadata fields.




## Executing the import

Once you have created an `ImportIndexRequest`, send it to the `ImportIndex` API endpoint. This triggers the import process, which exports data from BigQuery and ingests it into your Vector Search index. `ImportIndex` returns a long-running operation. You can use the operation ID to monitor the progress of the import operation.

After the imported data is stored, it resides within your Vector Search index and is indistinguishable from data ingested using other methods. The index can continue to be managed using standard Vector Search APIs.

The following code sample demonstrates a query result with `return_full_datapoint` set to true and the BigQuery connector configuration that specifies a `genre` restricts, a `year` numeric restricts, and metadata columns `title` and `description`.
    
    
    nearest_neighbors {
      neighbors {
        datapoint {
          datapoint_id: "4"
          feature_vector: 0.7
          feature_vector: 0.8
          restricts {
            namespace: "genre"
            allow_list: "Drama"
          }
          embedding_metadata {
            title: "A Movie"
            description: "The story of A Movie..."
          }
          crowding_tag {
            crowding_attribute: "0"
          }
          numeric_restricts {
            namespace: "year"
            value_int: 1942
          }
        }
        distance: 0.75
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
