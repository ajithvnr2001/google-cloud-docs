---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_release/
title: MCP Tools Reference: saasservicemgmt \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:13.695631+00:00
---

# MCP Tools Reference: saasservicemgmt  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_release/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  MCP Tools Reference: saasservicemgmt Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_release`

Gets a Release resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/releases/my-release).

The following sample demonstrate how to use `curl` to invoke the `get_release` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://saasservicemgmt.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_release",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request structure for the GetRelease method.

### GetReleaseRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the resource within a service.  
  
## Output Schema

A new version to be propagated and deployed to units. This includes pointers to packaged blueprints for actuation (e.g Helm or Terraform configuration packages) via artifact registry.

### Release

JSON representation  
---  
      
    
    {
      "name": string,
      "unitKind": string,
      "blueprint": {
        object ([Blueprint](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_releases#Output.Schema.Blueprint))
      },
      "releaseRequirements": {
        object ([ReleaseRequirements](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_releases#Output.Schema.ReleaseRequirements))
      },
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
      "inputVariableDefaults": [
        {
          object ([UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitVariable))
        }
      ],
      "applicationTemplateComponent": {
        object ([ComponentRef](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.ComponentRef))
      },
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
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/releases/{release}"  
`unitKind` |  `string` Required. Immutable. Reference to the UnitKind this Release corresponds to (required and immutable once created).  
`blueprint` |  `object (`[Blueprint](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_releases#Output.Schema.Blueprint)`)` Optional. Blueprints are OCI Images that contain all of the artifacts needed to provision a unit.  
`releaseRequirements` |  `object (`[ReleaseRequirements](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_releases#Output.Schema.ReleaseRequirements)`)` Optional. Set of requirements to be fulfilled on the Unit when using this Release.  
`inputVariables[]` |  `object (`[UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitVariable)`)` Optional. Output only. List of input variables declared on the blueprint and can be present with their values on the unit spec  
`outputVariables[]` |  `object (`[UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitVariable)`)` Optional. Output only. List of output variables declared on the blueprint and can be present with their values on the unit status  
`inputVariableDefaults[]` |  `object (`[UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units#Output.Schema.UnitVariable)`)` Optional. Mapping of input variables to default values. Maximum 100  
`applicationTemplateComponent` |  `object (`[ComponentRef](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.ComponentRef)`)` Output only. Reference to component and revision in a composite ApplicationTemplate.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Blueprint

JSON representation  
---  
      
    
    {
      "package": string,
      "engine": string,
      "version": string
    }  
  
Fields  
---  
`package` |  `string` Optional. Immutable. URI to a blueprint used by the Unit (required unless unitKind or release is set).  
`engine` |  `string` Output only. Type of the engine used to actuate the blueprint. e.g. terraform, helm etc.  
`version` |  `string` Output only. Version metadata if present on the blueprint.  
  
### ReleaseRequirements

JSON representation  
---  
      
    
    {
      "upgradeableFromReleases": [
        string
      ]
    }  
  
Fields  
---  
`upgradeableFromReleases[]` |  `string` Optional. A list of releases from which a unit can be upgraded to this one (optional). If left empty no constraints will be applied. When provided, unit upgrade requests to this release will check and enforce this constraint.  
  
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
  
### ComponentRef

JSON representation  
---  
      
    
    {
      "compositeRef": {
        object ([CompositeRef](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_saas#Output.Schema.CompositeRef))
      },
      "component": string,
      "revision": string
    }  
  
Fields  
---  
`compositeRef` |  `object (`[CompositeRef](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_saas#Output.Schema.CompositeRef)`)` Reference to the Composite ApplicationTemplate.  
`component` |  `string` Name of the component in composite.Components  
`revision` |  `string` Revision of the component. If the component does not have a revision, this field will be explicitly set to the revision of the composite ApplicationTemplate.  
  
### CompositeRef

JSON representation  
---  
      
    
    {
      "applicationTemplate": string,
      "revision": string,
      "syncOperation": string
    }  
  
Fields  
---  
`applicationTemplate` |  `string` Required. Reference to the ApplicationTemplate resource.  
`revision` |  `string` Revision of the ApplicationTemplate to use. Changes to revision will trigger manual resynchronization. If empty, ApplicationTemplate will be ignored.  
`syncOperation` |  `string` Output only. Reference to on-going AppTemplate import and replication operation (i.e. the operation_id for the long-running operation). This field is opaque for external usage.  
  
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
