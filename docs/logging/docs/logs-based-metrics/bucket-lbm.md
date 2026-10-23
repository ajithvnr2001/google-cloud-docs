---
url: https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm/
title: Bucket-scoped log-based metrics \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:19.016332+00:00
---

# Bucket-scoped log-based metrics  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Bucket-scoped log-based metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document summarizes the characteristics of bucket-scoped log-based metrics and describes how they differ from project-scoped log-based metrics.

## Characteristics of bucket-scoped log-based metrics

Bucket-scoped log-based metrics are user-defined log-based metrics that evaluate log entries routed to a specific log bucket. With bucket-scoped log-based metrics, you can create log-based metrics that extract data from logs in the following cases:

  * Logs that are routed from one project to a bucket in another project.
  * Logs that are routed into a bucket through an aggregated sink.



Like project-scoped log-based metrics, bucket-scoped log-based metrics are defined within a Google Cloud project, not at the folder or organization level. If you want to track the folder or organization from which a log entry was routed to the bucket, then you can define labels in the log-based metric to record that information.

  * For general information about log-based metrics, see [Log-based metrics overview](https://docs.cloud.google.com/logging/docs/logs-based-metrics).
  * For information about routing and sinks, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).



Bucket-scoped log-based metrics have several differences from project-scoped log based metrics.

## Projects and metrics scopes

Bucket-scoped log-based metrics are defined in the same project that contains the source bucket. By default, only the project that defines a bucket-scoped log-based metric can see the metric data for the log bucket. However, if your project appears in the metrics scope of other projects, those projects can also see your metrics.

The Google Cloud projects that route logs to the bucket **do not** need to be in the metrics scope of any project.

For more information about log-based-metrics and metrics scopes, see [Visibility to metrics scopes](https://docs.cloud.google.com/logging/docs/logs-based-metrics#lbm-scoping).

When the logs are received at the bucket, the routed log metric data derived is visible to any project that includes the bucket's project in its metrics scope. If a project routing logs is not in the metrics scope of any project, then other information in the routing project is not visible.

When using bucket-scoped log-based metrics, the following statements apply:

  * You define the log-based metric in the project with the destination bucket.
  * Your bucket-scoped log-based metrics evaluates all log entries routed to the bucket, regardless of whether the log is from the same project as the bucket or from a different project.
  * The metric data is visible to any other project that includes the project with the bucket in its metrics scope.
  * Projects routing logs don't need to be in any project's metrics scope.



## Monitored-resource type: `logging_bucket`

Bucket-scoped log-based metrics use the monitored-resource type `logging_bucket` when writing time-series data to Cloud Monitoring. The [`logging_bucket` resource type](https://docs.cloud.google.com/monitoring/api/resources#tag_logging_bucket) includes the following labels:

  * `project_id`: The identifier of your Google Cloud project, a string like `my-test-project`.
  * `bucket_id`: The name of the log bucket associated with the log-based metric, a string like `my-test-bucket`.
  * `location`: The location of the log bucket.
  * `monitored_resource_type`: The type of the monitored resource that produced this log entry; the value comes from the `type` field from the [`MonitoredResource`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/MonitoredResource) structure contained in the [`resource` field of the log entry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.resource).
  * `source_resource_container`: The identifier for the project, folder, or organization from which the log entry was sent, a string in one of the following forms: 
    * `projects/PROJECT_ID`
    * `organizations/ORGANIZATION_ID`
    * `folders/FOLDER_ID`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
