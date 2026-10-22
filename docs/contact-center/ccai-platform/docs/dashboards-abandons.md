---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-abandons/
title: Abandons dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:44.871360+00:00
---

# Abandons dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-abandons/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Abandons dashboards Stay organized with collections  Save and categorize content based on your preferences. 

With the **Abandons - Calls** and **Abandons - Chats** dashboards, get insights into abandons that occur for calls and chats, including the number and type of abandons.

An abandon occurs when a contact disconnects during their customer journey. An end-user might disconnect while navigating IVR menus if the menus are confusing or take too much time. An end-user might disconnect while waiting in a queue if the wait time is too long. To reduce the number of abandons, consider offering a call back number or providing estimated wait times.

## Use the dashboards

To use the dashboards, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **Abandons / Calls** or **Abandons / Chats**. The dashboard appears.

  3. Click the **Date** field to select a date range, and then do one of the following:

     * Select a preset data range. To do this follow these steps:

       1. Click expand_more **More** to view all of the preset date ranges.

       2. Click the date range that you want.

     * Select a custom range. To do this, follow these steps:

       1. Click **Custom**.

       2. In the **Custom** field, enter a start and end date for your date range. You can type your date range or click ![Click the calendar icon to see the
calendar.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-calendar.png)**Open calendar** to select start and end dates.

**Note:** The maximum date range that you can specify is 45 days. If you specify a date range of more than 45 days, the dashboard returns an error. 
  4. Filter your results using the following fields:

     * **Queue Group** : by queue group

     * **Queue Name** : by queue name

     * **Language** : by the language assigned to the queue

     * **Interaction Type** : by the type of interaction

     * **Start Time** and **End Time** : get results from only within this time range

     * **Queue Abandon Time** and **Total IVR Abandon Time** : by when abandons occurred

     * **Customer ANI** : by the end-user's ANI

  5. In the **Time Format** field, set the time format.

  6. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

These dashboards contain the following metrics tiles:

  * **Total IVR Abandons** : the number of interactions that abandoned before selecting and entering a queue

  * **Avg IVR Abandon Time** : the average of time across all interactions where contacts were in the IVR before disconnecting the interaction

  * **Total Queue Abandons** : the number of interactions that were waiting in queue and were disconnected by the caller before being accepted by an agent

  * **Avg Queue Abandon Time** : the average amount of time that calls or chats waited in a queue before disconnecting without being accepted by an agent

  * **Total Queue Interactions** : the number of all inbound interactions that have entered a queue, this number includes all transfers, escalations, and deflections to another queue

  * **Total Inbound Handled** : the number of inbound calls or Chat interactions that were handled by an agent

  * **Total Failed Interactions** : the number of calls or chats that were not successfully connected to an agent or representative




## Tables

These dashboards contain the following metrics tables. Hold the pointer over a table heading to see its description.

  * **Queue Abandon Summary** : displays in table format the results for queue abandons and the queue in which they are associated with

  * **Queue Abandons by 30 Min Interval** : a visualization showing queue abandons in 30-minute intervals for a single day. If multiple days are selected in the filter, the data will display by day, with an option to view interval details.

  * **Queue Abandon Details** : all of the queue abandons that occurred within the timeframe you apply by the filter

  * **IVR abandons by 30 Min Interval** : an interval chart for IVR Abandons by 30-minute intervals for a single day. If multiple days are selected in the filter, the data displays by day, with an option to drill down into all interval details.

  * **IVR Abandon Details** : all interactions that abandoned during the IVR phase




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
