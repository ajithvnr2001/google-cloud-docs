---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-payload-policy/
title: ParsePayload policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:39:16.427249+00:00
---

# ParsePayload policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-payload-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  ParsePayload policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The `ParsePayload` policy extracts logical operations from structured request payloads (such as JSON-RPC 2.0) into message flow variables. This functionality enables the proxy admin to implement conditional routing logic directly based on client request contents rather than basic resource paths or query parameters.

**Note:** The `ParsePayload` policy is available in Apigee `1-17-0-apigee-7` and later, and in Apigee Hybrid version 1.16.1 and later. **Warning:** The `ParsePayload` policy does not support message streaming. Using this policy with streaming enabled on the request or response will cause errors. See [Payload with Streaming Antipattern](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/payload-with-streaming) for more information. 

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## `<ParsePayload>` element

Specifies validation parsing properties applied toward application logic evaluation cycles.

Required? | Required  
---|---  
Parent Element | n/a  
Child Elements |  `<Source>`  
`<PayloadType>`  
`<Protocol>`  
  
### Syntax

The `ParsePayload` element uses the following syntax:
    
    
    <ParsePayload continueOnError="[false|true]" enabled="[true|false]" name="policy_name">
        <Source>request</Source>
        <PayloadType>JSON-RPC-2.0</PayloadType>
        <Protocol>MCP</Protocol>
    </ParsePayload>

### Example

The following example shows a standard configuration for the `ParsePayload` policy:
    
    
    <ParsePayload continueOnError="false" enabled="true" name="parse-payload-mcp">
        <Source>request</Source>
        <PayloadType>JSON-RPC-2.0</PayloadType>
        <Protocol>MCP</Protocol>
    </ParsePayload>

## `<Source>`

Indicates the request/response container context processed immediately through runtime evaluations.
    
    
    <Source>request</Source>

Attribute | Description | Default | Presence  
---|---|---|---  
N/A | Text node value. Must be `request` or `response`. | `request` | Optional  
  
## `<PayloadType>`

Governs overall evaluation structures recognized regarding data processing requirements.
    
    
    <PayloadType>JSON-RPC-2.0</PayloadType>

Attribute | Description | Default | Presence  
---|---|---|---  
N/A | Text node value. Supported values: `JSON-RPC-2.0`. | N/A | Required  
  
## `<Protocol>`

Determines formatting behaviors corresponding precisely with target interface declarations.
    
    
    <Protocol>MCP</Protocol>

Attribute | Description | Default | Presence  
---|---|---|---  
N/A | Text node value. Supported value: `MCP`. | N/A | Required  
  
## Extracted Flow Variables

After the policy executes successfully, it populates flow variables prefixed with the policy instance name. These variables follow the pattern `parsepayload.policyName.suffix`, where `policyName` is the value of the `name` attribute in the policy XML configuration. This naming convention is consistent with other Apigee policies such as VerifyAPIKey and allows multiple `ParsePayload` policies in the same proxy to maintain distinct variable namespaces.

For a policy named `parse-payload-mcp`, the following variables are set:

Variable Name | Description  
---|---  
`parsepayload.parse-payload-mcp.operation` | Constructed execution identifier. 

  * For `tools/call`, it is `tools/call/{name}` (e.g., `tools/call/get_weather`), distinguishing the specific tool being invoked.
  * For `tools/list`, it is `tools/list`, used when listing available tools without targeting a specific one.

  
`parsepayload.parse-payload-mcp.json-rpc.request.method` | The `method` field from the JSON-RPC request (e.g., `tools/call` or `tools/list`).  
`parsepayload.parse-payload-mcp.json-rpc.request.id` | The `id` field from the JSON-RPC request.  
`parsepayload.parse-payload-mcp.json-rpc.request.params.name` | The `name` field inside `params` (populated for `tools/call` to identify the tool).  
`parsepayload.parse-payload-mcp.json-rpc.request.params.arguments.{arg_name}` | Arguments passed in the `arguments` object. String values are stored directly; nested objects or arrays are stored as serialized JSON strings.  
  
### Example

For the following JSON-RPC request payload with simple arguments:
    
    
    {
      "jsonrpc": "2.0",
      "id": "req_001",
      "method": "tools/call",
      "params": {
        "name": "get_weather",
        "arguments": {
          "location": "San Francisco, CA",
          "forecast_days": 3
        }
      }
    }

The policy populates the following variables:

Variable | Value  
---|---  
`parsepayload.parse-payload-mcp.operation` | `tools/call/get_weather`  
`parsepayload.parse-payload-mcp.json-rpc.request.method` | `tools/call`  
`parsepayload.parse-payload-mcp.json-rpc.request.id` | `req_001`  
`parsepayload.parse-payload-mcp.json-rpc.request.params.name` | `get_weather`  
`parsepayload.parse-payload-mcp.json-rpc.request.params.arguments.location` | `San Francisco, CA`  
`parsepayload.parse-payload-mcp.json-rpc.request.params.arguments.forecast_days` | `3`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
