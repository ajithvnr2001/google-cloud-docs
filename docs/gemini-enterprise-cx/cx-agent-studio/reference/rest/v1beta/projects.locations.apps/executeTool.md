---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/executeTool/
title: Method: projects.locations.apps.executeTool \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:42.775152+00:00
---

# Method: projects.locations.apps.executeTool  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/executeTool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.executeTool Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * MockConfig
    * JSON representation
  * MockedToolCall
    * JSON representation
  * MockConfig.UnmatchedToolCallBehavior



Executes the given tool with the given arguments.

### HTTP request

`POST https://ces.googleapis.com/v1beta/{parent=projects/*/locations/*/apps/*}:executeTool`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the app which the tool/toolset belongs to. Format: `projects/{project}/locations/{location}/apps/{app}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "args": {
        object
      },
      "mockConfig": {
        object ([MockConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/executeTool#MockConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool))
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "variables": {
        object
      },
      "context": {
        object
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`args` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The input parameters and values for the tool in JSON object format.  
`mockConfig` |  `object (`[MockConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/executeTool#MockConfig)`)` Optional. Mock configuration for the tool execution. If this field is set, tools that call other tools will be mocked based on the provided patterns and responses.  
The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`tool` |  `string` Optional. The name of the tool to execute. Format: projects/{project}/locations/{location}/apps/{app}/tools/{tool}  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool)`)` Optional. The toolset tool to execute. Only one tool should match the predicate from the toolset. Otherwise, an error will be returned.  
End of mutually exclusive fields.  
Additional context to be provided for the tool execution The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`variables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The variables that are available for the tool execution.  
`context` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The [ToolCallContext](<https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/python#environment> for details) to be passed to the Python tool.  
End of mutually exclusive fields.  
  
### Response body

Response message for `[ToolService.ExecuteTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/executeTool#google.cloud.ces.v1beta.ToolService.ExecuteTool)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "response": {
        object
      },
      "variables": {
        object
      },
      "citations": {
        object ([Citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Citations))
      },
      "googleSearchSuggestions": {
        object ([GoogleSearchSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/GoogleSearchSuggestions))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`response` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`variables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The variable values at the end of the tool execution.  
`citations` |  `object (`[Citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Citations)`)` Citations that provide the source information for the tool's execution.  
`googleSearchSuggestions` |  `object (`[GoogleSearchSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/GoogleSearchSuggestions)`)` The suggestions returned from Google Search as a result of invoking the Google Search Tool during the tool execution.  
The identifier of the tool that got executed. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`tool` |  `string` The name of the tool that got executed. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool)`)` The toolset tool that got executed.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.tools.execute`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## MockConfig

Mock tool calls configuration for the session.

JSON representation  
---  
      
    
    {
      "mockedToolCalls": [
        {
          object ([MockedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/executeTool#MockedToolCall))
        }
      ],
      "unmatchedToolCallBehavior": enum ([MockConfig.UnmatchedToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/executeTool#MockConfig.UnmatchedToolCallBehavior))
    }  
  
Fields  
---  
`mockedToolCalls[]` |  `object (`[MockedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/executeTool#MockedToolCall)`)` Optional. All tool calls to mock for the duration of the session.  
`unmatchedToolCallBehavior` |  `enum (`[MockConfig.UnmatchedToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps/executeTool#MockConfig.UnmatchedToolCallBehavior)`)` Required. Beavhior for tool calls that don't match any args patterns in mockedToolCalls.  
  
## MockedToolCall

A mocked tool call.

Expresses the target tool + a pattern to match against that tool's args / inputs. If the pattern matches, then the mock response will be returned.

JSON representation  
---  
      
    
    {
      "tool": string,
      "expectedArgsPattern": {
        object
      },
      "mockResponse": {
        object
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "toolId": string,
      "toolset": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`tool  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated. Use tool_identifier instead.  
`expectedArgsPattern` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. A pattern to match against the args / inputs of all dispatched tool calls. If the tool call inputs match this pattern, then mock output will be returned.  
`mockResponse` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The mock response / output to return if the tool call args / inputs match the pattern.  
The identifier of the tool to mock. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`toolId` |  `string` Optional. The name of the tool to mock. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolset` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool)`)` Optional. The toolset to mock.  
End of mutually exclusive fields.  
  
## MockConfig.UnmatchedToolCallBehavior

What to do when a tool call doesn't match any mocked tool calls.

Enums  
---  
`UNMATCHED_TOOL_CALL_BEHAVIOR_UNSPECIFIED` | Default value. This value is unused.  
`FAIL` | Throw an error for any tool calls that don't match a mock expected input pattern.  
`PASS_THROUGH` | For unmatched tool calls, pass the tool call through to real tool.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
