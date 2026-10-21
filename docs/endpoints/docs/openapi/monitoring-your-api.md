---
url: https://docs.cloud.google.com/endpoints/docs/openapi/monitoring-your-api/
title: Monitoring your API \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:24.649690+00:00
---

# Monitoring your API  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/monitoring-your-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Monitoring your API Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/monitoring-your-api "View this page for the Cloud Endpoints gRPC docs")

This page describes how you can monitor the health of APIs you own by using the logs and metrics Cloud Endpoints maintains for you automatically. When users make requests to your API, Endpoints logs information about the requests and responses. Endpoints also tracks three of the [four golden signals of monitoring](https://landing.google.com/sre/book/chapters/monitoring-distributed-systems.html#xref_monitoring_golden-signals): latency, traffic, and errors. These usage and performance metrics help you monitor your API.

## Before you begin

You must deploy your API and send requests to it in order to generate logs and metrics for viewing. If you don't have anything set up yet, try the [Endpoints quickstart](https://docs.cloud.google.com/endpoints/docs/deploy-api).

## API overview

When you are debugging an issue with your service or just want to ensure that everything is running fine, go to your API's overview:

  1. In the Google Cloud console, go to the **Endpoints** > **Services** page for your project:

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  2. If you have more than one API, click the one you want to monitor.

  3. Ensure you are on the **Overview** tab.




### Graphs

At the top are graphs for some of the metrics, so you can spot any spikes and drops right away. You can:

  * In the top-right of the first graph, use the **Select graphs** drop-down list to show graphs for metrics you are interested in, and remove the ones you don't want to view. Each entry in the drop-down list has a question-mark that you can hold your pointer over to to see a description of the metric it displays.

  * In the top-right corner of the overview, adjust the graphs by selecting from the various time spans. This adjusts the time range of values displayed in these graphs, which also alters the point granularity.




### Methods table

When you are ready to drill down further, scroll below the graphs for a table with metrics for individual methods in your API. You can:

  * In the top-right of the table, use the **Select columns** drop-down list to show the metrics you are interested in and remove the ones you don't want displayed. Entries here also have the question-mark that you can hold your pointer over to see a description.

  * In the top-right corner of the overview, select a time span for the metric values in the table by using the time span picker. This picks a time span for both the graphs and the table.




### Logs

When you spot an issue in the metrics, go to the **Logs Explorer** page in the Google Cloud console to see logs of the requests and responses for your API.

  * To see logs for individual methods of your API, in the table click **View logs**.

  * To see logs for all methods in your API, in the bottom-right corner click **View all logs**.

  * To locate Endpoints logs directly from the Logs Explorer page:

    1. In the Google Cloud console, go to the **Stackdriver** > **Logging** page:

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

    2. Select **Produced API,` SERVICE_NAME`**, where `SERVICE_NAME` is the name of the Endpoints service.




See the [Endpoints logs reference](https://docs.cloud.google.com/endpoints/docs/openapi/ref-endpoints-logs) for details on the structure of the logs in the Logs Explorer.

Learn what else you can do with the logs:

  * Get started using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

Build queries to specify the set of log entries that you want to view, such as getting all requests with a latency greater than 300 milliseconds.

  * [Configure and manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) to route your logs to supported destinations This lets you stream logs to BigQuery for further analysis, save the raw logs to Cloud Storage, or send them to Pub/Sub messaging topics.




### Filter for a specific consumer project

**Alpha**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To see metrics for a specific consumer project, your API consumers must send an API key when making a request. Because Endpoints uses the API key to identify the project that the calling application is associated with, the API key must have been created in the API consumer's Google Cloud project. To learn how to restrict access to your API by using an API key, see [Restricting API access with API keys](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys). 

To filter metrics for a specific consumer project:

  1. Get the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the API consumer's project. If you don't have permission to access the API consumer's project, ask someone who has permission to get the project number for you.

  2. In the Google Cloud console, go to the **Endpoints** > **Services** page for your project.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  3. In the top-left corner of the **Overview** page, enter the project number in the **Filter by Project Number** field.

  4. Click **Filter**.




The metrics on the page update to reflect traffic only from the specified project.

## Alerting

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Metrics collected by Endpoints are also available in Cloud Monitoring. You can use Monitoring to set up alerting on latency, traffic, and errors. The only [golden signal](https://landing.google.com/sre/book/chapters/monitoring-distributed-systems.html#xref_monitoring_golden-signals) that you cannot set up an alert for using Endpoints metrics is saturation. The metrics that you need to monitor for saturation depend on your application. See the list of [metrics](https://docs.cloud.google.com/monitoring/api/metrics) available in Cloud Monitoring for metrics that you can use to set up alerting on saturation.

To set up alerting:

  1. In the Google Cloud console, select the Google Cloud project with your Endpoints monitored API which is associated with the account.

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. By using the navigation pane, select **Monitoring**.

  3. Create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts) to set up alerts for the [golden signals](https://landing.google.com/sre/book/chapters/monitoring-distributed-systems.html#xref_monitoring_golden-signals) by using the following:

     * Latency

       1. For **Condition Type** , enter `Metric Threshold`.
       2. For **Resource Type** , enter `Produced API`.
       3. For the metric, enter `Request latencies`.
       4. Enter the threshold you want to alert on and follow the rest of the [Alerts guide](https://docs.cloud.google.com/monitoring/alerts).
     * Traffic

       1. For **Condition Type** , enter `Metric Threshold`.
       2. For **Resource Type** , enter `Produced API`.
       3. For the metric, enter `Request count`.
       4. Enter the threshold you want to alert on and follow the rest of the [Alerts guide](https://docs.cloud.google.com/monitoring/alerts).
     * Errors

       1. For **Condition Type** , enter `Metric Threshold`.
       2. For **Resource Type** , enter `Produced API`.
       3. For the metric, enter `Request count`.
       4. For response-code-class, enter `5xx`.
       5. Enter the threshold you want to alert on and follow the rest of the [Alerts guide](https://docs.cloud.google.com/monitoring/alerts).

**Note:** If your API hasn't logged a 5xx response yet, the alerting policy form doesn't offer it as a response-code-class.**Note:** If the critical constraint for your service is network IO, you might be able to use one of the Endpoints's metrics to set up an alert. All Endpoints logs are under the **Resource Type** of `Produced API`.

## What's next

  * [Endpoints logs](https://docs.cloud.google.com/endpoints/docs/openapi/ref-endpoints-logs)
  * [Endpoints metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
