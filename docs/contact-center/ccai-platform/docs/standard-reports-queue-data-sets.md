---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports-queue-data-sets/
title: Standard Reports: Queue Datasets \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:35:12.701987+00:00
---

# Standard Reports: Queue Datasets  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports-queue-data-sets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Standard Reports: Queue Datasets Stay organized with collections  Save and categorize content based on your preferences. 

CCAI Platform provides standard reports for queue specific data. 

## Queue Summary - All Interactions Report

The **Queue Summary - All Interactions** report provides a summary including all interactions, including transfers to the same or different queues. This includes: the first time that the interaction entered a queue, and subsequent entries to a queue after the work was accepted by an agent. This report displays the number of queue interactions by queue for each day. For the queue interactions for each date, the report provides a breakdown of how the interactions exited the queue.

The **Queue Summary - All Interactions** report can be found at **Reports > Queues**.

The metrics included in this report are as follows:

**Metric Name** | **Definition**  
---|---  
**Queue Name** | The name of the queue including the full path names if the queue is a sub queue.  
**Queue Interactions** | The number of times that an interaction entered a queue. This includes: the first time that the interaction entered a queue, and subsequent entries to a queue after the work was accepted by an agent.  
**Queue Abandons** | The total number of calls that were disconnected by the caller before being accepted by an agent.  
**Avg Queue Abandon Time** | The average time from when an interaction enters a queue but disconnects by the caller before the interaction is accepted by an agent  
**Queue Abandon Rate %** | The total queue abandons as a percentage of the total queue entries for the given period. Short abandons are included. Failed calls are not treated as abandoned.  
**Short Abandons** | Short abandons are interactions that have entered a queue but are disconnected by the caller before a set number of seconds as configured by the customer.  
**Long Abandons** | Long abandons are interactions that have entered a queue but are terminated by the customer after a set number of seconds as configured by the customer.  
**Avg Speed of Answer (ASA)** | Average time that elapsed between when an interaction entered a queue and when it was assigned to an agent. (Avg Queue Time)  
**Max Speed to Answer** | The maximum time that elapsed from when an interaction entered a queue and when it was assigned to an agent. (Also known as Max Queue Time)  
**SLA %** | Out of all the interactions that entered the queue, the percentage of interactions that started an active conversation with an agent within the configured SLA threshold. If short abandons are excluded in your SLA configuration, interactions that abandon within the configuration abandon threshold aren't counted. Calculation: Count of calls In SLA / (Count of calls In SLA + count of calls Out SLA) Count In SLA = Count of calls where queued time is less than the SLA threshold Count Out SLA = count of calls where queued time is equal to or greater than the SLA threshold  
**Handled** | The sum of interactions that were handled.  
**Avg Talk Time** | The average length of time that the agent spent talking to a consumer. This metric doesn't include hold time or wrap-up time.  
**Avg Hold Time** | The average time across all interactions where a consumer was placed on hold.  
**Avg Wrap Up Time** | The average amount of time that an agent was logged in and was in wrap-up status  
**Avg Handle Time** | The average time across all handled interactions that elapsed from when an agent accepts an interaction to when they end their wrap-up phase. This is calculated as _Talk Time + Hold time + Wrap-up time / All handled interactions_  
**Failed Calls** | The total number of failed calls for the given date range.  
**Avg CSAT Score** | The average satisfaction scores given by customers to rate the interaction as a percentage of the total possible score.  
  
## All Queued Interactions Report

The All Queued Interactions report provides detailed metrics of all interactions that queued. This report provides insights to configured SLAs including thresholds and service level event status. This report does include transfer details, specifically cold transfer, where a transfer occurs without prior notification to its recipient. This report does not include any handled metrics.

The **All Queued Interactions Report** can be found at **Reports > Queues**.

The metrics included in this report are as follows:

