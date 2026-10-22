---
url: https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/api-overview/
title: Data Engineering Agent API: Build data pipelines with an agent \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:31.777951+00:00
---

# Data Engineering Agent API: Build data pipelines with an agent  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Data Engineering Agent API: Build data pipelines with an agent Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Data Engineering Agent API, which is accessed through `geminidataanalytics.googleapis.com`, to build, modify, and manage data pipelines to load and process data in BigQuery. The API uses the [A2A protocol](https://a2a-protocol.org/) that lets you use natural language prompts to generate and edit data pipelines for your data engineering needs.

For more information about the Data Engineering Agent, see [Use the Data Engineering Agent to build and modify data pipelines](https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines).

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Before you begin

Before you use the Data Engineering Agent API, perform the steps in these sections.

### Enable APIs

Ensure that you have enabled the required APIs and have the required permissions. For more information, see [Enable the required APIs](https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines#required-apis).

### Install client libraries

Install the following client libraries:

  * [Python SDK](https://github.com/a2aproject/a2a-python)
  * [JavaScript/TypeScript SDK](https://github.com/a2aproject/a2a-js)
  * [Java SDK](https://github.com/a2aproject/a2a-java)
  * [Go SDK](https://github.com/a2aproject/a2a-go)
  * [.NET SDK](https://github.com/a2aproject/a2a-dotnet)



For more information, see [Agent2Agent (A2A) Protocol](https://github.com/a2aproject#getting-started).

## Supported A2A extensions

The Data Engineering Agent supports the following A2A extensions, some of which are required when interacting with the Data Engineering Agent.

Extension Name | Requirement | Description | URI  
---|---|---|---  
`GcpResource` | Required | The Google Cloud resource ID for the resource that the agent operates on. This is required for each request. | `https://geminidataanalytics.googleapis.com/a2a/extensions/gcpresource/v1`  
`ConversationToken` | Optional | An extension for the multi-turn conversation history as an opaque conversation token.   
  
This extension is required for multi-turn conversations to continue the conversation from a previous state. To continue, copy the conversation token value in the metadata field of the previous response from the agent, and include it in the metadata field of the next request to the agent. | `https://geminidataanalytics.googleapis.com/a2a/extensions/conversationtoken/v1`  
`MessageLevel` | Optional | The message level for client visibility control over message updates.   
  
The agent supporting this extension attaches the `messageLevel` to each `message` for client visibility control. | `https://geminidataanalytics.googleapis.com/a2a/extensions/messagelevel/v1`  
`Finish Reason` | Optional | An extension that indicates the reason why the agent has stopped.   
  
When `DEADLINE_EXCEEDED` is returned, the client resumes the task from where it left off with the conversation token returned in the response in the metadata. | `https://geminidataanalytics.googleapis.com/a2a/extensions/finishreason/v1`  
`Instruction` | Optional | User-defined agent instruction.   
  
The agent supporting this extension accepts a list of agent instructions as additional context with the key `agentInstructions`. Agent instruction is defined by the following schema: 

  * `Name`: name of the instruction. This is usually the filename
  * `Definition`: definition of the instruction

| `https://geminidataanalytics.googleapis.com/a2a/extensions/instruction/v1`  
  
### Activate A2A extension

To activate the A2A extension, your client must include the `A2A-Extensions` header in the HTTP request to the agent. The value is a comma-separated list of extension URIs for activation.

The `GcpResource` extension must be activated to interact with the Data Engineering Agent A2A API.

The following example shows an HTTP request to activate the A2A extension.
    
    
    POST /v1/a2a/projects/{project}/locations/{location}/agents/dataengineeringagent/v1/message:stream HTTP/1.1
    Host: geminidataanalytics.googleapis.com
    Content-Type: application/json
    Authorization: Bearer $(gcloud auth print-access-token)
    A2A-Extensions: https://geminidataanalytics.googleapis.com/a2a/extensions/messagelevel/v1,
      https://geminidataanalytics.googleapis.com/a2a/extensions/instruction/v1,
      https://geminidataanalytics.googleapis.com/a2a/extensions/gcpresource/v1,
      https://geminidataanalytics.googleapis.com/a2a/extensions/conversationtoken/v1,
      https://geminidataanalytics.googleapis.com/a2a/extensions/finishreason/v1
    Content-Length: 869
    
    {
      "request": {
        "messageId": "0ad14bfa-8d17-48ce-8669-52a856129a66",
        "role": "ROLE_USER",
        "contextId": "test-context-id",
        "content": [{
          "text": "hi"
        }]
      },
      "metadata": {
        "https://geminidataanalytics.googleapis.com/a2a/extensions/conversationtoken/v1": "cmVxdWVzdGNvbnZlcnNhdGlvbnRva2Vu",
        "https://geminidataanalytics.googleapis.com/a2a/extensions/gcpresource/v1": {
          "gcpResourceId": "projects/{project}/locations/{location}/repositories/{repository}/workspaces/{workspace}"
        },
       "https://geminidataanalytics.googleapis.com/a2a/extensions/instruction/v1": {
          "agentInstructions": [{
            "definition": "Always use uppercase for SQL keywords.",
            "name": "style_guide.md"
          }]
        }
      },
      "tenant": "projects/{project}/locations/{location}/agents/dataengineeringagent"
    }

The response might be similar to the following.
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json
    A2A-Extensions: https://geminidataanalytics.googleapis.com/a2a/extensions/messagelevel/v1,
      https://geminidataanalytics.googleapis.com/a2a/extensions/instruction/v1,
      https://geminidataanalytics.googleapis.com/a2a/extensions/gcpresource/v1,
      https://geminidataanalytics.googleapis.com/a2a/extensions/conversationtoken/v1,
      https://geminidataanalytics.googleapis.com/a2a/extensions/finishreason/v1
    Transfer-Encoding: chunked
    
    {
      "statusUpdate": {
        "status": {
          "state": "TASK_STATE_COMPLETED",
          "timestamp": "example-timestamp"
        },
        "final": true,
        "metadata": {
          "https://geminidataanalytics.googleapis.com/a2a/extensions/conversationtoken/v1": "Y29udmVyc2F0aW9udG9rZW4=",
          "https://geminidataanalytics.googleapis.com/a2a/extensions/finishreason/v1": "FINISHED"
        }
      }
    }

## Key API operations

The API provides the following core endpoints for using the Data Engineering Agent:

Operation | HTTP method | Endpoint | Description  
---|---|---|---  
Get Agent Card | GET | `/v1/a2a/{tenant=projects/*/locations/*/agents/dataengineeringagent}/v1/card` | Retrieves the agent card information.  
Send Streaming Message | POST | `/v1/a2a/{tenant=projects/*/locations/*/agents/dataengineeringagent}/v1/message:stream` | A streaming method for sending a prompt to the agent and receiving streaming responses.  
  
The following permission is required: `geminidataanalytics.locations.useDataEngineeringAgent`.  
Send Message | POST | `/v1/a2a/{tenant=projects/*/locations/*/agents/dataengineeringagent}/v1/message:send` | A unary method for sending a prompt to the agent and receiving a synchronous response. This can be useful for quick validation or single-turn questions.  
  
The following permission is required: `geminidataanalytics.locations.useDataEngineeringAgent`.  
  
## Additional resources

For detailed descriptions of methods, endpoints, and type definitions for request and response structures, see [Data Engineering Agent API REST reference](https://docs.cloud.google.com/gemini/data-agents/reference/rest).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
