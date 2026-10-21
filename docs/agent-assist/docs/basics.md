---
url: https://docs.cloud.google.com/agent-assist/docs/basics/
title: Agent Assist basics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:47:51.303413+00:00
---

# Agent Assist basics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/basics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Agent Assist basics Stay organized with collections  Save and categorize content based on your preferences. 

This document is a basic guide to Agent Assist resources. More details about the resources described here can be found in the [reference documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/reference-index). We recommend that you familiarize yourself with this guide before diving into Agent Assist.

## Conversations

A [Conversation](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations) is a resource that represents an exchange between two or more [participants](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics#participants). Every time a conversation participant's utterance is passed to Agent Assist as part of a Conversation resource, a **message** is created and stored for the conversation.

## Conversation profiles

Each conversation is created using a **conversation profile**. Each conversation profile contains a set of parameters that control the suggestions provided to the human agent during a conversation. You can also configure a conversation profile for use with a [virtual agent](https://docs.cloud.google.com/dialogflow/cx/docs), which autogenerates a reply to the end user.

You can create a conversation profile either by using the [Agent Assist Console](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) or by [calling the API directly](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/how-to).

## Participants

Each conversation can have the following [participants](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants):

  * `END_USER`: Participant is an end-user. This is the person the agent is conversing with.
  * `AUTOMATED_AGENT`: Participant is an [automated agent](https://docs.cloud.google.com/dialogflow/cx/docs).
  * `HUMAN_AGENT`: Participant is a human agent.



## Virtual agents

Dialogflow agents are virtual agents that you can build and configure for conversations with your end-users. You can design your system so that end-users initially interact with a [virtual agent](https://docs.cloud.google.com/dialogflow/cx/docs) before being escalated to a human agent. You can use either a [Dialogflow ES](https://docs.cloud.google.com/dialogflow/es/docs/quick/build-agent) or [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent) agent.

## Conversation stages

A conversation with an end-user has multiple stages:

  1. **Connection stage** : The end-user initiates a chat dialog.
  2. **Virtual agent stage** : The end-user is connected to a [Dialogflow virtual agent](https://docs.cloud.google.com/dialogflow/cx/docs). The virtual agent communicates with the end-user and attempts to resolve all issues and requests. You can set up your system to bypass the virtual agent and handoff stages.
  3. **Handoff stage** : If the virtual agent cannot resolve all end-user issues, the conversation is [handed off](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas) to a human agent.
  4. **Agent Assist stage** : The end-user is connected to one or more human agents. [Agent Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist) supplies real-time document and response suggestions to the human agent that are relevant to the conversation.
  5. **Termination stage** : The end-user is disconnected from the text chat.



## Agent desktop

To implement Agent Assist for text-based conversations you must integrate the Agent Assist API into your agent desktop.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
