---
url: https://docs.cloud.google.com/architecture/single-agent-ai-system-adk-cloud-run/
title: Single-agent AI system using ADK and Cloud Run \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:10.893594+00:00
---

# Single-agent AI system using ADK and Cloud Run  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/single-agent-ai-system-adk-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Single-agent AI system using ADK and Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-20 UTC

This document provides a reference architecture to help you design a single-agent AI system on Google Cloud. The single-agent system in this architecture is built by using Agent Development Kit (ADK) and it's deployed on Cloud Run. You can also deploy the agent on Agent Runtime on Gemini Enterprise Agent Platform or Google Kubernetes Engine (GKE). The architecture uses [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro), which enables the agent to access and process information from multiple sources so that it can provide context-rich insights.

This document is intended for architects, developers, and administrators of AI applications. It assumes that you have a basic understanding of AI, machine learning (ML), and large language model (LLM) concepts. The document also assumes that you have a foundational understanding of AI agents and models. It doesn't provide specific guidance for designing and coding AI agents.

The Deployment section of this document lists code samples that you can use to learn how to build and deploy single-agent AI systems.

## Architecture

The following diagram shows an architecture for a single-agent AI system that's deployed on Cloud Run:

![A single-agent architecture that's deployed on Cloud Run.](https://docs.cloud.google.com/static/architecture/images/single-agent-ai-system-adk-cloud-run.svg)![A single-agent architecture that's deployed on Cloud Run.](https://docs.cloud.google.com/static/architecture/images/single-agent-ai-system-adk-cloud-run.svg)

### Architecture components

The example architecture consists of the following components:

Frontend
    Users interact with the agent through a frontend, such as a chat interface, that runs as a serverless [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) service.
Agent
    The agent receives user requests, interprets user intent, selects the appropriate tools, and then it synthesizes information to answer queries.
Agent runtime
    The agent is built by using [ADK](https://adk.dev/) and it's deployed as a [serverless Cloud Run service](https://docs.cloud.google.com/run/docs/ai-agents). You can also deploy the agent on [Agent Runtime on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) or as a containerized app on [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vertex). For information about how to choose an agent runtime, see [Choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components#agent_runtime).
ADK
    ADK provides tools and a framework to develop, test, and deploy agents. ADK abstracts the complexity of agent creation and lets AI developers focus on the agent's logic and capabilities. When you develop agents by using ADK, you can configure the agents to access and use [built-in tools](https://adk.dev/integrations/) like Google Search.
Model Armor
    Model Armor inspects and filters prompts and responses to protect the agent by helping to prevent malicious input, verify content safety, and protect sensitive data.
AI model and model runtime
    For inference serving, the agent in this example architecture uses the Gemini AI model on [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start).
MCP Toolbox
    [MCP Toolbox for Databases](https://mcp-toolbox.dev/) provides database-specific tools for the agent. It can handle complexities such as connection pooling and authentication.
MCP clients, servers, and tools
    [MCP](https://modelcontextprotocol.io/docs/getting-started/intro) facilitates access to tools by standardizing the interaction between agents and tools. For each agent-tool pair, an MCP client sends requests to an MCP server through which the agent accesses a tool such as a file system or an API. For example, external tools and the Google Search tool can provide data and grounding.
Observability
    The agent is monitored by using Google Cloud Observability for logging, monitoring, and tracing.

### Agentic flow

The example single-agent system in the preceding architecture has the following flow:

  1. A user enters a prompt through a frontend, such as a chat interface, which runs as a serverless Cloud Run service.
  2. The frontend routes the prompt to the agent, which sends the inference request through Model Armor to the AI model.
  3. Model Armor inspects and sanitizes prompts and model responses. For example, it masks or blocks personally identifiable information (PII) and it blocks malicious prompt injections or harmful content.
  4. The agent uses the AI model to reason about the user's prompt and synthesize a response: 
     * The AI model determines which tools to use to gather contextual information or to perform a task.
     * The agent performs tool calls and it adds the response to its context.
     * The agent performs grounding and intermediate validation.
  5. The agent sends the final response to the user through the frontend.



## Products used

This reference architecture uses the following Google Cloud and open-source products and tools:

  * [Agent Development Kit (ADK)](https://adk.dev/): A set of tools and libraries to develop, test, and deploy AI agents.
  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Gemini](https://ai.google.dev/gemini-api/docs/models): A family of multimodal AI models developed by Google. 
  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ Model Armor](https://cloud.google.com/security/products/model-armor): A service that provides protection for your generative and agentic AI resources against prompt injection, sensitive data leaks, and harmful content.
  * [ Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro): An open-source standard for connecting AI applications to external systems.
  * [ MCP Toolbox for Databases](https://mcp-toolbox.dev/documentation/introduction/): An open-source [ Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) server that lets AI agents securely connect to databases by managing database complexities like connection pooling, authentication, and observability.
  * [ Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs): Observability services including Cloud Monitoring, Cloud Logging, and Cloud Trace to help you understand the behavior, health, and performance of your applications. 



## Use cases

This section describes possible use cases for the architecture that's described in this document.

### Automated bug report triage

You can adapt this reference architecture to automate triage for incoming bug reports: understanding the issue, searching for duplicates, gathering relevant technical context, and then creating a bug in the system. An AI-powered agent can act as an intelligent assistant that can perform the initial investigation, which lets human experts focus on more complex problem-solving.

For this use case, the architecture provides the following benefits:

  * **Faster resolution times** : The agent automates the initial research and context-gathering, which can significantly reduce the time that it takes to assign and resolve bug tickets.
  * **Improved accuracy and consistency** : The agent can systematically search across multiple data sources (internal databases, code repositories, and the public web). This capability provides a more comprehensive and consistent analysis than manual triage might allow.
  * **Reduced manual workload** : The agent can offload repetitive triage tasks from IT support and engineering teams, which lets them focus on higher-value work.



This architecture is ideal for any organization that develops software and that wants to improve the efficiency and effectiveness of its bug resolution process. For information about how to configure tools for this use case, see [Custom tools for ADK](https://adk.dev/tools-custom/) and [ADK tools and integrations](https://adk.dev/integrations/).

### Customer service

You can adapt this reference architecture to help provide a seamless and personalized shopping experience for customers. An AI-powered agent can provide customer service, recommend products, manage orders, and schedule services, which lets human representatives focus on other tasks.

For this use case, the architecture provides the following benefits:

  * **Upselling and promotions** : The agent can help increase sales by suggesting products, services, and promotions. The agent's suggestions are based on the customer's current order and relevant sales, the customer's order history, and the items that are in their cart.

  * **Order management and scheduling** : The agent can increase efficiency and reduce customer friction by managing the contents of a customer's shopping cart and facilitating self-scheduling for services.

  * **Reduced manual workload** : The agent handles general inquiries, orders, and scheduling, which enables human customer service agents to focus on more complex customer issues.




This architecture is ideal for any retail organization that wants to improve their customer experience, increase sales, and simplify their order management and scheduling. For more information and deployment options, see [Retail Product Search Agent](https://github.com/google/adk-recipes/tree/main/contrib/python/retail-product-search).

### Time-series forecasting

You can adapt this reference architecture to help predict outcomes, such as demand forecasting, traffic patterns prediction, or machine failure analysis and prediction. An AI-powered agent can analyze real-time data, historical trends, and upcoming events. The agent can use these analyses to forecast outcomes for a specified period of time. These forecasts can help you plan and help reduce the time spent by human data analysts.

This use case can benefit organizations in many scenarios, such as the following:

  * **Inventory management** : By using advanced analytics combined with historical sales data and market trends, the agent can help you plan restock orders so that you can prepare for surges or lulls in customer demand.
  * **Travel routes** : The agent can help save time and reduce travel costs for delivery and service providers by analyzing real-time and historical traffic patterns along with events like construction or road closures.
  * **Avoid outages** : The agent can help you avoid potential service interruptions by helping to identify the root cause for historical outages. It can also help predict future potential failure states so that you can mitigate an issue before it becomes a problem.



This architecture is ideal for any organization that needs to adapt to changing patterns based on established trends. It's also ideal for organizations whose customers can benefit from proactive insights that help them plan for the future. For more information, see [Forecast time series with TimesFM](https://github.com/google/adk-recipes/tree/main/contrib/java/time-series-forecasting) and [MCP Toolbox for Databases](https://mcp-toolbox.dev/).

### Document retrieval

You can adapt this reference architecture to use [RAG Engine on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview) and create an agent to manage contextual data retrieval. A document-retrieval agent can fetch relevant data from a curated set of documents to provide factual answers with citations to the source material.

With a document-retrieval agent, you can help ensure that customers and internal users get informed and context-aware responses to their queries. This implementation can help reduce mistakes and inaccuracies by helping to ensure that answers are based on the information that you validated.

A document-retrieval architecture is ideal for knowledge bases about policy and process, technical infrastructure, product capabilities, and other fact-based documentation. For information about how to develop a retrieval-augmented generation (RAG)-powered document retrieval agent, see [RAG with Agent Platform Search](https://github.com/google/adk-recipes/tree/main/core/python/rag-agent-search) and [RAG with Vector Search](https://github.com/google/adk-recipes/tree/main/core/python/rag-vector-search).

## Design alternatives

This section presents alternative design approaches that you can consider for your AI agent deployment in Google Cloud.

### Agent runtime

In the architecture that this document describes, the agent and its tools are deployed on Cloud Run. You can also use GKE or Agent Runtime as an alternative runtime. For information about how to choose an agent runtime, see [Agent runtime](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components#agent_runtime) in "Choose your agentic AI architecture components".

### AI model runtime

In the architecture that this document describes, the AI model runtime is Agent Platform. You can also use Cloud Run or GKE as an alternative runtime. For information about how to choose a model runtime, see [Model runtime](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components#model-runtime) in "Choose your agentic AI architecture components".

## Design considerations

This section provides guidance to help you use this reference architecture to develop an architecture that meets your specific requirements for security, reliability, cost, operational efficiency, and performance. The guidance includes some agent-to-agent (A2A) considerations for broader scope architectures.

### System design

This section provides guidance to help you choose Google Cloud regions for your deployment and to select appropriate Google Cloud products and tools.

#### Region selection

When you select Google Cloud regions for your AI applications, consider the following factors:

  * [Availability of Google Cloud services](https://cloud.google.com/about/locations#products-available-by-location) in each region.
  * End-user [latency](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-latency#global-latency) requirements.
  * [Cost](https://cloud.google.com/products/calculator) of Google Cloud resources.
  * Regulatory requirements.



To select appropriate Google Cloud locations for your applications, use the following tools:

  * [Google Cloud Region Picker](https://cloud.withgoogle.com/region-picker/): An interactive web-based tool to select the optimal Google Cloud region for your applications and data based on factors like carbon footprint, cost, and latency.
  * [Cloud Location Finder API](https://docs.cloud.google.com/location-finder/docs/overview): A public API that provides a programmatic way to find deployment locations in Google Cloud, Google Distributed Cloud, and other cloud providers.



#### Agent design

This section provides general recommendations for designing AI agents. Detailed guidance about writing agent code and logic is outside the scope of this document.

  * **Agent definition and design** : 
    * Clearly define the business goal of the agentic AI system and the task that each agent performs.
    * Choose an [agent design pattern](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system) that best meets your requirements.
    * Use ADK to efficiently create, deploy, and manage your agentic architecture.
  * **Agent interactions** : 
    * Design the human-facing agents in the architecture to support natural language interactions.
    * Ensure that each agent clearly communicates its actions and status to its dependent clients.
    * Design the agents to detect and handle ambiguous queries and nuanced interactions.
  * **Context, tools, and data** : 
    * Ensure that the agents have sufficient [context](https://adk.dev/context/) to track multi-turn interactions and session parameters.
    * Clearly describe the purpose, arguments, and usage of the tools that the agents can use.
    * Ensure that the agents' responses are grounded in reliable data sources to reduce hallucinations.
    * Implement logic to handle no-match situations, such as when a prompt is off-topic.



#### Memory and session storage

The example architecture that's shown in this document doesn't include memory or session storage. In a production environment, you can improve the responses and add personalization by integrating state and memory into your agent.

  * [**Session**](https://adk.dev/sessions/session/): A session is the conversational thread between a user and the agent, from the initial interaction to the end of the dialogue.
  * [**State**](https://adk.dev/sessions/state/): State is the data that the agent uses and collects within a specific session. The state data that's collected includes the history of messages that the user and agent exchanged, the results of any tool calls, and other variables that the agent needs in order to understand the context of the conversation.



ADK can track sessions in short-term memory by using the `Session` object and `state` attributes. ADK also supports [long-term memory](https://adk.dev/sessions/memory/) across sessions with the same user, including through [Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank). To store session state, you can also use services like [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview).

For information about agent memory options, see [Choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components#agent-memory).

### Security

This section describes design considerations and recommendations to design a topology in Google Cloud that meets your workload's security requirements.

#### Security considerations for agents

AI agents introduce certain unique and critical security risks that conventional, deterministic security practices might not be able to mitigate adequately. Google recommends an [approach for securing AI](https://cloud.google.com/security/securing-ai) that combines the strengths of deterministic security controls with dynamic, reasoning-based defenses. This approach is grounded in three core principles: human oversight, carefully defined agent autonomy, and observability. The following are specific recommendations that are aligned with these core principles.

  * **Human oversight** : An agentic AI system might sometimes fail or not perform as expected. For example, the model might generate inaccurate content or an agent might select inappropriate tools. In business-critical agentic AI systems, incorporate a human-in-the-loop flow to let human supervisors monitor, override, and pause agents. For example, human users can review the output of agents, approve or reject the outputs, and provide further guidance to correct errors or to make strategic decisions. This approach combines the efficiency of agentic AI systems with the critical thinking and domain expertise of human users.
  * **Agent identity and least-privilege access** : 
    * Provide each agent a workload-bound, [SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview)-based identity by using [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview). You can use Agent Identity when you deploy agents to [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity) or to [Cloud Run](https://docs.cloud.google.com/run/docs/ai/agent-platform-features).
    * Configure per-agent permissions by using [Identity and Access Management (IAM) access policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iam-overview-uap) and [Agent Platform access control with IAM](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control). Grant each agent only the permissions that it needs to perform its tasks and to communicate with tools and with other agents. To further isolate each agent and limit the potential impact of a security breach, bind [Principal Access Boundary (PAB)](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies) policies to the agent identity.
    * When agents need to authenticate to external tools or to third-party APIs, use the [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/auth-manager-overview). With this approach, you can centrally control OAuth tokens and API keys instead of having to embed credentials within agent code or prompts.
  * **Ingress and egress traffic governance** : Route agent traffic through [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) to enforce runtime security policies at both the ingress and egress boundaries. For information about the runtime platforms that support Agent Gateway, see [Supported agent runtimes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview#agent-runtimes). 
    * **Client-to-Agent (ingress)** : Deploy [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-gateway-runtime-deploy) in front of your agent runtime. The gateway helps to authenticate callers and inspect inbound prompts in real time by using [Model Armor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor).
    * **Agent-to-Anywhere (egress)** : 
      * Route outbound agent-to-agent (A2A) and agent-to-tool (MCP) requests through Agent Gateway in egress mode.
      * Enforce default-deny access policies by using IAM access policies and [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/agent-overview).
      * Verify that target agents and tools are registered in [Agent Registry](https://docs.cloud.google.com/agent-registry/overview).
      * Inspect outbound tool invocations and responses with Model Armor to help prevent data exfiltration, indirect prompt injection, and tool misuse.
  * **Monitoring** : Monitor agent behavior by using comprehensive tracing capabilities that give you visibility into every action that an agent takes, including its reasoning process, tool selection, and execution paths. For more information, see [Logging an agent in Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/logging) and [Logging in ADK](https://adk.dev/observability/logging/).



For more information about securing AI agents, see [Safety and Security for AI Agents](https://adk.dev/safety/).

#### Agent Platform security considerations

To help ensure that your Agent Platform configurations and usage meet your security requirements, consider the following recommendations:

  * **Shared responsibility** : Security is a shared responsibility. Agent Platform secures the underlying infrastructure and provides tools and security controls to help you protect your data, code, and models. You are responsible for properly configuring your services, managing access controls, and securing your applications. For more information, see [Agent Platform shared responsibility](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/shared-responsibility).
  * **Security controls** : Agent Platform supports Google Cloud security controls that you can use to meet your requirements for data residency, [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/cmek), network security using [VPC Service Controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls), and [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview). For more information, see the following documentation: 
    * [Security controls for Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/security-controls)
    * [Security controls for Generative AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls)
    * [Agent Platform and zero data retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention)
  * **Safety** : AI models might produce harmful responses, sometimes in response to malicious prompts. 
    * To enhance safety and mitigate potential misuse of the agentic AI system, you can configure content filters to act as barriers to harmful inputs and responses. For more information, see [Safety and content filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters).
    * To inspect and sanitize inference requests, agent prompts, tool calls, and responses for threats like prompt injection and harmful content, you can use [Model Armor](https://docs.cloud.google.com/model-armor/overview) for direct model API calls _and_ for requests that are routed through [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor). Model Armor helps you prevent malicious input, verify content safety, protect sensitive data, maintain compliance, and enforce safety and security policies consistently.
  * **Model access** : You can set up organization policies to limit the type and versions of AI models that can be used in a Google Cloud project. For more information, see [Control access to Model Garden models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access).
  * **Data protection** : To discover and de-identify sensitive data in the prompts and responses and in log data, use the [Cloud Data Loss Prevention API](https://docs.cloud.google.com/sensitive-data-protection/docs/apis). For more information, see [De-identifying sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data).



#### MCP security considerations

To help ensure that your MCP implementation meets your security requirements, consider the following recommendations:

  * **Tool registration and discovery** : Register MCP servers and tools in [Agent Registry](https://docs.cloud.google.com/agent-registry/register-mcp-servers) so that agents only connect to inventoried, administrator-approved MCP endpoints.
  * **Access control and traffic inspection** : Route agent-to-MCP traffic through Agent Gateway in **Agent-to-Anywhere (egress)** mode and protect MCP servers (such as MCP servers hosted on Cloud Run) by using [IAP](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iap-cloud-run-mcp) and IAM access policies. Configure Model Armor or semantic governance policies on Agent Gateway to inspect MCP tool inputs and outputs for sensitive data exposure and indirect prompt injection.
  * **General MCP security** : When you configure your agents to use MCP, ensure that access to external data and tools is authorized, implement privacy controls like encryption, apply filters to protect sensitive data, and monitor agent interactions. For more information, see [MCP and security](https://cloud.google.com/discover/what-is-model-context-protocol#mcp-and-security).



#### A2A security considerations

To help ensure that your A2A implementation meets your security requirements, consider the following recommendations:

  * **Transport security** : The A2A protocol mandates HTTPS for all A2A communication in production environments and it recommends [Transport Layer Security (TLS)](https://a2a-protocol.org/latest/topics/enterprise-ready/#transport-level-security-tls) versions 1.2 or higher.
  * **Authentication** : The A2A protocol delegates authentication to standard web mechanisms like HTTP headers and to standards like OAuth2 and OpenID Connect. Each agent advertises the authentication requirements in its Agent Card. For more information, see [A2A authentication](https://a2a-protocol.org/latest/topics/enterprise-ready/#authentication).
  * **Inter-agent governance** : Register A2A agents in [Agent Registry](https://docs.cloud.google.com/agent-registry/register-agents) and route inter-agent requests through Agent Gateway. By combining Agent Gateway with Agent Identity, IAP, and IAM access policies, you can cryptographically verify the calling agent's identity, enforce fine-grained authorization between coordinator agents and subagents, and inspect inter-agent payloads with Model Armor.



#### Cloud Run security considerations

To help ensure that your Cloud Run implementation meets your security requirements, consider the following recommendations:

  * **Ingress security (for the frontend service)** : To control access to the application, [disable the default `run.app` URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url) of the frontend Cloud Run service and [set up a regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless). In addition to load-balancing incoming traffic to the application, the load balancer handles SSL certificate management. For added protection, you can use [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/integrating-cloud-armor#serverless) to provide request filtering, DDoS protection, and rate limiting for the service.
  * **User authentication** :

    * **Users inside your organization** : To authenticate internal user access to the frontend Cloud Run service, use IAP. When a user tries to access an IAP-secured resource, IAP performs authentication and authorization checks.
    * **Users outside your organization** : To authenticate external user access to the frontend service, use [Identity Platform](https://docs.cloud.google.com/identity-platform/docs) or [Firebase Authentication](https://firebase.google.com/docs/auth). To manage external user access, configure your application to handle a sign-in flow and to make authenticated API calls to the Cloud Run service.

For more information, see [Authenticating users](https://docs.cloud.google.com/run/docs/authenticating/end-users).

  * **Agent and MCP server security** : When you host agents or MCP servers on Cloud Run, configure [Agent Platform features for Cloud Run](https://docs.cloud.google.com/run/docs/ai/agent-platform-features) to assign a managed agent identity to the service, and use [IAP](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iap-cloud-run-mcp) with Agent Gateway to authenticate and authorize inbound agent and tool requests.

  * **Container image security** : To ensure that only authorized container images are deployed to Cloud Run, you can use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/run/overview). To identify and mitigate security risks in the container images, use Artifact Analysis to automatically run vulnerability scans. For more information, see [Container scanning overview](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).

  * **Data residency** : Cloud Run helps you meet data residency requirements. Your Cloud Run services run within the selected [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).




For more guidance about container security, see [General Cloud Run development tips](https://docs.cloud.google.com/run/docs/tips/general#container-security).

#### Security considerations for all of the Google Cloud products in the architecture

To help ensure that your architecture meets your security requirements, consider the following general recommendations:

  * **Data encryption** : By default, Google Cloud encrypts data at rest by using Google-owned and Google-managed encryption keys. To protect your agents' data by using encryption keys that you control, you can use [CMEKs](https://docs.cloud.google.com/kms/docs/cmek) that you create and manage in Cloud KMS. For information about Google Cloud services that are compatible with Cloud KMS, see [Compatible services](https://docs.cloud.google.com/kms/docs/compatible-services).
  * **Mitigate data exfiltration risk** : To reduce the risk of data exfiltration, create a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter around the infrastructure. VPC Service Controls supports all of the Google Cloud services that this reference architecture uses.
  * **Access control** : When you configure permissions for the resources in your topology, follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).
  * **Cloud environment security** : Use the tools in [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) to detect vulnerabilities, identify and mitigate threats, define and deploy a security posture, and export data for further analysis.
  * **Post-deployment optimization** : After you deploy your application in Google Cloud, get recommendations to further optimize security by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see [Find recommendations in Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).



For security principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

### Reliability

This section describes design considerations and recommendations to build and operate reliable infrastructure for your deployment in Google Cloud.

#### Agent reliability considerations

To help ensure that your agent meets your reliability requirements, consider the following recommendations:

  * **Simulate failures** : Before you deploy the agentic AI system to production, validate it by simulating a production environment. Identify and fix issues and unexpected behaviors.
  * **Scale horizontally** : To help ensure high availability and fault tolerance, run multiple instances of your agent application behind a load balancer. This approach can also help reduce latency and timeouts by distributing requests across instances. Some agent runtimes handle load balancing for you automatically, such as with [instance autoscaling in Cloud Run services](https://docs.cloud.google.com/run/docs/about-instance-autoscaling).
  * **Recover from outages** : To help ensure that the agent can gracefully handle restarts and maintain context, decouple state from runtime. To implement such a stateless agent application, use an external datastore like a database or a distributed cache. For example, you can use [Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank), [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview), or a database service like [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction).
  * **Handle errors** : To enable diagnosis and troubleshooting of errors, implement logging, exception handling, and retry mechanisms.



#### Agent Platform reliability considerations

To help ensure that your Agent Platform configurations and usage meet your reliability requirements, consider the following recommendations:

  * **Capacity planning** : If the number of your requests exceeds the allocated capacity, then [error code 429](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo#resource-exhausted-429-errors) is returned. For workloads that are business critical and consistently require high throughput, you can reserve throughput by using [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput).
  * **Model endpoint availability** : If data can be shared across multiple regions or countries, you can use a [global endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations#global-endpoint) for the model.



#### Cloud Run reliability considerations

To help ensure that your Cloud Run implementation meets your reliability requirements, consider the following recommendations:

  * **Robustness to infrastructure outages** : Cloud Run is a regional service. It stores data synchronously across multiple zones within a region and it automatically load-balances traffic across the zones. If a zone outage occurs, Cloud Run continues to run and data isn't lost. If a region outage occurs, the service stops running until Google resolves the outage.
  * **Horizontal scaling** : Cloud Run services handle [instance autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) for you. Autoscaling helps ensure that instances can handle all of the incoming requests, events, and CPU utilization that's needed to ensure high availability.



#### Reliability considerations for all of the Google Cloud products in the architecture

To help ensure that your architecture meets your reliability requirements, implement post-deployment optimization. After you deploy your application in Google Cloud, get recommendations to further optimize reliability by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see [Find recommendations in Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).

For reliability principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Reliability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability) in the Well-Architected Framework. 

### Operations

This section describes the factors to consider when you use this reference architecture to design a Google Cloud topology that you can operate efficiently.

#### Agent operations considerations

To help ensure that your agent meets your operational requirements, implement structured logging within your agent application for debugging and analysis. Logging and tracing lets you capture key information in a structured format, such as which tools were called, the inputs and outputs of the agent, and the latency of each step.

#### Agent Platform operations considerations

To help ensure that your Agent Platform configurations and usage meet your operational requirements, consider the following recommendations:

  * **Monitoring using logs** : By default, agent logs that are written to the `stdout` and `stderr` streams are routed to Cloud Logging. For advanced logging, you can integrate the Python logger with Logging. If you need full control over logging and structured logs, use the Logging client. For more information, see [Logging an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/logging) and [Logging in ADK](https://adk.dev/observability/logging/).
  * **Continuous evaluation** : Regularly perform a qualitative evaluation of the output of the agents and the trajectory or steps taken by the agents to produce the output. To implement agent evaluation, you can use the [Gen AI evaluation service](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation) or the [evaluation methods that ADK supports](https://adk.dev/evaluate/#how-evaluation-works-with-the-adk).



#### Cloud Run operations considerations

To help ensure that your Cloud Run implementation meets your operational requirements, monitor the health and performance of your Cloud Run services by using Google Cloud Observability. Set up alerts in Cloud Monitoring to notify you of potential issues, such as an increase in error rates, high latency, or abnormal resource utilization.

#### Database operations considerations

To help ensure that your database meets your operational requirements, monitor its health and performance by using Google Cloud Observability. Set up alerts in Monitoring to notify you of potential issues, such as an increase in error rates, high latency, or abnormal resource utilization.

#### MCP operations considerations

To help ensure that your MCP implementation meets your operational requirements, consider the following recommendations:

  * **Database tools** : To efficiently manage database tools for your AI agents and to ensure that the agents securely handle complexities like connection pooling and authentication, use the [MCP Toolbox for Databases](https://mcp-toolbox.dev/documentation/introduction/). It provides a centralized location to store and update database tools. You can share the tools across agents and update the tools without redeploying agents. The toolbox includes a wide range of tools for Google Cloud databases like AlloyDB for PostgreSQL and for third-party databases like MongoDB.
  * **Generative AI models** : To enable AI agents to use Google generative AI models like Imagen and Veo, you can use [MCP Servers for Google Cloud generative media APIs](https://github.com/GoogleCloudPlatform/genmedia-creative-studio/tree/main/experiments/mcp-genmedia).
  * **Google security products and tools** : To enable your AI agents to access Google security products and tools like Google Security Operations, Google Threat Intelligence, and Security Command Center, use [MCP servers for Google security products](https://google.github.io/mcp-security/).



#### Operations considerations for all of the Google Cloud products in the architecture

To help ensure that your architecture meets your operational requirements, continuously gather and analyze trace data by using Trace. Trace data lets you rapidly identify and diagnose latency issues within complex agent workflows. You can perform in-depth analysis through visualizations in the Google Cloud console Trace explorer page. For more information, see [Trace an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/traces).

For operational excellence principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Operational excellence](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence) in the Well-Architected Framework. 

### Cost optimization

This section provides guidance to optimize the cost of setting up and operating a Google Cloud topology that you build by using this reference architecture.

#### Agent Platform cost considerations

To help ensure that your Agent Platform configurations and usage meet your cost requirements, consider the following recommendations:

  * **Cost analysis and management** : To analyze and manage Agent Platform costs, we recommend that you create baseline metrics for queries per second (QPS) and tokens per second (TPS). Then, monitor these metrics after deployment. The baseline also helps with capacity planning. For example, the baseline helps you determine when [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput) might be necessary.
  * **Model selection** : The [model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models) that you select for your AI application directly affects both costs and performance. To identify the model that provides an optimal balance between performance and cost for your specific use case, test models iteratively. We recommend that you start with the most cost-efficient model and progress gradually to more powerful options.
  * **Cost-effective prompting** : The length of your prompts (input) and the generated responses (output) directly affect performance and cost. Write prompts that are short, direct, and provide sufficient context. Design your prompts to get concise responses from the model. For example, include phrases such as "summarize in 2 sentences" or "list 3 key points". For more information, see the [best practices for prompt design](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies#best-practices).
  * **Context caching** : To reduce the cost of requests that contain repeated content with high input token counts, use [context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview).
  * **Batch requests** : When relevant, consider [batch prediction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference). Batched requests incur a lower cost than standard requests.



#### Cloud Run cost considerations

To help ensure that your Cloud Run implementation meets your cost requirements, consider the following recommendations:

  * **Resource allocation** : When you create a Cloud Run service, you can specify the amount of memory and CPU to be allocated. Start with the default CPU and memory allocations. Observe the resource usage and cost over time, and adjust the allocation as necessary. For more information, see [Configure memory limits for services](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) and [Configure CPU limits for services](https://docs.cloud.google.com/run/docs/configuring/services/cpu).
  * **Rate optimization** : If you can predict the CPU and memory requirements, you can save money with [committed use discounts (CUDs)](https://docs.cloud.google.com/run/cud).



#### Cost considerations for all of the Google Cloud products in the architecture

After you deploy your application in Google Cloud, get recommendations to further optimize cost by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see [Find recommendations in Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).

To estimate the cost of your Google Cloud resources, use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).

For cost optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

### Performance optimization

This section describes design considerations and recommendations to design a topology in Google Cloud that meets the performance requirements of your workloads.

#### Performance considerations for agents

To help ensure that your agent configurations meet your performance requirements, consider the following recommendations:

  * **Model selection** : When you select models for your agentic AI system, consider the capabilities that are required for the tasks that the agents need to perform.
  * **Prompt optimization** : To rapidly improve and optimize prompt performance at scale and to eliminate the need for manual rewriting, use the [Agent Platform prompt optimizer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-optimizer). The optimizer helps you efficiently adapt prompts across different models.



#### Agent Platform performance considerations

To help ensure that your Agent Platform configurations and usage meet your performance requirements, consider the following recommendations:

  * **Model selection** : The [model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models) that you select for your AI application directly affects both costs and performance. To identify the model that provides an optimal balance between performance and cost for your specific use case, test models iteratively. We recommend that you start with the most cost-efficient model and progress gradually to more powerful options.
  * **Prompt engineering** : The length of your prompts (input) and the generated responses (output) directly affect performance and cost. Write prompts that are short, direct, and provide sufficient context. Design your prompts to get concise responses from the model. For example, include phrases such as "summarize in 2 sentences" or "list 3 key points". For more information, see the [best practices for prompt design](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies#best-practices).
  * **Context caching** : To reduce latency for requests that contain repeated content with high input token counts, use [context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview).



#### Cloud Run performance considerations

Depending on your performance requirements, configure the memory and CPU to be allocated to the Cloud Run service. For more information, see [Configure memory limits for services](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) and [Configure CPU limits for services](https://docs.cloud.google.com/run/docs/configuring/services/cpu).

For more performance optimization guidance, see [General Cloud Run development tips](https://docs.cloud.google.com/run/docs/tips/general#optimize_performance).

#### Performance considerations for all of the Google Cloud products in the architecture

After you deploy your application in Google Cloud, get recommendations to further optimize performance by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see [Find recommendations in Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).

For performance optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization) in the Well-Architected Framework. 

## Deployment

Automated deployment for this reference architecture isn't available. Use the following code samples to help you build a single-agent architecture:

  * Learn how to implement cross-session memory and state with [Cross-session memory](https://github.com/google/adk-recipes/tree/main/core/python/cross-session-memory).
  * Learn how to implement runner-wide safety guardrails with [Safety guardrails using plugins](https://github.com/google/adk-recipes/tree/main/core/python/safety-plugins).



For code samples to get started with using ADK together with MCP servers, see [MCP Tools](https://adk.dev/tools-custom/mcp-tools/).

For examples of additional single-agent AI systems, you can use the following code samples. These code samples are fully functional starting points for learning and experimentation. For optimal operation in production environments, you must customize the code based on your specific business and technical requirements.

  * [Personalized shopping](https://github.com/google/adk-samples/tree/main/python/agents/personalized-shopping): Provide personalized product recommendations for a specific brand, merchant, or online marketplace.
  * [Incident management](https://github.com/google/adk-samples/tree/main/python/agents/incident-management): Validate end-user token and identity on a per-request basis by using dynamic identity propagation.
  * [Order processing](https://github.com/google/adk-samples/tree/main/python/agents/order-processing): Process and store orders and orchestrate email confirmation with a conditional human review for specified order quantities.
  * [Data engineering](https://github.com/google/adk-samples/tree/main/python/agents/data-engineering): Develop Dataform pipelines, troubleshoot pipeline issues, and manage data engineering from complex SQL queries to data transformations and data dependencies.
  * [Documentation retrieval](https://github.com/google/adk-samples/tree/main/python/agents/RAG): Use RAG to query documents that you upload to RAG Engine on Gemini Enterprise Agent Platform and get answers with citations to documentation and code.



## What's next

  * [Explore sample agents and tools in Agent Garden](https://console.cloud.google.com/agent-platform/agent-garden).
  * [Build agents using ADK](https://adk.dev/agents/).
  * [Deploy agents to Google Cloud](https://adk.dev/deploy/).
  * [Host MCP servers on Cloud Run](https://docs.cloud.google.com/run/docs/host-mcp-servers).
  * [Host AI apps and agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents).
  * Learn how to implement a [RAG infrastructure for generative AI applications in Google Cloud](https://docs.cloud.google.com/architecture/rag-reference-architectures).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Megan O'Keefe](https://www.linkedin.com/in/askmeegs) | Developer Advocate
  * [Shir Meir Lador](https://www.linkedin.com/in/shirmeirlador) | Developer Relations Engineering Manager



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
