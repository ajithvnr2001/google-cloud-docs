---
url: https://docs.cloud.google.com/bigtable/docs/data-boost-eligibility/
title: View Data Boost eligibility metrics \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:36.809693+00:00
---

# View Data Boost eligibility metrics  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/data-boost-eligibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View Data Boost eligibility metrics

Bigtable Data Boost is a serverless compute service designed for high-throughput read jobs and queries. A workload must meet certain compatibility criteria to be able to use Data Boost.

This document describes how to check eligibility metrics to determine whether your workload is compatible with Data Boost. Review these metrics if you are are considering converting a **standard app profile that is already in use** to a Data Boost app profile.

Before you view eligibility metrics, review the details on ideal workloads and feature limitations at [Bigtable Data Boost overview](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).

## Eligibility metrics overview

To help you determine whether the workload for a given app profile is suitable for Data Boost, Bigtable provides two metrics:

  * Data Boost traffic eligibility count (`data_boost/eligibility_count`)
  * Data Boost traffic ineligible reasons (`data_boost/ineligible_reasons`)



For more information, see [Metrics](https://docs.cloud.google.com/bigtable/docs/metrics).

## Check eligible and ineligible request counts

To determine whether traffic that is sent by a given app profile is suitable for Data Boost, look at the metric `Data Boost traffic eligibility count`. This metric shows the number of requests that are eligible or ineligible for Data Boost for a given app profile for the last seven days.

To view this metric for a specific app profile, follow these steps:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose metrics you want to view. 

  3. In the navigation pane, under **Insights** , click **Monitoring**.

  4. Click the **Application profiles** tab.

  5. View the **Data Boost eligibility** chart.




## View an app profile's ineligibility reasons

The `Data Boost traffic ineligible reasons` metric tells you _why_ requests sent with a given app profile are considered ineligible for Data Boost. A single request can have multiple reasons for being ineligible. Reasons for ineligibility include the following:

  * The app profile was used for requests that called API methods other than `ReadRows`, `PingAndWarm`, `SampleRowKeys`, `ExecuteQuery`, or `PrepareQuery`.
  * The app profile was used for [reverse scans](https://docs.cloud.google.com/bigtable/docs/reads#reverse-scan).
  * Traffic was sent using an incompatible client library.
  * Requests using the app profile exceeded 1,000 [read requests per second](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring-resources). For more information, see [What it's not good for](https://docs.cloud.google.com/bigtable/docs/data-boost-overview#not-good-for).



To view this metric for a specific app profile, follow these steps:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose metrics you want to view. 

  3. In the navigation pane, under **Insights** , click **System insights**.

  4. Click the **Application profiles** tab.

  5. View the **Data Boost eligibility** chart.




## Conversion-blocking configurations

If you attempt to convert a standard app profile to use Data Boost, the conversion fails if any of the following conditions are true for the app profile.

  * The instance uses CMEK encryption.
  * It's configured for multi-cluster routing.
  * Single-row transactions are enabled.



## What's next

  * [Read the Bigtable Data Boost overview.](https://docs.cloud.google.com/bigtable/docs/data-boost-overview)
  * [Create or configure an app profile.](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles)
  * [Learn more about Bigtable monitoring.](https://docs.cloud.google.com/bigtable/docs/monitoring-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
