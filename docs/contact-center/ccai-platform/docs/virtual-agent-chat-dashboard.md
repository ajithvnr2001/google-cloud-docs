---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent-chat-dashboard/
title: Virtual agent chat dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:43.699364+00:00
---

# Virtual agent chat dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent-chat-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Virtual agent chat dashboard Stay organized with collections  Save and categorize content based on your preferences. 

This dashboard provides a range of status, session, and performance insights for Chat sessions attended by the Virtual Agents. The dashboard is controlled by a group of filters: Virtual Agent, Queue, and Time frame.

## Dashboard filters and behaviors

### Filter the dashboard

The current filter settings show in the **Filtered by** section.

  1. Go to **Dashboard** > **Virtual Agent**.

  2. Select a **Time zone** : Select the time zone of the dashboard data in the upper right corner dropdown.

  3. Click **Filter settings** to show the filter options.

  4. Select a **Virtual Agent**. Leave the default setting to see All Virtual Agents or select an individual Virtual Agent from the dropdown.

  5. Make a **queue** selection. Leave the default setting for All Queues or select any individual queue. This list includes queues without Virtual Agents active so if no results show, be sure there is an online Virtual Agent assigned to the queue.

  6. Select the **time frame.**

  7. Click **Apply** to save your settings.




### Data change indicators

Most tiles have a change indicator, marked by an up/down red/green arrow, and a numeric value of the chance percentage. Change is determined based on filter settings, comparing data to the time period before the current filtered data. The direction of the arrow indicates the numerical direction of the change in value, while green indicates a favorable change and red indicates an unfavorable change.

Tile - CSAT

Time frame - 24 hours

The change indicating arrow will point upwards and show green when the CSAT data from the previous 24 hours is lower than the current data. _The upward green arrow marks a positive change to the current data when compared to the previous 24 hours._

### Sections not impacted by filters

All tiles in the Current Status section are not impacted by the filter settings and show current data.

## Dashboard tiles and definitions

### Virtual agent sessions

**Consumer Initiated** : The total chat sessions initiated by the consumers and handled by Virtual Agents

**Transferred from Human Agent** : The total of chat sessions that are answered by a human agent and then transferred to a Virtual Agent

**Total Messages Exchanged** : The total number of individual messages exchanged between a Virtual Agent and a consumer during a chat session

**Avg. Messages per Session** : The average number of messages exchanged between a Virtual Agent and a consumer, per chat session. Calculation: (Total Messages exchanged in all VA chat sessions) / (Total number of Virtual Agent chat sessions)

**CSAT** : 1 to 5 rating given by the consumer at the end of a session which ended with a Virtual Agent. Chat may have started with a human agent and was transferred or could have been fully attended by a Virtual Agent. Must use the CCAI Platform CSAT feature to see a value here.

### Performance

  * **Resolved by Virtual Agent** : The total number of chat sessions handled by a Virtual Agent to the end of the relevant programmed discussion points

  * **Planned Transfer** : The total number of chat sessions handled by a Virtual Agent that are then transferred to another agent (human) due to configuration/standard operating procedure

  * **Escalated** : The total number of chat sessions that are handled by a Virtual Agent but do not reach the end of the relevant programmed discussion points (due to consumer clicking on the "escalation" button, typing an escalation message, or in rare cases, technical failure on the part of the Virtual Agent - such as going offline)

  * **Consumer Ended** : The total number of chat sessions that are handled by a Virtual Agent but do not reach the end of the relevant programmed discussion points (due to the consumer leaving the chat)

  * **Avg. Handle Time:** Average time (MM:SS) that a Virtual Agent spends on a chat session.

  * **Avg. abandoned time (Avg. Consumer Ended Time):** Average time (MM:SS) between the start and end of a chat session, only for chats marked _consumer ended_.

  * **Users Repeating/Returning:** Total number of consumers who returned to interact with the same Virtual Agent within 24 hours of a previous session




  * **"Did not Understand" Rate:** The % of Virtual Agent chat messages sent where a Virtual Agent states that they did not understand the consumer

    * (No. of default fallback responses / Total no. of VA responses) * 100



### Current status

  * **Top queues** : Top 5 chat queues in order of the highest to lowest total Virtual Agent sessions

  * Top Virtual Agents: Top 5 Virtual Agents in order of the highest success rates

  * **Virtual Agent status**

    * Online: Enabled and functioning Virtual Agents

    * Offline: Enabled but unreachable. See **Virtual Agent Platform statuses** in Virtual Agent configuration

    * Inactive: Virtual Agent is turned off




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
