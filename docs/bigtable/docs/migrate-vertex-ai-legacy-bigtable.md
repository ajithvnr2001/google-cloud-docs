---
url: https://docs.cloud.google.com/bigtable/docs/migrate-vertex-ai-legacy-bigtable/
title: Migrate from Vertex AI Feature Store (Legacy) to Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:15.989555+00:00
---

# Migrate from Vertex AI Feature Store (Legacy) to Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/migrate-vertex-ai-legacy-bigtable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate from Vertex AI Feature Store (Legacy) to Bigtable

Migrating a machine learning feature management workload from [Vertex AI Feature Store (Legacy)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/overview) to Bigtable can result in improved performance and flexibility. This guide provides an overview of related concepts and the migration process.

Vertex AI Feature Store (Legacy) is a managed environment that uses Bigtable for its online serving layer. Running your AI platform or feature store directly on Bigtable without using Vertex AI Feature Store (Legacy) can result in faster speeds and reduced costs.

We recommend a minimal viable migration path focused on migrating data from the underlying Bigtable tables in Vertex AI Feature Store (Legacy) to a Bigtable instance that you create in your Google Cloud project.

## Benefits of migration

Migration to Bigtable offers several strategic and operational advantages:

  * **Cost efficiency** : You eliminate the Vertex AI Feature Store (Legacy) specific node management premium, often reducing infrastructure costs.
  * **Direct control** : You gain full access to Bigtable capabilities. Bigtable monitoring exposes many more metrics than Vertex AI Feature Store (Legacy). You also have greater control over custom architecture layouts and scaling.
  * **High performance** : Bigtable supports [high-performance workloads](https://docs.cloud.google.com/bigtable/docs/performance) and high-performance features such as [aggregation on writes](https://docs.cloud.google.com/bigtable/docs/aggregates) and [vector search](https://docs.cloud.google.com/bigtable/docs/find-k-nearest-neighbors).
  * **Cross-product integration** : You get access to Bigtable integrations such as [BigQuery external tables](https://docs.cloud.google.com/bigtable/docs/BigQuery-analysis), connectors for [Apache Spark](https://docs.cloud.google.com/bigtable/docs/use-bigtable-spark-connector), [Apache Flink](https://docs.cloud.google.com/bigtable/docs/flink-connector), and [Kafka Connect](https://docs.cloud.google.com/bigtable/docs/kafka-sink-connector), and [reverse ETL from BigQuery](https://docs.cloud.google.com/bigquery/docs/export-to-bigtable).

  * **Change data capture** : You can enable [change streams](https://docs.cloud.google.com/bigtable/docs/change-streams-overview) to capture changes to your Bigtable feature store table as the changes happen.




## Key concepts

This section describes how core Vertex AI Feature Store (Legacy) concepts are implemented by Bigtable and BigQuery.

### Data retention

In Bigtable, you manage data retention with garbage collection. _Garbage collection_ is the automatic, ongoing process of removing expired and obsolete data from Bigtable tables. A _garbage collection policy_ is a set of rules you create that state when data in a specific feature, defined in Bigtable as a _column family_ , is no longer needed. Garbage collection policies are set based on the timestamp associated with the data or the number of versions you want to keep.

Garbage collection is a built-in, asynchronous background process that takes place during [compaction](https://docs.cloud.google.com/bigtable/docs/overview#compactions). Garbage collection occurs on a fixed schedule. Until data is deleted, it appears in read results, but you can filter your reads to exclude this data. For more information, see [Garbage collection overview](https://docs.cloud.google.com/bigtable/docs/garbage-collection).

Additionally, [Bigtable tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) can be a cost-effective solution for online feature stores that need to retain historical data for model training or regulatory compliance. Tiered storage manages the movement of infrequently accessed data from online serving on SSD storage to a lower-cost storage tier.

### Feature development

In Bigtable, you can implement online feature development with Bigtable SQL, and you can implement offline feature development using BigQuery DataFrames.

When you use Vertex AI Feature Store (Legacy), you work with developer APIs and data models that map to underlying data sources prepared in BigQuery. You then register these data sources and specific feature columns in the feature registry. With a Bigtable feature store, you work directly with data in the underlying BigQuery and Bigtable instances, without needing to map to the Vertex AI Feature Store (Legacy) data model.

### Online feature development

For online feature development, Bigtable offers several tools:

  * **Python client library** : Use the [Python client library for Bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest) to work directly with data in Bigtable.
  * **GoogleSQL** : Use [GoogleSQL](https://docs.cloud.google.com/bigtable/docs/googlesql-overview) to read and transform data in Bigtable. You can execute SQL queries directly in the Bigtable console or [from the Python client library](https://docs.cloud.google.com/bigtable/docs/googlesql-overview#client-libraries).
  * **Continuous materialized views** : For creating near real-time features that require recurring transformations and aggregations, use Bigtable [continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) to incrementally run a SQL query against data as it comes into Bigtable.



### Offline feature development

For offline feature development, [BigQuery DataFrames](https://docs.cloud.google.com/bigquery/docs/bigquery-dataframes-introduction) provides a Python interface with more than 750 pandas and scikit-learn APIs. These APIs are implemented through SQL conversion to BigQuery and BigQuery ML APIs. BigQuery DataFrames feature generation allows for both built-in and user-defined Python functions. It also provides automated data synchronization to Bigtable for serving features created in batch and offline processes, described in the next section.

### Online and offline feature synchronization

When using Bigtable directly for ML workloads, you can ensure that an offline feature value is imported from BigQuery and that same value is reused for both training and serving, keeping code paths in sync for generating features between training and serving. The following technologies enable feature synchronization:

  * **Batch synchronization** : [Reverse ETL from BigQuery to Bigtable](https://cloud.google.com/blog/products/databases/using-reverse-etl-between-bigtable-and-bigquery) provides the ability to export the results of a BigQuery query into Bigtable. These queries are run in batch and can be [scheduled directly from BigQuery](https://docs.cloud.google.com/bigquery/docs/scheduling-queries).
  * **Streaming synchronization** : BigQuery [continuous queries](https://docs.cloud.google.com/bigquery/docs/continuous-queries-introduction) are SQL statements that continuously run and output rows into a Bigtable table.
  * **Synchronization from BigQuery DataFrames** : To capture offline features developed in Python, you can use a [BigFrames StreamingDataFrame](https://docs.cloud.google.com/bigtable/docs/synchronize-with-bigquery-dataframes) to generate a BigQuery continuous query that captures your Python logic for feature generation and synchronizes the data results with Bigtable.
  * **Offline feature development directly on Bigtable data** : You can build offline features in BigQuery against data stored in Bigtable by using a [BigQuery external table](https://docs.cloud.google.com/bigtable/docs/BigQuery-analysis). An external table mirrors the look of a BigQuery table and offers most of the same functionality such as joins, scheduled queries, and advanced BigQuery SQL functions without the need to move data back into BigQuery storage. To avoid impacting your application-serving traffic, you can use Data Boost serverless compute when you read Bigtable data with BigQuery external tables. Using Data Boost is especially cost-effective for ad hoc queries. To use Data Boost, specify a Data Boost app profile when you create the external table definition. For more information about Data Boost, see [ Bigtable Data Boost overview](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).



After migration, you can continue using [Vertex AI Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview) to track the quality of your models.

The practice of using Bigtable and BigQuery together is a common pattern for building [real-time analytics databases](https://cloud.google.com/solutions/real-time-analytics-for-databases).

## Migration phases

To ensure service continuity, migration is typically executed in the following distinct phases.

### Phase 1: Prepare the infrastructure

Before beginning your migration, set up the destination environment:

  * [Create a Bigtable instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) in your project to serve as the new online store.
  * [Create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets) and [table](https://docs.cloud.google.com/bigquery/docs/tables) to temporarily store the data that you export from Vertex AI Feature Store (Legacy).
  * Configure IAM: Ensure that the account performing the migration has permissions to read from the legacy feature store and write to the new Bigtable instance. For more information, see [ Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control) and [Control access to Vertex AI Feature Store (Legacy) resources](https://docs.cloud.google.com/vertex-ai/docs/featurestore/resource-policy).



### Phase 2: Define your schema mapping between Vertex AI Feature Store (Legacy) and Bigtable

  1. Review and understand [Bigtable schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design). A general mapping of the Vertex AI Feature Store (Legacy) API to the Bigtable API is the following:

Vertex AI Feature Store (Legacy) resource | Bigtable component  
---|---  
`FeatureOnlineStore` | Bigtable instance  
`FeatureView` | Column family  
`featureValues` (batch) | Column (single cell per key)  
`featureValues` (continuous) | Column (multiple cells per key [versioning])  
  2. After you've defined your schema mapping, [create a Bigtable table](https://docs.cloud.google.com/bigtable/docs/managing-tables) that has a column family for each feature in the source feature store.




### Phase 3: Data extraction and synchronization

In this phase, you migrate data using a tiered approach based on the update frequency of the data.

#### Real-time feature synchronization

For features that you are writing with `write_feature_values` or equivalent API calls, begin writing the same data to the new Bigtable table.

  1. Install the [Python client library for Bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).
  2. Configure your application to simultaneously write feature data to Vertex AI Feature Store (Legacy) and Bigtable. For more information about writing data to Bigtable, see [Writes](https://docs.cloud.google.com/bigtable/docs/writes).



#### Batch feature migration

Next, migrate the data that was stored before you began dual writes. This involves moving the data from Vertex AI Feature Store (Legacy) to BigQuery and then to Bigtable.

  1. Export feature store data to BigQuery using Vertex AI Feature Store (Legacy) [exporting capabilities](https://docs.cloud.google.com/vertex-ai/docs/featurestore/export-features), which let you export all values or snapshots. This lets BigQuery serve as the Vertex AI Feature Store (Legacy) offline store.
  2. Migrate the historical data from BigQuery to Bigtable using one of the following: 
     * [Reverse ETL](https://docs.cloud.google.com/bigquery/docs/export-to-bigtable)
     * [Bigtable Spark connector](https://docs.cloud.google.com/bigtable/docs/use-bigtable-spark-connector)
     * [BigQuery to Bigtable Dataflow template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-bigtable)



### Phase 4: Application and SDK transition

The final step is cutting over the application layer.

  1. After the migration has been completed and tested, stop writing to Vertex AI Feature Store (Legacy).
  2. Modify your application to use only the Python client library for Bigtable.

The following example demonstrates using Python to pull a single feature from Bigtable.
         
         from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
         from google.cloud.bigtable import row_filters
         # Replace 'project_id' and 'instance_id' with your actual IDs.
         client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id)
         instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
         
         #return only the latest feature
         row_filter = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).row_filters.CellsColumnLimitFilter(1)
         
         # Replace 'user1' and 'feature0` with your actual row key and column qualifier.
         
         print("Getting a single feature by row key.")
         key = "user1".encode()
         
         row = table.read_row(key, row_filter)
         cell = row.[cells](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row.PartialRowData.html#google_cloud_bigtable_row_PartialRowData_cells)[column_family_id.decode("utf-8")][feature0][0]
         print(cell.value.decode("utf-8"))
         

For another example of how to read and write data using the Bigtable data and admin APIs, see the [Python hello world](https://docs.cloud.google.com/bigtable/docs/samples-python-hello).

The Python client library for Bigtable also lets you use GoogleSQL to return features that meet your filter criteria or to perform transformations of the features. The following example shows how to call a SQL query asynchronously from the Bigtable Python client library. For additional information on GoogleSQL for Bigtable, see [Additional SQL examples](https://docs.cloud.google.com/bigtable/docs/googlesql-examples).
         
         import asyncio
         from google.cloud.bigtable.data_async import BigtableDataClient
         from google.cloud.bigtable_v2.types import ExecuteQueryRequest
         
         async def run_bigtable_sql_query(project_id, instance_id, table_id):
             """
             Runs a GoogleSQL query on a Bigtable table using the async client.
             """
             client = BigtableDataClient(project_id=project_id)
             instance = client.instance(instance_id)
             table = instance.table(table_id)
         
             # Example query: Select a specific row and all columns from a column family
             # Replace 'my_table' and 'my_cf' with your actual table and column family IDs.
             # The table name in the SQL must be in the format `dataset.table`,
             # where dataset is the instance ID and table is the table ID (in backticks).
             sql_query = f"SELECT _key, my_cf FROM `{instance_id}`.`{table_id}` WHERE _key = 'user_123'"
         
             print(f"Executing query: {sql_query}")
         
             # The client library automatically handles the SQL execution
             try:
                 # The query method returns an AsyncPartialRowsIterator
                 results_iterator = await table.query(query=sql_query)
         
                 async for row in results_iterator:
                     print(f"Row key: {row.row_key.decode('utf-8')}")
                     # Iterate through the cells in the row
                     for col_family, cells in row.cells.items():
                         for cell in cells:
                             print(f"  Column Family: {col_family}, Qualifier: {cell.qualifier.decode('utf-8')}, Value: {cell.value.decode('utf-8')}, Timestamp: {cell.timestamp_micros}")
         
             except Exception as e:
                 print(f"An error occurred: {e}")
             finally:
                 await client.close()
         
         if __name__ == "__main__":
             # TODO(developer): Replace with your project, instance, and table IDs
             your_project_id = "your-gcp-project-id"
             your_instance_id = "your-bigtable-instance-id"
             your_table_id = "your-bigtable-table-id"
         
             # Run the asynchronous function
             asyncio.run(run_bigtable_sql_query(your_project_id, your_instance_id, your_table_id))
         

  3. Begin using Bigtable metrics to monitor latency and throughput. For more information, see [Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).




## Best practices

After you move from Vertex AI Feature Store (Legacy) to a Bigtable feature store implementation, you need to replicate the internal preprocessing and optimization logic that was previously handled by the service to maintain stability and performance.

### Client-side adaptive throttling

The Vertex AI Feature Store (Legacy) backend utilizes a client-side adaptive throttler to protect its underlying Bigtable instances from being overloaded during spikes in traffic or when the storage backend is experiencing high latency or errors. We recommend that you implement a similar throttler in your application code to register backend responses and proactively throttle requests when needed.

### Request partitioning and batch size optimization

Bigtable row filters have a hard limit of 20 KB. Requesting too many features or entity IDs in a single filtered read can cause requests to fail. To mirror the behavior of Vertex AI Feature Store (Legacy), do the following:

  * **Chunk feature IDs** : Limit the number of feature IDs per Bigtable read to approximately 100.
  * **Balance entity batches** : To prevent saturating client or server resources when performing multi-entity reads, take the following precautions: 
    * Partition entities into small concurrent batches, such as 10 entities per batch.
    * Limit the maximum number of concurrent batch requests, such as 10-20.



### Intelligent filter selection

Calculating and applying column filters on the server side adds overhead. If your application typically requests nearly all features in a column family, such as >99.9%, it's more efficient to skip the column filter and read the full row, filtering the results client-side.

### Concurrency and asynchronous execution

To minimize time-to-first-result in streaming scenarios, use asynchronous patterns or thread bundles to fetch entity batches in parallel. This ensures that the application can begin processing results as soon as the first batch returns, rather than waiting for a large serial read to complete.

## What's next

  * For assistance with high-throughput workloads or architectural guidance, contact your account representative.
  * Read about [Feast's Bigtable integration](https://cloud.google.com/blog/products/databases/how-feast-feature-store-streamlines-ml-development).
  * Learn how [Credit Karma scaled to 60 billion model predictions a day using Bigtable and BigQuery](https://cloud.google.com/blog/products/databases/meet-our-data-champions-scott-wong).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
