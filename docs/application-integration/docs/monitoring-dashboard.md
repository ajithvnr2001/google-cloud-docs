---
url: https://docs.cloud.google.com/application-integration/docs/monitoring-dashboard/
title: Use Application Integration dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:28.919914+00:00
---

# Use Application Integration dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/monitoring-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use Application Integration dashboard

The **Monitoring** page in Application Integration provides a predefined monitoring dashboard to view some of the key performance and usage metrics of your integrations in your Google Cloud project. All the metrics presented in the predefined dashboard are ingested from [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). 

Using the **Monitoring** page, you can: 

  * View and monitor key performance and usage metrics, both at an integration level and at a project level.
  * Analyze historical performance.
  * Filter the metrics based on the available attributes.
  * Display metrics for a specific time duration.
  * Create customized metric dashboards.



##  Use the predefined dashboard 

The predefined dashboard contains a set of curated widgets and charts to help you get a comprehensive view of your integration performance and data usage. For information about how to customize the predefined dashboard, see Customize dashboard.

To view the predefined dashboard, do the following: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Monitoring**. 
  3. In the **Monitoring** page, click the **Dashboard** drop-down menu and select **Predefined**. 

The predefined dashboard apperas displaying the predefined charts.




###  Predefined charts 

You can view the following widgets and charts in the predefined dashboard:

Charts category  | Chart Name  | Description   
---|---|---  
**Integration Performance** | **Successful executions (per hour)** | Number of successful integration executions per hour.   
**Execution failures (per minute)** | Number of integration execution failures per minute.   
**Average integration execution time (per hour)** | The average time, in milliseconds (ms), it takes an integration to complete an execution. Execution latencies are calculated by the minute.   
**Step (Trigger/Task) Performance** | **Successful step executions (per hour)** | Number of successful step (task/trigger) executions per hour.   
**Task execution failures (per minute)** | Number of unsuccessful task executions per minute.   
**Average task execution time (per hour)** | The average time, in milliseconds (ms), it takes a task to complete an execution. Task execution latencies are calculated by the minute.   
**Data Processed** | **Data processed by integration executions (per hour)** | The amount of data processed during integration executions.   
  
The following image shows a sample predefined dashboard:

![Monitoring dashboard page](https://docs.cloud.google.com/static/application-integration/images/monitoring-dashboard-ipsa.png)![Monitoring dashboard page](https://docs.cloud.google.com/static/application-integration/images/monitoring-dashboard-ipsa.png)

## Customized dashboards

To customize the default predefined deashboard in Application Integration, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration > Monitoring** page. 

[Go to Monitoring](https://console.cloud.google.com/integrations)

  2. Click **Customize dashboard**. 

You are redirected to the **Cloud Monitoring > Dashboards** page that is pre-populated with the predefined widgets and charts from Application Integration.

  3. Customized your dashboard using the available charts and widgets in the **Chart library**.
  4. Click **Save**.

Once saved, the customized dashboard is exported to Application Integration. To view your customized dashboard, go back to the **Application Integration >**Application Integration>Monitoring page, click the **Dashboard** drop-down menu and select **Customized**.




## View metrics in Metrics Explorer

To view any of the metric charts in the Cloud Monitoring [Metric Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), go to the desired chart, click  more_vert  (Actions menu) and select **View in Metrics Explorer**. 

Using the Metric Explorer, you can build temporary metric charts to visualize the available resource metrics for your Google Cloud project. Once you have created a metric chart, if desired, you can also save it to a custom monitoring dashboard. 

You can also select filters, group by metric labels, perform aggregations, and select chart viewing options using the Metric Explorer. For more information, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). 

## Filters and time range

The **Monitoring** page let's you to filter the metrics based on one or more of the following attributes: 

  * **Region:** Region of the integration.
  * **Integration Name:** Name of the integration.
  * **Integration Version:** Version of the integration.



You can configure the dashboard to display metrics for a specific time range. For example, you can choose to view the metrics gathered in the past few hours, days, or a custom time period. 

To configure the time range, you can either select the specific time periods such as **last 30 minutes** , **last 1 hour** or **last 6 hours** , or you click the **Custom** drop-down and select the required time value, and click **Apply**. 

## Considerations

  * Monitoring metrics are generated only for published integrations.
  * _Step execution count_ metrics won't be computed for tasks that are skipped during the execution of an integration.
  * All the performance metric data that is diaplayed in the Monitoring dashboards are for informational purpose only. The aggregated performance metric data might not be 100% accurate.
  * Cloud Monitoring metric values must not be used to calculate billing costs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
