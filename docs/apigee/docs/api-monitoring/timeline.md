---
url: https://docs.cloud.google.com/apigee/docs/api-monitoring/timeline/
title: Using the Timeline view \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:07:48.510010+00:00
---

# Using the Timeline view  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-monitoring/timeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using the Timeline view Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The API Monitoring Timeline view displays timelines of recent API traffic, to help you diagnose and investigate issues.

To access the Timeline view, follow the steps in [Accessing API Monitoring](https://docs.cloud.google.com/apigee/docs/api-monitoring#accessing_api_monitoring) and select **Timeline**. 

![Select timeline view.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/select-timeline.png)

The figure below shows the UI with **Timeline** selected.

![API Monitoring timeline view](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/timeline.png)

The Timeline view displays following graphs:

  * **Proxy Total Traffic** : Numbers of requests during 1 minute intervals of the time range.
  * **Proxy Error Rate** : Total errors (4xx and 5xx) divided by the total traffic in each interval.
  * **Proxy Latencies Percentile** : Percentiles for API [latency](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/latency-analysis-dashboard). The graph shows the following percentiles: 50th (median) 90th, 95th, and 99th percentile.
  * **Target Total Traffic**
  * **Target Error Rate**
  * **Target Latencies Percentile**



Hover the mouse over any point in a graph to display the values at that point.

![Hovering over a timeline graph.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/timeline-graph-hover.png)

You can choose which graphs to display in the **Graphs** drop-down menu.

## Graph options for all views

The following graph options are available in all three views: Timeline, Investigate, and Recent:

  * **ALERT** : Click **ALERT** to set up [alerts and notifications](https://cloud.google.com/monitoring/alerts) for events, such as spikes in traffic or latencies.
  * **View** : Select one of the API Monitoring views:

    * Timeline (shown above)
    * Investigate
    * Recent
  * **Graphs** : Select the graphs to display from the drop-down list.

When you select the graphs, they are displayed in the order in which you selected them, starting with the most recently selected.

  * **Time range** : Select the length of the time range for the graphs.

![Select time range.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/timeline-time-range.png)

You can also turn on **Auto Refresh** to automatically refresh the data once every minute.

  * **Environment** : Select the [environment](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview) for the API.

  * **Region** (Timeline and Investigate views only): Select the API [region](https://cloud.google.com/compute/docs/regions-zones).

  * **Proxy** (Timeline and Investigate views only): Select the API [proxy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
