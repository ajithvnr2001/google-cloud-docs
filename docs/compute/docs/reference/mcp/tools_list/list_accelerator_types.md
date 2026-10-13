---
url: https://docs.cloud.google.com/compute/docs/reference/mcp/tools_list/list_accelerator_types/
title: MCP Tools Reference: compute.googleapis.com \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:49.789571+00:00
---

# MCP Tools Reference: compute.googleapis.com  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/mcp/tools_list/list_accelerator_types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  MCP Tools Reference: compute.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_accelerator_types`

Lists the available Google Compute Engine accelerator types. Requires project and zone as input. Returns accelerator types, including id, creation timestamp, name, description, deprecated, zone, and maximum cards per instance.

The following sample demonstrate how to use `curl` to invoke the `list_accelerator_types` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://compute.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_accelerator_types",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for listing accelerator types.

### McpListAcceleratorTypesRequest

JSON representation  
---  
      
    
    {
      "project": string,
      "zone": string
    }  
  
Fields  
---  
`project` |  `string` Required. Project ID for this request.  
`zone` |  `string` Required. The zone of the accelerator types.  
  
## Output Schema

Response message for listing accelerator types.

### McpListAcceleratorTypesResponse

JSON representation  
---  
      
    
    {
      "acceleratorTypes": [
        {
          object ([AcceleratorType](https://docs.cloud.google.com/compute/docs/reference/mcp/tools_list/list_accelerator_types#Output.Schema.AcceleratorType))
        }
      ]
    }  
  
Fields  
---  
`acceleratorTypes[]` |  `object (`[AcceleratorType](https://docs.cloud.google.com/compute/docs/reference/mcp/tools_list/list_accelerator_types#Output.Schema.AcceleratorType)`)` The list of accelerator types.  
  
### AcceleratorType

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "deprecated": {
        object ([DeprecationStatus](https://docs.cloud.google.com/compute/docs/reference/mcp/tools_list/list_accelerator_types#Output.Schema.DeprecationStatus))
      },
      "zone": string,
      "selfLink": string,
      "maximumCardsPerInstance": integer,
      "resourceMetadata": {
        object ([ResourceMetadata](https://docs.cloud.google.com/compute/docs/reference/mcp/tools_list/list_accelerator_types#Output.Schema.ResourceMetadata))
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. [Output Only] The type of the resource. Always `compute#acceleratorType` for accelerator types.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` [Output Only] The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` [Output Only] Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` [Output Only] Name of the resource.  
`description` |  `string` [Output Only] An optional textual description of the resource.  
`deprecated` |  `object (`[DeprecationStatus](https://docs.cloud.google.com/compute/docs/reference/mcp/tools_list/list_accelerator_types#Output.Schema.DeprecationStatus)`)` [Output Only] The deprecation status associated with this accelerator type.  
`zone` |  `string` [Output Only] The name of the zone where the accelerator type resides, such as us-central1-a. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`selfLink` |  `string` Output only. [Output Only] Server-defined, fully qualified URL for this resource.  
`maximumCardsPerInstance` |  `integer` [Output Only] Maximum number of accelerator cards allowed per instance.  
`resourceMetadata` |  `object (`[ResourceMetadata](https://docs.cloud.google.com/compute/docs/reference/mcp/tools_list/list_accelerator_types#Output.Schema.ResourceMetadata)`)` Output only. Contains standard resource metadata for an AcceleratorType resource. It is populated for each instance of the AcceleratorType resource, and includes the `api_version` the instance was retrieved through, and its canonical `resource_type` name.  
  
### DeprecationStatus

JSON representation  
---  
      
    
    {
      "state": enum (State),
      "replacement": string,
      "deprecated": string,
      "obsolete": string,
      "deleted": string
    }  
  
Fields  
---  
`state` |  `enum (`State`)` The deprecation state of this resource. This can be `ACTIVE`, `DEPRECATED`, `OBSOLETE`, or `DELETED`. Operations which communicate the end of life date for an image, can use `ACTIVE`. Operations which create a new resource using a `DEPRECATED` resource will return successfully, but with a warning indicating the deprecated resource and recommending its replacement. Operations which use `OBSOLETE` or `DELETED` resources will be rejected and result in an error.  
`replacement` |  `string` The URL of the suggested replacement for a deprecated resource. The suggested replacement resource must be the same kind of resource as the deprecated resource.  
`deprecated` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DEPRECATED`. This is only informational and the status will not change unless the client explicitly changes it.  
`obsolete` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `OBSOLETE`. This is only informational and the status will not change unless the client explicitly changes it.  
`deleted` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DELETED`. This is only informational and the status will not change unless the client explicitly changes it.  
  
### ResourceMetadata

JSON representation  
---  
      
    
    {
      "resourceType": string,
      "apiVersion": string
    }  
  
Fields  
---  
`resourceType` |  `string` The canonical resource type name in the format of a resource type as defined by [AIP-123](https://google.aip.dev/123). For example, `"compute.googleapis.com/Instance"`.  
`apiVersion` |  `string` The version of the API interface that this resource was retrieved through. For example, `"2025-01-01"` or `"2025-01-01-preview"`.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
