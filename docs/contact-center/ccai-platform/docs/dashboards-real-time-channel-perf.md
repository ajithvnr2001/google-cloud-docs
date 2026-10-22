---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-channel-perf/
title: Real-time channel performance dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:25.730477+00:00
---

# Real-time channel performance dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-channel-perf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Real-time channel performance dashboards Stay organized with collections  Save and categorize content based on your preferences. 

With the **Real Time Calls Performance** and **Real Time Chats Performance** dashboards, get key performance indicators (KPIs) that provide a real-time overview of call and chat performance.

These dashboards refresh every 60 seconds by default.

## Use the dashboards

To use the dashboards, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **Real Time Channel Performance / Calls** or **Real Time Channel Performance / Chats**. The dashboard appears.

  3. Filter your results using the following fields:

     * **Queue Name**. Filter by queue name.

     * **Queue Group**. Filter by the group that the queue is assigned to.

     * **Teams Filter**. Filter by one or more teams.

     * **Location**. Filter by one or more locations.

     * **Direction**. Filter by the direction of the interaction.

  4. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

These dashboards contain the following metrics tiles:

  * **SLA** : out of all the interactions that entered the queue, the percentage of interactions that started an active conversation with an agent within the configured SLA threshold. If short abandons are excluded in your SLA configuration, interactions that abandon within the configuration abandon threshold aren't counted.

  * **Queued Now** : the number of calls or chats that are in queue and waiting to be connected to an agent. This is a live metric.

  * **Agent Status Breakdown** : the distribution of various agent statuses. For example, it provides insight into the real-time proportion of agents in different states, such as available, busy, on a call, or on break.

  * **Top 10 queued now** : indicates the total number of calls or chats in each queue, ordered from the highest to the lowest. This visualization will display the top 10 queues. This can help teams prioritize their responses to address the most significant traffic.

  * **Active Calls** or **Active Chats** : the number of interactions (calls or chats) that are active

  * **Max Queued Wait Time** : the maximum amount of time that elapsed when calls or chats spend time in a queue waiting for agent assignment.

  * **Total Handled** : the number of interactions (call or chat) handled by an agent

  * **Queue Abandons** : the number of queue abandons as a percentage of the total queue interactions for the given period. Failed calls are not treated as abandoned. This excludes Short Abandons.

  * **Avg Queue Time** : the average amount of time elapsed from when a call or chat entered a queue to when it was accepted by an agent or is abandoned

  * **Avg Speed to Answer** : the average speed of answer for calls. The average time that elapsed between when an interaction entered a queue and when it was assigned to an agent. ASA is only measured in instances where the call is ultimately handled by an agent.

  * **Avg Queue Abandon Time** : the average amount of time that calls or chats waited in a queue before disconnecting without being accepted by an agent

  * **Avg CSAT** : the average of all customer satisfaction scores (CSAT) awarded to the interaction. These are captured after an interaction ends.

  * **Avg Talk Time** : the average amount of time that the agent spent talking to an end-user

  * **Avg Hold Time** : the amount of time (in seconds) an agent placed a consumer on hold during an interaction. An agent that places a consumer on hold multiple times will only show the total hold duration for that interaction. When that agent transfers the call out, this would start a new interaction which would track its own hold time.

  * **Avg Wrap-up Time** : the average amount of time that elapsed from when an agent accepts a call or chat to when they end their wrap-up phase

  * **Avg Handle Time** : the average amount of time that elapsed from when an agent accepts a call or chat to when they end their wrap-up phase for a given date range. This starts when the call is assigned to the agent, not when the call is connected to the agent. For Calls this includes Hold Time.

  * **Top 10 queues by Wait Time** : displays the queues sorted by the length of time that calls or chats have been waiting. This information can be vital for addressing the most urgent cases.

  * **Total Transfers** : the number of interactions that have been transferred to other queues

  * **Voicemail Queued** : the number of voicemails that are queued and waiting to be accessed

  * **Voicemail Read** : the number of voicemails that have been handled




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
