---
url: https://docs.cloud.google.com/certificate-authority-service/quotas/
title: Quotas and limits \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:51.558280+00:00
---

# Quotas and limits  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Resources ](https://docs.cloud.google.com/certificate-authority-service/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This page lists the quotas and limits that apply to Certificate Authority Service.

## Resource limits

CA Service enforces the following usage limits:

Resource | Unit | Value  
---|---|---  
Pending CAs1 | per Location per Project | 100  
CAs | per Location per Project | 1000  
Unexpired revoked certificates2 | per CA or certificate revocation list (CRL) | 500 for CAs with external signing keys.  
500,000 for CAs with HSM or software signing keys.  
  
1A _pending_ certificate authority (CA) is a subordinate CA that has been created but not yet activated, and is thus in the `AWAITING_USER_ACTIVATION` [state](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1beta1/projects.locations.certificateAuthorities#State).

2A CRL can contain at most 500,000 unexpired revoked certificates. If you attempt to revoke more than this limit, the revocation request fails. If you need to revoke more than 500,000 certificates, we recommend that you wait until the existing revoked certificates have expired or revoke the issuing CA certificate.

## Rate quotas

The following rate quotas apply to CA Service requests:

Request | Unit | Maximum requests  
---|---|---  
[CreateCertificate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates/create) | per Certificate Authority (Enterprise tier) | 7 per second*  
[CreateCertificate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates/create) | per Certificate Authority (DevOps tier) | 25 per second*  
[CreateCertificate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates/create) | per Location per Project | 100 per second*  
[ListCertificates](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates/list) | per Location per Project | 10 per second*  
[CreateCertificateAuthority](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificateAuthorities/create) | per Location per Project | 5 per minute*  
All other mutation requests | per Location per Project | 40 per second*  
All other requests | per Location per Project | 400 per second*  
  
* Even if you have available quota, other factors can result in reduced throughput.

## Quota increases

You can use the Google Cloud console to request a quota increase. You can request a quota increase for certificate issuance, titled "CreateCertificate requests per project per minute per region".

For more information, see [Requesting a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
