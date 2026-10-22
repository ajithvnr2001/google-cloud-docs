---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/monitor/
title: Monitoring dashboard \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:10.949429+00:00
---

# Monitoring dashboard  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Monitoring dashboard Stay organized with collections  Save and categorize content based on your preferences. 

You can use the _Monitoring dashboard_ to evaluate the performance of your agent application over time and to find areas for improvement. Monitoring is useful in the following situations:

  * **Performance monitoring** : Analyze real-time and historical data on agent application performance, such as the number of interactions handled, average turns per session, and escalation rate.
  * **Issue detection and resolution** : Identify patterns or trends in end-user interactions where the agent application might struggle to understand requests or provide accurate responses. This can help you identify issues and take corrective actions, such as isolating tool failures, latency issues or updating agent application scripts, or providing additional training.
  * **End user insights** : Gain valuable insights into end-user behavior, preferences, and pain points by analyzing data from agent application interactions. You can use this information to better understand end-user needs, tailor agent application responses, and improve the overall end-user experience.
  * **Resource allocation** : Analyze data on agent application workload, availability, and performance, enabling you to optimize resource allocation. For example, you can identify peak hours when additional agent applications might be required to handle increased inquiries or assign agent applications based on their expertise.



## Open the monitoring dashboard

To open the monitoring dashboard:

  1. Ensure you have enabled interaction logging in the [agent application settings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#agent-application-settings).
  2. At the top of the agent builder, click **Monitor**. The monitoring dashboard appears.
  3. The date range for the data defaults to **Last 1 day** , but you can click this date range to change it.
  4. Click the **Date range** field to select a date range, its by default set to 24 hours
  5. Click **View Conversations** to be redirected to CX Insights to view the full log of conversations and perform conversation and transcript details analysis.



## Dashboard tiles

The monitoring dashboard displays the following tiles:

  * **Total Sessions** : The total number of conversations (sessions) which the agent application has had with end-users. This is also displayed as a time series.
  * **Escalation rate** : The percentage of interactions where the agent application was unable to handle the issue and it was escalated to a human agent. This could be due to the complexity of the issue or the agent application's inability to understand the request. This is also displayed as a time series.
  * **Escalation Count** : The total number of escalations.
  * **Turns per session** : Average number of turns per session.
  * **End to End latency** : End-to-end (E2E) latency is the amount of time between the end of a user utterance and the start of the following agent utterance. The metric calculates E2E latency for every user-agent interaction within both chat and voice conversations.
  * **End to End latency breakdown** : Illustrates E2E latency at the utterance level. The y-axis displays time in 50 millisecond increments. The x-axis indicates that you can view E2E latency for tools, the large language model (LLM), and text-to-speech (TTS). Lastly, the graph displays E2E latency as separate bars for three percentile categories: P50 is the 50th percentile, P90 is the 90th percentile, and P99 is the 99th percentile. For example, if the LLM P99 latency is 5 seconds, 99% of the utterance-level LLM latency values are less than 5 seconds.
  * **Tool failure rate** : Percentage of tool calls that failed across all uses of the tool in conversations for a specific agent in the selected time period and for the specified conversation medium.
  * **Tool latency** : Average latency of a tool call across all uses of the tool in the conversations for the specific agent, in the selected time period and conversation medium.
  * **Overall sentiment** : Average sentiment score over conversations handled by this agent. This is on a scale of -1 to 1, with 0 being neutral and 1 being positive.
  * **Sentiment breakdown** : A color-coded bar chart to illustrate the number of conversations of this agent per conversation-level sentiment category: negative, neutral, or positive.
  * **Conversation outcome** : Shows the number of conversations that ended with each of the following possible outcomes, where compute conversation outcomes use predefined questions in the prebuilt scorecard in CX Insights: 
    * Abandoned
    * Partially resolved
    * Escalated
    * Redirected
    * Successfully resolved
    * Unknown



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
