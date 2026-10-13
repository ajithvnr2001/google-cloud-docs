---
url: https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/bigtable/mcp/tools_list/update_logical_view/
title: MCP Tools Reference: bigtableadmin.googleapis.com \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:17.179087+00:00
---

# MCP Tools Reference: bigtableadmin.googleapis.com  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/bigtable/mcp/tools_list/update_logical_view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  MCP Tools Reference: bigtableadmin.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_logical_view`

Updates a Bigtable logical view within a specified instance. You can update the GoogleSQL query and/or the deletion protection setting. At least one field to update (e.g., `query` or `deletion_protection`) must be provided in logical_view field. Update query example: { "project_id": "my-project", "instance_id": "my-instance", "logical_view_id": "my-logical-view", logical_view: { "query": "SELECT CF FROM my-table" } } Update deletion protection example: { "project_id": "my-project", "instance_id": "my-instance", "logical_view_id": "my-logical-view", logical_view: { "deletion_protection": true } } Update query and deletion protection example: { "project_id": "my-project", "instance_id": "my-instance", "logical_view_id": "my-logical-view", logical_view: { "query": "SELECT CF FROM my-table", "deletion_protection": true } }

The following code sample shows how to use `curl` to call the `update_logical_view` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://bigtableadmin.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_logical_view",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for Bigtable.UpdateLogicalView

### UpdateLogicalViewRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "instanceId": string,
      "logicalViewId": string,
      "logicalView": {
        object ([LogicalView](https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/bigtable/mcp/tools_list/create_logical_view#Input.Schema.LogicalView))
      }
    }  
  
Fields  
---  
`projectId` |  `string` Required. The project ID (e.g., "my-project"). If not known from the context, the Agent should attempt to get the current project ID from the gcloud config by running `gcloud config get-value project`. If the attempt fails, prompt the user for the project ID.  
`instanceId` |  `string` Required. The instance ID within the project where the logical view will be created (e.g., "my-instance").  
`logicalViewId` |  `string` Required. The ID used for the logical view within its instance, e.g., `mylogicalview`.  
`logicalView` |  `object (`[LogicalView](https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/bigtable/mcp/tools_list/create_logical_view#Input.Schema.LogicalView)`)` Required. The logical view to update.  
  
### LogicalView

JSON representation  
---  
      
    
    {
      "name": string,
      "query": string,
      "deletionProtection": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the logical view.  
`query` |  `string` Required. The logical view's select query.  
`deletionProtection` |  `boolean` Optional. Set to true to make the LogicalView protected against deletion.  
  
## Output Schema

This resource represents a long-running operation that is the result of a network API call.

### Operation

JSON representation  
---  
      
    
    {
      "name": string,
      "metadata": {
        "@type": string,
        field1: ...,
        ...
      },
      "done": boolean,
    
      // Union field result can be only one of the following:
      "error": {
        object ([Status](https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/bigtable/mcp/tools_list/create_instance#Output.Schema.Status))
      },
      "response": {
        "@type": string,
        field1: ...,
        ...
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  `object` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`done` |  `boolean` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  `object (`[Status](https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/bigtable/mcp/tools_list/create_instance#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
`response` |  `object` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` Identifies the type of the serialized Protobuf message with a URI reference consisting of a prefix ending in a slash and the fully-qualified type name.Example: type.googleapis.com/google.protobuf.StringValueThis string must contain at least one `/` character, and the content after the last `/` must be the fully-qualified name of the type in canonical form, without a leading dot. Do not write a scheme on these URI references so that clients do not attempt to contact them.The prefix is arbitrary and Protobuf implementations are expected to simply strip off everything up to and including the last `/` to identify the type. `type.googleapis.com/` is a common default prefix that some legacy implementations require. This prefix does not indicate the origin of the type, and URIs containing it are not expected to respond to any requests.All type URL strings must be legal URI references with the additional restriction (for the text format) that the content of the reference must consist only of alphanumeric characters, percent-encoded escapes, and characters in the following set (not including the outer backticks): `/-.~_!$&()*+,;=`. Despite our allowing percent encodings, implementations should not unescape them to prevent confusion with existing parsers. For example, `type.googleapis.com%2FFoo` should be rejected.In the original design of `Any`, the possibility of launching a type resolution service at these type URLs was considered but Protobuf never implemented one and considers contacting these URLs to be problematic and a potential security issue. Do not attempt to contact type URLs.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Holds a Protobuf serialization of the type described by type_url.A base64-encoded string.  
  
### Status

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ✅

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
