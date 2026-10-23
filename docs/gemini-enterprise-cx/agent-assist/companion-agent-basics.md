---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-basics/
title: Companion agent basics \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:09.066587+00:00
---

# Companion agent basics  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-basics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Companion agent basics Stay organized with collections  Save and categorize content based on your preferences. 

The companion agent works with the resources and choices you provide to understand the end user's intent. It guides conversations to the intended outcome, in three phases:

  1. You provide resources like instructions, tools, and intended outcomes.

  2. The companion agent uses an LLM to respond to your configuration. The LLM uses all the provided resources to analyze human agent and end user conversations, generate suggestions, and automate tasks.

  3. The companion agent displays the results in a unified interface that seamlessly merges the automatic suggestions and conversation assistance. Human agents can see and interact with the interface.




## Visual interface

The companion agent displays the following windows:

  * Next best action
  * Interactive panel



To embed the companion agent interface in your agent desktop, use the [companion agent UI module](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-companion-agent).

### Next best action

When you start a customer service conversation, the next best action panel offers suggestions through guidance instructions and configured tools. This window displays suggested actions a human agent can take during a conversation. Some of the next best actions include related resources that extract information from your resources.

### Interactive panel

The interactive panel provides a conversational assistant where a human agent can enter questions related to a conversation.

The interactive panel consists of the following tabs:

  * **Your assistant** : In this tab, human agents can do the following:

    * Ask questions about a conversation
    * Web search
    * Find a tool to resolve customer queries. The companion agent takes the answer directly from your resources and gives relevant suggestions to the human agent. If a human agent asks something unrelated to the conversation, the companion agent performs a web search provided Google Search tool is added and enabled for the companion agent.
  * **Tool history** : This tab displays the tools that have been run in the companion agent.

  * **Settings** : On this tab, a human agent can change the display to use dark or light mode.




## Streaming reactive companion API

The streaming reactive companion API implements the companion agent's on-demand assistant mode. In this mode, companion agent analyzes a request in context. It uses both the human agent's prompt and the complete conversation history to stream real-time status updates, small response tokens, and verified source references.

### Example

  * Searching web Information 
    * Agent question: _What is the official USPS postal holiday schedule for 2026?_
    * How it works: If internal articles don't have the answer, the companion agent searches Google, shows a brief status message like _Searching Google_ , and provides the answer with links to public web pages.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
