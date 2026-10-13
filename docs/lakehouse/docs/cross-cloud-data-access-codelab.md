---
url: https://docs.cloud.google.com/lakehouse/docs/cross-cloud-data-access-codelab/
title: Set up cross-cloud data access \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:29.354066+00:00
---

# Set up cross-cloud data access  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/cross-cloud-data-access-codelab/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Set up cross-cloud data access Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, send an email to [biglake-help@google.com](mailto:biglake-help@google.com).

Learn how to set up cross-cloud data access to unify data silos across Amazon Web Services (AWS), Google Cloud, and [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview) without complex ETL.

You use [borderless Lakehouse](https://docs.cloud.google.com/lakehouse/docs/introduction) as the central intelligence hub, AlloyDB as an operational data source, and [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs/overview) for high-performance vectorized processing. Finally, you use Gemini to derive powerful business insights from your lakehouse.

## Scenario

In this scenario, you have data across the following sources:

  * Transactional data (users, orders, order items) in an operational AlloyDB database.
  * Product data in an AWS S3 bucket.
  * Clickstream event logs in Cloud Storage.



You join these datasets to identify target demographics for your next marketing campaign and generate personalized outreach emails.

## What you learn

In this codelab, you perform the following tasks:

  * Set up and configure Lakehouse catalog endpoints to unify data silos across AWS S3, Cloud Storage, and AlloyDB.
  * Run high-performance vectorized query processing using Managed Service for Apache Spark.
  * Join transactional, product, and clickstream datasets without data movement or complex ETL pipelines.
  * Use Gemini to derive business insights and generate personalized marketing outreach from your lakehouse.



## Take the codelab

Launch the step-by-step codelab:

[Start the borderless Lakehouse codelab](https://codelabs.developers.google.com/next26/multicloud-lakehouse)

## What's next

  * Learn more about [Lakehouse concepts](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access).
  * Learn how to [query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).
  * Check [supported regions and capabilities](https://docs.cloud.google.com/lakehouse/docs/regions-capabilities-cross-cloud-connections).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
