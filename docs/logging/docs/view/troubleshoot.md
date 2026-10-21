---
url: https://docs.cloud.google.com/logging/docs/view/troubleshoot/
title: Troubleshoot Logs Explorer \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:36.935538+00:00
---

# Troubleshoot Logs Explorer  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/view/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Troubleshoot Logs Explorer Stay organized with collections  Save and categorize content based on your preferences. 

This document explains common log viewing issues, and describes how to use the Google Cloud console to view and troubleshoot configuration mistakes or unexpected results.

### The all resources and all log name menus are disabled

You open the Logs Explorer page, and the **All resources** and **All log names** menus are disabled.

This is expected behavior when the Logs Explorer page is searching a log view that contains a [flexible filter](https://docs.cloud.google.com/logging/docs/logs-views#view-filter). These filters use an extended set of [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) such as disjunctive clauses.

### Download of logs fails

You are using the Logs Explorer and click _download_ **Download**. The command starts but then fails to complete or reports an error.

To resolve this issue, reduce the time it takes for the command to execute by trying the following:

  * In the **Download logs** dialog, reduce the value of **Maximum log entries**.
  * Reduce the time period over which logs are queried.
  * In the query results toolbar, click **Hide similar entries** before you begin the download.


  * Modify your query to use [indexed fields](https://docs.cloud.google.com/logging/docs/analyze/custom-index).

**Note:** The download feature isn't intended for the bulk download of logs. You can [copy logs](https://docs.cloud.google.com/logging/docs/routing/copy-logs) to a Cloud Storage bucket.

### Can't find console logs for a VM instance

Logs written to the console of a Compute Engine instance might not be available in the Logs Explorer. To view these logs, do the following:

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Select the instance, and then select **Serial port 1 (console)** in the **Logs** section of the page.




You can configure your instances such that their serial port output is sent to Cloud Logging. For more information, see [Enabling and disabling serial port output logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver).

### Get Google Cloud project or organization ID

To get a Google Cloud project or organization ID from anywhere in the Google Cloud console, expand the list of Google Cloud projects from the Google Cloud project and organization selector and find the Google Cloud project ID in the **ID** column.

### Can't see log entries

If you don't see any log entries, check the following:

  * Verify that the correct Google Cloud project is selected.

  * Verify that your Google Cloud project is using resources that generate logs and that there is activity on those resources. Even if the Google Cloud project is new, it should have audit logs recording the fact that it was created. For information about how to verify that you're using a resource that generates logs, see [Mapping services to resource types](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-mappings).

  * Ensure that the time range isn't too narrow.

  * View your [current exclusion queries](https://docs.cloud.google.com/logging/docs/exclusions#viewing-exclusion-filters) to ensure that the logs you're looking for aren't accidentally excluded.

  * Ensure that you have permission to view the log entries in the projects and log views referenced by setting of the **Refine scope** menu. For information about how to adjust the scope of your search, see [Refine scope](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope).




### My query is correct but I still don't see log entries

  * You can't see log entries that are older than the Logging retention period. See [Log retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) for the logs retention period in effect.

  * During periods of heavy load, there could be delays in sending logs to Logging or in receiving and displaying the logs.

  * The Logs Explorer doesn't show log entries that have timestamps in the future until the current time has "caught up" with them. This is an unusual situation, probably caused by a time skew in the application sending the logs.

  * The query scope was set too large and couldn't complete within a reasonable amount of time. You might see this as "deadline expired before operation could complete". Try making your query more specific or reducing the time range.




### Query returns an error

If you issue a query over a resource without specifying a bucket, then Cloud Logging uses the history of the sinks in the Google Cloud project to determine where entries might have been written for that resource. If Cloud Logging identifies more than 200 buckets where entries might have been written, then the query fails with the message `Error: Invalid query`.

To resolve this issue, refine the scope of your query to a subset of the storage. For more information, see [Refine scope](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope).

### Query results time range doesn't match query

The logs data you see in the **Query results** and **Fields** pane adjusts according to the time range captured by the histogram timeline. You adjust the histogram timeline using the histogram's time controls or the [time-range selector](https://docs.cloud.google.com/logging/docs/view/building-queries#time-range). Adjusting these time controls doesn't alter the query expression in the **Query** pane.

When you have a query with a timestamp, the time-range selector is disabled. The query uses the timestamp expression as its time-range restriction. If a query doesn't use a timestamp expression, then the query uses the time-range selector as its time-range restriction.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
