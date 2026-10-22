---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/function/
title: Client function tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:07.496549+00:00
---

# Client function tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/function/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Client function tools Stay organized with collections  Save and categorize content based on your preferences. 

If you have functionality accessible by your client code, but not accessible by hosted tools, such as [OpenAPI](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/open-api) or [MCP](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/mcp) you can use client function tools. Client function tools are always executed on the client side, not by the agent.

## How it works

When an agent triggers a client function tool:

  1. **Session Block** : The conversation session is effectively "blocked" on the server side.
  2. **Client Execution** : Your client application must identify the tool call and execute the corresponding logic in your local environment.
  3. **Providing Response** : Once the execution is complete, your client application must provide the response back to the agent using the `toolResponses` fields.



The agent waits for this response before proceeding with the conversation.

## Configuration

When creating a client function tool, you define how the agent understands and interacts with your client-side code:

  * **Name** : A unique identifier for the tool (for example: `open_settings`).
  * **Description** : A brief description of the tool's purpose. Agent models use this description to decide when to call the function.
  * **Input/Output Schema** : Defined in OpenAPI format. This determines the structure of the data the agent sends and expects to receive.



## Use cases

Client function tools are ideal for:

  * **UI/UX Actions** : Triggering changes in your application's interface (for example, "Navigate to the support screen").
  * **Local Device Data** : Accessing information that is only available within the app's context (for example, "Get current battery level").
  * **Private APIs** : Integrating with services that are only reachable from the client-side environment.



## Example

The following example is a session response indicating that the client application should call a function:
    
    
    "outputs": [
      {
        "toolCalls": {
          "toolCalls": [
            {
              "id": "<execution id>",
              "tool": "<client function tool's resource name>",
              "args": {
                "zip_code": "92031"
              },
              "displayName": "get_nearest_store"
            }
          ]
        },
        "turnCompleted": true,
      }
    ]
    

And the following example is a subsequent session run with the tool output attached to the request. The client application must populate those fields, and put the same `id`, `tool`, and `display_name` values as in the previous message.
    
    
    "inputs": [
      {
        "toolResponses": {
          "toolResponses": [
            {
              "displayName": "get_nearest_store",
              "id": "<execution id>",
              "tool": "<client function tool's resource name>",
              "response": {
                "name": "Alibaba",
                "address": "43 Alpha Road, Mountain View, CA 92039, USA"
              },
            }
          ]
        }
      }
    ]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
