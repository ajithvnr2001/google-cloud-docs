---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_flag_release/
title: MCP Tools Reference: saasservicemgmt \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:54:18.728871+00:00
---

# MCP Tools Reference: saasservicemgmt  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_flag_release/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  MCP Tools Reference: saasservicemgmt Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_flag_release`

Creates a FlagRelease resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'flag_release_id', 'flag_release'. Optional parameters: 'validate_only', 'request_id'.

The following sample demonstrate how to use `curl` to invoke the `create_flag_release` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://saasservicemgmt.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_flag_release",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request structure for the CreateFlagRelease method.

### CreateFlagReleaseRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "flagReleaseId": string,
      "flagRelease": {
        object ([FlagRelease](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases#Output.Schema.FlagRelease))
      },
      "validateOnly": boolean,
      "requestId": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent of the flag release.  
`flagReleaseId` |  `string` Required. The ID value for the new flag release.  
`flagRelease` |  `object (`[FlagRelease](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases#Output.Schema.FlagRelease)`)` Required. The desired state for the flag release.  
`validateOnly` |  `boolean` If "validate_only" is set to true, the service will try to validate that this request would succeed, but will not actually make changes.  
`requestId` |  `string` An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### FlagRelease

JSON representation  
---  
      
    
    {
      "name": string,
      "flagRevisions": [
        string
      ],
      "obsoleteFlags": [
        string
      ],
      "unitKind": string,
      "flagSets": [
        string
      ],
      "allFlags": boolean,
      "effectiveFlagRevisions": [
        string
      ],
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
    
      // Union field release_content can be only one of the following:
      "flagRevisionsRelease": {
        object ([FlagRevisionList](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases#Output.Schema.FlagRevisionList))
      },
      "flagSetsRelease": {
        object ([FlagSetList](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases#Output.Schema.FlagSetList))
      },
      "allFlagsRelease": boolean
      // End of list of possible types for union field release_content.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/flagReleases/{flag_release_id}"  
`flagRevisions[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. Immutable. DEPRECATED: Use flag_revisions_release instead. `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_revisions#Output.Schema.FlagRevision)`s to be rolled out. Only one of flag_revisions, all_flags, or flag_sets can be set. It used to be the ultimate source to truth and has been moved to effective_flag_revisions.  
`obsoleteFlags[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. Immutable. Deprecated: Use the 'state' field in the 'Flag' resource to manage the cleanup of flag lifecycles including removal from UnitKind and Units. `[Flag](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.Flag)`s to be removed from given UnitKind and all related Units. If `[Flag](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.Flag)` is provided here, its `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_revisions#Output.Schema.FlagRevision)`s will be removed from UnitKind and Units.  
`unitKind` |  `string` Required. Immutable. The `[UnitKind](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.UnitKind)` this FlagRelease applies to.  
`flagSets[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. Immutable. DEPRECATED: Use flag_sets_release instead. Flag sets to be rolled out. Only one of flag_revisions, all_flags, or flag_sets can be set.  
`allFlags  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Immutable. DEPRECATED: Use all_flags_release instead. Rollout all flags in the provided UnitKind. Only one of flag_revisions, all_flags, or flag_sets can be set.  
`effectiveFlagRevisions[]` |  `string` Output only. An OUTPUT_ONLY field that contains `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_revisions#Output.Schema.FlagRevision)`s to be rolled out. This is the ultimate source of truth of what a `[Rollout](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.Rollout)` or a `[UnitOperation](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_operations#Output.Schema.UnitOperation)` carries.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `release_content`. Defines the content or type of this flag release. Only one field within this oneof can be set. `release_content` can be only one of the following:  
`flagRevisionsRelease` |  `object (`[FlagRevisionList](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases#Output.Schema.FlagRevisionList)`)` Optional. Immutable. Specifies the release consists of a list of flag revisions.  
`flagSetsRelease` |  `object (`[FlagSetList](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases#Output.Schema.FlagSetList)`)` Optional. Immutable. Specifies the release consists of a list of flag sets.  
`allFlagsRelease` |  `boolean` Optional. Immutable. Specifies the release includes all flags.  
  
### FlagRevisionList

JSON representation  
---  
      
    
    {
      "revisions": [
        string
      ]
    }  
  
Fields  
---  
`revisions[]` |  `string` Required. `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_revisions#Output.Schema.FlagRevision)`s to be rolled out.  
  
### FlagSetList

JSON representation  
---  
      
    
    {
      "sets": [
        string
      ]
    }  
  
Fields  
---  
`sets[]` |  `string` Required. Flag sets to be rolled out.  
  
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
  
## Output Schema

A collection of `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_revisions#Output.Schema.FlagRevision)`s.

### FlagRelease

JSON representation  
---  
      
    
    {
      "name": string,
      "flagRevisions": [
        string
      ],
      "obsoleteFlags": [
        string
      ],
      "unitKind": string,
      "flagSets": [
        string
      ],
      "allFlags": boolean,
      "effectiveFlagRevisions": [
        string
      ],
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
    
      // Union field release_content can be only one of the following:
      "flagRevisionsRelease": {
        object ([FlagRevisionList](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases#Output.Schema.FlagRevisionList))
      },
      "flagSetsRelease": {
        object ([FlagSetList](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases#Output.Schema.FlagSetList))
      },
      "allFlagsRelease": boolean
      // End of list of possible types for union field release_content.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/flagReleases/{flag_release_id}"  
`flagRevisions[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. Immutable. DEPRECATED: Use flag_revisions_release instead. `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_revisions#Output.Schema.FlagRevision)`s to be rolled out. Only one of flag_revisions, all_flags, or flag_sets can be set. It used to be the ultimate source to truth and has been moved to effective_flag_revisions.  
`obsoleteFlags[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. Immutable. Deprecated: Use the 'state' field in the 'Flag' resource to manage the cleanup of flag lifecycles including removal from UnitKind and Units. `[Flag](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.Flag)`s to be removed from given UnitKind and all related Units. If `[Flag](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags#Output.Schema.Flag)` is provided here, its `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_revisions#Output.Schema.FlagRevision)`s will be removed from UnitKind and Units.  
`unitKind` |  `string` Required. Immutable. The `[UnitKind](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.UnitKind)` this FlagRelease applies to.  
`flagSets[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. Immutable. DEPRECATED: Use flag_sets_release instead. Flag sets to be rolled out. Only one of flag_revisions, all_flags, or flag_sets can be set.  
`allFlags  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Immutable. DEPRECATED: Use all_flags_release instead. Rollout all flags in the provided UnitKind. Only one of flag_revisions, all_flags, or flag_sets can be set.  
`effectiveFlagRevisions[]` |  `string` Output only. An OUTPUT_ONLY field that contains `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_revisions#Output.Schema.FlagRevision)`s to be rolled out. This is the ultimate source of truth of what a `[Rollout](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts#Output.Schema.Rollout)` or a `[UnitOperation](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_operations#Output.Schema.UnitOperation)` carries.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `release_content`. Defines the content or type of this flag release. Only one field within this oneof can be set. `release_content` can be only one of the following:  
`flagRevisionsRelease` |  `object (`[FlagRevisionList](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases#Output.Schema.FlagRevisionList)`)` Optional. Immutable. Specifies the release consists of a list of flag revisions.  
`flagSetsRelease` |  `object (`[FlagSetList](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases#Output.Schema.FlagSetList)`)` Optional. Immutable. Specifies the release consists of a list of flag sets.  
`allFlagsRelease` |  `boolean` Optional. Immutable. Specifies the release includes all flags.  
  
### FlagRevisionList

JSON representation  
---  
      
    
    {
      "revisions": [
        string
      ]
    }  
  
Fields  
---  
`revisions[]` |  `string` Required. `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_revisions#Output.Schema.FlagRevision)`s to be rolled out.  
  
### FlagSetList

JSON representation  
---  
      
    
    {
      "sets": [
        string
      ]
    }  
  
Fields  
---  
`sets[]` |  `string` Required. Flag sets to be rolled out.  
  
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

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
