---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools
title: REST Resource: projects.locations.workloadIdentityPools \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:56.005936+00:00
---

# REST Resource: projects.locations.workloadIdentityPools  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: projects.locations.workloadIdentityPools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WorkloadIdentityPool
    * JSON representation
  * State
  * Mode
  * InlineCertificateIssuanceConfig
    * JSON representation
  * KeyAlgorithm
  * InlineTrustConfig
    * JSON representation
  * Methods



## Resource: WorkloadIdentityPool

Represents a collection of workload identities. You can define IAM policies to grant these identities access to Google Cloud resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#State)),
      "disabled": boolean,
      "mode": enum ([Mode](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#Mode)),
      "expireTime": string,
    
      // Union field cert_issuance_config can be only one of the following:
      "inlineCertificateIssuanceConfig": {
        object ([InlineCertificateIssuanceConfig](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#InlineCertificateIssuanceConfig))
      }
      // End of list of possible types for union field cert_issuance_config.
    
      // Union field trust_config can be only one of the following:
      "inlineTrustConfig": {
        object ([InlineTrustConfig](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#InlineTrustConfig))
      }
      // End of list of possible types for union field trust_config.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the pool.  
`displayName` |  `string` Optional. A display name for the pool. Cannot exceed 32 characters.  
`description` |  `string` Optional. A description of the pool. Cannot exceed 256 characters.  
`state` |  `enum (`[State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#State)`)` Output only. The state of the pool.  
`disabled` |  `boolean` Optional. Whether the pool is disabled. You cannot use a disabled pool to exchange tokens, or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#Mode)`)` Immutable. The mode the pool is operating in.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time after which the workload identity pool will be permanently purged and cannot be recovered.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `cert_issuance_config`. Certificate issuance configuration to use for generating X.509 certificates for the workloads. `cert_issuance_config` can be only one of the following:  
`inlineCertificateIssuanceConfig` |  `object (`[InlineCertificateIssuanceConfig](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#InlineCertificateIssuanceConfig)`)` Optional. Defines the Certificate Authority (CA) pool resources and configurations required for issuance and rotation of mTLS workload certificates.  
Union field `trust_config`. Trust configuration for establishing trust with other trust domains. `trust_config` can be only one of the following:  
`inlineTrustConfig` |  `object (`[InlineTrustConfig](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#InlineTrustConfig)`)` Optional. Represents config to add additional trusted trust domains.  
  
## State

The current state of the pool.

Enums  
---  
`STATE_UNSPECIFIED` | State unspecified.  
`ACTIVE` | The pool is active, and may be used in Google Cloud policies.  
`DELETED` | The pool is soft-deleted. Soft-deleted pools are permanently deleted after approximately 30 days. You can restore a soft-deleted pool using `[workloadIdentityPools.undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/undelete#google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPool)`.You cannot reuse the ID of a soft-deleted pool until it is permanently deleted.While a pool is deleted, you cannot use it to exchange tokens, or use existing tokens to access resources. If the pool is undeleted, existing tokens grant access again.  
  
## Mode

Represents the mode for the pool.

Enums  
---  
`MODE_UNSPECIFIED` | State unspecified. New pools should not use this mode. Pools with an unspecified mode will operate as if they are in federation-only mode.  
`FEDERATION_ONLY` | Federation-only mode. Federation-only pools can only be used for federating external workload identities into Google Cloud. Unless otherwise noted, no structure or format constraints are applied to workload identities in a federation-only pool, and you cannot create any resources within the pool besides providers.  
`TRUST_DOMAIN` | Trust-domain mode. Trust-domain pools can be used to assign identities to Google Cloud workloads. All identities within a trust-domain pool must consist of a single namespace and individual workload identifier. The subject identifier for all identities must conform to the following format:`ns/<namespace>/sa/<workload_identifier>``[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`s cannot be created within trust-domain pools.  
  
## InlineCertificateIssuanceConfig

Represents configuration for generating mutual TLS (mTLS) certificates for the identities within this pool.

JSON representation  
---  
      
    
    {
      "caPools": {
        string: string,
        ...
      },
      "lifetime": string,
      "keyAlgorithm": enum ([KeyAlgorithm](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#KeyAlgorithm)),
      "rotationWindowPercentage": integer
    }  
  
Fields  
---  
`caPools` |  `map (key: string, value: string)` Optional. A required mapping of a Google Cloud region to the CA pool resource located in that region. The CA pool is used for certificate issuance, adhering to the following constraints:

  * Key format: A supported cloud region name equivalent to the location identifier in the corresponding map entry's value.
  * Value format: A valid CA pool resource path format like: "projects/{project}/locations/{location}/caPools/{ca_pool}"
  * Region Matching: Workloads are ONLY issued certificates from CA pools within the same region. Also the CA pool region (in value) must match the workload's region (key).

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`lifetime` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Lifetime of the workload certificates issued by the CA pool. Must be between 24 hours and 30 days. If not specified, this will be defaulted to 24 hours.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`keyAlgorithm` |  `enum (`[KeyAlgorithm](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#KeyAlgorithm)`)` Optional. Key algorithm to use when generating the key pair. This key pair will be used to create the certificate. If not specified, this will default to ECDSA_P256.  
`rotationWindowPercentage` |  `integer` Optional. Rotation window percentage, the percentage of remaining lifetime after which certificate rotation is initiated. Must be between 50 and 80. If no value is specified, rotation window percentage is defaulted to 50.  
  
## KeyAlgorithm

Key generation algorithm types for X.509 certificates.

Enums  
---  
`KEY_ALGORITHM_UNSPECIFIED` | Unspecified key algorithm. Defaults to ECDSA_P256.  
`RSA_2048` | Specifies RSA with a 2048-bit modulus.  
`RSA_3072` | Specifies RSA with a 3072-bit modulus.  
`RSA_4096` | Specifies RSA with a 4096-bit modulus.  
`ECDSA_P256` | Specifies ECDSA with curve P256.  
`ECDSA_P384` | Specifies ECDSA with curve P384.  
  
## InlineTrustConfig

Defines configuration for extending trust to additional trust domains. By establishing trust with another domain, the current domain will recognize and accept certificates issued by entities within the trusted domains. Note that a trust domain automatically trusts itself, eliminating the need for explicit configuration.

JSON representation  
---  
      
    
    {
      "additionalTrustBundles": {
        string: {
          object ([TrustStore](https://docs.cloud.google.com/iam/docs/reference/rest/v1/TrustStore))
        },
        ...
      }
    }  
  
Fields  
---  
`additionalTrustBundles` |  `map (key: string, value: object (`[TrustStore](https://docs.cloud.google.com/iam/docs/reference/rest/v1/TrustStore)`))` Optional. Maps specific trust domains (e.g., "example.com") to their corresponding `[TrustStore](https://docs.cloud.google.com/iam/docs/reference/rest/v1/TrustStore)`, which contain the trusted root certificates for that domain. There can be a maximum of 10 trust domain entries in this map.Note that a trust domain automatically trusts itself and don't need to be specified here. If however, this WorkloadIdentityPool's trust domain contains any trust anchors in the additionalTrustBundles map, those trust anchors will be _appended to_ the trust bundle automatically derived from your InlineCertificateIssuanceConfig's caPools.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/create)`

|  Creates a new `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/delete)`

|  Deletes a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/get)`

|  Gets an individual `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
  
### `[getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/getIamPolicy)`

|  Gets the IAM policy of a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/list)`

|  Lists all non-deleted `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`s in a project.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/patch)`

|  Updates an existing `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
  
### `[setIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/setIamPolicy)`

|  Sets the IAM policies on a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`  
  
### `[testIamPermissions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/testIamPermissions)`

|  Returns the caller's permissions on a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`  
  
### `[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/undelete)`

|  Undeletes a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`, as long as it was deleted fewer than 30 days ago.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-28 UTC."],[],[]] 
