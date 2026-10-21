---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/
title: REST Resource: organizations \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:29.475633+00:00
---

# REST Resource: organizations  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: organizations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Organization
    * JSON representation
  * State
  * Methods



## Resource: Organization

The root node in the resource hierarchy to which a particular entity's (a company, for example) resources belong.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations#State)),
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "etag": string,
    
      // Union field owner can be only one of the following:
      "directoryCustomerId": string
      // End of list of possible types for union field owner.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the organization. This is the organization's relative path in the API. Its format is "organizations/[organizationId]". For example, "organizations/1234".  
`displayName` |  `string` Output only. A human-readable string that refers to the organization in the Google Cloud Console. This string is set by the server and cannot be changed. The string will be set to the primary domain (for example, "google.com") of the Google Workspace customer that owns the organization.  
`state` |  `enum (`[State](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations#State)`)` Output only. The organization's current lifecycle state.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the Organization was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the Organization was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the Organization was requested for deletion.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. A checksum computed by the server based on the current value of the Organization resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
Union field `owner`. The owner of this organization. The owner should be specified on creation. Once set, it cannot be changed.The lifetime of the organization and all of its descendants are bound to the owner. If the owner is deleted, the organization and all its descendants will be deleted. `owner` can be only one of the following:  
`directoryCustomerId` |  `string` Immutable. The G Suite / Workspace customer id used in the Directory API.  
  
## State

Organization lifecycle states.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state. This is only useful for distinguishing unset values.  
`ACTIVE` | The normal and active state.  
`DELETE_REQUESTED` | The organization has been marked for deletion by the user.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/get)`

|  Fetches an organization resource identified by the specified resource name.  
  
### `[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/getIamPolicy)`

|  Gets the access control policy for an organization resource.  
  
### `[search](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/search)`

|  Searches organization resources that are visible to the user and satisfy the specified filter.  
  
### `[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/setIamPolicy)`

|  Sets the access control policy on an organization resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/testIamPermissions)`

|  Returns the permissions that a caller has on the specified organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
