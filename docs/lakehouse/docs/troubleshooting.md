---
url: https://docs.cloud.google.com/lakehouse/docs/troubleshooting/
title: Troubleshoot common borderless Lakehouse issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:51.644059+00:00
---

# Troubleshoot common borderless Lakehouse issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/troubleshooting/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Troubleshoot common borderless Lakehouse issues Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve common issues with _borderless Lakehouse_ and its associated resources.

## Cannot query metadata tables

This issue occurs when you query metadata tables, such as `.snapshots` or `.files`, for your Apache Iceberg tables supported by the Lakehouse runtime catalog in BigQuery using a five-part name identifier.

To resolve this issue, query these tables using Apache Spark.

## metadata.json file size limit

The Apache Iceberg `metadata.json` file size is limited to 1 MB. This limit applies to the metadata file that tracks table snapshots, schemas, and partition specs. If your metadata file exceeds this size, you might encounter errors when performing table operations through the Apache Iceberg REST catalog endpoint.

To resolve this issue, request a limit increase by contacting your Google account team.

## `NOT_FOUND` errors when querying multi-region catalogs

This issue occurs when you create a catalog in the _Lakehouse runtime catalog_ using a multi-region Cloud Storage bucket without specifying a primary location, and then attempt to query the catalog by specifying a BigQuery virtual region (such as `US` or `EU`).

When a catalog is created with a multi-region bucket, its metadata is stored in specific regional locations within the geographic scope of the multi-region rather than in the corresponding BigQuery virtual region. If you force a query to run in a virtual region where the metadata is not present, the query fails with a `NOT_FOUND` error.

To resolve this issue, specify the primary location (for example, `US` or `EU`) when you create the catalog. For more information, see [Specify primary regions for US and EU multi-regions](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#specify-primary-regions-for-us-and-eu-multi-regions).

**Note:** If you have already created a catalog using a multi-region bucket and want to use it with the BigQuery multi-regions (`US` or `EU`), you must delete and recreate the catalog to specify the primary location.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
