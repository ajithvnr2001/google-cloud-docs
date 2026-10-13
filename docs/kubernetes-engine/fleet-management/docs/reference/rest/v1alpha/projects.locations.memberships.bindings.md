---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings
title: REST Resource: projects.locations.memberships.bindings \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:07.573254+00:00
---

# REST Resource: projects.locations.memberships.bindings  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  REST Resource: projects.locations.memberships.bindings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MembershipBinding
    * JSON representation
  * MembershipBindingLifecycleState
    * JSON representation
  * MembershipBindingLifecycleState.Code
  * Methods



## Resource: MembershipBinding

MembershipBinding is a subresource of a Membership, representing what Fleet Scopes (or other, future Fleet resources) a Membership is bound to.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "state": {
        object ([MembershipBindingLifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings#MembershipBindingLifecycleState))
      },
      "labels": {
        string: string,
        ...
      },
    
      // Union field target can be only one of the following:
      "scope": string
      // End of list of possible types for union field target.
    }  
  
Fields  
---  
`name` |  `string` The resource name for the membershipbinding itself `projects/{project}/locations/{location}/memberships/{membership}/bindings/{membershipbinding}`  
`uid` |  `string` Output only. Google-generated UUID for this resource. This is unique across all membershipbinding resources. If a membershipbinding resource is deleted and another resource with the same name is created, it gets a different uid.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the membership binding was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the membership binding was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the membership binding was deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `object (`[MembershipBindingLifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings#MembershipBindingLifecycleState)`)` Output only. State of the membership binding resource.  
`labels` |  `map (key: string, value: string)` Optional. Labels for this MembershipBinding.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `target`. What type of membershipbinding this is. `target` can be only one of the following:  
`scope` |  `string` A Scope resource name in the format `projects/*/locations/*/scopes/*`.  
  
## MembershipBindingLifecycleState

MembershipBindingLifecycleState describes the state of a Binding resource.

JSON representation  
---  
      
    
    {
      "code": enum ([MembershipBindingLifecycleState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings#MembershipBindingLifecycleState.Code))
    }  
  
Fields  
---  
`code` |  `enum (`[MembershipBindingLifecycleState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings#MembershipBindingLifecycleState.Code)`)` Output only. The current state of the MembershipBinding resource.  
  
## MembershipBindingLifecycleState.Code

Code describes the state of a MembershipBinding resource.

Enums  
---  
`CODE_UNSPECIFIED` | The code is not set.  
`CREATING` | The membershipbinding is being created.  
`READY` | The membershipbinding active.  
`DELETING` | The membershipbinding is being deleted.  
`UPDATING` | The membershipbinding is being updated.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings/create)`

|  Creates a MembershipBinding.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings/delete)`

|  Deletes a MembershipBinding.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings/get)`

|  Returns the details of a MembershipBinding.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings/list)`

|  Lists MembershipBindings.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings/patch)`

|  Updates a MembershipBinding.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
