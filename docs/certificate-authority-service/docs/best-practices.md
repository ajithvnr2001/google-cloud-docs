---
url: https://docs.cloud.google.com/certificate-authority-service/docs/best-practices/
title: Best practices for Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:35.257134+00:00
---

# Best practices for Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Best practices for Certificate Authority Service

This page outlines some of the best practices that can help you use Certificate Authority Service more effectively.

## Roles and access control

Using Identity and Access Management (IAM), you can grant roles to users. Roles are a bundle of one or more permissions. Roles in IAM can either be basic, predefined, or custom.

IAM role type | Description  
---|---  
Basic | Includes the Owner, Editor, and Viewer roles that existed before the introduction of IAM.  
Predefined | Predefined roles are created and maintained by Google.  
Custom | Custom roles are user-defined, and let you bundle one or more supported permissions to meet your specific needs. For more information, see [Understanding custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).  
  
Individuals shouldn't be assigned more than one role at any given time. In addition, everyone holding an assigned role should be properly briefed and trained on their responsibilities and security practices. If you want to assign a diverse set of permissions to an individual, we recommend that you create a custom role using IAM. For information about creating a custom role, see [Creating and managing custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about permissions and predefined IAM roles, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).

## CA Service tiers

Tiers are set for the certificate authority (CA) pool. All CAs in a CA pool are assigned the same tier. CA Service provides two operational service tiers for CA pools: DevOps and Enterprise. These two tiers provide organizations with a balance of performance and lifecycle management capabilities based on operational requirements.

  * We recommend that you carefully consider using the DevOps tier because it doesn't support certificate revocation.
  * For CAs in the DevOps tier, issued certificates are not stored. You can only track certificates by reviewing [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit), if enabled. We recommend that you use the DevOps tier only for short-lived certificates that don't need to be revoked, such as certificates used with microservices, containers, session certificates, non-persistent virtual machines, and other isolated needs.
  * A Public Key Infrastructure (PKI) can consist of a combination of CAs in DevOps and Enterprise tiers to meet various needs.
  * In most cases, we recommend that you use the Enterprise tier to create CA pools that issue certificates to other CAs and end-entities.



For more information about CA Service tiers, see [Select the operation tiers](https://docs.cloud.google.com/certificate-authority-service/docs/tiers).

For information about enabling Cloud Audit Logs, see [Configuring Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## CA signing keys

The proper control of the underlying cryptographic key pair for CA certificates determines the security and integrity afforded by the PKI. This section lists some best practices for securing CA signing keys.

### Hardware Security Modules (HSM)

You can configure CA Service to use Google-owned and Google-managed encryption keys that use Cloud HSM for generating, storing, and using keys. However, if you want to use an existing Cloud KMS key, you can use the key during the setup of the CA.

For more information about Cloud HSM, see [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm).

**Note:** After you create or import a key to Cloud HSM, it is not possible to export that key and migrate to another platform.

For more information about importing a cryptographic key into Cloud HSM or Cloud KMS, see [Importing a key into Cloud KMS](https://docs.cloud.google.com/kms/docs/importing-a-key). 

### Google-managed versus customer-managed keys

If you don't have a custom security or operational requirement that requires direct management of keys outside of CA Service, we recommend that you use Google-owned and Google-managed encryption keys. Google-owned and Google-managed encryption keys provide a simplified and secure-by-default key generation, storage, and utilization system.

Google-owned and Google-managed encryption keys use Cloud HSM and aren't accessible or usable by any other organization. Access and use of Cloud HSM signing keys are auditable through Cloud Audit Logs.

**Note:** CA keys are only used for signing issued certificates. They are not used for encrypting information on CA Service.

For more information about lifecycle management models, see [Manage resources](https://docs.cloud.google.com/certificate-authority-service/docs/managed-resources). 

### Importing external CAs

It isn't possible to import previously issued certificates into CA Service. We recommend that you don't import an existing external CA with issued certificates into CA Service.

### Key Escrow

CA Service uses Cloud KMS and Cloud HSM to protect keys from export and extraction. If your organization wants to maintain a copy of its CA keys, you can generate keys using on-premises tools. To use those keys with CA Service, import the keys to Cloud KMS and Cloud HSM. You can then safely escrow the keys and maintain possession until needed in future.

For information about importing keys into Cloud KMS, see [Importing a key into Cloud KMS](https://docs.cloud.google.com/kms/docs/importing-a-key).

### CA key sizes and algorithms

Cryptographic key sizes and algorithms define the type and strength of the asymmetric key-pair that is used to sign certificates and Certificate Revocation Lists (CRLs). CAs can live for a relatively long period. Therefore, it is important that the keys are strong enough to be secure throughout the CA's intended lifetime.

If you have a well-defined PKI environment with modern devices, [Elliptic Curve Digital Signature Algorithm (ECDSA)](https://docs.cloud.google.com/certificate-authority-service/docs/choosing-key-algorithm#ecdsa) offers the best performance and security. In organizations with a wide range of systems and uncertainty about key support, it could be sufficient to use RSA-based keys.

There are also other considerations for CA signing keys, such as compliance with certifications, compatibility with other systems, and the specific threat models. Consider your use case when choosing a key size and algorithm.

Regardless of the CA lifetime, or key size and algorithm, we recommend that you set up a process for regular rotation of CA keys.

For more information about choosing an algorithm for signing keys, see [Choose a key algorithm](https://docs.cloud.google.com/certificate-authority-service/docs/choosing-key-algorithm).

## What's next

  * [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool)
  * [Create a root certificate authority](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca)
  * [Create a subordinate certificate authority](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca)
  * [Create a certificate template](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
