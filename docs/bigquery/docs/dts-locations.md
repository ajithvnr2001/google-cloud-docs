---
url: https://docs.cloud.google.com/bigquery/docs/dts-locations/
title: Data location and transfers \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:40.157233+00:00
---

# Data location and transfers  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/dts-locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data location and transfers

The BigQuery Data Transfer Service lets you transfer data from external sources into BigQuery regardless of where your source data is stored. Your transfer configuration automatically uses the location of your destination dataset to stage and process data, while certain data warehouse migrations require colocated staging resources. For more information about BigQuery locations, see [Dataset locations](https://docs.cloud.google.com/bigquery/docs/locations). 

## Transfer location

Transfer configurations have locations. When you set up a transfer configuration, set the transfer configuration up in the same project as the destination dataset. The location of the transfer configuration is automatically set to the same location that you specified for the destination dataset. The BigQuery Data Transfer Service processes and stages data in the same location as the destination BigQuery dataset. If you don't have a destination dataset when you create the transfer, you must create one in BigQuery before configuring the transfer.

## Source data location

The source data you want to transfer to BigQuery might have a location. However, the location where your source data is stored and the location of the destination dataset in BigQuery are irrelevant.

## Location considerations for data warehouse migrations

Data warehouse migrations from [Teradata](https://docs.cloud.google.com/bigquery/docs/migration/teradata-overview) require a Cloud Storage bucket as part of the transfer process. The Cloud Storage bucket must be colocated with the BigQuery destination dataset.

Redshift data warehouse migrations do not require a colocated Cloud Storage bucket.

**Key Point:** You can copy a dataset or manually move it to another location. See [Managing datasets](https://docs.cloud.google.com/bigquery/docs/managing-datasets) for details. For more information about using Cloud Storage to store and move large datasets, see [Using Cloud Storage with big data](https://docs.cloud.google.com/storage/docs/working-with-big-data).

## What's next

  * View [all the Google Cloud services available in locations worldwide](https://cloud.google.com/about/locations/#region).
  * [Explore additional location-based concepts](https://docs.cloud.google.com/docs/geography-and-regions), such as zones, that apply to other Google Cloud services.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
