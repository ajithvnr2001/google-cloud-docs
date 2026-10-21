---
url: https://docs.cloud.google.com/apigee/docs/api-monitoring/investigate/
title: Using the Investigate view \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:44:01.612255+00:00
---

# Using the Investigate view  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-monitoring/investigate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using the Investigate view Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The API Monitoring Investigate view displays pivot tables of metrics and attributes for all API traffic, to help you compare activity for different metrics.

To access the Investigate view, follow the steps in [Accessing API Monitoring](https://docs.cloud.google.com/apigee/docs/api-monitoring#accessing_api_monitoring) and select **Investigate**.

![Select investigate view.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/select-investigate.png)

The figure below shows the UI with **Investigate** selected.

![API Monitoring investigate view](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/investigate.png)

By default, the Investigate view displays three tables:

  * Fault Code by Time
  * Fault Code by Status Code
  * Fault Source by Proxy



As in the [Timeline view](https://docs.cloud.google.com/apigee/docs/api-monitoring/timeline#timeline), you can select any combination of tables from the **Graphs** menu to display. All other [graph options](https://docs.cloud.google.com/apigee/docs/api-monitoring/timeline#graph_options_for_all_views) are the same as in the Timeline view.

Each cell in a table shows the number of responses for a subset of the data. As an example, take a look at the first three columns of the **Fault Code by Time** table.

![Fault code by time table.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/fault-code-by-time.png)

The first cell in row 1 shows the number of responses (`444`) with fault code `steps.json2xml.SourceUnavailable` that were returned from `18:18 - 18:24`, on the selected date.

The first cell in row 2 shows the numbers of responses (`64`) during the same time interval for which the fault code was not set for some reason.

To learn about this particular fault code, see [JSON to XML policy runtime error troubleshooting](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsontoxml-runtime-errors).

### 2xx status codes

Requests that return a 2xx status code were successfully received and understood. Normally, most requests will return a 2xx status code. If you are primarily interested in viewing data for unsuccessful requests, you might want to restrict the displayed data to requests with status codes other than 2xx, to make the data easier to interpret. To do so, toggle the **Show 2xx Status Code** button, at the top-right of the Investigate view, to the left (off) position.

![Show 2xx Status Code button.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/show-2xx-status-code.png)

With this setting, the Investigate view only displays data from requests with response codes different from 2xx.

### Viewing the distribution of cell data

You can get a more granular view of the data for an individual table cell by clicking the cell. This displays the distribution of the cell data by several different attributes.

To see an example of this, first select **Region** in the **Graphs** menu to display the table shown below.

![Region by time table.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/investigate-region.png)

In the data for this example, there is just one region, `us-central1`. If there were data for other regions, you would see additional rows in the table.

Now, click the first cell in the table.

![Click first cell in region by time table.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/investigate-region-click-cell.png)

This displays several tables in the right-hand pane of the Investigate view. The first table is shown below.

![Distribution tables](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/distribution-tables.png)

The top of the pane displays the conditions that specify the cell data, in this case the region and time interval.

Below that, the table "Distribution by Fault Code" displays the number of responses for each fault code in the data. In this example, there are just two fault code values:

Fault code | Count  
---|---  
`steps.json2xml.SourceUnavailable` | `432`  
`not set` | `64`  
  
The counts for the fault codes add up to `496`, the total count in the cell.

**Note:** If you select a table cell in the main section whose attribute is `not set`, the right-hand pane displays data for all cells in the column (or row if the table is pivoted) for the selected cell. In that case, the sum of the values in a distribution table does not necessarily equal the value in the selected cell.

As another example, scroll down in the right-hand pane until you reach the table labeled "Distribution by Status Code," as shown below.

![Distribution tables](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/distribution-status-code.png)

In this case, there are two status codes in the data:

  * `500`: `432`
  * `200`: `64`

Status code | Count  
---|---  
`500` | `432`  
`200` | `64`  
  
Again, the counts add up to `496`.

## Using the Investigate view to diagnose an issue

You can use the Investigate view to diagnose API issues For example, suppose you receive an alert that indicates that the 5xx error rate exceeds the specified threshold. To investigate this issue, you might perform the following tasks in the Investigate view:

  * View the **FAULT CODE BY TIME** table to view the fault code activity over the last hour.
  * View the **FAULT CODE BY STATUS CODE** table to identify specific HTTP status codes associated with the fault codes whose counts have increased over the last hour, as identified in the previous step.
  * View the **FAULT CODE BY PROXY** matrix to identify the API proxies that are triggering the fault codes identified in the previous step.
  * [Set up an alert](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications) to further assist you with diagnosing the issue.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
