---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools
title: REST Resource: locations.workforcePools \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:43.887197+00:00
---

# REST Resource: locations.workforcePools  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: locations.workforcePools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WorkforcePool
    * JSON representation
  * State
  * AccessRestrictions
    * JSON representation
  * ServiceConfig
    * JSON representation
  * Methods



## Resource: WorkforcePool

Represents a collection of external workforces. Provides namespaces for federated users that can be referenced in IAM policies.

JSON representation  
---  
      
    
    {
      "name": string,
      "parent": string,
      "displayName": string,
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#State)),
      "disabled": boolean,
      "sessionDuration": string,
      "expireTime": string,
      "accessRestrictions": {
        object ([AccessRestrictions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#AccessRestrictions))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the pool.Format: `locations/{location}/workforcePools/{workforcePoolId}`  
`parent` |  `string` Immutable. The resource name of the parent.Format: `organizations/{org-id}`.  
`displayName` |  `string` Optional. A display name for the pool.Cannot exceed 32 characters.  
`description` |  `string` Optional. A description of the pool.Cannot exceed 256 characters.  
`state` |  `enum (`[State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#State)`)` Output only. The state of the pool.  
`disabled` |  `boolean` Optional. Disables the workforce pool. You cannot use a disabled pool to exchange tokens, or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again.  
`sessionDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Duration that the Google Cloud access tokens, console sign-in sessions, and `gcloud` sign-in sessions from this pool are valid.Must be greater than 15 minutes (900s) and less than 12 hours (43200s). If `sessionDuration` is not configured, minted credentials have a default duration of one hour (3600s).For SAML providers, the lifetime of the token is the minimum of the `sessionDuration` and the `SessionNotOnOrAfter` claim in the SAML assertion.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time after which the workforce pool will be permanently purged and cannot be recovered.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`accessRestrictions` |  `object (`[AccessRestrictions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#AccessRestrictions)`)` Optional. Configure access restrictions on the workforce pool users. This is an optional field. If specified web sign-in can be restricted to given set of services or programmatic sign-in can be disabled for pool users.  
  
## State

The current state of the pool.

Enums  
---  
`STATE_UNSPECIFIED` | State unspecified.  
`ACTIVE` | The pool is active and may be used in Google Cloud policies.  
`DELETED` | The pool is soft-deleted. Soft-deleted pools are permanently deleted after approximately 30 days. You can restore a soft-deleted pool using `[workforcePools.undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/undelete#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool)`.You cannot reuse the ID of a soft-deleted pool until it is permanently deleted.While a pool is deleted, you cannot use it to exchange tokens, or use existing tokens to access resources. If the pool is undeleted, existing tokens grant access again.  
  
## AccessRestrictions

Access related restrictions on the workforce pool.

JSON representation  
---  
      
    
    {
      "allowedServices": [
        {
          object ([ServiceConfig](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#ServiceConfig))
        }
      ],
      "disableProgrammaticSignin": boolean
    }  
  
Fields  
---  
`allowedServices[]` |  `object (`[ServiceConfig](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#ServiceConfig)`)` Optional. Immutable. Services allowed for web sign-in with the workforce pool. If not set by default there are no restrictions.  
`disableProgrammaticSignin` |  `boolean` Optional. Disable programmatic sign-in by disabling token issue via the Security Token API endpoint. See [Security Token Service API](https://cloud.google.com/iam/docs/reference/sts/rest).  
  
## ServiceConfig

Configuration for a service.

JSON representation  
---  
      
    
    {
      "domain": string
    }  
  
Fields  
---  
`domain` |  `string` Optional. Domain name of the service.Example: console.cloud.google  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/create)`

|  Creates a new `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/delete)`

|  Deletes a `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/get)`

|  Gets an individual `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
  
### `[getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/getIamPolicy)`

|  Gets IAM policies on a `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/list)`

|  Lists all non-deleted `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`s under the specified parent.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/patch)`

|  Updates an existing `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
  
### `[setIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/setIamPolicy)`

|  Sets IAM policies on a `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
  
### `[testIamPermissions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/testIamPermissions)`

|  Returns the caller's permissions on the `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
  
### `[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/undelete)`

|  Undeletes a `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`, as long as it was deleted fewer than 30 days ago.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-25 UTC."],[],[]] 
