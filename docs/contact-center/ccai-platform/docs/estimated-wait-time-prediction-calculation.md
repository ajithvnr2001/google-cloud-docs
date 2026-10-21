---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/estimated-wait-time-prediction-calculation/
title: Estimated wait time prediction calculation \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:49:56.451979+00:00
---

# Estimated wait time prediction calculation  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/estimated-wait-time-prediction-calculation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Estimated wait time prediction calculation Stay organized with collections  Save and categorize content based on your preferences. 

Estimated wait time (EWT) is used in determining when to launch [overcapacity deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#call-settings-overcapacity-deflection) and for In-Web and In-App UIs, which show wait time to end-users.

## EWT for calls

For calls, EWT is calculated based on the following formula:
    
    
    EWT = ((average duration in channel / active agents in channel) * (agents in
    common / active agents in current queue) * (queued calls - available agents)) +
    {EWT for callbacks, campaign calls, and scheduled calls}
    

## EWT for chats

For chats, EWT is calculated based on the following formula:
    
    
    EWT = (average duration in channel / active agents in channel) * (agents in
    common / active agents in current queue) * (queued chats - available agents)
    

**Note:** In chat channels, the value for `active agents` includes a multiplier based on the chat concurrency if the chat concurrency is >1\. This is because chat concurrency increases the amount of available chats a single agent can handle.

## Calculation considerations

The following are considered when calculating EWT:

  * Priority settings are considered when calculating the number of calls or chats in queue. Only calls or chats with higher priority than the end-user are counted.

  * Multiple assignments of agents are considered when calculating available agents. For example, if the agent is assigned to only one queue, the count is `1`. But if the agent is assigned to two queues, the count is `0.5`. If the agent is assigned to three queues, the count is `0.3`.

  * Offline agents are excluded when calculating active and available agents.

  * The `average duration` value is based on the previous hour.

  * 10 seconds of wait time is added to the EWT for all sessions. This is to account for channel-specific messages to the end-user.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
