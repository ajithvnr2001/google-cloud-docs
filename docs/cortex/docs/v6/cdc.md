---
url: https://docs.cloud.google.com/cortex/docs/v6/cdc/
title: Change Data Capture (CDC) ingestion processing \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:52.119263+00:00
---

# Change Data Capture (CDC) ingestion processing  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/cdc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Change Data Capture (CDC) ingestion processing 

This page guides you through Change Data Capture (CDC) ingestion within Google Cloud Cortex Framework in BigQuery. BigQuery is designed for efficiently storing and analyzing new data.

## CDC process

When data changes in your source data system (like SAP), BigQuery doesn't modify existing records. Instead, the updated information is added as a new record. To avoid duplicates, a merge operation needs to be applied afterwards. This process is called [Change Data Capture (CDC) ingestion](https://docs.cloud.google.com/bigquery/docs/change-data-capture).

The Data Foundation for SAP includes the option to create scripts for Managed Service for Apache Airflow or Apache Airflow to [merge](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#merge_statement) or `upsert` the new records resulting from updates and only keep the latest version in a new dataset. For these scripts to work the tables need to have some specific fields:

  * `operation_flag`: This flag tells the script whether a record was inserted, updated, or deleted.
  * `recordstamp`: This timestamp helps identify the most recent version of a record. This flag indicates whether the record is: 
    * Inserted (I)
    * Updated (U)
    * Deleted (D)



By utilizing CDC processing, you can ensure that your BigQuery data accurately reflects the latest state of your source system. This eliminates duplicate entries and provides a reliable foundation for your data analysis.

## Dataset structure

For all supported data sources, data from upstream systems are first replicated into a BigQuery dataset (`source` or `replicated dataset`), and the updated or merged results are inserted into another dataset (CDC dataset). The reporting views select data from the CDC dataset, to ensure the reporting tools and applications always have the latest version of a table.

The following flow shows how the CDC processing for SAP, dependent on the `operational_flag` and `recordstamp`.

![CDC processing example for SAP](https://docs.cloud.google.com/cortex/docs/images/cdc-processing.png)

**Figure 1**. CDC processing example for SAP.

The following flow depicts the integration from APIs into Raw data and CDC processing for Salesforce, dependent on the `Id` and `SystemModStamp` fields produced by Salesforce APIs.

![Integration from APIs into Raw data and CDC processing for Salesforce](https://docs.cloud.google.com/cortex/docs/images/cdc-api-integration.png)

**Figure 2**. Integration from APIs into Raw data and CDC processing for Salesforce.

Some replication tools can merge or upsert the records when inserting them into BigQuery, so the generation of these scripts is optional. In this case, the setup only has a single dataset. The reporting dataset fetches updated records for reporting from that dataset.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
