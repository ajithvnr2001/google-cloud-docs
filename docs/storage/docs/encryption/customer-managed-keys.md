---
url: https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys/
title: Customer-managed encryption keys \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:27:39.601865+00:00
---

# Customer-managed encryption keys  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

[Setup](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys)

By default, Cloud Storage encrypts customer content at rest. Cloud Storage handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Cloud Storage. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Cloud Storage resources is similar to using Google default encryption. For more information about CMEKs, see [ Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). To learn how to use manually-created CMEKs to protect your Cloud Storage resources, see [Use customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys).

For more information about other encryption options when using Cloud Storage, see [Data Encryption Options](https://docs.cloud.google.com/storage/docs/encryption).

## CMEK with Cloud KMS Autokey

You can either create CMEKs manually to protect your Cloud Storage buckets and the objects within them or use Cloud KMS Autokey. With Autokey, key rings and keys are generated on demand to support resource creation or update in Cloud Storage. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

Autokey doesn't create keys for objects. By default, objects in a bucket use the bucket default key. If you want to encrypt an object using a key other than the bucket default key, you can manually create a CMEK and use that key when creating the object.

To learn how to use CMEKs created by Cloud KMS Autokey to protect your Cloud Storage buckets and the objects within them, see [Using Autokey with Cloud Storage resources](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey#storage-autokey).

## When is the key used?

When you apply a CMEK to an object, Cloud Storage uses the key when encrypting:

  * The object's data.
  * The object's CRC32C checksum.
  * The object's MD5 hash.



Cloud Storage uses standard [server-side keys](https://docs.cloud.google.com/storage/docs/encryption/default-keys) to encrypt the remaining [metadata](https://docs.cloud.google.com/storage/docs/metadata) for the object, including the object's name. Thus, if you have sufficient [permission](https://docs.cloud.google.com/storage/docs/access-control), you can perform actions such as reading most metadata, listing objects, and deleting objects even after you've disabled or destroyed the associated CMEK.

**Note:** Because most metadata can be read regardless of encryption method, do not include sensitive information in your object and bucket metadata or names.

## Service agents

Each project has a special Cloud Storage service account called a _service agent_ that performs encryption and decryption with CMEKs. Once you [give the service agent access](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#service-agent-access) to an encryption key, that service agent encrypts:

  * Objects added to a bucket that [uses the key as the default key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#set-default-key).
  * Specific objects that you indicate should be [encrypted with that key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#add-object-key).



When adding or rewriting an object in Cloud Storage, if you have both a default key set on your bucket and a specific key included in your request, Cloud Storage uses the specific key to encrypt the object.

When a requester wants to read an object encrypted with a CMEK, they simply access the object as they normally would. During such a request, the service agent automatically decrypts the requested object as long as:

  * The service agent still has permission to decrypt using the key.
  * You have not disabled or destroyed the key.



If one of these conditions is not met, the service agent does not decrypt the data, and the request fails.

**Important:** There is a delay between when you [disable a key](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) and when that key no longer can be used to encrypt and decrypt objects. For information about the typical length of the delay and ways to effectively shorten it, see [Cloud KMS Resource Consistency](https://docs.cloud.google.com/kms/docs/consistency#key_versions).**Caution:** If you [destroy a key](https://docs.cloud.google.com/kms/docs/destroy-restore) that encrypts existing objects, you will be unable to recover that data, but you continue to be charged for storage of your objects until you delete them. If you destroy a key, use the object metadata field `kmsKeyName` to identify objects that used the destroyed key, and delete those objects.

## Restrictions

The following restrictions apply when using CMEKs:

  * You cannot encrypt an object with a CMEK by updating the object's metadata. Include the key as part of a rewrite of the object instead.

    * `gcloud storage` uses the `objects update` command to set encryption keys on objects, but the command rewrites the object as part of the request.
  * You must create the Cloud KMS key ring in the same location as the data you intend to encrypt. For example, if your bucket is located in `US-EAST1`, any key ring used for encrypting objects in that bucket must also be created in `US-EAST1`.

    * For [dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr), the Cloud KMS key ring location must match the dual-region's location code. For example, if your bucket is located in the configurable dual-region pair `US-EAST1`, `US-WEST1`, any key ring used for encrypting objects in that bucket must be created in the `US` multi-region, which matches this bucket's location code. If your bucket is located in the predefined dual-region `NAM4`, then you must create the key ring in the same predefined dual-region, `NAM4`.

For available Cloud KMS locations, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

  * The CRC32C checksum and MD5 hash of objects encrypted with CMEKs are not returned when [listing objects with the JSON API](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list).

    * When appropriate, some tools, such as `gcloud storage`, perform an additional metadata `GET` request on each object encrypted with a CMEK in order to retrieve the CRC32C and MD5 information. These additional requests can make listing substantially slower than listing objects encrypted with standard Cloud Storage encryption.
  * Only [symmetric encryption keys](https://docs.cloud.google.com/kms/docs/encrypt-decrypt) can be used as CMEKs.




### Cloud KMS quotas and Cloud Storage

When you use CMEK in Cloud Storage, your projects can consume Cloud KMS cryptographic requests quotas. 

Encryption and decryption operations using CMEK keys affect Cloud KMS quotas in these ways:

  * For software CMEK keys generated in Cloud KMS, no Cloud KMS quota is consumed.
  * For hardware CMEK keys—sometimes called Cloud HSM keys—encryption and decryption operations count against [Cloud HSM quotas](https://docs.cloud.google.com/kms/quotas#hsm) in the project that contains the key.
  * For external CMEK keys—sometimes called Cloud EKM keys—encryption and decryption operations count against [Cloud EKM quotas](https://docs.cloud.google.com/kms/quotas#ekm) in the project that contains the key.



For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

## Relation to customer-supplied encryption keys

In addition to customer-managed encryption, Cloud Storage offers [Customer-Supplied Encryption Keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) as a way of controlling your data encryption. You can encrypt different objects in a single bucket with different encryption methods, but note that:

  * A single object can only be encrypted by one of these methods at a time.

  * If you have a default CMEK set for your bucket and specify a customer-supplied key in a request, Cloud Storage uses the customer-supplied key to encrypt the object.




## Key management

This section discusses considerations when rotating keys, replacing keys, and disabling or destroying key versions.

### Key rotation

Cloud KMS supports both automatic and manual [key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) to a new [version](https://docs.cloud.google.com/kms/docs/object-hierarchy#key_version). After rotating a key, Cloud Storage uses the new version for all operations that encrypt using the key, such as:

  * Object uploads when the destination bucket uses the key as its default encryption key.

  * Object upload, copy, and rewrite operations that specifically use the key in the operation.




Previous versions of the key are not disabled or destroyed, so Cloud Storage can still decrypt existing objects that were previously encrypted using those versions.

### Key replacement

Use the following guidelines when replacing the key you use to encrypt Cloud Storage objects with a new key:

  1. [Check your buckets](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#view-default-key) to see which use the key as their default encryption key. For these buckets, replace the old key with a new key.

This ensures that all objects written to the bucket use the new key going forward.

  2. Inspect your source code to understand which requests use the key in ongoing operations, such as setting bucket configurations and uploading, copying, or rewriting objects. Update these instances to use the new key.

  3. [Check for objects](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#identify-object-key), in all of your buckets, encrypted with the old key. Use the [Rewrite Object method](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) to re-encrypt each object with the new key. To re-encrypt millions or billions of objects in bulk with a single job, use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview).

  4. [Disable](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) all versions of the old key. After disabling old key versions, monitor client and service logs for operations that fail due to a version becoming unavailable.




### Disabling or destroying a key version

**Caution:** Except in certain cases involving locked objects, you can destroy a Cloud KMS [key version](https://docs.cloud.google.com/kms/docs/object-hierarchy#key_version) even if it's actively being used to encrypt Cloud Storage objects. Permanent loss of data can occur if you destroy a key version that is still being used to encrypt objects.

  * When you [disable](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) or [destroy](https://docs.cloud.google.com/kms/docs/destroy-restore) a specific key version, you cannot decrypt any object that is currently encrypted with that key version.

For example, you cannot download, copy, or rewrite the object, and attempting to do so results in an error.

    * If you disable a key version, you can re-enable it. Once re-enabled, you can access objects that were encrypted by that key version.

    * If you destroy a key version, downloads of objects encrypted with that version are never possible again.

Before disabling or destroying a key version, you should [identify](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#identify-object-key) all objects, in all buckets, that were encrypted using the specific key version. Once identified, use the [Rewrite Object method](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) to re-encrypt each object using a new key version, a whole new key, or [server-side keys](https://docs.cloud.google.com/storage/docs/encryption/default-keys).

  * When you disable or destroy the [primary version](https://docs.cloud.google.com/kms/docs/object-hierarchy#key_version) of a key, you cannot use the key for encryption until you have a new primary version. For example, without a primary version:

    * You cannot specify the key as part of an object upload, copy, or rewrite.

    * You cannot upload, copy, or rewrite objects to a bucket that has the key set as its default encryption key **unless** you specify a different, valid key as part of the operation.

Once you have a primary version for your key, operations that use the key to encrypt objects succeed.

Before disabling or destroying a key version that is the primary version of the key, you should first stop using it as the primary version. You can do so by either:

    * Replacing it with a new primary version, typically by [performing a key rotation](https://docs.cloud.google.com/kms/docs/rotating-keys).
    * Removing instances where you use the key for encryption. When you do so, Cloud Storage uses [server-side keys](https://docs.cloud.google.com/storage/docs/encryption/default-keys) for encryption instead.

**Note:** Key disablement and destruction take effect after some time. [Cloud KMS documentation](https://docs.cloud.google.com/kms/docs/destroy-restore) contains detailed information about this behavior.

#### Key versions and locked objects

If a key version encrypts an object that is locked, either because the object is stored in a bucket with a [locked retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock) or because the object has its own [locked retention configuration](https://docs.cloud.google.com/storage/docs/object-lock), the key version can only be destroyed if the following conditions are met:

  * The encrypted object's _retention expiration time_ must be in the past.
  * The encrypted object must not have any [object holds](https://docs.cloud.google.com/storage/docs/object-holds) placed on it.



Once all relevant objects have met these conditions, it's possible to destroy the key version, even without deleting the objects. If you do so, affected object data becomes permanently inaccessible.

## What's next

  * [Set CMEKs](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys) on your Cloud Storage buckets and objects.
  * [Configure which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in your buckets.
  * Learn more about [encryption in Cloud Storage](https://docs.cloud.google.com/storage/docs/encryption).
  * Learn more about [Cloud KMS](https://docs.cloud.google.com/kms/docs/cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
