---
url: https://docs.cloud.google.com/kms/docs/hsm-for-workspace/
title: Cloud HSM for Google Workspace \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:27.861168+00:00
---

# Cloud HSM for Google Workspace  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/hsm-for-workspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Cloud HSM for Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

Cloud HSM for Google Workspace is an encryption key service that provides [client-side encryption (CSE)](https://support.google.com/a/answer/10741897) for Google Workspace.

Cloud HSM is a highly available, fully managed key management service operated at cloud scale with hardware-backed keys stored in FIPS 140-2 Level 3 compliant hardware security modules (HSMs). Cloud HSM for Google Workspace is available in the United States and Europe.

Using Google Workspace CSE adds another layer of encryption to your organization's data, including files and emails, in addition to the default encryption that Google Workspace provides. CSE is especially beneficial for organizations that store sensitive or regulated data, like intellectual property, healthcare records, or financial data. Cloud HSM for Google Workspace lets you have greater control over your encryption keys, and can help you meet regulatory and compliance requirements.

CHGWS is compatible with both Multi-tenant Cloud HSM keys and Single-tenant Cloud HSM keys.

## How Cloud HSM for Google Workspace works

Cloud HSM for Google Workspace uses [envelope encryption](https://docs.cloud.google.com/kms/docs/envelope-encryption) to protect your Google Workspace data such as files and emails. Protected data can only be encrypted and decrypted by authorized users according to your identity provider (IdP). All wrap and unwrap operations using Cloud HSM keys are performed inside the HSM. The key material never leaves the HSM protection boundary.

## Features and benefits

**Secure and standards-aligned** : Cloud HSM is built for customers who want to run cloud workloads that meet stringent security and regulatory standards. Cloud HSM uses FIPS 140-2 Level 3 validated Marvell LiquidSecurity HSMs. The Cloud HSM service has obtained compliance with numerous regulations and certifications including the following:

  * [FedRAMP](https://cloud.google.com/security/compliance/fedramp)
  * [DISA IL5](https://cloud.google.com/security/compliance/disa#services-in-scope)
  * [ITAR](https://cloud.google.com/security/compliance/itar)
  * [SOC 1](https://cloud.google.com/security/compliance/soc-1)
  * [SOC 2](https://cloud.google.com/security/compliance/soc-2)
  * [SOC 3](https://cloud.google.com/security/compliance/soc-3)
  * [HIPAA](https://cloud.google.com/security/compliance/hipaa-compliance)
  * [PCI DSS](https://cloud.google.com/security/compliance/pci-dss)



These compliance standards and certifications help customers in highly regulated market segments meet their regulatory and compliance needs for key management and data protection.

**Flat pricing** : Cloud HSM for Google Workspace offers flat pricing. Your costs don't change based on the number of users. For more information about pricing, see [Cloud Key Management Service pricing](https://docs.cloud.google.com/kms/pricing).

**Audit logs using Cloud Logging** : Like all Google Cloud services, Cloud HSM service writes audit logs that record administrative activities and accesses within your Google Cloud resources. Audit logs help you determine who did what and when. Enabling audit logs helps your security, auditing, and compliance entities monitor Google Cloud data and systems for possible vulnerabilities or external data misuse. For more information about audit logging, see [Cloud Key Management Service audit logging](https://docs.cloud.google.com/kms/docs/audit-logging).

## What's next

  * [Onboard to Cloud HSM for Google Workspace](https://docs.cloud.google.com/kms/docs/onboard-hsm-workspace).
  * Review the [best practices for Cloud HSM for Google Workspace](https://docs.cloud.google.com/kms/docs/hsm-for-workspace-best-practices).
  * Learn how [Cloud HSM](https://docs.cloud.google.com/docs/security/cloud-hsm-architecture#regulatory-compliance) can help you meet security and regulatory compliance requirements.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
