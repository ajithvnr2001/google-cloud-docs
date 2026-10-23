---
url: https://docs.cloud.google.com/agent-registry/reference/libraries/
title: Client libraries and ADK \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:20.364424+00:00
---

# Client libraries and ADK  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Client libraries and ADK Stay organized with collections  Save and categorize content based on your preferences. 

To interact with Agent Registry programmatically, you can use Google Cloud client libraries or the Agent Development Kit (ADK). The Google Cloud client libraries let you manage Agent Registry resources using standard Google Cloud APIs, while the ADK helps you build, evaluate, and deploy orchestrator agents.

## Client libraries

Google Cloud client libraries are the recommended way to call the Agent Registry API programmatically. Client libraries use the latest features of Agent Registry, provide an idiomatic experience for your supported programming language, and automatically handle authentication, retry logic, and pagination.

The Agent Registry API is supported in the following languages:

  * [C#](https://docs.cloud.google.com/dotnet/docs/reference)
  * [Go](https://docs.cloud.google.com/go/docs/reference)
  * [Java](https://docs.cloud.google.com/java/docs/reference)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference)
  * [PHP](https://docs.cloud.google.com/php/docs/reference)
  * [Python](https://docs.cloud.google.com/python/docs/reference)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference)



Google Cloud client libraries fully support [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), providing secure data perimeters for your API interactions.

## ADK

The ADK is an open-source Python framework for building, evaluating, and deploying AI agents.

The ADK provides abstractions for Agent Registry, automatically resolves connection details, and handles authentication to produce ADK components that are ready to use. By using the ADK, your orchestrator agents can dynamically resolve endpoints, discover [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a), and retrieve MCP tools managed within Agent Registry.

### Install the ADK

Install or upgrade to the latest version of the ADK with the A2A, Agent Identity, and MCP dependencies:

###  pip 
    
    
    pip install --upgrade "google-adk[a2a,agent-identity,mcp]"
    

###  uv 
    
    
    uv add "google-adk[a2a,agent-identity,mcp]"
    

You must upgrade to at least `google-adk>=1.29.0`.

### Python API reference

Review the Python API reference documentation for the ADK:

  * [ADK Python API reference](https://google.github.io/adk-docs/api-reference/python/)
  * [The GitHub `/google/adk-python` repository](https://github.com/google/adk-python)



### Use the ADK with Agent Registry

You can use the `AgentRegistry` client provided in the ADK to perform lookups and manage your resources from your Python code.

Set up the following environment variables:
    
    
    export GOOGLE_CLOUD_PROJECT=PROJECT_ID
    export GOOGLE_CLOUD_LOCATION=LOCATION
    

Replace the following:

  * `PROJECT_ID`: the project ID of your [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project).
  * `LOCATION`: the registry region or location, such as `us-central1`.



The following example demonstrates how to initialize the client, discover agents, and dynamically instantiate an MCP toolset directly from the registry:
    
    
    import os
    from google.adk.integrations.agent_registry.agent_registry import AgentRegistry
    
    # Initialize the client targeting your governance project and location
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "global")
    
    registry = AgentRegistry(
        project_id=project_id,
        location=location
    )
    
    # Discover agents by a required A2A skill, for example, translation
    translator_agents = registry.list_agents(
        filter_str='skills.tags:"translation"'
    )
    
    # Connect to a remote A2A agent using its resource name in short or full format
    # Short formats automatically imply the client's configured project and location
    # Short format: "agents/AGENT_ID"
    # Full format: f"projects/{project_id}/locations/{location}/agents/AGENT_ID"
    agent_name = "agents/AGENT_ID"
    summarizer_agent = registry.get_remote_a2a_agent(
        agent_name=agent_name
    )
    
    # Retrieve an MCP toolset using its resource name in short or full format
    # Short formats automatically imply the client's configured project and location
    # Short format: "mcpServers/SERVER_ID"
    # Full format: f"projects/{project_id}/locations/{location}/mcpServers/SERVER_ID"
    mcp_server_name = "mcpServers/SERVER_ID"
    bq_toolset = registry.get_mcp_toolset(
        mcp_server_name=mcp_server_name
    )
    

Replace the following:

  * `AGENT_ID`: your agent ID, for example, `agentregistry-1234-abcd`.
  * `SERVER_ID`: the MCP server ID, for example, `agentregistry-5678-efgh`.



For detailed task-based instructions on how to use the ADK to build dynamic agent workflows, see [Integrate Agent Registry with ADK](https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
