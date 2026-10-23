---
url: https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer-intro/
title: Introduction to Facebook Ads data transfers \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:31.087549+00:00
---

# Introduction to Facebook Ads data transfers  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to Facebook Ads data transfers

You can load data from Facebook Ads to BigQuery using the [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) for Facebook Ads connector. With BigQuery Data Transfer Service, you can schedule recurring transfer jobs that add your latest data from your Facebook Ads to BigQuery.

The BigQuery Data Transfer Service for the Facebook Ads connector supports the following options for your data transfer.

Data transfer options | Support  
---|---  
Supported reports |  The BigQuery Data Transfer Service for Facebook Ads supports the transfer of the following Facebook Ads reports: 

  * `AdAccounts`
  * `AdInsights`
  * `AdInsightsActions`
  * `AdInsightsMMM`  
**Note:** Support for this report is temporarily disabled. For more information, see [July 06, 2026](https://docs.cloud.google.com/bigquery/docs/transfer-changes#Jul06-fb-ads)
  * `Ads`
  * `AdCreatives`
  * `AdSets`
  * `Campaigns`
  * `AdImages`
  * `AdLabels`
  * `Businesses`
  * `CustomAudiences`

For information about how Facebook Ads reports are transformed into BigQuery tables and views, see [Facebook Ads report transformation](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transformation).  
Repeat frequency | The Facebook Ads connector supports daily data transfers.  
  
By default, data transfers are scheduled at the time when the data transfer is created. You can configure the time of data transfer when you [set up your data transfer](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer#fb_ads_transfer_setup).  
Refresh window | The Facebook Ads connector retrieves Facebook Ads data from up to 30 days at the time the data transfer is run. You cannot configure the refresh window for this connector.   
  
For more information, see [Refresh windows](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer-intro#refresh).  
Backfill data availability | [Run a data backfill](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer) to retrieve data outside of your scheduled data transfer. You can retrieve data as far back as the data retention policy on your data source allows.  
  
To learn how to schedule a Facebook Ads transfer, see [Load Facebook Ads data into BigQuery](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer).

## Data ingestion from Facebook Ads transfers

When you transfer data from Facebook Ads into BigQuery, the data is loaded into BigQuery tables that are partitioned by date. The table partition that the data is loaded into corresponds to the date from the data source. If you schedule multiple transfers for the same date, BigQuery Data Transfer Service overwrites the partition for that specific date with the latest data. Multiple transfers in the same day or running backfills don't result in duplicate data, and partitions for other dates are not affected. 

Some ingestion behaviors differ between different Facebook Ads reports:

  * For `AdAccounts`, `AdCreatives`, `AdImages`, `AdLabels`, `Businesses`, and `CustomAudiences` tables, snapshots are taken once a day and stored in the partition of the last transfer run date.

  * Data transfers for the `AdInsights`, `AdInsightsActions`, `Ads`, `AdSets` and `Campaigns` tables will transfer Facebook Ads data that corresponds to the run date of the transfer. For these tables, if you specify an `insightsTimeIncrement` value that is more than 1, then the data transfer includes data from a number of days before the run date according to the `insightsTimeIncrement` value, including the run date. For example, if the `insightsTimeIncrement` value is 3, then the data transfer only includes data from the run date and data from 2 days before the run date, for a total of 3 days of data.

  * For `AdInsights` and `AdInsightsActions` tables, the table partition that the data is loaded into corresponds to the date from the data source.

  * The refresh window only applies to the `AdInsights` and `AdInsightsActions` tables.




### Refresh windows

A _refresh window_ is the number of days that a data transfer retrieves data when a data transfer occurs. For example, if the refresh window is three days and a daily transfer occurs, the BigQuery Data Transfer Service retrieves all data from your source table from the past three days. In this example, when a daily transfer occurs, the BigQuery Data Transfer Service creates a new BigQuery destination table partition with a copy of your source table data from the current day, then automatically triggers backfill runs to update the BigQuery destination table partitions with your source table data from the past two days. The automatically triggered backfill runs will either overwrite or incrementally update your BigQuery destination table, depending on whether or not incremental updates are supported in the BigQuery Data Transfer Service connector.

When you run a data transfer for the first time, the data transfer retrieves all source data available within the refresh window. For example, if the refresh window is three days and you run the data transfer for the first time, the BigQuery Data Transfer Service retrieves all source data within three days.

To retrieve data outside the refresh window, such as historical data, or to recover data from any transfer outages or gaps, you can initiate or schedule a [backfill run](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer).

## Pricing

For pricing information about Facebook Ads transfers, see [Data Transfer Service pricing](https://docs.cloud.google.com/bigquery/pricing#data-transfer-service-pricing).

## What's next

  * Learn about [scheduling a Facebook Ads transfer](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer).
  * Learn more about the [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
