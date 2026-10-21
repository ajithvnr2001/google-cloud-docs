---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/metrics-views/
title: Monitor Cloud Data Fusion system, instance, and pipeline health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:35.335783+00:00
---

# Monitor Cloud Data Fusion system, instance, and pipeline health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/metrics-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Monitor Cloud Data Fusion system, instance, and pipeline health Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to monitor Cloud Data Fusion instances and pipelines. You can view key metrics in the Cloud Data Fusion monitoring dashboard. For additional aggregation or filtering, you can view the metrics in Cloud Monitoring.

## Before you begin

Before you start monitoring Cloud Data Fusion instances and pipelines, review the pricing and grant the required roles.

### Pricing

Cloud Monitoring usage incurs charges. For more information, see [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).

### Required roles

To get the permissions that you need to view metrics, ask your administrator to grant you the [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Monitor in Cloud Data Fusion

View and filter metrics for your instances and pipelines directly in Cloud Data Fusion using the monitoring dashboard:

  1. In the Google Cloud console, go to the Cloud Data Fusion page.

  2. Click **Instances** , and then click the instance's name to go to the **Instance details** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  3. Click the **Monitoring** tab. This displays a dashboard with charts for your instance and its pipelines.

The dashboard displays the following views:

     * **Overview:** Monitors Cloud Data Fusion system metrics.
     * **Instance:** Monitors all Cloud Data Fusion instances in the project.
     * **Pipeline:** Provides information about pipeline runs and performance.

For detailed information about the metrics in any view, hover over the widget and click **More > View in Metrics explorer**.




### Widgets in the monitoring dashboard

The following sections describe the widgets available in the **Overview** , **Instance** , and **Pipeline** views.

#### Overview view widgets

This table describes the widgets in the **Overview** view:

Widget | Description  
---|---  
Appfabric service health | Service availability for Appfabric  
Metric services health | Service availability for metrics  
Wrangler service health | Service availability for Wrangler  
Dataset executor health | Service availability for dataset  
Pipeline studio health | Service availability for Pipeline Studio  
Runtime service health | Service availability for runtime  
Log saver service health | Service availability for log saver  
Metadata service health | Service availability for metadata  
  
#### Pipeline view widgets

This table describes the widgets in the **Pipeline** view:

Widget | Description  
---|---  
Successful pipeline runs | Cumulative count of successful pipeline runs.  
Failed pipeline runs | Cumulative count of failed pipeline runs.  
Killed pipeline runs | Cumulative count of killed pipeline runs.  
Rejected pipeline runs | Cumulative count of rejected pipeline runs.  
Successful pipeline run time | Time taken for successful pipeline runs to complete.  
Pipeline start latency | Time taken for a pipeline run to reach a "Running" state.  
Managed Service for Apache Spark provisioning latency | Time taken to provision the Managed Service for Apache Spark cluster.  
Managed Service for Apache Spark API request count | Cumulative count of API requests made to Managed Service for Apache Spark.  
Successful preview run time | Time taken for successful preview runs to complete.  
Preview runs | Number of preview runs.  
Pipeline bytes read | Cumulative count of bytes read by a pipeline.  
Pipeline bytes written | Cumulative count of bytes written by a pipeline.  
Pipeline bytes shuffled | Cumulative count of bytes shuffled in a pipeline.  
Plugin records processed in | Cumulative count of records entering a plugin.  
Plugin records processed out | Cumulative count of records exiting a plugin.  
  
#### Instance view widgets

This table describes the widgets in the **Instance** view:

Widget | Description  
---|---  
Concurrent pipelines running | Number of pipelines running concurrently.  
Concurrent pipelines launched | Number of pipelines in a provisioning or starting state.  
API requests received | Cumulative count of API requests received.  
API responses count | Cumulative count of API responses sent.  
Authorization check count | Cumulative count of authorization checks.  
Authorization check time | Latency of authorization checks.  
Deployed pipeline count | Number of deployed pipelines.  
Draft pipeline count | Number of draft pipelines.  
Namespace count | Number of namespaces.  
  
## View metrics for advanced analysis in Cloud Monitoring

For additional filtering and aggregation options, view your metrics in Cloud Monitoring:

  1. In the Google Cloud console, go to the Cloud Monitoring **Metrics explorer** page.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. Select the **Cloud Data Fusion** monitored resource.

  3. Choose a metric.

  4. Select filters and aggregation.




## What's next

  * To learn about filters and metrics, see the [Cloud Data Fusion metrics overview](https://docs.cloud.google.com/data-fusion/docs/concepts/metrics-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
