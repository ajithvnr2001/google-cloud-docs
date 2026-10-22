---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/voice-virtual-agent-dashboard/
title: Voice virtual agent dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:51.484500+00:00
---

# Voice virtual agent dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/voice-virtual-agent-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Voice virtual agent dashboard Stay organized with collections  Save and categorize content based on your preferences. 

The dashboard displays metrics such as sentiment ratings, resolution rates, CSAT, and other performance data for virtual agents. Dashboard filters include Agent, Queue, and Timeframe.

If you have enabled the Voice Virtual Agent feature you can access this dashboard. To view the dashboard go to **Dashboards > Virtual Agents > Calls**.

## Filters

Filters (Agent, Queue, Timeframe) are available at the top of the dashboard.

## Metrics

This table describes each metric available in the **Voice Virtual Agent Dashboard**

**Metric** | **Description**  
---|---  
Total Sessions | The number of VA call sessions.  
Total Volume per Hour | The number of VA call sessions divided by the number of hours between provided from/to timestamps  
Consumer Initiated Sessions | The number of VA call sessions started by the consumer directly (for example, not the Agent).  
Transferred by Live Agent Sessions | The number of VA call sessions started by a transfer from a Live Agent call session by the Agent.  
Total Responses | The number of VA responses across all call sessions.  
Resolved by Virtual agent | The number of VA call sessions that the VA resolved. Usually a resolved call is one where the VA resolves the issue from the customer and gets some acknowledgement in the call that it has done so.  
Planned Transfer | Indicates when the voice virtual agent transferred the call to a human agent through planned interaction. For example, the virtual agent understood what the consumer was requesting and sent them to the proper queue/agent. This formats as True or False.  
Escalation | The number of VA call sessions that the VA escalated to an agent by explicit consumer intervention (either through clicking the escalate button or saying in a virtual agent call that they would like to talk to a human).  
Abandoned* (VA) | The number of VA call sessions where the end user left before VA could resolve the call or escalate to a live agent.  
Average Handle Time | The average time that a VA call session lasts.  
Average Abandon time* (VA) | The average time that an abandoned VA call session lasts.  
Average Session Responses | The average number of VA responses in a given VA session  
Rate of Misunderstanding | The average number of fallback responses a VA makes in a given call session. A fallback response is a response that is given from the VA when it doesn't have a rule for what to say next with a given customer response.  
Sessions over time | Time series data that plots the number of sessions over time within the given time range the query is operating in  
Rate of Misunderstanding over time | Time series data that plots the rate of misunderstanding over time within the given time range.  
Rate of Misunderstanding by Virtual Agent | A breakdown of Rate of Misunderstanding that computes the rate of misunderstanding for each virtual agent.  
Sentiment Score | Average Sentiment Score of VA Sessions. Calculation: _(Total Sentiment Score of all call sessions / Total no of Virtual Agent messages)_  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
