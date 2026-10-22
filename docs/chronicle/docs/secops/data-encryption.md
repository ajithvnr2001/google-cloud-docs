---
url: https://docs.cloud.google.com/chronicle/docs/secops/data-encryption/
title: Data encryption at rest and in transit \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:06.521699+00:00
---

# Data encryption at rest and in transit  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/data-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data encryption at rest and in transit

Supported in:

Google SecOps 

This document describes how Google Security Operations protects customer data using encryption at rest and in transit.

This guide is for security engineers and administrators who want to verify default data protection and manage cryptographic keys for Google SecOps. It explains how data is protected at rest and in transit, and how to use customer-managed encryption keys (CMEK) in Cloud Key Management Service. By following this guide, you maintain control over encryption key lifecycles and meet organizational compliance mandates. Successful implementation strengthens your data security posture and reduces compliance risks.

## Common use cases

The following use cases describe how security teams use encryption controls in Google SecOps:

### Verify default encryption for compliance audits

  * **Objective** : Confirm that all customer data stored on disk and transmitted across networks is automatically protected using industry-standard encryption algorithms and protocols.
  * **Value** : Satisfies baseline regulatory and security requirements without requiring manual configuration or operational overhead.



### Control cryptographic key lifecycles with CMEK

  * **Objective** : Manage encryption key creation, rotation, and revocation in Cloud KMS for a Google SecOps instance.
  * **Value** : Meets strict data governance and sovereignty mandates by maintaining direct administrative control over encryption keys.



## Key terminology

Review the following terms used throughout this document:

  * **Advanced Encryption Standard (AES)** : A symmetric block cipher standard using 256-bit keys to encrypt stored customer data.
  * **Transport Layer Security (TLS)** : A cryptographic protocol that protects data transmitted over networks from interception.
  * **Customer-managed encryption keys (CMEK)** : Encryption keys that you create, own, and manage in Cloud KMS to protect data at rest in your Google SecOps instance.



## Before you begin

