---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-queue-monitor/
title: Queue monitoring dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:39.774043+00:00
---

# Queue monitoring dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-queue-monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue monitoring dashboards Stay organized with collections  Save and categorize content based on your preferences. 

With the **Real-time Queue Monitoring - Calls** and the **Real-time Queue Monitoring - Chats** dashboards, monitor the performance of your queues in real time. Identify when an incident occurs and the time of resolution. Monitor talk time, wrap-up time, and historical trends.

These dashboards refresh every 60 seconds by default.

## Use the dashboards

To use the dashboards, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **Queue Monitoring / Calls** or **Queue Monitoring / Chats**. The dashboard appears.

  3. Filter your results using the following fields:

     * **Queue Group**. Filter by queue group.

     * **Queue Name**. Filter by queue name.

     * **Child Queues**. Specify whether to include child queues.

     * **Language**. Filter by the language assigned to the queue.

     * **Agent Teams**. Filter by the agent team handling the interaction.

     * **Location**. Filter by the location of the agent.

     * **Interaction Type**. Filter by the type of interaction.

     * **Direction**. Filter by the direction of the interaction.

  4. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

These dashboards contain the following metrics tiles:

  * **Total Active Calls** (calls only): the total number of calls that are active

  * **Total Active Chats** (chats only): the total number of chats that are active

  * **Total Queued Now** : the number of calls or chats that are in queue waiting to be answered. If there are interactions waiting in the queue, the tile turns pale blue.

  * **Current Max Queue Wait Time (H:M:S)** : the current longest time a call or chat is in a queue waiting for agent assignment. This indicates how long your contacts are waiting to be connected.

  * **Total Rolled Over Pending Callbacks** : the number of rolled over pending callbacks

  * **Total Rolled Over Completed Callbacks** : the number of rolled over completed callbacks

  * **Avg CSAT Calls** : the average number of CSAT calls

  * **Overall SLA %** : an aggregated SLA that is associated with all queues. If filters are applied to the dashboard for only a few queues, the widget updates to display the SLA for the chosen queues.

  * **Total Queue Interactions** : the total number of calls or chats waiting in the queue for agent assistance, including transfers

  * **Total Transfers** (chats only): the total number of interactions transferred from one agent or queue to another

  * **Avg Queue Time (H:M:S)** : the average amount of time that calls or chats wait in a queue before they are accepted by an agent or abandoned

  * **Avg Speed to Answer (H:M:S)** : the average time an interaction remains in the queue until it is assigned to an agent. This is only measured in instances where the interaction is ultimately handled by an agent.

  * **Total Repeat Contacts** : the number of contacts that returned to the same queue, using the same device, within the configured amount of time

  * **Total Queue Abandons** : the total number of interactions that failed while waiting in queue to be assigned to an agent

  * **Avg Queue Abandon Time (H:M:S)** : the average amount of time that calls or chats waited in a queue before disconnecting without being accepted by an agent

  * **Total Handled** : the number of interactions handled by an agent

  * **Avg Handle Time (H:M:S)** : the average amount of time across all interactions from when an agent was assigned a call, including before call work (BCW) for preview campaign calls, to when they ended the wrap-up phase. Includes Talk / Chat time + Hold Time + Wrap-up Time.

  * **Total Failed** : the number of calls or chats that failed to connect to an agent. This occurs for reasons such as expired transfer, no answer, or declined by consumer.




## Tables

These dashboards contain the following metrics tables. Hold the pointer over a table heading to see its description.

  * **Real Time Data** : real-time queue data

  * **Today's Scheduled Calls** (calls only): today's pending scheduled calls across your allowed scheduling window

  * **Upcoming Scheduled Calls** (calls only): upcoming pending scheduled calls across your allowed scheduling window

  * **Historical Data** : "on the day" historical data




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
