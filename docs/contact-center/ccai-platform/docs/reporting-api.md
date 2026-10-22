---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/reporting-api/
title: Reporting API \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:49.486026+00:00
---

# Reporting API  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/reporting-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Reporting API Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides a set of API that can be used to gather reporting data.

  * [Manager API documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api)

  * [Apps API documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api)




## Available endpoints

Endpoint | Description  
---|---  
Agent | Provides necessary details around the agents that are assigned to the CCAI Platform platform.  
Agent Status History | Enables status changes and associated timestamps for what agents are doing within the CCAI Platform platform. This data is extremely useful in time-series analysis.  
Call | Gives visibility into every call and call type that the CCAI Platform platform manages including inbound, outbound, voicemails, and their channels. Subset details can also be included including keys to join photos, videos, transfer, and call participants. Furthermore, keys are provided to link calls and agents together for deeper tracking analysis.  
Chat | Similar to the call data model, the chat data model allows for users to identify the details of all chats managed by the CCAI Platform platform including the menu path taken prior to the chat being taken and transfer of the chat if applicable.  
Call Participant | Allows for the data to be pulled on the agent, end-users and/or third party who participated in a particular call.  
Chat Participant | Allows for the data to be pulled on the agent and ensures who participated in a particular chat.  
Changed Detail | Provides a unique data model to account for data value changes between the former and new value by specific fields.  
User Info | A subset of data that is best categorized as a limited view of the full agent data model.  
Photo | Represents the end user-uploaded photos which can be traced to call and chat channels.  
Video | Represents the end user-uploaded videos which can be traced to call and chat channels.  
Team | Provides additional context into agent details and how a particular agent is grouped in the support center. Agents can belong to more than one team.  
Team With Assignees | Provides data into the team and the associated agents.  
Team Tree | Provides the tree structure of the teams configured in CCAI Platform. For example, the US Team has two sub-teams, East and West Coast. This hierarchy is exposed with the US being the parent with 2 siblings, East and West.  
  
## Basic call segment API metrics

The CCAI Platform portal reports and API requests are two ways to look at metrics. Due to the intricacies that exist between the different data sources, some call metrics will appear in the API that don't appear in reports.

### Basic call segments: API

  * **Billing TIme**

Start - API: created_at

End - API: ended_at"

  * **Call Time**

Start - API: created_at

End - API: ended_at

  * **IVR Time**

Start - API: created_at

End - API: queued_at

  * **Queued Time & Wait Time**

Start - API: queued_at

End - API: connected_at

  * **Handle Time**

Start - API: connected_at

End - API: ended_at

  * **Transfer**

Start - API: /call.transfers[]['created_at']

End - API: /call.participants[]['connected_at']

  * **Conference Time**

API: /calls.participants[]['connected_at']

API: /calls.participants[]['ended_at']

_Note: Overlap of agent participants connected & ended times_

  * **Third Party Talk Time**

API: /calls.participants[]['connected_at']

API: /calls.participants[]['ended_at']

_Note: Overlap of agent participants connected & ended times_

  * **Ring Time (Connecting Time)**

Start - API: connecting_at

End - API: connected_at

  * **Talk Time**

API: duration - hold_duration

  * **Hold Time**

API: hold_duration




![Call API schema](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fd057d882.png)

### Call types, segments, and events

The following chart shows how each type of call segment is reported through a call lifecycle model. Disabled boxes indicate a situation in which the metric does not apply and won't be captured in reports.

![call lifecycle](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fd057faa4.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
