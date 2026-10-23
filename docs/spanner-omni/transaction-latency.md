---
url: https://docs.cloud.google.com/spanner-omni/transaction-latency/
title: Identify transactions that might cause high latencies \u00a0|\u00a0 Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:46.583861+00:00
---

# Identify transactions that might cause high latencies  |  Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/transaction-latency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Identify transactions that might cause high latencies Stay organized with collections  Save and categorize content based on your preferences. 

Use the system insights dashboards and built-in statistics tables to identify transactions that cause high latencies in Spanner Omni. To ensure the consistency of multiple concurrent transactions, Spanner Omni uses [locks](https://docs.cloud.google.com/spanner/docs/transactions#locking) to control access to the data. Lock contention occurs when many transactions require frequent access to the same lock, leading to high latencies.

Spanner Omni operations acquire locks when the operations are part of a [read-write](https://docs.cloud.google.com/spanner/docs/transactions#read-write_transactions) transaction. Read-only transactions don't acquire locks.

To identify transactions that cause high latencies, follow these steps:

  1. Check for a spike in latencies using system insights.

  2. Identify lock contention issues using the lock wait time metric.

  3. Identify problematic transactions.




## Before you begin

If you haven't already, download and install the Spanner Omni console. For more information see [Spanner Omni downloads](https://docs.cloud.google.com/spanner-omni/download) and [Start the Spanner Omni console](https://docs.cloud.google.com/spanner-omni/use-console#start-the-console).

## Check for a spike in latencies using system insights

Spanner Omni doesn't use Cloud Monitoring. Instead, use the [system insights dashboard](https://docs.cloud.google.com/spanner-omni/use-console#system_insights) in the Spanner Omni console or [Grafana](https://docs.cloud.google.com/spanner-omni/grafana-dashboards). To check for latency spikes in the Spanner Omni console, do the following:

  1. In the Spanner Omni console, click **System Insights** in the navigation pane.

  2. In the system insights dashboard, check the latency charts for the following:

     * Request latency (`P50`, `P90`, `P99`)

     * Transaction latency (`P50`, `P90`, `P99`)

Check the 99th percentile (`P99`) for write operations on the latency charts. If you observe a spike in latency without a corresponding spike in CPU utilization or errors, the latency is likely due to lock contention issues.




## Check for lock contention issues

To check if high latencies are due to lock contention, use the lock wait time metric available in the **System Insights** dashboard.

### Check for high lock wait time

Check for high lock wait time in the Spanner Omni console system insights dashboard:

  1. Locate the **Lock wait time** chart, which shows the total lock wait time for lock conflicts for the selected database in a 5-minute interval.

  2. Check if this metric shows an increase that correlates with the latency spike you observed.




### Analyze the lock wait data using system tables

After you confirm that lock contention is the cause of high latencies, use system statistics tables to analyze lock wait data and identify the transactions that are causing the contention. You can use the [Spanner Omni CLI](https://docs.cloud.google.com/spanner-omni/cli-quickstart) to [query statistics tables](https://docs.cloud.google.com/spanner/docs/introspection/query-statistics) in the Spanner documentation.

For details on lock statistics tables, see [Lock statistics](https://docs.cloud.google.com/spanner/docs/introspection/lock-statistics) in the Spanner documentation.

## Identify contending transactions

To pinpoint the specific transactions that are contributing to high latencies, examine the transaction statistics for your database. Focus on transactions with high average latency. Optimize the transaction shape to reduce latencies. Consider applying the recommended practices to [reduce lock contention](https://docs.cloud.google.com/spanner/docs/introspection/lock-statistics#applying_best_practices_to_reduce_lock_contention) in the Spanner documentation.

For details on transaction statistics tables, see [Transaction statistics](https://docs.cloud.google.com/spanner/docs/introspection/transaction-statistics) in the Spanner documentation.

## What's next

  * [Use Prometheus alerts to monitor Spanner Omni](https://docs.cloud.google.com/spanner-omni/prometheus-alerts).

  * [Use Grafana dashboards to monitor Spanner Omni](https://docs.cloud.google.com/spanner-omni/grafana-dashboards).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
