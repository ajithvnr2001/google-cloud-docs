---
url: https://docs.cloud.google.com/contact-center/insights/docs/virtual-agent-platform/
title: Virtual agent platform \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:33:45.379266+00:00
---

# Virtual agent platform  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/virtual-agent-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Virtual agent platform Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The virtual agent platform is a feature within Quality AI that provides insights into the performance of conversational agents created with Dialogflow and [Customer Experience Agent Studio](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps) (CX Agent Studio). CX Agent Studio is a virtual agent builder that lets you create asynchronous multi-agent systems with bidirectional streaming.

## View platform

Follow these steps to view the platform in the [Customer Experience Insights (CX Insights) console](https://ccai.cloud.google.com/insights/projects).

  1. Click **Quality AI** > **Agents** > **Virtual agent**.
  2. Select an agent.



## Virtual agent performance

The virtual agent platform provides details about virtual agent performance. The platform displays details of both operational and Quality AI metrics.

### Operational metrics

The virtual agent platform displays each of the following metrics as a number or percentage.

**Name** | **Definition** | **Code**  
---|---|---  
Volume or Total sessions | Total number of conversations handled by this agent. | `volume` or `total_sessions`  
Escalation rate | Percentage of conversations escalated to a human agent. | `escalation_rate`  
Turns per session | Average number of turns per conversation. | `turns_per_session`  
No match rate | Percentage of conversations that did not match any intent, applicable only for flow-based virtual agents. | `no_match_rate`  
  
The virtual agent platform displays a graph of the change over time for each of the following metrics.

**Name** | **Definition** | **Code**  
---|---|---  
Volume or Total sessions | Total number of conversations handled by this agent. | `volume` or `total_sessions`  
End-to-end latency breakdown | Amount of time between the end of a user utterance and the start of the following agent utterance. | `percentile_end_to_end_latency`  
Escalation rate | Percentage of conversations escalated to a human agent. | `escalation_rate`  
Escalation type breakdown | Number of conversations per escalation initiator. | `escalation_type_breakdown`  
Tool failure rate | Percentage of tool calls that failed across all uses of the tool in conversations for a specific agent in the selected time period and for the specified conversation medium. | `tool_failure_rate`  
Tool latency | Average latency of a tool call across all uses of the tool in the conversations for the specific agent, in the selected time period and conversation medium. | `tool_latency`  
No match rate | Percentage of conversations that did not match any intent, applicable only for flow-based virtual agents. | `no_match_rate`  
  
#### End-to-end latency (E2E) breakdown

End-to-end (E2E) latency is the amount of time between the end of a user utterance and the start of the following agent utterance. The virtual agent platform calculates E2E latency for every user-agent interaction within both chat and voice conversations.

The virtual agent platform displays a graph titled E2E latency breakdown, which illustrates E2E latency at the utterance level. The y-axis displays time in 50 millisecond increments. The x-axis indicates that you can view E2E latency for tools, the large language model (LLM), and text-to-speech (TTS). Lastly, the graph displays E2E latency as separate bars for three percentile categories: P50 is the 50th percentile, P90 is the 90th percentile, and P99 is the 99th percentile. For example, if the LLM P99 latency is 5 seconds, that means 99% of the utterance-level LLM latency values are less than 5 seconds.

#### Escalation rate

Follow these methods to calculate the escalation rate:

  * **Dialogflow** : Calculated using a signal from Dialogflow.
  * **CX Agent Studio** : Calculated using a signal from the CX Agent Studio [end session](https://docs.cloud.google.com/agent-assist/docs/handoff-cxas#end-session) tracing.



Follow these steps in CX Agent Studio to set up escalation rate with the `end_session` tool:

  1. Add the `end_session` tool to the agent node. Navigate to the **Agent** page in Quality AI. Click **Tools** to view the `end_session` tool.
  2. Provide an agent instruction.

Example: When the customer asks for a live agent, run the `end_session` tool with the argument `{session_escalated = true}`




Within the `end_session` tool, CX Insights relies on the `session_escalated` argument and the `endSession` parameter to compute escalation rate.

#### Escalation type breakdown

The escalation type breakdown shows the number of conversations for each escalation initiator: user or agent. Quality AI determines the escalation initiator by answering the [predefined question](https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-basics#predefined_questions) _Who escalated the conversation?_ You can drill down on an escalation initiator to view a list of conversations with it.

#### Tools

Tool metrics are computed for [Conversational agent tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool). Aggregated metrics like tool latency and failure rates help bot builders identify performance bottlenecks across conversations.

### Quality AI metrics

The virtual agent platform displays the following Quality AI metrics.

  * **Quality score** : Average quality score per scorecard over conversations handled by this agent.
  * **Overall sentiment** : Average [sentiment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/sentiment-analysis) score over conversations handled by this agent.
  * **Sentiment breakdown** : A color-coded bar chart to illustrate the number of conversations of this agent per conversation-level sentiment category: negative, neutral, or positive.
  * **Conversation outcome** : Number of conversations for each possible outcome.
  * **Sentiment by discovery** : Breakdown of the number of conversations per conversation-level sentiment category for this metric.



The platform also displays graphs of the change over time for the following Quality AI metrics.

  * **Quality score** : Percentage of quality scores for all conversations handled by this agent.
  * **Score category breakdown** : Quality score numbers for each predefined category: business, compliance, customer, and any custom categories.



#### Conversation outcome

The conversation outcome graph shows the number of conversations that ended with each of the following possible outcomes:

  * Abandoned
  * Partially resolved
  * Escalated
  * Redirected
  * Successfully resolved
  * Unknown



Compute conversation outcomes using predefined questions in the prebuilt scorecard in Quality AI.

  1. To view outcome data in this graph, run a Quality AI analysis with prebuilt scorecard.
  2. Click an outcome to see a list of conversations with that outcome.



#### Sentiment breakdown

After you run [sentiment analysis](https://docs.cloud.google.com/gemini-enterprise-cx/insights/sentiment-analysis) on all your conversations, the sentiment breakdown chart displays the number of conversations with an overall sentiment in each category: negative, neutral, and positive.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
