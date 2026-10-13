---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies
title: REST Resource: folders.locations.accessPolicies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:28.601852+00:00
---

# REST Resource: folders.locations.accessPolicies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: folders.locations.accessPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AccessPolicy
    * JSON representation
    * AccessPolicyDetails
      * JSON representation
    * AccessPolicyRule
      * JSON representation
    * Effect
    * Operation
      * JSON representation
  * Methods



## Resource: AccessPolicy

An IAM access policy resource.

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
      "createTime": string,
      "updateTime": string,
      "details": {
        object ([AccessPolicyDetails](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies#AccessPolicy.AccessPolicyDetails))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the access policy.The following formats are supported:

  * `projects/{projectId}/locations/{location}/accessPolicies/{policyId}`
  * `projects/{projectNumber}/locations/{location}/accessPolicies/{policyId}`
  * `folders/{folderId}/locations/{location}/accessPolicies/{policyId}`
  * `organizations/{organizationId}/locations/{location}/accessPolicies/{policyId}`

  
`uid` |  `string` Output only. The globally unique ID of the access policy.  
`etag` |  `string` Optional. The etag for the access policy. If this is provided on update, it must match the server's etag.  
`displayName` |  `string` Optional. The description of the access policy. Must be less than or equal to 63 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User defined annotations. See <https://google.aip.dev/148#annotations> for more details such as format and size limitationsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the access policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the access policy was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`details` |  `object (`[AccessPolicyDetails](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies#AccessPolicy.AccessPolicyDetails)`)` Optional. The details for the access policy.  
  
### AccessPolicyDetails

Access policy details.

JSON representation  
---  
      
    
    {
      "rules": [
        {
          object ([AccessPolicyRule](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies#AccessPolicy.AccessPolicyRule))
        }
      ]
    }  
  
Fields  
---  
`rules[]` |  `object (`[AccessPolicyRule](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies#AccessPolicy.AccessPolicyRule)`)` Required. A list of access policy rules.  
  
### AccessPolicyRule

Access Policy Rule that determines the behavior of the policy.

JSON representation  
---  
      
    
    {
      "principals": [
        string
      ],
      "excludedPrincipals": [
        string
      ],
      "operation": {
        object ([Operation](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies#AccessPolicy.Operation))
      },
      "conditions": {
        string: {
          object ([Expr](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Expr))
        },
        ...
      },
      "description": string,
      "effect": enum ([Effect](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies#AccessPolicy.Effect))
    }  
  
Fields  
---  
`principals[]` |  `string` Required. The identities for which this rule's effect governs using one or more permissions on Google Cloud resources. This field can contain the following values:

  * `principal://goog/subject/{email_id}`: A specific Google Account. Includes Gmail, Cloud Identity, and Google Workspace user accounts. For example, `principal://goog/subject/alice@example.com`.
  * `principal://iam.googleapis.com/projects/-/serviceAccounts/{service_account_id}`: A Google Cloud service account. For example, `principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@iam.gserviceaccount.com`.
  * `principalSet://goog/group/{groupId}`: A Google group. For example, `principalSet://goog/group/admins@example.com`.
  * `principalSet://goog/cloudIdentityCustomerId/{customerId}`: All of the principals associated with the specified Google Workspace or Cloud Identity customer ID. For example, `principalSet://goog/cloudIdentityCustomerId/C01Abc35`.

If an identifier that was previously set on a policy is soft deleted, then calls to read that policy will return the identifier with a deleted prefix. Users cannot set identifiers with this syntax.

  * `deleted:principal://goog/subject/{email_id}?uid={uid}`: A specific Google Account that was deleted recently. For example, `deleted:principal://goog/subject/alice@example.com?uid=1234567890`. If the Google Account is recovered, this identifier reverts to the standard identifier for a Google Account.
  * `deleted:principalSet://goog/group/{groupId}?uid={uid}`: A Google group that was deleted recently. For example, `deleted:principalSet://goog/group/admins@example.com?uid=1234567890`. If the Google group is restored, this identifier reverts to the standard identifier for a Google group.
  * `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/{service_account_id}?uid={uid}`: A Google Cloud service account that was deleted recently. For example, `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@iam.gserviceaccount.com?uid=1234567890`. If the service account is undeleted, this identifier reverts to the standard identifier for a service account.

  
`excludedPrincipals[]` |  `string` Optional. The identities that are excluded from the access policy rule, even if they are listed in the `principals`. For example, you could add a Google group to the `principals`, then exclude specific users who belong to that group.  
`operation` |  `object (`[Operation](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies#AccessPolicy.Operation)`)` Required. Attributes that are used to determine whether this rule applies to a request.  
`conditions` |  `map (key: string, value: object (`[Expr](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Expr)`))` Optional. The conditions that determine whether this rule applies to a request. Conditions are identified by their key, which is the FQDN of the service that they are relevant to. For example:
    
    
    "conditions": {
     "iam.googleapis.com": <cel expression>
    }
    

Each rule is evaluated independently. If this rule does not apply to a request, other rules might still apply. Currently supported keys are as follows:

  * `eventarc.googleapis.com`: Can use `CEL` functions that evaluate resource fields.
  * `iam.googleapis.com`: Can use `CEL` functions that evaluate [resource tags](https://cloud.google.com/iam/help/conditions/resource-tags) and combine them using boolean and logical operators. Other functions and operators are not supported.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. Customer specified description of the rule. Must be less than or equal to 256 characters.  
`effect` |  `enum (`[Effect](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies#AccessPolicy.Effect)`)` Required. The effect of the rule.  
  
### Effect

An effect to describe the access relationship.

Enums  
---  
`EFFECT_UNSPECIFIED` | The effect is unspecified.  
`DENY` | The policy will deny access if it evaluates to true.  
`ALLOW` | The policy will grant access if it evaluates to true.  
  
### Operation

Attributes that are used to determine whether this rule applies to a request.

JSON representation  
---  
      
    
    {
      "permissions": [
        string
      ],
      "excludedPermissions": [
        string
      ]
    }  
  
Fields  
---  
`permissions[]` |  `string` Optional. The permissions that are explicitly affected by this rule. Each permission uses the format `{service_fqdn}/{resource}.{verb}`, where `{service_fqdn}` is the fully qualified domain name for the service. Currently supported permissions are as follows:

  * `eventarc.googleapis.com/messageBuses.publish`.

  
`excludedPermissions[]` |  `string` Optional. Specifies the permissions that this rule excludes from the set of affected permissions given by `permissions`. If a permission appears in `permissions` _and_ in `excludedPermissions` then it will _not_ be subject to the policy effect.The excluded permissions can be specified using the same syntax as `permissions`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/create)`

|  Creates an access policy, and returns a long running operation.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/delete)`

|  Deletes an access policy.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/get)`

|  Gets an access policy.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/list)`

|  Lists access policies.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/patch)`

|  Updates an access policy.  
  
### `[searchPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/searchPolicyBindings)`

|  Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
