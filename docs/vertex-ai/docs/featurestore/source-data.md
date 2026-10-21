---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/source-data/
title: Source data requirements \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:47:56.026837+00:00
---

# Source data requirements  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/source-data/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Source data requirements Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

For batch import, Vertex AI Feature Store (Legacy) can import data from tables in BigQuery or files in Cloud Storage.

  * Use BigQuery table if you need to import the entire dataset and don't require partition filters.

  * Use BigQuery view if you need to import a specific subset of the dataset. This option is more time-efficient and lets you import specific selections from the entire dataset, including multiple tables generated from the data.

  * Data contained in files imported from Cloud Storage must be in AVRO or CSV format.




For streaming import, you provide the feature values to import in the API request. These source data requirements don't apply. For more information, see the [writeFeatureValues API reference](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.featurestores.entityTypes/writeFeatureValues).

Each item (or row) must adhere to the following requirements:

  * You must have a column for entity IDs, and the values must be of type `STRING`. This column contains the entity IDs that the feature values are for.

  * Your source data value types must match the value types of the destination feature in the featurestore. For example, boolean values must be import into a feature that is of type `BOOL`.

  * All columns must have a header that are of type `STRING`. There are no restrictions on the name of the headers.

    * For BigQuery tables and BigQuery views, the column header is the column name.
    * For AVRO, the column header is defined by the AVRO schema that is associated with the binary data.
    * For CSV files, the column header is the first row.
  * If you provide a column for feature generation timestamps, use one of the following timestamp formats:

    * For BigQuery tables and BigQuery views, timestamps must be in the TIMESTAMP column.
    * For Avro, timestamps must be of type long and logical type timestamp-micros.
    * For CSV files, timestamps must be in the RFC 3339 format.
  * CSV files cannot include array data types. Use Avro or BigQuery instead.

  * For array types, you cannot include a null value in the array. Though, you can include an empty array.




## Feature value timestamps

For batch import, Vertex AI Feature Store (Legacy) requires user-provided timestamps for the imported feature values. You can specify a particular timestamp for each value or specify the same timestamp for all values:

  * If the timestamps for feature values are different, specify the timestamps in a column in your source data. Each row must have its own timestamp indicating when the feature value was generated. In your import request, you specify the column name to identify the timestamp column.
  * If the timestamp for all feature values is the same, you can specify it as a parameter in your import request. You can also specify the timestamp in a column in your source data, where each row has the same timestamp.



## Data source region

If your source data is in either BigQuery or Cloud Storage, the source dataset or bucket must be in the same region or in the same multi-regional location as your featurestore. For example, a featurestore in `us-central1` can import data only from Cloud Storage buckets or BigQuery datasets that are in `us-central1` or in the US multi-region location. You can't import data from, for example, `us-east1`. Also, source data from dual-region buckets is not supported.

## What's next

  * Learn about [setting up your project](https://docs.cloud.google.com/vertex-ai/docs/featurestore/setup) to use Vertex AI Feature Store (Legacy).
  * Learn how to [batch import feature values](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
