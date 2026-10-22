---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-dashboard/
title: Chat dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:25.942224+00:00
---

# Chat dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Chat dashboard Stay organized with collections  Save and categorize content based on your preferences. 

The chat dashboard shows both real-time and aggregated data. The dashboard can be filtered for various configurations, and you can drill into data by clicking to see filtered pages of [Connected, Queued, or Completed chats](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chats-connected-queued-and-completed#UUID-09c5f679-8917-2d05-4409-11f93b459f0e), or the [Agent Monitoring](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-monitoring-page#UUID-6ed9b514-d0e9-1459-c036-1d7828137145) page.

## Data refresh rate

The data refreshes at varying rates:

  * Every 20 seconds: Live data

  * Every 60 seconds: Service Level data

  * Every 5 Minutes: Daily aggregated data




### Filters

**Queue Group** : Filter by Queue Group.

**Queue**

  * **Language** : If you have multiple languages configured, select the language first, then the queue.

  * **Queue** : For Top-level queues, you can drill down and click **Apply** next to a sub-queue or leaf-queue.




**Team** : Filter by user teams.

  * When a top-level team is selected:

    * If the Top-level team is not assigned to a queue, the dashboard will show data aggregated for all of the queues and agents the sub-teams are assigned to.

    * If a top-level team is assigned to a queue, the dashboard will show data aggregated for the queues that the top-level team is assigned to AND all of the queues the sub-teams are assigned to.




**Date** : Filter by time range. The dashboard shows aggregate data with respect to your computer's time zone. The Date filter does not impact Live metrics (marked with an asterisk, below).

**Social** : enables you to filter and view the social messaging chat session metrics. For now only WhatsApp will display. This filter will only appear if WhatsApp has been enabled.

## Metrics

  * **Chats:** total number of chat interactions.

  * **Chat volume chart:** Chat interaction volume patterns over time in 15 minute increments.

  * **Service Level:** Monitors percentage of chats answered in x amount of seconds.

  * **Logged in Agent*:** Number of agents logged in.

  * **Live Chat*:** # of chats: connected, queued, or in-menu.

  * **Longest Chat Waiting:** Longest ongoing wait time for a chat in queue.

  * **% Transfers:** Percentage of chats that have been transferred.

  * **Volume per Hour:** Average volume of chat interactions per hour.

  * **Chats Handled:** Number of finished chat interactions.

  * **Average Handle Time:** Average length of the interaction [handle time] + [hold time].

  * **Queue: Most CIQ:** Queues with the highest number of chats waiting to be assigned to an Agent.

  * **Avg Queue Duration (LIVE):** Of the chats currently in queues, shows the average duration a consumer is spending waiting to be assigned to an Agent.

  * **Queues: Longest EWT:** Queues with longest estimated wait time.

  * **Queues: Highest Traffic:** Queues with the highest number of chats in the given time frame. Includes failed and abandoned chats.

  * **Agent Response Avg:** Average time for an agent to respond to an end user's message.

  * **Chats per Agent:** Average number of concurrent chat interactions per agent.

  * **Status Ratio:** Chat Status (finished, abandoned, and so on).

  * **Repeat Contacts:** # of callers who had multiple incoming sessions that finished in the same. queue within the configured repeat contact timeframe set in **Settings > Operation Management**.

  * **CSAT:** Average CSAT from chat interactions handled by Human Agents.

  * **Social** : display the total count of all Social Messaging chat sessions for the time period selected from the **Time** filter. Note: For now only WhatsApp will display. This tile will only appear if WhatsApp has been enabled.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
