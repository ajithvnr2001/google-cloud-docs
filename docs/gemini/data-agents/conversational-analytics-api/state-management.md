---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/state-management/
title: State management for data agents \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:39.647381+00:00
---

# State management for data agents  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/state-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  State management for data agents Stay organized with collections  Save and categorize content based on your preferences. 

When you build with the Conversational Analytics API, state management is a key architectural consideration. You manage the API's conversation state and, for applications that use the [Agent Development Kit (ADK)](https://google.github.io/adk-docs/), the framework's session state.

## API state modes

The `chat` method in the Conversational Analytics API supports mutually exclusive context parameters that determine how conversation states are handled.

Use the following table to compare these modes:

Mode | State | Conversation history | Agent | Parameter | Description  
---|---|---|---|---|---  
**Chat with a conversation reference** | Stateful | Managed by the API | Yes | [`ConversationReference`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#ConversationReference) | Continues a stateful conversation by referencing an existing conversation and its associated agent. Google Cloud stores and manages the conversation history. You send only the new message for each turn.  
**Chat with a data agent reference** | Stateless | Managed by your application | Yes | [`DataAgentContext`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#DataAgentContext) | Sends a stateless message that references a saved data agent for context. Your application must manage and provide the full conversation history with each request.  
**Chat with inline context** | Stateless | Managed by your application | No | [`InlineContext`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Context) | Sends a stateless message that provides all context directly in the request. This mode doesn't use a saved data agent. Your application must manage and provide the full conversation history.  
  
## ADK session state

If you use the ADK framework for orchestration, the ADK provides a state management layer that operates independently of the Conversational Analytics API state. Understanding both layers is essential for building multi-agent systems that function correctly.

The ADK uses key prefix conventions to control the scope and lifetime of state variables. Use the following table to evaluate these scopes:

Key prefix | Scope | Lifetime | Visible to | Examples  
---|---|---|---|---  
(no prefix) | Session | Current session only | All agents in the session | Current conversation topic or the results of the last query  
`user:` | User | Across all sessions for the same user | All agents and sessions for the specified user | User preferences, saved data agent IDs, or language settings  
`app:` | Application | Across all sessions for all users | All agents and all users | Global application configuration, shared data agent IDs, or feature flags  
`temp:` | Invocation | Current invocation only | The current agent within the active invocation | Intermediate response data, such as streaming chunks or in-progress calculations  
  
For more information on sharing state in multi-agent systems, see the [ADK documentation](https://google.github.io/adk-docs/agents/multi-agents/).

## How API state and ADK state interact

When you use the Conversational Analytics API with the ADK framework, the state layers function independently:

  * **API state** : If your application uses conversation references (stateful mode), then the API manages the conversation history. If your application uses data agent context or inline context (stateless modes), then the API remains stateless for each call.
  * **ADK session state** : The ADK framework maintains its own session, events, and state variables regardless of the mode that the Conversational Analytics API uses.



For example, when you use the [`ask_data_insights`](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns#schema-driven-adk) or [`ask_data_agent`](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns#governed-adk) tools within the ADK, each call is independently stateless at the API level, even though the ADK maintains the broader session context. The [ADK streaming demo](https://github.com/looker-open-source/ca-demos-and-tools/tree/main/ca-api-adk-streaming) illustrates the recommended pattern for this interaction: a data sub-agent writes parsed response data to the `temp:` state, which downstream agents then read within the same invocation.

## What's next

  * Compare architectural [integration patterns](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns) to determine the best approach for your application.
  * Learn about [Conversational Analytics API architecture and key concepts](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/key-concepts).
  * Explore how to [authenticate and connect to a data source](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication).
  * Learn how to [create and configure an agent with HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http).
  * Learn how to [create and configure an agent with Python](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk).
  * Learn more about [guiding an agent's behavior with authored context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions).
  * Understand [access control with IAM for the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control).
  * Learn how to [protect your data agents and conversations by using CMEK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).
  * Learn how to [render agent responses for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-looker-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
