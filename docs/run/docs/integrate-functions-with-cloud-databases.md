---
url: https://docs.cloud.google.com/run/docs/integrate-functions-with-cloud-databases/
title: Integrate with Cloud databases \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:18.904818+00:00
---

# Integrate with Cloud databases  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/integrate-functions-with-cloud-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Integrate with Cloud databases Stay organized with collections  Save and categorize content based on your preferences. 

You can write functions that integrate with Cloud databases by importing the appropriate Cloud Client Libraries for your chosen database into your source code. To deploy and trigger the function, you can use either:

  * Cloud Run functions (Recommended)
  * The Cloud Functions gcloud CLI



This page provides more information for learning about connecting with a Cloud database using Cloud Run.

## Connect to Cloud SQL

Learn how to add database functionality to your Cloud Run with Cloud SQL:

  * For connecting to a MySQL instance from a service running in Cloud Run, see [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run).
  * For connecting to a PostgreSQL instance from a service running in Cloud Run, see [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run).
  * For connecting to a SQL Server instance from a service running in Cloud Run, see [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/sqlserver/connect-run).



## Connect to Cloud BigQuery

Learn how to write an HTTP Cloud Run function that submits a query to BigQuery.

For details, see [Create a Cloud Run function that returns BigQuery results](https://docs.cloud.google.com/run/docs/tutorials/function-returns-bigquery-query).

## Connect to Memorystore for Redis

Learn about how to connect your Cloud Run functions to a Memorystore for Redis in-memory database.

For details, see [Connecting to a Redis instance from Cloud Run functions](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-functions) in the Memorystore documentation.

## User Spanner with Cloud Run functions

Learn about how to write, deploy, and trigger an HTTP Cloud Function that accesses Spanner.

For details, see [Create a Cloud Run function that returns Spanner results](https://docs.cloud.google.com/run/docs/tutorials/function-sends-query-to-spanner-database).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
