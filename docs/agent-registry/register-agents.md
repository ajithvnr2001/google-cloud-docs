---
url: https://docs.cloud.google.com/agent-registry/register-agents/
title: Register agents \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:13.500227+00:00
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

Agent Registry lets you register AI agents so that developers and orchestrator agents can discover and invoke their capabilities across your AI ecosystem. By publishing your agent's [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a), you help other developers and orchestrator agents in your organization find and reuse your work.

Agent Registry integrates with versions `0.3` and `1.0` of the open source [Agent2Agent (A2A)](https://a2a-protocol.org/latest/) protocol, which lets agents declare their capabilities and identity in an [Agent Card](https://docs.cloud.google.com/agent-registry/json-schemas#agent-card). Depending on where your agents run, you can register them using automatic registration or manual registration.

## Automatic registration

Supported Google Cloud runtimes register your agents automatically, and built-in Google agents are discoverable without configuration. Within the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled, automatic registration happens either by default or through an opt-in deployment step. The registration process operates at the project level and doesn't automatically discover remote agents deployed in other Google Cloud projects.

For information about Google Cloud runtimes that support automatic registration and the metadata indexed for automatically registered agents, see [Use automatic registration for agents](https://docs.cloud.google.com/agent-registry/automatic-registration).

## Manual registration

Agent Registry uses a central Google Cloud [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project). The term _remote_ refers to agents hosted outside the governance project in separate Google Cloud projects, on-premises environments, or external platforms, or running on Google Cloud runtimes that don't support automatic discovery. You must use manual registration to add remote agents to the governance project's registry.

To manually register an agent, use the Google Cloud console, the Google Cloud CLI, Terraform, or the Agent Registry API to create a `Service` resource that stores the agent's metadata, including its endpoint URL and configuration. After you create the `Service` resource, Agent Registry automatically creates a read-only `Agent` resource that you can use for [discovery](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#discovery-types).

To learn how to manually register A2A-compliant and standard REST agents, see [Use manual registration for agents](https://docs.cloud.google.com/agent-registry/manual-registration).

### Cross-project registration considerations

If your organization uses a centralized governance architecture with [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview), such as the multi-project pattern described in [Sample deployment patterns](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway#deployment-patterns), you can deploy a gateway in [Agent-to-Anywhere egress mode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview#modes) in a central [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled, while deploying agents in separate Google Cloud projects.

Because automatic registration only discovers resources in the governance project where Agent Registry is enabled, it doesn't automatically discover remote agents deployed in other Google Cloud projects. To let the central gateway locate and govern those remote agents, you must manually register each remote agent in the central governance project's registry. For instructions, see [Register an agent from another project](https://docs.cloud.google.com/agent-registry/manual-registration#cross-project).

## Integrate standalone skills

Agent Registry lets you manage and govern standalone [skills](https://docs.cloud.google.com/agent-registry/skills-architecture) for agents as top-level resources. Standalone skills are registered as `Skill` resources in your registry, letting administrators apply fine-grained access policies and manage version history using [skill revisions](https://docs.cloud.google.com/agent-registry/skills-architecture#skill-revision).

When [building and managing agents in Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents), you can reference these registered standalone skills to extend your Gemini Enterprise agent's capabilities. For information on how to register and manage standalone skills, see [Register skills](https://docs.cloud.google.com/agent-registry/register-skills) and [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
