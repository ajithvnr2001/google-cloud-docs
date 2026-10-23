---
url: https://docs.cloud.google.com/workflows/docs/monitor/
title: Monitor workflows \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:26.594808+00:00
---

# Monitor workflows  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Monitor workflows Stay organized with collections  Save and categorize content based on your preferences. 

[Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) provides monitoring, logging, and diagnostic tools. These tools can help you monitor and analyze workflow deployments and executions, and understand the behavior, health, and performance of your applications.

By default, Workflows is configured to do the following:

  * Send data and system audit logs to Cloud Logging. You can use the collected logs to debug, troubleshoot, and gain insights about your applications.
  * Send system and resource metrics to Cloud Monitoring. You can use the collected metrics to monitor health and performance, identify trends and issues, and notify for changes in behavior.



## Send audit logs to Cloud Logging

Workflows sends the following types of audit log data to Cloud Logging:

  * [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
  * [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access)
  * [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event)
  * [Policy Denied audit logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied)



Data Access audit logs are disabled by default because these audit logs can be quite large. For more information, see [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

For more information about audit logs in Workflows, see the following:

  * [Audit logging for workflows](https://docs.cloud.google.com/workflows/docs/audit-logging)
  * [Audit logging for workflow executions](https://docs.cloud.google.com/workflows/docs/audit-logging-workflow-executions)



You can also [send execution logs to Cloud Logging](https://docs.cloud.google.com/workflows/docs/log-workflow).

## Send metrics to Cloud Monitoring

Workflows sends metric data from monitored resources to Google Cloud Observability. A monitored resource in Monitoring represents a logical or physical entity, such as a virtual machine, a database, or an application. Monitored resources contain a unique set of metrics that can be explored, reported through a dashboard, or used to create alerts. Each resource also has a set of resource labels, which are key-value pairs that hold additional information about the resource. Resource labels are available for all metrics associated with the resource.

To view all resource types, see [Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources). To view all metric types, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp). Expand the following to see a list of the metric types sent from Workflows to Google Cloud Observability:

#### Workflows metric types

The "metric type" strings in this table must be prefixed with `workflows.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`await_callback_step_count` GA ** _(project)_**   
Await Callback Step Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps that wait for a callback. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`callback_requests_count` GA ** _(project)_**   
Callback Requests Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of requests made to trigger a callback. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`callback_timeout_count` GA ** _(project)_**   
Callback Timeout Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of callbacks that timed out. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`cmek_protected_workflow_count` GA ** _(project)_**   
CMEK Protected Workflow Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of workflows deployed with CMEK protection. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`compute_slice_count` GA ** _(project)_**   
Compute Slice Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of compute slices executed. Steps are executed in slices of work, which depends on the of type steps being executed (e.g. HTTP requests will run separately from “assign” steps). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`type`: The type of compute slice, such as "IO_REQUEST" or "WAKEUP".   
`has_parallel`: (BOOL) Whether the workflow uses parallel steps.   
`compute_slice_latencies` GA ** _(project)_**   
Compute Slice Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies from the time a compute slice was scheduled to the time it was executed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`type`: The type of compute slice, such as "IO_REQUEST" or "WAKEUP".   
`has_parallel`: (BOOL) Whether the workflow uses parallel steps.   
`compute_step_count` GA ** _(project)_**   
Compute Step Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of compute steps executed (e.g. "assign" and "for" steps). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`compute_step_latencies` GA ** _(project)_**   
Compute Step Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies of executed compute steps. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`create_callback_step_count` GA ** _(project)_**   
Create Callback Step Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps that create a callback. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`method`: The method type of the created callback, such as "POST".   
`deployment_attempt_count` GA ** _(project)_**   
Deployment Attempt Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of workflow deployment attempts. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`result`: The status of the deployment attempts.   
`deployment_latencies` GA ** _(project)_**   
Deployment Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies of workflow deployment attempts. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`duplicate_event_count` GA ** _(project)_**   
Duplicate Event Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of duplicate event triggers received. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`event_type`: The type of the event.   
`event_time_to_ack_latencies` GA ** _(project)_**   
Event Time To Ack Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies from the time an event starts to the time the workflows service acks it. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`event_type`: The type of the event.   
`event_trigger_count` GA ** _(project)_**   
Event Trigger Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of event triggers received. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`event_type`: The type of the event.   
`result`: The result of the event trigger.   
`execution_backlog_size` GA ** _(project)_**   
Execution Backlog Size   
`GAUGE`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executions that have not started yet. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`execution_times` GA ** _(project)_**   
Execution times   
`DELTA`, `DISTRIBUTION`, `s`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Distribution of workflow execution times. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`external_step_count` GA ** _(project)_**   
External step count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Count of executed external steps for the workflow. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._  
`finished_execution_count` GA ** _(project)_**   
Finished execution count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Count of finished executions for the workflow. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The execution status of the workflow.   
`revision_id`: The revision ID of the executed workflow.   
`internal_execution_error_count` GA ** _(project)_**   
Internal Execution Error Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executions that failed with an internal error. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`internal_step_count` GA ** _(project)_**   
Internal step count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Count of executed internal steps for the workflow. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._  
`io_internal_request_count` GA ** _(project)_**   
IO Internal Request Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of I/O requests made by a Workflow to Google services. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`service_domain`: The domain of the Google service being called, such as "bigquery.googleapis.com".   
`io_step_count` GA ** _(project)_**   
IO Step Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of I/O steps executed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`io_result`: The I/O step result.   
`io_step_type`: The I/O step type.   
`destination_type`: The I/O step destination type.   
`had_system_error`: (BOOL) Whether the I/O step had a system error.   
`io_step_latencies` GA ** _(project)_**   
IO Step Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies of I/O steps executed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`io_result`: The I/O step result.   
`io_step_type`: The I/O step type.   
`had_system_error`: (BOOL) Whether the I/O step had a system error.   
`kms_decrypt_latencies` GA ** _(project)_**   
KMS Decrypt Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies of decrypt requests to KMS by workflows for CMEK. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`status`: The status of the decrypt requests.   
`attempts`: (INT64) The attempts count of the decrypt requests.   
`kms_decrypt_request_count` GA ** _(project)_**   
KMS Decrypt Request Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of KMS decrypt requests made by the service for CMEK. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`status`: The status of the decrypt requests.   
`kms_encrypt_latencies` GA ** _(project)_**   
KMS Encrypt Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies of encrypt requests to KMS by workflows for CMEK. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`status`: The status of the encrypt requests.   
`attempts`: (INT64) The attempts count of the encrypt requests.   
`kms_encrypt_request_count` GA ** _(project)_**   
KMS Encrypt Request Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of KMS encrypt requests made by the service for CMEK. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`status`: The status of the encrypt requests.   
`parallel_branch_step_count` GA ** _(project)_**   
Parallel branch step count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps using parallel branches. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`parallel_branch_substep_count` GA ** _(project)_**   
Parallel branch substep count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps within parallel branches. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`parallel_iteration_step_count` GA ** _(project)_**   
Parallel iteration step count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps using parallel iterations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`parallel_iteration_substep_count` GA ** _(project)_**   
Parallel iteration substep count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps within parallel iterations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`parallel_unhandled_exceptions_limit_count` GA ** _(project)_**   
Parallel unhandled exceptions limit count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of times the unhandled parallel exception limit was reached. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`pending_io_requests` GA ** _(project)_**   
Pending IO Requests   
`GAUGE`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of in-flight I/O requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`sent_bytes_count` GA ** _(project)_**   
Network bytes sent   
`DELTA`, `INT64`, `By`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Count of outgoing HTTP bytes (URL, headers and body) sent by the workflow. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`started_execution_count` GA ** _(project)_**   
Started execution count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Count of started executions for the workflow. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`started_vpcsc_executions_count` GA ** _(project)_**   
Started VPC-SC Executions Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of VPC-SC restricted executions started. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`vpcsc_protected_io_count` GA ** _(project)_**   
VPC-SC Protected IO Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of I/O requests made using VPC-SC. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
  
Table generated at 2026-10-14 20:24:33 UTC.

### Read metric data

You can read metric data, also called time-series data, by using the `timeSeries.list` method in the Cloud Monitoring API. There are several ways to call the method, including using a language-specific client library, or by creating a chart with [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).You can also try out the `timeSeries.list` method using the forms-based [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer). For an introduction to metrics and time series, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics). To learn how to read your metric data, see [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics).

### Monitor quota metrics

The following example demonstrates how to use the APIs Explorer to query the total consumed allocation quota for Workflows. Specifically, it uses the `serviceruntime.googleapis.com/quota/allocation/usage` metric on the `Consumer Quota` resource type. You can set additional label filters (`service`, `quota_metric`) to specify the quota type. For more information about how to monitor quota metrics, including further examples and how to create alerting policies, see [Chart and monitor quota metrics](https://docs.cloud.google.com/monitoring/alerts/using-quota-metrics).

  1. Open the `timeSeries.list` [reference page](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list).

  2. If the **Try this method** pane isn't visible, click **Try it!**

  3. In the **name** field, enter your Google Cloud project ID using the following format:
         
         projects/PROJECT_ID
         

  4. In the **filter** field, specify a single metric type and, optionally, metric labels and other information. For example:
         
         metric.type = "serviceruntime.googleapis.com/quota/allocation/usage" AND resource.labels.service = "workflowexecutions.googleapis.com"
         

  5. In the **interval.endTime** field, enter an end time to limit how much data is returned, and that's applicable to your usage. It should be formatted as an RFC 3339 string; for example, `2024-11-07T03:01:02Z`.

  6. In the **interval.startTime** field, enter a start time to limit how much data is returned, and that's applicable to your usage. It should be formatted as an RFC 3339 string; for example, `2024-11-07T03:01:00Z`.

  7. Click **Execute**.

The result should be similar to the following with `350` indicating the [concurrent executions](https://docs.cloud.google.com/workflows/quotas#quotas) quota metric.
         
         {
         "timeSeries": [
            {
               "metric": {
               "labels": {
                  "quota_metric": "workflowexecutions.googleapis.com/concurrency"
               },
               "type": "serviceruntime.googleapis.com/quota/allocation/usage"
               },
               "resource": {
               "type": "consumer_quota",
               "labels": {
                  "service": "workflowexecutions.googleapis.com",
                  "project_id": "PROJECT_ID",
                  "location": "europe-west1"
               }
               },
               "metricKind": "GAUGE",
               "valueType": "INT64",
               "points": [
               {
                  "interval": {
                     "startTime": "2024-11-07T03:01:02Z",
                     "endTime": "2024-11-07T03:01:02Z"
                  },
                  "value": {
                     "int64Value": "350"
                  }
               }
               ]
            }
         

  8. In the collapsed APIs Explorer side panel, you can click Full screen fullscreen to expand the APIs Explorer. The full-screen panel displays an extra pane containing code samples, `application/json` responses, and Raw HTTP responses. For example, in this case, you can view the comparable curl command:
         
         curl \
         'https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%20%3D%20%22serviceruntime.googleapis.com%2Fquota%2Fallocation%2Fusage%22%20AND%20resource.labels.service%20%3D%20%22workflowexecutions.googleapis.com%22&interval.endTime=2024-11-07T03%3A01%3A02Z&interval.startTime=2024-11-07T03%3A01%3A00Z&key=YOUR_API_KEY' \
            --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
            --header 'Accept: application/json' \
            --compressed
         




### Use Monitoring dashboards and alerts

You can use Monitoring dashboards and their associated charts to visualize the data for Workflows metrics.

To monitor these metrics in Monitoring, you can [create custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#custom_dashboards). You can also [add alerts](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api) based on these metrics.

## What's next

  * [Debugging overview](https://docs.cloud.google.com/workflows/docs/debug)
  * [Known issues for Workflows](https://docs.cloud.google.com/workflows/docs/issues)
  * [Troubleshoot issues](https://docs.cloud.google.com/workflows/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
