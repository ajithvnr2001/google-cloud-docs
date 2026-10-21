---
url: https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators/
title: Resolve endpoints and build orchestrators \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:39:59.904495+00:00
---

# Resolve endpoints and build orchestrators  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Resolve endpoints and build orchestrators Stay organized with collections  Save and categorize content based on your preferences. 

The [Agent Development Kit (ADK)](https://github.com/google/adk-docs) provides a dedicated `AgentRegistry` client that lets you programmatically discover, look up, and connect to AI agents and Model Context Protocol (MCP) servers cataloged within Agent Registry.

Instead of hardcoding endpoint URLs into your application, you can use the ADK to resolve these endpoints at runtime.

Agent Registry provides the underlying endpoints, but production deployments typically route these invocations through [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview). Agent Gateway helps you enforce security policies, perform protocol mediation, and apply content filtering to the tools you discover.

This document describes how to retrieve remote agents and MCP toolsets from Agent Registry and include them in a parent orchestrator agent.

## Before you begin

Before you integrate the ADK with Agent Registry, complete the following:

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup) in your project.
  2. Install or upgrade to the latest version of the ADK with the A2A, Agent Identity, and MCP dependencies:

###  pip 
         
         pip install --upgrade "google-adk[a2a,agent-identity,mcp]"
         

###  uv 
         
         uv add "google-adk[a2a,agent-identity,mcp]"
         

You must upgrade to at least `google-adk>=1.29.0`.

  3. Configure [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc):
         
         gcloud auth application-default login
         




ADC credentials must have the necessary IAM permissions for the underlying services the agents or tools interact with. Optionally, you can also use custom headers for external toolsets. For more information, see [Authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets).

## Set environment variables

To follow this guide, set the following environment variables:
    
    
    export GOOGLE_CLOUD_PROJECT=PROJECT_ID
    export GOOGLE_CLOUD_LOCATION=LOCATION
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the registry region or location, such as `us-central1`.



## Initialize the registry client

To interact with your registry programmatically, initialize the `AgentRegistry` client with your project and location:
    
    
    import os
    from google.adk.integrations.agent_registry import AgentRegistry
    
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "global")
    
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT environment variable not set.")
    
    # Initialize the client
    registry = AgentRegistry(
        project_id=project_id,
        location=location,
    )
    

## Compose a multi-agent system

The ADK abstracts the underlying connection mechanics, letting you design scalable applications by composing multiple specialized agents into flexible hierarchies.

You can use the registry client to fetch specific resources and pass them directly into the definition of a new `LlmAgent` agent. Your orchestrator can invoke remote agents as subagents and execute MCP tools as if they were local Python functions.

Use the following methods:

  * **To fetch a remote agent** : Use `get_remote_a2a_agent()`
  * **To fetch an MCP toolset** : Use `get_mcp_toolset()`



