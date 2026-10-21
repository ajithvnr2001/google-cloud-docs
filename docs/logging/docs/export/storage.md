---
url: https://docs.cloud.google.com/logging/docs/export/storage/
title: View logs routed to Cloud Storage \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:40.518307+00:00
---

# View logs routed to Cloud Storage  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/export/storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  View logs routed to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how you can find log entries that you routed from Cloud Logging to [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs).

Log entries are saved to Cloud Storage buckets in hourly batches. It might take from 2 to 3 hours before the first entries begin to appear.

## Before you begin

For a conceptual discussion of sinks, see [Overview of routing and storage models: Sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks).

For instructions on how to route your logs, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## View logs

To view your logs routed to Cloud Storage, do the following:

  1. In the Google Cloud console, go to the **Buckets** page: 

[Go to **Buckets**](https://console.cloud.google.com/storage/browser)

If you use the search bar to find this page, then select the result whose subheading is **Cloud Storage**.

  2. Select the Cloud Storage bucket you are using as your routing destination.




## Logs organization

When you route logs to a Cloud Storage bucket, Logging writes a set of files to the bucket.

The files are organized in directory hierarchies by log type and date. The log type, referred to as `[LOG_ID]` in the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) reference, can be a name like `syslog` or a compound name like `appengine.googleapis.com/request_log`. If these logs were stored in a bucket named `my-gcs-bucket`, then the directories would be named as in the following example:
    
    
    my-gcs-bucket/syslog/YYYY/MM/DD/
    my-gcs-bucket/appengine.googleapis.com/request_log/YYYY/MM/DD/
    

A single Cloud Storage bucket can contain logs from multiple resource types. The maximum file size is 3.5 GiB.

Logging doesn't guarantee deduplication of log entries from sinks containing identical or overlapping queries; log entries from those sinks might be written multiple times to a Cloud Storage bucket.

The leaf directories (`DD/`) contain multiple files, each of which holds the routed log entries for a time period specified in the filename. The files are _sharded_ and their names end in a shard number, `Sn` or `An` (n=0, 1, 2, ...). For example, here are two files that might be stored within the directory `my-gcs-bucket/syslog/2015/01/13/`:
    
    
    08:00:00_08:59:59_S0.json
    08:00:00_08:59:59_S1.json

These two files together contain the `syslog` log entries for all instances during the hour beginning 08:00:00 UTC and ending 08:59:59 UTC. The log entry timestamps are expressed in UTC (Coordinated Universal Time).

Log entries that arrive with a `receiveTimestamp` within the 60-minute aligned window of their `timestamp` are written to _main shard_ files. For example, a log entry with a `timestamp` of 08:00:00 and a `receiveTimestamp` of 08:10:00 is stored in the main shard file.

These files include a numbered main shard in the suffix: `_Sn.json`.

Log entries that arrive with a `timestamp` in a different 60-minute aligned window than their `receiveTimestamp` are written to _addendum shard_ files. For example, A log entry with a `timestamp` of 08:00:00 and a `receiveTimestamp` of 09:10:00 is stored in an addendum shard file.

These files include a numbered addendum shard with the suffix: `_An:Unix_timestamp.json`.

For example, a log entry that has a `timestamp` between 08:00:00 and 08:59:59 but a `receiveTimestamp` in a different 60-minute aligned window is written to a file with the `_An:Unix_timestamp.json` suffix, where the Unix timestamp identifies the time the file was routed to Cloud Storage. If a log entry had a `timestamp` of 08:50:00 and a `receiveTimestamp` of 09:10:00, and was routed at 09:15:00 on March 25, 2021, the addendum file would be written as follows:
    
    
    08:00:00_08:59:59_A0:1616681700.json

To get all the log entries, you must read all the shards for each time period—in this case, file shards 0 and 1. The number of file shards written can change for each time period.

Within the individual sharded files, log entries are stored as a list of [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) objects. For an example of a `syslog` entry, see [Log entries organization](https://docs.cloud.google.com/logging/docs/export/bigquery#partition-table-organization).

Note that sort order of log entries within the files is neither uniform nor otherwise guaranteed.

### Limitation

The `LogEntry.errorGroups` field isn't available for this destination. Log sinks route the log entries sent to your project, but those log entries don't contain error groups.

## Late-arriving log entries

Routed log entries are saved to Cloud Storage buckets in hourly batches. It might take from 2 to 3 hours before the first entries begin to appear. Routed log file shards with the suffix `An` ("Append") hold log entries that arrived late.

If the destination experiences an outage, then Cloud Logging buffers the data until the outage is over.

If there aren't any logs in your sink's destination, check the [export system metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#system-defined_metrics). The export system metrics indicate how many log entries are routed and how many are dropped due to errors. If the export system metrics indicate that no log entries were routed to the destination, check your [filter][export-query] to verify that log entries matching your filter have recently arrived in Logging.

In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

### App Engine log entries

App Engine combines multiple sub-entries of type [`google.appengine.logging.v1.LogLine`](https://docs.cloud.google.com/logging/docs/reference/v1beta3/rest/v1beta3/LogLine) (also called AppLog or AppLogLine) under a primary log entry of type [`google.appengine.logging.v1.RequestLog`](https://docs.cloud.google.com/logging/docs/reference/v1beta3/rest/v1beta3/RequestLog) for the request that causes the log activity. The log lines each have a "request ID" that identifies the primary entry. The Logs Explorer displays the log lines with the request log entry. Logging attempts to put all the log lines into the batch with the original request, even if their timestamps would place them in the next batch. If that isn't possible, the request log entry might be missing some log lines, and there might be "orphan" log lines without a request in the next batch. If this possibility is important to you, be prepared to reconnect the pieces of the request when you process your logs.

## Troubleshooting

If logs seem to be missing from your sink's destination or you otherwise suspect that your sink isn't properly routing logs, then see [Troubleshoot routing logs](https://docs.cloud.google.com/logging/docs/export/troubleshoot).

## Pricing

For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page. If you route log data to other Google Cloud services, then see the following documents:

  * [Cloud Storage pricing](https://cloud.google.com/storage/pricing)
  * [BigQuery pricing](https://cloud.google.com/bigquery/pricing#data_ingestion_pricing)
  * [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
