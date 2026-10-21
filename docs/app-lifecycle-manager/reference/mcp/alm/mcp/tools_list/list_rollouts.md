---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts/
title: MCP Tools Reference: saasservicemgmt \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:14.013162+00:00
---

# MCP Tools Reference: saasservicemgmt  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  MCP Tools Reference: saasservicemgmt Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_rollouts`

Lists Rollout resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.

The following sample demonstrate how to use `curl` to invoke the `list_rollouts` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://saasservicemgmt.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_rollouts",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request structure for the ListRollouts method.

### ListRolloutsRequest

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
`parent` |  `string` Required. The parent of the rollout.  
`pageSize` |  `integer` The maximum number of rollouts to send per page.  
`pageToken` |  `string` The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page.  
`filter` |  `string` Filter the list as specified in <https://google.aip.dev/160>.  
`orderBy` |  `string` Order results as specified in <https://google.aip.dev/132>.  
  
## Output Schema

The response structure for the ListRollouts method.

### ListRolloutsResponse

JSON representation  
---  
      
    
    {
      "rollouts": [
        {
          object ([Rollout](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.Rollout))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`rollouts[]` |  `object (`[Rollout](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.Rollout)`)` The resulting rollouts.  
`nextPageToken` |  `string` If present, the next page token can be provided to a subsequent ListRollouts call to list the next page. If empty, there are no more pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Rollout

JSON representation  
---  
      
    
    {
      "name": string,
      "release": string,
      "flagRelease": string,
      "startTime": string,
      "endTime": string,
      "state": enum (RolloutState),
      "stateMessage": string,
      "stateTransitionTime": string,
      "rootRollout": string,
      "parentRollout": string,
      "rolloutOrchestrationStrategy": string,
      "unitFilter": string,
      "rolloutKind": string,
      "stats": {
        object ([RolloutStats](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.RolloutStats))
      },
      "control": {
        object ([RolloutControl](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.RolloutControl))
      },
      "effectiveUnitFilter": string,
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
      "deleteTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/rollout/{rollout_id}"  
`release` |  `string` Optional. Immutable. Name of the Release that gets rolled out to target Units. Required if no other type of release is specified.  
`flagRelease` |  `string` Optional. Immutable. Name of the FlagRelease to be rolled out to the target Units. Release and FlagRelease are mutually exclusive.Note: `release` comment needs to be adjusted to mention that "Release and FlagRelease are mutually exclusive" when visibility restriction will be lifted.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. The time when the rollout started executing. Will be empty if the rollout hasn't started yet.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. The time when the rollout finished execution (regardless of success, failure, or cancellation). Will be empty if the rollout hasn't finished yet. Once set, the rollout is in terminal state and all the results are final.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`RolloutState`)` Output only. Current state of the rollout.  
`stateMessage` |  `string` Output only. Human readable message indicating details about the last state transition.  
`stateTransitionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. The time when the rollout transitioned into its current state.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rootRollout` |  `string` Optional. Output only. The root rollout that this rollout is stemming from. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/rollouts/{rollout_id}"  
`parentRollout` |  `string` Optional. Output only. The direct parent rollout that this rollout is stemming from. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/rollouts/{rollout_id}"  
`rolloutOrchestrationStrategy` |  `string` Optional. The strategy used for executing this Rollout. This strategy will override whatever strategy is specified in the RolloutKind. If not specified on creation, the strategy from RolloutKind will be used.There are two supported values strategies which are used to control - "Google.Cloud.Simple.AllAtOnce" - "Google.Cloud.Simple.OneLocationAtATime"A rollout with one of these simple strategies will rollout across all locations defined in the targeted UnitKind's Saas Locations.  
`unitFilter` |  `string` Optional. CEL(<https://github.com/google/cel-spec>) formatted filter string against Unit. The filter will be applied to determine the eligible unit population. This filter can only reduce, but not expand the scope of the rollout. If not provided, the unit_filter from the RolloutKind will be used.  
`rolloutKind` |  `string` Required. Immutable. Name of the RolloutKind this rollout is stemming from and adhering to.  
`stats` |  `object (`[RolloutStats](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.RolloutStats)`)` Optional. Output only. Details about the progress of the rollout.  
`control` |  `object (`[RolloutControl](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.RolloutControl)`)` Optional. Requested change to the execution of this rollout. Default RolloutControl.action is ROLLOUT_ACTION_RUN meaning the rollout will be executed to completion while progressing through all natural Rollout States (such as RUNNING -> SUCCEEDED or RUNNING -> FAILED). Requests can only be made when the Rollout is in a non-terminal state.  
`effectiveUnitFilter` |  `string` Optional. Output only. Output only snapshot of the effective unit filter at Rollout start time. Contains a CEL(<https://github.com/google/cel-spec>) expression consisting of a conjunction of Rollout.unit_filter and RolloutKind.unit_filter. This field captures the filter applied by the Rollout to determine the Unit population. If the associated RolloutKind's unit_filter is modified after the rollout is started, it will not be updated here.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was marked for deletion (deletion is an asynchronous operation).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### RolloutStats

JSON representation  
---  
      
    
    {
      "operationsByState": [
        {
          object ([Aggregate](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.Aggregate))
        }
      ],
    
      // Union field _estimated_total_unit_count can be only one of the following:
      "estimatedTotalUnitCount": string
      // End of list of possible types for union field _estimated_total_unit_count.
    }  
  
Fields  
---  
`operationsByState[]` |  `object (`[Aggregate](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.Aggregate)`)` Optional. Output only. Unordered list. A breakdown of the progress of operations triggered by the rollout. Provides a count of Operations by their state. This can be used to determine the number of units which have been updated, or are scheduled to be updated.There will be at most one entry per group. Possible values for operation groups are: - "SCHEDULED" - "PENDING" - "RUNNING" - "SUCCEEDED" - "FAILED" - "CANCELLED"  
Union field `_estimated_total_unit_count`.`_estimated_total_unit_count` can be only one of the following:  
`estimatedTotalUnitCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Output only. Estimated number of units based. The estimation is computed upon creation of the rollout.  
  
### Aggregate

JSON representation  
---  
      
    
    {
      "group": string,
      "count": integer
    }  
  
Fields  
---  
`group` |  `string` Required. Group by which to aggregate.  
`count` |  `integer` Required. Number of records in the group.  
  
### RolloutControl

JSON representation  
---  
      
    
    {
      "action": enum (RolloutAction),
    
      // Union field action_params can be only one of the following:
      "runParams": {
        object ([RunRolloutActionParams](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.RunRolloutActionParams))
      }
      // End of list of possible types for union field action_params.
    }  
  
Fields  
---  
`action` |  `enum (`RolloutAction`)` Required. Action to be performed on the Rollout. The default behavior is to run the rollout until it naturally reaches a terminal state.  
Union field `action_params`. Setting for the action. The setting must match the action e.g.: action=RUN may only set run_params or omit all parameters. It is an error to set a setting that is not applicable to the action. `action_params` can be only one of the following:  
`runParams` |  `object (`[RunRolloutActionParams](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.RunRolloutActionParams)`)` Optional. Parameters for the RUN action. It is an error to specify this if the RolloutAction is not set to RUN. By default, the rollout will retry failed operations when resumed.  
  
### RunRolloutActionParams

JSON representation  
---  
      
    
    {
      "retryFailedOperations": boolean
    }  
  
Fields  
---  
`retryFailedOperations` |  `boolean` Required. If true, the rollout will retry failed operations when resumed. This is applicable only the current state of the Rollout is PAUSED and the requested action is RUN.  
  
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
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
