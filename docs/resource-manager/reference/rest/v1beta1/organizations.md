---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/
title: REST Resource: organizations \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:04.793160+00:00
---

# REST Resource: organizations  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: organizations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Organization
    * JSON representation
  * OrganizationOwner
    * JSON representation
  * LifecycleState
  * Methods



## Resource: Organization

The root node in the resource hierarchy to which a particular entity's (e.g., company) resources belong.

JSON representation  
---  
      
    
    {
      "name": string,
      "organizationId": string,
      "displayName": string,
      "owner": {
        object ([OrganizationOwner](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations#OrganizationOwner))
      },
      "creationTime": string,
      "lifecycleState": enum ([LifecycleState](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations#LifecycleState))
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the organization. This is the organization's relative path in the API. Its format is "organizations/[organizationId]". For example, "organizations/1234".  
`organizationId  
**(deprecated)**` |  `string` This item is deprecated!An immutable id for the Organization that is assigned on creation. This should be omitted when creating a new Organization. This field is read-only.  
`displayName` |  `string` A human-readable string that refers to the Organization in the Google Cloud console. This string is set by the server and cannot be changed. The string will be set to the primary domain (for example, "google.com") of the G Suite customer that owns the organization.  
`owner` |  `object (`[OrganizationOwner](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations#OrganizationOwner)`)` The owner of this Organization. The owner should be specified on creation. Once set, it cannot be changed. This field is required.  
`creationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the Organization was created. Assigned by the server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lifecycleState` |  `enum (`[LifecycleState](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations#LifecycleState)`)` The organization's current lifecycle state. Assigned by the server.  
  
## OrganizationOwner

The entity that owns an Organization. The lifetime of the Organization and all of its descendants are bound to the `OrganizationOwner`. If the `OrganizationOwner` is deleted, the Organization and all its descendants will be deleted.

JSON representation  
---  
      
    
    {
    
      // Union field owner_oneof can be only one of the following:
      "directoryCustomerId": string
      // End of list of possible types for union field owner_oneof.
    }  
  
Fields  
---  
Union field `owner_oneof`. The entity that owns an Organization. `owner_oneof` can be only one of the following:  
`directoryCustomerId` |  `string` The G Suite customer id used in the Directory API.  
  
## LifecycleState

Organization lifecycle states.

Enums  
---  
`LIFECYCLE_STATE_UNSPECIFIED` | Unspecified state. This is only useful for distinguishing unset values.  
`ACTIVE` | The normal and active state.  
`DELETE_REQUESTED` | The organization has been marked for deletion by the user.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/get)`

|  Fetches an Organization resource identified by the specified resource name.  
  
### `[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/getIamPolicy)`

|  Gets the access control policy for an Organization resource.  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/list)`

|  Lists Organization resources that are visible to the user and satisfy the specified filter.  
  
### `[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/setIamPolicy)`

|  Sets the access control policy on an Organization resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/testIamPermissions)`

|  Returns permissions that a caller has on the specified Organization.  
  
### `[update](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/update)   
**(deprecated)**`

|  Updates an Organization resource identified by the specified resource name.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
