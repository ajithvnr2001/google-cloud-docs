---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/retention-deletion/
title: Data retention and deletion \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:53.710682+00:00
---

# Data retention and deletion  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/retention-deletion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Data retention and deletion Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the data retention and deletion behavior for Conversational Analytics API data agent resources and conversation resources.

When a data agent or a conversation resource is deleted, whether manually or automatically, it enters a soft-deletion period before Google Cloud permanently deletes it. For this service, the soft-deletion period does not allow for user-initiated recovery of the deleted resource. Deleting the Google Cloud project that contains the agent also initiates the deletion of all Conversational Analytics API resources within that project.

For a general overview of data deletion on Google Cloud and details about project deletion timelines, see [Data deletion on Google Cloud](https://docs.cloud.google.com/docs/security/deletion).

## Data agents

Conversational Analytics API stores the following information for data agent resources:

  * The full resource name, including project ID, location, and agent ID
  * The data agent's description
  * The data agent's context, including the system description and the data source that the agent uses



Data agents are retained until you request deletion by using the [`projects.locations.dataAgents.delete`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/delete) method or the [`projects.locations.dataAgents.deleteSync`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/deleteSync) method, or until the Google Cloud project that contains the agent is deleted.

When a data agent is deleted, it immediately enters a 30-day soft-deletion period. During this period, the data agent is unavailable for use, but the stored information for the agent is retained. Soft-deleted agents cannot be recovered. After 30 days, Google Cloud permanently deletes the data agent.

To view soft-deleted agents, use the [`projects.locations.dataAgents.list`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/list) method with `show_deleted` set to `true`.

## Conversations

Conversational Analytics API stores the following information for conversation resources:

  * Messages in the conversation, including user prompts and agent responses
  * Topic titles, which can be derived from message content
  * Related metadata, such as timestamps



Conversations are retained until you request deletion by using the [`projects.locations.conversations.delete`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations/delete) method, until they are automatically deleted after 180 days of inactivity, or until the Google Cloud project that contains the agent is deleted.

When a conversation is deleted, it immediately enters a 30-day soft-deletion period, during which it is unavailable and cannot be viewed or recovered. After 30 days, Google Cloud begins to permanently delete the conversation. This process is completed within 63 days of the conversation entering the soft-deleted state.

## What's next

  * Learn more about [security, privacy, risk, and compliance](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/security-privacy-compliance).
  * Learn more about [data deletion on Google Cloud](https://docs.cloud.google.com/docs/security/deletion).
  * Learn more about [Conversational Analytics API architecture and key concepts](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/key-concepts).
  * Learn how to [build a data agent using HTTP and Python](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http).
  * Learn how to [build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
