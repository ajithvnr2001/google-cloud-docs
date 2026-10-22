---
url: https://docs.cloud.google.com/data-studio/bigquery-performance/
title: Optimize BigQuery data source performance \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:45.535268+00:00
---

# Optimize BigQuery data source performance  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/bigquery-performance/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Optimize BigQuery data source performance Stay organized with collections  Save and categorize content based on your preferences. 

You can optimize the performance of reports based on BigQuery data by using the following techniques. These techniques can help your visualizations render more quickly while minimizing BigQuery costs.

## Improve performance with the BigQuery Storage Read API

For queries that use paginated results, enabling the [BigQuery Storage Read API](https://docs.cloud.google.com/bigquery/docs/reference/storage) can lead to improved query times. Data Studio automatically uses the Storage Read API when doing so improves query runtimes.

To enable the BigQuery Storage Read API, grant the following permissions to your BigQuery user who is connected to Data Studio:

  * `bigquery.readsessions.create`
  * `bigquery.readsessions.getData`



## Accelerate reports with BigQuery BI Engine

**BigQuery BI Engine** is a fast, high-concurrency, in-memory analysis service built into BigQuery. By configuring BI Engine with Data Studio, your visualizations render in sub-second time while reducing query concurrency costs ([Learn more about the BigQuery BI Engine](https://cloud.google.com/bigquery/docs/bi-engine-intro)).

### Requirements to use BI Engine with Data Studio

To accelerate your Data Studio reports by using BI Engine, verify the following prerequisites:

  1. **Data storage:** You store reporting data in standard BigQuery tables or views.
  2. **Billing project:** You designate a valid BigQuery billing project that has active Google Cloud billing enabled.
  3. **API enablement:** You enable the BigQuery API (`bigquery.googleapis.com`) in your project.
  4. **Capacity reservation:** You have configured an active BI Engine capacity reservation (`SIZE_IN_GB`) for the project where queries execute.



For detailed performance benchmarks and table optimization guides for BI Engine, see [Analyze BigQuery data with Data Studio](https://cloud.google.com/bigquery/docs/visualize-looker-studio).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
