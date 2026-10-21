---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/a2a-protocol/
title: A2A Protocol tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:02.022158+00:00
---

# A2A Protocol tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/a2a-protocol/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  A2A Protocol tools Stay organized with collections  Save and categorize content based on your preferences. 

The Agent-to-Agent (A2A) protocol is an open messaging standard that enables autonomous AI agents to communicate and coordinate tasks across disparate systems.

In CX Agent Studio, A2A Protocol tools allow your agent application to delegate tasks to external remote agents, or allow external applications and orchestrators to invoke your CX Agent Studio agents using standardized messaging.

## How A2A works

The A2A protocol in CX Agent Studio operates using a _delegation_ model.

### Delegation model

In the delegation model, the initiating CX Agent Studio agent acts as the primary orchestrator and retains overall session control:

  * **Session ownership:** The primary agent maintains the user conversation session. When a specialized sub-task is required, the primary agent invokes the remote agent as a tool.
  * **Control flow:** The remote agent processes the request and returns structured response data. Control immediately returns to the primary agent, which summarizes or incorporates the results for the end user.
  * **Context transfer:** The primary agent transmits only the parameters and conversational context necessary for the delegated task.



![A2A delegation sequence diagram](https://docs.cloud.google.com/static/gemini-enterprise-cx/cx-agent-studio/images/a2a-delegation-flow.png)

### Text-based communication

All inter-agent communication in the A2A protocol is text-based:

  * If an end user interacts with a primary agent over a voice channel (such as telephony or WebRTC), the speech is first converted to text.
  * The primary agent sends the text transcript and parameters to the remote sub-agent in an HTTP request payload.
  * Raw audio streams and embeddings are not transmitted across the A2A network interface.



### Modality support

Modality (text versus voice) support for the A2A protocol depends on the direction of communication:

  * **Remote agent to CX Agent Studio:** Supports the text modality only.
  * **CX Agent Studio to remote agent:** Modality-agnostic for CX Agent Studio, meaning the CX Agent Studio session can use any supported modality such as voice or text, but the remote agent only receives text.



## Billing

If both the primary and remote sessions are in CX Agent Studio and are in the same project, you will be billed for 1 session.

Otherwise, for primary and remote sessions across multiple projects or third-party systems, you will be billed for 2 sessions.

## Authentication and access control

Authentication requirements depend on the direction of communication and the target service.

Direction | Target destination | Authentication mechanism | Required IAM role | Description  
---|---|---|---|---  
**Inbound** (External to CX Agent Studio) | CX Agent Studio agent application | OAuth 2.0 access token | `roles/ces.client` | Required for external callers to invoke the CX Agent Studio inbound endpoint.  
**Outbound** (CX Agent Studio to CX Agent Studio) | CX Agent Studio agent in another project | Service agent | `roles/ces.client` | Granted to the calling project's service agent on the target project.  
**Outbound** (CX Agent Studio to Cloud Run) | Cloud Run service | Service agent ID token | `roles/run.invoker` | Granted to the calling project's service agent on the Cloud Run service.  
**Outbound** (CX Agent Studio to Vertex AI) | Vertex AI Agent Engine | Service agent OAuth | `roles/aiplatform.user` | Granted to the calling project's service agent on the target project.  
**Outbound** (CX Agent Studio to third-party) | External endpoint (such as ServiceNow or Salesforce) | API Key or OAuth | Managed using Secret Manager | Stored credentials injected during tool execution.  
  
### Service agent identity

Outbound requests from CX Agent Studio use the CX Agent Studio service agent:
    
    
    service-PROJECT_NUMBER@gcp-sa-ces.iam.gserviceaccount.com
    

Replace `PROJECT_NUMBER` with your Google Cloud project number.

### Inbound authentication

When an external application, custom agent, or orchestrator calls into CX Agent Studio, it must pass a valid Google-issued OAuth 2.0 access token in the `Authorization` header:

  * **Testing:** Generate a temporary access token for your active account:
        
        gcloud auth print-access-token
        

  * **Programmatic clients:** Use Application Default Credentials (ADC):
        
        gcloud auth application-default print-access-token
        

  * **Production:** Use a dedicated Google service account with the `roles/ces.client` (`Customer Engagement Suite Client`) role.




## Prerequisites

Before configuring A2A Protocol tools:

  1. Enable the Gemini Enterprise for Customer Experience API (`ces.googleapis.com`) on your project:
         
         gcloud services enable ces.googleapis.com --project=PROJECT_ID
         

  2. Ensure the calling principal or service account has been granted the `Customer Engagement Suite Client` role (`roles/ces.client`).




## Configure an A2A Protocol tool

To connect your primary agent to an external remote agent:

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com).
  2. Select your project and open your agent application.
  3. In the agent builder, click the **Tools** icon.
  4. Click the **+** (Add) button to create a new tool.
  5. Select the **A2A Protocol** tool card.
  6. Configure your agent card using either the **UI Form** or the **JSON** editor.
  7. In the **URL** field, enter the remote agent's base endpoint URL (for example, `https://ces.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/apps/APP_ID` or your Cloud Run service URL). Don't append `/message:send` to the URL; CX Agent Studio automatically appends `/message:send` at runtime.
  8. Select the appropriate authentication type for the endpoint.
  9. Click **Create**.



