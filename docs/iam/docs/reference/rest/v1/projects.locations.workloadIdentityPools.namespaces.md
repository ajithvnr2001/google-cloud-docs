---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces
title: REST Resource: projects.locations.workloadIdentityPools.namespaces \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:57.894515+00:00
---

# REST Resource: projects.locations.workloadIdentityPools.namespaces  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: projects.locations.workloadIdentityPools.namespaces Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WorkloadIdentityPoolNamespace
    * JSON representation
  * State
  * OwnerService
    * JSON representation
  * Methods



## Resource: WorkloadIdentityPoolNamespace

Represents a namespace for a workload identity pool. Namespaces are used to segment identities within the pool.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#State)),
      "disabled": boolean,
      "expireTime": string,
    
      // Union field owner can be only one of the following:
      "ownerService": {
        object ([OwnerService](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#OwnerService))
      }
      // End of list of possible types for union field owner.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the namespace.  
`description` |  `string` Optional. A description of the namespace. Cannot exceed 256 characters.  
`state` |  `enum (`[State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#State)`)` Output only. The state of the namespace.  
`disabled` |  `boolean` Optional. Whether the namespace is disabled. If disabled, credentials may no longer be issued for identities within this namespace, however existing credentials will still be accepted until they expire.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time after which the namespace will be permanently purged and cannot be recovered.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `owner`. Defines the owner that is allowed to mutate this resource. If present, this resource can only be mutated by the owner. `owner` can be only one of the following:  
`ownerService` |  `object (`[OwnerService](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#OwnerService)`)` Output only. The Google Cloud service that owns this namespace.  
  
## State

The current state of the namespace.

Enums  
---  
`STATE_UNSPECIFIED` | State unspecified.  
`ACTIVE` | The namespace is active.  
`DELETED` | The namespace is soft-deleted. Soft-deleted namespaces are permanently deleted after approximately 30 days. You can restore a soft-deleted namespace using `[namespaces.undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/undelete#google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolNamespace)`.You cannot reuse the ID of a soft-deleted namespace until it is permanently deleted.  
  
## OwnerService

The Google Cloud service that owns this namespace.

JSON representation  
---  
      
    
    {
      "principalSubject": string
    }  
  
Fields  
---  
`principalSubject` |  `string` Required. The service agent principal subject, e.g. "serviceAccount:[service-1234@gcp-sa-gkehub.iam.gserviceaccount.com"](mailto:service-1234@gcp-sa-gkehub.iam.gserviceaccount.com").  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/create)`

|  Creates a new `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)` in a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/delete)`

|  Deletes a `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/get)`

|  Gets an individual `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/list)`

|  Lists all non-deleted `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`s in a workload identity pool.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/patch)`

|  Updates an existing `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)` in a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
  
### `[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/undelete)`

|  Undeletes a `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`, as long as it was deleted fewer than 30 days ago.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-28 UTC."],[],[]] 
