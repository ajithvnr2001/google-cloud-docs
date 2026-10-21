---
url: https://docs.cloud.google.com/agent-registry/register-agents/
title: Register agents \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:37:01.157286+00:00
---

# Register agents  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/register-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Register agents Stay organized with collections  Save and categorize content based on your preferences. 

Registering an [agent](https://docs.cloud.google.com/agent-registry/concepts#agent) turns it into a discoverable component within Agent Registry. By publishing your agent's [A2A skills](https://docs.cloud.google.com/agent-registry/concepts#a2a-skill), you help other developers and orchestrator agents in your organization find and reuse your work, accelerating overall AI development.

Agent Registry seamlessly integrates with the [Agent2Agent (A2A)](https://a2a-protocol.org/latest/) protocol and its specifications. A2A is an open standard that lets agents declare their capabilities and identity. Agent Registry supports versions `0.3` and `1.0` of the A2A specification. For more information, see [Agent Card schema](https://docs.cloud.google.com/agent-registry/json-schemas#agent-card).

Depending on your agent runtimes, Agent Registry supports two primary registration mechanisms: automatic registration and manual registration.

Select the registration mechanism that fits your agent runtimes.

## Automatic registration

Supported Google Cloud runtimes register your agents with Agent Registry within the same project, either by default or through an opt-in deployment step. Automatic registration operates at the project level and doesn't automatically discover agents deployed in other Google Cloud projects.

Automatic registration is supported for the following Google Cloud runtimes:

  * **Agent Runtime on Gemini Enterprise Agent Platform** : Agents deployed using the SDK are registered without additional configuration. For more information, see [Register agents from Agent Runtime](https://docs.cloud.google.com/agent-registry/automatic-registration#agent-engine).
  * **Built-in Google agents** : Agents that Google provides directly, such as Google Workspace and Gemini Enterprise agents, are discoverable without any configuration. For more information, see [Register built-in Google agents](https://docs.cloud.google.com/agent-registry/automatic-registration#built-in-agents).
  * **Google Kubernetes Engine** : Containerized agents deployed to Google Kubernetes Engine (GKE) are registered when configured with the AI agent functional type label and Agent Card annotation. The GKE cluster runtime controller executes the introspection scan and publishes the metadata to Agent Registry. For more information, see [Register agents from GKE](https://docs.cloud.google.com/agent-registry/automatic-registration#gke).
  * **Cloud Run** : Containerized agents deployed to Cloud Run services or jobs are registered when deployed with the functional and identity type flags. Cloud Run automatically registers the agent's name and type (`AGENT`) with Agent Registry. For more information, see [Register agents from Cloud Run](https://docs.cloud.google.com/agent-registry/automatic-registration#cloud-run).



The metadata and capabilities indexed for an agent during registration depend on whether the agent implements the Agent2Agent (A2A) protocol:

  * **Agents implementing the A2A protocol** : The system queries the agent's Agent Card (`/.well-known/agent-card.json`) to automatically extract its advertised [A2A skills](https://docs.cloud.google.com/agent-registry/concepts#a2a-skill) and capabilities into the registry catalog.
  * **Agents not implementing the A2A protocol (standard REST or gRPC endpoints)** : Agent Registry registers the agent, but cannot automatically capture metadata such as the endpoint URL, agent's identity, and A2A skills. To associate capabilities with non-A2A agents, use [manual registration](https://docs.cloud.google.com/agent-registry/manual-registration) or [register skills](https://docs.cloud.google.com/agent-registry/register-skills).



For information about Google Cloud runtimes that support automatic registration, see [Use automatic registration](https://docs.cloud.google.com/agent-registry/automatic-registration).

## Manual registration

For agents hosted on external platforms, on-premises, on Google Cloud runtimes that don't support automatic discovery, or across different Google Cloud projects, you must use manual registration.

To manually register an agent, use the Agent Registry API, Google Cloud CLI, or Terraform to create a `Service` resource that defines the agent's endpoint and configuration. This writable `Service` resource also contains the agent's specific details. After the `Service` is created, the registry generates a read-only `Agent` resource that you can use for [discovery](https://docs.cloud.google.com/agent-registry/concepts#discovery).

You can manually register two types of agents:

  * **A2A-compliant agents** : Agents that implement the A2A specification (`A2A_AGENT_CARD`). The registry scans their [Agent Card](https://a2a-protocol.org/latest/topics/agent-discovery/#the-role-of-the-agent-card) (`agent-card.json`) endpoint to index their A2A skills.
  * **Standard REST agents** : Remote agents that don't implement the A2A specification (`NO_SPEC`), such as a standard REST API endpoint.



To learn how to manually register agents, see [Use manual registration](https://docs.cloud.google.com/agent-registry/manual-registration).

### Cross-project registration considerations

If your organization uses a centralized governance architecture with [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview), you can deploy an Agent-to-Anywhere egress gateway in a central governance project and register agents deployed in multiple spoke or workload projects.

Because automatic registration only discovers resources in the local project, you must manually register the remote agents in the central governance project's registry. Cross-project registration lets the central gateway locate and govern the agents. For instructions, see [Register an agent from another project](https://docs.cloud.google.com/agent-registry/manual-registration#cross-project).

## Integrate standalone skills

Agent Registry lets you manage and govern standalone [skills](https://docs.cloud.google.com/agent-registry/concepts#skill) for agents as top-level resources. Standalone skills are registered as `Skill` resources in your registry, letting administrators apply fine-grained access policies and manage version history using [skill revisions](https://docs.cloud.google.com/agent-registry/concepts#skill-revision).

When [building and managing agents in Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents), you can reference these registered skills to extend your agent's capabilities. For information on how to register and manage standalone skills, see [Register skills](https://docs.cloud.google.com/agent-registry/register-skills) and [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
