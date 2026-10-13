---
url: https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp/tools_list/get_k8s_resource/
title: MCP Tools Reference: container.googleapis.com \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:21.530924+00:00
---

# MCP Tools Reference: container.googleapis.com  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp/tools_list/get_k8s_resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  MCP Tools Reference: container.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_k8s_resource`

Gets one or more Kubernetes resources from a cluster. Resources can be filtered by type, name, namespace, and label selectors. Returns the resources in YAML format. This is similar to running `kubectl get`.

The following sample demonstrate how to use `curl` to invoke the `get_k8s_resource` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://container.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_k8s_resource",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for retrieving Kubernetes resources.

### GetK8SResourceRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "resourceType": string,
      "name": string,
      "namespace": string,
      "labelSelector": string,
      "fieldSelector": string,
      "customColumns": string,
      "outputFormat": enum (OutputFormat)
    }  
  
Fields  
---  
`parent` |  `string` Required. The cluster, which owns this collection of resources. Format: projects/{project}/locations/{location}/clusters/{cluster}  
`resourceType` |  `string` Required. The type of resource to retrieve. Kubernetes resource/kind name in singular form, lower case. e.g. "pod", "deployment", "service".  
`name` |  `string` Optional. The name of the resource to retrieve. If not specified, all resources of the given type are returned.  
`namespace` |  `string` Optional. The namespace of the resource. If not specified, all namespaces are searched.  
`labelSelector` |  `string` Optional. A label selector to filter resources.  
`fieldSelector` |  `string` Optional. A field selector to filter resources.  
`customColumns` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The field mask to specify columns to display. Use a single "*" to get all fields. When both custom_columns and output_format are specified, output_format is ignored.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`outputFormat` |  `enum (`OutputFormat`)` Optional. The output format. One of: (table, wide, yaml, json). If not specified, defaults to table. When both custom_columns and output_format are specified, output_format is ignored.  
  
### FieldMask

JSON representation  
---  
      
    
    {
      "paths": [
        string
      ]
    }  
  
Fields  
---  
`paths[]` |  `string` The set of field mask paths.  
  
## Output Schema

Response for retrieving Kubernetes resources.

### GetK8SResourceResponse

JSON representation  
---  
      
    
    {
      "output": string,
      "errors": [
        {
          object ([Status](https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp/tools_list/list_k8s_api_resources#Output.Schema.Status))
        }
      ]
    }  
  
Fields  
---  
`output` |  `string` The output of the command in the requested format. It may contain resources in YAML or JSON format, or a table in plain text, or errors.  
`errors[]` |  `object (`[Status](https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp/tools_list/list_k8s_api_resources#Output.Schema.Status)`)` Errors encountered during retrieval.  
  
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
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
