---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/
title: Agent Platform Sessions overview \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:55:14.927519+00:00
---

# Agent Platform Sessions overview  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Agent Platform Sessions overview Stay organized with collections  Save and categorize content based on your preferences. 

Agent Platform Sessions maintains the history of interactions between a user and agents. Sessions provide definitive sources for long-term memory and conversation context.

You have several options to use Agent Platform Sessions:

  * [Agent Development Kit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-adk): Once you deploy your Agent Development Kit (ADK) agent to Gemini Enterprise Agent Platform, session management is handled automatically.

  * [API calls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-api): You can make direct API calls to Agent Platform Sessions if you don't want to manage sessions using an ADK agent.




## Core concepts

  * **Session** : A session represents the chronological sequence of messages and actions (events) for a single, ongoing interaction between a user and your agent system.

  * **Event** : An event stores the content of the conversation, as well as the actions taken by the agents such as function calls. Events support a flexible schema to accommodate custom data and different frameworks.

  * **State** : A state holds temporary data relevant only during the current conversation.

  * **Memory** : Memory is personalized information that can be accessed across multiple sessions for a particular user. The agent can use memories to personalize responses to the user and ensure cross-session continuity.




## Core functionalities

The core functionalities of Agent Platform Sessions include the following:

  * **Starting new conversations** : Create new sessions when a user begins an interaction with an agent.

  * **Resuming existing conversations** : Retrieving a specific session so the agent can resume a conversation that has been paused.

  * **Saving progress** : Append new interactions (events) to a session's history to update the session.

  * **Listing conversations** : Find the active session threads for a particular user and application.

  * **Cleaning up** : Delete session objects and their associated data when conversations are finished or no longer needed.




## What's next

  * [Manage sessions using ADK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-adk).
  * [Manage sessions using API calls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
