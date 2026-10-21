---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations
title: REST Resource: projects.locations.unitOperations \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:42:59.116801+00:00
---

# REST Resource: projects.locations.unitOperations  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  REST Resource: projects.locations.unitOperations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: UnitOperation
    * JSON representation
  * Provision
    * JSON representation
  * Upgrade
    * JSON representation
  * Deprovision
  * FlagUpdate
    * JSON representation
  * UnitOperationState
  * UnitOperationCondition
    * JSON representation
  * Status
  * Type
  * Schedule
    * JSON representation
  * UnitOperationErrorCategory
  * Methods



## Resource: UnitOperation

UnitOperation encapsulates the intent of changing/interacting with the service component represented by the specific Unit. Multiple UnitOperations can be created (requested) and scheduled in the future, however only one will be allowed to execute at a time (that can change in the future for non-mutating operations).

UnitOperations allow different actors interacting with the same unit to focus only on the change they have requested.

This is a base object that contains the common fields in all unit operations. Next: 22

JSON representation  
---  
      
    
    {
      "name": string,
      "unit": string,
      "parentUnitOperation": string,
      "rollout": string,
      "cancel": boolean,
      "state": enum ([UnitOperationState](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#UnitOperationState)),
      "conditions": [
        {
          object ([UnitOperationCondition](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#UnitOperationCondition))
        }
      ],
      "schedule": {
        object ([Schedule](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Schedule))
      },
      "engineState": string,
      "errorCategory": enum ([UnitOperationErrorCategory](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#UnitOperationErrorCategory)),
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
      "deleteTime": string,
    
      // Union field unit_operation_type can be only one of the following:
      "provision": {
        object ([Provision](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Provision))
      },
      "upgrade": {
        object ([Upgrade](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Upgrade))
      },
      "deprovision": {
        object ([Deprovision](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Deprovision))
      },
      "flagUpdate": {
        object ([FlagUpdate](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#FlagUpdate))
      }
      // End of list of possible types for union field unit_operation_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/unitOperations/{unitOperation}"  
`unit` |  `string` Required. Immutable. The Unit a given UnitOperation will act upon.  
`parentUnitOperation` |  `string` Optional. Reference to parent resource: UnitOperation. If an operation needs to create other operations as part of its workflow, each of the child operations should have this field set to the parent. This can be used for tracing. (Optional)  
`rollout` |  `string` Optional. Specifies which rollout created this Unit Operation. This cannot be modified and is used for filtering purposes only. If a dependent unit and unit operation are created as part of another unit operation, they will use the same rolloutId.  
`cancel` |  `boolean` Optional. When true, attempt to cancel the operation. Cancellation may fail if the operation is already executing. (Optional)  
`state` |  `enum (`[UnitOperationState](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#UnitOperationState)`)` Optional. Output only. UnitOperationState describes the current state of the unit operation.  
`conditions[]` |  `object (`[UnitOperationCondition](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#UnitOperationCondition)`)` Optional. Output only. A set of conditions which indicate the various conditions this resource can have.  
`schedule` |  `object (`[Schedule](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Schedule)`)` Optional. When to schedule this operation.  
`engineState` |  `string` Optional. Output only. The engine state for on-going deployment engine operation(s). This field is opaque for external usage.  
`errorCategory` |  `enum (`[UnitOperationErrorCategory](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#UnitOperationErrorCategory)`)` Optional. Output only. UnitOperationErrorCategory describe the error category.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was marked for deletion (deletion is an asynchronous operation).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `unit_operation_type`.`unit_operation_type` can be only one of the following:  
`provision` |  `object (`[Provision](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Provision)`)`  
`upgrade` |  `object (`[Upgrade](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Upgrade)`)`  
`deprovision` |  `object (`[Deprovision](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Deprovision)`)`  
`flagUpdate` |  `object (`[FlagUpdate](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#FlagUpdate)`)`  
  
## Provision

Provision is the unit operation that provision the underlying resources represented by a Unit. Can only execute if the Unit is not currently provisioned.

JSON representation  
---  
      
    
    {
      "release": string,
      "inputVariables": [
        {
          object ([UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/UnitVariable))
        }
      ]
    }  
  
Fields  
---  
`release` |  `string` Optional. Reference to the Release object to use for the Unit. (optional).  
`inputVariables[]` |  `object (`[UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/UnitVariable)`)` Optional. Set of input variables. Maximum 100. (optional)  
  
## Upgrade

Upgrade is the unit operation that upgrades a provisioned unit, which may also include the underlying resources represented by a Unit. Can only execute if the Unit is currently provisioned.

JSON representation  
---  
      
    
    {
      "release": string,
      "inputVariables": [
        {
          object ([UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/UnitVariable))
        }
      ]
    }  
  
Fields  
---  
`release` |  `string` Optional. Reference to the Release object to use for the Unit. (optional).  
`inputVariables[]` |  `object (`[UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/UnitVariable)`)` Optional. Set of input variables. Maximum 100. (optional)  
  
## Deprovision

This type has no fields.

Deprovision is the unit operation that deprovision the underlying resources represented by a Unit. Can only execute if the Unit is currently provisioned.

## FlagUpdate

FlagUpdate is a UnitOperation that pushes new flag values to Units.

JSON representation  
---  
      
    
    {
      "flagRelease": string
    }  
  
Fields  
---  
`flagRelease` |  `string` Required. Flag release being applied by UnitOperation.  
  
## UnitOperationState

UnitOperationState describes the current state of the unit operation.

Enums  
---  
`UNIT_OPERATION_STATE_UNKNOWN` |   
`UNIT_OPERATION_STATE_PENDING` | Unit operation is accepted but not ready to run.  
`UNIT_OPERATION_STATE_SCHEDULED` | Unit operation is accepted and scheduled.  
`UNIT_OPERATION_STATE_RUNNING` | Unit operation is running.  
`UNIT_OPERATION_STATE_SUCCEEDED` | Unit operation has completed successfully.  
`UNIT_OPERATION_STATE_FAILED` | Unit operation has failed.  
`UNIT_OPERATION_STATE_CANCELLED` | Unit operation was cancelled.  
  
## UnitOperationCondition

UnitOperationCondition describes the status of an Unit Operation. UnitOperationCondition is individual components that contribute to an overall state.

JSON representation  
---  
      
    
    {
      "status": enum ([Status](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Status)),
      "type": enum ([Type](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Type)),
      "lastTransitionTime": string,
      "message": string,
      "reason": string
    }  
  
Fields  
---  
`status` |  `enum (`[Status](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Status)`)` Required. Status of the condition.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations#Type)`)` Required. Type of the condition.  
`lastTransitionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Last time the condition transited from one status to another.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`message` |  `string` Required. Human readable message indicating details about the last transition.  
`reason` |  `string` Required. Brief reason for the condition's last transition.  
  
## Status

Enumeration of condition statuses.

Enums  
---  
`STATUS_UNSPECIFIED` | Condition status is unspecified.  
`STATUS_UNKNOWN` | Condition is unknown.  
`STATUS_TRUE` | Condition is true.  
`STATUS_FALSE` | Condition is false.  
  
## Type

Enumeration of condition types.

Enums  
---  
`TYPE_UNSPECIFIED` | Condition type is unspecified.  
`TYPE_SCHEDULED` | Condition type is scheduled.  
`TYPE_RUNNING` | Condition type is running.  
`TYPE_SUCCEEDED` | Condition type is succeeded.  
`TYPE_CANCELLED` | Condition type is cancelled.  
`TYPE_APP_CREATED` | Indicates if AppHub app has been created.  
`TYPE_APP_COMPONENTS_REGISTERED` | Indicates if services and workloads have been registered with AppHub.  
  
## Schedule

A time specification to schedule the maintenance.

JSON representation  
---  
      
    
    {
      "startTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Start of operation. If not set, will be set to the start of the next window. (optional)Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## UnitOperationErrorCategory

UnitOperationErrorCategory describes the error category of the unit operation.

Enums  
---  
`UNIT_OPERATION_ERROR_CATEGORY_UNSPECIFIED` | Unit operation error category is unspecified  
`NOT_APPLICABLE` | Unit operation error category is not applicable, or it is not an error  
`FATAL` | Unit operation error category is fatal  
`RETRIABLE` | Unit operation error category is retriable  
`IGNORABLE` | Unit operation error category is ignorable  
`STANDARD` | Unit operation error category is standard, counts towards Rollout error budget  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations/create)`

|  Create a new unit operation.  
  
### `[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations/delete)`

|  Delete a single unit operation.  
  
### `[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations/get)`

|  Retrieve a single unit operation.  
  
### `[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations/list)`

|  Retrieve a collection of unit operations.  
  
### `[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations/patch)`

|  Update a single unit operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
