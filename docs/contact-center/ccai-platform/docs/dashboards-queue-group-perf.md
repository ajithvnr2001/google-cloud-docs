---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-group-perf/
title: Queue group performance dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:02.778512+00:00
---

# Queue group performance dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-group-perf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue group performance dashboards Stay organized with collections  Save and categorize content based on your preferences. 

With the queue group performance dashboards, see an overview of real-time and historical data for queue groups. See the number of calls waiting in queues and the rate at which customers are hanging up before reaching an agent. Use data on underperforming and overperforming queues to make adjustments in routing or staffing.

These dashboards refresh every 60 seconds by default.

**Note:** These dashboards report only on queues that are part of a queue group. Google recommends removing a queue from a queue group outside of operating hours to minimize impact on reporting data.

## Queue Group Dashboards All

The **Queue Group Performance All** dashboard contains two queue group performance tables, one for calls and one for chats. In addition to filtering by queue group, you can also filter by queue name. This dashboard displays metrics that are either real-time or are taken from the current day.

### Use the dashboard

To use the **Queue Group Dashboards All** dashboard, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Queue Groups**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Queue Group Dashboards All** dashboard appears.

  2. In the **Time Format** field, set the time format.

  3. Filter your results using the following fields:

     * **Queue Group**. Filter by queue group.

     * **Queue Name**. Filter by queue name.

     * **Language**. Filter by the language assigned to the queue.

     * **Location**. Filter by one or multiple locations.

  4. Click ![The reload dashboard icon](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Reload**.




### Tables

This dashboard contains the following metrics tables. Hold the pointer over a column heading to see its description.

  * **Queue Group Performance Calls** : displays detailed performance information for calls by queue group

  * **Queue Group Performance Chats** : displays detailed performance information for chats by queue group




## Queue Groups Dashboard Calls and Queue Groups Dashboard Chats

The **Queue Groups Dashboard Calls** and **Queue Groups Dashboard Chats** dashboards contain both live and historical data. In addition to filtering by queue group, you can also filter by teams.

### Use the dashboards

To use the **Queue Groups Dashboard Calls** and **Queue Groups Dashboard Chats** dashboards, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Queue Groups**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Queue Group Dashboards All** dashboard appears.

  2. Click the **Calls** or the **Chats** tab.

  3. In the **Time Format** field, set the time format.

  4. Filter your results using the following fields:

     * **Queue Group**. Filter by queue group.

     * **Language**. Filter by the language assigned to the queue.

     * **Teams**. Filter by one or multiple teams.

     * **Location**. Filter by one or multiple locations.

  5. Click ![The reload dashboard icon](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Reload**.




### Tiles

These dashboards contain the following metrics tiles:

  * **Queued Now** : the number of calls or chats that are waiting in queue

  * **Current Max Queue Time** : the current maximum amount of time elapsed while calls or chats are in a queue waiting for agent assignment. This doesn't consider whether the call or chat was answered.

  * **Avg Queue Time** : the average amount of time that calls or chats waited in a queue before disconnecting without being accepted by an agent

  * **Total Handled Interactions** : the number of interactions (call or chat) handled by an agent. This includes work an agent received from a queue and work directly assigned to an agent that never entered a queue. This is the count of all **Call** interactions where the **Event** is **Finished** or **Failed**.

  * **Abandons** : the number of interactions that were waiting in queue and were disconnected by the consumer before being accepted by an agent. This excludes Short Abandons.

  * **Avg Handle Time** : the average amount of time that elapsed from when an agent was assigned a chat to when they ended the wrap-up phase. AHT starts when the call is assigned to the agent, not when it is connected. It is calculated as the sum of BCW Duration, Call Duration, and ACW Duration, divided by Total Handled Calls.

  * **Callbacks Waiting** (calls only): the number of calls that are waiting to be connected to an agent

  * **Avg Callback Wait time** (calls only): the average wait time for the callbacks in queue waiting to be reconnected to an agent

  * **Overall SLA %** : the SLA percentage for the current interval. This is the percentage of interactions that entered the queue and started an active conversation with an agent within the configured SLA threshold. If short abandons are excluded in your SLA configuration, interactions that abandon within the configuration abandon threshold aren't counted. Recovered calls are not considered. If the divisor is lower than the dividend, we set the dividend equal to the divisor, with a maximum of 100%.

  * **Avg Queue Abandon Time** : the average amount of time that calls or chats waited in a queue before disconnecting without being accepted by an agent. This is calculated as the sum of BCW Duration, Call Duration, and ACW Duration, divided by Total Handled Calls.

  * **Avg Response Time** (chats only): the average time for an agent to respond




### Tables

These dashboards contain the following metrics tables. Hold the pointer over a column heading to see its description.

  * **Live Data** : displays live data for calls or chats

  * **Historical Data** : displays historical data for calls or chats




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
