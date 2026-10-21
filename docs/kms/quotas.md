---
url: https://docs.cloud.google.com/kms/quotas/
title: Quotas \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:55:21.261685+00:00
---

# Quotas  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Resources ](https://docs.cloud.google.com/kms/docs/resources)



Send feedback 

#  Quotas Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud enforces quotas on resource usage. For Cloud Key Management Service (Cloud KMS), quotas are enforced on management and usage of resources such as keys and key versions, and locations. There are no quotas on the number of key rings, keys, key versions, or other Cloud KMS resources that you can have; only on their usage.

[View Cloud KMS quotas](https://console.cloud.google.com/apis/api/cloudkms.googleapis.com/quotas)

Effective February 16, 2026, Cloud KMS is changing the way quotas are tracked and enforced. This document provides information about how the quotas work before and after the change and helps you identify any steps you may need to take to prepare for the change.

## Timeline

The following table provides an overview of the expected timeline for the changes to Cloud KMS quotas.

Date | What is changing?  
---|---  
October 28, 2024 | Cloud KMS started allowing over-quota requests for hardware (Cloud HSM) keys as long as the Cloud KMS system is not overloaded.  
February 16, 2026 | 

  * Cloud KMS starts using the new metrics. The old metrics are still available for monitoring purposes, but are no longer used for quota enforcement.
  * You can opt in to using the [quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster) system to automatically adjust your Cloud KMS based on your usage.

  
August 31, 2026 | The old metrics are retired and can no longer be monitored.  
  
## Summary of changes

The revised quota system is designed to simplify quota management for Cloud KMS users. The following table summarizes the key changes:

| Before February 16, 2026 | After February 16, 2026  
---|---|---  
**Location scope** | **Mixed scope:** Some metrics are measured globally, and others are measured by region. | **Regional scope:** All metrics are measured per region. Multiregion usage is counted against the quota for the specific region that serves the request.  
**Quota limits** | **Static limits:** Default quota limits are applied to each project. You can request quota limit increases. | **Dynamic limits:** Quota limits are initially set based on your project-specific limits and usage prior to February 16, 2026. We recommend that you also opt in to the [quota adjuster service](https://docs.cloud.google.com/docs/quotas/quota-adjuster), so that your limits are automatically adjusted based on your typical usage.  
**Enforcement** | **Hard enforcement:** When a quota limit is exceeded, requests are denied, even if the system can serve the request. | **Soft enforcement:** When a quota limit is exceeded, read requests and most write requests and cryptographic operation requests are allowed if the system can serve the request. However, the following quota limits are hard-enforced:

  * Create and import requests for hardware (Cloud HSM) keys
  * All requests for external (Cloud EKM) keys

  
**Cloud HSM quotas** | **Many Cloud HSM quotas:** Cloud KMS enforces separate quotas for Cloud HSM symmetric, asymmetric, and `generateRandomBytes` requests. | **One Cloud HSM quota:** Cloud KMS enforces a single quota for all Cloud HSM requests. However, different key sizes and operations consume different quantities of quota.  
**What is measured?** | **Track requests:** Quotas count the number of operations performed, but don't help you understand how much processing resources you're consuming.  | **Track resource usage:** Quotas count tokens instead of operations; the number of tokens per operation indicates the relative processing cost of each operation. For more information, see Tokens per operation on this page.  
**Time scale** | **Mixed time scales:** Some quota metrics are reported per minute, but enforced per second. | **Consistent time scales:** All quota metrics are reported at the same time scale at which they are enforced. Most metrics are reported and enforced per minute. Cloud EKM usage is reported and enforced per second.  
**Project scope** | **Multiple projects:** Some quotas are applied to the project that contains the `CryptoKey` and `CryptoKeyVersion` resources, and others are applied to the project making the request. | **Single project:** All quotas are applied to the project that contains the `CryptoKey` and `CryptoKeyVersion` resources.  
**CMEK and Cloud KMS quotas** | **Unrestricted software CMEK usage:** Cloud KMS doesn't enforce quotas on software keys used in CMEK integrations. | **Restrict only exceptional usage:** CMEK usage counts against the Software usage limit, but with soft enforcement, usage that exceeds your limit is served if the system isn't over capacity.  
  
## Cloud KMS quotas after February 16, 2026

**Important:** The metrics and quotas described in the following sections are scheduled to go into effect on February 16, 2026. To learn about the metrics and quotas that are in effect prior to February 16, 2026, see Quotas before February 16, 2026.

The following table lists the metrics and quotas for Cloud KMS.

Metric | Time scale  
Default | Enforcement | Operations  
---|---|---|---  
Read usage  
`cloudkms.googleapis.com​/read_usage` | Minute  
600 TPM | 

  * Software-backed keys: Soft
  * Hardware-backed keys: Soft
  * External keys: Hard

|  **[cryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/get), [getIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/getIamPolicy), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list), [testIamPermissions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/testIamPermissions) **[cryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/get), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list) **[ekmConnections](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/get), [getIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/getIamPolicy), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/list), [testIamPermissions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/testIamPermissions), [verifyConnectivity](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/verifyConnectivity) **[importJobs](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get), [getIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/getIamPolicy), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/list), [testIamPermissions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/testIamPermissions) **[keyRings](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/get), [getIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/getIamPolicy), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/list), [testIamPermissions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/testIamPermissions) **[locations](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations/get), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations/list)  
Write usage  
`cloudkms.googleapis.com​/write_usage` | Minute  
100 TPM | 

  * Software-backed keys: Soft
  * Hardware-backed keys: Soft
  * External keys: Hard

