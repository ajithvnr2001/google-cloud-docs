---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-agent/
title: Use an agent \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:00.619616+00:00
---

# Use an agent  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Use an agent Stay organized with collections  Save and categorize content based on your preferences. 

## Using the Agent Platform SDK

When using the Agent Platform SDK, the code for querying an agent is the same regardless of whether it is running [locally](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-agent) or [deployed](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent) remotely. As the set of supported operations varies across frameworks, we provide usage instructions for framework-specific templates:

Framework | Description  
---|---  
[Agent Development Kit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-adk-agent) | Designed based on Google's internal best practices for developers building AI applications or teams needing to rapidly prototype and deploy robust agent-based solutions.  
[Agent2Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-a2a-agent) (preview) | The [Agent2Agent (A2A) protocol](https://a2a-protocol.org/) is an open standard designed to enable seamless communication and collaboration between AI agents.  
[LangChain](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-a-langchain-agent) | Easier to use for basic use cases because of its predefined configurations and abstractions.  
[LangGraph](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-a-langgraph-agent) | Graph-based approach to defining workflows, with advanced human-in-the-loop and rewind/replay capabilities.  
[AG2 (formerly AutoGen)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-ag2-agent) | AG2 provides multi-agent conversation framework as a high-level abstraction for building LLM workflows.  
[LlamaIndex](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-a-llamaindex-agent) (preview) | LlamaIndex's query pipeline offers a high-level interface for creating Retrieval-Augmented Generation (RAG) workflows.  
[Custom](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-a-custom-agent) | Agents that were developed and deployed without the use of a framework-specific template.  
[Runtime contract](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/runtime-contract) | HTTP API specification for custom container-based agents.  
  
## Use agents served on localhost

If you serve agents through an API server that are listening for requests on `http://localhost:PORT_NUMBER`, then you would send requests to
    
    
    http://localhost:PORT_NUMBER/API_PATH
    

where

  * `PORT_NUMBER` is the port number that the server is listening on (e.g. `8080`)
  * `API_PATH` is the path of the corresponding API endpoint (such as [`run`](https://adk.dev/runtime/api-server/#run-agent-single-response) or [`run_sse`](https://adk.dev/runtime/api-server/#run-agent-streaming))



## Use deployed agents through their underlying API

If you have [deployed](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent) an agent, then you would send requests to the corresponding endpoint:
    
    
    https://LOCATION-aiplatform.googleapis.com/reasoningEngines/v1/projects/PROJECT_NUMBER/locations/LOCATION/reasoningEngines/RESOURCE_ID/api/API_PATH
    

where

  * `PROJECT_ID` is the Google Cloud project ID where you [deployed](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent) the agent
  * `LOCATION` is the [region](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations) where the agent is deployed
  * `RESOURCE_ID` is the ID of the deployed agent as a [`reasoningEngine` resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines)
  * `API_PATH` is the path of the corresponding API endpoint



This endpoint is equivalent to replacing the localhost base URL with the deployed agent base URL. If you are deploying a custom container, the API endpoints and request and response structures are defined by the [runtime contract](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/runtime-contract).

To give a few examples, if you deployed the [ADK API server](https://adk.dev/runtime/api-server) from a [Dockerfile](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent#from-dockerfile) or [Container Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent#from-container-image), invoke the [API endpoints](https://adk.dev/runtime/api-server/#api-endpoints) as follows:

###  [Run agent (single response)](https://adk.dev/runtime/api-server/#run-agent-single-response)
    
    
    curl \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/reasoningEngines/RESOURCE_ID/api/run -d '{
      "appName": "my_sample_agent",
      "userId": "u_123",
      "sessionId": "s_abc",
      "newMessage": {
        "role": "user",
        "parts": [{"text": "What is the capital of France?"}]
      }
    }'

###  [Run agent (streaming)](https://adk.dev/runtime/api-server/#run-agent-streaming)
    
    
    curl \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/reasoningEngines/RESOURCE_ID/api/run_sse -d '{
      "appName": "my_sample_agent",
      "userId": "u_123",
      "sessionId": "s_abc",
      "newMessage": {
        "role": "user",
        "parts": [{"text": "What is the weather in New York?"}]
      },
      "streaming": true
    }'

## Use deployed agents in the Google Cloud console

For deployed agents developed using Agent Development Kit (ADK), you can use the Google Cloud console to interact with your agent:

  1. In the Google Cloud console, go to the **Agent Platform** Deployments page.  


[Go to Agent Platform Deployments](https://console.cloud.google.com/agent-platform/runtimes)

Runtimes that are part of the selected project appear in the list. You can use the **Filter** field to filter the list by your specified column.

  2. Click the name of your runtime.

  3. Click the **Playground** tab.

  4. You can **Type a message** to interact with your agent, and click **New Session** to start a new session with your agent.

  5. If you [enabled traces through OpenTelemetry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/tracing#write-traces), you can view details about your agent's behavior during your interactions:

     * **Trace** : Traces of your conversations with the agent.

     * **Event** : A graph of invoked APIs and event details during your conversations with the agent.

     * **State** : Information about your agent's state during your conversations.

     * **Sessions** : A list of sessions associated with your agent. For more information, see [Manage using Google Cloud console or API calls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-api)




### Playground support

You can use the following frameworks to try your agent:

Framework | Chat with agent | View sessions  
---|---|---  
Agent Development Kit (ADK) | Supported | Supported. Requires agent to implement [Agent Platform Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions) for persistency.  
Agent2Agent (A2A) | Supported. Requires agent to implement [Agent Platform Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions) for persistency. | Supported. Requires agent to use Agent Platform Sessions, and the agent must send the `user_id` value as part of the context object. For an example on how to pass the `user_id` value as part of the agent executor, see the [Get started with A2A](https://colab.sandbox.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_a2a_on_agent_engine.ipynb#scrollTo=R-d-VhZi7RIM) notebook.  
  
## What's next

  * [Evaluate an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation).
  * [Manage deployed agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents).
  * [Get support](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
