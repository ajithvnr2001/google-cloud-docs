---
url: https://docs.cloud.google.com/kms/docs/resource-hierarchy/
title: Cloud KMS resources \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:50.884598+00:00
---

# Cloud KMS resources  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/resource-hierarchy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Cloud KMS resources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes each type of resource in Cloud KMS. Cloud KMS resources can't be moved to a different location after they are created. You can learn more about the [hierarchy of resources](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#resource_hierarchy).

## Keys

A Cloud KMS key is a named object containing one or more key versions, along with metadata for the key. A key exists on exactly one key ring tied to a specific location.

You can allow and deny access to keys using Identity and Access Management (IAM) [permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles). You can't manage access to a key version.

Disabling or destroying a key also disables or destroys each key version.

The following sections discuss the properties of a key.

Depending on the context, a key's properties are shown in a different format.

  * When using the Google Cloud CLI or the Cloud Key Management Service API, the property is shown as a string of capital letters, like `SOFTWARE`.
  * When using the Google Cloud console, the property is shown as a string with initial capitalization, like **Software**.



In the following sections, each format is shown where it is appropriate.

### Type

A key's type determines whether the key is used for symmetric or asymmetric cryptographic operations.

In symmetric encryption or signing, the same key is used to encrypt and decrypt data or to sign and verify a signature.

In asymmetric encryption or signing, the key consists of a public key and a private key. A private key with its corresponding public key is called a _key pair_.

  * The private key is sensitive data, and is required to decrypt data or for signing, depending on the key's configured purpose.
  * The public key is not considered sensitive, and is required to encrypt data or to verify a signature, depending on the key's configured purpose.



A key's type is one component of the key's purpose, and can't be changed after the key is created.

### Purpose

A key's purpose indicates what kind of cryptographic operations the key can be used for—for example, **Symmetric encrypt/decrypt** or **Asymmetric signing**. You choose the purpose when creating the key, and all versions of a key have the same purpose. A key's purpose can't be changed after the key is created. For more information about key purposes, see [Key purposes](https://docs.cloud.google.com/kms/docs/algorithms#key_purposes).

### Protection level

A key's protection level determines the key's storage environment at rest. The protection level is one of the following:

  * Software (`SOFTWARE`)
  * Multi-tenant HSM (`HSM`)
  * Single-tenant HSM (`HSM_SINGLE_TENANT`)
  * External (`EXTERNAL`)
  * External_VPC (`EXTERNAL_VPC`)



The protection level of a key can't be changed after the key is created.

### Primary version

Keys can have multiple key versions active and enabled at one time. Symmetric encryption keys have a primary key version, which is the key version used by default to encrypt data if you don't specify a key version.

Asymmetric keys don't have primary versions; you must specify the version when using the key.

For both symmetric and asymmetric keys, you can use any enabled key version to encrypt and decrypt data or to sign and validate signatures.

## Key versions

Each version of a key contains key material used for encryption or signing. Each version is assigned a version number, starting at `1`. Rotating a key creates a new key version. You can learn more about [rotating keys](https://docs.cloud.google.com/kms/docs/asymmetric-key-rotation).

To decrypt data or verify a signature, you must use the same key version that was used to encrypt or sign the data. To find a key version's resource ID, see Retrieving a key's resource ID.

You can disable or destroy individual key versions without affecting other versions. You can also disable or destroy all key versions for a given key.

You can't control access to key versions independently of the permissions in effect on the key. Granting access to a key grants access to all of that key's enabled versions.

For security reasons, no Google Cloud principal can view or export the raw cryptographic key material represented by a key version. Instead, Cloud KMS accesses the key material on your behalf.

The following sections discuss the properties of a key version.

### State

Each key version has a _state_ that tells you what its status is. Usually, a key's state will be one of the following:

  * Enabled
  * Disabled
  * Scheduled for destruction
  * Destroyed



A key version can only be used when it's enabled. Key versions in any state other than destroyed incur [costs](https://docs.cloud.google.com/kms/pricing). For more information about key version states and how versions can transition between them, see [Key version states](https://docs.cloud.google.com/kms/docs/key-states).

### Algorithm

A key version's [algorithm](https://docs.cloud.google.com/kms/docs/algorithms) determines how the key material is created and the parameters required for cryptographic operations. Symmetric and asymmetric keys use different algorithms. Encryption and signing use different algorithms.

If you don't specify an algorithm when creating a new key version, the algorithm of the previous version is used.

Regardless of the algorithm, Cloud KMS uses probabilistic encryption, so that the same plaintext encrypted with the same key version twice doesn't return the same ciphertext.

## Key rings

A key ring organizes keys in a specific Google Cloud location and lets you manage access control on groups of keys. A key ring's name does not need to be unique across a Google Cloud project, but must be unique within a given location. After creation, a key ring cannot be deleted. Key rings don't incur any costs. For a list of available locations, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations). 

