---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds/
title: MCP Tools Reference: saasservicemgmt \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:13.124325+00:00
---

# MCP Tools Reference: saasservicemgmt  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  MCP Tools Reference: saasservicemgmt Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_unit_kinds`

Lists UnitKind resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.

The following sample demonstrate how to use `curl` to invoke the `list_unit_kinds` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://saasservicemgmt.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_unit_kinds",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request structure for the ListUnitKinds method.

### ListUnitKindsRequest

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
`parent` |  `string` Required. The parent of the unit kind.  
`pageSize` |  `integer` The maximum number of unit kinds to send per page.  
`pageToken` |  `string` The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page.  
`filter` |  `string` Filter the list as specified in <https://google.aip.dev/160>.  
`orderBy` |  `string` Order results as specified in <https://google.aip.dev/132>.  
  
## Output Schema

The response structure for the ListUnitKinds method.

### ListUnitKindsResponse

JSON representation  
---  
      
    
    {
      "unitKinds": [
        {
          object ([UnitKind](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.UnitKind))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`unitKinds[]` |  `object (`[UnitKind](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.UnitKind)`)` The resulting unit kinds.  
`nextPageToken` |  `string` If present, the next page token can be provided to a subsequent ListUnitKinds call to list the next page. If empty, there are no more pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### UnitKind

JSON representation  
---  
      
    
    {
      "name": string,
      "defaultRelease": string,
      "dependencies": [
        {
          object ([Dependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.Dependency))
        }
      ],
      "inputVariableMappings": [
        {
          object ([VariableMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.VariableMapping))
        }
      ],
      "outputVariableMappings": [
        {
          object ([VariableMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.VariableMapping))
        }
      ],
      "defaultFlagRevisions": [
        string
      ],
      "saas": string,
      "applicationTemplateComponent": {
        object ([ComponentRef](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.ComponentRef))
      },
      "appParams": {
        object ([AppParams](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.AppParams))
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
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/unitKinds/{unitKind}"  
`defaultRelease` |  `string` Optional. A reference to the Release object to use as default for creating new units of this UnitKind (optional).If not specified, a new unit must explicitly reference which release to use for its creation.  
`dependencies[]` |  `object (`[Dependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.Dependency)`)` Optional. Immutable. List of other unit kinds that this release will depend on. Dependencies will be automatically provisioned if not found. Maximum 10.  
`inputVariableMappings[]` |  `object (`[VariableMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.VariableMapping)`)` Optional. List of inputVariables for this release that will either be retrieved from a dependency's outputVariables, or will be passed on to a dependency's inputVariables. Maximum 100.  
`outputVariableMappings[]` |  `object (`[VariableMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.VariableMapping)`)` Optional. List of outputVariables for this unit kind will be passed to this unit's outputVariables. Maximum 100.  
`defaultFlagRevisions[]` |  `string` Optional. Default revisions of flags for this UnitKind. Newly created units will use the flag default_flag_revisions present at the time of creation.  
`saas` |  `string` Required. Immutable. A reference to the Saas that defines the product (managed service) that the producer wants to manage with App Lifecycle Manager. Part of the App Lifecycle Manager common data model. Immutable once set.  
`applicationTemplateComponent` |  `object (`[ComponentRef](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.ComponentRef)`)` Output only. Reference to component and revision in a composite ApplicationTemplate.  
`appParams` |  `object (`[AppParams](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.AppParams)`)` AppParams contains the parameters for creating an AppHub Application.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Dependency

JSON representation  
---  
      
    
    {
      "unitKind": string,
      "alias": string
    }  
  
Fields  
---  
`unitKind` |  `string` Required. Immutable. The unit kind of the dependency.  
`alias` |  `string` Required. An alias for the dependency. Used for input variable mapping.  
  
### VariableMapping

JSON representation  
---  
      
    
    {
      "variable": string,
    
      // Union field mapping_type can be only one of the following:
      "from": {
        object ([FromMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.FromMapping))
      },
      "to": {
        object ([ToMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.ToMapping))
      }
      // End of list of possible types for union field mapping_type.
    }  
  
Fields  
---  
`variable` |  `string` Required. name of the variable  
Union field `mapping_type`.`mapping_type` can be only one of the following:  
`from` |  `object (`[FromMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.FromMapping)`)` Optional. Output variables which will get their values from dependencies  
`to` |  `object (`[ToMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.ToMapping)`)` Optional. Input variables whose values will be passed on to dependencies.  
  
### FromMapping

JSON representation  
---  
      
    
    {
      "dependency": string,
      "outputVariable": string
    }  
  
Fields  
---  
`dependency` |  `string` Required. Alias of the dependency that the outputVariable will pass its value to  
`outputVariable` |  `string` Required. Name of the outputVariable on the dependency  
  
### ToMapping

JSON representation  
---  
      
    
    {
      "dependency": string,
      "inputVariable": string,
      "ignoreForLookup": boolean
    }  
  
Fields  
---  
`dependency` |  `string` Required. Alias of the dependency that the inputVariable will pass its value to  
`inputVariable` |  `string` Required. Name of the inputVariable on the dependency  
`ignoreForLookup` |  `boolean` Optional. Tells App Lifecycle Manager if this mapping should be used during lookup or not  
  
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
  
### AppParams

JSON representation  
---  
      
    
    {
      "group": string,
      "scope": {
        object ([Scope](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.Scope))
      }
    }  
  
Fields  
---  
`group` |  `string` Grouping used to construct the name of the AppHub Application. Multiple UnitKinds can specify the same group to use the same Application across their respective units. Corresponds to the app_boundary_id in the ADC composite ApplicationTemplate. Defaults to UnitKind.name  
`scope` |  `object (`[Scope](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds#Output.Schema.Scope)`)` Corresponds to the scope in the ADC composite ApplicationTemplate. Defaults to TYPE_REGIONAL.  
  
### Scope

JSON representation  
---  
      
    
    {
      "type": enum (Type)
    }  
  
Fields  
---  
`type` |  `enum (`Type`)` Required. Scope Type.  
  
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