Before you configure encryption controls for Google SecOps, confirm that you meet the following prerequisites:

  * **Permissions** : Default encryption at rest and in transit requires no setup or additional Identity and Access Management (IAM) roles. To configure CMEK, you must grant Google SecOps access to your Cloud KMS key during instance creation. For more information, see [Configure CMEK](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops).
  * **Environment check** : CMEK is available in all supported Google SecOps regions. For the full list of supported locations, see [Google SecOps service locations](https://cloud.google.com/terms/secops/data-residency). When you deploy an instance in the `eu` or `us` multi-regions, you must configure an additional CMEK in the `europe-west1` or `us-central1` region respectively.



### Limitations

Consider the following functional boundaries when planning your encryption strategy:

  * **Instance creation requirement** : You can enable CMEK only on a new Google SecOps instance. You can't enable CMEK on an existing instance.
  * **SOAR migration dependency** : If your instance includes SOAR, confirm that your [SOAR instance is migrated](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#check-migration) to Google.com before rotating keys.



## Encryption at rest

Google SecOps encrypts customer data at rest by default. No additional action is required from you. Google Cloud services automatically encrypt data before it is written to disk.

Key characteristics of encryption at rest include:

  * **Encryption algorithm** : Data is encrypted using the 256-bit Advanced Encryption Standard (AES). For example, data for each Cloud Storage object is encrypted under AES.
  * **Key management** : Google owns and manages the keys used in default encryption at rest. Each encryption key is itself encrypted with a regularly rotated set of master keys.



For more information, see [Default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

## Encryption in transit

Data in transit to and within Google SecOps is encrypted to protect it from interception.

Key characteristics of encryption in transit include:

  * **Secure protocols** : Data in transit is encrypted using standard Secure Sockets Layer (SSL) or Transport Layer Security (TLS) protocols.



For more information, see [Encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit).

## Customer-managed encryption keys

For more control over your encryption keys, you can use customer-managed encryption keys (CMEK). CMEK is available for Google SecOps instances to fulfill specific security or compliance requirements.

Consider the following when using CMEK with Google SecOps:

  * You must configure CMEK when you create a new Google SecOps instance. You cannot enable CMEK on an existing instance.
  * Certain transient system-generated temporary files might briefly use standard platform encryption during data processing operations.
  * You are responsible for managing the lifecycle of your keys in [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service), including rotation and disablement.



To learn how to configure and manage CMEK for your instance, see [Configure CMEK](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops).

## Enable CMEK for a new instance

Follow these steps to configure CMEK when onboarding a new Google SecOps instance.

### Prepare your project and encryption key

To prepare your Google Cloud environment and create your encryption key, complete the following steps:

  1. [Configure a Google Cloud project for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project) and accept the provisioning invitation.
  2. [Create a Cloud KMS key](https://docs.cloud.google.com/kms/docs/create-key) in the region where you plan to host your Google SecOps instance.

**Caution:** If you select the `eu` or `us` multi-region for your instance without creating a secondary key in `europe-west1` or `us-central1`, provisioning fails due to regional colocation requirements. Create keys in both required locations before linking your instance.

### Link your instance and assign the key

To link your instance and grant key access, complete the following steps:

  1. [Create a new Google SecOps instance](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud) and select the CMEK key that you created.
  2. When prompted during instance creation, grant Google SecOps access to the Cloud KMS key.
  3. Optional: Configure a [key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) schedule for each key to minimize the impact of potential key compromise.



## Access advanced assets and references

Use the resources in this section to enforce organization-wide encryption policies and manage key governance.

### Organization policy constraints

You can enforce CMEK usage across your organization by applying the following constraints at the organization, folder, or project level:

  * `constraints/gcp.restrictNonCmekServices`: Requires services to use CMEK. When you add Google SecOps to this constraint, administrators must select a CMEK key during instance creation.
  * `constraints/gcp.restrictCmekCryptoKeyProjects`: Restricts the Google Cloud projects that can supply CMEK keys for Google SecOps.



For more information about applying these constraints, see [Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy) and [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

## Troubleshooting

This section outlines key lifecycle timelines and provides self-service fixes for common encryption and key management issues.

### Latency and limits

Consider the following operational timelines when managing CMEK keys:

  * **Key rotation grace period** : After rotating a key, wait two weeks after the rotation begins before you disable or destroy the previous CMEK version.
  * **Data deletion timeline** : If Google SecOps loses access to a key, it deletes the data after 30 days.

**Caution:** Don't disable keys that are in active use, as this can cause permanent data loss.
  * **Service recovery time** : After you restore access to a disabled or unreachable key, Google SecOps automatically resumes ingesting and processing new data, which can take up to two weeks to complete.




### Error remediation

Use this table to remediate common CMEK configuration and operational issues:

Issue | Description | Fix  
---|---|---  
**Instance provisioning blocked** | Provisioning fails when `constraints/gcp.restrictNonCmekServices` is enforced without a CMEK key. | Select a valid Cloud KMS key during new instance creation. For more information, see [Configure CMEK](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops).  
**Data ingestion and processing stopped** | Google SecOps can't read, write, or process data because the active CMEK key is disabled or unreachable. | Re-enable the key version in Cloud KMS or restore External Key Manager (EKM) connectivity within 30 days to prevent data deletion.  
**Key rotation data loss risk** | Disabling or destroying a previous CMEK key version before SOAR migration causes irrecoverable data loss. | Confirm that your [SOAR instance is migrated](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#check-migration) to Google.com before rotating keys, and wait two weeks before disabling old key versions.  
  
### Validation and testing

Monitor your Google Cloud logs to detect keys that become unavailable or unauthorized so that you can restore access before data deletion occurs. Before rotating any CMEK key, verify your SOAR migration status by following the steps in [Check migration status](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#check-migration).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
