---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys
title: REST Resource: locations.workforcePools.providers.keys \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:47.519774+00:00
---

# REST Resource: locations.workforcePools.providers.keys  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: locations.workforcePools.providers.keys Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WorkforcePoolProviderKey
    * JSON representation
  * State
  * KeyUse
  * Methods



## Resource: WorkforcePoolProviderKey

Represents a public key configuration for a Workforce Pool Provider. The key can be configured in your identity provider to encrypt SAML assertions. Google holds the corresponding private key, which it uses to decrypt encrypted tokens.

JSON representation  
---  
      
    
    {
      "name": string,
      "keyData": {
        object ([KeyData](https://docs.cloud.google.com/iam/docs/reference/rest/v1/KeyData))
      },
      "state": enum ([State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#State)),
      "use": enum ([KeyUse](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#KeyUse)),
      "expireTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the key.Format: `locations/{location}/workforcePools/{workforcePoolId}/providers/{providerId}/keys/{keyId}`  
`keyData` |  `object (`[KeyData](https://docs.cloud.google.com/iam/docs/reference/rest/v1/KeyData)`)` Immutable. Public half of the asymmetric key.  
`state` |  `enum (`[State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#State)`)` Output only. The state of the key.  
`use` |  `enum (`[KeyUse](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#KeyUse)`)` Required. The purpose of the key.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time after which the key will be permanently deleted and cannot be recovered. Note that the key may get purged before this time if the total limit of keys per provider is exceeded.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

The current state of the key.

Enums  
---  
`STATE_UNSPECIFIED` | State unspecified.  
`ACTIVE` | The key is active.  
`DELETED` | The key is soft-deleted. Soft-deleted keys are permanently deleted after approximately 30 days. You can restore a soft-deleted key using `[keys.undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/undelete#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderKey)`.  
  
## KeyUse

The purpose of the key.

Enums  
---  
`KEY_USE_UNSPECIFIED` | KeyUse unspecified. Do not use. The purpose of the key must be specified.  
`ENCRYPTION` | The key is used for encryption.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/create)`

|  Creates a new `[WorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#WorkforcePoolProviderKey)` in a `[WorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers#WorkforcePoolProvider)`.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/delete)`

|  Deletes a `[WorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#WorkforcePoolProviderKey)`.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/get)`

|  Gets a `[WorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#WorkforcePoolProviderKey)`.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/list)`

|  Lists all non-deleted `[WorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#WorkforcePoolProviderKey)`s in a `[WorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers#WorkforcePoolProvider)`.  
  
### `[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/undelete)`

|  Undeletes a `[WorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#WorkforcePoolProviderKey)`, as long as it was deleted fewer than 30 days ago.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-18 UTC."],[],[]] 