|  **[cryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys):** [create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create), [patch](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/patch), [setIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/setIamPolicy), [updatePrimaryVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/updatePrimaryVersion) **[cryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions):** [create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/create), [destroy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/destroy), [import](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/import), [patch](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/patch), [restore](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/restore) **[ekmConnections](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections):** [create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/create), [patch](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/patch), [setIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/setIamPolicy) **[importJobs](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs):** [create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/create), [setIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/setIamPolicy) **[keyRings](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings):** [create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/create), [setIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/setIamPolicy)  
Software usage  
`cloudkms.googleapis.com​/software_usage` | Minute  
6,000,000 TPM | Soft |  **[cryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys):** [encrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt), [decrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/decrypt) **[cryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions):** [asymmetricDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricDecrypt), [asymmetricSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricSign), [decapsulate](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/decapsulate), [getPublicKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey), [macSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macSign), [macVerify](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macVerify), [rawEncrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawEncrypt), [rawDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawDecrypt) **[locations](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations):** [generateRandomBytes](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations/generateRandomBytes)  
HSM usage  
`cloudkms.googleapis.com​/hsm_usage` | Minute  
3,000,000 TPM | Soft  
External KMS usage  
`cloudkms.googleapis.com​/external_kms_usage` | Second  
10,000 TPS | Hard  
  
### Tokens per operation

The following table lists the number of quota tokens that are consumed by each operation for each Cloud KMS resource, key size, and operation. You can use this table to estimate how many tokens of quota a certain application can consume. Operations that are more processing intensive use more tokens of quota.

Cloud KMS resource | Operation | Tokens per operation  
---|---|---  
All Cloud KMS resources | All read operations | Read usage: 1  
All software-backed and external Cloud KMS resources | All write operations | Write usage: 1  
Hardware-backed keys | Write operations other than create and import | Write usage: 1  
Hardware-backed symmetric and MAC keys | Create and import operations | Write usage: 1  
HSM usage: 1,200  
Hardware-backed asymmetric keys | Create and import operations | Write usage: 1  
HSM usage: 50,000  
Software-backed keys | All cryptographic operations | Software usage: 100  
External (Cloud EKM) keys | All cryptographic operations | External KMS usage: 100  
Hardware (Cloud HSM) keys | 

  * Symmetric encryption or decryption
  * MAC sign or verify
  * `getPublicKey`

