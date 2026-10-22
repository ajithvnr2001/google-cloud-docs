---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-perf-overview/
title: Performance overview dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:38.559255+00:00
---

# Performance overview dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-perf-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Performance overview dashboard Stay organized with collections  Save and categorize content based on your preferences. 

With this dashboard, get high-level performance information for your channels. Quickly assess performance and identify potential issues that might require attention, such as SLA degradation or queue jams.

In graph tiles, hold the pointer over sections of the graph to get more information.

## Use the dashboard

To use the **Performance Overview Dashboard** , follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **Performance Overview / Calls & Chats**. The dashboard appears.

  3. Click the **Date** field to select a date range, and then do one of the following:

     * Select a preset date range. To do this, follow these steps:

       1. Click expand_more **More** to view all of the preset date ranges.

       2. Click the date range that you want.

     * Select a custom range. To do this, follow these steps:

       1. Click **Custom**.

       2. In the **Custom** field, enter a start and end date for your date range. You can type your date range or click ![Click the calendar icon to see the
calendar.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-calendar.png)**Open calendar** to select start and end dates.

**Note:** The maximum date range that you can specify is 45 days. If you specify a date range of more than 45 days, the dashboard returns an error. 
  4. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Calls

The **Calls** section contains the following metrics tiles:

  * **Total Handled Calls** : the number of calls handled

  * **Service Level - Calls** : the aggregated service level achieved for all call queues in your environment, as determined by the queue configuration

  * **Current Queued Now** : the total number of calls currently in the queue waiting to be assigned to an agent

  * **Current Max Queue Time** : the current wait time of the call that has been in the queue for the longest. If the queue is empty, this metric resets to zero.

  * **Avg Queue Time** : the average time a call spent in a queue until an agent accepted it or the end-user abandoned it

  * **ASA** : the Average Speed of Answer (ASA). This is the average time that elapsed between when a call entered a queue and when an agent assigned it. ASA is only measured when an agent handles the call.

  * **Queue Abandoned** : the number of calls abandoned while waiting in a queue before connecting to an agent

  * **Avg Queue Abandon Time** : the average time that calls waited in a queue before being disconnected without an agent accepting them

  * **Avg Vol per Hour** : the average number of calls completed per hour

  * **CSAT** : the average Customer Satisfaction Score for calls

  * **Sentiment Score** : the average sentiment score for calls

  * **Call Type Distribution** : the distribution of different call types

  * **Service Level - Calls** : the aggregated service level for all call queues, as determined by the queue configuration

  * **Average Handle Time** : the average handle time for calls




## Chats

The **Chats** section contains the following metrics tiles:

  * **Total Handled Chats** : the number of chats handled

  * **Service Level - Chats** : the aggregated service level achieved for all chat queues in your environment, as determined by the queue configuration

  * **Queued Now** : the total number of chats in the queue waiting to be assigned to an agent

  * **Max Queue Time** : the wait time of the chat that has been in the queue for the longest. If the queue is empty, this metric resets to zero.

  * **Avg Queue Time** : the average time a chat spent in a queue until an agent accepted it or the end-user abandoned it

  * **ASA** : the Average Speed of Answer (ASA). This is the average time that elapsed between when a chat entered a queue and when an agent assigned it. ASA is only measured when an agent handles the chat.

  * **Queue Abandoned** : the number of chats abandoned while waiting in a queue before connecting to an agent

  * **Avg Queue Abandon Time** : the average time that chats waited in a queue before being disconnected without an agent accepting them

  * **Avg Vol per Hour** : the average number of chats completed per hour

  * **CSAT** : the average Customer Satisfaction Score for chats

  * **Sentiment Score** : the average sentiment score for chats

  * **Chat Type Distribution** : the distribution of different chat types

  * **Service Level - Chats** : the aggregated service level for all chat queues, as determined by the queue configuration

  * **Average Handle Time** : the average handle time for chats




## Virtual agent voice and chat

The following metrics are collected for virtual agent performance. Virtual agent metrics appear only if virtual agents are configured.

  * **Total Virtual Agent Interactions** : the total interactions handled by virtual agents

  * **Total Escalations** : the total number of interactions that were escalated to a human agent from a virtual agent

  * **Fallback Rate %** : the percentage of virtual agent interactions where the virtual agent stated that it did not understand the end-user's query, and the interaction resulted in a fallback response. It is calculated as the number of default fallback responses divided by the total number of virtual agent responses, multiplied by 100.

  * **Average Responses per Second** : the average number of virtual agent responses per second

  * **Resolution Rate** : the number of calls or chats that were resolved by a virtual agent without escalating to a human agent




## Agent status

The **Agent Status** section contains the following metrics tiles:

  * **Agent Status** : a pie chart that displays the distribution of agent statuses for the date range that you specify. This includes custom statuses that you create.

  * **Occupancy Rate** : a bar chart that shows the agent occupancy rate




## Voicemail

The **Voicemail** section contains the following metrics tiles:

  * **Voicemails Queued** : the number of voicemails that are queued and waiting to be accessed by an agent

  * **Voicemails Handled** : the number of voicemails that have been accessed by an agent




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
