---
url: https://docs.cloud.google.com/migration-center/docs/estimate/specify-datawarehouse-requirements/
title: Specify data warehousing requirements \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:19.643205+00:00
---

# Specify data warehousing requirements  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/estimate/specify-datawarehouse-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Specify data warehousing requirements Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to specify your data warehousing requirements for evaluating the cost of running your data analytics and warehousing setup on BigQuery on Google Cloud.

## Before you begin

Complete the steps to [start a cost estimate](https://docs.cloud.google.com/migration-center/docs/estimate/start-estimation).

## Specify data warehousing requirements

  1. On the **Start your estimate** page, in the **Data warehousing** card, click **Start**.

If you have completed estimation for another environment and want to start specifying details in the data warehousing cost calculator, on the results page, click **Start** in the **Data warehousing** card.

  2. To add a warehouse, in the **Warehouses** section, click **Add Warehouse** and perform the following steps:

     1. Enter a warehouse name.

     2. From the **Select edition** list, choose a BigQuery edition for your estimate. To learn about BigQuery editions and the features associated with them, see [Introduction to BigQuery editions](https://docs.cloud.google.com/bigquery/docs/editions-intro).

     3. From the **Region** list, select a region for migrating your data warehouse.

     4. Choose a pricing track. The default pricing track is **3-year commitment**.

     5. From the **Environment** list, choose the environment from which you are migrating.

     6. In the additional fields that appear, provide the required details.

     7. Click **Done** to add the warehouse to your estimate.

  3. Repeat the previous step to add more warehouses to your estimate.

A cost estimate is displayed for each warehouse you add. If you want to view the cost breakdown for the warehouses, click **View details**.

  4. From the currency list, select the currency in which you want to see the estimate. The estimate is generated in US dollars by default.

  5. To review the estimate for your data warehouse migration, click **Submit**.




You can see the data warehouse cost estimate on the results page.

### Specify the migration environment details

The following sections describe how to specify your migration environment details.

#### Teradata

If you are migrating from Teradata, provide the following details:

  1. Select a Teradata generation.

  2. In the **TCore count** field, specify the number of TCores used in your current data warehouse environment. The default value is `0`.

  3. In the **% average usage of TCores** field, specify the average percentage of the total TCores used in your current warehouse. The default value is `75%`.

  4. In the **% sustained usage of TCores** field, specify the percentage of total TCores run in a sustained way for your workloads. The default value is `50%`.

  5. In the **% CPU used for index/stats** field, specify the percentage of total CPUs used for indexing and statistics. The default value is `10%`.

  6. In the **% CPU used for disaster recovery** field, specify the percentage of total CPUs used for disaster recovery.

  7. In the **% CPU for data ingestion and maintenance** field, specify the percentage of total CPUs used for data ingestion and maintenance tasks. The default value is `5%`.

  8. In the **Total compressed storage in Teradata (GB)** field, specify the total compressed storage, in GB, that you're using.

  9. In the **BigQuery storage** section, specify the percentages to reserve for active and long-term storage. The default values are `20%` and `80%` respectively. For more information, see [Storage pricing](https://cloud.google.com/bigquery/pricing#storage).




#### Snowflake

If you are migrating from Snowflake, provide the following details:

  1. In the **Snowflakes credits per month** field, specify the Snowflake credits you consume per month.

  2. In the **% average usage of Snowflakes credits** field, specify the average core utilization percentage of your existing workloads. The default value is `75%`.

  3. In the **% sustained usage of Snowflakes credits** field, specify percentage of your capacity run in a sustained way for your workloads. The default value is `50%`.

  4. Specify the total compressed storage for your cluster in Snowflake, in GB.

  5. In the **BigQuery storage** section, specify the percentages to reserve for active and long-term storage. The default values are `20%` and `80%` respectively. For more information, see [Storage pricing](https://cloud.google.com/bigquery/pricing#storage).




#### Exadata

If you are migrating from Exadata, provide the following details:

  1. From the **Exadata model** list, select your Exadata platform. 
  2. In the **Number of database servers** field, enter the total number of database servers that you have. 
  3. In the **Number of storage servers** field, enter the total number of storage servers that you have. 
  4. In the **% average usage of Exadata servers** field, enter the average core utilization for your existing workloads. The default value is `75%`. 
  5. In the **% sustained usage of average workload** field, enter the minimum system utilization as a percentage of your total system size. You can calculate your sustained usage with the following formula: 

$$ U = \mu{(u)} - \sigma{(u)} $$ 

where $U$ is the sustained usage, $\mu{(u)}$ is the average system utilization, and $\sigma{(u)}$ is the standard deviation of the system utilization. The default value is `50%`. 
  6. In the **Total compressed storage in Exadata** , enter the sum of your active and long-term compressed storage sizes in GB. 
  7. In the **BigQuery storage** section, specify the percentages to reserve for active and long-term storage. The default values are `20%` and `80%`, respectively. For more information, see [Storage pricing](https://cloud.google.com/bigquery/pricing#storage). 



## What's next

  * Learn how to [review and export the estimate results](https://docs.cloud.google.com/migration-center/docs/estimate/review-and-export-results).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
