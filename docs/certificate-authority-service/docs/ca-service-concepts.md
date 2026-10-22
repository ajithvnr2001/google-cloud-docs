---
url: https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-concepts/
title: Certificate Authority Service concepts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:50.611942+00:00
---

# Certificate Authority Service concepts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Certificate Authority Service concepts

This page explains some of the key concepts in Certificate Authority Service (CA Service).

## Resources

CA Service consists of the following resources:

### Certificate authority pool

A _certificate authority pool (CA pool)_ is the primary resource in CA Service. A CA pool is the container for certificate authorities and certificates. Identity and Access Management conditions, issuance policies, and other configurations are set on the CA pool. Certificate issuance also occurs through the CA pool, which distributes the certificate request load across the CAs in the CA pool.

### Certificate authority

A _certificate authority (CA)_ resource represents the individual certificate authority that is used to sign certificates. In CA Service, you can create both root CAs and subordinate CAs. The root CA has a self-signed certificate and is at the top of the certificate chain. For a subordinate CA, the signer of the CA certificate could either be another CA created in CA Service or an external CA. In the latter case, CA Service generates a certificate signing request (CSR) that must be signed by the external CA. You can use either the Google Cloud CLI or the Google Cloud console to activate the new CA by uploading the signed PEM-encoded certificate chain.

### Certificate

A _certificate_ is a signed X.509 certificate issued by the certificate authority.

### Certificate revocation list

A _certificate revocation list (CRL)_ contains the serial numbers of certificates that have been revoked and should no longer be trusted. CRLs exist as a cloud resource nested under CAs, but can also be published in PEM or DER encodings to a Cloud Storage bucket with a publicly-accessible HTTP-based URL.

### Certificate template

A _certificate template_ is a top-level resource that defines a distinct certificate issuance scenario. Certificates issued using a certificate template inherit pre-configured X.509 extensions like key usage and path length restrictions from the certificate template. A certificate template lets you define which extensions to keep and which ones to ignore from a certificate request. You can use certificate templates to define identity constraints to limit certificate identities. A certificate template can be used with one or more CA pools.

## CA signing keys

CA Service is automatically configured to use Cloud Key Management Service for generating, storing, and utilizing CA signing keys. In CA Service, a Cloud KMS key version is used to sign certificates and CRLs. You can create your own Cloud KMS key and subsequently create a CA which uses this key. Or you can specify the algorithm of the Cloud KMS key that you want to use for a CA, and CA Service will create and configure this key on your behalf. Cloud KMS keys can either be software or hardware backed. When CA Service creates the key on your behalf, it always creates a hardware-backed key.

## Cloud Storage buckets

CAs created in CA Service publish their artifacts such as CA certificates and CRLs in a Cloud Storage bucket in the same location as the deployed CA. Similar to the Cloud KMS keys, the Cloud Storage buckets can either be a Google-managed resource or a customer-managed resource.

## CA tier

The tier of a certificate authority indicates its supported features and billing SKU. CA Service provides the following two operational service tiers for each CA pool created:

  * DevOps: Provides issuance of certificates at a higher certificate issuance rate or throughput, which is helpful in high-volume scenarios. Certificates issued by DevOps CAs are not tracked in the CA database and subsequently can't be revoked. DevOps CAs only support Google-owned and Google-managed encryption keys. They don't support customer-managed Cloud KMS keys.
  * Enterprise: Provides a lower certificate issuance throughput but supports CA operations such as tracking certificates and revoking certificates. This makes the CAs in this tier better suited for long-lived certificate issuance. Enterprise CAs support both customer-managed Cloud KMS signing keys and Google-owned and Google-managed encryption keys.



## Policy controls

Policy controls let you control the type of certificates that your CA pool can issue. Policy controls are one of two types:

  * Coarse-grained policy controls such as issuance policies. A certificate issuance policy defines the types of certificates that the CAs in that CA pool can issue. For example, a user could restrict that their CA pool can only issue certificates that have the correct extended key usage fields set for client TLS, and that it cannot issue CA certificates.
  * Fine-grained policy controls represented using templates that determine the operations that a particular user can perform on a CA pool. Certificate templates can be used in conjunction with IAM conditions to effectively create different policy controls for different users on the same CA pool.



You can enforce policy controls in CA Service in the following ways:

  * Adding a baseline for certificate issuance from an entire CA pool.
  * Using reusable and parameterized templates for common issuance scenarios.
  * Enforcing fine-grained control over IAM bindings with conditions.
  * Simplifying workload certificate provisioning using [identity reflection](https://docs.cloud.google.com/certificate-authority-service/docs/using-identity-reflection).



## What's next

  * [Prepare your environment for Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/prepare-environment).
  * Get started with [CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/create-certificate).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
