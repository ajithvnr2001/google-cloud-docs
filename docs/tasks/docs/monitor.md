---
url: https://docs.cloud.google.com/tasks/docs/monitor/
title: Observability in Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:17.678183+00:00
---

# Observability in Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Observability in Cloud Tasks Stay organized with collections  Save and categorize content based on your preferences. 

[Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) lets you monitor and analyze Cloud Tasks activity, queue growth, and execution behavior. You can evaluate application health, diagnose task failures, and troubleshoot performance issues using collected metrics and logs.

By default, Cloud Tasks sends system and resource metrics to Cloud Monitoring and exports Admin Activity audit logs to Cloud Logging. Data Access audit logs are disabled by default and require explicit configuration.

## Send audit logs to Cloud Logging

Cloud Tasks sends the following types of audit log data to Cloud Logging:

  * [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
  * [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access)
  * [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event)
  * [Policy Denied audit logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied)



Data Access audit logs are [disabled by default](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) because these audit logs can be quite large.

For more information, see [Cloud Tasks audit logging](https://docs.cloud.google.com/tasks/docs/audit-logging).

## Use Cloud Logging with queues

You can use Cloud Logging with Cloud Tasks queues. The following operations are logged:

  * Task operations: 
    * `CreateTask`
    * `DeleteTask`
  * Attempt operations: 
    * `AttemptDispatch`
    * `AttemptResponse`



### Enable logging

You can enabling logging using the Google Cloud console or the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Tasks** > **Queues** page.

[Go to Queues](https://console.cloud.google.com/cloudtasks)

  2. Click the name of the queue that you want to enable logging for.

  3. On the **Queue details** page, click the **Logs** tab.

  4. Click **Enable logs** and, to confirm, click **Enable**.

![screenshot](https://docs.cloud.google.com/static/tasks/docs/images/enable-logs.png)




###  gcloud 

To enable logging, you can use either the [`gcloud tasks queues create`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/create) or the [`gcloud tasks queues update`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/update) command.
    
    
    gcloud tasks queues create QUEUE_ID \
        --log-sampling-ratio=LOG_SAMPLING_RATION

or
    
    
    gcloud tasks queues update QUEUE_ID \
        --log-sampling-ratio=LOG_SAMPLING_RATIO

Replace the following:

  * `QUEUE_ID`: the ID of your queue
  * `LOG_SAMPLING_RATIO`: the fraction of the operations logged. Any value between `1.0` and `0.0` logs that fraction of operations. To log all operations, set it to `1.0`. To log no operations, set it to `0.0` (this is the default).



### Disable logging

You can disable logging using the Google Cloud console or the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Tasks** > **Queues** page.

[Go to Queues](https://console.cloud.google.com/cloudtasks)

  2. Click the name of the queue that you want to disable logging for.

  3. On the **Queue details** page, click the **Logs** tab.

  4. Click the ellipsis icon more_vert> **Disable logs**. To confirm, click **Disable**.

![screenshot](https://docs.cloud.google.com/static/tasks/docs/images/disable-logs-tasks.png)




###  gcloud 

To disable logging, use the [`gcloud tasks queues update`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/update) command and set the `log-sampling-ratio` flag to `0.0`.
    
    
    gcloud tasks queues update QUEUE_ID \
        --log-sampling-ratio=0.0

Replace `QUEUE_ID` with the ID of your queue.

## Query and view logs

You can use following tools to view and analyze your logs:

  * **Logs Explorer** is designed to to help you troubleshoot and analyze the performance of your services and applications. To learn how to view logs in the Logs Explorer, follow the instructions in [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).
  * **Observability Analytics** is designed to run queries to analyze your logs, and then view or chart the results. To learn how to use Observability Analytics, follow the instructions in [Query and analyze logs with Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).



You can filter for Cloud Tasks logs in the Logs Explorer by searching for `cloudtasks` in the search field.

For more information about querying and analyzing logs, see [Query and view logs overview](https://docs.cloud.google.com/logging/docs/log-analytics).

## Send metrics to Monitoring

Cloud Tasks sends metric data from monitored resources to Google Cloud Observability. A monitored resource in Monitoring represents a logical or physical entity, such as a virtual machine, a database, or an application. Monitored resources contain a unique set of metrics that can be explored, reported through a dashboard, or used to create alerts. 

Cloud Tasks sends metric data from the following monitored resource to Google Cloud Observability:

  * [`cloud_tasks_queues`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_tasks_queue)



Each resource also has a set of resource labels, which are key-value pairs that hold additional information about the resource. Resource labels are available for all metrics associated with the resource and are detailed in the following table.

### Resource metrics and labels

The "metric type" strings in this table must be prefixed with `cloudtasks.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`api/request_count` GA ** _(project)_**   
API requests   
`DELTA`, `INT64`, `1`   
**[cloud_tasks_queue](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_tasks_queue)** |  _Count of Cloud Tasks API calls. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`api_method`: The API method called (e.g. CreateTask).   
`response_code`: Canonical response code as string (e.g. 'ok').   
`queue/depth` GA ** _(project)_**   
Queue depth   
`GAUGE`, `INT64`, `1`   
**[cloud_tasks_queue](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_tasks_queue)** |  _The number of tasks in the queue. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`queue/task_attempt_count` GA ** _(project)_**   
Task attempt count   
`DELTA`, `INT64`, `1`   
**[cloud_tasks_queue](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_tasks_queue)** |  _Count of task attempts broken down by response code. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`response_code`: Canonical response code as string (e.g. 'ok').   
`queue/task_attempt_delays` GA ** _(project)_**   
Task attempt delays   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_tasks_queue](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_tasks_queue)** |  _Delay between each scheduled attempt time and actual attempt time. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
  
Table generated at 2026-10-14 20:24:33 UTC.

To view all resource types, see [Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources). To view all metric types, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

### Read metric data

You can read metric data, also called time-series data, by using the `timeSeries.list` method in the Cloud Monitoring API. There are several ways to call the method, including using a language-specific client library, or by creating a chart with [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). For an introduction to metrics and time series, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics). To learn how to read your metric data, see [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics).

### Use Monitoring dashboards and alerts

You can use Monitoring dashboards and their associated charts to visualize the data for Cloud Tasks metrics.

To monitor these metrics in Monitoring, you can [create custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#custom_dashboards). You can also [add alerts](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api) based on these metrics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
