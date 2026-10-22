---
url: https://docs.cloud.google.com/logging/docs/structured-logging/
title: Structured logging \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:57.652685+00:00
---

# Structured logging  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/structured-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Structured logging Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses the concept of structured logging and the methods for adding structure to log entry payload fields. When the log payload is formatted as a JSON object and that object is stored in the `jsonPayload` field, the log entry is called a _structured log_. For these logs, you can construct queries that search specific JSON paths and you can index specific fields in the log payload. In contrast, when the log payload is formatted as a string and stored in the `textPayload` field, the log entry is _unstructured_. You can search the text field, but you can't index its content.

To create structured log entries, do any of the following:

  * Call the [`entries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write) API method and supply a fully formatted [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).
  * Use the `gcloud logging write` command.


  * Use a Cloud Logging client library which writes structured logs.


  * Use the BindPlane service.


  * Use an agent to write logs:

**Note:** We recommend that you use an agent to write logs, when that option is available. To write structured logs, configure your application to write serialized JSON objects. For a list of logging frameworks, see [Recommended logging frameworks](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach#logging-frameworks)
    * Some Google Cloud services contain an integrated logging agent that sends the data written to `stdout` or `stderr` as logs to Cloud Logging. You can use this approach for Google Cloud services such as Google Kubernetes Engine, App Engine flexible environment, and Cloud Run functions.
    * For Compute Engine virtual machines (VMs), we recommend that you install and configure the Ops Agent to send structured logs to Cloud Logging. If your existing VMs use the legacy Logging agent, note that the agent has reached its end of support. For information about migration alternatives from the legacy Logging agent, see the [migration guide](https://docs.cloud.google.com/logging/docs/agent/logging/migrating-to-fluentd), or see [Structured logging with the legacy Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/structured-logging) for information about using the legacy Logging agent to write structured logs.



For code examples, see [Writing structured logs](https://docs.cloud.google.com/logging/docs/samples/logging-write-log-entry).

## Write logs by using the gcloud CLI

You can write log data by using the gcloud CLI. The interface supports unstructured logs and structured logs. When you want to write a structured log, provide the command a serialized JSON object.

For a quickstart, see [Write and query log entries with the Google Cloud CLI](https://docs.cloud.google.com/logging/docs/write-query-log-entries-gcloud).

For code examples, see the [`gcloud logging write`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/write) reference.

## Write logs by using BindPlane

You can use the BindPlane service to send logs to Logging. For these logs, the payloads are in JSON format and are structured according to the source system. For information on finding and viewing logs ingested by using BindPlane, see the BindPlane [Quickstart Guide](https://bindplane.com/docs/getting-started/quickstart-guide).

## Write logs by using the Ops Agent

**Note:** The content of this section only applies to Compute Engine VM. This section doesn't apply if you are using other services such as Google Kubernetes Engine, App Engine flexible environment, and Cloud Run functions.

To get logs from your Compute Engine instances, you can use the [Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent). The Ops Agent combines logging and metrics into a single agent, provides a YAML-based configuration, and features high-throughput logging.

For information about how to configure the Ops Agent to support structured logging or to customize the form of a structured log, see [Configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration).

## Troubleshoot issues

To troubleshoot common issues found with installing or interacting with the Ops Agent, see [Troubleshooting the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshooting).

## What's next

  * To query and view log entries, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  * To read log entries using the Google Cloud CLI, see [Reading log entries](https://docs.cloud.google.com/logging/docs/api/gcloud-logging#reading_log_entries).

  * To read log entries using the Logging API, see the [`entries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) method.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
