---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units
title: REST Resource: projects.locations.units \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:00.044055+00:00
---

# REST Resource: projects.locations.units  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  REST Resource: projects.locations.units Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Unit
    * JSON representation
  * UnitDependency
    * JSON representation
  * MaintenanceSettings
    * JSON representation
  * UnitState
  * UnitCondition
    * JSON representation
  * Status
  * Type
  * ManagementMode
  * SystemManagedState
  * Methods



## Resource: Unit

A unit of deployment that has its lifecycle via a CRUD API using an actuation engine under the hood (e.g. based on Terraform, Helm or a custom implementation provided by a service producer). A building block of a SaaS Tenant.

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
          object ([UnitDependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#UnitDependency))
        }
      ],
      "dependencies": [
        {
          object ([UnitDependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#UnitDependency))
        }
      ],
      "inputVariables": [
        {
          object ([UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/UnitVariable))
        }
      ],
      "outputVariables": [
        {
          object ([UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/UnitVariable))
        }
      ],
      "maintenance": {
        object ([MaintenanceSettings](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#MaintenanceSettings))
      },
      "state": enum ([UnitState](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#UnitState)),
      "conditions": [
        {
          object ([UnitCondition](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#UnitCondition))
        }
      ],
      "managementMode": enum ([ManagementMode](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#ManagementMode)),
      "systemManagedState": enum ([SystemManagedState](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#SystemManagedState)),
      "systemCleanupAt": string,
      "flagRevisions": [
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
`dependents[]` |  `object (`[UnitDependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#UnitDependency)`)` Optional. Output only. List of Units that depend on this unit. Unit can only be deprovisioned if this list is empty. Maximum 1000.  
`dependencies[]` |  `object (`[UnitDependency](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#UnitDependency)`)` Optional. Output only. Set of dependencies for this unit. Maximum 10.  
`inputVariables[]` |  `object (`[UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/UnitVariable)`)` Optional. Output only. Indicates the current input variables deployed by the unit  
`outputVariables[]` |  `object (`[UnitVariable](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/UnitVariable)`)` Optional. Output only. Set of key/value pairs corresponding to output variables from execution of actuation templates. The variables are declared in actuation configs (e.g in helm chart or terraform) and the values are fetched and returned by the actuation engine upon completion of execution.  
`maintenance` |  `object (`[MaintenanceSettings](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#MaintenanceSettings)`)` Optional. Captures requested directives for performing future maintenance on the unit. This includes a request for the unit to skip maintenance for a period of time and remain pinned to its current release as well as controls for postponing maintenance scheduled in future.  
`state` |  `enum (`[UnitState](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#UnitState)`)` Optional. Output only. Current lifecycle state of the resource (e.g. if it's being created or ready to use).  
`conditions[]` |  `object (`[UnitCondition](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#UnitCondition)`)` Optional. Output only. A set of conditions which indicate the various conditions this resource can have.  
`managementMode` |  `enum (`[ManagementMode](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#ManagementMode)`)` Optional. Immutable. Indicates whether the Unit life cycle is controlled by the user or by the system. Immutable once created.  
`systemManagedState` |  `enum (`[SystemManagedState](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#SystemManagedState)`)` Optional. Output only. Indicates the system managed state of the unit.  
`systemCleanupAt` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. If set, indicates the time when the system will start removing the unit.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`flagRevisions[]` |  `string` Optional. Output only. Flag revisions used by this Unit.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`satisfiesPzs` |  `boolean` Reserved for future use.  
`satisfiesPzi` |  `boolean` Reserved for future use.  
  
## UnitDependency

Set of dependencies for this unit. Maximum 10.

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
  
## MaintenanceSettings

Captures requested directives for performing future maintenance on the unit. This includes a request for the unit to skip maintenance for a period of time and remain pinned to its current release as well as controls for postponing maintenance scheduled in future.

JSON representation  
---  
      
    
    {
      "pinnedUntilTime": string
    }  
  
Fields  
---  
`pinnedUntilTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. If present, it fixes the release on the unit until the given time; i.e. changes to the release field will be rejected. Rollouts should and will also respect this by not requesting an upgrade in the first place.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## UnitState

UnitState annotates what is the current state of the unit itself.

Enums  
---  
`UNIT_STATE_UNSPECIFIED` | Unspecified state.  
`UNIT_STATE_NOT_PROVISIONED` | Unit is not provisioned.  
`UNIT_STATE_PROVISIONING` | Unit is being provisioned.  
`UNIT_STATE_UPDATING` | Unit is being updated. This is typically when a unit is being upgraded to a new release or some of the input variables on the Unit is being changed. Certain kinds of updates may cause the Unit to become unusable while the update is in progress.  
`UNIT_STATE_DEPROVISIONING` | Unit is being deleted.  
`UNIT_STATE_READY` | Unit has been provisioned and is ready for use  
`UNIT_STATE_ERROR` | Unit has error, when it is not ready and some error operation  
  
## UnitCondition

UnitCondition describes the status of an Unit. UnitCondition is individual components that contribute to an overall state.

JSON representation  
---  
      
    
    {
      "status": enum ([Status](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#Status)),
      "type": enum ([Type](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#Type)),
      "lastTransitionTime": string,
      "message": string,
      "reason": string
    }  
  
Fields  
---  
`status` |  `enum (`[Status](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#Status)`)` Required. Status of the condition.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units#Type)`)` Required. Type of the condition.  
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
`TYPE_READY` | Condition type is ready.  
`TYPE_UPDATING` | Condition type is updating.  
`TYPE_PROVISIONED` | Condition type is provisioned.  
`TYPE_OPERATION_ERROR` | Condition type is operationError. True when the last unit operation fails with a non-ignorable error.  
  
## ManagementMode

ManagementMode describes who is responsible for the management of the unit.

Enums  
---  
`MANAGEMENT_MODE_UNSPECIFIED` |   
`MANAGEMENT_MODE_USER` | Unit's lifecycle is managed by the user.  
`MANAGEMENT_MODE_SYSTEM` | The system will decide when to deprovision and delete the unit. User still can deprovision or delete the unit manually.  
  
## SystemManagedState

Enums  
---  
`SYSTEM_MANAGED_STATE_UNSPECIFIED` |   
`SYSTEM_MANAGED_STATE_ACTIVE` | Unit has dependents attached.  
`SYSTEM_MANAGED_STATE_INACTIVE` | Unit has no dependencies attached, but attachment is allowed.  
`SYSTEM_MANAGED_STATE_DECOMMISSIONED` | Unit has no dependencies attached, and attachment is not allowed.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units/create)`

|  Create a new unit.  
  
### `[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units/delete)`

|  Delete a single unit.  
  
### `[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units/get)`

|  Retrieve a single unit.  
  
### `[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units/list)`

|  Retrieve a collection of units.  
  
### `[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units/patch)`

|  Update a single unit.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
