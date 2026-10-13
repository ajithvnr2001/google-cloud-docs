---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants
title: REST Resource: locations.workforcePools.providers.scimTenants \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:49.138541+00:00
---

# REST Resource: locations.workforcePools.providers.scimTenants  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: locations.workforcePools.providers.scimTenants Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WorkforcePoolProviderScimTenant
    * JSON representation
  * State
  * Methods



## Resource: WorkforcePoolProviderScimTenant

Gemini Enterprise only. Represents a SCIM tenant. Used for provisioning and managing identity data (such as Users and Groups) in cross-domain environments.

JSON representation  
---  
      
    
    {
      "name": string,
      "baseUri": string,
      "state": enum ([State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants#State)),
      "description": string,
      "displayName": string,
      "claimMapping": {
        string: string,
        ...
      },
      "purgeTime": string,
      "serviceAgent": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Gemini Enterprise only. The resource name of the SCIM Tenant.Format: `locations/{location}/workforcePools/{workforcePool}/providers/ {workforcePoolProvider}/scimTenants/{scim_tenant}`  
`baseUri` |  `string` Output only. Gemini Enterprise only. Represents the base URI as defined in [RFC 7644, Section 1.3](https://datatracker.ietf.org/doc/html/rfc7644#section-1.3). Clients must use this as the root address for managing resources under the tenant.Format: <https://iamscim.googleapis.com/{version}/{tenantId}/>  
`state` |  `enum (`[State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants#State)`)` Output only. Gemini Enterprise only. The state of the tenant.  
`description` |  `string` Optional. Gemini Enterprise only. The description of the SCIM tenant.Cannot exceed 256 characters.  
`displayName` |  `string` Optional. Gemini Enterprise only. The display name of the SCIM tenant.Cannot exceed 32 characters.  
`claimMapping` |  `map (key: string, value: string)` Required. Immutable. Gemini Enterprise only. Maps SCIM attributes to Google attributes.This mapping is used to associate the attributes synced via SCIM with the Google Cloud attributes used in IAM policies for Workforce Identity Federation. SCIM-managed user and group attributes are mapped to `google.subject` and `google.group` respectively.Each key must be a string specifying the Google Cloud IAM attribute to map to. The supported keys are as follows:

  * `google.subject`: The principal IAM is authenticating. You can reference this value in IAM bindings. This is also the subject that appears in Cloud Logging logs. This is a required field and the mapped subject cannot exceed 127 bytes.
  * `google.group`: Group the authenticating user belongs to. You can grant group access to resources using an IAM `principalSet` binding; access applies to all members of the group.

Each value must be a [Common Expression Language](https://opensource.google/projects/cel) expression that maps SCIM user or group attribute to the normalized attribute specified by the corresponding map key.Example: To map the SCIM user's `externalId` to `google.subject` and the SCIM group's `externalId` to `google.group`:
    
    
    {
      "google.subject": "user.externalId",
      "google.group": "group.externalId"
    }
    

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`purgeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Gemini Enterprise only. The timestamp that represents the time when the SCIM tenant is purged.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`serviceAgent` |  `string` Output only. Service Agent created by SCIM Tenant API. SCIM tokens created under this tenant will be attached to this service agent.  
  
## State

Gemini Enterprise only. The current state of the SCIM tenant.

Enums  
---  
`STATE_UNSPECIFIED` | Gemini Enterprise only. State unspecified.  
`ACTIVE` | Gemini Enterprise only. The tenant is active and may be used to provision users and groups.  
`DELETED` | Gemini Enterprise only. The tenant is soft-deleted. Soft-deleted tenants are permanently deleted after approximately 30 days.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/create)`

|  Gemini Enterprise only.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/delete)`

|  Gemini Enterprise only.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/get)`

|  Gemini Enterprise only.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/list)`

|  Gemini Enterprise only.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/patch)`

|  Gemini Enterprise only.  
  
### `[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/undelete)`

|  Gemini Enterprise only.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-18 UTC."],[],[]] 
