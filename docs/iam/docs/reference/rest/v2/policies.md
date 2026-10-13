---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/
title: REST Resource: policies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:41.938386+00:00
---

# REST Resource: policies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: policies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Policy
    * JSON representation
  * PolicyRule
    * JSON representation
  * DenyRule
    * JSON representation
  * Methods



## Resource: Policy

Data for an IAM policy.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "kind": string,
      "displayName": string,
      "annotations": {
        string: string,
        ...
      },
      "etag": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "rules": [
        {
          object ([PolicyRule](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies#PolicyRule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the `Policy`, which must be unique. Format: `policies/{attachmentPoint}/denypolicies/{policyId}`The attachment point is identified by its URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-deny-policy`.For organizations and folders, use the numeric ID in the full resource name. For projects, requests can use the alphanumeric or the numeric ID. Responses always contain the numeric ID.  
`uid` |  `string` Immutable. The globally unique ID of the `Policy`. Assigned automatically when the `Policy` is created.  
`kind` |  `string` Output only. The kind of the `Policy`. Always contains the value `DenyPolicy`.  
`displayName` |  `string` A user-specified description of the `Policy`. This value can be up to 63 characters.  
`annotations` |  `map (key: string, value: string)` A key-value map to store arbitrary metadata for the `Policy`. Keys can be up to 63 characters. Values can be up to 255 characters.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` An opaque tag that identifies the current version of the `Policy`. IAM uses this value to help manage concurrent updates, so they do not cause one update to be overwritten by another.If this field is present in a `CreatePolicyRequest`, the value is ignored.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the `Policy` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the `Policy` was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the `Policy` was deleted. Empty if the policy is not deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rules[]` |  `object (`[PolicyRule](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies#PolicyRule)`)` A list of rules that specify the behavior of the `Policy`. All of the rules should be of the `kind` specified in the `Policy`.  
  
## PolicyRule

A single rule in a `Policy`.

JSON representation  
---  
      
    
    {
      "description": string,
    
      // Union field kind can be only one of the following:
      "denyRule": {
        object ([DenyRule](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies#DenyRule))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
`description` |  `string` A user-specified description of the rule. This value can be up to 256 characters.  
Union field `kind`.`kind` can be only one of the following:  
`denyRule` |  `object (`[DenyRule](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies#DenyRule)`)` A rule for a deny policy.  
  
## DenyRule

A deny rule in an IAM deny policy.

JSON representation  
---  
      
    
    {
      "deniedPrincipals": [
        string
      ],
      "exceptionPrincipals": [
        string
      ],
      "deniedPermissions": [
        string
      ],
      "exceptionPermissions": [
        string
      ],
      "denialCondition": {
        object ([Expr](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Expr))
      }
    }  
  
Fields  
---  
`deniedPrincipals[]` |  `string` The identities that are prevented from using one or more permissions on Google Cloud resources. This field can contain the following values:

  * `principal://goog/subject/{email_id}`: A specific Google Account. Includes Gmail, Cloud Identity, and Google Workspace user accounts. For example, `principal://goog/subject/alice@example.com`.
  * `principal://iam.googleapis.com/projects/-/serviceAccounts/{service_account_id}`: A Google Cloud service account. For example, `principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@iam.gserviceaccount.com`.
  * `principalSet://goog/group/{groupId}`: A Google group. For example, `principalSet://goog/group/admins@example.com`.
  * `principalSet://goog/public:all`: A special identifier that represents any principal that is on the internet, even if they do not have a Google Account or are not logged in.
  * `principalSet://goog/cloudIdentityCustomerId/{customerId}`: All of the principals associated with the specified Google Workspace or Cloud Identity customer ID. For example, `principalSet://goog/cloudIdentityCustomerId/C01Abc35`.
  * `principal://iam.googleapis.com/locations/global/workforcePools/{pool_id}/subject/{subject_attribute_value}`: A single identity in a workforce identity pool.
  * `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/group/{groupId}`: All workforce identities in a group.
  * `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/attribute.{attribute_name}/{attribute_value}`: All workforce identities with a specific attribute value.
  * `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/*`: All identities in a workforce identity pool.
  * `principal://iam.googleapis.com/projects/{projectNumber}/locations/global/workloadIdentityPools/{pool_id}/subject/{subject_attribute_value}`: A single identity in a workload identity pool.
  * `principalSet://iam.googleapis.com/projects/{projectNumber}/locations/global/workloadIdentityPools/{pool_id}/group/{groupId}`: A workload identity pool group.
  * `principalSet://iam.googleapis.com/projects/{projectNumber}/locations/global/workloadIdentityPools/{pool_id}/attribute.{attribute_name}/{attribute_value}`: All identities in a workload identity pool with a certain attribute.
  * `principalSet://iam.googleapis.com/projects/{projectNumber}/locations/global/workloadIdentityPools/{pool_id}/*`: All identities in a workload identity pool.
  * `principalSet://cloudresourcemanager.googleapis.com/[projects|folders|organizations]/{projectNumber|folder_number|org_number}/type/ServiceAccount`: All service accounts grouped under a resource (project, folder, or organization).
  * `principalSet://cloudresourcemanager.googleapis.com/[projects|folders|organizations]/{projectNumber|folder_number|org_number}/type/ServiceAgent`: All service agents grouped under a resource (project, folder, or organization).
  * `deleted:principal://goog/subject/{email_id}?uid={uid}`: A specific Google Account that was deleted recently. For example, `deleted:principal://goog/subject/alice@example.com?uid=1234567890`. If the Google Account is recovered, this identifier reverts to the standard identifier for a Google Account.
  * `deleted:principalSet://goog/group/{groupId}?uid={uid}`: A Google group that was deleted recently. For example, `deleted:principalSet://goog/group/admins@example.com?uid=1234567890`. If the Google group is restored, this identifier reverts to the standard identifier for a Google group.
  * `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/{service_account_id}?uid={uid}`: A Google Cloud service account that was deleted recently. For example, `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@iam.gserviceaccount.com?uid=1234567890`. If the service account is undeleted, this identifier reverts to the standard identifier for a service account.
  * `deleted:principal://iam.googleapis.com/locations/global/workforcePools/{pool_id}/subject/{subject_attribute_value}`: Deleted single identity in a workforce identity pool. For example, `deleted:principal://iam.googleapis.com/locations/global/workforcePools/my-pool-id/subject/my-subject-attribute-value`.

  
`exceptionPrincipals[]` |  `string` The identities that are excluded from the deny rule, even if they are listed in the `deniedPrincipals`. For example, you could add a Google group to the `deniedPrincipals`, then exclude specific users who belong to that group.This field can contain the same values as the `deniedPrincipals` field, excluding `principalSet://goog/public:all`, which represents all users on the internet.  
`deniedPermissions[]` |  `string` The permissions that are explicitly denied by this rule. Each permission uses the format `{service_fqdn}/{resource}.{verb}`, where `{service_fqdn}` is the fully qualified domain name for the service. For example, `iam.googleapis.com/roles.list`.  
`exceptionPermissions[]` |  `string` Specifies the permissions that this rule excludes from the set of denied permissions given by `deniedPermissions`. If a permission appears in `deniedPermissions` _and_ in `exceptionPermissions` then it will _not_ be denied.The excluded permissions can be specified using the same syntax as `deniedPermissions`.  
`denialCondition` |  `object (`[Expr](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Expr)`)` The condition that determines whether this deny rule applies to a request. If the condition expression evaluates to `true`, then the deny rule is applied; otherwise, the deny rule is not applied.Each deny rule is evaluated independently. If this deny rule does not apply to a request, other deny rules might still apply.The condition can use CEL functions that evaluate [resource tags](https://cloud.google.com/iam/help/conditions/resource-tags). Other functions and operators are not supported.  
  
## Methods  
  
---  
  
### `[createPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/createPolicy)`

|  Creates a policy.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/delete)`

|  Deletes a policy.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/get)`

|  Gets a policy.  
  
### `[listPolicies](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/listPolicies)`

|  Retrieves the policies of the specified kind that are attached to a resource.  
  
### `[update](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/update)`

|  Updates the specified policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-28 UTC."],[],[]] 
