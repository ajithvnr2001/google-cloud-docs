---
url: https://docs.cloud.google.com/data-studio/improve-performance/
title: Improve Data Studio performance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:08.559751+00:00
---

# Improve Data Studio performance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/improve-performance/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Improve Data Studio performance Stay organized with collections  Save and categorize content based on your preferences. 

The speed with which a Data Studio report loads and responds to viewer changes, such as applying filters or changing the date range, depends on a number of factors, which include the following:

  * the performance of the underlying dataset
  * the amount of data that is being queried by the visualizations in the report
  * the complexity of those queries
  * network latency



Some of these factors are beyond your (or Data Studio's) ability to control. For example, there may not be much you can do to improve the responsiveness of the underlying data platform or speed up your network connection. There are, however, some things that you can do to fine-tune your report performance in Data Studio.

**Tip:** Performance tuning can involve tradeoffs between speed and responsiveness on one side, and up-to-date data and user customization on the other. The tips offered here may not be appropriate for every customer's use case.

## Adjust the data freshness rate

Most data source types have a data freshness option (the exception to this is extracted data sources). This option lets you balance your need for up-to-date information against report performance and potential query costs or quotas. Each type of data source has its own default data freshness threshold, but you can adjust this threshold as needed. For example, if you are measuring ad performance on your site or app, you might find that daily data updates are sufficient. Reports that are based on social media analytics, on the other hand, may need their data updated multiple times a day.

Learn more about [managing data freshness](https://docs.cloud.google.com/data-studio/manage-data-freshness).

## Use an extracted data source

An extracted data source is a static snapshot of up to 100 MB of data. Once created, data requests from your report go to this snapshot, not to the underlying dataset. Using an extracted data source can make your reports and explorations load faster and be more responsive than when working with a live connection to your data.

Extracted data sources don't have a data freshness option. Instead, you can schedule when you want to the data in the extracted data source to update.

Learn more about [extracting data](https://docs.cloud.google.com/data-studio/extract-data-for-faster-performance).

## Understanding Concurrency and Scaling

Data Studio is designed with a serverless architecture, meaning Data Studio itself does not impose hard limits on the number of concurrent users viewing reports. Performance and scaling are primarily determined by the capacity and responsiveness of the underlying data source(s) your reports connect to.

### Data source specifics

  * **BigQuery** : When using BigQuery, report concurrency and performance depend on factors like BigQuery slot availability, query complexity, data size, and caching. Monitor your BigQuery slot utilization and query performance.

To optimize, consider BigQuery best practices such as partitioning, clustering, and using BI Engine.

  * **Other data sources** : For other connectors (for example, Google Sheets, or third-party databases), concurrency limits are subject to the source system's API rate limits, database connection pools, and overall query processing capability.




### Actionable recommendations

  * **Optimize data source queries** : Ensure your queries are as efficient as possible.
  * **Leverage caching** : Utilize Data Studio's data freshness settings to cache data and reduce direct queries to the source.
  * **Phased rollout** : For very large user bases (for example, thousands of users), consider a phased rollout while monitoring the impact on the underlying data source.
  * **Monitor underlying systems** : Check the performance and quota usage of your data sources (for example, BigQuery slots, or API quotas).



## Improvements for BigQuery data sources

The following sections discuss tips for improving performance on reports that use BigQuery data.

### Accelerate BigQuery data sources with BI Engine

BigQuery BI Engine is a fast, in-memory analysis service. By using BI Engine you can analyze data stored in BigQuery with sub-second query response time and with high concurrency.

BI Engine integrates with Data Studio to accelerate data exploration and analysis. With BI Engine, you can build rich, interactive dashboards and reports in Data Studio without compromising performance, scale, security, or data freshness.

[Get started using Data Studio with BI Engine](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio).

### Use materialized tables for complex queries on large datasets

Connecting Data Studio to a BigQuery view can be slow if that view performs complex calculations or transformations at run-time, especially with large datasets. While views can be useful for restructuring data, they can lead to timeouts in Data Studio if they perform real-time calculations like dynamically generating signed URLs for millions of records.

Instead of using a view that performs heavy processing, materialize the result of the view's query to a table by using one of these options:

  * Use [BigQuery materialized views](https://docs.cloud.google.com/bigquery/docs/materialized-views-intro).
  * Create a table from a query result, and then use [BigQuery scheduled queries](https://docs.cloud.google.com/bigquery/docs/scheduling-queries) to refresh the data in that table periodically.



Then, connect Data Studio to the materialized view or table instead of the standard view. This avoids re-running the complex calculations for every request from Data Studio. For even faster performance on materialized data, use BI Engine.

### Enable the BigQuery Storage Read API

For queries that use paginated results, enabling the [BigQuery Storage Read API](https://docs.cloud.google.com/bigquery/docs/reference/storage) can lead to improved query times. Data Studio automatically uses the Storage Read API when doing so improves query runtimes.

To enable the BigQuery Storage Read API, grant the following permissions to your BigQuery user who is connected to Data Studio:

  * `bigquery.readsessions.create`
  * `bigquery.readsessions.getData`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
