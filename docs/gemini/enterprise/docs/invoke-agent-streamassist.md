---
url: https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-streamassist/
title: Call a specific agent with the StreamAssist API \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:05:19.370123+00:00
---

# Call a specific agent with the StreamAssist API  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-streamassist/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Call a specific agent with the StreamAssist API Stay organized with collections  Save and categorize content based on your preferences. 

To call a specific registered agent, supply the optional `agentsSpec` field in your `streamAssist` REST API request or client library call. The [AgentsSpec API](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist#AgentsSpec) defines the specification of agents that are used to serve the request. The assistant routes queries directly to that agent and preserves session context across turns.

## At a glance

Specification | Details  
---|---  
**API method** | `projects.locations.collections.engines.assistants.streamAssist`  
**Endpoint versions** | `v1alpha` for discovering agent IDs; `v1` for calling `streamAssist`  
**Key parameter** | `agentsSpec.agentSpecs[].agentId`  
**Supported agent types** | [Core Assistant](https://docs.cloud.google.com/gemini/enterprise/docs/core-assistant), [Deep Research](https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant), [Workflow Builder](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder) chat agents (formerly low-code), and Workflow Builder workflows (see Call a workflow)  
**Required IAM permission** | `discoveryengine.assistants.assist`  
**Required OAuth scope** | `https://www.googleapis.com/auth/cloud-platform`  
  
## Before you begin

  1. Enable the **Discovery Engine API** (`discoveryengine.googleapis.com`) in your Google Cloud project.
  2. Ensure your principal (user account or service account) has a role granting the `discoveryengine.assistants.assist` IAM permission, such as **Discovery Engine Editor** (`roles/discoveryengine.editor`) or **Gemini Enterprise Admin** (`roles/discoveryengine.agentspaceAdmin`).
  3. Verify that your Gemini Enterprise app (engine) is created and contains at least one registered agent.
  4. If you authenticate using Application Default Credentials (ADC), ensure your client sends the quota project header: `-H "X-Goog-User-Project: PROJECT_ID"`.



## Find your app ID and location

The `streamAssist` URL requires your engine ID and its location (`global`, `us`, or `eu`). If you only know the app's display name, list the engines in your project to locate the underlying ID:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines"
    

In the response, the engine `name` format is `projects/{project}/locations/{location}/collections/default_collection/engines/{ENGINE_ID}`. The `ENGINE_ID` segment is the `APP_ID` required in the call.

**Note:** The engine ID typically has a numeric suffix appended to the display name (for example, `my-app_1234567890`).

## Find the agent ID

The `agentId` is the final segment of the agent's full resource name in the Discovery Engine API:
    
    
    projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}/agents/{AGENT_ID}
    

Registered agents use a long numeric ID (for example, `15492003793394502655`) rather than a friendly display name. Supply only this final `{AGENT_ID}` numeric string in your request.

To list the agents registered to your app and discover their numeric IDs, call the `agents` collection on the `v1alpha` endpoint:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents"
    

**Important:** The `agents` collection is served exclusively on the `v1alpha` endpoint. Calling this list endpoint on `v1` or `v1beta` returns an HTTP `404 Not Found` error. However, the `streamAssist` invocation call itself operates on `v1`.

Each returned agent resource includes the following fields:

  * `name`: The full resource path ending in `{AGENT_ID}`.
  * `displayName`: The human-readable name shown in the Google Cloud console.
  * `state`: The operational state (such as `ENABLED` or `PRIVATE`).
  * A definition object indicating the agent type (such as `a2aAgentDefinition`, `lowCodeAgentDefinition`, or `workflowAgentDefinition`).



See [`agents` REST API reference](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.agents) for the complete agent resource schema.

## Send queries to agents

To send queries to a specific agent, you must construct your request with the appropriate `agentsSpec` and execute it using REST or client libraries.

**Note** : If an agent relies on internal connectors or data stores (such as Document Q&A agents), invoking it without configured data sources generates a "no data sources configured" response rather than an API error.

### Request body structure

To route a query to a specific agent, include the optional `agentsSpec` object in your POST request body:
    
    
    {
      "query": {
        "text": "QUERY_TEXT"
      },
      "session": "SESSION_RESOURCE_NAME",
      "agentsSpec": {
        "agentSpecs": [
          {
            "agentId": "AGENT_ID"
          }
        ]
      }
    }
    

#### Field reference

  * **`agentsSpec`** _(object, optional)_ : Specification of agents used to serve the request.
  * **`agentsSpec.agentSpecs[]`** _(array, optional)_ : A list of agent specifications. You can specify multiple agents in this array.
  * **`agentsSpec.agentSpecs[].agentId`** _(string, required within the spec)_ : The ID identifying the registered agent resource. Must conform to RFC-1034 with a maximum length of 63 characters.



See [`streamAssist` REST API reference](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist) for the complete request schema.

### Call streamAssist

### REST

The following `curl` command sends a query to a specific agent using the REST API:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant:streamAssist" \
      -d '{
        "query": {
          "text": "List all contact cards."
        },
        "agentsSpec": {
          "agentSpecs": [
            {
              "agentId": "AGENT_ID"
            }
          ]
        }
      }'
        