### Agent card example

The following sample JSON defines an agent card for a remote weather agent:
    
    
    {
      "name": "weather_agent",
      "description": "Agent capable of querying weather conditions and local time for given locations.",
      "version": "0.1.0",
      "supportedInterfaces": [
        {
          "url": "https://ces.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/apps/APP_ID",
          "protocolBinding": "HTTP+JSON",
          "protocolVersion": "1.0"
        }
      ],
      "skills": [
        {
          "id": "get_weather",
          "name": "get_weather",
          "description": "Retrieves weather conditions for a specified location.",
          "tags": [
            "weather",
            "forecast"
          ],
          "examples": [],
          "inputModes": [],
          "outputModes": []
        },
        {
          "id": "get_current_time",
          "name": "get_current_time",
          "description": "Retrieves current local time for a specified city or timezone.",
          "tags": [
            "time",
            "clock"
          ],
          "examples": [],
          "inputModes": [],
          "outputModes": []
        }
      ]
    }
    

### Add routing instructions

Instruct your primary agent when to delegate to the A2A tool. For example:
    
    
    If the user asks for weather information or local time, use {@TOOL: weather_agent}.
    Pass the city or location specified by the user.
    If the tool returns an error, inform the user that weather details are temporarily unavailable.
    

## Inbound messaging

External systems can send messages directly to a CX Agent Studio agent application using the inbound A2A messaging endpoint.

**Note:** Remote agents built with the ADK can return either a normalized Task wrapper object (with artifacts) or direct Message payloads.

### Inbound endpoint URL

Send HTTP POST requests to the following endpoint:
    
    
    https://ces.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/apps/APP_ID/message:send
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The region hosting your agent application (such as `us-central1`).
  * `APP_ID`: The unique identifier of your CX Agent Studio agent application.



### Request payload schema

The JSON payload structure for sending an inbound message:
    
    
    {
      "message": {
        "messageId": "msg-MY_UNIQUE_MESSAGE_UUID",
        "role": "ROLE_USER",
        "content": [
          {
            "text": "Hello! I would like help checking my account balance."
          }
        ],
        "metadata": {
          "gecx_a2a_agent_context": "MY_SERIALIZED_AGENT_CONTEXT_STRING"
        }
      }
    }
    

**Note:** In CX Agent Studio, the message payload uses the `content` field to contain message text parts.

### Example request using curl

You can test inbound messaging using `curl`:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      -H "Content-Type: application/json" \
      -d '{
        "message": {
          "messageId": "msg-'"$(uuidgen)"'",
          "role": "ROLE_USER",
          "content": [
            {
              "text": "Hello!"
            }
          ]
        }
      }' \
      "https://ces.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/apps/APP_ID/message:send"
    

## Context and state management

The A2A protocol uses the `AgentContext` message to manage variables and session states between agents. Context is passed in the metadata of the `SendMessageRequest` using the `gecx_a2a_agent_context` key.

### Variable mapping

When delegating a task, you can map variables between the primary and remote agents:

  * **Outbound mapping:** `RemoteAgentTool.input_variable_mapping` computes the `AgentContext.variables` sent to the remote agent.
  * **Inbound mapping:** `RemoteAgentTool.output_variable_mapping` updates the primary agent's variables when the remote agent responds.



For inbound requests (external client to CX Agent Studio), the application deserializes the `gecx_a2a_agent_context` metadata and writes the `AgentContext.variables` directly into the current session. The updated variables are written back to `AgentContext.variables` when responding to the client.

### Session closure

The primary agent monitors `AgentContext.session_metadata.closed` to determine when a remote session ends:

  * Outbound requests always set `closed` to `false`. If the remote agent's response sets `closed` to `true`, the A2A connection is terminated.
  * For inbound responses back to the client, the CX Agent Studio app sets `closed` to `true` if the session has ended.



### Stateful mode

Remote sessions with CXAS apps are always stateful. Primary and remote CXAS sessions will share the same session ID and remote sessions will keep the conversation history between the primary and the remote agents.

For remote sessions with third-party systems, the remote sessions will be stateless by default and remote agent will receive each message from the primary agent as a new session (aka a new context ID).

You can enable the `RemoteAgentTool.stateful_agent` field to automatically cache and reuse the first context ID returned by the remote agent.

This cached context ID is used for the remainder of the session unless the remote agent responds with `AgentContext.session_metadata.closed == true`. If the session is closed, the cache is reset and a new context ID will be cached on the next tool call.

## Deploy a remote sub-agent

You can deploy custom remote agents on Google Cloud services to act as sub-agents for CX Agent Studio.

