---
url: https://docs.cloud.google.com/architecture/agenticai-orchestrate-access-disparate-systems/
title: Agentic AI use case: Orchestrate access to disparate enterprise systems \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:31.910357+00:00
---

# Agentic AI use case: Orchestrate access to disparate enterprise systems  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/agenticai-orchestrate-access-disparate-systems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Agentic AI use case: Orchestrate access to disparate enterprise systems Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-12-03 UTC

This document provides a high-level architecture for an agentic AI system to orchestrate interactions with disparate enterprise systems. An orchestrator agent automates complex processes and unifies access to multiple enterprise systems through modern, conversational interfaces. These systems might be commercial third-party applications or proprietary internal systems. This design approach eliminates point-to-point system integrations, so that your operators can avoid constant context-switching (swivel-chair processing).

The intended audience for this document includes architects, developers, and administrators who build and manage agentic AI applications in the cloud. The document assumes that you have a foundational understanding of [agentic AI](https://cloud.google.com/discover/what-is-agentic-ai).

## Architecture

The following diagram shows a multi-layer architecture where an orchestrator agent uses AI to route client interactions from multiple channels to appropriate backend systems.

![Architecture for an agentic AI application that orchestrates access to disparate enterprise systems.](https://docs.cloud.google.com/static/architecture/images/agenticai-orchestrate-access-disparate-systems-architecture.png)![Architecture for an agentic AI application that orchestrates access to disparate enterprise systems.](https://docs.cloud.google.com/static/architecture/images/agenticai-orchestrate-access-disparate-systems-architecture.png)

The components in the architecture are organized in the following layers:

Layer | Components  
---|---  
Interaction channels | In the example architecture, clients interact with the agentic AI system through the following multiple channels:

  * A custom frontend, such as a web application that communicates with the agent over a secure REST API and supports human-in-the-loop processes.
  * An ad hoc chat interface on [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/concepts) that invokes the agent as a secure tool and lets users interact with complex backend systems by using natural language.
  * An external application that initiates system-to-system automation workflows by publishing business events to a [Pub/Sub topic](https://docs.cloud.google.com/application-integration/docs/listen-pub-sub-topic-send-email).

  
Agentic core | The core component of the architecture is an orchestrator agent that's built using [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) and deployed on Cloud Run. The orchestrator manages a multi-agent system. This serverless platform provides scalability and access control using Identity and Access Management (IAM) for the agent's REST API. To maintain state across multi-step tasks, the agent uses built-in ADK support to [persist state](https://google.github.io/adk-docs/sessions/state/) data in Gemini Enterprise Agent Platform Sessions or in Cloud Storage.  
Standardized integration with backend systems | For communication between the agent and the backend systems, the architecture uses [Model Context Protocol (MCP)](https://cloud.google.com/discover/what-is-model-context-protocol) servers that are deployed on Cloud Run.

  * [MCP Toolbox for Databases](https://mcp-toolbox.dev/dev/documentation/introduction/) provides a secure, out-of-the-box set of tools for access to databases like [Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/pre-built-tools-with-mcp-toolbox).
  * Custom MCP servers provide access to the backend applications.

Each MCP server exposes the API of a specific backend system as a standardized set of tools. The MCP servers form an [anti-corruption layer](https://en.wikipedia.org/wiki/Domain-driven_design#Context_Mapping_patterns:~:text=Anticorruption%20Layer) that isolates the agent from the backend systems. This approach helps avoid tight coupling of the agent with the backend systems. It simplifies the agent's logic and lets you modernize the backend systems independently of the agent.  
Backend systems | In the example architecture, the AI agent orchestrates access to the following backend systems:

  * An operational database in Cloud SQL.
  * An application that's deployed on Compute Engine VMs.
  * An application that runs outside Google Cloud.

  
  
## Products used

This example architecture uses the following Google Cloud products:

  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Pub/Sub](https://cloud.google.com/pubsub): An asynchronous and scalable messaging service that decouples services that produce messages from services that process those messages.
  * [ Gemini Enterprise](https://cloud.google.com/gemini-enterprise): A fully-managed secure platform to deploy and manage AI agents within an enterprise. 
  * [ Gemini](https://ai.google.dev/gemini-api/docs/models): A family of multimodal AI models developed by Google. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Cloud SQL](https://cloud.google.com/sql): A fully managed relational database service that helps you provision, operate, and manage your MySQL, PostgreSQL, and SQL Server databases on Google Cloud. 



## Use cases

This architecture is useful for the following use cases:

  * Automate swivel-chair processing between disparate external and internal applications.
  * Create a unified interface for multiple legacy systems without a large-scale migration.
  * Add intelligent, conversational capabilities to existing business processes.
  * Incrementally modernize your applications with event-driven functionality.



The architecture provides the following benefits:

  * **Productivity** : Automate repetitive tasks to reduce human error, so your teams can focus on value-added tasks.
  * **Scalability** : Use an event-driven approach to develop, deploy, and scale services independently.
  * **Enhanced user experience** : Build modern, flexible interfaces to integrate complex business processes.
  * **Future-proof integration** : Standardize integration with backend systems by using MCP servers, so you can replace and upgrade the backend systems independently.



## Design considerations

To implement this architecture for production, consider the following recommendations:

  * **Security** : For the Cloud Run services, use dedicated IAM service accounts with permissions based on the principle of least privilege. Secure the agent's API by configuring [Cloud Run ingress controls](https://docs.cloud.google.com/run/docs/securing/ingress) to restrict access to authenticated callers.
  * **Observability** : In distributed systems, logging and tracing are critical for troubleshooting. To get visibility into the entire agentic workflow, instrument your services to write structured logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) and emit traces to [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview).
  * **Performance** : Cloud Run scales automatically based on demand and it scales to zero when there's no load. For latency-sensitive applications, you can minimize cold starts by configuring a [minimum number of instances](https://docs.cloud.google.com/run/docs/configuring/min-instances).
  * **Deployment automation** : Automate the provisioning and management of resources by using an infrastructure-as-code (IaC) tool like [Terraform](https://docs.cloud.google.com/docs/terraform). IaC helps ensure repeatable, auditable deployments across development, staging, and production.
  * **Governance** : Streamline the design and deployment of your application's infrastructure by using [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview). You can use App Design Center to define templates that incorporate governance rules and best practices for your organization.



## What's next

  * (Codelab) [Deploy a secure MCP server on Cloud Run](https://codelabs.developers.google.com/codelabs/cloud-run/how-to-deploy-a-secure-mcp-server-on-cloud-run#0).
  * (Codelab) [Build and deploy an agent that uses an MCP server on Cloud Run](https://codelabs.developers.google.com/codelabs/cloud-run/use-mcp-server-on-cloud-run-with-an-adk-agent#0).
  * (Codelab) [Asynchronously invoke an agentic AI application by using events](https://codelabs.developers.google.com/codelabs/genai/agents/async-invocation-with-adk#0).
  * (Google Skills course) [Build intelligent agents with ADK](https://www.skills.google/course_templates/1382).
  * (Code samples) Discover more code samples in GitHub for [building agents with ADK](https://github.com/google/adk-samples).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 



## Contributors

Author: [Casey West](https://www.linkedin.com/in/caseywest) | Architecture Advocate, Google Cloud

Other contributors: 

  * [Amina Mansour](https://www.linkedin.com/in/aminamansour/) | Tech Lead, Global Developer Relations & Strategic Content
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Leonid Yankulin](https://www.linkedin.com/in/minherz) | Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-03 UTC."],[],[]] 
