---
url: https://docs.cloud.google.com/apigee/docs/api-monitoring/recent/
title: Using the Recent view \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:04:33.990796+00:00
---

# Using the Recent view  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-monitoring/recent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using the Recent view Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The API Monitoring Recent view displays [treemaps](https://developers.google.com/chart/interactive/docs/gallery/treemap) of API traffic by proxy.

To access the Recent view, follow the steps in [Accessing API Monitoring](https://docs.cloud.google.com/apigee/docs/api-monitoring#accessing_api_monitoring) and select **Recent**.

![Select recent view.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/select-recent.png)

The figure below shows the UI with **Recent** selected.

![API Monitoring recent view](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/recent.png)

The Recent view shows three treemaps in which the API traffic for each proxy is displayed as a rectangle, whose size is proportional to the amount of traffic for that proxy. The color of the rectangle indicates the relative size of one of the following variables (depending on which treemap you are viewing):

  * Number of incidents triggered by [alerts](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications)
  * Error rate
  * Maximum latency 50th percentile



Note that if you ignore the colors of the rectangles, all three graphs display the same underlying pattern of rectangles. This is so because the size of each proxy's rectangle depends only on traffic, which is the same in all three graphs.

As an example, the second graph, **Proxy Error Rate by Proxy** , displays the relative sizes of the error rate for each proxy: the darker the rectangle, the greater the error rate. To see the value of the error rate for a proxy in the Apigee UI, move the cursor over the rectangle for the proxy. An example is shown below:

![Error rate for proxy18.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/proxy43-error-rate.png)

The text in the rectangle displays the following data for proxy43:

  * The total traffic: 760
  * The error rate: 0.48



Since the error rate for proxy43 is the largest among all proxies, its rectangle has the darkest shade of blue in the graph.

By default, the Recent view displays three tables:

  * **Incidents by Proxy**
  * **Proxy Error Rate by Proxy**
  * **Max Proxy Latency p50 (in ms) by Proxy**



As in the [Timeline view](https://docs.cloud.google.com/apigee/docs/api-monitoring/timeline#timeline), you can select any combination of tables from the **Graphs** menu to display. All other [graph options](https://docs.cloud.google.com/apigee/docs/api-monitoring/timeline#graph_options_for_all_views) are the same as in the Timeline view.

### Taking a closer look at the distribution of cell data

As in the Investigate view, you can get a more granular view of the data for an individual table cell by clicking the cell. This displays the distributions of the cell data by several different attributes in the right-hand panel. See [Viewing the distribution of cell data](https://docs.cloud.google.com/apigee/docs/api-monitoring/investigate#viewing_the_distribution_of_cell_data) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
