---
url: https://docs.cloud.google.com/run/docs/ai-agents/
title: Host AI agents on Cloud Run resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:54.900384+00:00
---

# Host AI agents on Cloud Run resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/ai-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Host AI agents on Cloud Run resources Stay organized with collections  Save and categorize content based on your preferences. 

This page highlights use cases for hosting AI agents on Cloud Run.

AI agents are autonomous software entities that use LLM-powered systems to perceive, decide, and act to achieve goals. As more autonomous agents are built, their ability to communicate and collaborate becomes crucial.

For an introduction to AI agents, see [What is an AI agent](https://cloud.google.com/discover/what-are-ai-agents).

## Choose a Cloud Run resource

Depending on your agentic design, you can run your agent container as one of the following [Cloud Run resource types](https://docs.cloud.google.com/run/docs/resource-model):

  * **Services:** Best for stateless, request-driven agents that handle variable user traffic, benefit from autoscaling, and can scale to zero when idle. Examples include chatbot APIs and web API backends.
  * **Instances:** Best for dedicated, stateful always-on singleton agent loops requiring VM-like lifecycle state commands. Examples include personal agents like OpenClaw and Hermes.
  * **Worker pools:** Best for running background, distributed agent fleets that consume tasks from message queues, such as Kafka or Pub/Sub, and scale horizontally without exposing public HTTP endpoints.
  * **Jobs:** Best for run-to-completion agent workflows, such as batch evaluations, large-scale data ingestion pipelines, or scheduled sync scripts.



## Choose your agent framework

Before you deploy your agent to Cloud Run, choose and set up your agent framework locally or on your development platform. Examples of agent frameworks include [Agent Development Kit (ADK)](https://adk.dev/), [Dify](https://docs.dify.ai/en/introduction), [LangGraph](https://www.langchain.com/langgraph), and [n8n](https://docs.n8n.io/).

On Cloud Run, your code typically runs as a service or instance. Both of these resource types run sandboxed container instances in the same execution environment and integrate with Google Cloud services.

## AI agent on Cloud Run architecture

A typical AI agent architecture deployed on Cloud Run can involve several components from Google Cloud as well as from outside of Google Cloud. The following architecture shows an example of implementing an AI agent as a Cloud Run service to orchestrate a set of asynchronous tasks and provide information through multiple request-response interactions.

![The four components of AI agent hosted on Cloud Run.](https://docs.cloud.google.com/static/run/docs/images/ai-agent-cloud-run.svg)**Figure 1.** Architecture of an AI agent on Cloud Run.

The diagram shows the following:

  * **Hosting platform** : A Cloud Run service is a scalable API endpoint for your application's core logic. It efficiently manages multiple concurrent users through automatic, on-demand, and rapid scaling of instances. Cloud Run offers the following benefits:

    * Supports running any _agent framework_ to build different types of agents and agentic architectures.
    * Built-in support for [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview). Assigns a unique, cryptographically verifiable identity to your agent for calling Google Cloud APIs, tools, and connecting securely to other agents. To learn more, see [Configure agent platform features](https://docs.cloud.google.com/run/docs/ai/agent-platform-features).
    * Built-in integration with [Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry). Designate your deployed services as an agent or an MCP server for automatic discovery and robust Agent-to-Agent (A2A) authentication mechanisms. To learn more, see [Configure agent platform features](https://docs.cloud.google.com/run/docs/ai/agent-platform-features).
    * Supports connecting your agent framework to other services. You can connect your agent to first-party or third-party tools deployed on Cloud Run. For example, to gain visibility into your agent's tasks and executions, you can deploy and use tools like [Langfuse](https://langfuse.com/) and [Arize](https://arize.com/).
  * **Agent interactions** : Cloud Run supports [streaming HTTP responses](https://docs.cloud.google.com/run/docs/triggering/https-request#streaming) back to the user, and [WebSockets](https://docs.cloud.google.com/run/docs/triggering/websockets) for real-time interactions.

  * **GenAI models** : The orchestration layer calls models for reasoning capabilities. These models can be hosted on services, such as the following:

    * [Gemini API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference) for Google's generative AI models.
    * [Vertex AI endpoints](https://docs.cloud.google.com/vertex-ai/docs/general/deployment) for custom models or other foundation models.
    * [GPU-enabled-Cloud Run service](https://docs.cloud.google.com/run/docs/configuring/services/gpu) for your own fine-tuned models.
  * **Memory** : Agents often need memory to retain context and learn from past interactions. You can use the following services:

    * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run) for short-term memory.
    * [Firestore](https://docs.cloud.google.com/firestore/docs) for long-term memory, such as storing the conversational history or remembering the user's preferences based on raw data.
    * [Vertex AI Agent Engine Memory Bank](https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview) for long-term personalized memory. This feature automatically extracts from the user's conversational history to remember and update the user's preferences over time. Note that you need to [create at least one Agent Engine instance](https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/set-up) to use this feature with Cloud Run.
  * **Vector database** : For Retrieval-Augmented Generation (RAG) or fetching structured data, use a vector database to query specific entity information or perform a vector search over embeddings. Use the `pgvector` extension with the following services:

    * [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-run)
    * [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/quickstart/integrate-cloud-run)
  * **Tools:** The orchestrator uses tools to perform specific tasks to interact with external services, APIs, or websites. This can include:

    * Model Context Protocol (MCP): Use this standardized protocol to communicate with external tools that are executed through an [MCP server](https://docs.cloud.google.com/run/docs/host-mcp-servers).
    * Basic utilities: Precise math calculations, time conversions, or other similar utilities.
    * API calling: Make calls to other internal or third-party APIs (read or write access).
    * Image or chart generation: Quickly and effectively create visual content.
    * Browser and OS automation: Run a [headless or a full graphical Operating System](https://docs.cloud.google.com/run/docs/browser-automation) within container instances to allow the agent to browse the web, extract information from websites, or perform actions using clicks and keyboard input.
    * Code execution: [Execute code](https://docs.cloud.google.com/run/docs/code-execution) in a secure environment with multi-layered sandboxing, with minimal or no [IAM permissions](https://docs.cloud.google.com/run/docs/securing/service-identity). 
    * Vertex AI Agent Engine Code Execution: Execute code in a [secure, isolated, and managed sandbox environments](https://docs.cloud.google.com/agent-builder/agent-engine/code-execution/overview) that supports file input and output, less than one second code execution, and long-lived memory. Note that you need to [create at least one Vertex AI Agent Engine instance](https://docs.cloud.google.com/agent-builder/agent-engine/code-execution/quickstart) to use this feature in Cloud Run.



## What's next

  * Build and deploy agents on Cloud Run: 
    * [A2A](https://docs.cloud.google.com/run/docs/ai/a2a-agents)
    * [ADK](https://docs.cloud.google.com/run/docs/ai/build-and-deploy-ai-agents/deploy-adk-agent)
    * [n8n](https://docs.n8n.io/hosting/installation/server-setups/google-cloud-run/)
  * Watch [Build AI agents on Cloud Run](https://www.youtube.com/watch?v=GwL8e5Z1tl4).
  * Try the [codelab for learning how to build and deploy a LangChain app to Cloud Run](https://codelabs.developers.google.com/codelabs/build-and-deploy-a-langchain-app-on-cloud-run).
  * Learn how to [deploy Agent Development Kit (ADK) to Cloud Run](https://google.github.io/adk-docs/deploy/cloud-run/).
  * Learn how to [Create and manage Cloud Run instances](https://docs.cloud.google.com/run/docs/create-instances).
  * Try the [codelab for using an MCP server on Cloud Run with an ADK agent](https://codelabs.developers.google.com/codelabs/cloud-run/use-mcp-server-on-cloud-run-with-an-adk-agent).
  * Try the [codelab for deploying your ADK agent to Cloud Run with GPU](https://codelabs.developers.google.com/codelabs/cloud-run/how-to-connect-adk-to-deployed-cloud-run-llm).
  * Find ready-to-use agent samples in [ADK (ADK) samples](https://github.com/google/adk-samples).
  * [Host Model Context Protocol (MCP) servers on Cloud Run](https://docs.cloud.google.com/run/docs/host-mcp-servers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
