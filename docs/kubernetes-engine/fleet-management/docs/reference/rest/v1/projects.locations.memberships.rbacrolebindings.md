---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings
title: REST Resource: projects.locations.memberships.rbacrolebindings \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:59.026249+00:00
---

# REST Resource: projects.locations.memberships.rbacrolebindings  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  REST Resource: projects.locations.memberships.rbacrolebindings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: RBACRoleBinding
    * JSON representation
    * RBACRoleBindingLifecycleState
      * JSON representation
    * RBACRoleBindingLifecycleState.Code
    * RBACRoleBinding.Role
      * JSON representation
    * RBACRoleBinding.Role.PredefinedRoles
  * Methods



## Resource: RBACRoleBinding

RBACRoleBinding represents a rbacrolebinding across the Fleet

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "state": {
        object ([RBACRoleBindingLifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings#RBACRoleBinding.RBACRoleBindingLifecycleState))
      },
      "role": {
        object ([RBACRoleBinding.Role](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings#RBACRoleBinding.RBACRoleBinding.Role))
      },
      "labels": {
        string: string,
        ...
      },
    
      // Union field principal can be only one of the following:
      "user": string,
      "group": string
      // End of list of possible types for union field principal.
    }  
  
Fields  
---  
`name` |  `string` The resource name for the rbacrolebinding `projects/{project}/locations/{location}/scopes/{scope}/rbacrolebindings/{rbacrolebinding}` or `projects/{project}/locations/{location}/memberships/{membership}/rbacrolebindings/{rbacrolebinding}`  
`uid` |  `string` Output only. Google-generated UUID for this resource. This is unique across all rbacrolebinding resources. If a rbacrolebinding resource is deleted and another resource with the same name is created, it gets a different uid.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the rbacrolebinding was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the rbacrolebinding was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the rbacrolebinding was deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `object (`[RBACRoleBindingLifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings#RBACRoleBinding.RBACRoleBindingLifecycleState)`)` Output only. State of the rbacrolebinding resource.  
`role` |  `object (`[RBACRoleBinding.Role](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings#RBACRoleBinding.RBACRoleBinding.Role)`)` Required. Role to bind to the principal  
`labels` |  `map (key: string, value: string)` Optional. Labels for this RBACRolebinding.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `principal`. Principal that is be authorized in the cluster (at least of one the oneof is required). Updating one will unset the other automatically. `principal` can be only one of the following:  
`user` |  `string` user is the name of the user as seen by the kubernetes cluster, example "alice" or "alice@domain.tld"  
`group` |  `string` group is the group, as seen by the kubernetes cluster.  
  
### RBACRoleBindingLifecycleState

RBACRoleBindingLifecycleState describes the state of a RbacRoleBinding resource.

JSON representation  
---  
      
    
    {
      "code": enum ([RBACRoleBindingLifecycleState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings#RBACRoleBinding.RBACRoleBindingLifecycleState.Code))
    }  
  
Fields  
---  
`code` |  `enum (`[RBACRoleBindingLifecycleState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings#RBACRoleBinding.RBACRoleBindingLifecycleState.Code)`)` Output only. The current state of the rbacrolebinding resource.  
  
### RBACRoleBindingLifecycleState.Code

Code describes the state of a rbacrolebinding resource.

Enums  
---  
`CODE_UNSPECIFIED` | The code is not set.  
`CREATING` | The rbacrolebinding is being created.  
`READY` | The rbacrolebinding active.  
`DELETING` | The rbacrolebinding is being deleted.  
`UPDATING` | The rbacrolebinding is being updated.  
  
### RBACRoleBinding.Role

Role is the type for Kubernetes roles

JSON representation  
---  
      
    
    {
      "predefinedRole": enum ([RBACRoleBinding.Role.PredefinedRoles](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings#RBACRoleBinding.RBACRoleBinding.Role.PredefinedRoles)),
      "customRole": string
    }  
  
Fields  
---  
`predefinedRole` |  `enum (`[RBACRoleBinding.Role.PredefinedRoles](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings#RBACRoleBinding.RBACRoleBinding.Role.PredefinedRoles)`)` predefinedRole is the Kubernetes default role to use  
`customRole` |  `string` Optional. customRole is the name of a custom KubernetesClusterRole to use.  
  
### RBACRoleBinding.Role.PredefinedRoles

PredefinedRoles is an ENUM representation of the default Kubernetes Roles

Enums  
---  
`UNKNOWN` | UNKNOWN  
`ADMIN` | ADMIN has EDIT and RBAC permissions  
`EDIT` | EDIT can edit all resources except RBAC  
`VIEW` | VIEW can only read resources  
`ANTHOS_SUPPORT` | ANTHOS_SUPPORT gives Google Support read-only access to a number of cluster resources.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/create)`

|  Creates a Membership RBACRoleBinding.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/delete)`

|  Deletes a Membership RBACRoleBinding.  
  
### `[generateMembershipRBACRoleBindingYAML](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/generateMembershipRBACRoleBindingYAML)`

|  Generates a YAML of the RBAC policies for the specified RoleBinding and its associated impersonation resources.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/get)`

|  Returns the details of a Membership RBACRoleBinding.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/list)`

|  Lists all Membership RBACRoleBindings.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/patch)`

|  Updates a Membership RBACRoleBinding.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
