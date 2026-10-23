---
url: https://docs.cloud.google.com/spanner/docs/monitor-columnar-engine/
title: Monitor columnar engine performance \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:00.757766+00:00
---

# Monitor columnar engine performance  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/monitor-columnar-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Monitor columnar engine performance Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is available with the Spanner Enterprise edition and Enterprise Plus edition. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview). 

This page describes how to monitor Spanner's columnar engine. You can monitor using:

  * The query execution plan
  * Storage usage graphs in system insights



## View columnar data in the query plan

  1. Run a query.
  2. View its [query plan](https://docs.cloud.google.com/spanner/docs/query-execution-plans).
  3. In the **Query summary** section of the query execution, check for the **Columnar read share** information.

The following image shows the **Columnar read share** percentage:

![The **Query summary** shows the columnar read share percentage.](https://docs.cloud.google.com/static/spanner/docs/images/columnar-read-share.svg)




This metric shows the percentage of bytes read from columnar storage out of total bytes read from both row-based and columnar storage. A high percentage is optimal, while a low percentage suggests that much of the data remains unconverted to columnar format.

## Columnar data storage metrics

To view columnar data storage metrics:

  1. Go to the **Spanner Instances** page in the Google Cloud console.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  2. Select the instance you want to view metrics for.

  3. Click **System insights**.

  4. In the **Storage usage** section, you can see two new metrics:

**columnar storage - hdd** and **columnar storage - ssd**. These metrics show the columnar representation usage of HDD and SSD. The total storage metrics include both PAX and columnar data. You can see these metrics on storage usage graphs on the **System insights** page. For example:

![The amount of columnar storage ssd.](https://docs.cloud.google.com/static/spanner/docs/images/columnar-storage.svg)




## Query and table operations statistics

`SPANNER_SYS.QUERY_STATS_TOP_*` tables have a column named `AVG_COLUMNAR_READ_SHARE`, which is an average percentage of bytes read from columnar storage out of total bytes read from both row-based and columnar storage. A high percentage is optimal, while a low percentage suggests that much of the data remains unconverted to columnar format.

## What's next

  * Learn about [columnar engine](https://docs.cloud.google.com/spanner/docs/columnar-engine).
  * Learn how to [enable columnar engine](https://docs.cloud.google.com/spanner/docs/configure-columnar-engine).
  * Learn how to [query columnar data](https://docs.cloud.google.com/spanner/docs/query-columnar-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
