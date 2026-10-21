---
url: https://docs.cloud.google.com/memorystore/docs/redis/about-cmek/
title: About customer-managed encryption keys (CMEK) \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:53.194268+00:00
---

# About customer-managed encryption keys (CMEK)  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/about-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  About customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can use customer-managed encryption keys (CMEK) in [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) for your Memorystore for Redis instances. The document also outlines which data is encrypted in persistent storage and how your instances behave during key lifecycle events.

CMEK lets you control the cryptographic keys that protect your stored data. By managing your own keys in Cloud KMS, you gain greater control over key access, rotation, and usage, which helps you meet strict compliance and regulatory requirements.

Implementing CMEK provides an additional layer of security and control over your persistent data, such as backups and persistence files. You can enable CMEK only on new instances. You can't apply CMEK to existing instances.

## Who should use CMEK?

CMEK is intended for organizations that have sensitive or regulated data, and require control over their own encryption keys. For more information about whether to use CMEK to encrypt this data, see [Choose where to use CMEK](https://docs.cloud.google.com/kms/docs/cmek-recommended-practices#choose_where_to_use_cmek).

## Customer-managed encryption

CMEK lets you use your cryptographic keys to protect stored data in instances. To encrypt this data, Memorystore for Redis uses Google-managed data encryption keys (DEKs) and customer-managed key encryption keys (KEKs).

You can have the following levels of encryption:

  * **DEK encryption** : DEKs encrypt data in Memorystore for Redis.
  * **KEK encryption** : KEKs encrypt DEKs.



Memorystore for Redis uses KEKs to encrypt DEKs, and it uses DEKs to encrypt the stored data. If you use CMEK, then you can manage the KEKs that encrypt the DEKs in your instance.

The following diagram shows how an instance uses CMEK to encrypt data. Data that's uploaded to Google's storage infrastructure is chunked, and each chunk is encrypted with its own DEK. Cloud KMS provides the KEK to encrypt the DEKs, and Google's storage infrastructure distributes both the encrypted data chunks and the encrypted DEKs across the system.

![Data is uploaded to Google's storage infrastructure and divided into chunks. Each chunk is encrypted with its own DEK. The DEKs are then encrypted using a KEK that's retrieved from Cloud KMS. The encrypted chunks and encrypted DEKs are distributed across the storage infrastructure.](https://docs.cloud.google.com/static/memorystore/img/cmek2.png)

The following diagram shows how Memorystore for Redis decrypts data that's encrypted with CMEK. To access this encrypted data, Memorystore for Redis sends a request to Cloud KMS, which manages the KEK, to decrypt the DEK. Cloud KMS then returns the decrypted DEK, which the instance uses to decrypt the stored data.

![Data chunk encrypted with DEK and stored with the encrypted DEK. A request to decrypt the DEK is sent to Cloud KMS, which stores the KEK. Cloud KMS returns the decrypted DEK.](https://docs.cloud.google.com/static/memorystore/img/cmekdecrypt.png)

## Which data is encrypted using CMEK?

CMEK encrypts the following types of customer data that are stored in persistent storage:

  * [Backups](https://docs.cloud.google.com/memorystore/docs/redis/about-importing-exporting): backups let you recover your data to a point in time, as well as export and analyze it. Backups are also useful for disaster recovery, data migration, data sharing, and compliance scenarios.
  * [Persistence](https://docs.cloud.google.com/memorystore/docs/redis/about-rdb-snapshots): Memorystore for Redis supports Redis Database (RDB) persistence, which lets you save snapshots of your data on durable storage.
  * Metadata related to security features like `AUTH` and in-transit encryption. For more information, see [About Redis AUTH](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview) and [About in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption).



## CMEK components

The following sections describe the requirements and behaviors of the service accounts, cryptographic keys, key versions, and organization policies that make up your CMEK architecture.

### Service accounts

To create a CMEK-enabled instance, you must grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role to the Memorystore for Redis service account that uses the following format:
    
    
    service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com
    

Granting this permission lets the service account request key access from Cloud KMS.

### Keys

In Cloud KMS, you need to create a key ring, and then create a cryptographic key that uses a symmetric encryption algorithm. When you create a Memorystore for Redis instance, you select this key to encrypt the instance. You can create one project for both your keys and instances, or different projects for each of them.

CMEK is available in all Memorystore for Redis instance locations. You must create the key ring and key in the same region where you want to create the instance. A key for a multi-region or global region doesn't work. If the regions or locations don't match, then a request for creating the instance fails.

For the resource ID of the key, CMEK uses the following format:
    
    
    projects/CMEK_ENABLED_PROJECT/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
    

For more information about finding the resource IDs of existing keys, see [Getting a Cloud KMS resource ID](https://docs.cloud.google.com/kms/docs/getting-resource-ids).

**Warning** : Avoid disabling or destroying any version of the key that Memorystore for Redis uses to encrypt the instance. If Memorystore for Redis can't access any key version being used (for example, if you disable all key versions), then Memorystore for Redis suspends the instance.

In the Google Cloud console, a suspended instance shows a red exclamation mark tooltip on the _Instances_ page. If you hover over the tooltip, then a `No state` status appears. After the key becomes accessible, Memorystore for Redis resumes the instance automatically.

### External keys

As part of your CMEK strategy, you can use external keys. To do this, use [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) to encrypt data within Google Cloud by using external keys that you manage.

When you use a Cloud EKM key, Google has no control over the availability of your externally managed keys. If a key isn't available when you create your instance, then Memorystore for Redis doesn't create the instance. Furthermore, if the external key becomes unavailable at any point after you create the instance, then Memorystore for Redis suspends the instance until access is restored.

For more considerations about using external keys, see [Considerations](https://docs.cloud.google.com/kms/docs/ekm#considerations).

### Key versions

Cloud KMS stores the cryptographic key material that you use to encrypt and decrypt your data in a key version. A single key can contain multiple key versions. Whenever you rotate a key, you create a key version.

The following sections describe how your instances and their protected data behave during key lifecycle events, such as disabling, destroying, enabling, or restoring key versions. The sections also explain the impact of replacing a Cloud KMS key, provide guidance on manually re-encrypting data, and detail how to import or export data for a CMEK-enabled instance.

#### Disabling or destroying a CMEK key version

You might have situations where you want to make data that's encrypted with CMEK permanently inaccessible, such as when you're remediating a data spill. To achieve this high-assurance data destruction (also known as _crypto-shredding_), you destroy the key version. For more information about destroying key versions, see [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore).

If you want to ensure no data access to your instance, then disable your primary key version. This suspends your instance. Also, if any CMEK that's in use is disabled or destroyed, then Memorystore for Redis suspends the instance. This includes any older key version that the instance uses.

To see if Memorystore for Redis suspended your instance, use one of the following interfaces:

  * **Google Cloud console** : on the **Instances** page, a red exclamation mark tooltip appears next to your instance. If you hover over the tooltip, then a **No state** status appears.
  * **gcloud CLI** : use the [`gcloud redis instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/describe) command. Check the `state` field; a suspended instance doesn't display a `READY` or `REPAIRING` state.

**Important** : You have control over your keys and data access. If you disable a key version, then you can restore access later to resume the instance. However, after you destroy a key version, then the data is permanently inaccessible and Google can't recover the data. To recover from destroying a key version, you must create a new instance and import a backup. For more information, see [Import data to a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/import-data).

#### Replacing a protected Cloud KMS key

If you replace a protected Cloud KMS key with either a different key or a new primary key version, then Memorystore for Redis applies this change only to future operations.

Replacing a protected key impacts your resources in the following ways:

  * **Backups** : Memorystore for Redis exports backups to Cloud Storage. Therefore, the destination bucket's encryption settings (not the instance's CMEK) controls how the exported data is encrypted.
  * **Persistence** : the next time the instance restarts or has a maintenance event, the new key is used.
  * **Primary cache** : replacing this key has no impact. CMEK doesn't encrypt in-memory data because this data isn't considered as data at rest.

**Important** : If you revoke access to an active key by either disabling the key or removing its IAM permissions, then Memorystore for Redis suspends the instance.

#### Re-encrypting CMEK-protected data manually

Memorystore for Redis doesn't support on-demand rewrapping of existing data at rest. You can't trigger a process manually to use a new key version to re-encrypt existing backups or active persistence files. However, you can use the new key version to encrypt newly written data.

#### Importing or exporting data for a CMEK-enabled instance

If you want your exported data to remain protected by a CMEK, then you must configure CMEK on the destination Cloud Storage bucket before you export data to it. If your data is already stored on a CMEK-enabled instance, then there are no special requirements or restrictions for importing that data into a new instance. For more information, see [About importing and exporting data](https://docs.cloud.google.com/memorystore/docs/redis/import-export-overview).

#### Enabling or restoring the primary CMEK key version

If you enable or restore your primary key version, then Memorystore for Redis resumes your instance automatically.

### Organization policy constraints

Memorystore for Redis supports organization policy constraints for CMEK. By using these constraints, you can enforce CMEK protection for your instances and limit which Cloud KMS keys you can use for this protection.

You can configure the following organization policy constraints:

  * `constraints/gcp.restrictNonCmekServices`: use this constraint to enforce CMEK protection for your instances. If the [Memorystore for Redis API](https://docs.cloud.google.com/kms/docs/cmek-org-policy) is in the `Deny` policy list of services for this constraint, then you can't create non-CMEK-protected instances.
  * `constraints/gcp.restrictCmekCryptoKeyProjects`: use this constraint to limit which Cloud KMS keys you can use for CMEK protection. If you configure this constraint, then the instances that use CMEK encryption must use a key from an allowed project, folder, or organization.



Because both Memorystore for Redis and [Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster) share the same endpoint (`redis.googleapis.com`), you can't enforce CMEK for instances independently from clusters in Memorystore for Redis Cluster.

For more information about the CMEK-related organization policy constraints that Google manages for Memorystore for Redis, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

## Pricing

Memorystore for Redis bills for a CMEK-enabled instance just like any other instance; there are no additional costs. For more information, see [Memorystore for Redis pricing](https://docs.cloud.google.com/memorystore/docs/redis/pricing).

You use the [Cloud KMS API](https://docs.cloud.google.com/kms/docs/reference/rest) to manage CMEK. When you create an instance with CMEK, Memorystore uses the key periodically to encrypt data.

You're billed by Cloud KMS for the cost of the key and for encryption and decryption operations when Memorystore for Redis uses the key. For more information, see [Cloud KMS pricing](https://cloud.google.com/kms/pricing).

## Limitations

The following limitations apply when using CMEK with Memorystore for Redis:

  * You can't enable CMEK on an existing instance.
  * The key, key ring, and instance must be located in the same region.
  * You must use the symmetric encryption algorithm for your key.
  * Cloud KMS encryption and decryption rates are subject to a quota.



## What's next

  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek).
  * Learn how to [enhance data security by using CMEK](https://docs.cloud.google.com/memorystore/docs/redis/use-cmek).
  * Learn more about [backups](https://docs.cloud.google.com/memorystore/docs/redis/about-importing-exporting).
  * Learn more about [persistence](https://docs.cloud.google.com/memorystore/docs/redis/about-rdb-snapshots).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
