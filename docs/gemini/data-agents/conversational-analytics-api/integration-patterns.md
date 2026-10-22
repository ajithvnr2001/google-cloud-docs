---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns/
title: Integration patterns for data agents \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:23.321368+00:00
---

# Integration patterns for data agents  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Integration patterns for data agents Stay organized with collections  Save and categorize content based on your preferences. 

This page describes integration patterns for embedding data agent experiences into your applications. These patterns range in complexity from an embedded chat component to an orchestrated multi-agent system.

This guide is intended for cloud architects and data engineers who design generative AI applications. You should have a foundational understanding of Google Cloud concepts, Identity and Access Management (IAM), and REST APIs. You should also be familiar with the architecture of the data source that your application uses.

## Overview of integration patterns

This guide is organized into the following primary tracks, each of which is based on your starting point:

  * **Looker track** : Select this track if you want to provide chat functionality through Looker embedding, the Looker API, or the Conversational Analytics API.
  * **BigQuery and database track** : Select this track if you're building a custom application that uses BigQuery, Data Studio, or a supported operational database.



The following table summarizes the available integration patterns:

Integration pattern | Description | Data source  
---|---|---  
**Looker iframe embed** | Adds the standard chat interface to an application that requires minimal code. | Looker  
**Looker API and SDKs** | Builds a custom chat interface that uses the Looker API for authentication. | Looker  
**Conversational Analytics API (Looker source)** | Manages Looker data agents as Google Cloud resources that work across multiple surfaces and multi-agent systems. | Looker  
**Direct API (single-agent)** | Uses a direct API integration for text-to-answer flows. | BigQuery, databases, Looker  
**Direct API (orchestrator)** | Routes queries between the API and other tools by using function calling. | BigQuery, databases, Looker  
**ADK (schema-driven) with`BigQueryToolset`** | Generates rapid insights from table references by using the `ask_data_insights` tool. | BigQuery  
**ADK (governed) with`DataAgentToolset`** | Queries pre-configured data agents that use the `ask_data_agent` tool to ensure consistent behavior. | BigQuery, databases, Looker  
**ADK (custom streaming)** | Supports real-time streaming of charts and SQL by using a custom agent class. | BigQuery, databases, Looker  
**MCP with`McpToolset` or `ToolboxToolset`** | Connects applications to data tools that use the Model Context Protocol (MCP). | BigQuery Looker  
**A2A protocol** | Enables secure collaboration between specialized agents that operate on different systems. | Framework dependent  
  
## Integration options for Looker

If you use Looker, you can provide [Looker Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) to your users through the following patterns:

  * Embed with iframes: A low-code pattern that adds the standard chat interface to an existing application.
  * Build with the Looker API and SDKs: A flexible approach that lets you build a custom frontend through Looker authentication and agent management.
  * Use the Conversational Analytics API: A direct integration with the API that allows data agents to be used across multiple Google Cloud surfaces.



### Summary of Looker integration patterns

The following table summarizes the primary integration patterns for Looker:

Pattern | Best for | Advantages | Considerations  
---|---|---|---  
**Embed with iframes** : A low-code method to quickly add the standard Looker chat experience to an application. | Teams that require a production-ready conversational analytics experience with minimal custom development. | 

  * Requires minimal code to implement.
  * Automatically enforces the existing Looker security model.
  * Doesn't require separate Google Cloud authentication.
  * Supports the Looker Embed SDK, which accelerates development by managing iframe lifecycles and event passing.

| 

  * Offers limited UI customization and depends on the standard Looker chat user interface.
  * Your Looker instance must be Looker-hosted.

  
**Build with the Looker API and SDKs** : A flexible approach to building a custom chat interface while keeping authentication and agent management within Looker. | Teams that require a custom chat user experience but want to keep user authentication and agent management within the Looker ecosystem. This pattern is ideal for applications that already use Looker embedding or the API. | 

  * Provides a single authentication layer and full control over the user interface.
  * Simplifies the architecture for existing Looker customers.
  * Uses the Looker semantic layer to improve query accuracy.
  * Doesn't require separate Google Cloud authentication.

