---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-interval/
title: Queue Interval dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:26.234193+00:00
---

# Queue Interval dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-interval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue Interval dashboards Stay organized with collections  Save and categorize content based on your preferences. 

With the **Queue Interval Dashboard Calls** and **Queue Interval Dashboard Chats** dashboards, see how successfully queues are meeting service level agreement (SLA) targets over 30-minute intervals for a full day. See the total number of calls handled, handle times, and abandoned contacts by interval.

You can do trend analysis by regularly exporting and monitoring data to verify that SLAs are being met. Where queues are exceeding SLAs, you can consider allowing agents go offline to perform other tasks, for example.

## Use the dashboards

To use the dashboards, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **Queue Interval / Calls** or **Queue Interval / Chats**. The dashboard appears.

  3. Click the **Date** field to select a date range, and then do one of the following:

     * Select a preset date range. To do this, follow these steps:

       1. Click expand_more **More** to view all of the preset date ranges.

       2. Click the date range that you want.

     * Select a custom range. To do this, follow these steps:

       1. Click **Custom**.

       2. In the **Custom** field, enter a start and end date for your date range. You can type your date range or click ![Click the calendar icon to see the
calendar.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-calendar.png)**Open calendar** to select start and end dates.

**Note:** The maximum date range that you can specify is 45 days. If you specify a date range of more than 45 days, the dashboard returns an error. 
  4. Filter your results using the following fields:

     * **Start Time** and **End Time**. Filter results to this time range.

     * **Queue**. Filter by queue.

     * **Queue Group**. Filter by queue group.

     * **Interaction Type**. Filter by one or more interaction types.

     * **Direction**. Filter by interaction direction.

     * **Location**. Filter by one or more locations.

  5. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

These dashboards contain the following metrics tiles:

  * **SLA by Interval** : Displays the percentage of interactions that were in SLA, by interval. When you filter for a single day, each bar represents a 30-minute interval. When you filter for multiple days, each bar represents one day. Click a bar to display the **SLA by Interval** table for that interval.

  * **Service Level** : Displays the percentage of interactions that were in and out of SLA.

  * **In SLA** : Displays the number of interactions that were in SLA.

  * **Out SLA** : Displays the number of interactions that were out of SLA.

  * **Queue Interactions Versus Queue Abandons by Interval** : Displays the total number of interactions that entered a queue versus the number of queue abandons. When you filter for a single day, each bar represents a 30-minute interval. When you filter for multiple days, each bar represents one day.

  * **Handled Interactions by Interval** : Displays the total handled interactions by interval. When you filter for a single day, each bar represents a 30-minute interval. When you filter for multiple days, each bar represents one day.




## Table

These dashboards contain the following metrics table. Hold the pointer over a table heading to see its description.

  * **Queue Interval Metrics** : Data about queue interval performance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
