---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds
title: REST Resource: projects.locations.unitKinds \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:07:35.204989+00:00
---

# REST Resource: projects.locations.unitKinds  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  REST Resource: projects.locations.unitKinds Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: UnitKind
    * JSON representation
  * Dependency
    * JSON representation
  * VariableMapping
    * JSON representation
  * FromMapping
    * JSON representation
  * ToMapping
    * JSON representation
  * AppParams
    * JSON representation
  * Scope
    * JSON representation
  * Type
  * Methods



## Resource: UnitKind

Definition of a Unit. Units belonging to the same UnitKind are managed together; for example they follow the same release model (blueprints, versions etc.) and are typically rolled out together.

JSON representation  
---  
      
    
    {
      "name": string,
      "defaultRelease": string,
      "dependencies": [
        {
          object ([Dependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#Dependency))
        }
      ],
      "inputVariableMappings": [
        {
          object ([VariableMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#VariableMapping))
        }
      ],
      "outputVariableMappings": [
        {
          object ([VariableMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#VariableMapping))
        }
      ],
      "defaultFlagRevisions": [
        string
      ],
      "saas": string,
      "applicationTemplateComponent": {
        object ([ComponentRef](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/ComponentRef))
      },
      "appParams": {
        object ([AppParams](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#AppParams))
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
`dependencies[]` |  `object (`[Dependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#Dependency)`)` Optional. Immutable. List of other unit kinds that this release will depend on. Dependencies will be automatically provisioned if not found. Maximum 10.  
`inputVariableMappings[]` |  `object (`[VariableMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#VariableMapping)`)` Optional. List of inputVariables for this release that will either be retrieved from a dependency's outputVariables, or will be passed on to a dependency's inputVariables. Maximum 100.  
`outputVariableMappings[]` |  `object (`[VariableMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#VariableMapping)`)` Optional. List of outputVariables for this unit kind will be passed to this unit's outputVariables. Maximum 100.  
`defaultFlagRevisions[]` |  `string` Optional. Default revisions of flags for this UnitKind. Newly created units will use the flag defaultFlagRevisions present at the time of creation.  
`saas` |  `string` Required. Immutable. A reference to the Saas that defines the product (managed service) that the producer wants to manage with App Lifecycle Manager. Part of the App Lifecycle Manager common data model. Immutable once set.  
`applicationTemplateComponent` |  `object (`[ComponentRef](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/ComponentRef)`)` Output only. Reference to component and revision in a composite ApplicationTemplate.  
`appParams` |  `object (`[AppParams](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#AppParams)`)` AppParams contains the parameters for creating an AppHub Application.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Dependency

Dependency represent a single dependency with another unit kind by alias.

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
  
## VariableMapping

Mapping of input variables to their respective output variable for depedenencies

JSON representation  
---  
      
    
    {
      "variable": string,
    
      // Union field mapping_type can be only one of the following:
      "from": {
        object ([FromMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#FromMapping))
      },
      "to": {
        object ([ToMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#ToMapping))
      }
      // End of list of possible types for union field mapping_type.
    }  
  
Fields  
---  
`variable` |  `string` Required. name of the variable  
Union field `mapping_type`.`mapping_type` can be only one of the following:  
`from` |  `object (`[FromMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#FromMapping)`)` Optional. Output variables which will get their values from dependencies  
`to` |  `object (`[ToMapping](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#ToMapping)`)` Optional. Input variables whose values will be passed on to dependencies.  
  
## FromMapping

Output variables whose values will be passed on to dependencies

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
  
## ToMapping

Input variables whose values will be passed on to dependencies

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
  
## AppParams

AppParams contains the parameters for creating an AppHub Application.

JSON representation  
---  
      
    
    {
      "group": string,
      "scope": {
        object ([Scope](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#Scope))
      }
    }  
  
Fields  
---  
`group` |  `string` Grouping used to construct the name of the AppHub Application. Multiple UnitKinds can specify the same group to use the same Application across their respective units. Corresponds to the app_boundary_id in the ADC composite ApplicationTemplate. Defaults to UnitKind.name  
`scope` |  `object (`[Scope](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#Scope)`)` Corresponds to the scope in the ADC composite ApplicationTemplate. Defaults to REGIONAL.  
  
## Scope

Scope of an application.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#Type))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#Type)`)` Required. Scope Type.  
  
## Type

Scope Type.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`REGIONAL` | Deprecated: Use TYPE_REGIONAL.This item is deprecated!  
`GLOBAL` | Deprecated: Use TYPE_GLOBAL.This item is deprecated!  
`TYPE_REGIONAL` | Regional type.  
`TYPE_GLOBAL` | Global type.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds/create)`

|  Create a new unit kind.  
  
### `[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds/delete)`

|  Delete a single unit kind.  
  
### `[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds/get)`

|  Retrieve a single unit kind.  
  
### `[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds/list)`

|  Retrieve a collection of unit kinds.  
  
### `[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds/patch)`

|  Update a single unit kind.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