| HSM usage: 100  
Hardware (Cloud HSM) keys | `generateRandomBytes` | HSM usage: 1,000  
Hardware (Cloud HSM) keys | 

  * Asymmetric sign with 2048-bit RSA keys
  * Asymmetric decrypt with 2048-bit keys

| HSM usage: 1,500  
Hardware (Cloud HSM) keys | 

  * Asymmetric sign with 3072-bit RSA keys
  * Asymmetric decrypt with 3072-bit keys

| HSM usage: 3,500  
Hardware (Cloud HSM) keys | 

  * Asymmetric sign with `EC_SIGN_P224_SHA256` keys
  * Asymmetric sign with `EC_SIGN_P256_SHA256` keys
  * Asymmetric sign with `EC_SIGN_SECP256K1_SHA256` keys

| HSM usage: 4,500  
Hardware (Cloud HSM) keys | 

  * Asymmetric sign with `EC_SIGN_P384_SHA384` keys
  * Asymmetric sign with `EC_SIGN_P521_SHA512` keys

| HSM usage: 7,000  
Hardware (Cloud HSM) keys | 

  * Asymmetric decrypt with 4096-bit keys
  * Asymmetric sign with 4096-bit RSA keys

| HSM usage: 14,000  
  
### Suggested actions to prepare for quota changes

