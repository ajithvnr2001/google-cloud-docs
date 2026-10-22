---
url: https://docs.cloud.google.com/datastore/docs/use-monitoring-dashboard/
title: Use the Cloud Monitoring dashboard \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:26.347089+00:00
---

# Use the Cloud Monitoring dashboard  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/use-monitoring-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Use the Cloud Monitoring dashboard Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Cloud Monitoring dashboard to view the available metrics, create a custom dashboard, and set alerts.

## View Firestore in Datastore mode metrics

To view the different Firestore in Datastore mode metrics and create charts, use the Metrics explorer within Cloud Monitoring in the Google Cloud console. For more information about creating charts, see [Create charts with Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

## Set up a Cloud Monitoring dashboard

In Cloud Monitoring, custom dashboards allow you to display information that is relevant to you in an organized way. For example, you might create a dashboard to display the performance metrics and alerting policies for your project in your production environment.

For more information about setting up a custom dashboard, see [Manage custom dashboard](https://cloud.google.com/monitoring/charts/dashboards) and [Add dashboard widgets](https://cloud.google.com/monitoring/charts).

#### Monitor error rates

You can create a monitoring dashboard to monitor error rates and ensure availability of your database. Availability refers to the rate at which your database responds within an expected timeframe with a successful status code. The [Firestore in Datastore mode SLA](https://cloud.google.com/firestore/sla) defines the specific details of what is classified as a valid request.

The error rate is determined by dividing the number of requests that resulted in an error response by the total number of requests sent.

An example dashboard for calculating error rates can be created by calculating the A/B ratio for `api/request_count` of valid requests with `4xx` or `5xx` error codes contrasted with the `api/request_count` of all valid requests.

[ ![ Understand availability with error rate](https://docs.cloud.google.com/static/firestore/native/docs/images/cloudmon-error-rate.png)](https://docs.cloud.google.com/static/firestore/native/docs/images/cloudmon-error-rate.png) **Figure 1.** Understand availability with error rate.

In **Figure 1** , you can see how to visualize the error rate ratio using the **api/request_count** metrics in the Metrics explorer.

## Create an alerting policy

Cloud Monitoring lets you create [alerts](https://cloud.google.com/monitoring/alerts) to notify you when a change in a metric condition occurs. You can use these alerts to be notified of potential problems before they impact your users.

For more information about creating alerts, see [Create metric-threshold alerting policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui).

Consider the following example where we create a latency alert policy. The alerting policy checks p99 latency over a 5 minute rolling window. If the p99 latency stays higher than 250ms for 5 minutes, the alert is triggered.

### Console

  1. In the Google Cloud console, go to the **Monitoring** page then select _notifications_ **Alerting**.

[Go to Monitoring](https://console.cloud.google.com/monitoring/alerting)

  2. Select **Create policy**.

  3. Select the **Request Latencies** metric from the **Consumed API** resource.

  4. Add a service filter for `datastore.googleapis.com`. The `api/request_latencies` metric is monitored over the 5 min rolling window.

[ ![Select the api/request_latencies metric to create a trigger.](https://docs.cloud.google.com/static/firestore/native/docs/images/cloudmon-dashboard-latencies.png)](https://docs.cloud.google.com/static/firestore/native/docs/images/cloudmon-dashboard-latencies.png) **Figure 2.** Select the api/request_latencies metric to create a trigger.
  5. Click **Next** to configure the trigger.

  6. Select the **Condition Types** as **Threshold**.

A threshold condition is set to a threshold value of 250ms. An alert is triggered when the p99 latency value stays the same for the entire period of the rolling window (5 min).

[ ![Add the threshold for the metric.](https://docs.cloud.google.com/static/firestore/native/docs/images/cloudmon-dashboard-alerts.png)](https://docs.cloud.google.com/static/firestore/native/docs/images/cloudmon-dashboard-alerts.png) **Figure 3.** Add the threshold for the metric.
  7. Set the **Threshold value** as **250**.

  8. Click **Next** to configure notifications.

  9. Set the alert policy name and click **Next**.

  10. Review the alert configurations and click **Create Policy**.




### PromQL

You can implement the same latency alert policy using a [Prometheus Query Language](https://docs.cloud.google.com/monitoring/promql) (PromQL) query.
    
    
      histogram_quantile(0.99,
        rate({
          "__name__"="serviceruntime.googleapis.com/api/request_latencies_bucket",
          "monitored_resource"="consumed_api",
          "service"="firestore.googleapis.com"
        }[5m])
      )
      > 0.25
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
