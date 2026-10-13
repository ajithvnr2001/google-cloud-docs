---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings
title: REST Resource: projects.locations.policyBindings \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:26.929080+00:00
---

# REST Resource: projects.locations.policyBindings  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: projects.locations.policyBindings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PolicyBinding
    * JSON representation
  * Methods



## Resource: PolicyBinding

IAM policy binding resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "etag": string,
      "displayName": string,
      "annotations": {
        string: string,
        ...
      },
      "target": {
        object ([Target](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings#PolicyBinding.Target))
      },
      "policyKind": enum ([PolicyKind](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings#PolicyBinding.PolicyKind)),
      "policy": string,
      "policyUid": string,
      "condition": {
        object ([Expr](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Expr))
      },
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the policy binding, in the format `{binding_parent/locations/{location}/policyBindings/{policyBindingId}`. The binding parent is the closest Resource Manager resource (project, folder, or organization) to the binding target.Format:

  * `projects/{projectId}/locations/{location}/policyBindings/{policyBindingId}`
  * `projects/{projectNumber}/locations/{location}/policyBindings/{policyBindingId}`
  * `folders/{folderId}/locations/{location}/policyBindings/{policyBindingId}`
  * `organizations/{organizationId}/locations/{location}/policyBindings/{policyBindingId}`

  
`uid` |  `string` Output only. The globally unique ID of the policy binding. Assigned when the policy binding is created.  
`etag` |  `string` Optional. The etag for the policy binding. If this is provided on update, it must match the server's etag.  
`displayName` |  `string` Optional. The description of the policy binding. Must be less than or equal to 63 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User-defined annotations. See <https://google.aip.dev/148#annotations> for more details such as format and size limitationsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`target` |  `object (`[Target](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings#PolicyBinding.Target)`)` Required. Immutable. The full resource name of the resource to which the policy will be bound. Immutable once set.  
`policyKind` |  `enum (`[PolicyKind](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings#PolicyBinding.PolicyKind)`)` Immutable. The kind of the policy to attach in this binding. This field must be one of the following:

  * Left empty (will be automatically set to the policy kind)
  * The input policy kind

  
`policy` |  `string` Required. Immutable. The resource name of the policy to be bound. The binding parent and policy must belong to the same organization.  
`policyUid` |  `string` Output only. The globally unique ID of the policy to be bound.  
`condition` |  `object (`[Expr](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Expr)`)` Optional. The condition to apply to the policy binding. When set, the `expression` field in the `Expr` must include from 1 to 10 subexpressions, joined by the "||"(Logical OR), "&&"(Logical AND) or "!"(Logical NOT) operators and cannot contain more than 250 characters.The condition is currently only supported when bound to policies of kind principal access boundary.When the bound policy is a principal access boundary policy, the only supported attributes in any subexpression are `principal.type` and `principal.subject`. An example expression is: "principal.type == 'iam.googleapis.com/ServiceAccount'" or "principal.subject == 'bob@example.com'".Allowed operations for `principal.subject`:

  * `principal.subject == <principal subject string>`
  * `principal.subject != <principal subject string>`
  * `principal.subject in [<list of principal subjects>]`
  * `principal.subject.startsWith(<string>)`
  * `principal.subject.endsWith(<string>)`

Allowed operations for `principal.type`:

  * `principal.type == <principal type string>`
  * `principal.type != <principal type string>`
  * `principal.type in [<list of principal types>]`

Supported principal types are workspace, workforce pool, workload pool, service account, and agent identity. Allowed string must be one of:

  * `iam.googleapis.com/WorkspaceIdentity`
  * `iam.googleapis.com/WorkforcePoolIdentity`
  * `iam.googleapis.com/WorkloadPoolIdentity`
  * `iam.googleapis.com/ServiceAccount`
  * `iam.googleapis.com/AgentPoolIdentity`

  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy binding was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy binding was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/create)`

|  Creates a policy binding and returns a long-running operation.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/delete)`

|  Deletes a policy binding and returns a long-running operation.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/get)`

|  Gets a policy binding.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/list)`

|  Lists policy bindings.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/patch)`

|  Updates a policy binding and returns a long-running operation.  
  
### `[searchTargetPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/searchTargetPolicyBindings)`

|  Search policy bindings by target.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-30 UTC."],[],[]] 
