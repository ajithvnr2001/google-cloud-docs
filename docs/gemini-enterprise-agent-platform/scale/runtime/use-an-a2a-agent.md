---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-a2a-agent/
title: Use an Agent2Agent (A2A) agent \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:05.256195+00:00
---

# Use an Agent2Agent (A2A) agent  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-a2a-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Use an Agent2Agent (A2A) agent Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Before you begin

This tutorial assumes that you have read and followed the instructions in:

  * [Create an Agent2Agent (A2A) agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-a2a-agent) to create an agent as an instance of [`A2aAgent`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.frameworks.A2aAgent).
  * [User authentication](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/setup#authentication) to authenticate as a user for querying the agent.
  * [Import and initialize the SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/setup#sdk-import) to initialize the client for getting a deployed instance (if needed).



## Get an instance of an agent

To query an [`A2aAgent`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.frameworks.A2aAgent), you need to first [create a new instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent#create-agent-platform-instance) or [get an existing instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents#get).

To get the [`A2aAgent`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.frameworks.A2aAgent) that corresponds to a specific resource ID:

###  Agent Platform SDK 
    
    
    import agentplatform
    from agentplatform import types
    
    PROJECT_ID = "PROJECT_ID"
    LOCATION = "LOCATION"
    RESOURCE_ID = "RESOURCE_ID"
    RESOURCE_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{RESOURCE_ID}"
    
    client = agentplatform.Client(
        project=PROJECT_ID,
        location=LOCATION,
        http_options={"api_version": "v1beta1"},
    )
    
    remote_agent = client.runtimes.get(name=RESOURCE_NAME)
    
    print(remote_agent)
    

where

  * `PROJECT_ID` is the Google Cloud project ID under which you [create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-agent) and [deploy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent) agents, and
  * `LOCATION` is one of the [supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations).
  * `RESOURCE_ID` is the ID of the deployed agent as a [`reasoningEngine` resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines).



### A2A Python SDK

This method uses the official A2A Python SDK, which provides a client library for interacting with A2A-compliant agents. For more information, see the [A2A Python SDK documentation](https://a2a-protocol.org/latest/sdk/python/).

First, install the SDK:
    
    
    pip install a2a-sdk>=0.3.4

Then, get the agent's card to create a client instance. The `A2AClient` handles the discovery and communication for you.
    
    
    from google.auth import default
    from google.auth.transport.requests import Request
    from a2a.client import ClientConfig, ClientFactory
    from a2a.types import TransportProtocol
    import httpx
    
    # We assume 'agent_card' is an existing AgentCard object.
    
    # Fetch credentials for authentication for demo purpose. Use your own auth
    credentials, _ = default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
    credentials.refresh(Request())
    
    # Create the client by chaining the factory and config initialization.
    factory = ClientFactory(
        ClientConfig(
            supported_transports=[TransportProtocol.http_json], # only support http_json
            use_client_preference=True,
            httpx_client=httpx.AsyncClient(
                headers={
                    "Authorization": f"Bearer {credentials.token}",
                    "Content-Type": "application/json",
                }
            ),
        )
    )
    a2a_client = factory.create(agent_card)
    

### Python requests library

The A2A protocol is built on standard HTTP endpoints. You can interact with these endpoints using any HTTP client.

Retrieve the A2A URL from the agent card and define the request headers.
    
    
    from google.auth import default
    from google.auth.transport.requests import Request
    
    # We assume 'agent_card' is an existing object
    a2a_url = agent_card.url
    
    # Get an authentication token for demonstration purposes. Use your own authentication mechanism.
    credentials, _ = default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
    credentials.refresh(Request())
    
    headers = {
        "Authorization": f"Bearer {credentials.token}",
        "Content-Type": "application/json",
    }
    

When using the Agent Platform SDK, the `remote_agent` object corresponds to an [`AgentRuntime`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.types.AgentRuntime) class that contains the following:

  * [`remote_agent.api_resource`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.types.ReasoningEngine) with information about the deployed agent. You can also call `remote_agent.operation_schemas()` to return the list of operations that the `remote_agent` supports. See Supported operations for details.
  * [`remote_agent.api_client`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.runtimes.Runtimes) that allows for synchronous service interactions
  * [`remote_agent.async_api_client`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.runtimes.AsyncRuntimes) that allows for asynchronous service interactions



The rest of this section assumes that you have an `AgentRuntime` instance, named as `remote_agent`.

## Supported operations

An A2A agent hosted on Agent Runtime exposes a set of operations that correspond directly to the A2A protocol's API endpoints.

  * `on_message_send`: Sends a new message to the agent to start a task.
  * `on_get_task`: Retrieves the status and artifacts of an existing task.
  * `on_cancel_task`: Cancels a running task.
  * `handle_authenticated_agent_card`: Retrieves the agent's full capabilities and skills.



## Retrieve the agent card

Note that Agent Runtime does not serve the public agent card. To retrieve the authenticated agent card:

###  Agent Platform SDK 
    
    
    response = await remote_agent.handle_authenticated_agent_card()
    

### A2A Python SDK
    
    
    response = await a2a_client.get_card()
    

### Python requests library
    
    
    card_endpoint = f"{a2a_url}/v1/card"
    response = httpx.get(card_endpoint, headers=headers)
    print(json.dumps(response.json(), indent=4))
    

## Send a message

To send a message:

###  Agent Platform SDK 
    
    
    message_data = {
      "messageId": "remote-agent-message-id",
      "role": "user",
      "parts": [{"kind": "text", "text": "What is the exchange rate from USD to EUR today?"}],
    }
    
    response = await remote_agent.on_message_send(**message_data)
    

You can override the timeout used for `on_message_send` by setting the `timeout` field of `HttpOptions` when creating `agentplatform.Client`.

### A2A Python SDK
    
    
    from a2a.types import Message, Part, TextPart
    import pprint
    
    message = Message(
        message_id="remote-agent-message-id",
        role="user",
        parts=[Part(root=TextPart(text="What's the currency rate of USD and EUR"))],
    )
    
    response_iterator = a2a_client.send_message(message)
    
    async for chunk in response_iterator:
        pprint.pp(chunk)
    

### Python requests library
    
    
    import httpx
    import json
    
    endpoint = f"{a2a_url}/v1/message:send"
    
    payload = {
        "message": {
            "messageId": "remote-agent-message-id",
            "role": "1",
            "content": [{"text": "What is the exchange rate from USD to EUR today?"}],
        },
        "metadata": {"source": "python_script"},
    }
    
    response = httpx.post(endpoint, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=4))
    

## Get a task

To get a task and its status

###  Agent Platform SDK 
    
    
    task_data = {
        "id": task_id,
    }
    
    response = await remote_agent.on_get_task(**task_data)
    

### A2A Python SDK
    
    
    from a2a.types import TaskQueryParams
    
    task_data ={
        "id":task_id,
    }
    response = await a2a_client.get_task(TaskQueryParams(**task_data))
    

### Python requests library
    
    
    task_end_point = f"{a2a_url}/v1/tasks/{task_id}"
    response = httpx.get(task_end_point, headers=headers)
    print(json.dumps(response.json(), indent=4))
    

## Cancel a task

To cancel a task:

###  Agent Platform SDK 
    
    
    task_data = {
        "id": task_id,
    }
    response = await remote_agent.on_cancel_task(**task_data)
    

### A2A Python SDK
    
    
    from a2a.types import TaskQueryParams
    
    task_data = {
        "id":task_id,
    }
    response = await a2a_client.cancel_task(TaskQueryParams(**task_data))
    

### Python requests library
    
    
    task_end_point = f"{a2a_url}/v1/tasks/{task_id}:cancel"
    response = httpx.post(task_end_point, headers=headers)
    print(json.dumps(response.json(), indent=4))
    

## What's next

  * [Use an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-agent).
  * [Evaluate an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation).
  * [Manage deployed agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents).
  * [Get support](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
