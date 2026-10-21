---
url: https://docs.cloud.google.com/certificate-manager/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:00:08.541720+00:00
---

# Quotas and limits  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/certificate-manager/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Certificate Manager.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Certificate Manager resources. System limits can't be changed. 

Your use of Certificate Manager is governed by the following types of quotas:

  * **Rate quotas** determine how quickly you can call the Certificate Manager API as well as create and access Certificate Manager resources.

  * **Resource quotas** determine the total amount of Certificate Manager resources you can create within your Google Cloud project.




For more information about working with quotas, including steps for increasing them, and for setting up monitoring and alerting on quota metrics, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

## Rate quotas

The following table lists the rate quotas for Certificate Manager.

Item | Default quota | Description  
---|---|---  
**API requests** | [300 per minute](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=api-requests) | All calls to the Certificate Manager API  
**Read requests** | [300 per minute](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=read-requests) | `GET` and `LIST` calls to the Certificate Manager API  
**Write requests** | [300 per minute](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=write-requests) | `CREATE`, `PATCH`, and `DELETE` calls to the Certificate Manager API  
  
## Resource quotas and limits

The following table lists the resource quotas and limits for Certificate Manager certificates.

Item | Default quotas and limits | Description  
---|---|---  
**Google-managed certificates** | [1000](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fmanaged-certificates) | Total number of Google-managed certificates within the Google Cloud project  
**Regional Google-managed certificates** | [100](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fregional-managed-certificates) | Total number of regional Google-managed certificates per region within the Google Cloud project  
**Self-managed certificates** | [1000](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fself-managed-certificates) | Total number of self-managed certificates within the Google Cloud project  
**Regional self-managed certificates** | [100](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fregional-self-managed-certificates) | Total number of regional self-managed certificates per region within the Google Cloud project  
**Certificate maps** | [100](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fcertificate-maps) | Total number of certificate maps within the Google Cloud project  
**Certificate map entries** | [5000](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fcertificate-map-entries) | Total number of certificate map entries within the Google Cloud project  
**Resources associated with a certificate** | Limit: 100 | Total number of resources, such as certificate map entries and target proxies, associated with a certificate.  
**Certificates per certificate map entry** | Limit: 4 | Total number of certificates that you can attach to a certificate map entry  
**Certificates per target proxy** | Limit: 100 | Total number of certificates that you can directly attach to a target https proxy  
**Certificate map per target proxy** | Limit: 1 | Total number of certificate maps that you can attach to a target https proxy  
**DNS authorizations** | [1000](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fdns-authorizations) | Total number of DNS authorizations within the Google Cloud project  
**Regional DNS authorizations** | [300](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fregional-dns-authorizations) | Total number of regional DNS authorizations per region within the Google Cloud project  
**Certificate issuance configs** | [100](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fcertificate-issuance-configs) | Total number of certificate issuance configs within the Google Cloud project  
**Regional certificate issuance configs** | [5](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fregional-certificate-issuance-configs) | Total number of regional certificate issuance configs per region within the Google Cloud project  
**Trust config size** | [10000](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Ftrust-config-size) | Total size of all global trust configs within the Google Cloud project. For details on how the size is calculated, see Trust config size calculation.   
**Regional trust config size** | [10000](https://console.cloud.google.com/iam-admin/quotas?service=certificatemanager.googleapis.com&metric=certificatemanager.googleapis.com%2Fregional-trust-config-size) | Total size of regional trust configs per region within the Google Cloud project. For details on how the size is calculated, see Trust config size calculation.  
**Supported key types for self-managed certificates** | 

  * RSA-2048
  * RSA-3072
  * RSA-4096
  * ECDSA P-256
  * ECDSA P-384

|   
**Supported key type for publicly trusted Google-managed certificates** | RSA-2048 |   
**Supported key types for privately trusted Google-managed certificates** | 

  * RSA-2048
  * ECDSA P-256

|   
  
## Domain name length limitations for Google-managed certificates

The following table lists domain name length limitations specific to Google-managed certificates in Certificate Manager.

Item | Characters | Domain  
---|---|---  
**Load balancer authorization** | 253 | All  
**DNS authorization** | 237 | All  
**Per-project DNS authorization with Google CA** | 220 | All  
  
## Additional resource limits for Google-managed certificates

The following table lists additional resource limits specific to Google-managed certificates in Certificate Manager. These limits _cannot be increased_.

Item | Limit | Description  
---|---|---  
**Domains per certificate with load balancer authorization** | 5 | Maximum number of domains allowed per Google-managed certificate with load balancer authorization.  
**Domains per certificate with DNS authorization** | 100 | Maximum number of domains allowed per Google-managed certificate with DNS authorization.  
  
## Additional request quotas for Public CA operations

Quotas for Public CA operations are independent of quotas governing Certificate Manager operations on Google-managed certificates. They are also independent of any other quotas governing operations on Google-managed certificates performed by any other Google Cloud products.

Certificate Manager enforces the quota limits listed in this section for Public CA operations. Keep the following guidelines in mind:

  * Certificate Manager can rate-limit your per-minute requests.
  * Certificate Manager can return HTTP 429 response code asking an ACME client to retry a request after waiting a few seconds. Your ACME clients must support this response code and respect the `Retry-After` header that Certificate Manager sends with the response.



The production and the staging environment have the same limits, but they are independent of each other. Requests to the production environment and the staging environment only consume their respective quotas.

## Public CA request quotas

The following table lists the Public CA request quotas that apply to [ACME certificate management operations](https://datatracker.ietf.org/doc/html/rfc8555#section-7).

**Note:** Certificate Manager applies quotas at the Google Cloud project level. If you create two or more ACME accounts within the same Google Cloud project, those accounts share request quotas.Quota | Default limit | Description  
---|---|---  
**Request a certificate  
(`newOrder`)** | 100 per hour | Maximum number of new certificate requests  
**Create an ACME account  
(`newAccount`)** | 25 per minute, 100 per hour | Maximum number of account creation requests  
**Create an authorization  
(`newAuthz`)** | 300 per hour | Maximum number of authorization creation requests  
**Poll an authorization  
(`authz`)** | 600 per minute | Maximum number of authorization polling requests  
**Verify or poll a challenge  
(`challenge`)** | 100 per minute | Maximum number of challenge verification or polling requests  
**Poll certificate issuance  
(`cert`)** | 50 per minute | Maximum number of certificate issuance polling requests  
**Revoke certificate  
(`revokeCert`)** | 25 per 30s | Maximum number of certificate revocation requests  
  
## Trust config

The limits documented here cannot be increased and apply to classic Application Load Balancers and global external Application Load Balancers.

Item | Quotas and limits | Notes  
---|---|---  
Number of trust stores | Limit: 1 | This limit is per `TrustConfig` resource.  
Combined number of trust anchors and intermediate certificates | Limit: 200 | This limit is per trust store.  
Number of intermediate certificates | Limit: 100 | This limit is per trust store.  
Number of name constraints allowed during validation of root and intermediate certificates | Limit: 10 |   
Intermediate certificates that share the same Subject and Subject Public Key information | Limit: 10 | This limit is per trust store.  
Certificate chain depth | Limit: 10 | The maximum depth for a certificate chain, including the root and client certificates.  
Number of times intermediate certificates can be evaluated when attempting to build the chain of trust | Limit: 100 |   
Supported key types | 

  * RSA-2048
  * RSA-3072
  * RSA-4096
  * ECDSA P-256
  * ECDSA P-384

|   
Number of certificates in allowlist (`allowlistedCertificates`)  | Limit: 500 |   
  
### Trust config size calculation

The following quotas track the size limit for trust configs:

  * `certificatemanager.googleapis.com/trust-config-size` for global trust configs.
  * `certificatemanager.googleapis.com/regional-trust-config-size` for regional trust configs.



Certificate Manager determines the quota usage of a trust config based on its total size, and calculates it using the following rules:

  1. Certificate PEMs: each Privacy-Enhanced Mail (PEM) certificate that you include as a trust anchor or an intermediate CA certificate, use 1 quota unit for every 1 kB of size, rounded up to the nearest 1 kB.
  2. Certificates on the allowlist: every 32 certificates on the allowlist (rounded up) use 1 unit of quota.

  3. Secure Production Identity Framework for Everyone (SPIFFE) trust domains: every 4 SPIFFE trust domains (rounded up) use 1 unit of quota.

  4. Overhead: every trust config uses a constant overhead of 2 units of quota, even if the trust config is empty.




#### Examples

  * An empty `TrustConfig` resource uses 2 units of quota.
  * A small `TrustConfig` resource (single 3 kB certificate) uses 5 units of quota (3 for the certificate + 2 overhead).
  * A complex `TrustConfig` resource uses: 
    * 4 certificates with sizes 3.5 kB, 5 kB, 4.5 kB, and 6 kB: (4 + 5 + 5 + 6) = 20 units of quota.
    * 10 certificates on the allowlist: 1 unit of quota.
    * 5 SPIFFE trust domains: 2 units of quota.
    * Constant overhead: 2 units of quota.
    * Total quota usage: 20 + 1 + 2 + 2 = 25 units of quota.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
