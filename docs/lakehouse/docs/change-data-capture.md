---
url: https://docs.cloud.google.com/lakehouse/docs/change-data-capture/
title: Change data capture ingestion \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:50.648237+00:00
---

# Change data capture ingestion  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/change-data-capture/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Change data capture ingestion Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Change data capture (CDC) ingestion lets you synchronize your source databases with borderless Lakehouse [Apache Iceberg managed tables (formerly BigLake tables for Apache Iceberg in BigQuery)](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery) in real time. By capturing incremental changes—such as inserts, updates, and deletes—CDC ensures that your lakehouse reflects the most current state of your operational data without requiring full table reloads.

Apache Iceberg managed tables use [BigQuery CDC concepts and capabilities](https://docs.cloud.google.com/bigquery/docs/change-data-capture) to efficiently process these changes and enable low-latency analytics on data stored in open formats like Apache Iceberg. This approach significantly reduces the management overhead associated with typical ETL processes.

## Limitations

Apache Iceberg managed tables support change data capture (CDC) ingestion, and leverage the same concepts and capabilities as standard BigQuery CDC ingestion. However, there are a few additional limitations to be aware of:

  * Out-of-order deletions are not supported. Unlike BigQuery CDC ingestion, a [delete retention window](https://docs.cloud.google.com/bigquery/docs/change-data-capture#deleted_data_considerations) is not maintained for CDC-enabled Iceberg managed tables. If a `DELETE` event arrives before the corresponding record is inserted, the deletion is discarded by the background apply jobs. This can result in out of order records remaining in your table that were intended to be deleted.
  * All limitations under [Apache Iceberg managed tables limitations](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery#limitations).
  * All limitations under [BigQuery CDC ingestion limitations](https://docs.cloud.google.com/bigquery/docs/change-data-capture#limitations).



## What's next

For more information, see the following BigQuery documentation:

  * [Stream data with change data capture](https://docs.cloud.google.com/bigquery/docs/change-data-capture)
  * [Stream data with the BigQuery Storage Write API (gRPC)](https://docs.cloud.google.com/biglake/docs/bigquery-storage-api)
  * [Learn how to use Datastream to replicate transactional databases to BigLake tables](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery#limitations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