Replace the following placeholders:

  * **`LOCATION`** : The multi-region for both the hostname and resource path (`global`, `us`, or `eu`). If your app resides in the `global` location, omit the location prefix from the hostname (`discoveryengine.googleapis.com`).
  * **`PROJECT_ID`** : Your Google Cloud project ID.
  * **`APP_ID`** : Your Gemini Enterprise engine ID (discovered in Find your app ID and location).
  * **`AGENT_ID`** : The numeric agent ID (discovered in Find the agent ID).



### Python

This Python example calls `streamAssist` using the `google-cloud-discoveryengine` client library:
    
    
    # Install library: pip install google-cloud-discoveryengine
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Replace placeholder values with your project and agent details.
    project_id = "PROJECT_ID"
    location = "LOCATION"          # For example: "us", "eu", or "global"
    engine_id = "APP_ID"
    agent_id = "AGENT_ID"          # The numeric agent ID
    query_text = "List all contact cards."
    
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )
    client = discoveryengine.AssistantServiceClient(client_options=client_options)
    
    assistant_path = client.assistant_path(
        project=project_id,
        location=location,
        collection="default_collection",
        engine=engine_id,
        assistant="default_assistant",
    )
    
    request = discoveryengine.StreamAssistRequest(
        name=assistant_path,
        query=discoveryengine.Query(text=query_text),
        agents_spec=discoveryengine.StreamAssistRequest.AgentsSpec(
            agent_specs=[
                discoveryengine.StreamAssistRequest.AgentsSpec.AgentSpec(
                    agent_id=agent_id,
                )
            ]
        ),
    )
    
    for response in client.stream_assist(request=request):
        for reply in response.answer.replies:
            # Filter out model reasoning fragments (thought: true)
            if hasattr(reply, "grounded_content") and reply.grounded_content.content:
                print(reply.grounded_content.content.text, end="", flush=True)
    
    print()
        

### Understand the streaming response

The `streamAssist` endpoint returns a stream of JSON chunks over REST, or an iterator of response objects in client libraries:

  * **Answer text** : Incremental response text arrives in `answer.replies[].groundedContent.content.text`. Concatenate these text fragments in receipt order to reconstruct the complete answer.
  * **Reasoning fragments** : Fragments marked with `"thought": true` represent the model's internal reasoning process. Filter out these fragments when presenting the final output to end users.
  * **Execution state** : The `answer.state` field progresses from `IN_PROGRESS` to a terminal state: 
    * `SUCCEEDED`: The request completed and generated an answer.
    * `SKIPPED`: The query was ignored or bypassed. Inspect `assistSkippedReasons` for details (such as `NON_ASSIST_SEEKING_QUERY_IGNORED` for brief greetings).
    * `FAILED`: The invocation encountered an execution error.
  * **Session continuity** : The terminal chunk includes `sessionInfo.session` (the session resource name) and an `assistToken`.



### Continue the conversation in the same session

