---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/forward-cloud-storage-fuse-logs-to-cloud-logging/
title: Forward Cloud Storage FUSE logs to Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:27:58.800021+00:00
---

# Forward Cloud Storage FUSE logs to Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/forward-cloud-storage-fuse-logs-to-cloud-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Forward Cloud Storage FUSE logs to Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage FUSE logs help you understand how Cloud Storage FUSE operates, troubleshoot issues, and monitor performance. When you generate logs by using the [`--log-severity` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#log-severity) or the [`logging:severity` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#severity), you can view them as standard output or in local log files on the machine where Cloud Storage FUSE runs. Forwarding these logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) lets you view, filter, alert on, and retain them in a central location.

This document describes how to forward Cloud Storage FUSE logs to Cloud Logging.

## Benefits of forwarding logs to Cloud Logging

When you forward Cloud Storage FUSE logs to Cloud Logging, you can do the following:

  * View all Cloud Storage FUSE logs in a single location in the Google Cloud console, which provides a holistic view of Cloud Storage FUSE behavior and makes it easier to correlate events across different components.

  * Filter Cloud Storage FUSE logs by severity level, timestamp, resource type, and other fields, which can help you pinpoint errors or performance issues.

  * Create metrics-based alerts that are triggered by specific log events. For example, you can set up an alert to notify you whenever an `error` or `warning` log message from Cloud Storage FUSE is detected, allowing you to react to problems proactively.

  * Store logs in Cloud Logging for a configurable period, and export them to Cloud Storage for long-term storage, archival, or in-depth analysis.




## Pricing

For pricing information about Cloud Logging, see [Cloud Logging costs](https://docs.cloud.google.com/stackdriver/pricing#logging-costs).

## Get required roles

To get the permissions that you need to use Cloud Logging to view Cloud Storage FUSE logs, grant the [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) IAM role on the project you want to collect metrics for.

This predefined role contains the permissions required to use Cloud Logging. For more information about the Logs Writer role, see the [IAM documentation about `roles/logging.logWriter`](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter).

For instructions on granting roles for projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Before you begin

  1. Enable the Cloud Storage API.

[Go to Cloud Storage API](https://console.cloud.google.com/apis/enableflow?apiid=storage-component.googleapis.com&_ga=2.70110096.1642044780.1726157710-823539626.1726157710)

  2. Enable the Cloud Logging API.

[Go to Cloud Logging API](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com)

  3. [Install the Cloud Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index), which is Google Cloud's primary agent for collecting logs and metrics. Select an installation method based on the type of virtual machine you're using.

  4. Set the logging severity to `trace` by using either the [`--log-severity`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#log-severity) option or the [`severity`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#severity) field to `trace`.




## Forward Cloud Storage FUSE logs to Cloud Logging

  1. Specify `/gcsfuse.log` for your `gcsfuse` mount:
         
         logging:
           file-path: "/gcsfuse.log"
           severity: trace
         

  2. Configure the Cloud Ops Agent to forward logs from the `/gcfuse.log` file to Cloud Logging using the following configuration. In this configuration, `gcsfuse_trace_logs` is a `receiver` element which receives logs from the `/gcsfuse.log` file. The `service` element links the `receiver` element in the pipeline.
         
         logging:
          receivers:
           gcsfuse_trace_logs:
           type: files
           include_paths:
           - /gcsfuse.log
         service:
          pipelines:
            gcsfuse_pipeline:
              receivers: [gcsfuse_trace_logs]
         

To learn about additional logging configurations, see [Cloud Logging configurations](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-config).

  3. Put the configuration for the Cloud Ops Agent in a path based on your operating system. To choose which path to put the configuration, see the [Google Cloud Observability documentation for user-specified configurations](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#file-location).

  4. Restart the Cloud Ops Agent to pick up new configuration changes using the `systemctl restart` command:
         
         sudo systemctl restart google-cloud-ops-agent`
         

  5. Go to Cloud Logging in the Google Cloud console.

  6. Run the `fuse_debug` filtering query to validate the `gcsfuse` trace logs that are forwarded to Cloud Logging.




## What's next

  * Learn how you can [improve Cloud Storage FUSE performance](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
