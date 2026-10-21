---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags/
title: MCP Tools Reference: saasservicemgmt \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:15.097055+00:00
---

# MCP Tools Reference: saasservicemgmt  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  MCP Tools Reference: saasservicemgmt Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_flags`

Lists Flag resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.

The following sample demonstrate how to use `curl` to invoke the `list_flags` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://saasservicemgmt.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_flags",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request structure for the ListFlags method.

### ListFlagsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string,
      "orderBy": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent of the flag.  
`pageSize` |  `integer` The maximum number of flags to send per page.  
`pageToken` |  `string` The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page.  
`filter` |  `string` Filter the list as specified in <https://google.aip.dev/160>.  
`orderBy` |  `string` Order results as specified in <https://google.aip.dev/132>.  
  
## Output Schema

The response structure for the ListFlags method.

### ListFlagsResponse

JSON representation  
---  
      
    
    {
      "flags": [
        {
          object ([Flag](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.Flag))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`flags[]` |  `object (`[Flag](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.Flag)`)` The resulting flags.  
`nextPageToken` |  `string` If present, the next page token can be provided to a subsequent ListFlags call to list the next page. If empty, there are no more pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Flag

JSON representation  
---  
      
    
    {
      "name": string,
      "key": string,
      "valueType": enum (FlagValueType),
      "flagValueType": enum (ValueType),
      "evaluationSpec": {
        object ([EvaluationSpec](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.EvaluationSpec))
      },
      "unitKind": string,
      "description": string,
      "variants": [
        {
          object ([FlagVariant](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.FlagVariant))
        }
      ],
      "flagSet": string,
      "state": enum (State),
      "labels": {
        string: string,
        ...
      },
      "annotations": {
        string: string,
        ...
      },
      "uid": string,
      "etag": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/flags/{flag_id}"  
`key` |  `string` Required. Immutable. Flag key used in runtime evaluation APIs (OpenFeature). Max length: 256 bytes.  
`valueType  
**(deprecated)**` |  `enum (`FlagValueType`)` This item is deprecated!Optional. Immutable. Deprecated: Use `flag_value_type` instead. Flag value type.  
`flagValueType` |  `enum (`ValueType`)` Optional. Immutable. Flag value type.  
`evaluationSpec` |  `object (`[EvaluationSpec](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.EvaluationSpec)`)` Optional. Specification of how the flag value should be evaluated.If a bool flag is created without an evaluation_spec specified, two default variants, "Enabled" (with bool_value = true) and "Disabled" (with bool_value = false), are created by default, and "Disabled" is set as the default_target.  
`unitKind` |  `string` Required. Immutable. `[UnitKind](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.UnitKind)` that can consume this flag.  
`description` |  `string` Optional. Description of the flag. Max length: 500 bytes.  
`variants[]` |  `object (`[FlagVariant](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.FlagVariant)`)` Optional. A list of variants.  
`flagSet` |  `string` Optional. Flag set this flag belongs to.  
`state` |  `enum (`State`)` Optional. Current state of the flag.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### EvaluationSpec

JSON representation  
---  
      
    
    {
      "variants": [
        {
          object ([Variant](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.Variant))
        }
      ],
      "defaultTarget": string,
      "allocations": [
        {
          object ([Allocation](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.Allocation))
        }
      ],
      "rules": [
        {
          object ([EvaluationRule](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.EvaluationRule))
        }
      ],
      "attributes": [
        string
      ]
    }  
  
Fields  
---  
`variants[]  
**(deprecated)**` |  `object (`[Variant](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.Variant)`)` This item is deprecated!Optional. A list of variants.  
`defaultTarget` |  `string` Required. Default variant or allocation of the flag.  
`allocations[]` |  `object (`[Allocation](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.Allocation)`)` Optional. A list of allocations.  
`rules[]` |  `object (`[EvaluationRule](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.EvaluationRule)`)` Optional. Evaluation rules define the logic for evaluating the flag against a given context. The rules are evaluated sequentially in their specified order.  
`attributes[]` |  `string` Optional. Names of the context attributes that are used in the evaluation rules and allocations.  
  
### Variant

JSON representation  
---  
      
    
    {
      "name": string,
    
      // Union field value can be only one of the following:
      "boolValue": boolean,
      "intValue": string,
      "stringValue": string,
      "doubleValue": number
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the variant. Max length: 128 bytes.  
Union field `value`. value is a single flag value for the variant. `value` can be only one of the following:  
`boolValue` |  `boolean` Optional. Boolean flag value.  
`intValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Integer flag value.  
`stringValue` |  `string` Optional. String flag value.  
`doubleValue` |  `number` Optional. Double flag value.  
  
### Allocation

JSON representation  
---  
      
    
    {
      "id": string,
      "randomizedOn": string,
      "description": string,
      "slots": [
        {
          object ([AllocationSlot](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.AllocationSlot))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. Allocation ID. Max length: 128 bytes.  
`randomizedOn` |  `string` Required. Key of the context attribute that is used for traffic splitting.  
`description` |  `string` Optional. Description of the allocation. Max length: 500 bytes.  
`slots[]` |  `object (`[AllocationSlot](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.AllocationSlot)`)` Required. Slots defines the weighted distribution of variants.  
  
### AllocationSlot

JSON representation  
---  
      
    
    {
      "variant": string,
      "weight": integer
    }  
  
Fields  
---  
`variant` |  `string` Required. Variant of the allocation slot.  
`weight` |  `integer` Required. Weight defines the proportion of traffic to allocate to the variant, relative to other slots in the same allocation.  
  
### EvaluationRule

JSON representation  
---  
      
    
    {
      "id": string,
      "condition": string,
      "target": string
    }  
  
Fields  
---  
`id` |  `string` Required. Evaluation rule ID. Max length: 128 bytes.  
`condition` |  `string` Required. A Common Expression Language (CEL) expression that evaluates to a boolean. The expression is evaluated against the provided context. If it returns true, the rule's target is applied.  
`target` |  `string` Required. The target variant or allocation to apply if the condition is met. This should match the name of a defined variant or allocation's ID.  
  
### FlagVariant

JSON representation  
---  
      
    
    {
      "id": string,
      "trackingId": string,
      "description": string,
    
      // Union field value can be only one of the following:
      "booleanValue": boolean,
      "integerValue": string,
      "stringValue": string,
      "doubleValue": number
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
`id` |  `string` Required. Variant ID. Max length: 128 bytes.  
`trackingId` |  `string` Optional. trackingId is unique depending on name and value of the variant within the scope of the service. It is typically generated by the server and must not be changed. trackingId is used to uniquely identify and track variants.  
`description` |  `string` Optional. A human-readable description of what this variant does or represents.  
Union field `value`. value is a single flag value for the variant. `value` can be only one of the following:  
`booleanValue` |  `boolean` Optional. Boolean variant value.  
`integerValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Integer variant value.  
`stringValue` |  `string` Optional. String variant value.  
`doubleValue` |  `number` Optional. Double variant value.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### AnnotationsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
