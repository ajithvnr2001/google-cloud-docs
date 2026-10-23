---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview/
title: Build data agents and chat with your data \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:27.247869+00:00
---

# Build data agents and chat with your data  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Build data agents and chat with your data Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** The Data QnA API is deprecated. If you're migrating from the Data QnA API, see the [migration guide](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/migration-guide) for an overview of key differences and required migration steps. 

Developers can use the Conversational Analytics API, which is accessed through `geminidataanalytics.googleapis.com` or regional endpoints, to build an artificial intelligence (AI)-powered chat interface, or _data agent_. The API uses natural language to answer questions about structured data in BigQuery, Looker, Data Studio, and database data sources (AlloyDB, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL in Preview in `v1beta`). In addition to multi-turn chat, you can use the [`QueryData` method](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/queryData) to run single-turn queries.

With the Conversational Analytics API, you provide your data agent with business information and data (_context_), as well as access to tools such as SQL, Python, and visualization libraries. These agent responses are presented to the user and can be logged by the client application, creating a seamless and auditable data chat experience.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Get started with the Conversational Analytics API

To start using the Conversational Analytics API, review the following documentation to understand the available integration approaches and core concepts:

  * [Architecture and key concepts](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/key-concepts): Understand how data agents process requests, workflows for agent creators and users, conversation modes, and required Identity and Access Management (IAM) roles.
  * [Integration patterns for data agents](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns): Compare architectural approaches to determine the best connection method for your application.
  * [State management](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/state-management): Learn about stateful and stateless conversation modes, how the API manages conversation history, and ADK session state scopes.
  * [Security, privacy, risk, and compliance](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/security-privacy-compliance): Understand the security and compliance options for the Conversational Analytics API.
  * [Conversational Analytics API locations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/locations): Provides an overview of the regional or multi-regional API endpoints that let you control the geographic location of your agent's resources, configuration, and data.



To start building data agents, complete the steps in the setup and prerequisites documentation. For guided walkthroughs, sample applications, SDKs, and other development tools, see [Conversational Analytics API tutorials, demos, and tools](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/tutorials-demos-and-tools).

### Setup and prerequisites

Before you use the API or the examples, complete the following steps:

  * [Enable the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api): Describes prerequisites to enable the Conversational Analytics API.
  * [Access control with IAM](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control): Describes how to use Identity and Access Management to share and manage access to data agents.
  * [Authenticate and connect to a data source](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication): Provides instructions for authenticating to the API and configuring connections to your BigQuery, Lakehouse, Looker, Data Studio, and database data sources (AlloyDB, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL).
  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek): Describes how to use your own encryption keys in Cloud Key Management Service to protect data agents and conversations.
  * [Organization policy constraints](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/organization-policies): Describes how to use predefined organization policy constraints to control resources at the organization, folder, or project level.



### Build and interact with a data agent

After completing the previous steps, use the Conversational Analytics API to build and interact with a data agent by following these steps:

  * [Build a data agent using HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http): Provides a complete example of building and interacting with a data agent by using direct HTTP requests with Python.
  * [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk): Provides a complete example of building and interacting with a data agent by using the Python SDK.
  * [Orchestrate data agents with A2A](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/orchestrate-agents-a2a): Learn how to discover agent capabilities, delegate analytical queries, and stream SQL queries and chart visualizations across multi-agent systems.
  * [Guide agent behavior with authored context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions): Learn how to provide authored context to guide agent behavior and improve response accuracy. You can also view examples of authored context with [BigQuery data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq) and with [Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-looker).
  * [Render a Conversational Analytics API agent response as a visualization](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-visualization): Provides an example of processing chart specifications from API responses and rendering them as visualizations by using the Python SDK and the Vega-Altair library.

**Note:** Rendering visualizations is not supported for database data sources (AlloyDB, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL).



## Best practices

