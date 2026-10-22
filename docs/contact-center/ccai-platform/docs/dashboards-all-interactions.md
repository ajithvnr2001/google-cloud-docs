---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-all-interactions/
title: All interactions dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:46.778654+00:00
---

# All interactions dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-all-interactions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  All interactions dashboards Stay organized with collections  Save and categorize content based on your preferences. 

With the **All Interactions - Calls** and **All Interactions - Chats** dashboards, see data on a wide variety of interaction types for calls and chats.

## Use the dashboards

To use the dashboards, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **All Interactions / Calls** or **All Interactions / Chats**. The dashboard appears.

  3. Click the **Date** field to select a date range, and then do one of the following:

     * Select a preset date range. To do this, follow these steps:

       1. Click expand_more **More** to view all of the preset date ranges.

       2. Click the date range that you want.

     * Select a custom range. To do this, follow these steps:

       1. Click **Custom**.

       2. In the **Custom** field, enter a start and end date for your date range. You can type your date range or click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-calendar.png)**Open calendar** to select start and end dates.

**Note:** The maximum date range that you can specify is 45 days. If you specify a date range of more than 45 days, the dashboard returns an error. 
  4. Filter your results using the following fields:

     * **Start Time** and **End Time** : get results from only within this time range

     * **Queue Name** : filter by queue name

     * **Queue Group** : filter by queue group

     * **Call ID** (calls only): filter by call ID

     * **Chat ID** (chats only): filter by chat ID

     * **Call Type** (calls only): filter by call type

     * **Chat Type** (chats only): filter by chat type

     * **Location** : filter by one or multiple locations

     * **Language** : filter by the language assigned to the queue

     * **Direction** : filter by the direction of the session

     * **Queue Time** , **Abandon Time** , **Talk Time** (calls only), **Chat Time** (chats only), **Hold Time** (calls only), and **Wrap-up Time** : filter by a specified duration of different phases of the session

     * **Support Phone Number** (calls only): filter by the public support phone number assigned to the queue. This is for inbound interactions only.

     * **Outbound Number** (calls only): filter by the outbound phone number

     * **Customer Phone Number** (calls only): filter by the phone number that the end-user used to call in

     * **Failed Interaction** : filter by whether or not the session failed

     * **Failed Reason** : filter by the reason that the session failed

     * **Failed Interaction** Filter by whether or not the session failed

     * **Failed Reason** : filter by the reason that the session failed.

  5. Click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Reload**.




## Tiles

These dashboards contain the following metrics tiles:

  * **SLA %** : the percentage of interactions that were queued and answered within the thresholds set up for each queue as configured in the portal. The data displayed is the overall aggregated data.

  * **Total Handled** : the total number of inbound and outbound interactions that were answered

  * **Total Inbound Handled** : the total number of inbound interactions handled.

  * **Total Outbound Handled** : the total number of outbound interactions handled.

  * **Total Queue Abandons** : the total number of interactions that joined a queue but were abandoned before being connected to an agent

  * **Avg Queue Abandon Time** : the average amount of time that an end-user waited in queue before abandoning the session

  * **Avg Queue Time** : the average queue time that an end-user waited in a queue prior to connecting with an agent

  * **ASA** : the average time that contacts waited in a queue before being connected to an agent. The calculation is only based on interactions that were handled and does not consider abandons.

  * **Avg Talk Time** or **Avg Chat Time** : the average time an agent actively talked or chatted across all interactions

  * **Avg Hold Time** : the average across all interactions where an agent placed the contact on hold. This is only available for calls.

  * **Avg Handle Time** : the average time elapsed from when an agent was assigned a **Call** or **Chat** , to when they ended the wrap-up phase. For

**Calls** , this is the sum of the talk time, hold time, and wrap up time. For **Chats** , this is the sum of the chat time and wrap up time.

  * **CSAT** : the end-user satisfaction awarded to the session. If there are transfers, this is only available on the final interaction

  * **Max Concurrent Accepts** : the maximum number of interactions that were accepted during the date or time threshold applied by the filters

  * **Voicemails Received** : the number of voicemails received

  * **Voicemails Handled** : the number of voicemails assigned to an agent

  * **SLA by 30 minute interval** : shows SLA achievements in 30-minute intervals for a single day. If multiple days are selected, the intervals adjust to display daily results.




## Tables

These dashboards contain the following metrics tables. Hold the pointer over a column heading to see its description.

  * **IVR Interactions** (calls only): information about IVR calls.

  * **Call Metrics Detail** (calls only): information about calls of all types.

  * **Chat Metric Detail** (chats only): information about chats of all types. If you configure chat transcript storage for your CRM, the values in the **Chat ID** column become links to the chat transcripts.

  * **Virtual Agent Interactions** (calls only): information about virtual agent calls.

  * **Virtual Agent Chats** (chats only): information about virtual agent chats.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