| 

  * Requires Looker API development expertise.
  * Limited to Looker data sources.
  * Agents are managed within Looker and aren't portable to other Google Cloud services.

  
**Use the Conversational Analytics API** : Direct integration with the API to manage agents as cloud-level resources. | Looker customers who require cross-platform portability for their data agents. | 

  * Ensures that the data agent is portable across all Google Cloud surfaces.
  * Governed centrally by IAM.
  * Lets you integrate data agents into ADK or MCP workflows.

| 

  * Requires that you manage the full integration stack, including both Google Cloud and Looker authentication.
  * Data agents are managed independently of the Looker user interface.

  
  
### Embed with iframes

You can [embed Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-embedding) as an iframe to deliver the chat experience outside of the Looker UI. This pattern is a direct way to provide Conversational Analytics that requires no custom UI development, backend orchestration, or API state management. To use this pattern, you add a preformatted URL into your application.

The Looker [Embed SDK](https://github.com/looker-open-source/embed-sdk) provides tools that manage tasks such as secure URL generation, iframe lifecycle management, and JavaScript event passing between the host application and the iframe. You can embed the **Agents** page, the **Conversations** page, or a specific conversation by adding a preformatted URL into your application.

You can use the following authentication methods for embedded content:

  * [Private embedding](https://docs.cloud.google.com/looker/docs/private-embedding): Authenticates users with their existing Looker credentials. When you set the embed URL as the iframe source, users sign in with their Looker accounts. This method automatically enforces existing roles, content access, and data-level permissions, such as [access filters](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter) or [access grants](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant), without requiring additional IAM configuration or token mapping.
  * [Signed embedding](https://docs.cloud.google.com/looker/docs/signed-embedding): Authenticates users through your application by using single sign-on (SSO). You construct a signed URL that includes the Conversational Analytics content path, which lets you dynamically specify exactly which permissions to grant.



### Build with the Looker API and SDKs

For more flexibility in the chat experience, you can use the [`ConversationalAnalytics` methods](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ConversationalAnalytics) in the Looker API or use a [Looker SDK](https://docs.cloud.google.com/looker/docs/api-sdk) to build a custom application. This approach lets you build a custom frontend that communicates directly with Looker endpoints.

Integrating with the Looker API provides the following benefits:

  * You only manage authentication with Looker. There is no need to authenticate separately with the Conversational Analytics API.
  * For applications that already use Looker embedding or the API, this pattern simplifies the project architecture by avoiding secondary authentication mechanisms and eliminating the need to manage external data agents.
  * You have full control over the chat interface, conversation flow, and how the application renders results (such as charts and tables).

**Note:** Agents that you create within Looker Conversational Analytics are managed by Looker and aren't available to other Google Cloud resources. If you must share the same agent across multiple platforms, such as a custom web app and Google Chat, use the Conversational Analytics API with a Looker data source.

For a reference implementation, see the [Conversational Analytics Looker API guide](https://github.com/looker-open-source/ca-demos-and-tools/tree/main/looker-api-ca-demo) on GitHub.

### Use the Conversational Analytics API with Looker data

You can integrate directly with the Conversational Analytics API at `geminidataanalytics.googleapis.com` if you need to perform any of the following tasks:

  * Share the same data agent across multiple Google Cloud surfaces, such as custom web applications, Google Chat, and Gemini Enterprise.
  * Combine Looker data sources with BigQuery or operational database sources in a single multi-agent system.
  * Manage your data agent as a cloud-level resource that is governed by IAM rather than the Looker permission model.

**Note:** While Identity and Access Management (IAM) governs access to the data agent, the Looker permissions that the user has determine data access if you use a user access token. For more details, see the [authentication documentation](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication).

For more information about common architecture patterns for the Conversational Analytics API, see Integration options for BigQuery and databases.

## Integration options for BigQuery, Data Studio, and databases

This section describes architectural patterns for applications that use BigQuery, Data Studio, or supported Google Cloud operational databases to build custom experiences with the Conversational Analytics API.

If you use the Conversational Analytics API with a Looker data source, the patterns that are described in this section also apply to your integration.

The Conversational Analytics API provides the following primary methods for interacting with data:

  * [`chat` method](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat): Supports BigQuery, Looker, Data Studio, and operational databases.
  * [`queryData` method](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/queryData): Supports operational databases such as AlloyDB, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL.

**Note:** While the architectural patterns that are described in this section apply broadly across supported data sources, some framework implementations, such as the ADK prebuilt BigQuery toolsets, are designed specifically for BigQuery.

When you build a custom application, you can use one or more of the following integration patterns:

  * Direct API integration: A custom approach that provides the most flexibility but requires you to build the infrastructure for authentication, conversation management, and response parsing.
  * Framework-driven orchestration (ADK): An approach that uses the Agent Development Kit (ADK) for multi-agent routing, tool execution, and state management.
  * Vertical integration (MCP): An approach that uses the Model Context Protocol (MCP) to provide a uniform way to connect AI applications to tools and data sources across different environments.
  * Horizontal orchestration (A2A): An approach that uses the Agent-to-Agent (A2A) protocol to allow specialized agents on different systems to collaborate securely without requiring custom integration code.



### Summary of BigQuery and database integration patterns

The following table summarizes the specific implementation patterns for BigQuery and operational databases:

Pattern | Best for | Advantages | Considerations  
---|---|---|---  
**Single-agent integration (direct API)** : A pattern where your application calls the API directly to return insights from your data sources. | Single-agent applications, prototypes, or microservices that require direct control over every API call. | 

  * Provides granular control with no framework dependencies.
  * Provides the simplest architecture for single-agent use cases.
  * Supports both stateful and stateless modes.

| 

  * Requires that you build all infrastructure for authentication, state management, response parsing, error handling, streaming, and deployment.
  * Doesn't scale well for multi-agent scenarios.

  
**Custom orchestrator (direct API)** : A pattern that uses a root agent and function calling to route queries between the Conversational Analytics API and other tools or services. | Applications that combine data queries with other tasks, such as email or documents, in a single conversational flow. | 

  * Provides maximum orchestration control with no framework dependencies.
  * Lets you define exactly how the model routes between tools.
  * Works with any Gemini model.

| 

  * Requires that you manually manage tool definitions, conversation loops, multi-turn state, error handling, and deployment.
  * Development overhead might become burdensome compared to using a framework such as the ADK.

  
**Schema-driven integration with`BigQueryToolset` (ADK)**: A pattern that uses table references to return data insights quickly. | Rapid prototyping, internal tools where data governance is less critical, or scenarios where data insights are one of several capabilities in an ADK agent. | 

  * Provides the fastest integration path within the ADK framework.
  * Requires no data agent pre-configuration.
  * Works directly with database table names.

| 

  * Lacks semantic governance and generates SQL from schema inference only.
  * Operates in a stateless mode at the API level.
  * Provides text-only answers and doesn't support charts.

  
**Governed integration with`DataAgentToolset` (ADK)**: A pattern that queries a pre-configured data agent by referencing the agent's ID. | Production applications that require consistent data access or multi-agent systems where the data agent is a trusted, reusable component. | 

  * Provides semantic governance and consistent behavior across all consumers.
  * Improves accuracy by using verified queries and a business glossary.
  * Ensures that data agents are reusable across ADK, MCP, and direct API integrations.

| 

  * Requires that you pre-configure data agent resources.
  * Operates in a stateless mode at the API level.
  * Returns text-only answers and doesn't support charts.

  
**Custom sub-agents (ADK)** : A pattern that uses a custom agent class to connect directly to the API and stream data chunks back to the user. | User-facing applications where low response latency is a priority or multi-agent pipelines where data retrieval feeds downstream agents. | 

  * Provides real-time streaming feedback.
  * Accesses all response types, such as charts, tables, and SQL.
  * Composable with other ADK agents through session state.

| 

  * Requires more development effort to build a custom ADK agent class.
  * Requires that you manage the streaming connection and response parsing directly.

  
**Model Context Protocol (MCP)** : A pattern that uses an open standard to connect AI applications to data sources and tools across different environments. | Organizations that require tool interoperability across multiple AI clients and IDEs, or teams that need the same data tools to be accessible from the ADK framework, IDEs, and custom applications. | 

  * Uses a universal tool standard that works with any MCP-compliant client.
  * Decouples tool implementation from consumer applications.
  * Offers managed server options, such as the Google Cloud MCP server.

| 

  * Requires an additional infrastructure layer for the toolbox server.
  * Provides looser integration than ADK toolsets.
  * Depends on the evolving ecosystem of the MCP Toolbox.
  * Operates in a stateless mode that requires that you manage multi-turn state externally.

  
**Agent-to-Agent (A2A)** : A pattern that uses the A2A protocol, an open standard that lets specialized agents on different systems collaborate securely without requiring custom integration code. | Highly distributed enterprise environments where a central routing agent must delegate tasks to data agents that operate on different systems or networks. | 

  * Reduces the need for custom integration code between disparate frameworks.
  * Ensures seamless cross-platform interoperability.
  * Provides secure and standardized capability discovery.

| 

  * Introduces minor network latency compared to internal sub-agents.
  * Requires that you configure A2A server settings.

  
  
### Direct API integration

Direct API integration provides granular control over your application's logic and architecture but requires you to build the supporting infrastructure. With this approach, you're responsible for tasks such as authentication, conversation management, response parsing, and deployment.

This section covers the following topics:

  * Single-agent integration: A pattern where your application calls the Conversational Analytics API directly to return insights from your data sources.
  * Custom orchestrator integration: An advanced pattern that uses a root agent and function calling to route queries between the Conversational Analytics API.



#### Single-agent integration

With a single-agent integration, your backend directly calls the Conversational Analytics API by using REST or a [client library](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/tutorials-demos-and-tools#client-libraries) and passes the user's query and context. This pattern is suitable for low-complexity applications, such as web apps, internal chat tools, or microservices, that use a straightforward text-to-answer flow. You can also use this approach for prototyping and proof-of-concept work.

This pattern supports both _stateful_ chat, where Google manages the conversation history, and _stateless_ chat, where your application manages the history.

For reference implementations, see the [Conversational Analytics API quickstart](https://github.com/looker-open-source/ca-api-quickstarts) or the [Conversational Analytics API golden demo](https://github.com/looker-open-source/ca-demos-and-tools/tree/main/ca-api-golden-demo) on GitHub.

#### Custom orchestrator integration

With this approach, you build a root agent that acts as the primary entry point and coordinator for your application. The root agent uses a standard Gemini model that is equipped with tools through [function calling](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling). When a user asks a data-related question, the root agent emits a tool call to the Conversational Analytics API, receives the result, and can then continue reasoning or call other tools downstream.

Function calling involves the following stages:

  1. **Declare** : Define tool schemas as `FunctionDeclaration` objects that include parameter definitions.
  2. **Invoke** : The model returns a structured `functionCall` message that contains the function name and arguments.
  3. **Execute** : Your application performs the API call and returns the result in a `FunctionResponse` message.
  4. **Synthesize** : The Gemini model uses the result to generate a final answer or to determine the next action.



This approach is suitable for applications where users might ask for data insights alongside other tasks. For example, a user might ask the agent to "Show me sales, and then draft an email to the sales team." The root agent can route the data question to the Conversational Analytics API and use other tools for non-data tasks.

For a reference implementation, see the **orchestrate** or **multimodal** pages in the [Conversational Analytics API golden demo](https://github.com/looker-open-source/ca-demos-and-tools/tree/main/ca-api-golden-demo) on GitHub.

### Framework-driven orchestration (ADK)

The [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) is a code-first framework for building AI agents that manages the complexity of multi-agent routing, tool execution, and state management. The ADK framework is the same framework that powers Gemini Enterprise.

By using the ADK, you can chain the Conversational Analytics API with other tools and agents to perform complex actions.

This section covers the following topics:

  * Schema-driven integration: A pattern that uses the `ask_data_insights` tool from the [`BigQueryToolset`](https://google.github.io/adk-docs/integrations/bigquery/) toolset to return data insights from BigQuery table references.
  * Governed integration: A pattern that uses the `ask_data_agent` tool from the [`DataAgentToolset`](https://google.github.io/adk-docs/integrations/data-agent/) toolset to query a pre-configured data agent by referencing the agent's ID.
  * Advanced UX integration with custom sub-agents: A pattern that uses a custom sub-agent component to connect directly to the Conversational Analytics API and stream data chunks back to the user asynchronously.



#### Schema-driven integration with `BigQueryToolset`

The [`BigQueryToolset`](https://google.github.io/adk-docs/integrations/bigquery/) toolset in the ADK framework includes a prebuilt `ask_data_insights` tool. To use this tool, you pass table names and the user's question to the tool, which then calls the Conversational Analytics API by using inline context.

When you call the tool, it sends a stateless request that includes the specified BigQuery table references to the Conversational Analytics API. The API infers the database schema, generates and executes the SQL query, and returns a text answer. The result is then passed back to the ADK agent as a tool response.

This pattern is an effective way to add conversational analytics to an agent quickly. However, because the call to the API is stateless and lacks governance, the API generates SQL that's based entirely on the table schema without semantic guardrails. This pattern is faster to deploy but riskier for production business logic where naming conventions, business logic, or access controls apply.

#### Governed integration with `DataAgentToolset`

The [`DataAgentToolset`](https://google.github.io/adk-docs/integrations/data-agent/) toolset in the ADK framework provides a prebuilt integration that references a pre-configured data agent by its ID. The ADK agent passes the user's question to the `ask_data_agent` tool, which calls the Conversational Analytics API with the specified data agent context.

You can create a data agent programmatically by using the Conversational Analytics API or through the [Agent Catalog](https://docs.cloud.google.com/bigquery/docs/create-data-agents) in the Google Cloud console. A data agent comes equipped with the following components:

  * **Knowledge sources** : Tables, views, or user-defined functions (UDFs) that the agent can query
  * **Structured context** : Descriptions for tables and columns that help the agent understand the underlying data
  * **Instructions** : Additional guidance for the agent to interpret and query the data sources
  * **Verified queries** : Pre-validated SQL queries that serve as examples for common questions
  * **Glossary** : Business term definitions that help the agent understand domain-specific language



For an in-depth guide on creating agents through the Agent Catalog, see the [conversational analytics in BigQuery](https://codelabs.developers.google.com/ca-in-bigquery) codelab.

Because the agent is defined as a governed unit, it uses the same trusted logic, context, and guardrails regardless of which application or sub-agent calls it.

#### Advanced UX integration with custom sub-agents

The `BigQueryToolset` and `DataAgentToolset` toolsets don't return results to the user until the API request finishes processing. Because the ADK framework treats the API as a tool that blocks responses until completion, longer-running queries might leave users without feedback.

As an alternative for applications where low response latency is a priority or where data retrieval feeds downstream agents, you can build a custom ADK agent class that connects directly to the Conversational Analytics API and asynchronously streams data in chunks back to the user. This pattern supports the following response types as they're produced:

  * **Thought messages** : The data agent's reasoning process as it interprets the question.
  * **Progress messages** : Status updates during data retrieval for data sources.
  * **Query generation** : The generated SQL or Looker query, which is streamed as it's produced.
  * **Data** : The data results in JSON format.
  * **Visualization** : Vega-Lite chart specifications.
  * **Summary** : The final text-based answer.



For a full list of the types of data that are returned, see the [`SystemMessage`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message#SystemMessage) type in the API reference documentation.

This asynchronous approach ensures that users don't have to wait for a complex data retrieval process to finish completely. As the data agent flows through the query process, it continuously shares incremental updates—such as text summaries, raw data, or chart configurations—into a temporary, shared workspace. This data can then be rendered for the user in real time and shared with specialized sub-agents to perform additional tasks.

For a reference implementation that includes a root agent, a data sub-agent, and a visualization agent, see the [ADK streaming demo](https://github.com/looker-open-source/ca-demos-and-tools/tree/main/ca-api-adk-streaming) on GitHub.

### Vertical integration (MCP)

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard that provides a uniform way for AI applications to connect to external tools and data sources. MCP standardizes the interface between AI models and the tools that they use.

This section covers the following topics:

  * MCP Toolbox for Databases: Describes prebuilt tools for connecting to BigQuery and Looker.
  * MCP implementation patterns for standalone and ADK architectures: Describes patterns for using MCP as a standalone server or within an Agent Development Kit (ADK) workflow.



#### MCP Toolbox for Databases

While there is no dedicated Conversational Analytics API MCP server, you can access the API through the [MCP Toolbox for Databases](https://mcp-toolbox.dev/documentation/introduction/) server. This open-source server provides prebuilt, MCP-compatible tools that expose the `chat` method in the Conversational Analytics API:

  * [`bigquery-conversational-analytics`](https://mcp-toolbox.dev/integrations/bigquery/tools/bigquery-conversational-analytics/): Wraps the `chat` method for BigQuery data sources.
  * [`looker-conversational-analytics`](https://mcp-toolbox.dev/integrations/looker/tools/looker-conversational-analytics/): Wraps the `chat` method for Looker data sources.



MCP is an interoperability layer that exposes analytics capabilities as tools to MCP-compatible clients rather than a separate execution model of the Conversational Analytics API.

#### MCP implementation patterns for standalone and ADK architectures

You can implement MCP through the following patterns:

Pattern | Details  
---|---  
**Standalone MCP (without ADK)** |  Use the MCP Toolbox for Databases server as a standalone server to connect to any MCP-compliant client. This pattern is commonly used for the following tasks:

  * **IDE integration** : Connect an IDE—such as Antigravity, Cursor, or VS Code—to the server to query data conversationally from an editor.
  * **Custom MCP client** : Build an application that uses the server to provide a uniform tool interface across multiple AI providers.
  * **Gemini CLI** : Use the CLI as an MCP client for terminal-based data conversations.

  
**MCP within ADK** |  The ADK framework provides the following mechanisms for integrating MCP servers into agent workflows:

  * [`ToolboxToolset`](https://adk.dev/integrations/mcp-toolbox-for-databases/#authentication): A specialized variant for the MCP Toolbox for Databases server that supports multiple authentication methods.
  * [`McpToolset`](https://adk.dev/tools-custom/mcp-tools/#mcptoolset-class): Connects an ADK agent to any MCP server by using either local or remote MCP server connections. Automatically discovers the server's tools and exposes them to the agent.

  
  
You can also build MCP servers by using the FastMCP framework to expose tools that were built with the ADK framework to any MCP-compliant client. This approach makes your ADK agents available as tools in other ecosystems.

Choose an integration pattern that meets the specific architectural requirements of your application:

  * Using built-in Agent Development Kit (ADK) toolsets, such as `BigQueryToolset` or `DataAgentToolset`, provides tighter integration with no external server dependencies. This approach is ideal for systems that exist entirely within the ADK framework.
  * Using the tools in the MCP Toolbox provides interoperability across MCP-compliant clients. This approach is ideal for data tools that must serve multiple consumer applications or third-party IDEs.



### Horizontal orchestration (A2A)

The [Agent-to-Agent (A2A) protocol](https://a2a-protocol.org/) is an open standard that enables specialized agents on different systems to communicate and collaborate securely without requiring custom integration code.

As systems scale, organizations often deploy multiple specialized agents that are built on different frameworks or cloud infrastructures. A2A establishes a universal messaging tier for these autonomous agents. Instead of using custom APIs, each agent publishes an _agent card_ , which is a discoverable profile that details the agent's capabilities, supported data formats, and security requirements.

When a central orchestrator or peer agent requires analytical data, it securely delegates the task to a data agent through structured A2A messaging. The data agent processes the request autonomously and returns the findings, which decouples the execution logic from the requester.

To learn how to discover agent cards, send messages, and stream structured artifacts by using the A2A protocol, see [Orchestrate data agents with A2A](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/orchestrate-agents-a2a).

## Choose an integration pattern

Use the following table to compare the complexity, governance, and capabilities of each integration pattern.

Complexity levels are defined as follows:

  * **Low** : Patterns that require minimal custom code and rely on prebuilt user interfaces or tools.
  * **Medium** : Patterns that require custom frontend development and API or SDK integration but avoid complex backend orchestration infrastructure.
  * **High** : Patterns that require full-stack application development, conversation state management, multiple authentication layers, or intermediate orchestrator infrastructure.
  * **Varies** : Patterns where the complexity depends on the underlying integration method that you choose.

Integration pattern | Complexity | Customization | Agent governance | Access control | Multi-agent | Streaming | Portability  
---|---|---|---|---|---|---|---  
**Looker iframe embed** | Low | Low | Managed through Looker | Looker | No | Built-in | Looker only  
**Looker API and SDKs** | Medium | High | Managed through Looker | Looker | No | Built-in | Looker only  
**Conversational Analytics API with Looker source** | Varies | High | Managed through the API | Looker and IAM | Yes | Yes | Any Google Cloud surface  
**Single-agent (direct API)** | Medium | High | Managed through the API | IAM | No | Yes (supported) | Any Google Cloud surface  
**Custom orchestrator** | High | Very high | Managed through the API | IAM | Manual | Manual | Any Google Cloud surface  
**Schema-driven with`BigQueryToolset` (ADK)** | Low | Medium | None (schema inference) | IAM | Yes (ADK) | No (blocking) | ADK ecosystem  
**Governed with`DataAgentToolset` (ADK)** | Low | Medium | Managed through the API | IAM | Yes (ADK) | No (blocking) | ADK ecosystem  
**Custom streaming sub-agent (ADK)** | High | Very high | Managed through the API | IAM | Yes (ADK) | Yes (custom) | ADK ecosystem  
**Standalone MCP** | Medium | Medium | None (schema inference) | IAM | No | No | Any MCP client  
**MCP within ADK** | Medium | High | None (schema inference) | IAM | Yes (ADK) | No | ADK and MCP clients  
**A2A Protocol** | High | High | Framework dependent | IAM | Yes | Yes | Cross-platform  
  
## What's next

  * Learn about [Conversational Analytics API architecture and key concepts](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/key-concepts).
  * Understand [state management](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/state-management) for data agents and how the API manages conversation context.
  * Explore how to [authenticate and connect to a data source](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication).
  * Learn how to [create and configure an agent with HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http).
  * Learn how to [create and configure an agent with Python](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk).
  * Learn more about [guiding an agent's behavior with authored context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions).
  * Understand [access control with IAM for the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control).
  * Learn how to [protect your data agents and conversations by using CMEK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).
  * Learn how to [orchestrate data agents with A2A](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/orchestrate-agents-a2a).
  * Learn how to [render agent responses for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-looker-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
