---
url: https://docs.cloud.google.com/agent-registry/register-custom-adk-agents/
title: Register a custom ADK agent \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:20.544016+00:00
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

If you build a custom agent using the [Agent Development Kit (ADK)](https://github.com/google/adk-docs) and host it on your own infrastructure, you can make it discoverable in Agent Registry by exposing an [Agent Card](https://www.agentcard.net/) and manually registering its endpoint.

This document explains how to make sure your ADK agent conforms to the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/), letting the registry index its [A2A skills](https://docs.cloud.google.com/agent-registry/concepts#a2a-skill).

## The Agent Card endpoint

To enable Agent Registry to understand your custom agent's capabilities, the agent must expose its metadata and available A2A skills using the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/).

The A2A specification requires agents to serve an [Agent Card](https://agent2agent.info/docs/concepts/agentcard/), which is a JSON document describing the agent's identity and tools, at a specific endpoint, typically `/.well-known/agent-card.json`.

When you use the ADK's specific A2A server plugins or modules to register your agent, the framework can automatically generate and serve this Agent Card based on the `Agent` definition and `tools` you provide in your code.

## Register the exposed agent

After you deploy the ADK agent to your hosting environment and it successfully serves its REST endpoints, instruct Agent Registry to discover it.

Because custom deployments require [manual registration](https://docs.cloud.google.com/agent-registry/register-agents#manual-registration), you create a `Service` resource in the registry. Save your agent's generated Agent Card as a local JSON file, for example, `agent-card.json`.

Use Google Cloud CLI to register the agent, making sure to specify the `a2a-agent-card` specification type, and upload your local file using the `--agent-spec-content` flag:
    
    
    gcloud agent-registry services create AGENT_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --display-name="DISPLAY_NAME" \
      --agent-spec-type=a2a-agent-card \
      --agent-spec-content=agent-card.json
    

The maximum file size for the specification file is 10 KB.

Replace the following:

  * `AGENT_NAME`: The name you want to give to your agent, for example, `my-custom-agent`.
  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location or region.
  * `DISPLAY_NAME`: The human-readable name of your agent.



After the `Service` resource is created, Agent Registry parses the Agent Card, creates a discoverable `Agent` resource, and indexes the A2A skills defined in your ADK Python code so that other developers can [search for them](https://docs.cloud.google.com/agent-registry/search-agents-and-tools).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
