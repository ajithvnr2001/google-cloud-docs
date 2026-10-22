---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/key-concepts/
title: Conversational Analytics API architecture and key concepts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:55.304414+00:00
---

# Conversational Analytics API architecture and key concepts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/key-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Conversational Analytics API architecture and key concepts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes key concepts for using the Conversational Analytics API (accessed through `geminidataanalytics.googleapis.com` or regional endpoints), which lets you create and interact with data agents that use natural language to answer questions about your structured data. This document describes agent architecture, typical workflows, conversation modes, Identity and Access Management (IAM) roles, and multi-agent system design.

To review available architectural approaches for the Conversational Analytics API and how the API manages conversation context, see [integration patterns](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns) and [state management](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/state-management).

## How data agents work

Conversational Analytics API data agents use _context_ (business information and data), which you provide, and tools (such as SQL and Python) to interpret natural language questions and generate responses from your structured data.

The following diagram illustrates the stages of an agent's workflow when a user asks a question:

![Conversational Analytics API architecture diagram, showing the flow from user input through a reasoning engine, to the final output.](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-agent-architecture.png)

![](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-agent-architecture.png)

As shown in the diagram, when a user asks a question, the agent processes the request in the following stages:

  1. **Input** : The user submits a question in natural language, along with any additional context that you provided previously.
  2. **Data sources** : The agent connects to your data in Looker, BigQuery (including either tables or a graph), Data Studio, or database data sources (AlloyDB, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL in Preview in `v1beta`).
  3. **Reasoning engine** : The core of the agent processes the user's question by using available tools to generate an answer.
  4. **Output** : The agent returns a stream of messages, which can contain text, data, or charts. These messages might include [citations](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#Citation) that link specific parts of the response text to your provided context sources, such as glossary terms or example queries. For some data sources, text messages provide step-by-step insight into the agent's reasoning, report progress on an action, or provide the final answer to your query.



## Workflows for designing and using agents

The Conversational Analytics API supports workflows for _agent creators_ (who build and configure agents) and for _agent consumers_ (who interact with existing agents).

The following diagram illustrates the end-to-end process, from the initial setup by an agent creator to the final interactions with an agent consumer:

![The end-to-end workflow for agent design and use, from creator tasks like creating and sharing to data user tasks like interacting with an agent.](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-agent-workflows.png)

![](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-agent-workflows.png)

The following sections describe the workflows for agent creators and agent consumers in more detail.

### The agent creator workflow

The agent creator is responsible for setting up and configuring agents. This workflow involves the following steps:

  1. **Create agent** : The creator starts by creating a new agent and providing the necessary context, including system instructions and connections to data sources. This step is crucial for enabling the agent to understand and respond to user questions effectively.
  2. **Share the agent** : Once the agent is configured, the creator shares it with other users and sets the appropriate role-based access controls to manage permissions.



### The agent consumer workflow

The agent consumer is typically a business user who needs to get answers from a configured agent. This workflow involves the following steps:

  1. **Find an agent** : The user starts by finding an agent that has been shared with them.
  2. **Ask a question** : The user asks a question in natural language. This question can be a single query or part of a multi-turn conversation.
  3. **Agent "thinks"** : The agent's reasoning engine processes the question. The reasoning engine uses the agent's predefined knowledge and available agent tools (like SQL, Python, and charts) in a "reasoning loop" to determine the best way to answer the question.
  4. **Agent responds** : The agent returns a stream of messages, which can contain text, data, or charts. For some data sources, text messages provide step-by-step insight into the agent's reasoning, report progress on an action, or provide the final answer to your query.



## Conversation modes

Conversational Analytics API agents support different conversation modes that determine how an agent handles conversation history and the persistence of context across interactions. The following conversation modes are available:

  * **Stateless mode** : The agent doesn't store conversation history. Each interaction is treated independently. This mode is useful for applications where you don't need to maintain context across multiple turns.
  * **Stateful mode** : The agent retains context and conversation history, allowing for more contextualized interactions. This mode is useful for applications where you need to maintain context across multiple turns. Using stateful mode is recommended for better accuracy and personalized responses.



Choose a conversation mode based on your application's requirements for conversation history and context persistence.

![The different modes of chat for a Conversational Analytics API agent.](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-chat-modes.png)

![](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-chat-modes.png)

## IAM roles

IAM roles control who can create, manage, share, and interact with Conversational Analytics API agents. The following table describes the key [IAM roles for the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control):

Role | Typical scope | What the role enables | Who might use this role  
---|---|---|---  
Gemini Data Analytics Data Agent Creator (`roles/geminidataanalytics.dataAgentCreator`) | Project | Create agents and inherit owner permissions on the agent. | Any data analyst  
Gemini Data Analytics Data Agent Owner (`roles/geminidataanalytics.dataAgentOwner`) | Project, Agent | Edit, share, or delete agents with other users. | Senior data analyst  
Gemini Data Analytics Data Agent Editor (`roles/geminidataanalytics.dataAgentEditor`) | Agent, Project | Update an agent's configuration or context. | Junior data analyst  
Gemini Data Analytics Data Agent User (`roles/geminidataanalytics.dataAgentUser`) | Agent, Project | Chat with an agent. | Marketer, store owner  
Gemini Data Analytics Data Agent Viewer (`roles/geminidataanalytics.dataAgentViewer`) | Project, Agent | List agents and get their details. You can't edit the agent. | Any user  
Gemini Data Analytics Data Query User (`roles/geminidataanalytics.queryDataUser`) | Project | Query data from supported database sources using the `QueryData` method. | Application developer, Data analyst  
Gemini Data Analytics Stateless Chat User (`roles/geminidataanalytics.dataAgentStatelessUser`) | Project | Chat with an agent without storage of context or conversation history. | Any user  
  
## Systems with multiple agents

You can design complex systems by integrating multiple Conversational Analytics API agents. A common pattern is to use a primary "orchestrator" agent that delegates tasks to one or more specialized agents that handle specific domains, such as sales or marketing data. This approach lets you build a system that can handle a wide range of questions by combining the strengths of multiple agents.

The Conversational Analytics API supports the open [Agent-to-Agent (A2A) protocol](https://a2a-protocol.org/), which provides a standardized interface for discovering capabilities, delegating queries, and streaming structured SQL and chart artifacts across agents. To learn how to implement multi-agent workflows by using the A2A protocol, see [Orchestrate data agents with A2A](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/orchestrate-agents-a2a).

The following diagram illustrates this multi-agent pattern and shows how a primary agent can delegate a data question to a specialized Conversational Analytics agent:

![A primary orchestrator agent delegates a data question to a specialized sales agent, which then returns an answer to the user.](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-multi-agent.png)

![](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-multi-agent.png)

The typical workflow for a multi-agent system involves the following steps:

  1. A business user or data analyst asks a question in natural language, such as "Show me the top three stores by revenue."
  2. A primary "orchestrator" agent delegates the request to the appropriate specialized agent.
  3. A specialized agent receives the delegated request, connects to the relevant data sources, uses its tools to generate the necessary SQL queries and charts, and generates a response.
  4. The specialized agent's response is returned to the user, such as "Stores 4, 9, and 3 have the highest revenue. Here's a chart."



## What's next

After understanding the core concepts of the Conversational Analytics API, explore how to implement these features:

  * Learn how to [orchestrate data agents with A2A](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/orchestrate-agents-a2a).
  * Compare architectural [integration patterns](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns) to determine the best approach for your application.
  * Understand [state management](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/state-management) for data agents and how the API manages conversation context.
  * Explore how to [authenticate and connect to a data source](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication).
  * Learn how to [create and configure an agent with HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http).
  * Learn how to [create and configure an agent with Python](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk).
  * Learn more about [guiding an agent's behavior with authored context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions).
  * Understand [access control with IAM for the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control).
  * Learn how to [protect your data agents and conversations by using CMEK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).
  * Learn how to [render agent responses for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-looker-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
