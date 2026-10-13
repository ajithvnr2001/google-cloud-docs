---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes
title: REST Resource: projects.locations.scopes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:10.256090+00:00
---

# REST Resource: projects.locations.scopes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  REST Resource: projects.locations.scopes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Scope
    * JSON representation
  * ScopeLifecycleState
    * JSON representation
  * ScopeLifecycleState.Code
  * Methods



## Resource: Scope

Scope represents a Scope in a Fleet.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "state": {
        object ([ScopeLifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes#ScopeLifecycleState))
      },
      "namespaceLabels": {
        string: string,
        ...
      },
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` The resource name for the scope `projects/{project}/locations/{location}/scopes/{scope}`  
`uid` |  `string` Output only. Google-generated UUID for this resource. This is unique across all scope resources. If a scope resource is deleted and another resource with the same name is created, it gets a different uid.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the scope was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the scope was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the scope was deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `object (`[ScopeLifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes#ScopeLifecycleState)`)` Output only. State of the scope resource.  
`namespaceLabels` |  `map (key: string, value: string)` Optional. Scope-level cluster namespace labels. For the member clusters bound to the Scope, these labels are applied to each namespace under the Scope. Scope-level labels take precedence over Namespace-level labels (`namespaceLabels` in the Fleet Namespace resource) if they share a key. Keys and values must be Kubernetes-conformant.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Optional. Labels for this Scope.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## ScopeLifecycleState

ScopeLifecycleState describes the state of a Scope resource.

JSON representation  
---  
      
    
    {
      "code": enum ([ScopeLifecycleState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes#ScopeLifecycleState.Code))
    }  
  
Fields  
---  
`code` |  `enum (`[ScopeLifecycleState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes#ScopeLifecycleState.Code)`)` Output only. The current state of the scope resource.  
  
## ScopeLifecycleState.Code

Code describes the state of a Scope resource.

Enums  
---  
`CODE_UNSPECIFIED` | The code is not set.  
`CREATING` | The scope is being created.  
`READY` | The scope active.  
`DELETING` | The scope is being deleted.  
`UPDATING` | The scope is being updated.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/create)`

|  Creates a Scope.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/delete)`

|  Deletes a Scope.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/get)`

|  Returns the details of a Scope.  
  
### `[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/list)`

|  Lists Scopes.  
  
### `[listMemberships](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/listMemberships)`

|  Lists Memberships bound to a Scope.  
  
### `[listPermitted](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/listPermitted)`

|  Lists permitted Scopes.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/patch)`

|  Updates a scopes.  
  
### `[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
