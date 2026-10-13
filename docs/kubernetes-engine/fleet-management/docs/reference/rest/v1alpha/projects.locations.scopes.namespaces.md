---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces
title: REST Resource: projects.locations.scopes.namespaces \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:12.273339+00:00
---

# REST Resource: projects.locations.scopes.namespaces  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  REST Resource: projects.locations.scopes.namespaces Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Namespace
    * JSON representation
  * NamespaceLifecycleState
    * JSON representation
  * NamespaceLifecycleState.Code
  * Methods



## Resource: Namespace

Namespace represents a namespace across the Fleet

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "state": {
        object ([NamespaceLifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces#NamespaceLifecycleState))
      },
      "scope": string,
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
`name` |  `string` The resource name for the namespace `projects/{project}/locations/{location}/namespaces/{namespace}`  
`uid` |  `string` Output only. Google-generated UUID for this resource. This is unique across all namespace resources. If a namespace resource is deleted and another resource with the same name is created, it gets a different uid.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the namespace was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the namespace was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the namespace was deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `object (`[NamespaceLifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces#NamespaceLifecycleState)`)` Output only. State of the namespace resource.  
`scope` |  `string` Required. Scope associated with the namespace  
`namespaceLabels` |  `map (key: string, value: string)` Optional. Namespace-level cluster namespace labels. These labels are applied to the related namespace of the member clusters bound to the parent Scope. Scope-level labels (`namespaceLabels` in the Fleet Scope resource) take precedence over Namespace-level labels if they share a key. Keys and values must be Kubernetes-conformant.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Optional. Labels for this Namespace.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## NamespaceLifecycleState

NamespaceLifecycleState describes the state of a Namespace resource.

JSON representation  
---  
      
    
    {
      "code": enum ([NamespaceLifecycleState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces#NamespaceLifecycleState.Code))
    }  
  
Fields  
---  
`code` |  `enum (`[NamespaceLifecycleState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces#NamespaceLifecycleState.Code)`)` Output only. The current state of the Namespace resource.  
  
## NamespaceLifecycleState.Code

Code describes the state of a Namespace resource.

Enums  
---  
`CODE_UNSPECIFIED` | The code is not set.  
`CREATING` | The namespace is being created.  
`READY` | The namespace active.  
`DELETING` | The namespace is being deleted.  
`UPDATING` | The namespace is being updated.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces/create)`

|  Creates a fleet namespace.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces/delete)`

|  Deletes a fleet namespace.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces/get)`

|  Returns the details of a fleet namespace.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces/list)`

|  Lists fleet namespaces.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces/patch)`

|  Updates a fleet namespace.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
