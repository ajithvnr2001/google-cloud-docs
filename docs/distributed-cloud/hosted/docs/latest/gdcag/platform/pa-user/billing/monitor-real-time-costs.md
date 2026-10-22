---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/monitor-real-time-costs/
title: Monitor real-time costs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:51.319850+00:00
---

# Monitor real-time costs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/monitor-real-time-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Monitor real-time costs Stay organized with collections  Save and categorize content based on your preferences. 

The Customer Real Time Cost dashboard helps you monitor real-time cost and resource usage for your infrastructure as it occurs. This dashboard displays active resource consumption and accumulated costs through line graph panels for costs and usage.

To get the permissions that you need to view the Customer Real Time Cost dashboard, ask your IAM Org Admin to grant you the corresponding project viewer role for the `platform-obs` project.

## Access the Customer Real Time Cost dashboard

Access the Customer Real Time Cost dashboard in the GDC console:

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Billing > Reports**. The **Billing reports** page opens. 
  3. In the **Real Time Cost** section, click **View in Dashboard** to open the Customer Real Time Cost dashboard. 



## Real Time Cost dashboard functionalities

The dashboard features the following primary visualization panels:

  * **Costs** : Line graph displaying the active cost incurred for your selected resources. You can view it in discrete or cumulative mode.
  * **Resource Usage** : Line graph displaying the active volume of resource consumption (such as vCPU, memory, or storage allocation) for your selected resources.



The time interval for the panels adjusts dynamically based on your selected time range: hourly for durations of 8 days or less, and daily for durations greater than 8 days.

## Filter real-time cost data

The following filters can be applied to the dashboard:

  * **Aggregation Level** : A drop-down list that lets you select the grouping level of the data. You can view costs aggregated by individual SKU, Product Family (such as Compute or Storage), Cloud Service Model (such as IaaS or PaaS) or the Total cost.
  * **Project Name** : A drop-down list that lets you select a specific project name to view. This drop-down defaults to **All**.
  * **SKU** : A drop-down list that lets you select which SKU to view. This drop-down defaults to **All**.
  * **Time Range** : User can pick any custom time range from the Grafana time picker. There are also some preset time periods (buttons) made available in the dashboard:

    * **Previous Billing Period**
    * **Current Billing Period**
    * **Year To Date**
    * **Last 7 Days**
    * **Current Day**



## Download dashboard data

You can download the underlying data from any line graph panel to a comma-separated values (CSV) file for external analysis. To download the data through Grafana, work through the following steps:

  1. Hover over the title of the line graph panel you want to export, and click the **⋮** icon.
  2. In the drop-down menu, select **Inspect > Data**. The data inspection drawer opens.
  3. In the data inspection drawer, click **Download CSV**. The CSV file downloads to your local system.

![Data inspection drawer highlight over Download CSV button](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/billing-download-csv.png)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
