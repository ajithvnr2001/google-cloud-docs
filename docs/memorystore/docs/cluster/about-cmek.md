---
url: https://docs.cloud.google.com/memorystore/docs/cluster/about-cmek/
title: About customer-managed encryption keys (CMEK) \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:02.011061+00:00
---

# About customer-managed encryption keys (CMEK)  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/about-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  About customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can use customer-managed encryption keys (CMEK) in [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) for your clusters in Memorystore for Redis Cluster. The document also outlines which data is encrypted in persistent storage and how your clusters behave during key lifecycle events.

CMEK lets you control the cryptographic keys that protect your stored data. By managing your own keys in Cloud KMS, you gain greater control over key access, rotation, and usage, which helps you meet strict compliance and regulatory requirements.

Implementing CMEK provides an additional layer of security and control over your persistent data, such as backups and persistence files. You can enable CMEK only on new clusters. You can't apply CMEK to existing clusters.

## Who should use CMEK?

CMEK is intended for organizations that have sensitive or regulated data, and require control over their own encryption keys. For more information about whether to use CMEK to encrypt this data, see [Choose where to use CMEK](https://docs.cloud.google.com/kms/docs/cmek-recommended-practices#choose_where_to_use_cmek).

## Customer-managed encryption

CMEK lets you use your cryptographic keys to protect stored data in clusters. To encrypt this data, Memorystore for Redis Cluster uses Google-managed data encryption keys (DEKs) and customer-managed key encryption keys (KEKs).

You can have the following levels of encryption:

  * **DEK encryption** : DEKs encrypt data in Memorystore for Redis Cluster.
  * **KEK encryption** : KEKs encrypt DEKs.



Memorystore for Redis Cluster uses KEKs to encrypt DEKs, and it uses DEKs to encrypt the stored data. If you use CMEK, then you can manage the KEKs that encrypt the DEKs in your cluster.

The following diagram shows how a cluster uses CMEK to encrypt data. Data that's uploaded to Google's storage infrastructure is chunked, and each chunk is encrypted with its own DEK. Cloud KMS provides the KEK to encrypt the DEKs, and Google's storage infrastructure distributes both the encrypted data chunks and the encrypted DEKs across the system.

![Data is uploaded to Google's storage infrastructure and divided into chunks. Each chunk is encrypted with its own DEK. The DEKs are then encrypted using a KEK that's retrieved from Cloud KMS. The encrypted chunks and encrypted DEKs are distributed across the storage infrastructure.](https://docs.cloud.google.com/static/memorystore/img/cmek2.png)

The following diagram shows how Memorystore for Redis Cluster decrypts data that's encrypted with CMEK. To access this encrypted data, Memorystore for Redis Cluster sends a request to Cloud KMS, which manages the KEK, to decrypt the DEK. Cloud KMS then returns the decrypted DEK, which the cluster uses to decrypt the stored data.

![Data chunk encrypted with DEK and stored with the encrypted DEK. A request to decrypt the DEK is sent to Cloud KMS, which stores the KEK. Cloud KMS returns the decrypted DEK.](https://docs.cloud.google.com/static/memorystore/img/cmekdecrypt.png)

## Which data is encrypted using CMEK?

CMEK encrypts the following types of customer data that are stored in persistent storage:

  * [Backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups): backups let you recover your data to a point in time, as well as export and analyze it. Backups are also useful for disaster recovery, data migration, data sharing, and compliance scenarios.
  * [Persistence](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview): Memorystore for Redis Cluster supports two types of persistence: 
    * **RDB persistence:** The Redis database (RDB) feature protects your data by saving snapshots of your data on durable storage.
    * **AOF persistence:** This feature prioritizes data durability. It stores data durably by recording every write command to a log file called the Append-Only File (AOF). If a system failure or restart occurs, then the server replays AOF file commands sequentially to restore your data.
  * Metadata related to security features like basic token-based authentication and in-transit encryption. For more information, see [Secure access to your clusters by using basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-basic-auth) and [About in-transit encryption](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption).



## CMEK components

The following sections describe the requirements and behaviors of the service accounts, cryptographic keys, key versions, and organization policies that make up your CMEK architecture.

### Service accounts

To create a CMEK-enabled cluster, you must grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role to the Memorystore for Redis Cluster service account that uses the following format:
    
    
    service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com
    

Granting this permission lets the service account request key access from Cloud KMS.

### Keys

In Cloud KMS, you need to create a key ring, and then create a cryptographic key that uses a symmetric encryption algorithm. When you create a cluster, you select this key to encrypt the cluster. You can create one project for both your keys and clusters, or different projects for each of them.

CMEK is available in all cluster locations. You must create the key ring and key in the same region where you want to create the cluster. For a multi-region cluster, you must set the key ring and key to the same location as the cluster. If the regions or locations don't match, then a request for creating the cluster fails.

For the resource ID of the key, CMEK uses the following format:
    
    
    projects/CMEK_ENABLED_PROJECT/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
    

For more information about finding the resource IDs of existing keys, see [Getting a Cloud KMS resource ID](https://docs.cloud.google.com/kms/docs/getting-resource-ids).

### External keys

As part of your CMEK strategy, you can use external keys. To do this, use [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) to encrypt data within Google Cloud by using external keys that you manage.

When you use a Cloud EKM key, Google has no control over the availability of your externally managed keys. If a key isn't available when you create your cluster, then Memorystore for Redis Cluster doesn't create the cluster. Furthermore, if the external key becomes unavailable at any point after you create the cluster, then Memorystore for Redis Cluster deactivates backups and persistence, but regular in-memory caching operations continue to serve traffic.

For more considerations about using external keys, see [Considerations](https://docs.cloud.google.com/kms/docs/ekm#considerations).

### Key versions

Cloud KMS stores the cryptographic key material that you use to encrypt and decrypt your data in a key version. A single key can contain multiple key versions. Whenever you rotate a key, you create a key version.

The following sections describe how your clusters and their protected data behave during key lifecycle events, such as disabling, destroying, rotating, enabling, or restoring key versions. The sections also explain the impact of revoking access to or replacing a Cloud KMS key, and provide guidance on manually re-encrypting data.

#### Disabling or destroying a CMEK key version

You might have situations where you want to make data that's encrypted with CMEK permanently inaccessible, such as when you're remediating a data spill. To achieve this high-assurance data destruction (also known as _crypto-shredding_), you destroy the key version. For more information about destroying key versions, see [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore).

**Important** : You have control over keys and data access. After you destroy a key version that's associated with a cluster, Google can't get the data back. Also, even though you disable or destroy the key version, the cluster continues to run read and write operations.

If you disable or destroy your primary key version, then the following conditions apply to backups and persistence.

##### Backups

When you destroy your primary key version, the following restrictions apply to your cluster's backups:

  * You can't create on-demand or automated backups. However, if you enable an older key version, then you can access any backups that you created using this key version.
  * You can't update or re-enable automated backups until you enable or restore the primary key version. For more information, see Enabling or restoring the primary CMEK key version.



##### Persistence

When you destroy your primary key version, the following restrictions apply to persistence for your cluster:

  * If you configure your cluster to use persistence, then Memorystore for Redis Cluster deactivates persistence when the key version becomes unavailable. You're no longer charged for using persistence.
  * Memorystore for Redis Cluster doesn't flush new data to persistent storage using the CMEK.
  * Memorystore for Redis Cluster can't read existing data that's present in the persistent storage.
  * You can't update or re-enable persistence until you enable or restore the primary key version.

**Important** : If you disable or destroy the primary key version, then the cluster is considered out of SLA. For more information, see the [Memorystore SLA](https://cloud.google.com/memorystore/sla).

If you enable your primary key version, but you disable or destroy an older key version, then the following conditions apply to backups and persistence:

  * You can create backups. However, if a backup is encrypted with an older key version that's disabled or destroyed, then the backup remains inaccessible.
  * If you enable persistence, then it remains enabled. If the older key version that's used in persistence is disabled or destroyed, then Memorystore for Redis Cluster performs an update that's similar to the one that's used in maintenance and re-encrypts the data with the primary key version.



#### Revoking access to a Cloud KMS key

If you revoke access to an active Cloud KMS key by either disabling the key or removing IAM permissions for the key, then Memorystore for Redis Cluster prioritizes the availability of the primary cache. Regular, in-memory caching operations continue to serve traffic.

However, backups and persistence are deactivated. Memorystore for Redis Cluster immediately stops writing new data to the disk and doesn't read data from the customer-encrypted disk into memory.

#### Rotating the primary CMEK key version

If you rotate your primary key version and create a new primary key version, then the following conditions apply to backups and persistence:

  * The latest primary key version of your CMEK encrypts new backups.
  * For existing backups, no re-encryption is done.
  * For persistence, the nodes don't take any action. The nodes continue to use the older key version until the next maintenance event.



#### Re-encrypting CMEK-protected data manually

Memorystore for Redis Cluster doesn't support on-demand re-encrypting of stored data. You can't trigger a process manually to use a new key version to re-encrypt existing backups or active persistence files. However, you can use the new key version to encrypt newly written data.

If you rotate a key and must force a cluster to use the new key version, then the following conditions apply to backups and persistence:

##### Backups

You can't re-encrypt existing backups. If compliance requires that all data must be encrypted with the newest key, create a backup that uses this key, and then delete existing backups manually. You can also export this backup to a Cloud Storage bucket so that the Cloud Storage encryption key is used.

**Caution** : If you disable or destroy the key versions that you used originally to encrypt the existing backups, then you can't recover the backups. For more information, see  Disabling or destroying a CMEK key version.

##### Persistence

To force the cluster to use a new Cloud KMS key, you can run simulated maintenance on the cluster. After you complete this operation, Memorystore for Redis Cluster can write persistence data by using the updated primary key version.

#### Replacing a protected Cloud KMS key

If you replace a protected Cloud KMS key with either a different key or a new primary key version, then Memorystore for Redis Cluster applies this change only to future operations.

Replacing a protected key impacts your resources in the following ways:

  * **Backups** : all subsequent backups are encrypted by using the new key. Existing backups maintain their original keys.
  * **Persistence** : the next time the cluster restarts or has a maintenance event, the new key is used.
  * **Primary cache** : replacing this key has no impact. CMEK doesn't encrypt in-memory data because this data isn't considered as stored data.



#### Enabling or restoring the primary CMEK key version

If you enable or restore your primary key version, then the following conditions apply to backups and persistence:

  * You can create on-demand and automated backups again.
  * Memorystore for Redis Cluster performs an update that's similar to the one used in maintenance and re-enables persistence.



### Organization policy constraints

Memorystore for Redis Cluster supports organization policy constraints for CMEK. By using these constraints, you can enforce CMEK protection for your clusters and limit which Cloud KMS keys you can use for this protection.

You can configure the following organization policy constraints:

  * `constraints/gcp.restrictNonCmekServices`: use this constraint to enforce CMEK protection for your clusters. If the [Memorystore for Redis Cluster API](https://docs.cloud.google.com/kms/docs/cmek-org-policy) is in the `Deny` policy list of services for this constraint, then you can't create non-CMEK-protected clusters.
  * `constraints/gcp.restrictCmekCryptoKeyProjects`: use this constraint to limit which Cloud KMS keys you can use for CMEK protection. If you configure this constraint, then the clusters that use CMEK encryption must use a key from an allowed project, folder, or organization.



Because both Memorystore for Redis Cluster and [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis) share the same endpoint (`redis.googleapis.com`), you can't enforce CMEK for clusters independently from Memorystore for Redis instances.

For more information about the CMEK-related organization policy constraints that Google manages for Memorystore for Redis Cluster, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

## Pricing

Memorystore for Redis Cluster bills for a CMEK-enabled cluster just like any other cluster; there are no additional costs. For more information, see [Memorystore for Redis Cluster pricing](https://docs.cloud.google.com/memorystore/docs/cluster/pricing).

You use the [Cloud KMS API](https://docs.cloud.google.com/kms/docs/reference/rest) to manage CMEK. When you create a cluster with CMEK, Memorystore uses the key periodically to encrypt data.

You're billed by Cloud KMS for the cost of the key and for encryption and decryption operations when Memorystore for Redis Cluster uses the key. For more information, see [Cloud KMS pricing](https://cloud.google.com/kms/pricing).

## Limitations

The following limitations apply when using CMEK with Memorystore for Redis Cluster:

  * You can't enable CMEK on an existing cluster.
  * The key, key ring, and cluster must be located in the same region.
  * You must use the symmetric encryption algorithm for your key.
  * Cloud KMS encryption and decryption rates are subject to a quota.



## What's next

  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek).
  * Learn how to [enhance data security by using CMEK](https://docs.cloud.google.com/memorystore/docs/cluster/use-cmek).
  * Learn more about [backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups).
  * Learn more about [persistence](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
