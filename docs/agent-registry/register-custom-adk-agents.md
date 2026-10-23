---
url: https://docs.cloud.google.com/agent-registry/register-custom-adk-agents/
title: Register a custom ADK agent \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:15.574756+00:00
---

# Register a custom ADK agent  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/register-custom-adk-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Register a custom ADK agent Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry lets you register custom agents that you build with the [Agent Development Kit (ADK)](https://github.com/google/adk-docs) and host on your own infrastructure so that other developers and orchestrator agents can discover them. By exposing an [Agent Card](https://agent2agent.info/docs/concepts/agentcard/) that conforms to the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/) and manually registering the agent's endpoint, you make its [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a) discoverable in Agent Registry.

## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. Get [the project ID](https://support.google.com/googleapi/answer/7014113) for the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.
  3. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).



### Required roles

To get the permissions that you need to register custom ADK agents in Agent Registry, ask your administrator to grant you the [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) IAM role on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## The Agent Card endpoint

So that Agent Registry can index your custom agent's capabilities, the agent must expose its metadata and available A2A skills using the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/).

The A2A specification requires agents to serve an [Agent Card](https://agent2agent.info/docs/concepts/agentcard/), which is a JSON document describing the agent's identity and tools, at a specific endpoint, typically `/.well-known/agent-card.json`.

When you use the ADK's specific A2A server plugins or modules to register your agent, the framework can automatically generate and serve this Agent Card based on the `Agent` definition and `tools` you provide in your code.

## Register the exposed agent

After you deploy the ADK agent to your hosting environment and it successfully serves its REST endpoints, instruct Agent Registry to discover it.

Because custom deployments require [manual registration](https://docs.cloud.google.com/agent-registry/register-agents#manual-registration), you create a `Service` resource in the registry. Save your agent's generated Agent Card as a local JSON file, for example, `agent-card.json`.

Use gcloud CLI to register the agent with the [`gcloud agent-registry services create`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/create) command, making sure to specify the `a2a-agent-card` specification type, and upload your local file using the `--agent-spec-content` flag:
    
    
    gcloud agent-registry services create AGENT_NAME \
        --project=PROJECT_ID \
        --location=LOCATION \
        --display-name="DISPLAY_NAME" \
        --agent-spec-type=a2a-agent-card \
        --agent-spec-content=agent-card.json
    

The maximum file size for the specification file is 10 KB.

Replace the following:

  * `AGENT_NAME`: the name you want to give to your agent, for example, `my-custom-agent`.
  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location or region.
  * `DISPLAY_NAME`: the human-readable name of your agent.



After the `Service` resource is created, Agent Registry parses the Agent Card, creates a read-only `Agent` resource, and indexes the A2A skills defined in your ADK Python code so that other developers can [search for them](https://docs.cloud.google.com/agent-registry/search-agents-and-tools).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
