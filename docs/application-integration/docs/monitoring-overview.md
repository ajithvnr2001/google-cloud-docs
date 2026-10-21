---
url: https://docs.cloud.google.com/application-integration/docs/monitoring-overview/
title: Monitor Application Integration resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:51.551998+00:00
---

# Monitor Application Integration resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/monitoring-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor Application Integration resources

This page provides details on how to monitor the usage and performance of Application Integration resources in your Google Cloud project. 

Application Integration leverages [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to provide visibility into the usage, performance, alerts, and the overall health of your integration resources. You can use Cloud Monitoring to create custom charts and dashboards to visualize the different performance metrics and resource usages of your integrations. Cloud Monitoring also lets you configure alerts and alert policies for these metrics. For example, you can create a chart to view and monitor the amount of data processed for a specific time period. In addition, you can also set up an alert to check if the total data processed exceeds a specified threshold value. For information about configuring alerts, see [Alerts](https://docs.cloud.google.com/application-integration/docs/alerts). 

You can access and monitor all your integration metrics and resource usages in the following ways:

  * Using [Cloud Monitoring](https://docs.cloud.google.com/application-integration/docs/cloud-monitoring).
  * Using the [monitoring dashboard](https://docs.cloud.google.com/application-integration/docs/monitoring-dashboard) in Application Integration.

**Important:** Cloud Monitoring is a billable component of Google Cloud. For information about the costs and charges of using Cloud Monitoring, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-costs).

## Available metrics and labels

### Resource metrics

The "metric type" strings in this table must be prefixed with `integrations.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`integration/execution_count` GA ** _(project)_**   
Integration execution count   
`DELTA`, `INT64`, `1`   
**[integrations.googleapis.com/IntegrationVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_integrations.googleapis.com/IntegrationVersion)** |  _Count of integration executions since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 86400 seconds._   
`status`: Integration execution status, one of [SUCCEEDED, FAILED, CANCELLED, RETRY_ON_HOLD].   
`trigger_name`: Type of the trigger used for Integration execution, for example, "API trigger" or "Cloud Pub/Sub trigger".   
`trigger_id`: Trigger Id which triggered the execution of Integration.   
`error_enum`: Canonical code of the last error occurred during Integration execution, for example, "PERMISSION_DENIED" or "INVALID_ARGUMENT".   
`is_retry`: (BOOL) Indicates whether the integration execution is a retry or a first attempt, one of [true, false].   
`integration/execution_latencies` GA ** _(project)_**   
Integration execution latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[integrations.googleapis.com/IntegrationVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_integrations.googleapis.com/IntegrationVersion)** |  _A distribution of time taken by the integrations to complete execution. Sampled every 60 seconds. After sampling, data is not visible for up to 86400 seconds._   
`status`: Integration execution status, one of [SUCCEEDED, FAILED, CANCELLED, RETRY_ON_HOLD].   
`trigger_name`: Type of the trigger used for Integration execution, for example, "API trigger" or "Cloud Pub/Sub trigger".   
`trigger_id`: Trigger Id which triggered the execution of Integration.   
`error_enum`: Canonical code of the last error occurred during Integration execution, for example, "PERMISSION_DENIED" or "INVALID_ARGUMENT".   
`is_retry`: (BOOL) Indicates whether the integration execution is a retry or a first attempt, one of [true, false].   
`processed_bytes_count` GA ** _(project)_**   
Processed bytes count   
`DELTA`, `INT64`, `By`   
**[integrations.googleapis.com/IntegrationVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_integrations.googleapis.com/IntegrationVersion)** |  _Size of data consumed by the integration executions since the last sample. It is computed by taking the size of input and output parameters to the integration, along with the request and response payload size for Rest and Connector tasks. Sampled every 60 seconds. After sampling, data is not visible for up to 86400 seconds._   
`step_type`: Indicates whether the data is processed by parameters of the integration, or task request and response payload, one of [Trigger, Task].   
`step_name`: Type of the task used for processing request and response payload, or type of the trigger used for processing parameters of the integration.   
`step_id`: Task number used for processing request and response payload, or Trigger Id used for processing parameters of the integration.   
`step/execution_count` GA ** _(project)_**   
Step execution count   
`DELTA`, `INT64`, `1`   
**[integrations.googleapis.com/IntegrationVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_integrations.googleapis.com/IntegrationVersion)** |  _Count of step (task or trigger) executions since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 86400 seconds._   
`status`: Step execution status, for example "SUCCEEDED" or "FAILED".   
`step_type`: Type of the step executed, one of [Trigger, Task].   
`step_name`: Type of the trigger or task executed, for example, "API Trigger" or "Data Mapping task".   
`step_id`: Trigger Id or task number depending upon which type of step is executed.   
`error_enum`: Canonical code of the error occurred during the step execution, for example, "PERMISSION_DENIED" or "INVALID_ARGUMENT".   
`is_retry`: (BOOL) Indicates whether the step execution is a retry or a first attempt, one of [true, false].   
`is_step_external`: (BOOL) Indicates whether the task executed is internal or external, one of ["true" - external tasks such as Rest or Connector task.; "false" - internal tasks such as Data Mapper or Inline Scripting task].   
`step/execution_latencies` GA ** _(project)_**   
Step execution latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[integrations.googleapis.com/IntegrationVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_integrations.googleapis.com/IntegrationVersion)** |  _A distribution of time taken by the steps (task) to complete execution. Sampled every 60 seconds. After sampling, data is not visible for up to 86400 seconds._   
`status`: Step execution status, for example "SUCCEEDED" or "FAILED".   
`step_name`: Type of the trigger or task executed, for example, "API Trigger" or "Data Mapping task".   
`step_id`: Trigger Id or task number depending upon which type of step is executed.   
`error_enum`: Canonical code of the error occurred during the step execution, for example, "PERMISSION_DENIED" or "INVALID_ARGUMENT".   
`is_retry`: (BOOL) Indicates whether the step execution is a retry or a first attempt, one of [true, false].   
`is_step_external`: (BOOL) Indicates whether the task executed is internal or external, one of ["true" - external tasks such as Rest or Connector task.; "false" - internal tasks such as Data Mapper or Inline Scripting task].   
  
Table generated at 2026-10-08 15:22:12 UTC.

### Labels

Labels are available for Application Integration in the Google Cloud console. You can group or filter each metric using these labels. 

#### Labels for monitored resource

Label  | Description   
---|---  
**resource_container** | The Google Cloud project ID of the integration.  
**location** | The region of the integration.   
**integration** | Name of the integration.  
**version** | The version ID of the integration.  
  
#### Labels for metric type

Label  | Description   
---|---  
**status** | Execution status of the integration or integration step (task or trigger).  
**trigger_name** | Type of trigger used to execute the integration. For example: **API trigger** or **Cloud Pub/Sub trigger**.  
**trigger_id** | The ID of the trigger used to invoke the integration.  
**step_type** | Type of integration step, trigger or task.  
**step_name** | Name of the task or trigger. For example: **API Trigger** or **Data Mapping task**.  
**step_id** | For **Trigger** type: ID of the respective trigger. For **Task** type: Task number of the respective task.  
**error_enum** | The canonical code of the error that occurred during the integration or integration step execution  
**is_retry** | A boolean value to determine if the integration or task execution was retried.  
**is_step_external** | A boolean value to determine if the trigger or task execution was internal or external to the Application Integration execution engine.  For example, the **Call REST Endpoint** task is external, since the API call is made from outside the execution engine. In contrast, the **Data Mapping** task is internal.   
  
For a complete list of available Google Cloud metrics, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-integrations).

## What's next

  * Monitor using [Cloud Monitoring](https://docs.cloud.google.com/application-integration/docs/cloud-monitoring).
  * Monitor using the [monitoring dashboard](https://docs.cloud.google.com/application-integration/docs/monitoring-dashboard) in Application Integration.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
