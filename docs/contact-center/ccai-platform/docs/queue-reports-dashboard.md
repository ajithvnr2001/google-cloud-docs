---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-reports-dashboard/
title: Queue reports dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:32.697302+00:00
---

# Queue reports dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-reports-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue reports dashboard Stay organized with collections  Save and categorize content based on your preferences. 

The Queue Reports dashboard gives you a detailed, live overview of your Queue Groups and the queues within each group. This dashboard is well suited for monitoring the day to day performance and status of your operation.

## View the dashboard

  1. Go to **Dashboard > Queue Reports**.



## Dashboard details

  * Only inbound interactions are available in dashboards. Because outbound calls are not associated with a queue, they are not included on this dashboard

  * Queue selection must be completed to show in the dashboard

  * In-menu abandons are not represented in Dashboards currently




## Views

From the top-left of the Queue Groups Dashboard page, you can toggle between two different views. One view shows metrics at the Queue Group level and the other shows detailed metrics for each queue within the Queue Group.

### Queue groups summary (Today)

Displays detailed information on the health of your enabled voice and chat Queue Groups. Each row represents one of your Queue Groups - with exception of the **Totals** row, which displays an aggregate of all Queue Groups. The columns show metric (totaled or averaged depending on the metric) for all queues in the queue groups. The timeframe is always set to "Today" and all Call and Chat queue groups show on the same page.

### Queue group details

The Queue Groups Details shows metrics from one queue group at a time. The queue group is selected from the dropdown in the upper-right view shows each queue as a separate line item and the individual metrics for each queue in the enabled queue groups.

### Call, chat, or all display

Toggle between **Call,Chat, or All** icon to display the specific view options on the dashboard.

This is beneficial for users that would like to display the dashboards in different locations on Wallboards where only Chat or only Calls are applicable.

Click the **All** , **Call** , or **Chat** Icon to launch a new page and display the dashboard of your choice.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa7bb3be6ee.png)

## Data details

Data is categorized into three sections:

  * Service Level: Metrics displayed in this section are tied to service level (as set in **Settings** > **Operation Management** or the Queue Level Target Metrics.

  * Live Queue Metrics: Metrics displayed in this section reflect the live, current state of the Queue Group

  * Live Agent Status: Current count of Agents in a status or status category

    * Click on any metric within the Live Agent section to drill down and see additional detail including a list of the agents in the respective status. You can use the filters at the top to adjust which statuses you're viewing.
  * Today: Metrics displayed in this section are aggregated across the current day. Time zone is typically set by your browser unless otherwise specified by your Admin team.




### Time zone

The time zone is displayed at the top right of the dashboard and generally reflects the user's locally configured time zone. The **Today** section of the dashboard aggregates data for the current date based on the time zone displayed here.

**Note:** If your company has requested a time zone override for all its users, then the requested time zone will be displayed instead

### Metric definitions

|  |   
---|---|---  
Service Level | SL / 30min | Service Level within the past 30min  
SL / day | Service Level for the current day |   
SL Target | Service Level Target set for the queue |   
Live | CIQ | Consumers in Queue  
LCW / Sec | Longest Call Waiting |   
AQD / Sec | Average Queue Duration (Waiting for an Agent) |   
Live | Number of calls currently in progress with an agent |   
Productive Agents | Number of agents with a productive status |   
Live Agent Status | Available | Count of all available agents  
On-hold | (Calls only)Count of agents who have placed a consumer on-hold |   
Wrap-up | Count of all agents in the wrap-up status |   
Custom | Count of all agents in custom statuses that are configured as productive |   
Productive Agents | Count of all agents in a productive status as configured in **Settings > Queue Groups** |   
Today | ABN % | Abandon rate  
Volume | Total offered interactions including failed/abandoned sessions. Excludes in-menu abandoned sessions. |   
Handled | Total number of completed interactions |   
ASA / Sec | Average speed to answer |   
AHT / Sec | Average Handle Time |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