## Key handles

A key handle is a Cloud KMS resource that helps you safely span the separation of duties to create new Cloud KMS keys for CMEK using Autokey. The creation of a key handle in a resource project triggers the creation of a Cloud KMS key in the key project for on-demand CMEK setup.

A key handle holds a reference to the Cloud KMS key that was created. You can retrieve the Cloud KMS resource ID of a key created by Autokey from the key handle. Infrastructure-as-code tooling like Terraform can work with key handles to manage CMEK-protected resources without elevated privileges.

Key handles are not visible in the Google Cloud console, but to use Autokey with the REST API or Terraform, you must work with key handles. For more information about using key handles, see [Create protected resources using Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey).

## Autokey configs

An Autokey config is a folder- or project-level resource that defines whether Autokey is enabled for resources within the folder. The Autokey config also defines which key project is used for keys created by Cloud KMS Autokey to protect resources in that folder. When you enable Autokey, you create or update an Autokey config on the resource folder or project. For more information about using Autokey configs, see [Enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey). 

## EKM connections

An EKM connection is a Cloud KMS resource that organizes VPC connections to your on-premises EKMs in a specific Google Cloud location. An EKM connection lets you connect to and use keys from an external key manager over a VPC network. After creation, an EKM connection cannot be deleted. EKM connections don't incur any costs. 

## Retrieving a resource's ID

Some API calls and gcloud CLI might require you to refer to a key ring, key, or key version by its resource ID, which is a string representing the fully-qualified [CryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion) name. Resource IDs are hierarchical, similar to a file system path. A key's resource ID also contains information about the key ring and location.

Object | Resource Id format  
---|---  
Key ring | `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING`  
Key | `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME`  
Key version | `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions/KEY_VERSION`  
Key handle | `projects/RESOURCE_PROJECT_ID/locations/LOCATION/keyHandles/KEY_HANDLE`  
EKM connection | `projects/PROJECT_ID/locations/LOCATION/ekmConnections/EKM_CONNECTION`  
Autokey config | `folders/FOLDER_NUMBER/autokeyConfig`  
`projects/PROJECT_ID/autokeyConfig`  
  
To learn more, see [Getting a Cloud KMS resource ID](https://docs.cloud.google.com/kms/docs/getting-resource-ids).

## Organizing resources

When you are planning how to organize the resources in your Google Cloud project, consider your business rules and how you plan to manage access. You can grant access to a single key, all keys on a key ring, or all keys in a project. The following organization patterns are common:

  * By environment, such as `prod`, `test`, and `develop`.
  * By work area, such as `payroll` or `insurance_claims`.
  * By data sensitivity or characteristics, such as `unrestricted`, `restricted`, `confidential`, `top-secret`.



## Resource life cycles

Key rings can't be deleted. You can [delete keys and key versions](https://docs.cloud.google.com/kms/docs/delete-kms-resources) in some circumstances, but names of deleted keys can't be reused. This ensures that the [resource identifier](https://docs.cloud.google.com/kms/docs/getting-resource-ids) of a key version is unique and always points to the original key material for that key version unless it has been destroyed. You can store an unlimited number of key rings, enabled or disabled keys, and enabled, disabled, or destroyed key versions. For more information, see [Pricing](https://docs.cloud.google.com/kms/pricing) and [Quotas](https://docs.cloud.google.com/kms/quotas). 

To learn how to destroy or restore a key version, see [Destroying and restoring key versions](https://docs.cloud.google.com/kms/docs/destroy-restore).

After you schedule the [shutdown of a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects), you can't access the project's resources, including Cloud KMS resources, unless you recover the project by following the steps to [restore a project](https://support.google.com/cloud/answer/6251787).

**Warning:** Once you schedule the shutdown of a project, there is a [limited period of time](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects) when you can recover the project. After the limited time, the project and all the resources under it are permanently destroyed and can't be recovered.

## What's next

  * [Create a key](https://docs.cloud.google.com/kms/docs/creating-keys).
  * Learn more about [permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles) in Cloud KMS.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