Metric name | Definition  
---|---  
Queue | The name of the queue including the full path names if the queue is a sub queue - where the interaction waited.  
Started At | The timestamp (date and time) when the interaction started.  
Ended At | The timestamp of when the interaction finished.  
Queue Time | The time from when an interaction enters a queue until it is either answered or the caller abandons.  
Agent Name | The identity of the individual that handled the interaction.  
Agent ID | The Contact Center AI Platform (CCAI Platform) unique ID of the individual that handled the interaction.  
Agent Email | The email address of the individual that handled the interaction  
Lang | The language associated with the queue the call was routed through.  
Transfer | Identifies whether the interaction was transferred.  
Service Level Event | The outcome of the interaction as per the configured SLA. 3 possible values: In SLA: (the interaction was handled within the SLA as configured for the queue) Not in SLA: (the interaction was handled outside of the SLA as configured for the queue) Excluded: (The interaction was not considered as part of the SLA as per the queue configuration.)  
Service Level Target Time | The time target for the SLA as per the queue configuration threshold.  
Service Level Abandon Time Threshold | The Service Level Abandon threshold as configured for the queue.  
Interaction Type | The source of where the interaction originated. Possible values include:

  * IVR Call
  * Incoming call
  * Numbered Incoming Call

  
Cold Transfer | An interaction where a transfer occurs without prior notification to its recipient. Returns (1) if a transfer is completed as cold, as opposed to warm.  
Event Status | The outcome of the Interaction. Possible values are:

  * All finished
  * ACW Ended

  
Interaction ID | The unique identifier of the interaction.  
  
## Queue Summary - Distinct Interactions Report

The **Queue Summary - Distinct Interactions** report provides a summary of all distinct queued interactions. Distinct queued interactions (the metric **Queue Entries**) only counts the first queue entry for the interaction. If a call is transferred to a second queue, only one queue entry is counted for the interaction. This does not include any transfers. This report provides insights to configured SLAs including all handled and abandoned metrics. This report can be used to reflect on the distinct count of contacts into your business.

This Queue Summary - Distinct Interactions report displays the number of queue entries by queue for each day. For the queue entries for each date, the report provides a breakdown of how those interactions exited the queue.

The Queue Summary - Distinct Interactions report can be found in the CCAI Platform portal at **Reports > Queues**.

The metrics included in this dataset are as follows:

**Metric Name** | **Definition**  
---|---  
**Queue Name** | The name of the queue including the full path names if the queue is a sub queue - where the interaction waited.  
**Queue Entries** | This only counts the first queue entry for the interaction. If a call is transferred to a second queue, only one queue entry is counted for the interaction.  
**Queue Abandons** | The total number of calls that were disconnected by the caller without being accepted by an agent.  
**Avg. Queue Abandon Time** | The average time from when an interaction enters a queue but disconnects by the caller before the interaction is accepted by an agent  
**Queue Abandon Rate %** | The total queue abandons as a percentage of the total queue entries for the given period. Short abandons are included. Failed calls are not treated as abandoned.  
**Short Abandons** | Short abandons are interactions that have entered a queue but are disconnected by the consumer before a set number of seconds as configured by the customer.  
**Long Abandons** | Long abandons are interactions that have entered a queue but are terminated by the consumer after a set number of seconds as configured by the customer.  
**Avg. Speed of Answer (ASA)** | Average Speed of Answer (ASA) is the average time an interaction remains in the queue until it is assigned to an agent. ASA is only measured in instances where the interaction is ultimately handled by an agent.  
**Max. Speed of Answer** | The maximum time that elapsed from when an interaction entered a queue and when it got assigned to an agent. ASA is only measured in instances where the call is ultimately handled by an agent.  
**SLA %** | Out of all the interactions that entered the queue, the percentage of interactions that started an active conversation with an agent within the configured SLA threshold. If short abandons are excluded in your SLA configuration, interactions that abandon within the configuration abandon threshold aren't counted. Calculation: Count of calls In SLA / (Count of calls In SLA + count of calls Out SLA) Count In SLA = Count of calls where queued time is less than the SLA threshold Count Out SLA = count of calls where queued time is equal to or greater than the SLA threshold  
**Handled** | The sum of interactions that were handled.  
**Avg. Talk Time** | The average length of time that the agent spent talking to a customer. This metric doesn't include hold time or wrap-up time.  
**Avg. Hold Time** | The average time across all interactions where a customer was placed on hold.  
**Avg. Wrap-Up Time** | The average amount of time that an agent was logged in and was in the wrap-up state  
**Avg Handle Time (AHT)** | The average time across all handled interactions that elapsed from when an agent accepts an interaction to when they end their wrap-up phase. This is calculated as _Talk Time + Hold time + Wrap-up time / All handled interactions_  
**Failed Calls** | The total number of failed calls for the given date range.  
**Avg. CSAT Score** | The average satisfaction scores given by customers to rate the interaction as a percentage of the total possible score.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
