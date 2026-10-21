---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_rollout_kind/
title: MCP Tools Reference: saasservicemgmt \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:14.364540+00:00
---

# MCP Tools Reference: saasservicemgmt  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_rollout_kind/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  MCP Tools Reference: saasservicemgmt Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_rollout_kind`

Gets a RolloutKind resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/rolloutKinds/my-rolloutkind).

The following sample demonstrate how to use `curl` to invoke the `get_rollout_kind` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://saasservicemgmt.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_rollout_kind",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request structure for the GetRolloutKind method.

### GetRolloutKindRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the resource within a service.  
  
## Output Schema

An object that describes various settings of Rollout execution. Includes built-in policies across Google Cloud and Google Distributed Cloud, and customizable policies.

### RolloutKind

JSON representation  
---  
      
    
    {
      "name": string,
      "unitKind": string,
      "rolloutOrchestrationStrategy": string,
      "unitFilter": string,
      "updateUnitKindStrategy": enum (UpdateUnitKindStrategy),
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
      "updateTime": string,
    
      // Union field _error_budget can be only one of the following:
      "errorBudget": {
        object ([ErrorBudget](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollout_kinds#Output.Schema.ErrorBudget))
      }
      // End of list of possible types for union field _error_budget.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/rolloutKinds/{rollout_kind_id}"  
`unitKind` |  `string` Required. Immutable. UnitKind that this rollout kind corresponds to. Rollouts stemming from this rollout kind will target the units of this unit kind. In other words, this defines the population of target units to be upgraded by rollouts.  
`rolloutOrchestrationStrategy` |  `string` Optional. The strategy used for executing a Rollout. This is a required field.There are two supported values strategies which are used to control - "Google.Cloud.Simple.AllAtOnce" - "Google.Cloud.Simple.OneLocationAtATime"A rollout with one of these simple strategies will rollout across all locations defined in the associated UnitKind's Saas Locations.  
`unitFilter` |  `string` Optional. CEL(<https://github.com/google/cel-spec>) formatted filter string against Unit. The filter will be applied to determine the eligible unit population. This filter can only reduce, but not expand the scope of the rollout.  
`updateUnitKindStrategy` |  `enum (`UpdateUnitKindStrategy`)` Optional. The config for updating the unit kind. By default, the unit kind will be updated on the rollout start.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `_error_budget`.`_error_budget` can be only one of the following:  
`errorBudget` |  `object (`[ErrorBudget](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollout_kinds#Output.Schema.ErrorBudget)`)` Optional. The configuration for error budget. If the number of failed units exceeds max(allowed_count, allowed_ratio * total_units), the rollout will be paused. If not set, all units will be attempted to be updated regardless of the number of failures encountered.  
  
### ErrorBudget

JSON representation  
---  
      
    
    {
    
      // Union field _allowed_count can be only one of the following:
      "allowedCount": integer
      // End of list of possible types for union field _allowed_count.
    
      // Union field _allowed_percentage can be only one of the following:
      "allowedPercentage": integer
      // End of list of possible types for union field _allowed_percentage.
    }  
  
Fields  
---  
Union field `_allowed_count`.`_allowed_count` can be only one of the following:  
`allowedCount` |  `integer` Optional. The maximum number of failed units allowed in a location without pausing the rollout.  
Union field `_allowed_percentage`.`_allowed_percentage` can be only one of the following:  
`allowedPercentage` |  `integer` Optional. The maximum percentage of units allowed to fail (0, 100] within a location without pausing the rollout.  
  
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
