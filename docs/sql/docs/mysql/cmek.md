---
url: https://docs.cloud.google.com/sql/docs/mysql/cmek/
title: About customer-managed encryption keys (CMEK) \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:53.570520+00:00
---

# About customer-managed encryption keys (CMEK)  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  About customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/cmek "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/cmek "View this page for the SQL Server database engine")

By default, Cloud SQL for MySQL encrypts customer content at rest. Cloud SQL for MySQL handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Cloud SQL for MySQL. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Cloud SQL for MySQL resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## CMEK with Cloud KMS Autokey

You can either create CMEKs manually to protect your Cloud SQL for MySQL resources or use Cloud KMS Autokey. With Autokey, key rings and keys are generated on demand to support resource creation in Cloud SQL for MySQL. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

Autokey doesn't create keys for Cloud SQL for MySQL `BackupRun` resources. When you create a backup of a Cloud SQL for MySQL instance, the backup is encrypted with the primary instance's customer-managed key.

Cloud SQL for MySQL is only compatible with Cloud KMS Autokey when creating resources using Terraform or the REST API.

To learn how to use manually-created CMEKs to protect your Cloud SQL for MySQL resources, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek).

To use CMEKs created by Cloud KMS Autokey to protect your Cloud SQL for MySQL resources, use the steps provided for Secret Manager at [Using Autokey with Secret Manager resources](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey#secret-manager-autokey) as an example.

## Google-managed encryption versus customer-managed encryption

The diagrams below show how [data-at-rest encryption](https://docs.cloud.google.com/security/encryption/default-encryption) works inside a Cloud SQL instance when using default Google encryption versus customer-managed encryption keys.

### Without CMEK

![Data is uploaded to Google, then chunked and each chunk is encrypted with its own data encryption key. Data Encryption keys are wrapped using a key encryption key. With default Google Encryption, the key encryption key is retrieved from Google's internal Keystore. Encrypted chunks and wrapped encryption keys are distributed across Google's storage infrastructure.](https://docs.cloud.google.com/sql/images/cmek1.png)

### With CMEK

![Data is uploaded to Google, then chunked and each chunk is encrypted with its own data encryption key. Data Encryption keys are wrapped using a key encryption key. With CMEK using Cloud KMS, the key encryption key is retrieved from Cloud KMS. Encrypted chunks and wrapped encryption keys are distributed across Google's storage infrastructure.](https://docs.cloud.google.com/sql/images/cmek2.png)

When decrypting data wrapped with customer-managed encryption keys, Cloud SQL uses the KEK to decrypt the DEK and the unencrypted DEK to decrypt data-at-rest.

![Data chunk encrypted with DEK and stored with wrapped DEK. A request to unwrap the DEK is sent to KMS storage, which stores the unexportable KEK. KMS Storage returns the unwrapped DEK.](https://docs.cloud.google.com/sql/images/cmekdecrypt.png)

**Note:** Customer-managed encryption keys differ from Customer-Supplied Encryption Keys (CSEK), which let you specify the _contents_ of the encryption key. Customer-managed encryption keys let you create and manage a key using Cloud KMS, and assign keys to specific resources across Google Cloud. Cloud SQL does not support CSEK.

## When does Cloud SQL interact with CMEK keys?

**Operation** | **Notes**  
---|---  
Instance creation  | During instance creation, you configure the instance to use customer- managed encryption keys.   
Backup creation  | During backups for a CMEK-enabled instance, customer-managed encryption keys encrypt user data, such as user queries and responses. Backups from a CMEK-enabled instance inherit its encryption with same Cloud KMS key as the source instance. For enhanced backups, Backup and DR Service uses the CMEK inherited from the instance, not the CMEK configured on the backup vault.   
Instance restore  | During restores for a CMEK-enabled instance, Cloud SQL uses the key to access data on the backup instance being restored. When restoring to a different instance, the target instance can use a different key for encryption.   
Replica creation  | When you create a read or failover replica of a Cloud SQL instance in the same region, it inherits the CMEK from the parent instance. If you create a read or failover replica in a different region, you must select a CMEK from the other region. Each region uses its own set of keys.   
Clone creation  | Clones from a CMEK-enabled instance inherit CMEK encryption with same Cloud KMS key as the source instance.   
Instance update  | During updates to a CMEK-enabled instance, Cloud SQL checks the CMEK key.   
  
## What locations support CMEK-enabled Cloud SQL instances?

CMEK is available in all Cloud SQL [instance locations](https://docs.cloud.google.com/sql/docs/mysql/locations).

**Note:** The Cloud KMS key ring location must match the region where you want to create a Cloud SQL instance. A multi-region or global region key **will not** work. A request for creating a Cloud SQL instance fails if the regions don't match.

## About service accounts

When your Cloud SQL instances have CMEK enabled, you need to use a service account to request key access from Cloud KMS.

To use a customer-managed encryption key on a project, you must have a service account and you must grant the customer-managed encryption key access to the service account. The service account must exist inside of the project. The service account is visible in all regions.

If you use the Console to create an instance, Cloud SQL automatically creates the service account when you first choose the **Customer-managed key** option (if a service account does not already exist). You don't need to have special permissions on your user account when Cloud SQL automatically creates the service account.

## About keys

In Cloud KMS, you need to create a key ring with a cryptographic key, set with a location. When you create a new Cloud SQL instance, you select this key to encrypt the instance.

You need to know the key ID and key region when you create new Cloud SQL instances that use customer-managed encryption keys. You must put new Cloud SQL instances in the same region as the customer-managed encryption key associated with the instance. You can create one project for both keys and Cloud SQL instances, or different projects for each.

Customer-managed encryption keys use the following format:
    
    
    projects/[KMS_PROJECT_ID]/locations/[LOCATION]/keyRings/[KEY_RING]/cryptoKeys/[KEY_NAME]
    

If Cloud SQL is unable to access the key (such as if you disable the key version), Cloud SQL suspends the instance. Once the key becomes accessible again, Cloud SQL automatically resumes the instance. However, this can take up to 10 minutes because of the associated internal validation process. 

When you rotate keys, instances that are encrypted with that key aren't automatically re-encrypted with the new primary key version. You can re-encrypt any existing CMEK primary instance or replica with the new primary key version. For most instances, re-encryption causes zero downtime. For more information about how to re-encrypt a Cloud SQL instance or replica after a key rotation, see [Re-encrypt an existing CMEK-enabled instance or replica](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#reencrypt).

**Note:** Automated and manual backups use the latest primary key version. **Warning:** Never destroy the key version that you initially used to encrypt your instance. If you destroy it, you also destroy the backups created from the instance, because the key is used to decrypt the backup. Even when the key version is rotated, you must maintain the original key. If it is destroyed, it can't be re-created. You must also never destroy the key version that was used when creating the backup. 

### External key managers

You can use keys stored in supported external key managers as your customer-managed encryption keys. To learn how to use external keys with Cloud KMS, and to see a list of compatible EKMs, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

### Key Access Justifications

You can use Key Access Justifications as part of Cloud EKM. Key Access Justifications enable you to view the reason for each Cloud EKM request. Additionally, based on the justification provided, you can automatically approve or deny a request. To learn more, see the [Key Access Justifications overview](https://docs.cloud.google.com/cloud-provider-access-management/key-access-justifications/docs/overview).

Thus, Key Access Justifications provides extra control over your data by providing a justification for each attempt to decrypt the data.

For related information about using your keys with Cloud SQL instances, see [Creating a Cloud SQL instance with CMEK](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#createcmekinstance).

## How do I make CMEK-encrypted data permanently inaccessible?

**Warning:** You have complete control over keys and data access. Once you destroy a key version that is associated with a Cloud SQL instance, Google can't get the data back. However, if you disable the key version, you can re-enable it to get the data back.

You might have situations where you want to permanently destroy data encrypted with CMEK. To do this, you destroy the customer-managed encryption key version. You can destroy individual key versions or destroy all key versions for a key.

## Revoking key access for CMEK-encrypted enhanced backups

To backup and restore CMEK-enabled enhanced backups, you must maintain access to the CMEK used by the instance from both the Cloud SQL service agent and the Backup and DR Service service agent. This section explains how backup and restore functionality is affected by revoking key access.

  * **Revoke access from the Cloud SQL service agent** : If the Cloud SQL service agent loses access to the CMEK, your instance is suspended, and new backups can't be created. However, since the Backup and DR service agent has its own access to the CMEK, your existing enhanced backups can still be restored.

  * **Revoke access from the Backup and DR service agent** : If the Backup and DR service agent loses access to the CMEK, your instance remains usable, but new enhanced backups can't be created, and existing enhanced backups can't be restored until access to the key is restored to the Backup and DR service account.

  * **Disable the key version** : If the key version that was used to encrypt an enhanced backup is disabled, then that backup can't be restored unless the key is re-enabled. Enhanced backups encrypted using a key version that has been destroyed become permanently unrestorable. However, as long as the key contains an active primary key version, your instance can continue to create new backups.




## How do I export and import data from and to a CMEK-enabled instance?

If you want your data to remain encrypted with a customer-managed key during an export or import, you must set a customer-managed encryption key on the Cloud Storage bucket before exporting data to it. There are no special requirements or restrictions to importing data to a new instance when the data was previously stored on an instance enabled with a customer-managed encryption key.

## Restrictions

The following restrictions apply when using customer-managed encryption keys:

  * You can't enable customer-managed encryption keys on an existing instance.
  * You can't assign a different key to a replica in the same region as the primary instance. For cross-region replicas, you need to create a new key for the replica region.
  * You can't assign a different key to a clone.
  * You can't use customer-managed encryption keys to encrypt: 
    * External servers (external primary instances and external replicas)
    * Instance metadata, such as the instance ID, database version, machine type, flags, backup schedule, etc.
  * You can't use customer-managed encryption keys to encrypt user data in transit, such as user queries and responses.
  * After you create a Cloud SQL instance, you can't change the encryption key type. You can't switch from a Google-owned and Google-managed encryption key to a Cloud Key Management Service (Cloud KMS) key, or the other way around.



## What's next

  * Learn about [encryption at rest in Google Cloud](https://docs.cloud.google.com/security/encryption/default-encryption).
  * Learn how to [create an instance with CMEK enabled](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek).
  * Learn about [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs/key-management-service).
  * Learn about [Quotas for Cloud KMS resources](https://docs.cloud.google.com/kms/quotas#quotas_all).
  * Learn about [IAM service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).
  * Learn how to add [key access justifications](https://docs.cloud.google.com/cloud-provider-access-management/key-access-justifications/docs/overview) to your keys.
  * Find [other products](https://docs.cloud.google.com/kms/docs/using-other-products) that use CMEK.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
