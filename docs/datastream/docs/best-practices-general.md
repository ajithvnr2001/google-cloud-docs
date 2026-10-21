---
url: https://docs.cloud.google.com/datastream/docs/best-practices-general/
title: General best practices when using Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:44.377159+00:00
---

# General best practices when using Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/best-practices-general/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Resources ](https://docs.cloud.google.com/datastream/docs/quotas)



Send feedback 

#  General best practices when using Datastream Stay organized with collections  Save and categorize content based on your preferences. 

In this page, you'll find best practices for using Datastream. These include general best practices when using Datastream.

## Change a stream's source database

In some cases, you may have to change the source database of a stream. For example, you may have to modify the stream to replicate from a replica instead of from the primary database instance.

  1. [Create a connection profile](https://docs.cloud.google.com/datastream/docs/create-connection-profiles) for the replica instance.
  2. [Create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream), using the connection profile for the replica that you created and the existing connection profile for the destination.
  3. [Start the stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#startastream) with historical backfill disabled. When the stream is started, it will bring only the data from the binary logs.
  4. Optional. After the stream is running, [modify it](https://docs.cloud.google.com/datastream/docs/modify-a-stream) to enable automatic backfill.
  5. [Pause the stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#pauseastream) that's reading from the primary instance.
  6. Optional. [Delete the stream](https://docs.cloud.google.com/datastream/docs/delete-a-stream) that was streaming data from the primary instance.
  7. Optional. [Delete the connection profile](https://docs.cloud.google.com/datastream/docs/delete-a-connection-profile) for the primary instance.



## Alert and monitor in Datastream

The Datastream dashboard contains a great deal of information. This information can be helpful for debugging purposes. Additional information can be found in the logs, which are available in Cloud Logging.

**Tip:** Use [Google Cloud Monitoring](https://docs.cloud.google.com/monitoring) to create a custom dashboard to suit your business needs.

### Datastream alerts

There's no default alert set up for Datastream. For example, you can create an alerting policy for the **Data freshness** metric by clicking the _Create alerting policy_ link in the **Overview** tab. For the remaining metrics, follow these steps:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page:

[ Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

  2. Click **Create policy**.

  3. Click the **Select a metric** drop-down.

  4. In the filter field, enter `Datastream`.

  5. Optional: You might need to disable the **Active** filter to view all available metrics.

  6. Search for the metric that you want to monitor under **Datastream Stream**.

  7. Click **Apply**.

  8. Optional: Enter the required details in the **Add filters** and **Transform data** sections. Click **Next**.

  9. Enter the required information in the **Configure alert trigger** section. Click **Next**.

  10. Configure your notifications in the **Configure notifications and finalize alert** section.

  11. Review your alert and click **Create policy** when ready.

For detailed information about how to complete each of these steps, see [Create alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).




We recommend creating alerts for the following Datastream[ metrics](https://docs.cloud.google.com/datastream/docs/monitor-a-stream#monitorstreams):

  * Data freshness
  * Stream unsupported event count
  * Stream total latencies



An alert on any of these metrics can indicate a problem with either the stream or the source database.

## Understand latency

Datastream provides the following metrics to help you understand replication latency:

  * **Data freshness** : the difference between the time when the data was committed to the source and the time when the data was read by Datastream. If this metric is high, it indicates that Datastream is reading data slower than it's being generated at the source. This indicates that there might be an issue with the source or with the network connection to the source.
  * **System latency** : the time that it takes for Datastream to process an event, from the moment the event is read from the source until it's written to the destination.
  * **Total latency** : the end-to-end replication lag, representing the total time from when data is committed to the source until it's written to the destination.



If data freshness is high, common causes include:

  * **Source overload:** the source database is generating logs (binlog files, redo log files, WAL files) faster than Datastream can read them. 
    * **Action for MySQL/Oracle:** [Increase the `maxConcurrentCdcTasks` parameter](https://docs.cloud.google.com/datastream/docs/stream-concurrency-controls) to read more logs in parallel.
    * **Action for PostgreSQL:** isolate high-churn tables into their own dedicated streams.
    * **Action for SQL Server:** increase the `maxConcurrentCdcTasks` parameter to read more change tables in parallel.
  * **Source resource starvation:** the source database server itself experiences issues such as high CPU usage, low memory or disk I/O bottlenecks. 
    * **Action:** make sure that the source instance is healthy. Check CPU/RAM usage. For PostgreSQL, consider increasing the value for the `logical_decoding_work_mem` parameter; for Oracle, ensure that sufficient system global area (SGA) is allocated.
  * **Network capacity issues:** high ping time or saturated bandwidth between your source and Google Cloud. 
    * **Action:** monitor your VPN or Cloud Interconnect bandwidth and latency.
  * **Single large transaction:** a large batch job, such as an `UPDATE` on millions of rows, can cause a temporary spike in latency. 
    * **Action:** this is expected. Wait for Datastream to process the large event. Consider breaking large batch jobs into smaller chunks in the future.



If system latency is high, this may indicate an issue within Datastream or the destination.

  * **Action:** check Cloud Logging for persistent, row-level errors (for example, `invalid input for type json`. If the stream is in a retry loop because of data type or constraint errors, this might require manual data correction at the source. If there are no obvious errors, contact Google Support for assistance.



## How many tables can a single stream handle?

We recommend that a single stream includes up to 10,000 tables. There's no limit to the size of the tables. If you need to create a stream with more tables, then the stream might enter an error state. To avoid this, consider splitting the source into multiple streams.

Keep in mind the impact on the source database. Each stream will have its own limit on the number of connections and simultaneous tasks, so combining multiple streams could overwhelm the database.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
