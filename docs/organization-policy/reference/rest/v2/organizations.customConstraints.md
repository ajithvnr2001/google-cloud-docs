---
url: https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints
title: REST Resource: organizations.customConstraints \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:40.213187+00:00
---

# REST Resource: organizations.customConstraints  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  REST Resource: organizations.customConstraints Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CustomConstraint
    * JSON representation
  * MethodType
  * ActionType
  * Methods



## Resource: CustomConstraint

A custom constraint defined by customers which can _only_ be applied to the given resource types and organization.

By creating a custom constraint, customers can apply policies of this custom constraint. _Creating a custom constraint itself does NOT apply any policy enforcement_.

JSON representation  
---  
      
    
    {
      "name": string,
      "resourceTypes": [
        string
      ],
      "methodTypes": [
        enum ([MethodType](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints#MethodType))
      ],
      "condition": string,
      "actionType": enum ([ActionType](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints#ActionType)),
      "displayName": string,
      "description": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Name of the constraint. This is unique within the organization. The name must be of the form:

  * `organizations/{organization_id}/customConstraints/{custom_constraint_id}`

Example: `organizations/123/customConstraints/custom.createOnlyE2TypeVms`The max length is 71 characters and the minimum length is 1. Note that the prefix `organizations/{organization_id}/customConstraints/custom.` is not counted.  
`resourceTypes[]` |  `string` Immutable. The resource instance type on which this policy applies. Format will be of the form : `<service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.

  
`methodTypes[]` |  `enum (`[MethodType](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints#MethodType)`)` All the operations being applied for this constraint.  
`condition` |  `string` A Common Expression Language (CEL) condition which is used in the evaluation of the constraint. For example: `resource.instanceName.matches("(production|test)_(.+_)?[\d]+")` or, `resource.management.auto_upgrade == true`The max length of the condition is 1000 characters.  
`actionType` |  `enum (`[ActionType](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints#ActionType)`)` Allow or deny type.  
`displayName` |  `string` One line display name for the UI. The max length of the displayName is 200 characters.  
`description` |  `string` Detailed information about this custom policy constraint. The max length of the description is 2000 characters.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time this custom constraint was updated. This represents the last time that the `customConstraints.create` or `customConstraints.patch` methods were called.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## MethodType

The operation for which this constraint will be applied. To apply this constraint only when creating new resources, set `methodTypes` to `CREATE` only. To apply this constraint when creating or updating resources, set `methodTypes` to `CREATE` and `UPDATE`.

`UPDATE` only custom constraints are not supported. Use `CREATE` or `CREATE, UPDATE`.

Enums  
---  
`METHOD_TYPE_UNSPECIFIED` | This is only used for distinguishing unset values, and results in an error if used.  
`CREATE` | Constraint applied when creating the resource.  
`UPDATE` | Constraint applied when updating the resource.  
`DELETE` | Constraint applied when deleting the resource. Not supported.  
`REMOVE_GRANT` | Constraint applied when removing an IAM grant.  
`GOVERN_TAGS` | Constraint applied when enforcing forced tagging.  
  
## ActionType

Allow or deny type.

Enums  
---  
`ACTION_TYPE_UNSPECIFIED` | This is only used for distinguishing unset values, and results in an error if used.  
`ALLOW` | Allowed action type.  
`DENY` | Deny action type.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/create)`

|  Creates a custom constraint.  
  
### `[delete](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/delete)`

|  Deletes a custom constraint.  
  
### `[get](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/get)`

|  Gets a custom or managed constraint.  
  
### `[list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/list)`

|  Retrieves all of the custom constraints that exist on a particular organization resource.  
  
### `[patch](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/patch)`

|  Updates a custom constraint.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
