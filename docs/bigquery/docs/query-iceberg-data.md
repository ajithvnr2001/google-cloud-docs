---
url: https://docs.cloud.google.com/bigquery/docs/query-iceberg-data/
title: Query Apache Iceberg external tables \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:51:46.364688+00:00
---

# Query Apache Iceberg external tables  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/query-iceberg-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query Apache Iceberg external tables

This document describes how to query data stored in [Iceberg external tables](https://docs.cloud.google.com/bigquery/docs/iceberg-external-tables).

## Required roles

To query Iceberg external tables, ensure that the caller of the BigQuery API has the following roles:

  * BigQuery Connection User (`roles/bigquery.connectionUser`)
  * BigQuery Data Viewer (`roles/bigquery.dataViewer`)
  * BigQuery User (`roles/bigquery.user`)



The caller can be your account, a [Spark connection service account](https://docs.cloud.google.com/bigquery/docs/connect-to-spark#create-spark-connection), or a [Cloud resource connection service account](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection#create-cloud-resource-connection). Depending on your permissions, you can grant these roles to yourself or ask your administrator to grant them to you. For more information about granting roles, see [Viewing the grantable roles on resources](https://docs.cloud.google.com/iam/docs/viewing-grantable-roles).

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `bigquery.connections.use`
  * `bigquery.jobs.create`
  * `bigquery.readsessions.create` (Only required if you are [reading data with the BigQuery Storage Read API](https://docs.cloud.google.com/bigquery/docs/reference/storage))
  * `bigquery.tables.get`
  * `bigquery.tables.getData`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

## Query Iceberg external tables

After creating an Iceberg external table, you can [query it using GoogleSQL syntax](https://docs.cloud.google.com/bigquery/docs/running-queries), the same as if it were a standard BigQuery table. For example, `SELECT field1, field2 FROM mydataset.my_iceberg_table;`.

## What's next

  * Learn about [using SQL in BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction-sql).
  * Learn about [BigQuery quotas](https://docs.cloud.google.com/bigquery/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
