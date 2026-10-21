---
url: https://docs.cloud.google.com/run/docs/monitoring/
title: Monitor Health and Performance \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:03.120079+00:00
---

# Monitor Health and Performance  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Monitor Health and Performance Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) provides Cloud Run performance monitoring, [metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-run), and [uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks), along with [alerts](https://docs.cloud.google.com/monitoring/alerts) to send notifications when certain metric thresholds are exceeded. [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) applies, which means there is no charge for metrics on the fully managed version of Cloud Run.

Cloud Run incidents are published to [Personalized Service Health](https://docs.cloud.google.com/service-health/docs/overview). You should consider [setting up alerts on Personalized Service Health events](https://docs.cloud.google.com/service-health/docs/configure-alerts-dashboard).

## Built-in metrics

Cloud Run is automatically integrated with Cloud Monitoring **with no setup or configuration required**. This means that metrics of your Cloud Run resources are captured automatically when they are running.

You can view metrics either in Cloud Monitoring or in the Cloud Run resource pages in the console. Cloud Monitoring provides more charting and filtering options.

Key Cloud Run metrics include the following:

Metric | Services | Jobs | Worker pools | Instances  
---|---|---|---|---  
Billable container instance time | ✓ | ✓ | ✓ | ✓  
Container CPU allocation | ✓ | ✓ | ✓ | ✓  
Container CPU utilization | ✓ | ✓ | ✓ |   
Container memory allocation | ✓ | ✓ | ✓ | ✓  
Container memory utilization | ✓ | ✓ | ✓ |   
Container startup latency | ✓ | ✓ | ✓ | ✓  
Container GPU memory usage | ✓ | ✓ | ✓ |   
Container GPU memory utilization | ✓ | ✓ | ✓ |   
Container GPU utilization | ✓ | ✓ |  |   
Container instance count | ✓ |  | ✓ | ✓  
Request count | ✓ |  |  | ✓  
Request latencies | ✓ |  |  | ✓  
Maximum concurrent requests | ✓ |  |  | ✓  
Received bytes | ✓ | ✓ | ✓ | ✓  
Sent bytes | ✓ | ✓ | ✓ | ✓  
Completed executions |  | ✓ |  |   
Completed task attempts |  | ✓ |  |   
Running executions |  | ✓ |  |   
Running task attempts |  | ✓ |  |   
  
For a list of all available Cloud Run metrics and more in-depth details, refer to the [full overview of Cloud Run metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-run) in Cloud Monitoring.

## Create custom metrics

To generate custom metrics from your Cloud Run service, you can deploy a sidecar agent such as [OpenTelemetry](https://docs.cloud.google.com/run/docs/tutorials/custom-metrics-opentelemetry-sidecar) or [Prometheus](https://docs.cloud.google.com/run/docs/monitoring-managed-prometheus-sidecar).

Alternatively, you can use [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) to collect custom metrics.

## Resource types

The monitoring resource names for Cloud Run are:

  * _Cloud Run Revision_ ([`cloud_run_revision`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision))
  * _Cloud Run Job_ ([`cloud_run_job`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job))


  * _Cloud Run Worker Pool_ ([`cloud_run_worker_pool`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool))
  * _Cloud Run Instances_ ([`cloud_run_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance))



## View metrics in Cloud Run

You can view metrics for your Cloud Run resource in the corresponding Cloud Run page in the Google Cloud console.

### Services

To view service metrics in the Cloud Run page:

  1. In the Google Cloud console, go to the **Cloud Run** page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Services** in the Cloud Run navigation menu.

  3. Locate the service in the services list, and click on it.

  4. Click the **Metrics** tab to show the metrics for that service.




Metrics charts for Cloud Run services display deployment events.

### Jobs

To view job metrics in the Cloud Run page:

  1. In the Google Cloud console, go to the **Cloud Run** page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Jobs** in the Cloud Run navigation menu.

  3. Click the job in the jobs list.

  4. Click the **Metrics** tab to show the metrics for that job.




### Worker pools

To view worker pool metrics in the Cloud Run page:

  1. In the Google Cloud console, go to the **Cloud Run** page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Worker pools** in the Cloud Run navigation menu.

  3. Locate the worker pool in the worker pools list, and click on it.

  4. Click the **METRICS** tab to show the metrics for that worker pool.




Metrics charts for Cloud Run worker pools display deployment events.

### Instances

Not applicable to this resource.

## View metrics in Cloud Monitoring

To use Metrics Explorer to view the metrics for a monitored resource, follow these steps:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Configuration** tab, and then enter or select a **Resource type** and a **Metric**. Use the following information to complete the fields: 
     1. For the **Resource** , select the resource type (service, job, worker pool, or instance). 
     2. For the **Metric** , select one of the metrics in menu. For a full description of the available metrics, see: [Monitoring Google Cloud metrics page](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-run). 
  3. (Optional) To configure how the data is viewed, use the **Filter** , **Group By** , and **Aggregator** menus. For example, you can group by resource or metric labels. For more information, see [Selecting metrics](https://docs.cloud.google.com/monitoring/charts/metrics-selector). 



## Add Uptime checks

You can use Cloud Monitoring to keep track of your services' performance. For more information, see [Create public uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks).

## Add Alerts

You can use Cloud Monitoring to send notification about certain events, such as uptime check failures. For more information, see [Create and manage alerting policies](https://docs.cloud.google.com/monitoring/alerts) for your service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
