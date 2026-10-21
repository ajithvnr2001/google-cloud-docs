---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-virtual-agent/
title: Virtual agent dashboards \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:59:24.177768+00:00
---

# Virtual agent dashboards  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-virtual-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Virtual agent dashboards Stay organized with collections  Save and categorize content based on your preferences. 

With the **Virtual Agent Dashboard Calls** and **Virtual Agent Dashboard Chats** dashboards, evaluate the performance of your virtual agents to find areas for improvement.

## Use cases

The virtual agent dashboards can help with the following:

  * **Performance monitoring** : analyze real-time and historical data on virtual agent performance, such as the number of interactions handled, average response time, and customer satisfaction ratings. This lets you monitor and assess the effectiveness of virtual agents and identify areas for improvement.

  * **Issue detection and resolution** : identify patterns or trends in end-user interactions where virtual agents might struggle to understand requests or provide accurate responses. This can help you identify issues and take corrective actions, such as updating virtual agent scripts or providing additional training.

  * **End user insights** : gain valuable insights into end-user behavior, preferences, and pain points by analyzing data from virtual agent interactions. You can use this information to better understand end-user needs, tailor virtual agent responses, and improve the overall end-user experience.

  * **Resource allocation** : analyze data on virtual agent workload, availability, and performance, enabling you to optimize resource allocation. For example, you can identify peak hours when additional virtual agents might be required to handle increased inquiries or assign virtual agents based on their expertise.

  * **ROI analysis** : measure the return on investment (ROI) of virtual agents by analyzing data on their performance, cost savings, and customer satisfaction. This can help you assess the value and effectiveness of virtual agents in achieving business goals.




## Use the dashboards

To use the dashboards, follow these steps:

  1. In the CCAI Platform portal, click **Dashboard > Advanced Reporting**. If you don't see the **Dashboard** menu, expand the window horizontally until the **Dashboard** menu appears. The **Advanced Reporting Landing Page** appears.

  2. Click **Virtual Agent / Calls** or **Virtual Agent / Chats**. The dashboard appears.

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

     * **Start Time** and **End Time** : Get results from only within this time range.

     * **Virtual Agent** : Filter by virtual agent.

     * **Queue** : Filter by queue.

     * **VA Escalation in Queue** : Filter by whether there was a virtual agent escalation in the queue.

  5. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

These dashboards contain the following metrics tiles for both calls and chats.

  * **Total Virtual Agent Interactions** : the sum of interactions in which the virtual agent was presented to end-users. For example, if an end-user contacts a support center and interacts with one virtual agent and then is transferred to another queue where they interact with another virtual agent, then that would include two virtual agent interactions.

  * **Total Human Agent Initiated Interactions** : the sum of interactions that were transferred from the virtual agent to a human agent for further assistance

  * **Avg Messages per Session** : the average number of messages per session

  * **Total Messages Exchanged** : the sum of messages that were exchanged between the end user and the virtual agent

  * **Resolution Rate %** : the percentage of virtual agent interactions that were successfully resolved by the virtual agent

  * **Total Consumer Initiated Interactions** : the sum of interactions that were started by a consumers

  * **Total VA In-Queue Interactions** (calls only): the number of calls where wait-time virtual agents were active while end-users were in a queue

  * **Total VA In-Queue Time** (calls only): the total time that wait-time virtual agents were active while end-users were in a queue

  * **Avg VA In-Queue Time** (calls only): the average time that wait-time virtual agents were active while end-users were in a queue

  * **Virtual Agent Interactions** : provides a graphical representation of the volume of virtual agent interactions, so that you can see the usage patterns and trends over time. It can be a valuable tool in assessing the effectiveness of virtual agents in handling consumer interactions and optimizing their deployment in your contact center. The chart is displayed in 30 minute intervals, providing insights into the usage of virtual agents throughout the day. If you select a date range of more than one day in the reporting dashboard, the chart will automatically aggregate the data to display the total number of virtual agent interactions by day.

  * **Resolved by Virtual Agent** : indicates the number of calls or chats that were resolved by the virtual agent, meaning the virtual agent was able to successfully handle and resolve the issue without escalation.

  * **Planned Transfer** : the occurrences when the virtual agent has answered a call or chat from the queue and escalates it to a human agent in the same queue. For example, the virtual agent understood what the consumer was requesting and sent them to the proper queue/agent/phone number/SIP Endpoint.

  * **Escalated** : the sum of interactions where the virtual agent was unable to handle the issue and it was escalated to a queue where a human agent is assigned. This could be due to the complexity of the issue or the virtual agent's inability to understand the request.

  * **Total Abandons** The number of virtual agent call sessions where the end user left before the virtual agent could resolve the call or escalate to a live agent.

  * **Avg Abandon Time** : the average amount of time that calls or chats waited in the queue before being disconnected by the caller without being accepted by an agent. This helps you assess the efficiency of your queue management and optimize the wait times for better customer experience.

  * **Avg Handle Time** : the average call duration in seconds, plus the average time spent in wrap-up time. AHT starts when the call is assigned to the agent, not when the call is connected to the agent.

  * **Avg Sentiment Score** : the average sentiment score across all interactions handled by the virtual agent. Sentiment analysis helps you gauge the customer's emotional state during the interaction and assess the overall satisfaction level.

  * **CSAT** : the customer satisfaction scores (CSAT) awarded to the entire call or chat interaction. CSAT scores are captured after the interaction ends and provide insights into how satisfied customers were with the virtual agent service. This metric is displayed as a gauge, allowing you to quickly assess the level of customer satisfaction. This only applies if the VA resolved the interaction.

  * **Fallback Response Rate** : the percentage of virtual agent interactions where the virtual agent states that they did not understand the consumer's query, and the interaction resulted in a fallback response. It is calculated as the number of default fallback responses divided by the total number of virtual agent responses, multiplied by 100.

  * **Fallback Response Count** : the total number of virtual agent default fallback responses. It is the sum of interactions where the virtual agent was unable to understand the consumer's query and had to fallback to a default response.

  * **Fallback Responses** : a visual representation of when virtual agents fail to resolve issues, resulting in escalations to human agents. If you select a date range of more than one day, the chart shows the total number of fallback responses by day. Click a day to get additional data




## Tables

These dashboards contain the following metrics tables. Hold the pointer over a table heading to see its description.

  * **Virtual Agent Performance Metrics Table** : the table displays the metrics for each virtual agent

  * **Total Interactions per Virtual Agent** : the total interactions for each virtual agent

  * **Resolution Rate per Virtual Agent** : the resolution rate for each virtual agent

  * **Top Queues** : the virtual agent in the top queues

  * **Virtual Agent Status** : the status of the virtual agent




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