Use case | Suggested preparation  
---|---  
Ensure adequate quotas for existing projects | For existing projects, quota limits for the new metrics will be calculated automatically based on the project's actual usage. No action is required for existing projects.  
Ensure adequate quotas for new projects | If you are planning to create a new project and expect high quota usage, opt in to automated quota adjustment using the [quota adjuster service](https://docs.cloud.google.com/docs/quotas/quota-adjuster). Allow 1-2 weeks of gradual traffic increase to allow the systems to adjust to your usage, or proactively request the quota limits that you think you will need.  
Update monitoring to use new quotas | Monitoring using existing quota metrics is available through August 31, 2026. We recommend setting up monitoring using the new metrics after they are available on February 16, 2026 but before August 31, 2026.  
Opt in to quota adjuster | We recommend that you opt in to using the [quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster) system to automatically adjust your Cloud KMS quotas based on your usage. Each project that contains Cloud KMS resources must be opted-in to quota adjuster separately.  
  
## Cloud KMS quotas before February 16, 2026

**Important:** The metrics and quotas described in the following sections are scheduled to be replaced on February 16, 2026. You can continue to monitor your usage of the old metrics and quotas until August 31, 2026. For details on how to manage or increase your quotas, see [Monitor and adjust Cloud KMS quotas](https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas).

Some quotas on these operations apply to the _calling project_ , the Google Cloud project that **makes calls to the Cloud KMS service**. Other quotas apply to the _hosting project_ , the Google Cloud project that **contains the keys used for the operation**.

Calling project quotas don't include usage generated by Google Cloud services using Cloud KMS keys for [customer-managed encryption key (CMEK) integration](https://docs.cloud.google.com/kms/docs/using-other-products#cmek_integrations). For example, encryption and decryption requests coming directly from BigQuery, Bigtable, or Spanner don't contribute to Cryptographic requests quotas.

The Google Cloud console lists the limit for each quota in queries per minute (QPM), but hosting project quotas are enforced by the second. Quotas enforced in queries per second (QPS) deny requests that exceed the QPS limit, even if your per-minute usage is less than the listed QPM limit. If you exceed a QPS limit, you receive a `RESOURCE_EXHAUSTED` error.

### Quotas on the usage of Cloud KMS resources

The following table lists each quota applied to Cloud KMS resources. The table gives the name and limit of each quota, which project the quota applies to, and the operations that count against the quota. You can enter a keyword in the field to filter the table. For example, you can enter _calling_ to see only the quotas applied to the calling project or _encrypt_ to see only the quotas related to encryption operations:

Quota | Project | Limit | Resources and operations  
---|---|---|---  
Read requests  
`cloudkms.googleapis.com​/read_requests` | Calling project | 300 QPM |  **[cryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/get), [getIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/getIamPolicy), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list), [testIamPermissions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/testIamPermissions) **[cryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/get), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list) **[ekmConnections](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/get), [getIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/getIamPolicy), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/list), [testIamPermissions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/testIamPermissions), [verifyConnectivity](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/verifyConnectivity) **[importJobs](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get), [getIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/getIamPolicy), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/list), [testIamPermissions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/testIamPermissions) **[keyRings](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/get), [getIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/getIamPolicy), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/list), [testIamPermissions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/testIamPermissions) **[locations](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations):** [get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations/get), [list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations/list) Exempted: operations from Google Cloud console.  
Write requests  
`cloudkms.googleapis.com​/write_requests` | Calling project | 60 QPM |  **[cryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys):** [create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create), [patch](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/patch), [setIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/setIamPolicy), [updatePrimaryVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/updatePrimaryVersion) **[cryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions):** [create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/create), [destroy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/destroy), [import](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/import), [patch](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/patch), [restore](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/restore) **[ekmConnections](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections):** [create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/create), [patch](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/patch), [setIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/setIamPolicy) **[importJobs](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs):** [create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/create), [setIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/setIamPolicy) **[keyRings](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings):** [create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/create), [setIamPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/setIamPolicy) Exempted: operations from Google Cloud console.  
Cryptographic requests  
`cloudkms.googleapis.com​/crypto_requests` | Calling project | 60,000 QPM |  **[cryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys):** [encrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt), [decrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/decrypt) **[cryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions):** [asymmetricDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricDecrypt), [asymmetricSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricSign), [getPublicKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey), [macSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macSign), [macVerify](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macVerify), [rawEncrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawEncrypt), [rawDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawDecrypt) **[locations](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations):** [generateRandomBytes](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations/generateRandomBytes) Exempted: operations from CMEK integrations.  
HSM symmetric cryptographic requests per region   
`cloudkms.googleapis.com​/hsm_symmetric_requests` | Hosting project | 500 QPS |  **[cryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys):** [encrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt), [decrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/decrypt) **[cryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions):** [asymmetricDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricDecrypt), [asymmetricSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricSign), [getPublicKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey), [macSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macSign), [macVerify](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macVerify), [rawEncrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawEncrypt), [rawDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawDecrypt) Exempted: Single-tenant Cloud HSM keys.  
HSM asymmetric cryptographic requests per region  
`cloudkms.googleapis.com​/hsm_asymmetric_requests` | Hosting project | 50 QPS |  **[cryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys):** [encrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt), [decrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/decrypt) **[cryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions):** [asymmetricDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricDecrypt), [asymmetricSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricSign), [getPublicKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey), [macSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macSign), [macVerify](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macVerify) Exempted: Single-tenant Cloud HSM keys.  
HSM generate random requests per region  
`cloudkms.googleapis.com​/hsm_generate_random_requests` | Hosting project | 50 QPS |  **[locations](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations):** [generateRandomBytes](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations/generateRandomBytes) Exempted: Single-tenant Cloud HSM keys.  
External cryptographic requests per region  
`cloudkms.googleapis.com​/external_kms_requests` | Hosting project | 100 QPS |  **[cryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys):** [encrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt), [decrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/decrypt) **[cryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions):** [asymmetricDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricDecrypt), [asymmetricSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricSign), [getPublicKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey), [macSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macSign), [macVerify](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macVerify)  
  
### Quota examples

The following sections include examples of each quota using the following example projects:

  * `KEY_PROJECT` \- A Google Cloud project that contains Cloud KMS keys, including Multi-tenant Cloud HSM and Cloud EKM keys.

  * `SPANNER_PROJECT` \- A Google Cloud project that contains a Spanner instance which uses the customer-managed encryption keys (CMEKs) that reside in `KEY_PROJECT`.

  * `SERVICE_PROJECT` \- A Google Cloud project that contains a service account that you use to manage Cloud KMS resources that reside in `KEY_PROJECT`.




