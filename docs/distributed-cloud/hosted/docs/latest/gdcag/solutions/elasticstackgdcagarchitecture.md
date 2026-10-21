---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/elasticstackgdcagarchitecture/
title: Solution reference architecture: Deploying Elastic Stack's generative AI features on GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:19:42.437309+00:00
---

# Solution reference architecture: Deploying Elastic Stack's generative AI features on GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/elasticstackgdcagarchitecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Solution reference architecture: Deploying Elastic Stack's generative AI features on GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This reference architecture defines the conceptual design for deploying the Elastic Stack (Elasticsearch and Kibana) on Google Distributed Cloud (GDC) air-gapped and integrating it with a Large Language Model (LLM) service to enable Elastic's generative AI features.

The [Elastic Stack](https://www.elastic.co/elastic-stack) is a widely adopted search, observability, and security analytics platform. Recent Elastic releases add generative AI capabilities to Kibana, including the [Elastic AI Agent](https://www.elastic.co/docs/explore-analyze/ai-features/agent-builder/builtin-agents-reference#elastic-ai-agent), custom agents built with [Agent Builder](https://www.elastic.co/docs/explore-analyze/ai-features/elastic-agent-builder), and [Attack Discovery](https://www.elastic.co/docs/solutions/security/ai/attack-discovery). These features rely on an LLM to translate natural-language requests into Elasticsearch queries, orchestrate multi-step tool calls, and correlate security alerts.

This architecture deploys the Elastic Stack using the official [Elastic Cloud on Kubernetes (ECK) operator](https://www.elastic.co/guide/en/cloud-on-k8s/current/index.html) available in the GDC air-gapped Marketplace, and connects Kibana to an LLM inference endpoint hosted inside the GDC boundary, either the managed Gemini service on GDC or a self-managed OpenAI-compatible inference server such as Ollama or vLLM.

### Features and capabilities

The solution provides several core functional components for AI-assisted search, observability, and security analytics:

  * **Marketplace-Based Lifecycle Management** : Install the ECK operator from the GDC air-gapped Marketplace into a project namespace on a shared cluster, and let it automate the provisioning, configuration, and reconciliation of `Elasticsearch` and `Kibana` custom resources.
  * **Natural-Language Data Investigation** : Use the Elastic AI Agent to explore Elasticsearch data in natural language. The agent discovers indices and mappings, generates and executes ES|QL queries, and synthesizes findings without requiring prior knowledge of the underlying schema.
  * **Custom Agents and Automated Workflows** : Use Agent Builder to create purpose-built agents that combine custom instructions with built-in tools, custom ES|QL tools, and Kibana Workflows (for example, automatically opening Kibana Security Cases with investigation findings).
  * **AI-Driven Security Alert Correlation** : Use Attack Discovery to analyze open Elastic Security alerts, map them to the MITRE ATT&CK framework, and correlate related alerts, IP addresses, and user accounts into attack chains.
  * **Air-Gapped Compatibility** : The ECK operator, Elasticsearch, and Kibana container images are pulled from the local GDC Harbor registry, and all LLM inference traffic stays on the internal GDC network.
  * **Pluggable LLM Backends** : Connect Kibana to managed Gemini on GDC or to any self-managed inference server exposing an OpenAI-compatible `/v1/chat/completions` API through Kibana's OpenAI connector.



### Architectural principles

  * **Shared Responsibility Model** : GDC provides the shared cluster, Marketplace package, Harbor registry, and networking. The customer operates the Elastic Stack deployment, manages Elastic licensing, and owns the selection and operation of the self-managed LLM service (if used).
  * **Data Sovereignty** : All operational and security data, prompts, and model responses remain within the GDC air-gapped boundary. No traffic is sent to Elastic-hosted or public LLM services.
  * **Cloud-Native Operations** : Uses the Kubernetes operator pattern to manage stateful Elastic workloads declaratively, ensuring consistent and repeatable deployments.
  * **Protocol Standardization** : Relies on the widely supported OpenAI-compatible chat completions API with native function calling, decoupling Kibana from any specific inference engine or model vendor.



## Architecture

The architecture consists of an Elastic Stack deployment managed by the ECK operator inside a project namespace on a GDC shared user cluster. Kibana communicates over the internal GDC network with an LLM inference endpoint.

![Elastic Stack architecture diagram.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/elastic-stack-diagram.png)

Key components of this architecture include:

  * **GDC shared cluster** : An organization-scoped [shared Kubernetes cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters) attached to multiple projects, hosting GDC Marketplace software packages and application workloads.
  * **GDC project** : The project namespace on the shared cluster that isolates the ECK operator, Elasticsearch cluster, Kibana instance, and associated Kubernetes Secrets and NetworkPolicies.
  * **Elastic Cloud on Kubernetes (ECK) operator** : Installed from the GDC Marketplace into the project namespace, the operator manages the `Elasticsearch` and `Kibana` custom resources and reconciles the Elastic license required for generative AI features and external LLM connectors.
  * **Elasticsearch** : Stores and indexes operational and security data, and executes search and ES|QL queries generated by Kibana's AI features and agents.
  * **Kibana** : Hosts Elastic's generative AI features (Elastic AI Agent, Agent Builder, and Attack Discovery) and manages the LLM action connectors that orchestrate multi-step tool calling between the user, Elasticsearch, and the LLM service.
  * **LLM service** : A managed LLM service (such as Gemini on GDC) or a self-managed inference server (such as Ollama or vLLM) that provides chat completion and tool-calling capabilities to Kibana over the internal GDC network.



## Concepts and technologies

This section details the functional components, their responsibilities, and how they communicate within the system.

### Infrastructure and platform

  * **GDC Shared Cluster** : The primary compute environment where the ECK operator, Elasticsearch, and Kibana pods reside within a project namespace.
  * **GDC Marketplace** : The catalog used to install and upgrade the Elastic Marketplace package, which registers the Elastic CustomResourceDefinitions and deploys the `elastic-operator` StatefulSet.
  * **Harbor Registry** : The secure, local source of truth for the ECK operator, Elasticsearch, and Kibana container images in the air-gapped environment.
  * **Persistent storage** : PersistentVolumeClaims provisioned through the Elasticsearch `volumeClaimTemplates` provide durable block storage for Elasticsearch data.
  * **GDC networking** : LoadBalancer Services expose Elasticsearch (port `9200`) and Kibana (port `5601`), while Kubernetes `NetworkPolicy` and global `ProjectNetworkPolicy` resources govern inbound and cross-project traffic, including connectivity to the LLM service.



### Services and logic

  * **ECK operator** : The controller that watches `Elasticsearch` and `Kibana` custom resources and reconciles them into StatefulSets, Deployments, Services, and Secrets. Its `license-controller` continuously reconciles the cluster license against license Secrets in the operator namespace.
  * **Elastic AI Agent** : The default conversational agent in Kibana. It uses built-in Agent Builder tools (`platform.core.list_indices`, `platform.core.get_index_mapping`, `platform.core.search`, and `platform.core.execute_esql`) to discover data, generate ES|QL, and summarize results.
  * **Agent Builder** : The framework for creating custom agents that combine custom system instructions with built-in tools and user-defined tools (`esql`, `index_search`, `workflow`, and `mcp`).
  * **Kibana Workflows** : Declarative, YAML-defined automations (for example, `cases.createCase`) that can be registered as Agent Builder tools to let agents take actions such as opening Kibana Security Cases.
  * **Attack Discovery** : An Elastic Security feature that sends anonymized alert context to the LLM to correlate alerts from the `.alerts-security.alerts-default` index into attack chains mapped to MITRE ATT&CK tactics.
  * **LLM service** : Provides instruction-tuned chat completions with native tool-calling support. The model must reliably generate valid tool invocations, structured JSON, and ES|QL queries.



### Data flow and interfaces

  * **OpenAI-compatible chat completions API (`/v1/chat/completions`)**: The interface between Kibana's OpenAI (`.gen-ai`) connector and the LLM service, configured with the **Other (OpenAI Compatible Service)** provider, native function calling enabled, and Server-Sent Events streaming.
  * **Elasticsearch REST and ES|QL APIs** : Used by Kibana and its agents to inspect mappings, run searches, and execute ES|QL aggregations.
  * **Kibana REST APIs** : Used for programmatic management of connectors (`/api/actions`), agents and tools (`/api/agent_builder`), workflows (`/api/workflows`), detection rules (`/api/detection_engine`), and Attack Discovery (`/api/attack_discovery`).
  * **HTTPS with built-in authentication** : Elasticsearch and Kibana endpoints are served over TLS using ECK-generated certificates, with credentials stored in ECK-managed Kubernetes Secrets.



## Considerations

  * **Scalability and performance** : 
    * Elasticsearch and Kibana resource requests, limits, node counts, and storage sizes must be adjusted from evaluation defaults to match production data volumes and query concurrency.
    * Kibana's OpenAI connector enforces a default 60-second timeout per streaming turn. The LLM service must run on GPU acceleration with optimizations such as Flash Attention to keep each turn within this limit.
    * A single agent turn can trigger nested LLM sub-calls. The inference server should maintain multiple parallel KV cache slots (for example, `OLLAMA_NUM_PARALLEL=2`) to prevent sub-calls from evicting the main conversation's cached context.
  * **LLM model requirements** : 
    * The model must be instruction-tuned with native function-calling support. Native function calling should be enabled on the Kibana connector, as prompt-based simulated function calling is less reliable for nested tool calls.
    * A context window of at least 128,000 tokens is strongly recommended, since multi-step investigations combining tool definitions, index schemas, ES|QL documentation, and search results can exceed 70,000 tokens.
    * An output token limit of at least 8,192 tokens and a gentle repetition penalty are recommended for reasoning-capable models, because Kibana treats a `length` finish reason as a fatal error and uses greedy decoding.
    * Attack Discovery requires a 30B-class or larger model (such as `gemma4:31b`) to reliably synthesize multi-alert structured outputs.
  * **Security and compliance** : 
    * All prompts, retrieved data, and model responses remain on the internal GDC network.
    * Network policies should be tightened from permissive evaluation settings to restrict inbound access to Elasticsearch and Kibana to authorized clients and to limit egress to the LLM service endpoint.
    * Access to Kibana and Elasticsearch should be governed through Elastic role-based access controls rather than the `elastic` superuser.
  * **Resource management and licensing** : 
    * Elastic's generative AI features and external LLM connectors require an Enterprise license (or an active 30-day Enterprise trial), which must be provisioned through an ECK license Secret to persist across operator reconciliation cycles.
  * **Availability and reliability** : 
    * Production deployments should use multiple Elasticsearch nodes with replica shards and multiple Kibana instances to avoid single points of failure.
    * The availability of AI features depends on the availability and latency of the LLM service.
  * **Operational management** : 
    * The customer is responsible for upgrading the Elastic Marketplace package and Elastic Stack versions, managing licenses, and backing up Elasticsearch data.
    * When a self-managed LLM service is used, the customer owns its deployment, GPU capacity planning, model updates, and tuning.



## Design decision

The primary architectural choices for this solution focus on enabling Elastic's generative AI features within the constraints of the air-gapped environment.

### ECK operator from the GDC Marketplace

The ECK operator is installed from the GDC air-gapped Marketplace rather than deployed manually. The Marketplace package comes pre-configured to pull container images from the local Harbor registry, registers the required CustomResourceDefinitions, and integrates with GDC project-level IAM roles. This reduces image-mirroring effort and keeps the deployment aligned with the GDC software lifecycle.

### Shared cluster deployment

The solution deploys the Elastic Stack into a project namespace on a GDC shared cluster. This lets customers consume Marketplace software alongside other project workloads without provisioning and operating a dedicated cluster, while the project namespace provides isolation of resources, Secrets, and network policies.

### LLM service options

Managed Gemini on GDC is the preferred option where available, as it removes the operational burden of hosting inference infrastructure. Where it is not available, or where customers require a specific open model, Kibana can connect to any self-managed inference server that exposes an OpenAI-compatible `/v1/chat/completions` endpoint. Standardizing on this API keeps the Elastic configuration independent of the inference engine (such as Ollama or vLLM).

### Native function calling

Native function calling is enabled on the Kibana connector so that tool-call formatting is delegated to the inference server's OpenAI `tools` protocol. Kibana's default prompt-based simulated function calling is less reliable during nested tool calls and can fail with parsing errors.

### ECK-managed license reconciliation

The Enterprise (or trial) license is declared as an ECK license Secret instead of being activated directly through the Elasticsearch license API. Because ECK continuously reconciles the cluster license, licenses applied outside of ECK are reverted to `basic` on the next reconciliation cycle.

## Assumptions and limitations

### Assumptions

  * A GDC shared cluster and an attached project are available, with sufficient compute and persistent storage capacity for the ECK operator, Elasticsearch, and Kibana.
  * The Elastic Marketplace package and the matching Elasticsearch and Kibana container images are available in the GDC air-gapped Marketplace and the local Harbor registry.
  * Users have the required project roles (`namespace-admin`, `project-viewer`, `marketplace-editor`, and `project-networkpolicy-admin`).
  * An LLM service (managed Gemini on GDC or a self-managed OpenAI-compatible inference server) is deployed and reachable from the Kibana pod over the internal GDC network.
  * An Elastic Enterprise license is available, or the 30-day Enterprise trial is used for evaluation.



### Limitations

  * **LLM service out of scope** : Deploying and operating a self-managed LLM service, including GPU infrastructure, is not covered by this architecture.
  * **No Elastic-hosted AI services** : Elastic Managed LLMs and other cloud-hosted Elastic AI services are unavailable in the air-gapped environment.
  * **Model-dependent quality** : The accuracy and reliability of AI Agent, Agent Builder, and Attack Discovery results depend on the capabilities of the selected model and its runtime configuration.
  * **Evaluation-grade defaults** : The reference implementation uses a single-node Elasticsearch cluster, self-signed certificates, and permissive network policies, which must be hardened for production use.
  * **Version specificity** : The solution was validated with Elastic v9.4.0, the Elastic Kubernetes Operator v3.4.0, and GDC v1.16.2. Other versions may require adjustments.



## Additional materials

Solution Reference Implementation (SRI): [Deploying Elastic Stack's generative AI features on GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/elasticstackgdcagimpl)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