The following example demonstrates how to compose a multi-agent system by building an orchestrator agent that takes advantage of a registered travel agent and a registered [Compute Engine MCP server](https://docs.cloud.google.com/compute/docs/use-compute-engine-mcp). In this example, authentication is handled by the agent's own identity, but you can use other methods, such as API keys and OAuth. For more information, see [Authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets).

To design and orchestrate agents using a visual, low-code interface, configure registered subagents directly in the Agent Studio canvas. For more information, see [Design agents in Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/design-agents).
    
    
    import httpx
    import google.auth
    from google.auth.transport.requests import Request
    from google.adk.agents.llm_agent import LlmAgent
    
    # Define the GoogleAuth class for the HTTP client
    class GoogleAuth(httpx.Auth):
        def __init__(self):
            self.creds, _ = google.auth.default()
        def auth_flow(self, request):
            if not self.creds.valid:
                self.creds.refresh(Request())
            request.headers["Authorization"] = f"Bearer {self.creds.token}"
            yield request
    
    # Connect to a remote A2A agent using its resource name in short or full format
    # Short formats automatically imply the client's configured project and location
    # Short format: "agents/AGENT_ID"
    # Full format: f"projects/{project_id}/locations/{location}/agents/AGENT_ID"
    agent_name = "agents/AGENT_ID"
    
    # Configure the HTTP client with GoogleAuth and a 60-second timeout
    httpx_client = httpx.AsyncClient(auth=GoogleAuth(), timeout=httpx.Timeout(60.0))
    my_remote_agent = registry.get_remote_a2a_agent(
        agent_name=agent_name,
        httpx_client=httpx_client
    )
    
    # Retrieve an MCP toolset using its resource name in short or full format
    # Short formats automatically imply the client's configured project and location
    # Short format: "mcpServers/SERVER_ID"
    # Full format: f"projects/{project_id}/locations/{location}/mcpServers/SERVER_ID"
    mcp_server_name = "mcpServers/SERVER_ID"
    my_mcp_toolset = registry.get_mcp_toolset(mcp_server_name=mcp_server_name)
    
    # Compose the orchestrator agent
    main_agent = LlmAgent(
        model="MODEL_ID", # Replace with a model such as gemini-1.5-flash
        name="travel_orchestrator",
        instruction="""You are a travel coordinator. You can use your
                       subagents to book travel and your tools to query
                       historical travel data.""",
        tools=[my_mcp_toolset],
        sub_agents=[my_remote_agent],
    )
    
    # You can now run your orchestrator agent
    # response = await main_agent.run('Book a flight to Paris and check my past trips.')
    

## Best practices for reusing agents

To minimize network latency, fetch your agents and toolsets from the registry once at application startup instead of calling `get_remote_a2a_agent()` on every invocation.

An agent can only have one parent agent at a time. If you attempt to assign the same fetched agent instance to multiple orchestrators, the ADK might throw an error indicating that the agent already has a parent.

To reuse a discovered agent across multiple parent agents, use the `.clone()` method to create a new instance of the agent object.

The following example shows how to fetch an agent once and clone it for use in different orchestrators:
    
    
    import httpx
    import google.auth
    from google.auth.transport.requests import Request
    from google.adk.agents.llm_agent import LlmAgent
    
    # Define the GoogleAuth class for the HTTP client
    class GoogleAuth(httpx.Auth):
        def __init__(self):
            self.creds, _ = google.auth.default()
        def auth_flow(self, request):
            if not self.creds.valid:
                self.creds.refresh(Request())
            request.headers["Authorization"] = f"Bearer {self.creds.token}"
            yield request
    
    # Configure the HTTP client with GoogleAuth and a 60-second timeout
    httpx_client = httpx.AsyncClient(auth=GoogleAuth(), timeout=httpx.Timeout(60.0))
    
    # Fetch the remote agent once during startup
    # Use the resource name in short or full format
    # Short formats automatically imply the client's configured project and location
    # Short format: "agents/AGENT_ID"
    # Full format: f"projects/{project_id}/locations/{location}/agents/AGENT_ID"
    agent_name = f"projects/PROJECT_ID/locations/LOCATION/agents/AGENT_ID"
    base_remote_agent = registry.get_remote_a2a_agent(
        agent_name=agent_name,
        httpx_client=httpx_client
    )
    
    # Use .clone() to assign the agent to different parent orchestrators
    flight_orchestrator = LlmAgent(
        model="gemini-1.5-flash",
        name="flight_orchestrator",
        sub_agents=[base_remote_agent.clone()]
    )
    
    hotel_orchestrator = LlmAgent(
        model="gemini-1.5-flash",
        name="hotel_orchestrator",
        sub_agents=[base_remote_agent.clone()]
    )
    

## What's next

  * Learn how to [set up Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) to route the traffic for your resolved endpoints.
  * Learn how to [authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets) using custom headers or bindings.
  * Learn how to [register skills](https://docs.cloud.google.com/agent-registry/register-skills) and [manage skills](https://docs.cloud.google.com/agent-registry/manage-skills) in Agent Registry.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
