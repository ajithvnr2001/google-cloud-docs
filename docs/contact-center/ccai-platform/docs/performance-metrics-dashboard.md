---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/performance-metrics-dashboard/
title: Performance metrics dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:48.510313+00:00
---

# Performance metrics dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/performance-metrics-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Performance metrics dashboard Stay organized with collections  Save and categorize content based on your preferences. 

The Performance Metrics dashboard gives you a high level overview of your support center for both calls and chats. It is split into two primary sections: Global Metrics and SLA Metrics.

## Details

  * Only inbound interactions are represented. Because outbound calls are not associated with a queue, they are not included.

  * Queue selection must be completed to show in the dashboard

  * In-menu abandons are not represented




## View the dashboard

  * **Go to Dashboard > Performance Metrics**.



## Time filters

In the top right corner a filter drop down is available.

  * **Today** : the current date based on your locally configured time zone

  * **Last 24 hours**

  * **This quarter** : Starts at the first day of the current calendar quarter until the current day




## Global metrics

The left-hand tile contains call-specific data, while the right-hand tile contains chat data.

|   
---|---  
Call Volume | Count of inbound or outbound interactions offered, regardless of whether they were handled by an agent or not (includes abandons, failed contacts, etc)  
Handled | Count of inbound or outbound interactions touched by an agent (excludes agent <> agent transfers)  
Transfer % | SUM of finished or failed segments that are a transfer / SUM of all finished or failed segments  
Inbound | Count of interactions created by a consumer and offered - regardless of whether it was handled by an agent (includes abandons, failed contacts, etc)  
Outbound | Count of interactions created by an agent or auto-dialing system, regardless of whether the consumer answers the call  
Calls in Queue | Count of inbound interactionscurrentlywaiting in queue  
AHT | (average call duration + average wrap-up status associated with a Call ID)  
Chat Volume | Count of interactions offered, regardless of whether they were handled by an agent or not (includes abandons, failed contacts, etc)  
Handled | Count of interactions touched by an agent (excludes agent <> agent transfers)  
Transfer % | Sum of finished or failed interactions that are a transfer / Sum of all finished or failed interactions  
Chat Concurrency | The average concurrency of all ongoing chats (live metric)  
Avg Response Time | Average time (seconds) that it takes for an agent to respond to a consumer  
Chats in Queue | Count of inbound interactionscurrentlywaiting in queue  
AHT | Average chat duration (no wrap-up status applied)  
  
## SLA metrics

The top of the SLA Metrics shows two charts for Call SLA and Chat SLA respectively. The time range displayed here is representative of the time range selected at the top right of the page. The SLA displayed represents the total SLA across the support center.

### Call and chat metrics: SLA bands

This section will help you quickly identify how many sessions are falling below the set SLA threshold. There are three pre-configured thresholds displayed by default:

  1. SLA >= 80

  2. 60 > SLA < 80

  3. SLA <= 60




The metrics displayed are defined as follows:

|   
---|---  
Queues | See Data Dictionary  
Total SLA | See Data Dictionary  
Volume | Total interactions which qualify for SLA calculation. See SLA in Data Dictionary for more details.  
Handled | Total completed interactions which qualify for SLA calculation. See Data Dictionary.  
Abandoned | See Data Dictionary  
  
If you're interested in exploring the data further, click the explore button  on the right of each row to open a new, more detailed view. In this view, you can see which specific queues fall into each SLA band.

The metrics displayed are defined as follows:

|   
---|---  
Queues | See Data Dictionary  
Total SLA | See Data Dictionary  
Volume | Interactions which qualify for SLA calculation. See SLA in Data Dictionary for more details  
Handled | See Data Dictionary  
Abandoned % | See Data Dictionary  
Incoming SLA | See Data Dictionary  
Transfer SLA | See Data Dictionary  
  
## Call and chat average handle time (AHT)

The final section on this dashboard will give you insight into AHT (Average Handle Time) for your highest volume queues. Up to 5 queues show at a time and the volume shows everything including abandoned interactions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
