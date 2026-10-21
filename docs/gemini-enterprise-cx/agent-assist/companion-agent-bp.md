---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-bp/
title: Companion agent best practices \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:15.568646+00:00
---

# Companion agent best practices  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-bp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Companion agent best practices Stay organized with collections  Save and categorize content based on your preferences. 

The companion agent empowers human agents by proactively fetching verified information with the help of tools and automating tasks. It helps agents with on-demand search, leveraging full conversation context for precise answers. Follow these recommendations to optimize the companion agent's real time guidance and the productivity of your human agents.

## Enter model guidance

When you create a companion agent, add [overarching guidance](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ai-coach-best-practices#overarching-guidance) to improve the writing style, output format, and tone of how the companion agent responds and communicates its suggestions to a human agent.

## Add resources

Upload accurate and concise sources of information, and create tools that a human agent could use. The companion agent uses these same resources to provide the most accurate information, useful suggestions, and perform actions in real time during live conversations.

  * **Instructions** : Structured business rules and guidelines for process adherence. Instructions enable companion agent to provide useful next action suggestions and sample responses.
  * **Tool Definitions** : [Tools](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-tools) connect the companion agent to external applications, APIs, and subagents. With tools, the companion agent can automatically retrieve real time data from third party systems or perform specific actions on behalf of the human agent during a conversation.



### Tools

Follow these recommendations to optimize your external tools:

  * Disable the chat input box while your companion agent searches for answers or generates responses to ensure human agents wait for complete information.
  * Add links next to key answers so human agents can quickly click through and verify facts in official company documents.
  * Disable query input or call `cancel_reactive_query` before initiating a new query to ensure your companion agent handles only one active query per session.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
