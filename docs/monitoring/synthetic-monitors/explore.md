---
url: https://docs.cloud.google.com/monitoring/synthetic-monitors/explore/
title: Explore synthetic monitor results \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:36.733572+00:00
---

# Explore synthetic monitor results  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/synthetic-monitors/explore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Explore synthetic monitor results Stay organized with collections  Save and categorize content based on your preferences. 

Reviewing synthetic monitor execution results lets you diagnose test failures, inspect request latency, and analyze how your monitored applications respond. For each synthetic monitor, you can view the execution history, logs, and trace data, as well as the performance metrics and logs for the underlying Cloud Run function.

## Before you begin

Complete the following in the Google Cloud project that stores your synthetic monitor:

  * To get the permissions that you need to view synthetic monitors execution results by using the Google Cloud console, ask your administrator to grant you the following IAM roles on your project: 

    * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
    * [Cloud Functions Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)
    * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## View execution history for a synthetic monitor

To understand the history of passing and failing executions, view the **Synthetic monitor details** page for the synthetic monitor:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. To open the **Synthetic monitor details** page, locate the synthetic monitor that you want to view, and then click its name.



The **Synthetic monitor details** page lists summary information, such as the success rate, the duration, and the most recent status. This page also charts the recorded duration of the execution, and it contains a table that displays one row for each execution.

Each row in the table lists the status, date, and duration, and links to a page that displays the current code and logs relevant to that execution.

## View logs and traces for an execution

To view the logs, traces, and summary information for an execution, on the **Synthetic monitor details** page, click the link to the execution. From this page, you can do the following:

  * View log data.
  * View trace data.
  * View the _current_ code.

**Note:** Cloud Run functions stores one copy of your code. When you view the results for any execution, the displayed code is the _current_ code and it might not be relevant to the specific execution.
  * Access the Cloud Run function.

  * For [Mocha](https://mochajs.org/) tests, view the results for each test. For example, if your synthetic monitor contains four Mocha tests, then the **Test results** pane contains four entries. Each entry in the list is annotated as a pass or fail.

If you select an entry marked as failed, then the failing code is displayed and highlighted.




### View log data

Logs are automatically collected by Cloud Monitoring. These logs contain information about the test and failure details. The available logs depend on your Cloud Run function. For example, if you use [Mocha](https://mochajs.org/), then the logs include information about whether the test passed or failed, test duration, and, in the case of failure, a full stack trace. The stack trace includes the line of code that failed, error types, and error messages.

To view details of your related logs, in the **Execution logs** pane, expand a log entry.

The log entry is displayed in JSON format. If you prefer to view the logs with the Logs Explorer, then click **Open in Logs Explorer**. The Logs Explorer is opened and a query is preconfigured.

### View trace data

Trace data is collected when your Cloud Run function executes. To view trace data, use the Google Cloud console or the Cloud Trace API.

###  Console 

To view your trace data, do one of the following:

  * To view summary information for a trace, in the toolbar of the details page for an execution, click **View trace details**.

The **Details** panel opens and displays a Gantt chart with information about each span, which is a record of an operation, in the trace. For complete information about the trace and its spans, click **View in Cloud Trace** , which opens the **Trace Explorer** page.

  * View your traces in Cloud Trace:

    1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

    2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
    3. In the heatmap chart or in the table, select a trace.



Your trace and spans can include circles in the timeline that represent log entries or events that occurred during execution. Click the circle to display information about the log entry or event. To identify a Cloud Run function in a log entry, view the `resource.labels.service_name` field.

For more information about exploring your trace data, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

###  REST 

We recommend that you use the Google Cloud console to view trace data. However, if you want to use the Cloud Trace API, use the [`traces.list` method](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces/list) to list the available traces, and then use the [`traces.get` method](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces/get) to get the details of a trace.

## View logs and metrics for a Cloud Run function

Logs and metrics provide you with information about the actions your Cloud Run function is performing. For example, logs that contain a field named `userAgent` with a value of `GoogleStackdriverMonitoring-UptimeChecks` indicate that your service received a request from the uptime check service.

The remainder of this section describes how to view the logs and metrics collected by Cloud Run functions.

### View function logs

###  Console 

To view Cloud Run function logs, do the following:

  1. In the pane with the name of your synthetic monitor, click the Cloud Run function name.
  2. On the **Function details** page, select the **Logs** tab.



To explore the log data in a chart in more detail, expand a log entry and then select **Open in Logs Explorer**. From the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), you can perform actions such as refining the query, creating a [log-based metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics), or creating a [log-based alert](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

###  REST 

For information about how to read and write Cloud Run function logs programmatically, see [Writing, Viewing, and Responding to Logs](https://docs.cloud.google.com/functions/docs/monitoring/logging).

### View function metrics

For synthetic monitors, metrics are collected by both Cloud Monitoring and Cloud Run functions:

  * Cloud Monitoring collects metrics about each execution of a synthetic monitor. These metrics include the latency of the code execution and the success history. For information about how to view these metrics, see View execution history for a synthetic monitor.

  * Cloud Run functions collects metrics about each Cloud Run function. These metrics record the execution time, the memory utilization, the instance count, and the number of invocations per second. The remainder of this section describes how to view these metrics.




To view Cloud Run function metrics in the Google Cloud console, do the following:

  1. In the pane with the name of your synthetic monitor, click the Cloud Run function name.
  2. On the **Function details** page, select the **Metrics** tab.



To zoom into a specific time range, do the following:

  1. On a chart, place your pointer at one end of the time range and then left-click your pointer.
  2. Drag your pointer horizontally to the other end of the time range, and then release the pointer button.



To explore the displayed data in a chart in more detail, on the chart toolbar, select _more_vert_ **More chart options** , and then make a selection. The options include the following:

  * Download the chart as a PNG or CSV
  * Save the chart to a custom dashboard
  * Open Metrics Explorer
  * Expand or collapse the chart legend
  * Reset the zoom



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
