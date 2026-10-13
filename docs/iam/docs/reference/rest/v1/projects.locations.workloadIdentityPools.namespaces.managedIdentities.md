---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities
title: REST Resource: projects.locations.workloadIdentityPools.namespaces.managedIdentities \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:59.386975+00:00
---

# REST Resource: projects.locations.workloadIdentityPools.namespaces.managedIdentities  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: projects.locations.workloadIdentityPools.namespaces.managedIdentities Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WorkloadIdentityPoolManagedIdentity
    * JSON representation
  * State
  * Methods



## Resource: WorkloadIdentityPoolManagedIdentity

Represents a managed identity for a workload identity pool namespace.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#State)),
      "disabled": boolean,
      "expireTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the managed identity.  
`description` |  `string` Optional. A description of the managed identity. Cannot exceed 256 characters.  
`state` |  `enum (`[State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#State)`)` Output only. The state of the managed identity.  
`disabled` |  `boolean` Optional. Whether the managed identity is disabled. If disabled, credentials may no longer be issued for the identity, however existing credentials will still be accepted until they expire.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time after which the managed identity will be permanently purged and cannot be recovered.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

The current state of the managed identity.

Enums  
---  
`STATE_UNSPECIFIED` | State unspecified.  
`ACTIVE` | The managed identity is active.  
`DELETED` | The managed identity is soft-deleted. Soft-deleted managed identities are permanently deleted after approximately 30 days. You can restore a soft-deleted managed identity using `[managedIdentities.undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/undelete#google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolManagedIdentity)`.You cannot reuse the ID of a soft-deleted managed identity until it is permanently deleted.  
  
## Methods  
  
---  
  
### `[addAttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/addAttestationRule)`

|  Add an `[AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule)` on a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/create)`

|  Creates a new `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)` in a `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/delete)`

|  Deletes a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/get)`

|  Gets an individual `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/list)`

|  Lists all non-deleted `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`s in a namespace.  
  
### `[listAttestationRules](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/listAttestationRules)`

|  List all `[AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule)` on a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/patch)`

|  Updates an existing `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)` in a `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`.  
  
### `[removeAttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/removeAttestationRule)`

|  Remove an `[AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule)` on a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
  
### `[setAttestationRules](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/setAttestationRules)`

|  Set all `[AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule)` on a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
  
### `[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/undelete)`

|  Undeletes a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`, as long as it was deleted fewer than 30 days ago.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-25 UTC."],[],[]] 
