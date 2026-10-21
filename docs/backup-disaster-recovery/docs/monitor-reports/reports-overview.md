---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/reports-overview/
title: Reporting system overview \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:59.935999+00:00
---

# Reporting system overview  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/reports-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Reporting system overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the Backup and DR reporting system and how to get started using it.

Backup and DR provides a comprehensive set of reporting capabilities to help you analyze your backups and recovery operations.

These reporting capabilities give you insight into your Backup and DR activities to identify trends and make informed decisions to optimize your data protection strategy.

Backup and DR integrates with Cloud Monitoring, Cloud Logging, and BigQuery services and provides the following benefits:

  * With BigQuery, you can do the following:

    * **View prebuilt reports.**

Access a library of prebuilt reports that offer insight into various backup and restore aspects, including backup and restore jobs, backup compliance, and resource usage.

    * **Create custom reports using SQL query language.**

Write your own custom reports using SQL query language based on prebuilt reports or dataset tables.

    * **Automate data refresh, email reports, and use tools to analyze data.**

You can automate the data refresh process to ensure reports are always based on the latest data. Additionally, it provides a range of tools for data analysis and insights.

  * With Cloud Monitoring and Cloud Logging, you can do the following:

    * **Discover, view, and analyze trends.**

Interactive dashboards and visualizations let you discover and visualize trends in your data to identify patterns and anomalies. You can explore data from different perspectives and learn more about specific areas of interest.

    * **Set up custom alerts on reporting data.**

Set up custom alerts to notify you when specific conditions are met in the reporting data. This proactive approach helps you to identify potential issues and address them promptly.




## Get started

You can do the following:

  * [Set up prebuilt reports in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery)
  * [View prebuilt reports in Data Studio](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio)
  * [Create custom reports in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#custom-queries)
  * [View metric dashboards in Cloud Monitoring](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/metrics)
  * [Analyze job logs in Cloud Logging](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/job-logs)
  * [Set up event related alerts in Cloud Logging](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts)



If you are an existing Backup and DR customer and using a report manager, see [Frequently asked questions](https://docs.cloud.google.com/backup-disaster-recovery/docs/faq#reports).

## Pricing

The following section summarizes the pricing information for Cloud Logging, Cloud Monitoring, and BigQuery. You can use the free data usage allotments to get started.

  * Backup and DR metrics in Cloud Monitoring.

    * [Backup and DR metrics](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/metrics#metrics) are all [non-chargeable Google Cloud metrics](https://cloud.google.com/stackdriver/pricing#metrics-non-chargeable). Monitoring these metrics in Cloud Monitoring doesn't have associated charges.
    * User-defined metrics are chargeable. For pricing details, see [Chargeable metrics](https://cloud.google.com/stackdriver/pricing#metrics-chargeable).
    * For detailed pricing information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-costs).
  * Backup and DR logs in Cloud Logging.

    * Cloud Logging is priced based on the logs storage volume and logs retention period.
    * There is no charge for storing up to 50 GiB per project per month of logs.
    * Logs retained for the [default retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) don't incur a retention cost. Since Backup and DR reporting logs are routed and stored in BigQuery, it is recommended to retain logs only in BigQuery beyond the default retention period.
    * There are no charges for forwarding logs received through the Cloud Logging API to a supported destination.
    * For detailed pricing information, see [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary).
  * Backup and DR reports in BigQuery.

    * In BigQuery, there are three main pricing components associated with the Backup and DR reports:

      * [Compute pricing](https://cloud.google.com/bigquery/pricing#analysis_pricing_models): This refers to the cost incurred for processing queries, such as SQL queries, user-defined functions, scripts, and specific data manipulation language (DML) and data definition language (DDL) statements.

The free tier includes 1 TiB of query data processed per month. For query data exceeding 1 TiB, you are charged $6.25 per TiB.

      * [Storage pricing](https://cloud.google.com/bigquery/pricing#storage): This refers to the cost incurred for storing data that is loaded into BigQuery.

The first 10 GiB of storage per month doesn't have associated charges.

The first 10 GiB of storage per month doesn't have associated charges. For storage exceeding 10 GiB per month, you are charged $0.01 to $0.04 per GiB depending on the type of storage selected.

      * [Data ingestion pricing](https://cloud.google.com/bigquery/pricing#data_ingestion_pricing): This refers to the stream data for one record at a time or in small batches.

You are charged $0.01 per 200 MB for rows that are successfully inserted. Individual rows are calculated using a 1 KB minimum size.

      * For detailed pricing information, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing#free).




The final cost of using the Backup and DR reporting system can be calculated using the following dimensions:

  * The volume of log data in Cloud Logging if the data exceeds 50 GiB per month and the retention period is longer than the default retention period.
  * The volume of data streamed to BigQuery is charged at $0.01 per 200 MB.
  * The volume of reporting data stored in BigQuery if the data stored exceeds 10 GiB per month.



The following is an example to help you understand the pricing for using the Backup and DR reporting system.

For this example:

  * There are 1,000 resources backed up every hour.
  * The approximate volume of reporting data being generated per month is 2 GiB.
  * The retention period of reporting data is set to the default retention period.



The incurred charges for the earlier example is $0.1 and is calculated as follows:

  * The cost for working with Backup and DR metrics in Cloud Monitoring is $0 as the metrics are non-chargeable.
  * The cost for working with logs in Cloud Logging is $0, as the monthly volume of reporting data is less than 50 GiB and the retention period of reporting data is set to the default retention period.
  * The cost for viewing reports in BigQuery is $0.1.

    * The streaming charges are calculated as _2 GB / 200 MB x $0.01 = $0.1_.
    * As the volume of reporting data stored per month is less than 10 GiB, the cost for storing reporting data is $0.
    * As the volume of query data is less than 1 TiB, the cost for querying the data is $0.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
