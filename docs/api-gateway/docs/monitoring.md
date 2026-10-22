---
url: https://docs.cloud.google.com/api-gateway/docs/monitoring/
title: Monitoring your API \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:37.280528+00:00
---

# Monitoring your API  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitoring your API

This page describes how you can monitor the health of your API Gateway APIs using the logs and metrics that API Gateway maintains for you automatically.

When you create an API, API Gateway automatically creates a corresponding [managed service](https://docs.cloud.google.com/service-infrastructure/docs/overview#creating_apis_and_services). The name of the managed service created can be found in the output of the following command:
    
    
    gcloud api-gateway apis describe API_ID

The name of your service is the value of the `managedService` field.

When users make requests to your API, API Gateway logs information about the requests and responses. API Gateway also tracks three of the [four golden signals of monitoring](https://landing.google.com/sre/book/chapters/monitoring-distributed-systems.html#xref_monitoring_golden-signals): latency, traffic, and errors. These usage and performance metrics help you monitor your API.

## Before you begin

To generate logs and metrics for viewing, deploy an API and send requests to it. If you have not created and deployed an API to a gateway yet, try the [API Gateway quickstart](https://docs.cloud.google.com/api-gateway/docs/quickstart).

## API overview

When you are debugging an issue with your service or just want to ensure that everything is running as expected, go to your API's overview:

  1. In the Google Cloud console, go to the **API Gateway** > **APIs** page for your project:

[Go to APIs](https://console.cloud.google.com/api-gateway/api)

  2. If you have more than one API, click the one you want to monitor.

  3. Ensure you are on the **Overview** tab.




### Graphs

The overview page provides a number of graphs for some of the metrics, so you can spot any spikes, drops, or unexpected activity right away. Using the filters at the top of the page, you can:

  * Use the **Select graphs** drop-down list to show graphs for metrics you are interested in, and remove the ones you don't want to view.
  * Adjust the scope of the graphs by selecting from the various time spans. This adjusts the time range of values displayed, which also alters the point granularity.



### Methods table

When you are ready to drill down further, scroll below the graphs for a table with metrics for individual methods in your API. You can:

  * In the top-left corner of the table, click the **Filter Table** icon to select refined filter query options from the drop-down table. Add an `OR` between each filter query to search for multiple terms.
  * In the top-right corner of the table, click the **Column Display Options** icon to display a drop-down list. Check the metrics you are interested in and clear the ones you don't want displayed.
  * In the top-right corner of the **Overview** page, select a time span for the metric values in the table by using the time span picker. This picks a time span for both the graphs and the table.



### Metrics

To monitor your gateway, execute the following steps: 

  1. In the Google Cloud console, go to the **Monitoring > Metrics explorer** page.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. In the **Metric Query Builder** pane, click the **Select a metric** menu.
  3. In the **Filter** field, enter **API Gateway > Proxy > Request Count**.
  4. Click **Apply**.



This query results in data for all gateways in the current project. This data may be grouped by:

  * `location`: The region in which the Gateway is running.
  * `gateway_id`: The ID of the Gateway.
  * `response_code_class`: HTTP response code class (1xx, 2xx, 3xx, 4xx, 5xx).
  * `api_config`: The name of API Config resource hosted by the Gateway.



The chart on the **Metrics Explorer** page automatically updates to match the given query. To save the chart, click **Save As** and specify the dashboard to save it (or create a new dashboard).

### Logs

When you spot an issue in the metrics, you can use the **Logs Explorer** page in the Google Cloud console to see logs of the requests and responses for your API.

  * To see logs for individual methods of your API, in the table click **View logs**.

  * To see logs for all methods in your API, in the bottom-right corner click [**View all logs**](https://console.cloud.google.com/logs/query).

  * To locate API Gateway logs directly from the Logs Explorer page:

    1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer ](https://console.cloud.google.com/logs/query)

    2. Click **All resources**.

    3. Select **API Gateway,` LOCATION`**, and **`GATEWAY_ID`**. Where `LOCATION` is the region where your API Gateway instance is deployed, and `GATEWAY_ID` is the name of your API Gateway instance.

    4. Click **Apply**.




See the [API Gateway logs reference](https://docs.cloud.google.com/api-gateway/docs/platform-logging) for details on the structure of the logs in the Logs Explorer.

Learn what else you can do with the logs:

  * Get started using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

Use the query pane to specify the set of log entries that you want to view, such as getting all requests with a latency greater than 300 milliseconds.

  * [Configure and manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2). This lets you stream logs to BigQuery for further analysis, save the raw logs to Cloud Storage, or send them to Pub/Sub messaging topics.




### Filter for a specific consumer project

To filter metrics for a specific consumer project:

  1. Get the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the API consumer's project. If you don't have permission to access the API consumer's project, ask someone who has permission to get the project number for you.

  2. In the Google Cloud console, go to the **API Gateway** > **APIs** page for your project.

[Go to APIs](https://console.cloud.google.com/api-gateway/api)

  3. In the top-left corner of the **Overview** page, enter the project number in the **Filter by Project Number** field.

  4. Click **Filter**.




The metrics on the page update to reflect traffic only from the specified project.

## What's next

  * [Tracing your API](https://docs.cloud.google.com/api-gateway/docs/tracing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
