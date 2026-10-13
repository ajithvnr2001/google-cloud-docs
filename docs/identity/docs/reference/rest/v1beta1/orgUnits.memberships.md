---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships
title: REST Resource: orgUnits.memberships \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:56.409107+00:00
---

# REST Resource: orgUnits.memberships  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: orgUnits.memberships Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: OrgMembership

A membership in an OrgUnit.

An `OrgMembership` defines a relationship between an `OrgUnit` and an entity belonging to that `OrgUnit`, referred to as a "member".

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([EntityType](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#EntityType)),
      "member": string,
      "memberUri": string
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `[OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership)`.Format: orgUnits/{$orgUnitId}/memberships/{$membership}The `$orgUnitId` is the `orgUnitId` from the [Admin SDK `OrgUnit` resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits).The `$membership` shall be of the form `{$entityType};{$memberId}`, where `$entityType` is the enum value of [OrgMembership.EntityType], and `memberId` is the `id` from [Drive API (V3) `Drive` resource](https://developers.google.com/drive/api/v3/reference/drives#resource) for `[OrgMembership.EntityType.SHARED_DRIVE](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#EntityType.ENUM_VALUES.SHARED_DRIVE)`.  
`type` |  `enum (`[EntityType](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#EntityType)`)` Immutable. Entity type for the org member.  
`member` |  `string` Immutable. Org member id as full resource name.Format for shared drive resource: //drive.googleapis.com/drives/{$memberId}where `$memberId` is the `id` from [Drive API (V3) `Drive` resource](https://developers.google.com/drive/api/v3/reference/drives#resource).  
`memberUri` |  `string` Uri with which you can read the member.This follows <https://aip.dev/122>Format for shared drive resource: <https://drive.googleapis.com/drive/v3/drives/{$memberId>}where `$memberId` is the `id` from [Drive API (V3) `Drive` resource](https://developers.google.com/drive/api/v3/reference/drives#resource).  
  
## EntityType

Entity type for an org member.

Enums  
---  
`ENTITY_TYPE_UNSPECIFIED` | Equivalent to no resource type mentioned  
`SHARED_DRIVE` | Shared drive as resource type  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships/list)`

|  List `[OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership)` resources in an OrgUnit treated as 'parent'.  
  
### `[move](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships/move)`

|  Move an `[OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership)` to a new OrgUnit.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-06 UTC."],[],[]] 