### Read requests

The **Read requests** quota limits read requests from the Google Cloud project calling the Cloud KMS API. For example, viewing a list of keys in `KEY_PROJECT` from `KEY_PROJECT` using Google Cloud CLI counts against the `KEY_PROJECT` **Read requests** quota. If you use a service account in `SERVICE_PROJECT` to view your list of keys, the read request counts against the `SERVICE_PROJECT` **Read requests** quota.

Using the Google Cloud console to view Cloud KMS resources doesn't contribute to the **Read requests** quota.

#### Write requests

The **Write requests** quota limits write requests from the Google Cloud project calling the Cloud KMS API. For example, creating keys in `KEY_PROJECT` using gcloud CLI counts against the `KEY_PROJECT` **Write requests** quota. If you use a service account in `SERVICE_PROJECT` to create keys, the write request counts against the `SERVICE_PROJECT` **Write requests** quota.

Using the Google Cloud console to create or manage Cloud KMS resources doesn't contribute to the **Read requests** quota.

#### Cryptographic requests

The **Cryptographic requests** quota limits cryptographic operations from the Google Cloud project calling the Cloud KMS API. For example, encrypting data using API calls from a service account resource running in `SERVICE_PROJECT` using keys from `KEY_PROJECT` counts against the `SERVICE_PROJECT` **Cryptographic requests** quota.

Encryption and decryption of data in a Spanner resource in `SPANNER_PROJECT` using CMEK integration doesn't count toward the **Cryptographic requests** quota of `SPANNER_PROJECT`.

#### HSM symmetric cryptographic requests per region 

The **HSM symmetric cryptographic requests per region** quota limits cryptographic operations using symmetric [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) keys on the Google Cloud project that contains those keys. For example, encrypting data in a Spanner resource using symmetric HSM keys counts against the `KEY_PROJECT` **HSM symmetric cryptographic requests per region** quota.

#### HSM asymmetric cryptographic requests per region

The **HSM asymmetric cryptographic requests per region** quota limits cryptographic operations using asymmetric [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) keys on the Google Cloud project that contains those keys. For example, encrypting data in a Spanner resource using asymmetric HSM keys counts against the `KEY_PROJECT` **HSM asymmetric cryptographic requests per region** quota.

#### HSM generate random requests per region

The **HSM generate random requests per region** quota limits generate random bytes operations using [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) in the Google Cloud project specified in the request message. For example, requests from any source to generate random bytes in `KEY_PROJECT` counts against the `KEY_PROJECT` **HSM generate random requests per region** quota.

#### External cryptographic requests per region

The **External cryptographic requests per region** quota limits cryptographic operations using external ([Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm)) keys on the Google Cloud project that contains those keys. For example, encrypting data in a Spanner resource using EKM keys counts against the `KEY_PROJECT` **External cryptographic requests per region** quota.

### Quota error information

If you make a request after your quota is reached, your request results in a `RESOURCE_EXHAUSTED` error. The HTTP status code is `429`. For information on how client libraries surface the `RESOURCE_EXHAUSTED` error, see [Client library mapping](https://docs.cloud.google.com/apis/design/errors#client_library_mapping).

If you receive the `RESOURCE_EXHAUSTED` error, you might be sending too many cryptographic operation requests per second. You can receive the `RESOURCE_EXHAUSTED` error even if the Google Cloud console shows that you are within the queries per minute limit. This issue can happen because Cloud KMS hosting project quotas are displayed per minute, but are enforced on a per second scale. To learn more about monitoring metrics, see [Set up quota alerts and monitoring](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts).

For details about troubleshooting Cloud KMS quota issues, see [Troubleshoot quota issues](https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas#troubleshoot_quotas).

## What's next

  * Learn about [using Cloud Monitoring with Cloud KMS](https://docs.cloud.google.com/kms/docs/monitoring#rate_quota_metrics).
  * Learn how to [monitor and adjust Cloud KMS quotas](https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
