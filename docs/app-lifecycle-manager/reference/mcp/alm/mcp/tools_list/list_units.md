---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units/
title: MCP Tools Reference: saasservicemgmt \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:15.791365+00:00
---

# MCP Tools Reference: saasservicemgmt  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  MCP Tools Reference: saasservicemgmt Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_units`

Lists Unit resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.

The following sample demonstrate how to use `curl` to invoke the `list_units` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://saasservicemgmt.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_units",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request structure for the ListUnits method.

### ListUnitsRequest

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
`parent` |  `string` Required. The parent of the unit.  
`pageSize` |  `integer` The maximum number of units to send per page.  
`pageToken` |  `string` The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page.  
`filter` |  `string` Filter the list as specified in <https://google.aip.dev/160>.  
`orderBy` |  `string` Order results as specified in <https://google.aip.dev/132>.  
  
## Output Schema

The response structure for the ListUnits method.

### ListUnitsResponse

JSON representation  
---  
      
    
    {
      "units": [
        {
          object ([Unit](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.Unit))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`units[]` |  `object (`[Unit](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.Unit)`)` The resulting units.  
`nextPageToken` |  `string` If present, the next page token can be provided to a subsequent ListUnits call to list the next page. If empty, there are no more pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Unit

JSON representation  
---  
      
    
    {
      "name": string,
      "unitKind": string,
      "release": string,
      "tenant": string,
      "ongoingOperations": [
        string
      ],
      "pendingOperations": [
        string
      ],
      "scheduledOperations": [
        string
      ],
      "dependents": [
        {
          object ([UnitDependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitDependency))
        }
      ],
      "dependencies": [
        {
          object ([UnitDependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitDependency))
        }
      ],
      "inputVariables": [
        {
          object ([UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitVariable))
        }
      ],
      "outputVariables": [
        {
          object ([UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitVariable))
        }
      ],
      "maintenance": {
        object ([MaintenanceSettings](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.MaintenanceSettings))
      },
      "state": enum (UnitState),
      "conditions": [
        {
          object ([UnitCondition](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitCondition))
        }
      ],
      "managementMode": enum (ManagementMode),
      "systemManagedState": enum (SystemManagedState),
      "systemCleanupAt": string,
      "flagRevisions": [
        string
      ],
      "application": string,
      "flagConfigName": string,
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
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/units/{unit}"  
`unitKind` |  `string` Optional. Reference to the UnitKind this Unit belongs to. Immutable once set.  
`release` |  `string` Optional. Output only. The current Release object for this Unit.  
`tenant` |  `string` Optional. Reference to the Saas Tenant resource this unit belongs to. This for example informs the maintenance policies to use for scheduling future updates on a unit. (optional and immutable once created)  
`ongoingOperations[]` |  `string` Optional. Output only. List of concurrent UnitOperations that are operating on this Unit.  
`pendingOperations[]` |  `string` Optional. Output only. List of pending (wait to be executed) UnitOperations for this unit.  
`scheduledOperations[]` |  `string` Optional. Output only. List of scheduled UnitOperations for this unit.  
`dependents[]` |  `object (`[UnitDependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitDependency)`)` Optional. Output only. List of Units that depend on this unit. Unit can only be deprovisioned if this list is empty. Maximum 1000.  
`dependencies[]` |  `object (`[UnitDependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitDependency)`)` Optional. Output only. Set of dependencies for this unit. Maximum 10.  
`inputVariables[]` |  `object (`[UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitVariable)`)` Optional. Output only. Indicates the current input variables deployed by the unit  
`outputVariables[]` |  `object (`[UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitVariable)`)` Optional. Output only. Set of key/value pairs corresponding to output variables from execution of actuation templates. The variables are declared in actuation configs (e.g in helm chart or terraform) and the values are fetched and returned by the actuation engine upon completion of execution.  
`maintenance` |  `object (`[MaintenanceSettings](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.MaintenanceSettings)`)` Optional. Captures requested directives for performing future maintenance on the unit. This includes a request for the unit to skip maintenance for a period of time and remain pinned to its current release as well as controls for postponing maintenance scheduled in future.  
`state` |  `enum (`UnitState`)` Optional. Output only. Current lifecycle state of the resource (e.g. if it's being created or ready to use).  
`conditions[]` |  `object (`[UnitCondition](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitCondition)`)` Optional. Output only. A set of conditions which indicate the various conditions this resource can have.  
`managementMode` |  `enum (`ManagementMode`)` Optional. Immutable. Indicates whether the Unit life cycle is controlled by the user or by the system. Immutable once created.  
`systemManagedState` |  `enum (`SystemManagedState`)` Optional. Output only. Indicates the system managed state of the unit.  
`systemCleanupAt` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. If set, indicates the time when the system will start removing the unit.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`flagRevisions[]` |  `string` Optional. Output only. Flag revisions used by this Unit.  
`application` |  `string` Optional. Reference to the AppHub Application this unit belongs to. All resources deployed in this Unit will be associated with the specified Application.  
`flagConfigName` |  `string` Output only. This field stores the unique identifier for the flag configuration to be used by this Unit.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`satisfiesPzs` |  `boolean` Output only. Indicates whether the resource location satisfies Zone Separation constraints. This is false by default.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
  
### UnitDependency

JSON representation  
---  
      
    
    {
      "alias": string,
      "unit": string
    }  
  
Fields  
---  
`alias` |  `string` Output only. Alias for the name of the dependency.  
`unit` |  `string` Output only. A reference to the Unit object.  
  
### UnitVariable

JSON representation  
---  
      
    
    {
      "variable": string,
      "type": enum (Type),
      "value": string
    }  
  
Fields  
---  
`variable` |  `string` Required. Immutable. Name of the variable from actuation configs.  
`type` |  `enum (`Type`)` Optional. Immutable. Name of a supported variable type. Supported types are string, int, bool.  
`value` |  `string` Optional. String encoded value for the variable.  
  
### MaintenanceSettings

JSON representation  
---  
      
    
    {
      "pinnedUntilTime": string
    }  
  
Fields  
---  
`pinnedUntilTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. If present, it fixes the release on the unit until the given time; i.e. changes to the release field will be rejected. Rollouts should and will also respect this by not requesting an upgrade in the first place.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### UnitCondition

JSON representation  
---  
      
    
    {
      "status": enum (Status),
      "type": enum (Type),
      "lastTransitionTime": string,
      "message": string,
      "reason": string
    }  
  
Fields  
---  
`status` |  `enum (`Status`)` Required. Status of the condition.  
`type` |  `enum (`Type`)` Required. Type of the condition.  
`lastTransitionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Last time the condition transited from one status to another.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`message` |  `string` Required. Human readable message indicating details about the last transition.  
`reason` |  `string` Required. Brief reason for the condition's last transition.  
  
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
