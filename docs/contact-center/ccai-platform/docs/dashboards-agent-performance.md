---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-agent-performance/
title: Agent performance dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:15.380339+00:00
---

# Agent performance dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-agent-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent performance dashboard Stay organized with collections  Save and categorize content based on your preferences. 

With the **Agent Performance** dashboard, get a summary of the overall performance of your contact center without having to run performance reports. See what's in-queue, maximum wait times, call or chat volumes, response times, agent statuses, virtual agent performance, and more. Use this data to evaluate agent performance and identify areas for improvement.

## Use the dashboard

To use the dashboard, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **Agent Performance**. The dashboard appears.

  3. Click the **Date** field to select a date range, and then do one of the following:

     * Select a preset data range. To do this follow these steps:

       1. Click expand_more **More** to view all of the preset date ranges.

       2. Click the date range that you want.

     * Select a custom range. To do this, follow these steps:

       1. Click **Custom**.

       2. In the **Custom** field, enter a start and end date for your date range. You can type your date range or click ![Click the calendar icon to see the
calendar.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-calendar.png)**Open calendar** to select start and end dates.

**Note:** The maximum date range that you can specify is 45 days. If you specify a date range of more than 45 days, the dashboard returns an error. 
  4. Filter your results using the following fields:

     * **Select Channel** : by channel

     * **Start Time** and **End Time** : get results from only within this time range

     * **Agent Name** , **Agent ID** , **Custom Agent ID** , and **Agent Email** : by agent

     * **Team** : by team

     * **Answered By** : by the type of agent

     * **Location** : by location

     * **Direction** : by the direction of the session

     * **Total Talk Time** , **Total Chat Time** , **Total Hold Time** , **Total Wrap Up Time** , and **Total Handle Time** : by time spent in different phases of a session

  5. In the **Time Format** field, set the time format.

  6. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

This dashboard contains the following metrics tiles:

  * **Total Inbound Handled** : the number of inbound interactions handled by the agent

  * **Total Outbound Handled** : the number of outbound interactions handled by the agent

  * **Total Transferred** : the total number of interactions transferred by an agent to another queue or agent

  * **Avg Occupancy Rate (%)** : the percentage of time the agent is actively handling customer interactions (in-call or in-chat) to the total time the agent is either handling interactions or available to take calls.

  * **Avg CSAT Score** : the customer satisfaction scores (CSAT) awarded to the interaction. These are captured after an interaction ends.

  * **Avg Handled per Hour** : the average sessions handled per hour by the logged in agents

  * **Avg Chat/Talk Time** : the total time that the agent spent talking to a customer. This excludes BCW and ACW . For example, if the agent is on a call for 10 minutes and the hold time is 1 minute, then the talk time is 9 minutes.

  * **Avg Hold Time** : the average time an end user was placed in a hold status by the agent. For chat data this won't be available, and it will display **N/A**.

  * **Avg Wrap Up Time** : the average time spent in after call or chat wrap-up (ACW)

  * **Avg Handled Time** : the average amount of time that has elapsed from when an agent was assigned a call or chat to when they end the wrap-up phase

  * **Time in Status Reason** : displays the reason codes with the highest values and the amount of time the agents have spent in each status. Values are shown in percentage. When a code is selected, the **Total Time (in hours)** displays.

  * **Occupancy Rate (%)** : displays the percentage of time agents spend handling calls during a 30-minute period. It's calculated by dividing the total time agents spend on calls by the total time they are available to take calls and multiplying by 100. For example, if agents are available for a total of 2 hours in a given 30-minute interval, and they spend 1 hour and 30 minutes on calls, the occupancy rate forthat interval would be 75%. If multiple days are selected through the filter, the 30 minute intervals will be replaced by individual days.

  * **Handled by Direction** : displays the number of handled contacts,inbound and outbound, by 30 minute intervals. Each interval shows a sum of calls and chats.

  * **Handled by Agent (Top 20)** : displays all agents and the number of calls and chats they have handled. The total number of chats handled will be displayed over the total number of calls handled. The values for each will display and you can hover over an agent to see the breakdown of the calls and chats handled.

  * **Avg Handle Time by Agent (Top 20)** : displays the average handle time of the top 20 agents




## Tables

This dashboard contains the following metrics tables. Hold the pointer over a table heading to see its description.

  * **Agent Productivity** : provides a supervisor with insights on the performance of each agent. This table shows all the available metrics as well as the aggregated data. This information only displays once filters have been applied to the dashboard.

  * **Agent Productivity Detailed - Calls** : provides performance data specific to calls

  * **Agent Productivity Detailed - Chats** : provides performance data specific to chats

  * **Agent Activity Summary** : provides a performance summary for each agent




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