To maintain context across turns, pass the `session` string from `sessionInfo` in subsequent requests:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant:streamAssist" \
      -d '{
        "session": "projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/sessions/SESSION_ID",
        "query": {
          "text": "Who is John Doe?"
        },
        "agentsSpec": {
          "agentSpecs": [
            {
              "agentId": "AGENT_ID"
            }
          ]
        }
      }'
    

If you omit the `session` field or specify `-` as the session ID, the API generates a new, isolated session automatically.

## Call a workflow

To run a Workflow Builder workflow, send the same request with the workflow's ID in `agentsSpec.agentSpecs[].agentId`. Each call starts a manual run of the workflow.

  * **Version that runs** : If the workflow is published, the call runs its published version. Changes saved in Workflow Builder but not yet published don't affect API callers until you publish them. If the workflow has never been published, the call runs its draft.
  * **Who can call it** : The workflow's owner and admins can call it. Other users can call a published workflow after it's shared with them. Only the owner or an admin can call a workflow that has never been published; other callers receive `HTTP 403`.
  * **Triggers** : The workflow must have exactly one manual trigger. Calls fail for a workflow that combines a manual trigger with any other trigger, or that has more than one manual trigger.
  * **Inputs** : You can't set the manual trigger's input variables through `streamAssist`. If the manual trigger has a required input, the run fails, even if the input has a default value. Optional inputs are empty, and their default values aren't applied. The query text is passed to the workflow's LLM nodes, so you can include data there, but it doesn't fill input variables.



## Limitations

The following limitations apply when calling agents with `streamAssist`:

  * **Unsupported agent types** : A2A or ADK agents registered to a Gemini Enterprise app are not supported through `streamAssist`. To call an A2A agent directly using its registry endpoint, see [Call an agent using its registry A2A endpoint](https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-a2a).
  * **Mutative actions** : The `streamAssist` API is optimized for conversational queries and read-only retrieval over connectors. Programmatic execution of mutative tools and actions (such as email drafting, calendar event creation, or chat messaging) is not supported over `streamAssist`. Attempting to invoke an agent workflow that executes mutative actions may result in silent failures or ungrounded execution loops.



## Troubleshooting

Use the following table to troubleshoot common `streamAssist` invocation errors:

Symptom | Likely cause | Resolution  
---|---|---  
**HTTP 404 when listing agents** | Calling `agents` on the `v1` or `v1beta` endpoint. | Send the list request to the `v1alpha` endpoint instead.  
**Response appears generic despite setting`agentsSpec`** | Invalid numeric `agentId`, or the query is too generic to trigger domain behavior. | Confirm the exact numeric ID from the `v1alpha` agent list; send a domain-specific query; check response text for agent-specific wording.  
**No error returned, but target agent did not execute** | Malformed `agentId` caused a silent fallback to default orchestration. | Verify that the `agentId` consists of digits only and exactly matches an ID from the registry list.  
**Response state returns`SKIPPED`** | Input evaluated as a non-assist-seeking query (such as a brief greeting). | Send a substantive task query; inspect `assistSkippedReasons` in the response payload.  
`HTTP 401` or `HTTP 403 Permission Denied` | Missing OAuth scope, insufficient IAM role, or missing quota project header. | Verify the caller has `discoveryengine.assistants.assist`; ensure OAuth scope includes `cloud-platform`; add `-H "X-Goog-User-Project: PROJECT_ID"` if using ADC.  
`HTTP 403` with `Only the agent owner or an admin can run a draft of this agent.` | The workflow has never been published, and the caller isn't its owner or an admin. | Publish the workflow in Workflow Builder and share it with the caller.  
`HTTP 403` with `User does not have permission to access the Agent.` | The workflow isn't shared with the caller. | Share the workflow with the caller.  
Workflow behaves like an older version | The call runs the published version, not unpublished changes in Workflow Builder. | Publish the workflow.  
Workflow call ends with `answer.state` `FAILED` and an `INTERNAL` error | The workflow has a manual trigger plus another trigger, or more than one manual trigger. | Keep a single manual trigger.  
  
## What's next

  * [Get search results from StreamAssist](https://docs.cloud.google.com/gemini/enterprise/docs/get-answers-from-streamassist)
  * [streamAssist REST API reference](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist)
  * [Agents overview](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
