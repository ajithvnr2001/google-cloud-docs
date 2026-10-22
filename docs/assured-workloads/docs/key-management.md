---
url: https://docs.cloud.google.com/assured-workloads/docs/key-management/
title: Supporting compliance with key management \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:08.287083+00:00
---

# Supporting compliance with key management  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/key-management/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supporting compliance with key management

This page provides information about supporting compliance with key management using encryption for Assured Workloads.

## Overview

[Encryption key management](https://docs.cloud.google.com/assured-workloads/docs/encryption-keys) is fundamental to supporting regulatory compliance of Google Cloud resources. Assured Workloads supports compliance through encryption in the following ways.

**CJIS, ITAR, and IL5:** Mandated customer-managed keys and separation of duties:

  * **CMEK** : Assured Workloads mandates the use of customer-managed encryption keys (CMEK) to support these control packages.
  * **Key management project** : Assured Workloads creates a key management project to align with NIST 800-53 security controls, the [key management project](https://docs.cloud.google.com/assured-workloads/docs/key-concepts#key_management) is separated from resource folders to establish [separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties) between security administrators and developers.
  * **Key ring** : Assured Workloads also creates a [key ring](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_rings) to store your keys. The CMEK project restricts key ring creation to compliant locations that you select. After you create the key ring, you manage creating or importing encryption keys. Strong encryption, key management, and separation of duties all support positive security and compliance outcomes on Google Cloud.

**Note:** After Assured Workloads creates the key ring, you must [create your CMEK key](https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek). Unless your control package mandates a certain encryption key strategy, you can use any Google key management service, including Cloud Key Management Service, Cloud External Key Manager, or CMEK. You can also use default [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/kms/docs/key-management-service), which are FIPS validated.



**Other control packages (including IL4):** Google-owned and Google-managed encryption keys and other encryption options:

  * [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/default-keys) provides on-by-default, FIPS 140-2 validated encryption in transit and at rest to all Google Cloud services.
  * [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs): Assured Workloads supports Cloud KMS. Cloud KMS covers all Google Cloud products and services by default providing FIPS 140-2 validated encryption-in-transit and encryption-at-rest.
  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek): Assured Workloads supports CMEK for control packages such as IL4, for which CMEK is optional.
  * [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) Assured Workloads supports Cloud EKM.
  * [Key import](https://docs.cloud.google.com/kms/docs/importing-a-key)



## Encryption strategies

This section describes Assured Workloads encryption strategies.

### Assured Workloads CMEK Creation

**Note:** Assured Workloads only provides configuration guidance for CMEK when you select the CJIS control package.

CMEK lets you have advanced controls over your data and key management by enabling you to manage your complete key lifecycle, from creation to deletion. This capability is critical to supporting cryptographic erase requirements in the [Cloud Computing SRG](https://rmf.org/wp-content/uploads/2018/05/Cloud_Computing_SRG_v1r3.pdf).

## Services

### CMEK-integrated services

CMEK covers the following services, which store customer data for CJIS.

  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Persistent Disk](https://cloud.google.com/persistent-disk)
  * [BigQuery](https://docs.cloud.google.com/bigquery)

**Note:** After you setup CMEK, the resource ID of the key(s) you create in the CMEK project will need to be shared with developers working in the Assured Workloads resource folder(s). Today CMEK integration is limited to the in-scope services which support CMEK capabilities.

#### Other services: Custom Key Management

For services that aren't integrated with CMEK, or for customers whose control packages don't require CMEK, Assured Workloads customers have the option to use Google-managed [Cloud Key Management Service](https://docs.cloud.google.com/kms) keys. This option is offered in order to provide customers with additional options for key management to fit your organizational needs. Today, CMEK integration is limited to the [in-scope services](https://docs.cloud.google.com/kms/docs/using-other-products#cmek_integrations) which support CMEK capabilities. Google-managed KMS is an acceptable encryption method as it covers all Google Cloud products and services by default providing [FIPS 140-2 validated](https://cloud.google.com/security/compliance/fips-140-2-validated) encryption in transit and at rest.

For other products supported by Assured Workloads, see [Supported products by control package](https://docs.cloud.google.com/assured-workloads/docs/supported-products).

## Key management roles

Administrators and developers typically support compliance and security best practices through key management and [separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties). For example, while developers might have access to the Assured Workloads resources folder, administrators have access to the CMEK key management project.

### Administrators

Administrators typically control access to the encryption project and the key resources within it. The administrators are responsible for allocating key resource IDs to developers to encrypt resources. This practice separates the management of keys from the development process and provides the security administrators with the ability to manage encryption keys centrally in the CMEK project.

Security administrators can use the following encryption key strategies with Assured Workloads:

  * [Cloud KMS](https://docs.cloud.google.com/kms/docs)
  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek)
  * [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm)
  * [Key import](https://docs.cloud.google.com/kms/docs/importing-a-key)

**Note:** It is recommended that you create resources in the Assured Workloads resource project and not in the key management project.

### Developers

During development, when you provision and configure in-scope Google Cloud resources that require a CMEK encryption key, you request the resource ID of the key from your administrator. If you don't use CMEK, we recommend that you use Google-owned and Google-managed encryption keys to ensure data is encrypted.

The request method is determined by your organization as part of your documented security processes and procedures.

## What's next

  * Learn how to [create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder).
  * Learn which [products are supported](https://docs.cloud.google.com/assured-workloads/docs/supported-products) for each control package.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