Review the following guides to learn about best practices for using the Conversational Analytics API:

  * [Manage BigQuery costs for your agents](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/manage-costs): Learn how to monitor and manage BigQuery costs for your Conversational Analytics API agents by setting project-level, user-level, and query-level spending limits.
  * [Ask effective questions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/ask-effective-questions): Learn how to craft effective questions for your agents to get the most out of the Conversational Analytics API.
  * [Data retention and deletion](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/retention-deletion): Learn about data retention and deletion for Conversational Analytics API data agents and conversations.
  * [Quotas and limits](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/quotas): Learn about the quotas and limits for the Conversational Analytics API.
  * [Troubleshoot Conversational Analytics API errors](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/troubleshoot-ca-errors): Troubleshoot common Conversation Analytics API errors.
  * [Known limitations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/known-limitations): Provides detailed information about known limitations of the Conversational Analytics API, including limitations of queries, data, visualizations, and questions.
  * [Render agent responses for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-looker-data): Learn best practices for rendering Conversational Analytics API responses in a user interface when you're using Looker data sources.



## API reference and client libraries

  * [Gemini Data Analytics REST reference](https://docs.cloud.google.com/gemini/data-agents/reference/rest): Provides detailed descriptions of API versions, methods, endpoints, and type definitions.
  * [SDKs and development tools](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/tutorials-demos-and-tools#client-libraries): Lists language-specific client libraries.



## Key API operations

The API provides the following core endpoints for managing data agents and conversations. The `v1` endpoints in the following table support BigQuery, Looker, and Data Studio data sources. Because database data sources are in Preview in `v1beta`, specify the corresponding `/v1beta/` paths for database sources.

When constructing these paths (or their corresponding SDK resource names), replace the wildcards (`*`) with your project ID, location identifier (such as `global` or `us`), and the resource ID (such as the agent ID or conversation ID) where applicable.

**Important:** The location in your request path must match the location of the endpoint that you're calling. For example, if you call the `geminidataanalytics.us.rep.googleapis.com` endpoint, specify `us` in your request path (such as `/locations/us`). For details on data residency and endpoint configuration, see [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).Operation | HTTP method | Endpoint | Description  
---|---|---|---  
Create an agent | `POST` | `/v1/projects/*/locations/*/dataAgents` | Creates a new data agent.  
Create an agent synchronously | `POST` | `/v1/projects/*/locations/*/dataAgents:createSync` | Creates a new data agent synchronously.  
Get an agent | `GET` | `/v1/projects/*/locations/*/dataAgents/*` | Retrieves the details of a specific data agent.  
Get Identity and Access Management policy | `POST` | `/v1/projects/*/locations/*/dataAgents/*:getIamPolicy` | Gets the Identity and Access Management permissions that are assigned to each user for a specific data agent. Users with a [Data Agent Owner role](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control#data-agent-owner) can call this endpoint to view the data agent's Identity and Access Management policy before using the `setIAMpolicy` endpoint to share a data agent with other users.  
Set Identity and Access Management policy | `POST` | `/v1/projects/*/locations/*/dataAgents/*:setIamPolicy` | Sets the Identity and Access Management policy for a specific data agent. Users with a [Data Agent Owner role](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control#data-agent-owner) should call this endpoint to share a data agent with other users, which effectively updates those users' Identity and Access Management permissions.  
Update an agent | `PATCH` | `/v1/projects/*/locations/*/dataAgents/*` | Modifies an existing data agent.  
Update an agent synchronously | `PATCH` | `/v1/projects/*/locations/*/dataAgents/*:updateSync` | Modifies an existing data agent synchronously.  
List agents | `GET` | `/v1/projects/*/locations/*/dataAgents` | Lists available data agents in a project.  
List accessible agents | `GET` | `/v1/projects/*/locations/*/dataAgents:listaccessible` | Lists accessible data agents in a project. A data agent is considered accessible if the user that invokes this API has the `get` permission on the agent. You can use the `creator_filter` field to manage which agents this method returns: 

  * `NONE` (default): Returns all data agents that are accessible to the user, regardless of who created the agents.
  * `CREATOR_ONLY`: Returns only the data agents that are accessible to the user and that were created by that user.
  * `NOT_CREATOR_ONLY`: Returns only the data agents that are accessible to the user and that were created by others.

  
Delete an agent | `DELETE` | `/v1/projects/*/locations/*/dataAgents/*` | Removes a data agent.  
Delete an agent synchronously | `DELETE` | `/v1/projects/*/locations/*/dataAgents/*:deleteSync` | Removes a data agent synchronously.  
Create a conversation | `POST` | `/v1/projects/*/locations/*/conversations` | Starts a new, persistent conversation.  
Chat by using a conversation reference | `POST` | `/v1/projects/*/locations/*:chat` | Continues a stateful conversation by sending a chat message that references an existing conversation and its associated agent context. For multi-turn conversations, Google Cloud stores and manages the conversation history.  
Chat by using a data agent reference | `POST` | `/v1/projects/*/locations/*:chat` | Sends a stateless chat message that references a saved data agent for context. For multi-turn conversations, your application must manage and provide the conversation history with each request.  
Chat by using inline context | `POST` | `/v1/projects/*/locations/*:chat` | Sends a stateless chat message by providing all context directly in the request, without using a saved data agent. For multi-turn conversations, your application must manage and provide the conversation history with each request.  
Get a conversation | `GET` | `/v1/projects/*/locations/*/conversations/*` | Retrieves the details of a specific conversation.  
List conversations | `GET` | `/v1/projects/*/locations/*/conversations` | Lists the conversations in a specific project.  
List messages in a conversation | `GET` | `/v1/projects/*/locations/*/conversations/*/messages` | Lists messages within a specific conversation.  
Delete a conversation | `DELETE` | `/v1/projects/*/locations/*/conversations/*` | Deletes a specific conversation. The [Topic Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.topicAdmin) Identity and Access Management role or at least the [`cloudaicompanion.topics.delete`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.topics.delete) Identity and Access Management permission is required to call this endpoint.   
Query data | `POST` | `/v1beta/projects/*/locations/*/conversations:queryData` | Queries data from AlloyDB, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL databases by using natural language.  
Get agent card (A2A) | `GET` | `/v1/a2a/projects/*/locations/*/agents/*/v1/card` | Retrieves the capabilities, skills, and supported extensions for a built-in or custom data agent by using the A2A protocol.  
Send message (A2A) | `POST` | `/v1/a2a/projects/*/locations/*/agents/*/v1/message:send` | Sends a message to a data agent by using the A2A protocol.  
Send streaming message (A2A) | `POST` | `/v1/a2a/projects/*/locations/*/agents/*/v1/message:stream` | Sends a streaming message to a data agent by using the A2A protocol, returning real-time reasoning progress and structured artifacts (such as SQL queries and chart visualizations).  
  
## Support and feedback

To get help or report an issue, contact Customer Care. Follow the guidance on [Create and manage support cases](https://docs.cloud.google.com/support/docs/customer-care-procedures) to open your support case. Use the following guidelines when creating your case:

  * For support for Conversational Analytics API with BigQuery, in the **Select a product** list, select **BigQuery** , and in the **Feature** field, select **AI and Machine Learning::Conversational Analytics API in BigQuery**.
  * For support for Conversational Analytics API with Looker, in the **Select a product** list, select **Looker (original)** , and in the **Feature** field, select **Gemini in Looker::Conversational Analytics API**.

**Note:** Support for the Conversational Analytics API covers technical issues related to the use of the API service. General and custom code debugging are out of scope. Customers are responsible for debugging their own custom code. 

If you have general feedback or questions about the Conversational Analytics API, send an email to [conversational-analytics-api-feedback@google.com](mailto:conversational-analytics-api-feedback@google.com). We don't guarantee a response to email communications, but we do read emails and refer to this feedback during roadmap planning.

You can also [file a feature request](https://issuetracker.google.com/issues/new?component=1747873&template=2131795) for new Conversational Analytics API functionality.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
