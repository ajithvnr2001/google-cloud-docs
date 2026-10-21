---
url: https://docs.cloud.google.com/kms/docs/encrypting-application-data/
title: Encrypting application data \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:34.396543+00:00
---

# Encrypting application data  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/encrypting-application-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Encrypting application data Stay organized with collections  Save and categorize content based on your preferences. 

This page shows one way to use Cloud Key Management Service to directly encrypt application data on a client, before transmitting it across a network.

In this example, the encrypted data is transmitted to Google Cloud and is stored in a [Cloud Storage](https://docs.cloud.google.com/storage) bucket. Cloud Storage also supports automatic [server-side encryption using customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys), which automates this entire process. To protect application data before transmitting it to Google Cloud, we recommend that you use the [Tink library](https://github.com/google/tink).

The Tink library is a multi-language, cross-platform library that provides APIs for common cryptographic tasks. This can be used to encrypt data before it enters Google Cloud data stores, and supports Java, Python, C++, Go, Objective-C, and other languages, and both object storage and relational database services.

In this walkthrough, you encrypt a file using Cloud KMS before you upload it to a bucket. Next, you download and decrypt the same data so that you can read it on the client.

When you follow these instructions, your keys and all cryptographic operations remain in Google Cloud and you need to use Cloud KMS for decryption. [Raw symmetric encryption](https://docs.cloud.google.com/kms/docs/raw-encryption) lets you encrypt or decrypt data locally on-premises or move encrypted data between different libraries and service providers without having to decrypt it first. 

**Note:** Cloud KMS stores keys that are used to encrypt and decrypt secrets, but does not store the encrypted sensitive data directly. To store sensitive data in Google Cloud, we recommend [Secret Manager](https://docs.cloud.google.com/secret-manager).

## Before you begin

Within your Google Cloud organization, you need permission to create new projects, and to enable billing, create users, and manage permissions within these projects. The [`roles/resourcemanager.organizationAdmin`](https://docs.cloud.google.com/resource-manager/docs/access-control-org#permissions_and_roles) role grants this permission.

## Setup

We recommend using two projects and two users to ensure [separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties). If you follow the steps in this guide, users and services that **manage** encryption keys are distinct from users and services that **use** them. One project contains and manages the keys, and the other project stores the encrypted data in a Cloud Storage bucket, and decrypts it as needed.

### Create projects

You create projects in the Google Cloud console. For step-by-step instructions, see the [Identity and Access Management quickstart](https://docs.cloud.google.com/iam/docs/grant-role-console#create-project).

Create the following projects within your organization:

  1. [Create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to contain the Cloud Storage bucket used to store the secrets. The secrets will be stored as objects in the bucket. This project is called STORAGE_PROJECT_ID.

  2. Create a second Google Cloud project to manage the Cloud KMS keys used to encrypt and decrypt the secret. This project is called KEY_PROJECT_ID.

  3. **For each project** , enable the Cloud KMS API and enable billing, by following the steps in the [Before you begin](https://docs.cloud.google.com/kms/docs/create-encryption-keys#before-you-begin) section of the Cloud KMS Quickstart.




### Create users

You create users and grant them roles in the Google Cloud console. For step-by-step instructions, see the [Identity and Access Management quickstart](https://docs.cloud.google.com/iam/docs/grant-role-console#grant_an_iam_role).

This procedure creates two users. The key administrator manages the encryption keys, and the key user can encrypt and decrypt data using the keys.

Perform this procedure in the KEY_PROJECT_ID project.

  1. Create the key administrator account.

  2. Grant the [`roles/cloudkms.admin`](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) Identity and Access Management role to the key administrator. This role lets the key administrator create and manage keys.

  3. Create the key user account.

  4. Grant the [`roles/cloudkms.cryptoKeyEncrypterDecrypter`](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) IAM role to the key user. This role lets the key user encrypt and decrypt data.

**Note:** If a user or application only needs encryption permissions or only needs decryption permissions, you can use the [`roles/cloudkms.cryptoKeyEncrypter`](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) and [`roles/cloudkms.cryptoKeyDecrypter`](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) IAM roles. This helps you follow the principle of least privilege.



### Create a storage bucket

Perform this procedure in the `STORAGE_PROJECT_ID` project.

  1. [Create a storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) called `STORAGE_BUCKET`.
  2. [Grant](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant_access) the [`roles/storage.objectAdmin`](https://docs.cloud.google.com/storage/docs/access-control/iam#roles) role on the STORAGE_BUCKET storage bucket to the key user account.



## Create an encryption key

Perform this procedure as the key administrator user in the KEY_PROJECT_ID project.

  1. Create a key ring. The name of a key ring must be unique within the project. A key ring can't be renamed or deleted. Use the Google Cloud CLI to [create a key ring](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keyrings).
         
         gcloud kms keyrings create KEY_RING \
           --location LOCATION
         

Replace the following:

     * `KEY_RING`: the name to use for the storage key ring—for example, `storage`.
     * `LOCATION`: the location where you want to create the key ring. This should be geographically near the location where you want to create the Cloud Storage bucket.
  2. Create an encryption key in the key ring. The name of the key must be unique within the key ring. Keys can't be renamed or deleted, but their key versions can be destroyed. Use the Google Cloud CLI to [create the key](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys). An initial key version is created automatically and becomes the primary version.
         
         gcloud kms keys create KEY_NAME \
           --location LOCATION \
           --keyring KEY_RING \
           --purpose encryption
         

Replace the following:

     * `LOCATION`: the location where you created the key ring.
     * `KEY_NAME`: the name to use for the storage key—for example, `storage`.
     * `KEY_RING`: the name you used for the storage key ring—for example, `storage`.

Note: To use [raw symmetric encryption](https://docs.cloud.google.com/kms/docs/raw-encryption) keys, set the purpose field to [`raw-encryption`](https://docs.cloud.google.com/kms/docs/algorithms#key_purposes). 




You can learn more about [Creating key rings and keys](https://docs.cloud.google.com/kms/docs/creating-keys).

## Encrypt the file that contains the secret

Perform this procedure as the key user account, working in both projects.

  1. On your local machine, save the secret.
         
         echo "SECRET_TEXT" > PATH_TO_SECRET
         

Replace the following:

     * `SECRET_TEXT`: the secret that you want to protect, in plain text—for example, `this is a secret`.
     * `PATH_TO_SECRET`: the path where you want to create the secret—for example, `secret.txt`.
  2. Encrypt the secret using Cloud KMS and the encryption key.
         
         gcloud kms encrypt \
           --location LOCATION \
           --keyring KEY_RING \
           --key KEY_NAME \
           --plaintext-file PATH_TO_SECRET \
           --ciphertext-file PATH_TO_ENCRYPTED_SECRET
         

Replace the following:

     * `LOCATION`: the location where you created the key ring.
     * `KEY_RING`: the name of the key ring.
     * `KEY_NAME`: the name of the encryption key.
     * `PATH_TO_SECRET`: the path where you created the secret.
     * `PATH_TO_ENCRYPTED_SECRET`: the path where you want to save the encrypted secret—for example, `secret.txt.encrypted`.

You can learn more about encrypting data by following the [encrypt data quickstart](https://docs.cloud.google.com/kms/docs/create-encryption-keys#encrypt_data).

Use [`raw-encrypt`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawEncrypt) instead for [raw symmetric encryption](https://docs.cloud.google.com/kms/docs/raw-encryption). 

  3. Upload the encrypted secret file to the storage bucket. You can use the following gcloud CLI command:
         
         gcloud storage cp PATH_TO_ENCRYPTED_SECRET gs://STORAGE_BUCKET
         

You can learn more about [uploading](https://docs.cloud.google.com/storage/docs/uploading-objects) objects to a storage bucket.

  4. Optional: Delete the plaintext secret file (`PATH_TO_SECRET`) from the local machine. This is a good practice for files containing unencrypted sensitive data.




The `STORAGE_BUCKET` storage bucket now contains the encrypted secret file, which is encrypted using the `KEY_NAME` encryption key.

## Decrypt the file that contains the secret

Perform these steps as the key user account, working in both projects.

  1. Download the encrypted secret file from the storage bucket. You can use the following gcloud CLI command:
         
         gcloud storage cp gs://STORAGE_BUCKET/PATH_TO_ENCRYPTED_SECRET .
         

You can learn more about [downloading](https://docs.cloud.google.com/storage/docs/downloading-objects) objects from a storage bucket.

  2. Decrypt the file using the same key that you used to encrypt it.
         
         gcloud kms decrypt --location LOCATION \
           --keyring KEY_RING \
           --key KEY_NAME \
           --ciphertext-file PATH_TO_ENCRYPTED_SECRET \
           --plaintext-file PATH_TO_DECRYPTED_SECRET
         

Replace the following:

     * `LOCATION`: the location where you created the key ring.
     * `KEY_RING`: the name of the key ring.
     * `KEY_NAME`: the name of the encryption key.
     * `PATH_TO_ENCRYPTED_SECRET`: the path to the downloaded encrypted secret—for example, `secret.txt.encrypted`.
     * `PATH_TO_DECRYPTED_SECRET`: the path where you want to save the decrypted secret—for example, `secret_decrypted.txt`.

You can learn more about decrypting data by following the [encrypt data quickstart](https://docs.cloud.google.com/kms/docs/create-encryption-keys#encrypt_data).

Use [`raw-decrypt`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawDecrypt) instead for [raw symmetric encryption](https://docs.cloud.google.com/kms/docs/raw-encryption). 

You can now read the decrypted plaintext of the secret using `cat` or a text editor. The contents are identical to the original contents of `PATH_TO_SECRET`.

  3. Optional: Delete the `PATH_TO_ENCRYPTED_SECRET` and `PATH_TO_DECRYPTED_SECRET` files from the local machine.




## Cleaning up

To clean up, delete all the files you created on the local machine, then delete the `KEY_PROJECT_ID` and `STORAGE_PROJECT_ID` projects.

## What's next

  * Read more about [secret management](https://docs.cloud.google.com/solutions/secret-management).
  * Learn about [separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties).
  * Learn about [granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to resources.
  * Learn about [creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
