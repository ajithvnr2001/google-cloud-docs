---
url: https://docs.cloud.google.com/bigtable/docs/synchronize-with-bigquery-dataframes/
title: Synchronize online and offline datasets with BigQuery DataFrames \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:18.772977+00:00
---

# Synchronize online and offline datasets with BigQuery DataFrames  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/synchronize-with-bigquery-dataframes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Synchronize online and offline datasets with BigQuery DataFrames

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Using Bigtable with BigQuery, you can build a _real-time analytics database_ and use it in machine learning (ML) pipelines. This lets you keep your data in sync, supporting data manipulation and model development (offline access) and low-latency application serving (online access).

To build your real-time analytics database, you can use [BigQuery DataFrames](https://docs.cloud.google.com/bigquery/docs/bigquery-dataframes-introduction), a set of open-source Python libraries for BigQuery data processing. BigQuery DataFrames lets you develop and train models in BigQuery and automatically replicate a copy of the latest data values used for your ML models in Bigtable for online serving.

This document provides an overview of using the `bigframes.streaming API` to create BigQuery jobs that automatically replicate and synchronize datasets across BigQuery and Bigtable. Before you read this document, make sure that you understand the following documents:

  * [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)
  * [BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction)
  * [Build a real-time analytics database with Bigtable and BigQuery](https://docs.cloud.google.com/solutions/real-time-analytics-for-databases)



## BigQuery DataFrames

BigQuery DataFrames helps you develop and train models in BigQuery and automatically replicate a copy of the latest data values used for your ML models in Bigtable for online serving. It lets you do the following:

  * Develop data transformations in a Pandas-compatible interface (`bigframes.pandas`) directly against BigQuery data
  * Train models using a scikit-learn-like API (`bigframes.ML`)
  * Synchronize the data needed for low-latency inference with Bigtable (`bigframes.streaming`) to support user-facing applications

**Note:** If you want to batch export from BigQuery to Bigtable using SQL, you can set up a reverse extract-load-transform (ETL). For more information, see [Export data to Bigtable (Reverse ETL)](https://docs.cloud.google.com/bigquery/docs/export-to-bigtable).

## BigFrames StreamingDataFrame

`bigframes.streaming.StreamingDataFrame` is a DataFrame type in the BigQuery DataFrames package. It lets you create a `StreamingDataFrame` object that can be used to generate a continuously running job that streams data from a designated BigQuery table into Bigtable for online serving. This is done by generating [ BigQuery continuous queries](https://docs.cloud.google.com/bigquery/docs/continuous-queries-introduction).

A `BigFrames StreamingDataFrame` can do the following:

  * Create a `StreamingDataFrame` from a designated BigQuery table
  * Optionally, perform additional Pandas operations like select, filter, and preview the content
  * Create and manage streaming jobs to Bigtable



## Required roles

To get the permissions that you need to use BigQuery DataFrames in a BigQuery notebook, ask your administrator to grant you the following IAM roles:

  * [BigQuery User (`roles/bigquery.user`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.user)

  * [Notebook Runtime User (`roles/aiplatform.notebookRuntimeUser`)](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.notebookRuntimeUser)

  * [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator)




To get the permissions that you need to write data to a Bigtable table, ask your administrator to grant you the following IAM roles:

  * [Bigtable User (roles/bigtable.user)](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.user)



## Get started

BigQuery DataFrames is an open-source package. To install the latest version, run `pip install --upgrade bigframes`.

To create your first `BigFrames StreamingDataFrame` and synchronize data between BigQuery and Bigtable, run following code snippet. For the complete code sample, see the GitHub notebook [BigFrames StreamingDataFrame](https://github.com/googleapis/python-bigquery-dataframes/blob/main/notebooks/streaming/streaming_dataframe.ipynb).
    
    
      import bigframes.streaming as bst
    
      bigframes.options._bigquery_options.project = "PROJECT"
    
      sdf = bst.read_gbq_table("birds.penguins_bigtable_streaming")
    
      job = sdf.to_bigtable(instance="BIGTABLE_INSTANCE",
    
        table="TABLE",
    
        app_profile=None,
    
        truncate=True,
    
        overwrite=True,`
    
        auto_create_column_families=True,
    
        bigtable_options={},
    
        job_id=None,
    
        job_id_prefix= "test_streaming_",)
    
      print(job.running())
    
      print(job.error_result)
    

Replace the following:

  * PROJECT: the ID of your Google Cloud project
  * BIGTABLE_INSTANCE: the ID of the Bigtable instance that contains the table you are writing to
  * TABLE: the ID of the Bigtable table that you are writing to



Once the job is initialized, it runs as a continuous query in BigQuery and streams any data changes to Bigtable.

## Costs

There are no additional charges for using the BigQuery BigFrames API, but you are charged for the underlying resources used for continuous queries, Bigtable, and BigQuery.

Continuous queries use [BigQuery capacity compute pricing](https://cloud.google.com/bigquery/pricing#capacity_compute_analysis_pricing), which is measured in [slots](https://docs.cloud.google.com/bigquery/docs/slots). To run continuous queries, you must have a [reservation](https://docs.cloud.google.com/bigquery/docs/reservations-workload-management) that uses the [Enterprise or Enterprise Plus edition](https://docs.cloud.google.com/bigquery/docs/editions-intro) and a [reservation assignment](https://docs.cloud.google.com/bigquery/docs/reservations-intro#assignments) that uses the `CONTINUOUS` job type.

Usage of other BigQuery resources, such as data ingestion and storage, are charged at the rates shown in [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

Usage of Bigtable services that receive continuous query results are charged at the [Bigtable pricing](https://cloud.google.com/bigtable/pricing) rates.

## Limitations

All [feature](https://docs.cloud.google.com/bigquery/docs/continuous-queries-introduction#limitations) and [location](https://docs.cloud.google.com/bigquery/docs/continuous-queries-introduction#locations) limitations associated with continuous queries are also applicable for streaming DataFrames.

## What's next

  * [Getting started with Feast on Google Cloud](https://cloud.google.com/blog/products/databases/getting-started-with-feast-on-google-cloud)
  * [Streamlining ML Development with Feast](https://cloud.google.com/blog/products/databases/how-feast-feature-store-streamlines-ml-development)
  * [Query Bigtable data stored in an external table.](https://docs.cloud.google.com/bigquery/docs/external-data-bigtable)
  * [Export data from BigQuery to Bigtable.](https://docs.cloud.google.com/bigquery/docs/export-to-bigtable)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
