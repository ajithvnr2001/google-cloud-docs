---
url: https://docs.cloud.google.com/composer/docs/composer-3/cleanup-airflow-database/
title: Clean up the Airflow database \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:51.528784+00:00
---

# Clean up the Airflow database  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/cleanup-airflow-database/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Clean up the Airflow database Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/cleanup-airflow-database "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/cleanup-airflow-database "View this page for Managed Airflow \(Legacy Gen 1\)")

This page explains how to maintain the Airflow database in your environment.

## Automatic database cleanup with a database retention policy

You can configure automatic database cleanup for your Managed Airflow (Gen 3) environment by setting a database retention policy. After you set up this policy, records older than a certain period are automatically removed from the Airflow database daily. For more information, see [Configure database retention policy](https://docs.cloud.google.com/composer/docs/composer-3/configure-db-retention).

## Deprecated cleanup procedures

**Deprecated:** The **maintenance DAG approach is obsolete** in Managed Airflow (Gen 3). If you still use the database maintenance DAG, we recommend to remove or pause it and configure a [database retention policy](https://docs.cloud.google.com/composer/docs/composer-3/configure-db-retention) instead.

Before the database retention policy became available in Managed Airflow, we recommended a different approach for automating the database cleanup, through a [database cleanup DAG](https://docs.cloud.google.com/composer/docs/composer-2/cleanup-airflow-database). This approach is obsolete in Managed Airflow (Gen 3). This DAG does redundant work and you can reduce the resource consumption by removing it and replacing it with a [database retention policy](https://docs.cloud.google.com/composer/docs/composer-3/configure-db-retention).

## Limits for database size

As the time goes, the Airflow database of your environment stores more and more data. This data includes information and logs related to past DAG runs, tasks, and other Airflow operations.

  * If the Airflow database size is more than 20 GB, then you can't upgrade your environment to a later version.

  * If the Airflow database size is more than 20 GB, it is not possible to create snapshots.




## Maintain database performance

  * Airflow database performance issues can lead to overall DAG execution issues. [Observe Database CPU and memory usage](https://docs.cloud.google.com/composer/docs/composer-3/use-monitoring-dashboard#db-statistics) statistics. If CPU and memory utilization approaches the limits, then the database is overloaded and requires scaling. The amount of resources available to the Airflow database is controlled by the environment size property of your environment. To scale the database up [change the environment size](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments) to a larger tier. Increasing the environment size increases the costs of your environment. 

  * If you use the XCom mechanism to transfer files, make sure that you [use it according to Airflow's guidelines](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html#object-storage-xcom-backend). Transferring big files or a large number of files using XCom impacts Airflow database's performance and can lead to failures when loading snapshots or upgrading your environment. Consider using alternatives such as Cloud Storage to transfer large volumes of data.




## Remove entries for unused DAGs

You can remove database entries for unused DAGs by [removing DAGs from the Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags#delete-md).

## What's next

  * [Configure database retention policy](https://docs.cloud.google.com/composer/docs/composer-3/configure-db-retention)
  * [Access Airflow command-line interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