### Deploy to Cloud Run

To host an agent built with the [Agent Development Kit (ADK)](https://docs.cloud.google.com/agent-builder/agent-development-kit/overview) on Cloud Run:

  1. Create a `Dockerfile` in your agent project directory:
         
         FROM python:3.11-slim
         
         WORKDIR /app
         
         COPY pyproject.toml requirements.txt ./
         RUN pip install --no-cache-dir -r requirements.txt
         RUN pip install --no-cache-dir "google-adk[a2a]==1.32.0" "a2a-sdk[all]==0.3.26"
         
         COPY . .
         
         ENV PORT=8080
         ENV PYTHONUNBUFFERED=1
         
         EXPOSE 8080
         
         CMD ["python", "-m", "app.a2a_rest_server"]
         

  2. Deploy the container to Cloud Run:
         
         gcloud run deploy my-adk-agent \
           --project=PROJECT_ID \
           --region=us-central1 \
           --source=. \
           --memory=4Gi \
           --no-cpu-throttling
         

  3. Grant the `roles/run.invoker` role on the Cloud Run service to your calling project's CX Agent Studio service agent.

  4. Follow the steps in Configure an A2A Protocol tool to attach the Cloud Run service URL to CX Agent Studio.




### Deploy to Vertex AI Agent Engine

To deploy an ADK agent onto [Vertex AI Agent Engine](https://docs.cloud.google.com/agent-builder/agent-engine/overview):

  1. Define your dependencies in `requirements.txt`:
         
         a2a-sdk==0.3.26
         google-adk[a2a]>=1.15.0,<2.0.0
         

  2. Deploy the engine using the Vertex AI SDK:
         
         import os
         import sys
         from google.protobuf import json_format
         import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
         from vertexai.agent_engines import _agent_engines
         
         sys.path.append("./")
         from app.agent_runtime_app import agent_runtime
         
         client = [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).Client(project="PROJECT_ID", location="us-central1")
         
         ops = agent_runtime.register_operations()
         class_methods_proto = _agent_engines._generate_class_methods_spec_or_raise(
             agent_engine=agent_runtime,
             operations=ops
         )
         class_methods_list = [
             json_format.MessageToDict(cm, preserving_proto_field_name=True)
             for cm in class_methods_proto
         ]
         
         agent_config = {
             "entrypoint_module": "app.agent_runtime_app",
             "entrypoint_object": "agent_runtime",
             "source_packages": ["app", "requirements.txt"],
             "requirements_file": "requirements.txt",
             "class_methods": class_methods_list,
             "agent_framework": "google-adk",
             "env_vars": {
                 "GOOGLE_CLOUD_LOCATION": "us-central1",
             },
             "min_instances": 1,
             "max_instances": 10,
             "resource_limits": {"cpu": "4", "memory": "8Gi"},
         }
         
         engine = client.[agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html).create(config=agent_config)
         print(f"Deployed Engine Resource Name: {engine.api_resource.name}")
         

  3. Grant the `roles/aiplatform.user` role on the target project to your calling project's CX Agent Studio service agent.

  4. Follow the steps in Configure an A2A Protocol tool to attach the Agent Engine endpoint to CX Agent Studio.




### Connect to third-party endpoints

CX Agent Studio can delegate tasks to external third-party endpoints, such as ServiceNow or Salesforce.

When configuring the tool in the console:

  1. Follow the steps in Configure an A2A Protocol tool.
  2. Select the authentication method required by the third-party endpoint (such as API key or OAuth).
  3. Store credentials securely using Secret Manager.



## A2A Protocol tools compared to Agent as a tool

CX Agent Studio provides multiple methods for coordinating multi-agent workflows.

Feature | Agent as a tool | A2A Protocol tool  
---|---|---  
**Scope** | Intra-application (agents within the same CX Agent Studio app). | Inter-application (external agents, remote services, or third-party platforms).  
**Communication** | Direct in-memory / internal execution. | Network HTTP requests using the A2A messaging standard.  
**Use cases** | Reusing internal sub-agents without handing off the session. | Calling custom ADK agents on Cloud Run, Vertex AI, or external APIs.  
**Protocol** | Platform-internal tool execution. | Standardized A2A JSON payload over REST.  
  
## LLM tool execution

Under the hood, A2A protocol calls operate through standard LLM tool calling:

  1. When an A2A tool is assigned to an agent, the tool description and skill definitions are provided to the model as function declarations.
  2. When the model decides to delegate a sub-task, it generates a function call event.
  3. The CX Agent Studio runtime intercepts the function call, translates the parameters into an A2A HTTP request, and sends it to the configured remote endpoint.
  4. The response returned by the remote agent is passed back to the model to continue generating the conversation response.



To learn more about how agents are encapsulated as callable tools, see the [ADK AgentTool implementation](https://github.com/google/adk-python/blob/main/src/google/adk/tools/agent_tool.py) on GitHub.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
