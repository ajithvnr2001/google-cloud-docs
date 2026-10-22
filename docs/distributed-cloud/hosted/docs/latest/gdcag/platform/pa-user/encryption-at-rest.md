---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/encryption-at-rest/
title: Encryption at rest \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:07.742083+00:00
---

# Encryption at rest  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/encryption-at-rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Encryption at rest Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped provides a comprehensive security strategy to help protect your data, featuring automatic encryption at rest. Encryption at rest is a security measure that prevents unauthorized access to data stored on non-volatile storage (storage that retains data even after losing power), such as disks (including solid-state drives) and backup media. GDC encrypts your content at rest, without requiring any action from you.

This document describes the default encryption at rest mechanisms in GDC and explains the Customer-Managed Encryption Keys (CMEK) feature, which lets you control the encryption keys protecting your stored data.

This document assumes a basic understanding of encryption and cryptographic data types, and is for audiences who manage security (such as IT admins or security engineers) within GDC. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Types of customer data protected

Customer data refers to data that customers or end users provide to GDC through the services under their account. GDC handles the following two categories of customer data:

  * **Customer content** : Data that you generate yourself or provide to GDC, such as stored data, disk snapshots, and Identity and Access Management (IAM) policies. Default encryption at rest, as described in this document, primarily protects customer content.

  * **Customer metadata** : All other customer data. Customer metadata can include auto-generated project numbers, timestamps, IP addresses, the byte size of an object, or the virtual machine type. GDC protects customer metadata to a degree that is reasonable for ongoing performance and operations.




## Benefits of encryption at rest

Encryption at rest has the following benefits:

  * Reduces the impact of unauthorized physical access to data stored on disks. Even if attackers gain physical access to storage devices, they can't read or decrypt the data without the encryption keys, as the disks only expose encrypted data.
  * Focuses the security strategy on key management. Because the data is encrypted, protecting the encryption keys is one important security measure for preventing unauthorized data access.
  * Provides an important privacy mechanism. When GDC encrypts data at rest, it limits the access that systems and engineers have to the data.



## Default encryption layers

GDC automatically encrypts all customer content stored at rest using multiple layers of encryption. This layered approach means a compromise at one layer is less likely to expose the data. These layers are implemented across the primary storage types used by customer workloads, including the following:

  * **Block Storage**

    * **Hardware-level encryption:** Utilizes FIPS 140-2 compliant Self-Encrypting Drives (SEDs). The encryption keys for these SEDs are stored in an external Hardware Security Module (HSM), providing FIPS 140-3 compliant storage.
    * **Software-level encryption:** Implements an additional layer called Volume Encryption (VE). Each block storage volume is encrypted with a unique XTS-AES-256 key. These volume-specific keys are also stored in the external HSM and managed as CMEKs.



## Customer-managed encryption keys

Customer-Managed Encryption Keys (CMEK) give you control over the keys that protect your data at rest in GDC. By default, all data stored within GDC is encrypted at rest using FIPS 140 validated cryptographic modules and HSM-backed keys, requiring no setup or configuration.

CMEKs offer the following advantages that can help you meet your compliance requirements:

  * **Control:** You control the keys, including the ability to delete them.
  * **Transparency:** You can audit access to the key to help ensure that your data is protected.
  * **Cryptographic erasure:** CMEK adoption enables this high-assurance data destruction method for data spill remediation and off-boarding. You can delete keys out-of-band of the data they protect.
  * **Centralized enforcement:** Centrally managed encryption keys create a single place to enforce access policies and audit key usage.



### Types of CMEK resources

CMEKs are encryption keys that the platform administrator group can monitor, audit, and delete. You manage these keys through Kubernetes resources using HSM APIs or the [Key Management System (KMS)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/kms).

There are two types of CMEK Kubernetes resources:

  * **`CTMKey`** : A Kubernetes resource created and managed directly within the HSM using the Thales CipherTrust Manager (CTM). You can manage `CTMKey` resources using `kubectl` to interact with the HSM API.

Services such as block storage use `CTMKey` resources as CMEKs.

  * **`AEADKey`** : A Kubernetes resource managed by the KMS. KMS lets you create and manage your own encryption and signing keys. KMS uses an HSM-backed root key to wrap the `AEADKey` material, ensuring it's encrypted at rest. While the root of trust is still the HSM, KMS provides an additional layer of key management. You manage `AEADKey` resources using `kubectl` to interact with the KMS API.

Services such as object storage bucket encryption use `AEADKey` resources as CMEKs.




### CMEK supported services in GDC

When you create resources that store data within GDC services, the services automatically generate the encryption keys that protect your data and make them available as CMEK resources.

**Warning:** Keys automatically generated by GDC services for CMEK are tied to the lifecycle of the corresponding resource. Don't use these keys for any other purpose (such as encrypting other data using KMS APIs). If you use such a key for other purposes, and the original resource is later deleted, the service might also delete the key, leading to permanent data loss for any other data encrypted with that key.

Only some services support CMEK rotation. Consult the documentation for each service for instructions on key rotation.

The following GDC services support CMEK:

  * **Block storage** : Encrypts each block storage device.
  * **Virtual machine (VM) disks** : Encrypts VM disks.
  * **Database service** : Encrypts data for your database instance. Note that backups for your database are out of scope for CMEK and are instead encrypted using the backup storage system's settings.
  * **User container workloads** : Encrypts the Kubernetes metadata and the `etcd` cluster. Persistent volumes (PVs) used by container workloads are encrypted as part of block storage encryption.
  * **Storage** : Encrypts each object with a unique AES-256-GCM key, wrapped by a bucket-level KMS AEAD key.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
