---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-unresponsive/
title: Unresponsive agent threshold \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:41.427650+00:00
---

# Unresponsive agent threshold  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-unresponsive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Unresponsive agent threshold Stay organized with collections  Save and categorize content based on your preferences. 

Unresponsive status is a system-set status different from most other default statuses. It allows Managers and Admins to **identify an unresponsive Adapter** and take action to return the adapter and agent to a state where calls or chats can be received.

## Unresponsive status details

When a session chat or call is routed to an agent using Deltacast and the system does not receive a response from the Agent's Adapter, the system logs this event as a **_Skipped_** call or chat.

By default, an Agent is set to Unresponsive after three (3) consecutive _skipped_ calls or chats are recorded for that Agent. This is a "passive status" as neither Agents nor Managers can place an agent in this status; the status is triggered only by non-responsive Adapters that have logged skipped events.

If Agents are being put into Unresponsive, they are NOT intentionally avoiding calls/chats, instead, their machines are failing to receive CCAI Platform notifications. Agents generally don't know their call adapters are unresponsive and might be seeing a valid status, such as "Available". Unresponsive status allows Managers and Admins to identify an unresponsive Adapter and take action to return the adapter and agent to a state where calls or chats can be received.

## Administrator configuration

This default value of (3) is configurable in the CCAI Platform portal by going to **Settings** > **Operation Management** > **Deltacast** , and can be customized by specifying how many consecutive skipped calls or chats need to occur before the Agent is placed into "Unresponsive" status.

## Skipped versus Missed Calls

  * **Skipped call** \- Our system does not receive an acknowledgment that a call notification was sent to the agent's call adapter. This leads to an agent status of "Unresponsive" (depending on the configured number of sequential occurrences).

  * **Missed call** \- The agent's adapter successfully received the call notification and the agent was notified, but the agent did not pick up the call. This leads to a "Missed call" status.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
