---
url: https://docs.cloud.google.com/logging/docs/view/correlate-logs/
title: Correlate log entries \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:33.120527+00:00
---

# Correlate log entries  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/view/correlate-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Correlate log entries Stay organized with collections  Save and categorize content based on your preferences. 

In the Logs Explorer, you can correlate log entries associated with the same trace to group and view them together, which simplifies troubleshooting operations across a request. When you correlate log entries by setting the `trace` field in the [`LogEntry` object](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry), the Logs Explorer displays child log entries nested under their parent request log entry.

## When log entries can be correlated

For log entries to correlate, each entry must include the `trace` field. When you instrument an application with OpenTelemetry, the trace and span IDs are extracted from the trace context and included in the OTLP log data sent to your project. If you use Google Cloud exporters, then they also extract these fields. Alternatively, you can set the `trace` field manually.

The following Google Cloud services capture trace data and write log entries that include trace information:

  * App Engine standard environment
  * Cloud Run functions
  * Cloud Run



In addition, Compute Engine and Google Kubernetes Engine environments capture and include trace data when they use the Ops Agent or the OpenTelemetry Collector.

For information about instrumenting your application to collect trace data, see [Instrument for Cloud Trace](https://docs.cloud.google.com/trace/docs/setup).

### Correlation requirements

For the Logs Explorer to correlate a collection of log entries, the log entries must meet the following requirements:

  * The `trace` field in the [`LogEntry` object](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) is set to a string with one of the following formats:
        
        TRACE_ID
        

or
        
        projects/PROJECT_ID/traces/TRACE_ID
        

In the preceding expressions, PROJECT_ID is the ID of your project and TRACE_ID is the ID of the trace.

  * The value of the `trace` field is the same across all log entries.

  * Each log entry has a different `logName` value.

  * The timestamp of the parent log entry is no later than the timestamp of any child log entry.




## Before you begin

To get the permissions that you need to use the Logs Explorer to view log entries, ask your administrator to grant you the following IAM roles: 

  * To view log entries in the `_Required` bucket and those in the `_Default` view on the `_Default` bucket, or to select a log scope: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on your project, folder, or organization. 
  * To view all log entries in the `_Required` and `_Default` buckets: [Private Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer) (`roles/logging.privateLogViewer`) on your project, folder, or organization. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View and search correlated log entries in the Logs Explorer

To view and search log entries using a parent-child structure, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **Correlate by** menu, select the parent log name. For example, select `request_log` for App Engine applications.

The **Query results** pane displays one row for each log entry that matches the parent log name.

To view correlated log entries, click _chevron_right_ **Expand this log entry** :

![Display of correlated log entries.](https://docs.cloud.google.com/static/logging/docs/images/nested-logs.png)

The preceding screenshot shows a parent log entry that has two child log entries.

If you expand a parent log entry and no child log entries appear, then no other log entries within the query's time range share that trace ID.

  3. Optional: Enter a search term or update the query expression to filter or search the correlated log entries.

For example, if you enter `"app log message"` in the search bar and click **Run query** , then the **Query results** pane shows only log entries that contain the text `"app log message"`.




## What's next

  * For instrumentation information, see [Instrument for Cloud Trace](https://docs.cloud.google.com/trace/docs/setup).

  * For information about App Engine request logs and application logs, see [Reading and writing application logs](https://docs.cloud.google.com/appengine/docs/legacy/standard/python).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
