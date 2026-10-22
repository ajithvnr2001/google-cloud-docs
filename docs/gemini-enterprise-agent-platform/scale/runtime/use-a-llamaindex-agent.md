---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-a-llamaindex-agent/
title: Use a LlamaIndex Query Pipeline agent \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:14.195299+00:00
---

# Use a LlamaIndex Query Pipeline agent  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-a-llamaindex-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Use a LlamaIndex Query Pipeline agent Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Before you begin

This tutorial assumes that you have read and followed the instructions in:

  * [Create a LlamaIndexQueryPipeline agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-a-llamaindex-agent): to create `agent` as an instance of [`LlamaIndexQueryPipelineAgent`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.frameworks.LlamaIndexQueryPipelineAgent).
  * [User authentication](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/setup#authentication) to authenticate as a user for querying the agent.
  * [Import and initialize the SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/setup#sdk-import) to initialize the client for getting a deployed instance (if needed).



## Get an instance of an agent

To query a [`LlamaIndexQueryPipelineAgent`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.frameworks.LlamaIndexQueryPipelineAgent), you need to first [create a new instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent#create-agent-platform-instance) or [get an existing instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents#get).

To get the [`LlamaIndexQueryPipelineAgent`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.frameworks.LlamaIndexQueryPipelineAgent) that corresponds to a specific resource ID:

###  Agent Platform SDK 

Run the following code:
    
    
    import agentplatform
    
    client = agentplatform.Client(  # For service interactions via client.runtimes
        project="PROJECT_ID",
        location="LOCATION",
    )
    
    agent = client.runtimes.get(name="projects/PROJECT_ID/locations/LOCATION/reasoningEngines/RESOURCE_ID")
    
    print(agent)
    

where

  * `PROJECT_ID` is the Google Cloud project ID under which you [create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-agent) and [deploy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent) agents, and
  * `LOCATION` is one of the [supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations).
  * `RESOURCE_ID` is the ID of the deployed agent as a [`reasoningEngine` resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines).



###  Python requests library 

Run the following code:
    
    
    from google import auth as google_auth
    from google.auth.transport import requests as google_requests
    import requests
    
    def get_identity_token():
        credentials, _ = google_auth.default()
        auth_request = google_requests.Request()
        credentials.refresh(auth_request)
        return credentials.token
    
    response = requests.get(
    f"https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/reasoningEngines/RESOURCE_ID",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {get_identity_token()}",
        },
    )
    

###  REST API 
    
    
    curl \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/reasoningEngines/RESOURCE_ID

When using the Agent Platform SDK, the `agent` object corresponds to an [`AgentRuntime`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.types.AgentRuntime) class that contains the following:

  * [`agent.api_resource`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.types.ReasoningEngine) with information about the deployed agent. You can also call `agent.operation_schemas()` to return the list of operations that the `agent` supports. See Supported operations for details.
  * [`agent.api_client`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.runtimes.Runtimes) that allows for synchronous service interactions
  * [`agent.async_api_client`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.runtimes.AsyncRuntimes) that allows for asynchronous service interactions



The rest of this section assumes that you have an `AgentRuntime` instance, named as `agent`.

## Supported operations

The following operations are supported for `LlamaIndexQueryPipelineAgent`:

  * `query`: for getting a response to a query synchronously.



## Query the agent

To query the agent, use the [`.query`](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/agentplatform.frameworks.LlamaIndexQueryPipelineAgent#vertexai_preview_reasoning_engines_LlamaIndexQueryPipelineAgent_query) method:
    
    
    agent.query(input="What is Paul Graham's life in college?")
    

is equivalent to the following (in full form):
    
    
    agent.query(input={"input": "What is Paul Graham's life in college?"})
    

To customize the input dictionary, see [Customize the prompt template](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-a-llamaindex-agent#prompt-template).

You can also customize the agent's behavior beyond `input` by passing additional keyword arguments to `query()`.
    
    
    response = agent.query(
        input={
          "input": [
            "What is Paul Graham's life in college?",
            "How did Paul Graham's college experience shape his career?",
            "How did Paul Graham's college experience shape his entrepreneurial mindset?",
          ],
        },
        batch=True  # run the pipeline in batch mode and pass a list of inputs.
    )
    print(response)
    

See the [`QueryPipeline.run` code](https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/query_pipeline/query.py#L392) for a complete list of available parameters.

## What's next

  * [Use an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/use-an-agent).
  * [Evaluate an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation).
  * [Manage deployed agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents).
  * [Get support](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
